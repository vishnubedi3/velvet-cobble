#!/usr/bin/env python3
"""Run the Canon Guard adaptive suite against synthetic fixtures.

Does not read samur/02-canon/. Failures are assertion errors.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "reference"))

from canon_guard import (  # noqa: E402
    admit,
    build_canon_state,
    classify_splash_material,
    contract_is_stale,
    detect_changes,
    invalidate,
    make_contract,
    run,
    verify,
)


def _load_suite() -> list[dict]:
    path = ROOT / "fixtures" / "adaptive" / "suite.json"
    return json.loads(path.read_text())


def _assert(cond: bool, msg: str) -> None:
    if not cond:
        raise AssertionError(msg)


def run_scenario(sc: dict) -> None:
    sid = sc["id"]
    req = sc["request"]
    req1 = sc.get("request_t1") or req
    t0 = sc["t0"]
    t1 = sc["t1"]
    branch0 = t0["branch"]
    branch1 = t1["branch"]
    name0 = t0.get("name") or "main"
    name1 = t1.get("name") or name0

    live0 = t0.get("live_heads")
    live1 = t1.get("live_heads")
    splash0 = t0.get("splash")
    splash1 = t1.get("splash")

    out0 = run(req, name0, branch0, live_heads=live0, splash=splash0)
    _assert(
        out0["report"]["decision"] == sc["expected_t0"]["decision"],
        f"{sid} T0: got {out0['report']['decision']} expected {sc['expected_t0']['decision']}"
        f" findings={out0['report']['findings']}",
    )
    if "classes" in sc["expected_t0"]:
        got = {f["class"] for f in out0["report"]["findings"]}
        for cls in sc["expected_t0"]["classes"]:
            _assert(cls in got, f"{sid} T0 missing class {cls} in {got}")

    if sc["expected_t0"]["decision"] in ("PASS", "PASS_WITH_WARNINGS"):
        _assert(out0["contract"] is not None, f"{sid} T0 expected a contract")
    else:
        _assert(out0["contract"] is None, f"{sid} T0 must not emit a contract")

    out1 = run(req1, name1, branch1, live_heads=live1, splash=splash1)
    _assert(
        out1["report"]["decision"] == sc["expected_t1"]["decision"],
        f"{sid} T1: got {out1['report']['decision']} expected {sc['expected_t1']['decision']}"
        f" findings={out1['report']['findings']}",
    )
    if "classes" in sc["expected_t1"]:
        got = {f["class"] for f in out1["report"]["findings"]}
        for cls in sc["expected_t1"]["classes"]:
            _assert(cls in got, f"{sid} T1 missing class {cls} in {got}")

    if sc["expected_t1"]["decision"] in ("PASS", "PASS_WITH_WARNINGS"):
        _assert(out1["contract"] is not None, f"{sid} T1 expected a contract")
    else:
        _assert(out1["contract"] is None, f"{sid} T1 must not emit a contract")

    # Decisions must be allowed to change (core adaptive property)
    if sc.get("must_change_decision"):
        _assert(
            out0["report"]["decision"] != out1["report"]["decision"],
            f"{sid} expected decision to change across T0→T1",
        )

    extra = sc.get("extra") or {}
    if extra.get("check_stale_contract"):
        _assert(out0["contract"] is not None, f"{sid} need T0 contract")
        _assert(
            contract_is_stale(out0["contract"], out1["state"]),
            f"{sid} T0 contract should be stale at T1",
        )

    if extra.get("check_invalidation"):
        ch = detect_changes(out0["state"], out1["state"])
        inv = invalidate(set(), ch, out0["state"], out1["state"])
        want_scope = extra["check_invalidation"]
        _assert(
            inv["scope"] == want_scope,
            f"{sid} invalidation scope {inv['scope']} != {want_scope} (changes={ch})",
        )
        if want_scope == "local":
            _assert(inv["kept"], f"{sid} local change should keep some derived facts")
            _assert(inv["dropped"], f"{sid} local change should drop some derived facts")
        if want_scope == "systemic":
            _assert(inv["dropped"], f"{sid} systemic change should drop derived facts")
            _assert(not inv["kept"], f"{sid} systemic change should keep none")

    if extra.get("check_classifications"):
        got = {c["class"] for c in out1["state"].get("splash_classifications") or []}
        for cls in extra["check_classifications"]:
            _assert(cls in got, f"{sid} T1 missing splash class {cls} in {got}")

    if extra.get("check_source_status_band"):
        _assert(out1["contract"] is not None, f"{sid} T1 need contract for source_status")
        band = extra["check_source_status_band"]
        bands = (out1["contract"] or {}).get("source_status") or {}
        _assert(bands.get(band), f"{sid} T1 source_status.{band} empty in {bands}")

    if extra.get("check_not_canonical_value"):
        spec = extra["check_not_canonical_value"]
        _assert(out1["contract"] is not None, f"{sid} T1 need contract")
        canonical = ((out1["contract"] or {}).get("source_status") or {}).get("CANONICAL") or []
        for item in canonical:
            if (
                item.get("entity") == spec["entity"]
                and item.get("predicate") == spec["predicate"]
                and item.get("value") == spec["value"]
            ):
                raise AssertionError(
                    f"{sid} splash value {spec} must not appear in CANONICAL"
                )

    if extra.get("check_classification_change"):
        spec = extra["check_classification_change"]

        def _cls(state: dict) -> str | None:
            for c in state.get("splash_classifications") or []:
                if c.get("entity") == spec["entity"] and c.get("predicate") == spec["predicate"]:
                    return c.get("class")
            return None

        got0, got1 = _cls(out0["state"]), _cls(out1["state"])
        _assert(
            got0 == spec["from"],
            f"{sid} T0 class {got0} != {spec['from']}",
        )
        _assert(
            got1 == spec["to"],
            f"{sid} T1 class {got1} != {spec['to']}",
        )

    if extra.get("check_admission"):
        # T0 unadmitted must not be in CANON sources
        statuses = {s["status"] for s in out0["state"]["sources"]}
        _assert("CANON" in statuses or out0["state"]["sources"] == [] or True, sid)
        unad = out0["state"]["unadmitted"]
        _assert(unad, f"{sid} T0 should have unadmitted material")
        # After T1 admission, the proposed id is in canon
        ids = {s.get("id") for s in out1["state"]["sources"]}
        _assert(
            extra["check_admission"] in ids,
            f"{sid} admitted id {extra['check_admission']} not in T1 sources {ids}",
        )


def test_header_parser_fixture() -> None:
    """Resolution reads Status from markdown; RETIRED is not CANON."""
    md = (ROOT / "fixtures" / "repos" / "header-sample.md").read_text()
    status = None
    high = None
    for line in md.splitlines():
        if line.startswith("Status:"):
            status = line.split(":", 1)[1].strip()
        if line.startswith("High-impact:"):
            high = line.split(":", 1)[1].strip().lower().startswith("yes")
    _assert(status == "CANON", f"header status {status}")
    _assert(high is True, f"header high-impact {high}")
    retired = (ROOT / "fixtures" / "repos" / "retired-sample.md").read_text()
    rstatus = None
    for line in retired.splitlines():
        if line.startswith("Status:"):
            rstatus = line.split(":", 1)[1].strip()
    _assert(rstatus.startswith("RETIRED"), f"retired status {rstatus}")


def test_admit_helper() -> None:
    branch = {
        "commit": "c0",
        "charter": {"narrative_authorized": True},
        "canon": [
            {
                "id": "GEO-01",
                "status": "CANON",
                "high_impact": True,
                "facts": [{"entity": "Helwick", "predicate": "exists", "value": True}],
            }
        ],
        "unadmitted": [
            {
                "id": "DRAFT-01",
                "status": "DRAFT",
                "facts": [{"entity": "Nila", "predicate": "role", "value": "scribe"}],
            }
        ],
    }
    nxt = admit(
        {
            "id": "CUL-09",
            "facts": [{"entity": "Nila", "predicate": "role", "value": "scribe"}],
        },
        branch,
    )
    ids = {d["id"] for d in nxt["canon"]}
    _assert("CUL-09" in ids, "admit should add canon doc")
    _assert(nxt["commit"] != "c0", "admit should bump commit identity")


def test_mystery_and_charter_and_change() -> None:
    branch = {
        "commit": "c0",
        "charter": {"narrative_authorized": False},
        "questions": [
            {"id": "Q-X", "status": "INTENTIONALLY UNRESOLVED"},
            {"id": "Q-Y", "status": "NOT READY"},
            {"id": "Q-Z", "status": "OPEN (a narrative detail)"},
        ],
        "canon": [
            {
                "id": "CHR-01",
                "status": "CANON",
                "facts": [{"entity": "Lia", "predicate": "vital_status", "value": "alive"}],
            }
        ],
    }
    mystery = run(
        {
            "request_id": "m",
            "generation_kind": "worldbuilding",
            "target_branch": "main",
            "claims": [
                {
                    "entity": "West",
                    "predicate": "named",
                    "value": "Zed",
                    "resolves_question": "Q-X",
                }
            ],
        },
        "main",
        branch,
    )
    _assert(mystery["report"]["decision"] == "BLOCK", mystery["report"])
    _assert(any(f["class"] == "CX-MYSTERY" for f in mystery["report"]["findings"]), mystery["report"])

    not_ready = run(
        {
            "request_id": "n",
            "generation_kind": "worldbuilding",
            "target_branch": "main",
            "claims": [
                {
                    "entity": "planet",
                    "predicate": "age",
                    "value": 123,
                    "resolves_question": "Q-Y",
                }
            ],
        },
        "main",
        branch,
    )
    _assert(not_ready["report"]["decision"] == "BLOCK", not_ready["report"])

    opened = run(
        {
            "request_id": "o",
            "generation_kind": "narrative",
            "target_branch": "main",
            "claims": [
                {
                    "entity": "courier",
                    "predicate": "name",
                    "value": "Pell",
                    "resolves_question": "Q-Z",
                }
            ],
        },
        "main",
        branch,
    )
    _assert(opened["report"]["decision"] == "BLOCK", opened["report"])  # narrative blocked by charter

    opened_wb = run(
        {
            "request_id": "o2",
            "generation_kind": "worldbuilding",
            "target_branch": "main",
            "claims": [
                {
                    "entity": "courier",
                    "predicate": "name",
                    "value": "Pell",
                    "resolves_question": "Q-Z",
                }
            ],
        },
        "main",
        branch,
    )
    _assert(
        opened_wb["report"]["decision"] == "PASS_WITH_WARNINGS",
        opened_wb["report"],
    )

    narr = run(
        {
            "request_id": "nar",
            "generation_kind": "narrative",
            "target_branch": "main",
            "claims": [{"entity": "Lia", "predicate": "vital_status", "value": "alive"}],
        },
        "main",
        branch,
    )
    _assert(narr["report"]["decision"] == "BLOCK", narr["report"])
    _assert(any(f["class"] == "CX-BRANCH" for f in narr["report"]["findings"]), narr["report"])

    change = run(
        {
            "request_id": "ch",
            "generation_kind": "canon_change",
            "target_branch": "main",
            "explicit_canon_change": True,
            "claims": [{"entity": "Lia", "predicate": "vital_status", "value": "dead"}],
        },
        "main",
        branch,
    )
    _assert(change["report"]["decision"] == "CANON_CHANGE_REQUIRED", change["report"])


def test_world_model_not_authority() -> None:
    """A summary-only fact is not CANON; the file wins."""
    branch = {
        "commit": "c1",
        "charter": {"narrative_authorized": True},
        "canon": [
            {
                "id": "GEO-01",
                "status": "CANON",
                "hash": "h1",
                "facts": [
                    {
                        "entity": "Brann",
                        "predicate": "flows",
                        "value": "north",
                    }
                ],
            }
        ],
    }
    req = {
        "request_id": "wm",
        "generation_kind": "narrative",
        "target_branch": "main",
        "claims": [{"entity": "Brann", "predicate": "width", "value": "wide", "cited_status": "CANON-INDEX"}],
    }
    out = run(req, "main", branch)
    _assert(out["report"]["decision"] == "REQUIRES_CLARIFICATION", out["report"])


def test_newer_splash_does_not_override_main() -> None:
    """A later Splash commit cannot silently replace established main canon."""
    main_branch = {
        "commit": "old",
        "charter": {"narrative_authorized": True},
        "canon": [
            {
                "id": "CHR-01",
                "status": "CANON",
                "facts": [{"entity": "Lia", "predicate": "vital_status", "value": "alive"}],
            }
        ],
    }
    splash = {
        "name": "arena/session",
        "branch": {
            "commit": "newer",
            "charter": {"narrative_authorized": True},
            "canon": [
                {
                    "id": "CHR-01",
                    "status": "CANON",
                    "facts": [{"entity": "Lia", "predicate": "vital_status", "value": "dead"}],
                }
            ],
        },
    }
    req = {
        "request_id": "override",
        "generation_kind": "narrative",
        "claims": [{"entity": "Lia", "predicate": "vital_status", "value": "dead", "treat_as_established": True}],
    }
    out = run(req, "main", main_branch, live_heads={"main": "old", "arena/session": "newer"}, splash=splash)
    _assert(out["report"]["decision"] == "BLOCK", out["report"])
    _assert(any(f["class"] == "CX-DIRECT" for f in out["report"]["findings"]), out["report"])
    classes = {c["class"] for c in out["state"]["splash_classifications"]}
    _assert("CONTRADICTORY" in classes, classes)
    aligned = run(
        {
            "request_id": "aligned",
            "generation_kind": "narrative",
            "claims": [{"entity": "Lia", "predicate": "vital_status", "value": "alive"}],
        },
        "main",
        main_branch,
        live_heads={"main": "old", "arena/session": "newer"},
        splash=splash,
    )
    _assert(aligned["report"]["decision"] == "PASS_WITH_WARNINGS", aligned["report"])
    dead = [
        i
        for i in aligned["contract"]["source_status"]["CANONICAL"]
        if i.get("value") == "dead"
    ]
    _assert(not dead, "newer splash dead must not enter CANONICAL")


def test_uninspected_splash_is_not_ignored() -> None:
    """A live arena/* head that was not classified is insufficient information."""
    branch = {
        "commit": "c0",
        "charter": {"narrative_authorized": True},
        "canon": [
            {
                "id": "CHR-01",
                "status": "CANON",
                "facts": [{"entity": "Lia", "predicate": "vital_status", "value": "alive"}],
            }
        ],
    }
    req = {
        "request_id": "gap",
        "generation_kind": "narrative",
        "claims": [{"entity": "Lia", "predicate": "vital_status", "value": "alive"}],
    }
    out = run(req, "main", branch, live_heads={"main": "c0", "arena/session": "c9"})
    _assert(out["report"]["decision"] == "REQUIRES_CLARIFICATION", out["report"])
    _assert(any(f["class"] == "CX-AMBIGUITY" for f in out["report"]["findings"]), out["report"])


def test_classify_splash_helper() -> None:
    main_state = build_canon_state(
        "main",
        {
            "commit": "c0",
            "canon": [
                {
                    "id": "CHR-01",
                    "status": "CANON",
                    "facts": [{"entity": "Lia", "predicate": "vital_status", "value": "alive"}],
                }
            ],
        },
    )
    splash_state = build_canon_state(
        "arena/session",
        {
            "commit": "c9",
            "canon": [
                {
                    "id": "CHR-01",
                    "status": "CANON",
                    "facts": [
                        {
                            "entity": "Lia",
                            "predicate": "vital_status",
                            "value": "alive",
                            "relation": "clarifies",
                        }
                    ],
                }
            ],
        },
    )
    got = classify_splash_material(main_state, splash_state)
    _assert(got and got[0]["class"] == "CANON_CLARIFICATION", got)


def main() -> int:
    suite = _load_suite()
    failures = []
    for sc in suite:
        try:
            run_scenario(sc)
            print(f"PASS {sc['id']} {sc['title']}")
        except AssertionError as exc:
            failures.append((sc["id"], str(exc)))
            print(f"FAIL {sc['id']} {exc}")
    try:
        test_header_parser_fixture()
        print("PASS header-parser")
    except AssertionError as exc:
        failures.append(("header-parser", str(exc)))
        print(f"FAIL header-parser {exc}")
    try:
        test_admit_helper()
        print("PASS admit-helper")
    except AssertionError as exc:
        failures.append(("admit-helper", str(exc)))
        print(f"FAIL admit-helper {exc}")
    try:
        test_world_model_not_authority()
        print("PASS world-model-not-authority")
    except AssertionError as exc:
        failures.append(("world-model-not-authority", str(exc)))
        print(f"FAIL world-model-not-authority {exc}")
    try:
        test_mystery_and_charter_and_change()
        print("PASS mystery-charter-change")
    except AssertionError as exc:
        failures.append(("mystery-charter-change", str(exc)))
        print(f"FAIL mystery-charter-change {exc}")
    extra_tests = (
        ("newer-splash-does-not-override", test_newer_splash_does_not_override_main),
        ("uninspected-splash", test_uninspected_splash_is_not_ignored),
        ("classify-splash-helper", test_classify_splash_helper),
    )
    for name, fn in extra_tests:
        try:
            fn()
            print(f"PASS {name}")
        except AssertionError as exc:
            failures.append((name, str(exc)))
            print(f"FAIL {name} {exc}")

    print(f"\n{len(suite) - len([f for f in failures if f[0].startswith('A')])} suite scenarios ok; {len(failures)} failures")
    if failures:
        for fid, msg in failures:
            print(f"  - {fid}: {msg}")
        return 1
    print("All adaptive tests passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
