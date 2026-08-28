# DECISION_PROTOCOL.md

The decision is a function of findings plus request intent. Hosts must not "upgrade" a BLOCK to PASS because generation is desired.

---

## 1. Inputs

- `GenerationRequest`
- `CanonState` (fresh)
- `Finding[]` typed by [`CONFLICT_TAXONOMY.md`](CONFLICT_TAXONOMY.md)

If the Canon State is stale relative to the repo at evaluation time, do not decide; re-resolve.

---

## 2. Precedence (first match wins)

1. **Host/error** (cannot read refs or required sources) → do not emit a canon decision; emit a host error.
2. **CX-DIVERGENCE** (non-splash unnamed live head) → `REQUIRES_CLARIFICATION`. Extra `arena/*` heads are **not** this class; they are classified against `main`.
3. **CX-AMBIGUITY** including live Splash that was not inspected, or unresolved Splash overlapping the request → `REQUIRES_CLARIFICATION`.
4. **CX-SPLASH-CONFLICT** (severity `stop`: would establish Splash over `main`) or **CX-SPLASH-PROPOSED** (treating proposed/developmental Splash as established) → `REQUIRES_CLARIFICATION`. Warn-level Splash conflict → later `PASS_WITH_WARNINGS`.
5. **CX-BRANCH** (kind forbidden on this branch, e.g. narrative while the live charter forbids it — Splash charter applies only when continuing a Splash storyline) → `BLOCK`.
6. Request has `explicit_canon_change: true` **or** finding `CX-CHANGE-INTENT` → `CANON_CHANGE_REQUIRED` (even if other conflicts exist; the change protocol then lists them).
7. **CX-ADMISSION** (using draft as canon) → `BLOCK`.
8. **CX-MYSTERY** or **CX-NOT-READY** or **CX-HIGH-IMPACT-SMUGGLE** or **CX-RETIRED** → `BLOCK`.
9. **CX-DIRECT** / **CX-INDIRECT** / **CX-TEMPORAL** / **CX-KNOWLEDGE** / **CX-CAUSAL** → `BLOCK`.
10. **CX-UNRESOLVED-REGISTER** intersecting the request → `REQUIRES_CLARIFICATION`.
11. **CX-AUTHORITY** (unclear citation) → `REQUIRES_CLARIFICATION`.
12. **CX-WORKING-DIRECTION** (ignore or diverge from current Arena development) → `PASS_WITH_WARNINGS`. Not a BLOCK.
13. Warnings only (OPEN narrative-detail fill, classified Arena conflict that does not replace `main`, provisional working material, WORLD-MODEL lagging its files, permitted expansion) → `PASS_WITH_WARNINGS`.
14. No findings → `PASS`.

`CX-STALE` is handled before this table by re-verification. A stale contract is never itself a PASS.

---

## 3. Meaning of each decision

**PASS.** Compatible with the applicable Canon State. Emit a Generation Contract. Generation may proceed **only** inside that contract. Future requests must re-verify.

**PASS_WITH_WARNINGS.** Same, plus the contract's `warnings`, `uncertainties`, and `source_status` bands are binding. Typical warnings: filling an OPEN narrative-detail question; classified Splash conflict while `main` remains baseline; continuing a Splash storyline with developmental material that must not be presented as established canon.

**REQUIRES_CLARIFICATION.** Stop. Inspect unclassified Splash, resolve unresolved Splash overlapping the request, refuse to treat proposed Splash as established, resolve a register mismatch, or supply missing story-time. Do not generate. Do not guess Splash into canon.

**BLOCK.** Stop. Report the conflicting sources (branch, document, location, hash). Do not generate. Do not "fix" the world to make the request true.

**CANON_CHANGE_REQUIRED.** Stop generation. Open [`CANON_CHANGE_PROTOCOL.md`](CANON_CHANGE_PROTOCOL.md). Identify affected canon, dependents, local vs systemic scope. Require the project's changelog + dependency-sweep mechanism.

---

## 4. PASS is time-stamped

Record:

- `canon_state_id`
- branch + commit(s)
- contributing content hashes
- decision
- timestamp

Anyone may later ask: "why did this pass?" The answer is the audit record, not a new opinion.

---

## 5. Re-decision after source change

When sources change, **previous decisions are not updated in place**. They become historical. The next request produces a new decision. Tests must show both directions:

- a prior PASS becoming BLOCK
- a prior BLOCK becoming PASS after an authorized canon change
