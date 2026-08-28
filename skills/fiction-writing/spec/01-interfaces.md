# 01 — Portable interfaces

The skill is a data-transform pipeline. No vendor APIs.

---

## 1. Functions

```
resolve_branches(repo_view) -> BranchContext
resolve_canon(branch_context, request) -> CanonState
verify(request, canon_state) -> VerificationReport
decide(report) -> Decision
contract(request, canon_state, report) -> GenerationContract | null
detect_changes(prev: CanonState, next: CanonState) -> ChangeSet
invalidate(derived_index, change_set) -> InvalidationReport
admit(proposal, workflow_result) -> AdmissionRecord
```

Same inputs → same outputs for the deterministic core. LLM extraction is optional and must be validated.

---

## 2. Host capabilities

Required:

- read current Git refs and file contents at a commit (or an equivalent snapshot API)
- persist verification reports

Optional:

- `llm(contract, input_json) -> output_json`

---

## 3. Prompt contracts (optional LLM)

### C-CG-01 `request-analyze`

- In: raw generation request + generation kind.
- Out: structured `GenerationRequest` (claims, story-time, viewpoint, explicit_canon_change).
- Quality: every claim is quoted or clearly implied; no extra world facts.
- Fallback: if claims cannot be structured, `REQUIRES_CLARIFICATION`.

### C-CG-02 `constraint-extract`

- In: relevant source documents (excerpts) + request.
- Out: constraint list with provenance (path, section, hash).
- Quality: every constraint cites a span; no constraint without a hash; no RESEARCH/HYPOTHESIS marked as CANON.
- Fallback: drop uncited constraints.

### C-CG-03 `consistency-read`

- In: claims + constraints + dependency graph.
- Out: candidate findings with class IDs from the taxonomy.
- Quality: class ID required; evidence span required.
- Fallback: candidates without evidence become non-blocking observations.

### C-CG-04 `contract-compact`

- In: PASS/PASS_WITH_WARNINGS report + Canon State identity.
- Out: compact Generation Contract.
- Quality: every `must_remain_unchanged` item has provenance; no unsourced world-law list.
- Fallback: omit unsourced fields; if `must_remain_unchanged` would be empty despite findings of constraints, fail closed (no contract).

Temperature: as low as the host allows. Validators are code, not a second model vote.

---

## 4. Schemas

- [`../schemas/generation-request.schema.json`](../schemas/generation-request.schema.json)
- [`../schemas/canon-state.schema.json`](../schemas/canon-state.schema.json)
- [`../schemas/verification-report.schema.json`](../schemas/verification-report.schema.json)
- [`../schemas/generation-contract.schema.json`](../schemas/generation-contract.schema.json)
- [`../schemas/canon-change-proposal.schema.json`](../schemas/canon-change-proposal.schema.json)
- [`../schemas/admission-record.schema.json`](../schemas/admission-record.schema.json)
