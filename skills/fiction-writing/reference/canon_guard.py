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
)


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


def verify(request: dict, state: dict, *, live_heads: dict | None = None) -> dict:
    findings: list[dict] = []
    kind = request.get("generation_kind")
    charter = (state.get("branch_context") or {}).get("charter") or {}
    ordinal = None
    if request.get("story_time") and request["story_time"].get("ordinal") is not None:
        ordinal = request["story_time"]["ordinal"]

    # Divergence: unchosen applicable branch
    divergence = (state.get("branch_context") or {}).get("divergence") or []
    if live_heads and len(live_heads) > 1 and not request.get("target_branch"):
        # material divergence if any other head present
        findings.append(
            {
                "class": "CX-DIVERGENCE",
                "severity": "stop",
                "summary": "Multiple live heads and no target_branch",
            }
        )
    elif divergence and not request.get("target_branch"):
        findings.append(
            {
                "class": "CX-DIVERGENCE",
                "severity": "stop",
                "summary": "Recorded divergence without target_branch",
            }
        )

    # Charter / branch constraints
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

        # Authority: citing non-canon
        if claim.get("cited_status") and claim["cited_status"] not in ("CANON", None):
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
        ("CX-AUTHORITY", "REQUIRES_CLARIFICATION"),
    ]
    for cls, result in order:
        if cls in classes:
            return result
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
        ],
        "authorized_changes": [],
        "source_hashes": hashes,
    }
    report["contract_id"] = contract["contract_id"]
    return contract


def run(request: dict, branch_name: str, branch: dict, *, live_heads: dict | None = None) -> dict:
    state = build_canon_state(branch_name, branch)
    report = verify(request, state, live_heads=live_heads)
    contract = make_contract(request, state, report)
    return {"state": state, "report": report, "contract": contract}


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
