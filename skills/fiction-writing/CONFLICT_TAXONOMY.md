# CONFLICT_TAXONOMY.md

Findings are typed. Severity is not a vibe: it is the decision-protocol input.

---

## 1. Classes

| ID | Class | Typical decision |
|---|---|---|
| **CX-DIRECT** | Claim contradicts an applicable CANON fact at overlapping story-time | BLOCK |
| **CX-INDIRECT** | Claim contradicts a dependent / entailed fact (including negative space) | BLOCK |
| **CX-TEMPORAL** | Claim is at the wrong story-time (dead then alive, institution not yet founded, era mismatch, order vs exact-date mixup) | BLOCK |
| **CX-KNOWLEDGE** | Viewpoint entity acts on facts it has not acquired by that story-time; or author-level truth is treated as in-world knowledge | BLOCK |
| **CX-CAUSAL** | Claim breaks a recorded causal chain (effect without cause; winner/loser inversion; precluded consequence) | BLOCK |
| **CX-MYSTERY** | Claim would resolve an INTENTIONALLY UNRESOLVED question | BLOCK |
| **CX-NOT-READY** | Claim would invent an answer currently marked NOT READY | BLOCK |
| **CX-HIGH-IMPACT-SMUGGLE** | Narrative or draft introduces a new high-impact fact (geography, law, succession, currency, core religion, calendar, world-law) | BLOCK (send to worldbuilding + change protocol) |
| **CX-AUTHORITY** | Claim cites RESEARCH / HYPOTHESIS / DRAFT / WORLD-MODEL as if CANON | BLOCK or REQUIRES_CLARIFICATION |
| **CX-BRANCH** | Request violates a live charter constraint on the applicable branch (e.g. narrative not authorized), or mixes diverged branches | BLOCK or REQUIRES_CLARIFICATION |
| **CX-DIVERGENCE** | Non-splash unnamed live head with material difference; applicable branch not chosen | REQUIRES_CLARIFICATION (not used merely because `arena/*` exists) |
| **CX-SPLASH-CONFLICT** | Arena Splash statement contradicts established `main` at overlapping story-time | Warn if `main` remains baseline; `REQUIRES_CLARIFICATION` if the request would *establish* Splash over `main` |
| **CX-SPLASH-PROPOSED** | Request treats proposed / developmental / exploratory / intent Splash as established canon | REQUIRES_CLARIFICATION |
| **CX-AMBIGUITY** | Insufficient reliable information; register vs file disagreement; missing dependency | REQUIRES_CLARIFICATION |
| **CX-UNRESOLVED-REGISTER** | Active item in `CONTRADICTIONS.md` intersects the request | REQUIRES_CLARIFICATION (unless the request is specifically to resolve it via the change protocol) |
| **CX-STALE** | Evaluation or contract is bound to a Canon State whose hashes no longer match | Re-verify; do not honor the old PASS |
| **CX-ADMISSION** | Treating unadmitted generated material as CANON | BLOCK (contamination) |
| **CX-RETIRED** | Citing RETIRED canon as live | BLOCK |
| **CX-EXPANSION** | New compatible information | Not a conflict — permitted creative space |
| **CX-CHANGE-INTENT** | User explicitly wants an incompatible outcome | CANON_CHANGE_REQUIRED |

Near-misses that are **not** conflicts (this project's own audit practice):

- A range source containing a later exact date (exact is a refinement inside the range).
- A non-exhaustive table omitting a name established elsewhere, if the table does not claim exhaustiveness.
- Cosmetic staleness of a lower-bound phrase that remains true.
- Summary-vs-file disagreement **after** the file is taken as winner — still log it as a **process finding** (update-the-summary), not as two equal facts.

---

## 2. Direct vs. indirect

**Direct:** same entity, same predicate, incompatible values, overlapping story-time.

**Indirect:** the claim forces a dependent to be false (dependency graph, recorded consequences, negative space "this did not happen", integration-cost style non-events).

---

## 3. Temporal vs. knowledge vs. causal

These are easy to collapse and must not be:

- **Temporal:** the world-state at story-time S.
- **Knowledge:** who knows what at S (and at which epistemic layer).
- **Causal:** why S is possible.

A character can be alive at S (temporal PASS) and still not know a fact established at S (knowledge BLOCK). A later-repo chapter can narrate S without moving later story-time knowledge backward.

---

## 4. Ambiguity vs. mystery vs. missing information

| | Meaning | Guard behavior |
|---|---|---|
| Deliberate mystery | INTENTIONALLY UNRESOLVED | Must remain unresolved |
| NOT READY | Stewardship: leave untouched | Do not invent |
| OPEN narrative detail | May be filled in drafts | PASS_WITH_WARNINGS; not canon until admitted |
| Missing information | Should exist but doesn't | REQUIRES_CLARIFICATION |
| Genuine contradiction | Two CANON claims collide | Unresolved-register or BLOCK; never silently pick |

---

## 5. Branch conflicts are not world conflicts

Two session branches disagreeing is **not** automatically **CX-DIRECT**. CX-DIRECT is evaluated *inside* the `main` Canon State (the baseline).

Arena Splash vs `main` is **classification**, not a merge and not a dismissal:

- compatible restatement → `CONFIRMED_CANON`
- compatible explanation → `CANON_CLARIFICATION`
- incompatible claim → `CONTRADICTORY` / `CX-SPLASH-CONFLICT` (do not silently pick Splash because it is newer)
- extra `arena/*` head, unclassified → `CX-AMBIGUITY` (inspect it)
- extra `arena/*` head, classified as clarification → not a stop

See [`BRANCH_RELATIONSHIP.md`](BRANCH_RELATIONSHIP.md).
