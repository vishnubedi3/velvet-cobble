# CONFIG — Configuration Definitions

The skill has exactly one configuration surface: the parameters below. Every
parameter mentioned anywhere in the skill resolves to this file. Where a
spec document states a number, that number is a **default** — the parameter
lives here, and overrides come only through `analysis_options` in the
`SkillInput` ([`spec/03-input-schema.md`](spec/03-input-schema.md) §4),
which are validated against the ranges below.

## 1. Analysis options (author-facing)

Set per run via `analysis_options`; defaults when absent:

| Parameter | Default | Range | Meaning |
|---|---|---|---|
| `max_intervention_level` | `6` | 0–6 | Highest intervention level permitted this run. `0` = analysis-only (draft never mutated). |
| `confidence_floor_for_action` | `medium` | high / medium / low / none | Minimum tell confidence for any action. `low` findings are report-only unless raised deliberately. |
| `batch_gate` | `true` | bool | Level ≥4 edits are collected and reviewed together before application. |
| `author_gate` | `true` | bool | Worldview-touching edits (N07/F03/E05/F05 class) require explicit author consent. |
| `long_form_threshold_words` | `10000` | integer | Drafts ≥ this length enable the long-form framework ([`frameworks/06-long-form-consistency.md`](frameworks/06-long-form-consistency.md)). |
| `baseline_source` | `auto` | auto / internal / corpus | Which baselines uniformity/explicitness are measured against ([`glossary.md`](glossary.md) §"baseline"). |

## 2. Scoring parameters ([`spec/06-scoring.md`](spec/06-scoring.md))

| Parameter | Default | Meaning |
|---|---|---|
| `confidence_weight.high` | `1.0` | multiplier for High-confidence findings |
| `confidence_weight.medium` | `0.6` | multiplier for Medium-confidence findings |
| `confidence_weight.low` | `0.2` | multiplier for Low-confidence findings (report-only by default) |
| `function_loss` | 0–1 | 1 = passage does no work; 0.3 = partially redundant; 0 = does work (→ Observation). Not a tunable constant; computed by the function test. |
| `false_positive_penalty` | 0 / 0.3 / 0.6 | maps from taxonomy false-positive risk 1 / 2 / 3 |
| `intent_protection` | 0 / 0.5 / ∞ | 0 = no intent match; 0.5 = possible device (caps level); ∞ = declared device → Observation |
| `queue_threshold` | `1.2` | priority floor for the intervention queue (priority range −0.6…3.0). Lowering below 0.8 is discouraged (false-positive-dominated region). |
| `edit_budget_warning` | `8%` | median chars changed per 1k words (metric M3). Not a quota; a review trigger for outliers. |

## 3. Calibration keys ([`spec/12-advanced-architecture.md`](spec/12-advanced-architecture.md) §4)

Per-generator baselines are stored under the key
`(model_family, decoding_settings_hash, genre)` with values:

- repetition thresholds (near-duplicate similarity, skeleton-cluster distance);
- uniformity thresholds (sentence-length variance percentiles);
- explicitness thresholds (interpretation-statement density, emotion-label density);
- register baselines (formality/nominalization counts).

When no key matches, the run is `uncalibrated`: conservative defaults apply and
edits are capped at Level 3 ([`spec/06-scoring.md`](spec/06-scoring.md) §4).
A conformant implementation must expose the calibration store as config
(storage location, TTL, and re-baseline trigger on generator version change).

## 4. Lexicon configuration

All lexicon-based detectors (emotion labels, hedge density, sensory
vocabulary, signpost phrases) are parameterized per language:

| Parameter | Default | Meaning |
|---|---|---|
| `lexicons.language` | `en` | Lexicon set to load. Non-`en` runs without a retuned lexicon are marked `uncalibrated` (findings capped, flagged). |
| `lexicons.path` | `<impl-defined>` | Where the implementation keeps lexicon files. This repository ships **no** word lists: the taxonomy bans list-based detection, so lexicons must be built from the taxonomy's documented behavioral patterns, not imported. |

## 5. Prompt-contract parameters ([`spec/02-api-interface.md`](spec/02-api-interface.md) §3)

| Parameter | Default | Meaning |
|---|---|---|
| `llm.temperature.analysis` | `0.0–0.2` | analysis contracts (C-01, C-02, C-04) |
| `llm.temperature.reconstruction` | `0.6–0.9` | Level 3–6 edit contracts (C-03) |
| `llm.max_output_tokens` | implementation-defined | JSON outputs must fit; schema-repair retries = 1 |
| `knowledge.load_strategy` | `per-finding` | full / per-finding / index-only ([`spec/12-advanced-architecture.md`](spec/12-advanced-architecture.md) §1) |

## 6. Pipeline parameters ([`spec/05-pipeline.md`](spec/05-pipeline.md))

| Parameter | Default | Meaning |
|---|---|---|
| `chunk_size_words` | `3500` | analysis chunking for C-02 (aggregation call stitches chunk results) |
| `max_parallel_findings` | unbounded | findings are independent; causal-grouped intervention batches stay sequential |
| `revert_on_postcheck_failure` | `true` | automatic revert when post-edit checks fail (must be `true` for conformance) |

## 7. Validation rules

1. Overrides must be in-range (table above); out-of-range values are
   `input_rejection`s, never clamped silently.
2. `max_intervention_level: 0` must make the pipeline byte-preserving
   (invariant I-5).
3. `author_gate: false` does **not** disable the genre gate or the
   preservation constraints; it only removes the *additional* consent step
   for worldview-touching edits. Setting it false is discouraged.
4. `confidence_floor_for_action: none` does **not** make Folklore items
   actionable — Folklore is a tier, not a confidence level, and is
   permanently non-actionable ([`research/02-evidence-hierarchy.md`](research/02-evidence-hierarchy.md) §2.3.5).

## 8. What is deliberately NOT configurable

- The preservation dimensions PV-1…PV-14 and the rejection rule
  ([`interventions/02-preservation-constraints.md`](interventions/02-preservation-constraints.md)) — they are the skill's safety contract.
- The intervention level *definitions* and escalation rules
  ([`interventions/01-intervention-hierarchy.md`](interventions/01-intervention-hierarchy.md)).
- Detector scores as an input — excluded by design ([`spec/07-failure-modes.md`](spec/07-failure-modes.md) F-4).
- Error insertion / randomization — hard-excluded ([`interventions/02-preservation-constraints.md`](interventions/02-preservation-constraints.md) §7).
- The Pass A narrative-voice-baseline capture and the final read FR-1…FR-8
  ([`spec/05-pipeline.md`](spec/05-pipeline.md) Stage 4b) — they are the skill's
  preservation substrate and self-check, not tuning surfaces; a run cannot
  disable them.
- The correction laws "the right word repeated is correct" (no cosmetic-variation
  fixes) and the kicker rule (no upgraded closing aphorisms)
  ([`frameworks/01-detection.md`](frameworks/01-detection.md) §2, [`frameworks/05-narrative-analysis.md`](frameworks/05-narrative-analysis.md) §3).
- **The project binding and the supremacy laws** — Stage 0 validation, Pass
  B0, the PST score floor and queue priority, and
  [`interventions/02-preservation-constraints.md`](interventions/02-preservation-constraints.md)
  §8 are structural to the skill ([`spec/01-project-binding.md`](spec/01-project-binding.md)):
  no configuration value can unbind the skill from Samur, disable the
  project-tell scan, let an empirical fix outrank a project finding, or
  permit a canon-editing intervention.
