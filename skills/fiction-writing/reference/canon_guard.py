"""Deterministic reference core for the Pre-Generation Canon Guard.

Operates on structured Canon States (already resolved). It does not read
the project's fictional sources and must not be fed them by tests.

Host agents still re-resolve live branches per CANON_RESOLUTION.md; this
module exists so the adaptive property can be tested without a model.
"""

from __future__ import annotations

import copy
import hashlib
import json
from typing import Any

DECISIONS = (
    "PASS",
    "PASS_WITH_WARNINGS",
    "REQUIRES_CLARIFICATION",
    "BLOCK",
    "CANON_CHANGE_REQUIRED",
)

CHECKS = (
    "branch",
    "authority",
    "direct",
    "indirect",
    "temporal",
    "knowledge",
    "causal",
    "mystery",
    "not_ready",
    "high_impact_smuggle",
    "admission",
    "unresolved_register",
    "ambiguity",
    "divergence",
    "charter",
    "splash",
    "working_direction",
    "contamination",
    "bypass",
    "continuity",
    "stale",
    "retired",
)

SEVERITY_TO_BAND = {
    "info": "informational",
    "warn": "warning",
    "stop": "significant",
    "block": "blocking",
}

CONSTRAINT_BAND_KEYS = (
    "HARD_CONSTRAINTS",
    "SOFT_CONTEXT",
    "CURRENT_AUTHORIAL_DIRECTION",
    "PROVISIONAL_MATERIAL",
    "FORBIDDEN_ASSUMPTIONS",
)

LOCK_COMPARE_KEYS = (
    "canon_state_id",
    "must_remain_unchanged",
    "source_hashes",
    "source_status",
    "constraint_bands",
    "forbidden_assumptions",
    "authorized_changes",
)

SPLASH_CLASSES = (
    "CONFIRMS_CANON",
    "CLARIFIES_CANON",
    "EXTENDS_CANON",
    "DEVELOPS_INTENDED_CANON",
    "PROPOSED_CANON",
    "DEVELOPMENTAL",
    "EXPLORATORY",
    "CONTRADICTS_CANON",
    "RETCON_PROPOSAL",
    "ABANDONED_OR_SUPERSEDED",
    "UNRESOLVED",
)

CLASS_ALIASES = {
    "CONFIRMED_CANON": "CONFIRMS_CANON",
    "CANON_CLARIFICATION": "CLARIFIES_CANON",
    "CANON_EXTENSION": "EXTENDS_CANON",
    "AUTHORIAL_INTENT": "DEVELOPS_INTENDED_CANON",
    "CONTRADICTORY": "CONTRADICTS_CANON",
}

ESTABLISHED_SPLASH = frozenset({"CONFIRMS_CANON", "CLARIFIES_CANON"})

NON_ESTABLISHED_SPLASH = frozenset(
    {
        "EXTENDS_CANON",
        "DEVELOPS_INTENDED_CANON",
        "PROPOSED_CANON",
        "DEVELOPMENTAL",
        "EXPLORATORY",
    }
)

PROVISIONAL_SPLASH = frozenset({"PROPOSED_CANON", "DEVELOPMENTAL", "EXPLORATORY"})

STRONG_DIRECTION = frozenset({"DEVELOPS_INTENDED_CANON", "EXTENDS_CANON"})

RELATION_TO_CLASS = {
    "clarifies": "CLARIFIES_CANON",
    "clarification": "CLARIFIES_CANON",
    "extends": "EXTENDS_CANON",
    "extension": "EXTENDS_CANON",
    "intent": "DEVELOPS_INTENDED_CANON",
    "authorial_intent": "DEVELOPS_INTENDED_CANON",
    "intended": "DEVELOPS_INTENDED_CANON",
    "develops_intended": "DEVELOPS_INTENDED_CANON",
    "proposed": "PROPOSED_CANON",
    "proposed_canon": "PROPOSED_CANON",
    "developmental": "DEVELOPMENTAL",
    "draft": "DEVELOPMENTAL",
    "development": "DEVELOPMENTAL",
    "exploratory": "EXPLORATORY",
    "experiment": "EXPLORATORY",
    "alternate": "EXPLORATORY",
    "contradicts": "CONTRADICTS_CANON",
    "contradiction": "CONTRADICTS_CANON",
    "confirmed": "CONFIRMS_CANON",
    "confirms": "CONFIRMS_CANON",
    "restates": "CONFIRMS_CANON",
    "retcon": "RETCON_PROPOSAL",
    "retcon_proposal": "RETCON_PROPOSAL",
    "abandoned": "ABANDONED_OR_SUPERSEDED",
    "superseded": "ABANDONED_OR_SUPERSEDED",
    "unresolved": "UNRESOLVED",
}

CONTRACT_BANDS = (
    "ESTABLISHED_CANON",
    "CURRENT_WORKING_DEVELOPMENT",
    "CANON_CLARIFICATIONS",
    "AUTHORIAL_DIRECTION",
    "PROVISIONAL",
    "CONFLICTS",
    "OPEN_QUESTIONS",
)


def _norm_class(cls: str | None) -> str | None:
    if not cls:
        return cls
    return CLASS_ALIASES.get(cls, cls)


def _hash_obj(obj: Any) -> str:
    blob = json.dumps(obj, sort_keys=True, default=str).encode("utf-8")
    return hashlib.sha256(blob).hexdigest()[:16]


def _incompatible(a: Any, b: Any) -> bool:
    return a != b


def _time_overlaps(fact: dict, ordinal: float | None) -> bool:
    if ordinal is None:
        return True
    start = fact.get("story_time_start")
    end = fact.get("story_time_end")
    if start is not None and ordinal < start:
        return False
    if end is not None and ordinal > end:
        return False
    return True


def _continues_splash(request: dict, splash_state: dict | None) -> bool:
    if request.get("continue_splash_storyline"):
        return True
    target = request.get("target_branch") or ""
    if splash_state is not None and str(target).startswith("arena/"):
        return True
    return False


def _treats_as_established(request: dict, claim: dict) -> bool:
    if request.get("uses_unadmitted_as_canon"):
        return True
    if claim.get("treat_as_established"):
        return True
    return False


def _splash_heads(live_heads: dict | None) -> list[str]:
    if not live_heads:
        return []
    return [n for n in live_heads if str(n).startswith("arena/")]


def _hinted_class(fact: dict) -> str | None:
    relation = (fact.get("relation") or "").strip().lower()
    if not relation:
        return None
    return RELATION_TO_CLASS.get(relation)


def _splash_fact_records(splash_state: dict) -> list[dict]:
    records = []
    splash_name = (splash_state.get("branch_context") or {}).get("applicable_branch") or "splash"
    for fact in splash_state.get("facts") or []:
        rec = dict(fact)
        rec["_origin"] = "canon"
        records.append(rec)
    for u in splash_state.get("unadmitted") or []:
        digest = _hash_obj(u)
        for i, fact in enumerate(u.get("facts") or []):
            rec = dict(fact)
            rec.setdefault(
                "source",
                {
                    "branch": splash_name,
                    "path": f"unadmitted/{u.get('id')}",
                    "location": f"fact[{i}]",
                    "hash": digest,
                },
            )
            rec["_origin"] = "unadmitted"
            if not rec.get("relation"):
                rec["relation"] = "developmental"
            records.append(rec)
    return records


def classify_splash_material(main_state: dict, splash_state: dict) -> list[dict]:
    """Classify each Arena statement against current main. Re-run when either side moves.

    Branch membership never determines the class. Compatible restatement on main is
    CONFIRMS_CANON; a newer Arena value does not override main.
    """
    out: list[dict] = []
    for fact in _splash_fact_records(splash_state):
        entity, predicate, value = fact.get("entity"), fact.get("predicate"), fact.get("value")
        if entity is None or predicate is None:
            continue
        hinted = _norm_class(_hinted_class(fact))
        ordinal = fact.get("story_time_start")
        if ordinal is None:
            ordinal = fact.get("story_time_ordinal")
        matches = list(_matching_facts(main_state, entity, predicate, ordinal))
        origin = fact.get("_origin") or "canon"
        if hinted == "ABANDONED_OR_SUPERSEDED":
            cls = "ABANDONED_OR_SUPERSEDED"
        elif matches:
            incompatible = any(
                (m.get("polarity") or "asserted") == "asserted"
                and _incompatible(m.get("value"), value)
                for m in matches
            )
            if incompatible:
                if hinted == "EXPLORATORY":
                    cls = "EXPLORATORY"
                elif hinted == "RETCON_PROPOSAL":
                    cls = "RETCON_PROPOSAL"
                else:
                    cls = "CONTRADICTS_CANON"
            elif hinted == "CLARIFIES_CANON":
                cls = "CLARIFIES_CANON"
            else:
                cls = "CONFIRMS_CANON"
        else:
            if hinted:
                cls = hinted
            elif origin == "unadmitted":
                cls = "DEVELOPMENTAL"
            else:
                cls = "UNRESOLVED"
        item = {
            "entity": entity,
            "predicate": predicate,
            "value": value,
            "class": cls,
            "origin": origin,
            "source": fact.get("source"),
        }
        if fact.get("relation"):
            item["relation"] = fact.get("relation")
        out.append(item)
    return out


def build_working_canon_context(state: dict) -> dict:
    """Established canon + classified Arena. Not a merge. Not a second canon."""
    classifications = list(state.get("splash_classifications") or [])
    return {
        "established_canon": [
            {
                "entity": f.get("entity"),
                "predicate": f.get("predicate"),
                "value": f.get("value"),
                "source": f.get("source"),
            }
            for f in state.get("facts") or []
        ],
        "arena_developments": classifications,
        "authorial_direction": [
            c for c in classifications if c.get("class") in STRONG_DIRECTION
        ],
        "provisional": [
            c for c in classifications if c.get("class") in PROVISIONAL_SPLASH
        ],
        "conflicts": [
            c
            for c in classifications
            if c.get("class") in ("CONTRADICTS_CANON", "RETCON_PROPOSAL")
        ],
        "open_questions": [
            c for c in classifications if c.get("class") == "UNRESOLVED"
        ],
        "abandoned": [
            c for c in classifications if c.get("class") == "ABANDONED_OR_SUPERSEDED"
        ],
    }


def attach_splash(state: dict, splash_name: str, splash_branch: dict) -> dict:
    """Annotate a main Canon State with classified Splash context. Does not merge facts."""
    splash_state = build_canon_state(splash_name, splash_branch)
    classifications = classify_splash_material(state, splash_state)
    state["splash_classifications"] = classifications
    state["branch_context"]["splash"] = {
        "name": splash_name,
        "commit": splash_state["branch_context"]["commit"],
    }
    for s in splash_state.get("sources") or []:
        state["sources"].append(
            {
                "id": s.get("id"),
                "path": f"splash:{s['path']}",
                "hash": s["hash"],
                "status": "SPLASH",
                "high_impact": False,
                "depends_on": [],
                "dependents": [],
            }
        )
    for u in splash_state.get("unadmitted") or []:
        state["sources"].append(
            {
                "id": u.get("id"),
                "path": f"splash:unadmitted/{u.get('id')}",
                "hash": _hash_obj(u),
                "status": "SPLASH",
                "high_impact": False,
                "depends_on": [],
                "dependents": [],
            }
        )
    state["canon_state_id"] = (
        f"{state['canon_state_id']}+splash@{splash_state['branch_context']['commit']}"
    )
    state["working_canon_context"] = build_working_canon_context(state)
    return splash_state


def build_canon_state(branch_name: str, branch: dict, *, state_id: str | None = None) -> dict:
    """Turn a fixture branch snapshot into a CanonState."""
    sources = []
    facts = []
    for doc in branch.get("canon", []):
        body = {k: doc[k] for k in doc if k != "facts"}
        digest = doc.get("hash") or _hash_obj(doc)
        src = {
            "id": doc.get("id"),
            "path": doc.get("path") or f"canon/{doc.get('id')}.md",
            "hash": digest,
            "status": doc.get("status", "CANON"),
            "high_impact": bool(doc.get("high_impact", False)),
            "depends_on": list(doc.get("depends_on") or []),
            "dependents": list(doc.get("dependents") or []),
        }
        sources.append(src)
        for i, fact in enumerate(doc.get("facts") or []):
            f = dict(fact)
            f.setdefault("polarity", "asserted")
            f.setdefault("high_impact", src["high_impact"])
            f["source"] = {
                "branch": branch_name,
                "path": src["path"],
                "location": fact.get("location") or f"fact[{i}]",
                "hash": digest,
            }
            f.setdefault("id", f"{src['id']}:{i}")
            facts.append(f)
    questions = list(branch.get("questions") or [])
    contradictions = list(branch.get("contradictions") or [])
    unadmitted = list(branch.get("unadmitted") or [])
    charter = dict(branch.get("charter") or {})
    commit = branch.get("commit") or _hash_obj(branch)
    state = {
        "canon_state_id": state_id or f"{branch_name}@{commit}",
        "evaluated_at": branch.get("evaluated_at") or "fixture",
        "branch_context": {
            "applicable_branch": branch_name,
            "commit": commit,
            "divergence": list(branch.get("divergence") or []),
            "charter": charter,
        },
        "sources": sources,
        "facts": facts,
        "questions": questions,
        "contradictions": contradictions,
        "unadmitted": unadmitted,
    }
    return state


def detect_changes(prev: dict, nxt: dict) -> dict:
    prev_map = {s["path"]: s for s in prev.get("sources", [])}
    next_map = {s["path"]: s for s in nxt.get("sources", [])}
    added = [p for p in next_map if p not in prev_map]
    removed = [p for p in prev_map if p not in next_map]
    changed = [
        p
        for p in next_map
        if p in prev_map and prev_map[p]["hash"] != next_map[p]["hash"]
    ]
    high = False
    for p in changed + added:
        src = next_map.get(p) or prev_map.get(p)
        if src and src.get("high_impact"):
            high = True
    for p in changed:
        if prev_map[p].get("high_impact") or next_map[p].get("high_impact"):
            high = True
    charter_changed = prev.get("branch_context", {}).get("charter") != nxt.get(
        "branch_context", {}
    ).get("charter")
    questions_changed = _hash_obj(prev.get("questions")) != _hash_obj(nxt.get("questions"))
    if high or charter_changed:
        scope = "systemic"
    elif changed or added or removed or questions_changed:
        scope = "local"
    else:
        scope = "none"
    return {
        "added": added,
        "removed": removed,
        "changed": changed,
        "high_impact": high,
        "charter_changed": charter_changed,
        "questions_changed": questions_changed,
        "scope": scope,
    }


def invalidate(prev_derived_paths: set[str], change_set: dict, prev_state: dict, next_state: dict) -> dict:
    """Return which derived fact IDs must be dropped.

    Local: facts from changed paths + facts whose source depends_on those IDs.
    Systemic: all derived facts.
    """
    all_ids = [f.get("id") for f in prev_state.get("facts", [])]
    if change_set["scope"] == "none":
        return {"dropped": [], "kept": all_ids, "scope": "none"}
    if change_set["scope"] == "systemic":
        return {"dropped": all_ids, "kept": [], "scope": "systemic"}
    changed_paths = set(change_set["changed"] + change_set["removed"] + change_set["added"])
    changed_ids = {
        s.get("id")
        for s in prev_state.get("sources", []) + next_state.get("sources", [])
        if s.get("path") in changed_paths
    }
    dropped = []
    kept = []
    for fact in prev_state.get("facts", []):
        src_path = (fact.get("source") or {}).get("path")
        src_id = None
        for s in prev_state.get("sources", []):
            if s.get("path") == src_path:
                src_id = s.get("id")
                break
        depends = []
        for s in prev_state.get("sources", []):
            if s.get("path") == src_path:
                depends = s.get("depends_on") or []
        if src_path in changed_paths or src_id in changed_ids or any(
            d in changed_ids for d in depends
        ):
            dropped.append(fact.get("id"))
        else:
            kept.append(fact.get("id"))
    return {"dropped": dropped, "kept": kept, "scope": "local"}


def contract_is_stale(contract: dict, current_state: dict) -> bool:
    current = {s["path"]: s["hash"] for s in current_state.get("sources", [])}
    for item in contract.get("source_hashes") or []:
        path, digest = item["path"], item["hash"]
        if path not in current or current[path] != digest:
            return True
    if contract.get("canon_state_id") != current_state.get("canon_state_id"):
        # Different id is stale unless hashes still match *and* caller treats id as alias.
        # Spec: id mismatch with any hash mismatch is stale; id mismatch alone with
        # identical hashes still means a new evaluation identity — treat as stale.
        return True
    return False


def _finding(cls: str, severity: str, summary: str, evidence: dict | None = None) -> dict:
    band = "canon_change" if cls == "CX-CHANGE-INTENT" else SEVERITY_TO_BAND.get(severity, "warning")
    item = {
        "class": cls,
        "severity": severity,
        "band": band,
        "summary": summary,
    }
    if evidence is not None:
        item["evidence"] = evidence
    return item


def _annotate_bands(findings: list[dict]) -> list[dict]:
    for f in findings:
        if "band" not in f:
            if f.get("class") == "CX-CHANGE-INTENT":
                f["band"] = "canon_change"
            else:
                f["band"] = SEVERITY_TO_BAND.get(f.get("severity"), "warning")
    return findings


def _request_ordinal(request: dict) -> float | None:
    if request.get("story_time") and request["story_time"].get("ordinal") is not None:
        return request["story_time"]["ordinal"]
    return None


def _on_established_main(
    state: dict, entity: str, predicate: str, value: Any, ordinal: float | None
) -> bool:
    for fact in _matching_facts(state, entity, predicate, ordinal):
        if (fact.get("polarity") or "asserted") == "asserted" and not _incompatible(
            fact.get("value"), value
        ):
            return True
    return False


def build_continuity_ledger(state: dict) -> list[dict]:
    """Derived ledger from an evaluated Canon State. Cache only; hashes must still match."""
    rows = []
    for fact in state.get("facts") or []:
        src = fact.get("source") or {}
        rows.append(
            {
                "entity": fact.get("entity"),
                "predicate": fact.get("predicate"),
                "value": fact.get("value"),
                "story_time_start": fact.get("story_time_start"),
                "story_time_end": fact.get("story_time_end"),
                "source_hash": src.get("hash"),
            }
        )
    return rows


def _continuity_findings(request: dict, ledger: list | None) -> list[dict]:
    if not ledger:
        return []
    findings = []
    ordinal = _request_ordinal(request)
    for claim in request.get("claims") or []:
        entity, predicate, value = claim.get("entity"), claim.get("predicate"), claim.get("value")
        c_ord = claim.get("story_time_ordinal")
        if c_ord is None:
            c_ord = ordinal
        for row in ledger:
            if row.get("entity") != entity or row.get("predicate") != predicate:
                continue
            window = {
                "story_time_start": row.get("story_time_start"),
                "story_time_end": row.get("story_time_end"),
            }
            if not _time_overlaps(window, c_ord):
                continue
            if _incompatible(row.get("value"), value):
                findings.append(
                    _finding(
                        "CX-CONTINUITY",
                        "block",
                        (
                            f"{entity}.{predicate}={value!r} breaks continuity "
                            f"with prior {row.get('value')!r}"
                        ),
                        evidence={"source_hash": row.get("source_hash")}
                        if row.get("source_hash")
                        else None,
                    )
                )
    return findings


def _contamination_findings(request: dict, state: dict) -> list[dict]:
    findings = []
    if request.get("cites_contract_as_canon") or request.get("presents_generated_as_canon"):
        findings.append(
            _finding(
                "CX-CONTAMINATION",
                "block",
                "Generated or contract material presented as established canon",
            )
        )
    ordinal = _request_ordinal(request)
    for claim in request.get("claims") or []:
        c_ord = claim.get("story_time_ordinal")
        if c_ord is None:
            c_ord = ordinal
        src = claim.get("source") or {}
        cites_contract = bool(claim.get("cites_contract")) or str(src.get("path") or "").startswith(
            "contract:"
        ) or src.get("kind") == "generation_contract"
        if cites_contract:
            findings.append(
                _finding(
                    "CX-CONTAMINATION",
                    "block",
                    f"Claim {claim.get('entity')}.{claim.get('predicate')} cites the Generation Contract as a world source",
                )
            )
            continue
        if claim.get("presents_as_canon"):
            if not _on_established_main(
                state, claim["entity"], claim["predicate"], claim["value"], c_ord
            ):
                findings.append(
                    _finding(
                        "CX-CONTAMINATION",
                        "block",
                        (
                            f"Claim {claim['entity']}.{claim['predicate']} presented as "
                            "established canon is not on main"
                        ),
                    )
                )
    return findings


def _bypass_findings(request: dict) -> list[dict]:
    findings = []
    if (
        request.get("redefines_constraints")
        or request.get("contract_override")
        or request.get("skip_pre_generation")
        or request.get("promote_provisional_to_hard")
    ):
        findings.append(
            _finding(
                "CX-BYPASS",
                "block",
                "Generator attempted to redefine, skip, or relabel locked constraints",
            )
        )
    return findings


def lock_contract(contract: dict) -> dict:
    """Mark a Generation Contract immutable for the generator. Mutates and returns it."""
    contract["locked"] = True
    payload = {k: contract[k] for k in contract if k != "lock_hash"}
    contract["lock_hash"] = _hash_obj(payload)
    return contract


def contract_was_mutated(locked: dict, presented: dict) -> bool:
    """True when the generator altered hard/status/hash fields of a locked contract."""
    if not locked or not presented:
        return False
    for key in LOCK_COMPARE_KEYS:
        if _hash_obj(locked.get(key)) != _hash_obj(presented.get(key)):
            return True
    return False


def _constraint_bands(state: dict, source_status: dict) -> dict:
    hard = list(source_status.get("ESTABLISHED_CANON") or [])
    for fact in state.get("facts") or []:
        pol = fact.get("polarity") or "asserted"
        if pol in ("forbidden", "denied"):
            hard.append(
                {
                    "entity": fact.get("entity"),
                    "predicate": fact.get("predicate"),
                    "value": fact.get("value"),
                    "polarity": pol,
                    "source": fact.get("source"),
                    "band": "HARD_CONSTRAINTS",
                }
            )
    for q in state.get("questions") or []:
        status = (q.get("status") or "").upper()
        if "INTENTIONALLY UNRESOLVED" in status or "NOT READY" in status or status in (
            "INTENTIONALLY_UNRESOLVED",
            "NOT_READY",
        ):
            hard.append(
                {
                    "id": q.get("id"),
                    "status": q.get("status"),
                    "band": "HARD_CONSTRAINTS",
                    "kind": "mystery_or_not_ready",
                }
            )
    extensions = [
        x
        for x in (source_status.get("CURRENT_WORKING_DEVELOPMENT") or [])
        if x.get("class") == "EXTENDS_CANON"
    ]
    soft = list(source_status.get("CANON_CLARIFICATIONS") or []) + extensions
    return {
        "HARD_CONSTRAINTS": hard,
        "SOFT_CONTEXT": soft,
        "CURRENT_AUTHORIAL_DIRECTION": list(source_status.get("AUTHORIAL_DIRECTION") or []),
        "PROVISIONAL_MATERIAL": list(source_status.get("PROVISIONAL") or []),
        "FORBIDDEN_ASSUMPTIONS": [
            "unadmitted drafts are not canon",
            "research is not canon",
            "do not resolve intentional mysteries",
            "Arena Splash is not automatically canon",
            "do not present proposed or developmental splash as established canon",
            "do not override main merely because splash is newer",
            "the generator must not redefine locked constraints",
            "do not cite the Generation Contract as a world source",
        ],
    }


def post_verify(
    output: dict,
    contract: dict | None,
    state: dict,
    *,
    live_heads: dict | None = None,
    splash_state: dict | None = None,
    current_state: dict | None = None,
    presented_contract: dict | None = None,
    continuity_ledger: list | None = None,
) -> dict:
    """Second layer. Does not replace pre-generation. Never admits material."""
    extra: list[dict] = []
    if contract is None:
        extra.append(
            _finding(
                "CX-BYPASS",
                "block",
                "Post-generation without a locked pre-generation contract",
            )
        )
    else:
        if not contract.get("locked") or not contract.get("lock_hash"):
            extra.append(
                _finding(
                    "CX-BYPASS",
                    "block",
                    "Pre-generation contract was not locked",
                )
            )
        if presented_contract is not None and contract_was_mutated(contract, presented_contract):
            extra.append(
                _finding(
                    "CX-BYPASS",
                    "block",
                    "Generator mutated the locked Generation Contract",
                )
            )
        check_state = current_state if current_state is not None else state
        if contract_is_stale(contract, check_state):
            extra.append(
                _finding(
                    "CX-STALE",
                    "stop",
                    "Generation Contract is stale relative to the current Canon State",
                )
            )
        if contract.get("canon_state_id") != state.get("canon_state_id"):
            extra.append(
                _finding(
                    "CX-STALE",
                    "stop",
                    "Post-generation Canon State identity does not match the locked contract",
                )
            )
    eval_state = state
    ledger = continuity_ledger or (state.get("continuity_ledger") if state else None)
    if ledger:
        eval_state = dict(state)
        eval_state["continuity_ledger"] = ledger
    inner = verify(
        output,
        eval_state,
        live_heads=live_heads,
        splash_state=splash_state,
        classifications=eval_state.get("splash_classifications") or [],
    )
    inner["findings"] = extra + list(inner.get("findings") or [])
    _annotate_bands(inner["findings"])
    inner["decision"] = decide(inner["findings"], output)
    inner["layer"] = "post_generation"
    inner["pre_generation_contract_id"] = (contract or {}).get("contract_id")
    inner["admitted"] = False
    inner["checks_performed"] = list(CHECKS) + ["post_generation"]
    inner["must_re_resolve"] = any(f.get("class") == "CX-STALE" for f in inner["findings"])
    return {"report": inner, "admitted": False, "contract": None}


def _matching_facts(state: dict, entity: str, predicate: str, ordinal: float | None):
    for fact in state.get("facts", []):
        if fact.get("status_override") == "RETIRED":
            continue
        if fact.get("entity") != entity or fact.get("predicate") != predicate:
            continue
        if fact.get("source_status") == "RETIRED":
            continue
        src_status = None
        path = (fact.get("source") or {}).get("path")
        for s in state.get("sources", []):
            if s.get("path") == path:
                src_status = s.get("status")
        if src_status and src_status != "CANON":
            continue
        if _time_overlaps(fact, ordinal):
            yield fact


def verify(
    request: dict,
    state: dict,
    *,
    live_heads: dict | None = None,
    splash_state: dict | None = None,
    classifications: list[dict] | None = None,
) -> dict:
    findings: list[dict] = []
    kind = request.get("generation_kind")
    charter = (state.get("branch_context") or {}).get("charter") or {}
    ordinal = None
    if request.get("story_time") and request["story_time"].get("ordinal") is not None:
        ordinal = request["story_time"]["ordinal"]

    continue_splash = _continues_splash(request, splash_state)
    if continue_splash and splash_state:
        charter = (splash_state.get("branch_context") or {}).get("charter") or charter

    classifications = classifications if classifications is not None else list(
        state.get("splash_classifications") or []
    )

    # Extra live heads are not automatic CX-DIVERGENCE. Arena Splash must be
    # inspected and classified against main; existence alone is not a stop.
    splash_head_names = _splash_heads(live_heads)
    if splash_head_names and splash_state is None and not request.get("target_branch"):
        findings.append(
            {
                "class": "CX-AMBIGUITY",
                "severity": "stop",
                "summary": "Live Arena Splash head present but not classified against main",
            }
        )

    divergence = (state.get("branch_context") or {}).get("divergence") or []
    if (
        divergence
        and not request.get("target_branch")
        and splash_state is None
        and not splash_head_names
    ):
        findings.append(
            {
                "class": "CX-DIVERGENCE",
                "severity": "stop",
                "summary": "Recorded non-splash divergence without target_branch",
            }
        )

    # Charter / branch constraints (Splash charter only when continuing Splash)
    if kind == "narrative" and charter.get("narrative_authorized") is False:
        findings.append(
            {
                "class": "CX-BRANCH",
                "severity": "block",
                "summary": "Narrative generation is not authorized on this branch",
            }
        )

    if request.get("uses_unadmitted_as_canon"):
        findings.append(
            {
                "class": "CX-ADMISSION",
                "severity": "block",
                "summary": "Request cites unadmitted generated material as canon",
            }
        )

    # Unadmitted documents must not be used as CANON facts (already excluded);
    # additionally, claiming an unadmitted entity is canon:
    unadmitted_ids = {u.get("id") for u in state.get("unadmitted") or []}
    for claim in request.get("claims") or []:
        if claim.get("cites_unadmitted") or claim.get("entity") in unadmitted_ids:
            if request.get("treat_unadmitted_as_canon"):
                findings.append(
                    {
                        "class": "CX-ADMISSION",
                        "severity": "block",
                        "summary": f"Unadmitted entity {claim.get('entity')} treated as canon",
                    }
                )

    q_by_id = {q.get("id"): q for q in state.get("questions") or []}

    for claim in request.get("claims") or []:
        entity, predicate, value = claim["entity"], claim["predicate"], claim["value"]
        c_ord = claim.get("story_time_ordinal")
        if c_ord is None:
            c_ord = ordinal

        # Mystery / not ready / open
        qid = claim.get("resolves_question")
        if qid and qid in q_by_id:
            status = (q_by_id[qid].get("status") or "").upper()
            if "INTENTIONALLY UNRESOLVED" in status or status == "INTENTIONALLY_UNRESOLVED":
                findings.append(
                    {
                        "class": "CX-MYSTERY",
                        "severity": "block",
                        "summary": f"Would resolve {qid}",
                    }
                )
            elif "NOT READY" in status or status == "NOT_READY":
                findings.append(
                    {
                        "class": "CX-NOT-READY",
                        "severity": "block",
                        "summary": f"Would invent {qid}",
                    }
                )
            elif status.startswith("OPEN"):
                findings.append(
                    {
                        "class": "CX-EXPANSION",
                        "severity": "warn",
                        "summary": f"Fills OPEN {qid} (not canon until admitted)",
                    }
                )

        if claim.get("high_impact") and kind == "narrative":
            findings.append(
                {
                    "class": "CX-HIGH-IMPACT-SMUGGLE",
                    "severity": "block",
                    "summary": f"Narrative introduces high-impact claim on {entity}.{predicate}",
                }
            )

        matches = list(_matching_facts(state, entity, predicate, c_ord))
        if c_ord is not None and not matches:
            for fact in state.get("facts") or []:
                if fact.get("status_override") == "RETIRED":
                    continue
                if fact.get("entity") != entity or fact.get("predicate") != predicate:
                    continue
                start = fact.get("story_time_start")
                if start is None:
                    continue
                if (
                    c_ord < start
                    and (fact.get("polarity") or "asserted") == "asserted"
                    and not _incompatible(fact.get("value"), value)
                    and not _time_overlaps(fact, c_ord)
                ):
                    findings.append(
                        {
                            "class": "CX-TEMPORAL",
                            "severity": "block",
                            "summary": (
                                f"{entity}.{predicate}={value!r} is not yet established "
                                f"at story-time {c_ord} (starts {start})"
                            ),
                            "evidence": fact.get("source"),
                        }
                    )
                    break
        for fact in matches:
            pol = fact.get("polarity") or "asserted"
            if pol == "forbidden":
                findings.append(
                    {
                        "class": "CX-INDIRECT",
                        "severity": "block",
                        "summary": f"{entity}.{predicate} is negative space",
                        "evidence": fact.get("source"),
                    }
                )
                continue
            if pol == "denied" and value not in (False, "false", "denied"):
                findings.append(
                    {
                        "class": "CX-DIRECT",
                        "severity": "block",
                        "summary": f"{entity}.{predicate} is denied in canon",
                        "evidence": fact.get("source"),
                    }
                )
                continue
            if pol == "asserted" and _incompatible(fact.get("value"), value):
                # temporal class if the fact is time-bounded and claim misses the window
                cls = "CX-DIRECT"
                findings.append(
                    {
                        "class": cls,
                        "severity": "block",
                        "summary": (
                            f"{entity}.{predicate}={value!r} conflicts with "
                            f"canon {fact.get('value')!r}"
                        ),
                        "evidence": fact.get("source"),
                    }
                )

        # Knowledge: if a matching fact is knowledge-bound and viewpoint doesn't include knower
        viewpoint = set(request.get("viewpoint_entities") or [])
        if claim.get("requires_knowledge_of"):
            target = claim["requires_knowledge_of"]
            # find facts about that knowledge
            knew = False
            for fact in state.get("facts", []):
                if (
                    fact.get("predicate") == "knows"
                    and fact.get("entity") in viewpoint
                    and fact.get("value") == target
                    and _time_overlaps(fact, c_ord)
                ):
                    knew = True
            if viewpoint and not knew:
                findings.append(
                    {
                        "class": "CX-KNOWLEDGE",
                        "severity": "block",
                        "summary": f"Viewpoint {sorted(viewpoint)} does not know {target} at this story-time",
                    }
                )
        # facts that are known_by restricted: acting as if world-public
        if claim.get("as_if_public"):
            for fact in matches:
                known_by = fact.get("known_by")
                if known_by is not None and not (viewpoint & set(known_by)):
                    findings.append(
                        {
                            "class": "CX-KNOWLEDGE",
                            "severity": "block",
                            "summary": f"{entity}.{predicate} is not public knowledge for {sorted(viewpoint)}",
                            "evidence": fact.get("source"),
                        }
                    )

        # Causal: claim.precluded_by
        if claim.get("needs_cause"):
            cause_id = claim["needs_cause"]
            present = any(f.get("id") == cause_id or f.get("value") == cause_id for f in state.get("facts", []))
            # also allow cause as a fact value on a named event
            present = present or any(
                f.get("entity") == cause_id and _time_overlaps(f, c_ord) and (f.get("story_time_start") is None or (c_ord is not None and f.get("story_time_start") <= c_ord))
                for f in state.get("facts", [])
            )
            if not present:
                findings.append(
                    {
                        "class": "CX-CAUSAL",
                        "severity": "block",
                        "summary": f"Claim requires cause {cause_id} which is not in applicable canon",
                    }
                )
        for fact in matches:
            for precluded in fact.get("precludes") or []:
                if value == precluded or claim.get("event") == precluded:
                    findings.append(
                        {
                            "class": "CX-CAUSAL",
                            "severity": "block",
                            "summary": f"Canon fact precludes {precluded}",
                            "evidence": fact.get("source"),
                        }
                    )

        # Authority: citing non-canon. RETIRED is a hard block, not a guess.
        if claim.get("cited_status") and claim["cited_status"] not in ("CANON", None):
            if claim["cited_status"] == "RETIRED":
                findings.append(
                    {
                        "class": "CX-RETIRED",
                        "severity": "block",
                        "summary": f"Claim cites RETIRED material as live canon",
                    }
                )
            else:
                findings.append(
                    {
                        "class": "CX-AUTHORITY",
                        "severity": "stop",
                        "summary": f"Claim cites {claim['cited_status']} as canon",
                    }
                )

    # Active contradictions intersecting request entities
    req_entities = {c["entity"] for c in request.get("claims") or []}
    for item in state.get("contradictions") or []:
        if item.get("status", "OPEN") != "OPEN":
            continue
        involved = set(item.get("entities") or [])
        if not involved or involved & req_entities:
            findings.append(
                {
                    "class": "CX-UNRESOLVED-REGISTER",
                    "severity": "stop",
                    "summary": f"Active contradiction {item.get('id')} intersects request",
                }
            )

    if request.get("ambiguous"):
        findings.append(
            {
                "class": "CX-AMBIGUITY",
                "severity": "stop",
                "summary": "Request marked ambiguous",
            }
        )

    # Expansion: claim with no match and no other block — warning if tagged expansion
    for claim in request.get("claims") or []:
        if claim.get("expansion") and not any(
            f["class"] in ("CX-DIRECT", "CX-INDIRECT", "CX-TEMPORAL", "CX-CAUSAL")
            for f in findings
        ):
            findings.append(
                {
                    "class": "CX-EXPANSION",
                    "severity": "info",
                    "summary": f"Legitimate expansion: {claim['entity']}.{claim['predicate']}",
                }
            )

    # Arena vs main: classify, do not merge, do not ignore.
    live_classifications = [
        c for c in classifications if c.get("class") != "ABANDONED_OR_SUPERSEDED"
    ]
    for item in live_classifications:
        if item.get("class") in ("CONTRADICTS_CANON", "RETCON_PROPOSAL"):
            findings.append(
                {
                    "class": "CX-SPLASH-CONFLICT",
                    "severity": "warn",
                    "summary": (
                        f"Arena {item.get('entity')}.{item.get('predicate')}="
                        f"{item.get('value')!r} {item.get('class')} vs main "
                        f"(classified, not merged)"
                    ),
                    "evidence": item.get("source"),
                }
            )

    # Competing current Arena directions on the same predicate.
    by_key: dict[tuple, list[dict]] = {}
    for item in live_classifications:
        if item.get("class") not in STRONG_DIRECTION | PROVISIONAL_SPLASH | ESTABLISHED_SPLASH:
            continue
        if item.get("class") == "EXPLORATORY":
            continue
        key = (item.get("entity"), item.get("predicate"))
        by_key.setdefault(key, []).append(item)
    for key, items in by_key.items():
        values = {i.get("value") for i in items}
        strong = [i for i in items if i.get("class") in STRONG_DIRECTION]
        strong_values = {i.get("value") for i in strong}
        if len(strong_values) > 1:
            findings.append(
                {
                    "class": "CX-AMBIGUITY",
                    "severity": "stop",
                    "summary": (
                        f"Competing Arena directions for {key[0]}.{key[1]}: "
                        f"{sorted(strong_values, key=str)}"
                    ),
                }
            )
        elif len(values) > 1 and len(strong_values) <= 1:
            # Provisional disagreement is a warning, not a freeze.
            findings.append(
                {
                    "class": "CX-WORKING-DIRECTION",
                    "severity": "warn",
                    "summary": (
                        f"Arena has competing provisional values for {key[0]}.{key[1]}"
                    ),
                }
            )

    claims = list(request.get("claims") or [])
    req_entities = {c["entity"] for c in claims}
    if request.get("ignore_arena_development") and any(
        c.get("class") in STRONG_DIRECTION for c in live_classifications
    ):
        findings.append(
            {
                "class": "CX-WORKING-DIRECTION",
                "severity": "warn",
                "summary": "Request ignores strong current Arena development",
            }
        )

    for claim in claims:
        entity, predicate, value = claim["entity"], claim["predicate"], claim["value"]
        related = [
            c
            for c in live_classifications
            if c.get("entity") == entity and c.get("predicate") == predicate
        ]
        established_claim = _treats_as_established(request, claim)
        for item in related:
            cls = item.get("class")
            if cls == "UNRESOLVED":
                findings.append(
                    {
                        "class": "CX-AMBIGUITY",
                        "severity": "stop",
                        "summary": (
                            f"Unresolved Arena material overlaps {entity}.{predicate}"
                        ),
                    }
                )
            splash_value = item.get("value")
            uses_splash_value = not _incompatible(splash_value, value)
            diverges = _incompatible(splash_value, value)
            if cls in ("CONTRADICTS_CANON", "RETCON_PROPOSAL") and uses_splash_value:
                if established_claim or cls == "RETCON_PROPOSAL" and established_claim:
                    findings.append(
                        {
                            "class": "CX-SPLASH-CONFLICT",
                            "severity": "stop",
                            "summary": (
                                f"Would establish Arena {cls} {entity}.{predicate}="
                                f"{value!r} over main"
                            ),
                        }
                    )
                elif continue_splash:
                    findings.append(
                        {
                            "class": "CX-SPLASH-CONFLICT",
                            "severity": "warn",
                            "summary": (
                                f"Arena storyline uses {cls} "
                                f"{entity}.{predicate}; do not present as "
                                f"established canon"
                            ),
                        }
                    )
            if cls == "RETCON_PROPOSAL" and uses_splash_value and established_claim:
                # already handled; keep explicit
                pass
            if cls in NON_ESTABLISHED_SPLASH:
                if established_claim:
                    findings.append(
                        {
                            "class": "CX-SPLASH-PROPOSED",
                            "severity": "stop",
                            "summary": (
                                f"Request treats Arena {cls} {entity}.{predicate} "
                                f"as established canon"
                            ),
                        }
                    )
                elif cls in PROVISIONAL_SPLASH and uses_splash_value:
                    findings.append(
                        {
                            "class": "CX-EXPANSION",
                            "severity": "warn",
                            "summary": (
                                f"Arena {cls} {entity}.{predicate} used as "
                                f"working material, not established canon"
                            ),
                        }
                    )
            if diverges and cls in STRONG_DIRECTION:
                findings.append(
                    {
                        "class": "CX-WORKING-DIRECTION",
                        "severity": "warn",
                        "summary": (
                            f"Request diverges from current Arena direction "
                            f"{entity}.{predicate}={splash_value!r}"
                        ),
                    }
                )
            if diverges and cls in PROVISIONAL_SPLASH and cls != "EXPLORATORY":
                findings.append(
                    {
                        "class": "CX-WORKING-DIRECTION",
                        "severity": "warn",
                        "summary": (
                            f"Request diverges from provisional Arena "
                            f"{entity}.{predicate}={splash_value!r}"
                        ),
                    }
                )

    findings.extend(_bypass_findings(request))
    findings.extend(_contamination_findings(request, state))
    findings.extend(
        _continuity_findings(
            request,
            state.get("continuity_ledger") or request.get("continuity_ledger") or [],
        )
    )
    _annotate_bands(findings)

    decision = decide(findings, request)
    report = {
        "request_id": request.get("request_id") or "req",
        "canon_state_id": state.get("canon_state_id"),
        "branch_context": state.get("branch_context"),
        "evaluated_at": state.get("evaluated_at"),
        "relevant_sources": [
            {"path": s["path"], "hash": s["hash"]} for s in state.get("sources", [])
        ],
        "constraints_extracted": [
            {
                "entity": f.get("entity"),
                "predicate": f.get("predicate"),
                "value": f.get("value"),
                "source": f.get("source"),
            }
            for f in state.get("facts", [])
        ],
        "checks_performed": list(CHECKS),
        "findings": findings,
        "decision": decision,
        "invalidation": None,
        "contract_id": None,
        "splash_classifications": classifications,
        "working_canon_context": state.get("working_canon_context")
        or build_working_canon_context(state),
        "layer": "pre_generation",
        "admitted": False,
    }
    return report


def decide(findings: list[dict], request: dict) -> str:
    classes = {f["class"] for f in findings}
    if request.get("explicit_canon_change") or "CX-CHANGE-INTENT" in classes:
        return "CANON_CHANGE_REQUIRED"
    order = [
        ("CX-DIVERGENCE", "REQUIRES_CLARIFICATION"),
        ("CX-BRANCH", "BLOCK"),
        ("CX-ADMISSION", "BLOCK"),
        ("CX-CONTAMINATION", "BLOCK"),
        ("CX-BYPASS", "BLOCK"),
        ("CX-CONTINUITY", "BLOCK"),
        ("CX-MYSTERY", "BLOCK"),
        ("CX-NOT-READY", "BLOCK"),
        ("CX-HIGH-IMPACT-SMUGGLE", "BLOCK"),
        ("CX-RETIRED", "BLOCK"),
        ("CX-DIRECT", "BLOCK"),
        ("CX-INDIRECT", "BLOCK"),
        ("CX-TEMPORAL", "BLOCK"),
        ("CX-KNOWLEDGE", "BLOCK"),
        ("CX-CAUSAL", "BLOCK"),
        ("CX-UNRESOLVED-REGISTER", "REQUIRES_CLARIFICATION"),
        ("CX-AMBIGUITY", "REQUIRES_CLARIFICATION"),
        ("CX-STALE", "REQUIRES_CLARIFICATION"),
        ("CX-AUTHORITY", "REQUIRES_CLARIFICATION"),
    ]
    for cls, result in order:
        if cls in classes:
            return result
    if any(
        f["class"] == "CX-SPLASH-CONFLICT" and f.get("severity") == "stop"
        for f in findings
    ):
        return "REQUIRES_CLARIFICATION"
    if any(
        f["class"] == "CX-SPLASH-PROPOSED" and f.get("severity") == "stop"
        for f in findings
    ):
        return "REQUIRES_CLARIFICATION"
    if any(f.get("severity") == "warn" for f in findings) or "CX-EXPANSION" in classes:
        # expansion-only with no warn can still be PASS if tagged info
        if any(f.get("severity") == "warn" for f in findings):
            return "PASS_WITH_WARNINGS"
        if "CX-EXPANSION" in classes and not any(
            f["class"] not in ("CX-EXPANSION",) for f in findings
        ):
            return "PASS"
    if findings and all(f.get("severity") in ("info", "warn") for f in findings):
        if any(f.get("severity") == "warn" for f in findings):
            return "PASS_WITH_WARNINGS"
        return "PASS"
    if not findings:
        return "PASS"
    return "PASS_WITH_WARNINGS"


def make_contract(request: dict, state: dict, report: dict) -> dict | None:
    if report["decision"] not in ("PASS", "PASS_WITH_WARNINGS"):
        return None
    hashes = [{"path": s["path"], "hash": s["hash"]} for s in state.get("sources", [])]
    unchanged = []
    for fact in state.get("facts", []):
        unchanged.append(
            {
                "entity": fact.get("entity"),
                "predicate": fact.get("predicate"),
                "value": fact.get("value"),
                "source": fact.get("source"),
            }
        )
    warnings = [f["summary"] for f in report["findings"] if f.get("severity") == "warn"]
    contract = {
        "contract_id": f"contract:{report['request_id']}:{state['canon_state_id']}",
        "canon_state_id": state["canon_state_id"],
        "branch_context": state.get("branch_context"),
        "evaluated_at": state.get("evaluated_at"),
        "must_remain_unchanged": unchanged,
        "character_constraints": [
            f for f in unchanged if f.get("predicate") in ("vital_status", "role", "knows")
        ],
        "relationship_constraints": [
            f for f in unchanged if f.get("predicate") in ("allied_with", "married_to", "relation")
        ],
        "timeline_constraints": [
            f for f in unchanged if f.get("predicate") in ("occurs", "date", "era")
        ],
        "knowledge_constraints": [f for f in unchanged if f.get("predicate") == "knows"],
        "location_constraints": [
            f for f in unchanged if f.get("predicate") in ("located_in", "capital")
        ],
        "political_faction_constraints": [
            f for f in unchanged if f.get("predicate") in ("allied_with", "controls", "faction")
        ],
        "causal_constraints": [
            {"id": f.get("id"), "precludes": f.get("precludes")}
            for f in state.get("facts", [])
            if f.get("precludes") or f.get("caused_by")
        ],
        "world_rules": [
            f
            for f in unchanged
            if (f.get("source") or {}).get("path", "").endswith("LAW.md")
            or f.get("predicate") == "world_rule"
        ],
        "permitted_creative_space": [
            f["summary"] for f in report["findings"] if f["class"] == "CX-EXPANSION"
        ],
        "warnings": warnings,
        "uncertainties": [
            q["id"]
            for q in state.get("questions", [])
            if "UNRESOLVED" in (q.get("status") or "").upper()
            or "NOT READY" in (q.get("status") or "").upper()
        ],
        "forbidden_assumptions": [
            "unadmitted drafts are not canon",
            "research is not canon",
            "do not resolve intentional mysteries",
            "Arena Splash is not automatically canon",
            "do not present proposed or developmental splash as established canon",
            "do not override main merely because splash is newer",
        ],
        "authorized_changes": [],
        "source_hashes": hashes,
        "source_status": _contract_source_status(state),
        "working_canon_context": state.get("working_canon_context")
        or build_working_canon_context(state),
    }
    contract["constraint_bands"] = _constraint_bands(state, contract["source_status"])
    for item in state.get("splash_classifications") or []:
        if item.get("class") in ("CONTRADICTORY", "CONTRADICTS_CANON"):
            contract["forbidden_assumptions"].append(
                f"conflict: splash {item.get('entity')}.{item.get('predicate')}="
                f"{item.get('value')!r} vs main — classified, not silently resolved"
            )
    lock_contract(contract)
    report["contract_id"] = contract["contract_id"]
    return contract


def _contract_source_status(state: dict) -> dict:
    bands = {k: [] for k in CONTRACT_BANDS}
    for fact in state.get("facts") or []:
        bands["ESTABLISHED_CANON"].append(
            {
                "entity": fact.get("entity"),
                "predicate": fact.get("predicate"),
                "value": fact.get("value"),
                "class": "CONFIRMS_CANON",
                "source": fact.get("source"),
            }
        )
    for item in state.get("splash_classifications") or []:
        cls = _norm_class(item.get("class"))
        payload = {
            "entity": item.get("entity"),
            "predicate": item.get("predicate"),
            "value": item.get("value"),
            "class": cls,
            "source": item.get("source"),
        }
        if cls in ("CONFIRMS_CANON", "ABANDONED_OR_SUPERSEDED"):
            continue
        if cls == "CLARIFIES_CANON":
            bands["CANON_CLARIFICATIONS"].append(payload)
        elif cls == "DEVELOPS_INTENDED_CANON":
            bands["AUTHORIAL_DIRECTION"].append(payload)
            bands["CURRENT_WORKING_DEVELOPMENT"].append(payload)
        elif cls == "EXTENDS_CANON":
            bands["CURRENT_WORKING_DEVELOPMENT"].append(payload)
        elif cls in PROVISIONAL_SPLASH:
            bands["PROVISIONAL"].append(payload)
        elif cls in ("CONTRADICTS_CANON", "RETCON_PROPOSAL"):
            bands["CONFLICTS"].append(payload)
        elif cls == "UNRESOLVED":
            bands["OPEN_QUESTIONS"].append(payload)
    return bands


def run(
    request: dict,
    branch_name: str,
    branch: dict,
    *,
    live_heads: dict | None = None,
    splash: dict | None = None,
    continuity_ledger: list | None = None,
) -> dict:
    state = build_canon_state(branch_name, branch)
    ledger = continuity_ledger or request.get("continuity_ledger")
    if ledger:
        state["continuity_ledger"] = ledger
    splash_state = None
    if splash:
        splash_state = attach_splash(state, splash["name"], splash["branch"])
    report = verify(
        request,
        state,
        live_heads=live_heads,
        splash_state=splash_state,
        classifications=state.get("splash_classifications") or [],
    )
    contract = make_contract(request, state, report)
    if contract:
        report["contract_id"] = contract["contract_id"]
        report["lock_hash"] = contract.get("lock_hash")
    return {
        "state": state,
        "report": report,
        "contract": contract,
        "splash_state": splash_state,
    }


def admit(unadmitted_doc: dict, branch: dict) -> dict:
    """Move a proposed document into canon on a copy of the branch snapshot."""
    nxt = copy.deepcopy(branch)
    nxt.setdefault("canon", [])
    nxt["unadmitted"] = [
        u for u in nxt.get("unadmitted") or [] if u.get("id") != unadmitted_doc.get("id")
    ]
    doc = copy.deepcopy(unadmitted_doc)
    doc["status"] = "CANON"
    doc.pop("proposed", None)
    nxt["canon"].append(doc)
    nxt["commit"] = _hash_obj(nxt)
    return nxt
