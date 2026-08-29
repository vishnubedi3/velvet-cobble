# 12 — Advanced Implementation Architecture

**Goal.** Full-fidelity implementation: complete taxonomy, calibrated
baselines, long-form state, structural interventions, and measurable
evaluation.

## Component map

```
[Intake]  SkillInput → validators → calibration selection
[Analyze] C-01 story-model (full) → C-02 tell-detect (full taxonomy, RAG)
          → deterministic framework checks (repetition, ledgers, arcs,
             voice profiles, skeleton clustering)
[Score]   priority model (06-scoring.md) → queue
[Fix]     C-03 per-level contracts L1..L6 → causality audit engine →
          batch gate → author gate
[Verify]  C-04 reevaluate → ledger diff engine → revert engine →
          final read (FR-1..FR-7) over the whole revised draft
[Report]  SkillReport + what-changed list + benchmark metrics
```

## 1. Knowledge layer (RAG over this repository)

- Index: taxonomy cluster files, frameworks, interventions, research
  synthesis, source index — chunked with per-chunk metadata (tell IDs,
  confidence, K-codes).
- Retrieval per finding: tell ID + cluster + genre → the exact
  documentation the LLM needs (no need to hold everything in context).
- Version pinning: taxonomy/schemas versioned; findings record the version
  they were computed against.

## 2. Deterministic analysis engines (code, not LLM)

| Engine | Implements |
|---|---|
| Near-duplicate finder | L02/L08/L10 (n-gram + embedding clusters); construction-level clustering for the variation audit's cosmetic-variation class (P02/P04/SC05) and referent-coreference detection for its referent class (P01) (frameworks/01 §2 Pass B) |
| Sentence/register statistics | P01/P03/P04/P07, V06 (length variance, nominalization density, register contrast vs. internal baseline) |
| Ledger engines (facts, timeline, world rules, reader-information) | L04/L05/L09, A02/A03, PV-7/PV-10 checks |
| Scene segmentation + skeleton clustering | SC01–SC05, T01, L03, N05 |
| Valence arc plotter | N08, E05 (hedonometer-style, S08 method) |
| Voice profiler | D04/C03/H03, L01 (feature extraction per speaker/chapter) |
| Emotion/explicitness tagger | C01/E01–E02/U01–U04 (lexicon + pattern rules, parameterized per language) |
| Stereotype auditor | C07 (S07-style markedness comparison on the draft's own characters) |

The LLM contracts then consume engine outputs as structured evidence
(faster, cheaper, and — critically — objective, satisfying the
"no verdict without evidence" rule).

## 3. Intervention engine

- Per-level contracts as in `../interventions/01-intervention-hierarchy.md`; the LLM receives the
  finding + engine evidence + story-model neighborhood (not the whole
  draft).
- **Causality audit engine:** event-graph diff (frameworks/05 §4) before
  any Level ≥4 apply.
- **Batch gate:** structural proposals grouped by shared causal chains;
  solved jointly (multiple LLM passes allowed) so interacting edits don't
  conflict.
- **Author gate:** worldview/content-class edits (N07/F03/E05/F05) are
  emitted as proposals with the analysis attached; zero auto-apply.

## 4. Calibration subsystem

- Per-generator baselines (taxonomy/17 §17.3): maintain a small
  calibration corpus per model family + decoding setting (benchmark/README
  §Corpus); thresholds stored per (family, decoding, genre) key.
- `uncalibrated` handling: conservative defaults + Level ≤3 cap + flagged
  findings.
- Calibration drift monitor: re-baseline when generator versions change.

## 5. Long-form subsystem

- Story-state store (the full story model, versioned per chapter).
- Segment conditioning for generation-time prevention (frameworks/06 §4) —
  optionally upstream of the skill proper (the skill can *emit* the state
  summaries for the generator to consume on continuation).
- Post-pass audits: all ledgers + skeleton clustering + diversity curves
  (frameworks/06 §3).

## 6. Evaluation harness

- Benchmark runner (09-evaluation-benchmark.md + ../benchmark/): seeded cases, traps, genre
  matrix, human-control cases; metrics A1–A7, P1–P5, M1–M4.
- Human rating pipeline for P5 (blind pairs, ≥2 raters, rubric).
- Regression gate: implementation releases must pass M1 (adversarial
  suite) and maintain P1–P4 at 100% on the case suite.

## 7. Hardening

- Prompt-injection defense: the draft is data, never instructions; all
  contracts treat draft text as untrusted content (explicit in the
  contracts).
- Reversibility: every applied edit carries a byte-level revert.
- Audit log: full InterventionLog persisted per run (04-output-schema.md).
