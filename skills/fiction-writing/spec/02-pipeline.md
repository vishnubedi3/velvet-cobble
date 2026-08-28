# 02 — Pipeline

Normative order. Skipping a stage is a failed run, not a shortcut.

---

## Stage 0 — Request intake

Normalize a `GenerationRequest`. If `generation_kind` is missing, infer only if unambiguous; else `REQUIRES_CLARIFICATION`.

Kinds this project actually produces: `narrative`, `worldbuilding`, `canon_change`, `question_resolution`, `revision`, `historical_audit`.

---

## Stage 1 — Branch context

`resolve_branches`. Record heads, recovery tags. Treat `main` as the canonical baseline. If Arena Splash (`arena/*`) is live, inspect and classify it against `main` — do not mix facts, do not skip Splash.

Invariant **I-1:** verification never unions Splash facts into `main`. Uninspected live Splash is a stop, not a silent pass.

---

## Stage 2 — Canon resolution

`resolve_canon`. Inventory, hash, select relevant subset, extract constraints, bind provenance.

Invariant **I-2:** every constraint has `(branch, path, hash)`.

Invariant **I-3:** RESEARCH / HYPOTHESIS / DRAFT / ANALYSIS are never marked CANON.

---

## Stage 3 — Verification

Run checks 6–13 from [`../SKILL.md`](../SKILL.md) §5. Emit typed findings.

Invariant **I-4:** story-time and repository-time are not substituted for each other.

---

## Stage 4 — Decision

[`../DECISION_PROTOCOL.md`](../DECISION_PROTOCOL.md).

Invariant **I-5:** BLOCK / REQUIRES_CLARIFICATION / CANON_CHANGE_REQUIRED never emit a contract.

---

## Stage 5 — Contract or stop

If permitted, compact contract. Persist the verification report.

Invariant **I-6:** the contract's `canon_state_id` equals the report's.

---

## Stage 6 — (outside the skill) Generation

Only after PASS / PASS_WITH_WARNINGS. The generator is not this skill.

---

## Stage 7 — (outside the skill) Admission

[`../CANON_ADMISSION_PROTOCOL.md`](../CANON_ADMISSION_PROTOCOL.md).

---

## Stage 8 — Next time

Detect changes. Invalidate. Do not reuse Stage 4's decision.

Invariant **I-7:** every new request starts at Stage 0.
