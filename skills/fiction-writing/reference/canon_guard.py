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
)

SPLASH_CLASSES = (
    "CONFIRMED_CANON",
    "CANON_CLARIFICATION",
    "CANON_EXTENSION",
    "AUTHORIAL_INTENT",
    "PROPOSED_CANON",
    "DEVELOPMENTAL",
    "EXPLORATORY",
    "CONTRADICTORY",
    "UNRESOLVED",
)

ESTABLISHED_SPLASH = frozenset({"CONFIRMED_CANON", "CANON_CLARIFICATION"})

NON_ESTABLISHED_SPLASH = frozenset(
    {
        "CANON_EXTENSION",
        "AUTHORIAL_INTENT",
        "PROPOSED_CANON",
        "DEVELOPMENTAL",
        "EXPLORATORY",
    }
)

RELATION_TO_CLASS = {
    "clarifies": "CANON_CLARIFICATION",
    "clarification": "CANON_CLARIFICATION",
    "extends": "CANON_EXTENSION",
    "extension": "CANON_EXTENSION",
    "intent": "AUTHORIAL_INTENT",
    "authorial_intent": "AUTHORIAL_INTENT",
    "proposed": "PROPOSED_CANON",
    "proposed_canon": "PROPOSED_CANON",
    "developmental": "DEVELOPMENTAL",
    "draft": "DEVELOPMENTAL",
    "development": "DEVELOPMENTAL",
    "exploratory": "EXPLORATORY",
    "experiment": "EXPLORATORY",
    "alternate": "EXPLORATORY",
    "contradicts": "CONTRADICTORY",
    "contradiction": "CONTRADICTORY",
    "confirmed": "CONFIRMED_CANON",
    "restates": "CONFIRMED_CANON",
    "unresolved": "UNRESOLVED",
}

CONTRACT_BANDS = (
    "CANONICAL",
    "CANON_CLARIFICATION",
    "AUTHORIAL_INTENT",
    "PROPOSED",
    "CONFLICT",
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
    """Classify each Splash statement against current main. Re-run when either side moves.

    Branch membership never determines the class. Compatible restatement on main is
    CONFIRMED_CANON; a newer Splash value does not override main.
    """
    out: list[dict] = []
    for fact in _splash_fact_records(splash_state):
        entity, predicate, value = fact.get("entity"), fact.get("predicate"), fact.get("value")
        if entity is None or predicate is None:
            continue
        hinted = _hinted_class(fact)
        ordinal = fact.get("story_time_start")
        if ordinal is None:
            ordinal = fact.get("story_time_ordinal")
        matches = list(_matching_facts(main_state, entity, predicate, ordinal))
        origin = fact.get("_origin") or "canon"
        if matches:
            incompatible = any(
                (m.get("polarity") or "asserted") == "asserted"
                and _incompatible(m.get("value"), value)
                for m in matches
            )
            if incompatible:
                cls = "EXPLORATORY" if hinted == "EXPLORATORY" else "CONTRADICTORY"
            elif hinted == "CANON_CLARIFICATION":
                cls = "CANON_CLARIFICATION"
            else:
                # Main already holds a compatible value: Splash restates established canon.
                cls = "CONFIRMED_CANON"
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

    # Splash vs main: classify, do not merge, do not ignore.
    for item in classifications:
        if item.get("class") == "CONTRADICTORY":
            findings.append(
                {
                    "class": "CX-SPLASH-CONFLICT",
                    "severity": "warn",
                    "summary": (
                        f"Splash {item.get('entity')}.{item.get('predicate')}="
                        f"{item.get('value')!r} contradicts main "
                        f"(classified, not merged)"
                    ),
                    "evidence": item.get("source"),
                }
            )

    for claim in request.get("claims") or []:
        entity, predicate, value = claim["entity"], claim["predicate"], claim["value"]
        related = [
            c
            for c in classifications
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
                            f"Unresolved splash material overlaps {entity}.{predicate}"
                        ),
                    }
                )
            splash_value = item.get("value")
            uses_splash_value = not _incompatible(splash_value, value)
            if cls == "CONTRADICTORY" and uses_splash_value:
                if established_claim:
                    findings.append(
                        {
                            "class": "CX-SPLASH-CONFLICT",
                            "severity": "stop",
                            "summary": (
                                f"Would establish splash {entity}.{predicate}="
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
                                f"Splash storyline uses contradictory "
                                f"{entity}.{predicate}; do not present as "
                                f"established canon"
                            ),
                        }
                    )
            if cls in NON_ESTABLISHED_SPLASH:
                if established_claim:
                    findings.append(
                        {
                            "class": "CX-SPLASH-PROPOSED",
                            "severity": "stop",
                            "summary": (
                                f"Request treats splash {cls} {entity}.{predicate} "
                                f"as established canon"
                            ),
                        }
                    )
                elif continue_splash:
                    findings.append(
                        {
                            "class": "CX-EXPANSION",
                            "severity": "warn",
                            "summary": (
                                f"Splash {cls} {entity}.{predicate} used as "
                                f"authoring context, not established canon"
                            ),
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
        "splash_classifications": classifications,
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
    }
    for item in (state.get("splash_classifications") or []):
        if item.get("class") == "CONTRADICTORY":
            contract["forbidden_assumptions"].append(
                f"conflict: splash {item.get('entity')}.{item.get('predicate')}="
                f"{item.get('value')!r} vs main — classified, not silently resolved"
            )
    report["contract_id"] = contract["contract_id"]
    return contract


def _contract_source_status(state: dict) -> dict:
    bands = {k: [] for k in CONTRACT_BANDS}
    for fact in state.get("facts") or []:
        bands["CANONICAL"].append(
            {
                "entity": fact.get("entity"),
                "predicate": fact.get("predicate"),
                "value": fact.get("value"),
                "class": "CONFIRMED_CANON",
                "source": fact.get("source"),
            }
        )
    for item in state.get("splash_classifications") or []:
        cls = item.get("class")
        payload = {
            "entity": item.get("entity"),
            "predicate": item.get("predicate"),
            "value": item.get("value"),
            "class": cls,
            "source": item.get("source"),
        }
        if cls == "CONFIRMED_CANON":
            continue
        if cls == "CANON_CLARIFICATION":
            bands["CANON_CLARIFICATION"].append(payload)
        elif cls == "AUTHORIAL_INTENT":
            bands["AUTHORIAL_INTENT"].append(payload)
        elif cls in (
            "PROPOSED_CANON",
            "CANON_EXTENSION",
            "DEVELOPMENTAL",
            "EXPLORATORY",
        ):
            bands["PROPOSED"].append(payload)
        elif cls in ("CONTRADICTORY", "UNRESOLVED"):
            bands["CONFLICT"].append(payload)
    return bands


def run(
    request: dict,
    branch_name: str,
    branch: dict,
    *,
    live_heads: dict | None = None,
    splash: dict | None = None,
) -> dict:
    state = build_canon_state(branch_name, branch)
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
