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
2. **CX-DIVERGENCE** or unchosen applicable branch → `REQUIRES_CLARIFICATION`.
3. **CX-BRANCH** (kind forbidden on this branch, e.g. narrative while the live charter forbids it) → `BLOCK`.
4. Request has `explicit_canon_change: true` **or** finding `CX-CHANGE-INTENT` → `CANON_CHANGE_REQUIRED` (even if other conflicts exist; the change protocol then lists them).
5. **CX-ADMISSION** (using draft as canon) → `BLOCK`.
6. **CX-MYSTERY** or **CX-NOT-READY** or **CX-HIGH-IMPACT-SMUGGLE** or **CX-RETIRED** → `BLOCK`.
7. **CX-DIRECT** / **CX-INDIRECT** / **CX-TEMPORAL** / **CX-KNOWLEDGE** / **CX-CAUSAL** → `BLOCK`.
8. **CX-UNRESOLVED-REGISTER** intersecting the request → `REQUIRES_CLARIFICATION`.
9. **CX-AMBIGUITY** or **CX-AUTHORITY** (unclear citation) → `REQUIRES_CLARIFICATION`.
10. Warnings only (OPEN narrative-detail fill, non-exhaustive sources, WORLD-MODEL lagging its files, permitted expansion) → `PASS_WITH_WARNINGS`.
11. No findings → `PASS`.

`CX-STALE` is handled before this table by re-verification. A stale contract is never itself a PASS.

---

## 3. Meaning of each decision

**PASS.** Compatible with the applicable Canon State. Emit a Generation Contract. Generation may proceed **only** inside that contract. Future requests must re-verify.

**PASS_WITH_WARNINGS.** Same, plus the contract's `warnings` and `uncertainties` are binding. Typical warnings on this project: filling an OPEN narrative-detail question; using a name that must later be admitted to a pool; drawing on a mystery as *atmosphere* without resolving it.

**REQUIRES_CLARIFICATION.** Stop. Ask the user / host to choose a branch, resolve a register mismatch, or supply missing story-time. Do not generate.

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
