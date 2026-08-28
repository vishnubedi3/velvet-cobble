# 05 — Processing Pipeline

The pipeline implements the loop
`Generate → Analyze → Detect → Cause → Prioritize → Intervene → Re-evaluate →
Preserve or reject`, with the escalation discipline of
`../interventions/01-intervention-hierarchy.md`.

## Stage 0 — Intake

1. Validate `SkillInput` (`../spec/03-input-schema.md`).
2. Record generator metadata; select baselines (internal / corpus /
   uncalibrated).
3. If `length_words ≥ long_form_threshold`: enable frameworks/06.

## Stage 1 — Analyze (Pass A + B + C)

1. **Pass A — contract.** Genre/subgenre gate (frameworks/07), narration
   contract, intent fields, declared devices, content boundaries.
2. **Pass B — surface scan.** Framework detectors in the cheap-first order
   (frameworks/01 §2: repetition → explicitness → continuity → uniformity →
   template).
3. **Pass C — evidence + intent.** Attach evidence/confidence/cause to each
   candidate; run the function test; run the intentionality check
   (`../interventions/02-preservation-constraints.md` §3). Unsupported candidates → Observations.

## Stage 2 — Prioritize

Score findings (`../spec/06-scoring.md`); sort; drop below-threshold items
into Observations; emit the intervention queue.

## Stage 3 — Intervene (level-ordered, draft-wide)

1. **Level 1 pass** (whole draft) → apply → re-analyze changed spans only.
2. **Level 2 pass** → apply → re-analyze.
3. **Level 3 pass** → apply → re-analyze.
4. **Level ≥4 batch gate.** Collect all remaining structural proposals;
   run causality audits; group interacting proposals (same causal chain);
   author-gate worldview-touching changes; apply batch; re-analyze.
5. After every level: re-run the **Level 0 re-check**
   (`../interventions/01-intervention-hierarchy.md` §2.4) — previously preserved patterns may now be
   redundant, and applied fixes may need reversion.

## Stage 4 — Re-evaluate (per applied edit / batch)

1. Preservation checks (all 14) on the changed span — simulate against the
   StoryModel before apply, verify after.
2. Tell re-check: did the targeted cause disappear? Did a new tell appear
   (new-artifact rule)?
3. Ledger diffs (frameworks/06): continuity, timeline, information state.
4. Any failure → automatic revert, logged.

## Stage 5 — Report

Emit `SkillReport` (`../spec/04-output-schema.md`): analysis, intervention log
with rejections, revised draft, updated StoryModel, summary.

## Ordering invariants (testable properties)

- **I-1.** No Level k+1 edit is applied before all Level ≤k candidates have
  been applied or rejected-with-reason.
- **I-2.** Every applied edit has a logged preservation result for all 14
  dimensions.
- **I-3.** Every rejected edit cites the violated constraint.
- **I-4.** The revised draft, when re-analyzed, has no *new* high-confidence
  findings introduced by edits (violations → revert).
- **I-5.** Analysis-only runs (max level 0) never mutate the draft.
- **I-6.** The pipeline is idempotent-ish: a second run on the revised draft
  applies no Level ≥3 edits unless the author changed intent fields (Level
  1–2 findings may re-trigger if thresholds changed; they must re-pass
  evidence).

## Concurrency & state

- The pipeline is sequential by design (each stage consumes the previous
  stage's output). Parallelism is allowed *within* a stage (findings are
  independent; intervention batches are independent after causal grouping).
- State (Draft + StoryModel + logs) is explicit and versioned; every stage
  reads the previous version and writes the next.
