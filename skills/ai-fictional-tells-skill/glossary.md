# Glossary — Canonical Terminology

Terms must be used consistently across every file in this folder. When two
files disagree, this file wins; flag the disagreement via
[`tests/02-static-consistency-checklist.md`](tests/02-static-consistency-checklist.md) T-6.

## 1. The pipeline

| Term | Definition |
|---|---|
| **Skill** | The whole artifact in this folder: research + taxonomy + frameworks + interventions + spec + schemas + tests + examples. |
| **SkillInput** | The top-level input object ([`spec/03-input-schema.md`](spec/03-input-schema.md); schema [`schemas/skill-input.schema.json`](schemas/skill-input.schema.json)). |
| **SkillReport** | The top-level output object ([`spec/04-output-schema.md`](spec/04-output-schema.md)). |
| **AnalysisReport** | The Analyze-stage output: contract, story model, findings, observations, calibration, priority queue. |
| **Finding** | One evidence-bound candidate artifact: tell IDs, spans, pattern evidence, confidence, cause, function test, intentionality, proposed level. Actionable. |
| **Observation** | A candidate that is not actionable (`low_confidence`, `folklore`, `intentional`, `contractual`, `uncalibrated`, `below_threshold`). Reported, never edited. |
| **Pass A / B / C / D** | Contract extraction / surface scan / evidence & intent / prioritization — the four detection passes ([`frameworks/01-detection.md`](frameworks/01-detection.md) §2). |
| **Stage 0–5** | Pipeline stages: intake / analyze / prioritize / intervene / re-evaluate / report ([`spec/05-pipeline.md`](spec/05-pipeline.md)). |
| **Intervention queue** | The prioritized, cause-clustered list of findings selected for intervention (type name `InterventionQueue` in [`spec/02-api-interface.md`](spec/02-api-interface.md) §2 refers to exactly this). |
| **InterventionLog** | The applied/rejected edit trace ([`spec/04-output-schema.md`](spec/04-output-schema.md) §3). |

## 2. Interventions

| Term | Definition |
|---|---|
| **Level 0–6** | No intervention / redundant wording / unnecessary exposition / dialogue differentiation & local specificity / repetitive structures / sentence-paragraph reconstruction / scene reconstruction ([`interventions/01-intervention-hierarchy.md`](interventions/01-intervention-hierarchy.md) §1). |
| **Escalation** | Moving a finding to a higher level; requires written evidence of lower-level insufficiency (never done mechanically). |
| **Function test** | The taxonomy/20 contrast test asking what deliberate work a passage does; failing it is a precondition for intervention. |
| **Intentionality check** | The three-step test (author intent → story-model consistency → function test) that separates deliberate choice from accidental artifact; undetermined → preserve. |
| **Genre gate** | The contract check every flag must pass before any intervention ([`frameworks/07-genre-awareness.md`](frameworks/07-genre-awareness.md) §2). |
| **Causality audit** | Event-graph before/after comparison required for all Level ≥4 edits ([`frameworks/05-narrative-analysis.md`](frameworks/05-narrative-analysis.md) §4). |
| **Re-evaluation** | Post-edit re-check: preservation dimensions, tell detectors on the changed span, ledger diffs. Failures auto-revert. |

## 3. Preservation

| Term | Definition |
|---|---|
| **PV-1…PV-14** | The fourteen preservation dimensions: plot, character, character voice, narrative voice, setting, world rules, timeline, point of view, emotional trajectory, information availability, tone, genre, thematic intent, stylistic intent ([`interventions/02-preservation-constraints.md`](interventions/02-preservation-constraints.md) §1). Written "PV-1", never "dimension 1". |
| **Rejection rule** | An edit is applied only if all PV dimensions pass (or an author-approved trade-off is logged). |
| **New-artifact rule** | Reject any edit that introduces another documented tell. |
| **Churn rule** | Reject edits whose only measurable effect is text churn. |
| **Hard exclusions** | Error insertion, randomization, synonym swapping, detector-score-driven edits, provenance removal — never permissible. |
| **Author gate** | Extra consent step for worldview/content-class edits (N07, F03, E05, F05). |
| **Batch gate** | Level ≥4 proposals collected and reviewed together (causal interactions). |

## 4. Story model ([`interventions/03-story-model.md`](interventions/03-story-model.md))

| Term | Definition |
|---|---|
| **Story model** | The descriptive structural representation of the draft (characters, facts, timeline, events, scenes, information state, themes, motifs, foreshadowing, conflicts, world rules, perspective, emotional state). Descriptive only — never prescriptive. |
| **Ledger** | A specific extractable register of the story model: fact ledger, timeline ledger, world-rule ledger, character-state ledger, voice ledger, scene-type ledger, motif register, reader-information register, setup/payoff ledger. |
| **`unknown` field** | A story-model field the draft does not establish. Implementations must never invent content for it. |

## 5. Evidence

| Term | Definition |
|---|---|
| **Tier 0–4** | Evidence tiers: fiction-specific empirical / adjacent empirical / mechanisms & benchmarks / practitioner / folklore ([`research/02-evidence-hierarchy.md`](research/02-evidence-hierarchy.md) §2.1). |
| **Confidence** | `High` / `Medium` / `Low` / `Folklore` — per-tell evidentiary status ([`research/02-evidence-hierarchy.md`](research/02-evidence-hierarchy.md) §2.2). Folklore is permanently non-actionable. |
| **S01–S53** | Source IDs; defined only in [`research/03-source-index.md`](research/03-source-index.md). Never redefined locally; never invented. |
| **K1–K9** | Causal mechanism codes (maximum-likelihood training … prompt/template behavior) defined in [`research/01-research-synthesis.md`](research/01-research-synthesis.md) §1.3. |
| **Baseline** | What uniformity/explicitness are compared against: `internal` (the work's own distribution), `corpus` (a genre reference), or `uncalibrated` (none — conservative defaults, Level ≤3 cap). |

## 6. Taxonomy

| Term | Definition |
|---|---|
| **Tell** | A documented behavioral pattern that makes generated fiction feel machine-written. IDs are `P` (prose), `N` (narrative), `C` (character), `D` (dialogue), `S` (description), `E` (emotion), `T` (pacing), `SC` (scene), `V` (voice), `U` (subtext), `W` (worldbuilding), `F` (conflict), `FS` (foreshadowing), `H` (humor), `A` (action), `R` (romance), `L` (long-form) + number. Canonical list: [`taxonomy/README.md`](taxonomy/README.md). Note: `S` is used for both *description tells* (S01–S06) and *source IDs* (S01–S53) — context disambiguates; in tables, tell IDs appear as "S01–S06" only inside the description cluster file. |
| **Severity** | 1–3: how strongly the tell contributes to the AI-fiction feel. |
| **False-positive risk (FPR)** | 1–3: how easily a human literary choice is mistaken for the tell. |
| **Monitored / folklore table** | Patterns deliberately *not* acted upon, with reasons — part of every taxonomy cluster file. |
| **Genre contract** | Genre conventions that are features, never tells ([`frameworks/07-genre-awareness.md`](frameworks/07-genre-awareness.md) §1). |
| **Over-execution** | A contractual pattern executed past the point where it serves the genre — the only part of a contract that may be intervened on. |

## 7. Failure modes & tests

| Term | Definition |
|---|---|
| **F-1…F-10** | Failure-mode codes ([`spec/07-failure-modes.md`](spec/07-failure-modes.md)). F-1 deliberate imperfection; F-2 synonym substitution; F-3 shuffling; F-4 detector optimization; F-5 anti-tell tell; F-6 over-editing; F-7 preservation failure; F-8 calibration drift; F-9 provenance misuse; F-10 humanness theater. |
| **A-T1…A-T23** | Adversarial test IDs ([`tests/01-adversarial-suite.md`](tests/01-adversarial-suite.md)). |
| **T-1…T-10** | Static consistency check IDs ([`tests/02-static-consistency-checklist.md`](tests/02-static-consistency-checklist.md)). |
| **I-1…I-6** | Pipeline ordering invariants ([`spec/05-pipeline.md`](spec/05-pipeline.md) §"Ordering invariants"). |
| **A1–A7 / P1–P5 / M1–M4** | Benchmark metric IDs ([`spec/09-evaluation-benchmark.md`](spec/09-evaluation-benchmark.md) §1). |

## 8. Architecture

| Term | Definition |
|---|---|
| **Prompt contract** | A model-agnostic LLM task spec: role, knowledge load, input schema, output schema, quality checks, temperature guidance, fallback (C-01…C-04). |
| **Deterministic validator / engine** | Code (not LLM) that computes evidence, validates schemas, and applies the preservation checks. The LLM proposes; the validators dispose. |
| **Minimal build** | Two contracts + validators + fact-level ledgers ([`spec/11-minimal-architecture.md`](spec/11-minimal-architecture.md)). |
| **Advanced build** | RAG knowledge layer + full deterministic engines + calibration + long-form state ([`spec/12-advanced-architecture.md`](spec/12-advanced-architecture.md)). |
| **Uncalibrated** | A run with no matching calibration key or non-English lexicons: conservative defaults, Level ≤3 cap, flagged findings. |

## 9. Cross-file numbering

- Spec files keep their original deliverable numbers (02–13); gaps exist
  because the adversarial suite and examples moved to `tests/` and `examples/`
  (see [`CONSOLIDATION-REPORT.md`](CONSOLIDATION-REPORT.md)). The numbers are identifiers, not sequence.
- Taxonomy files number 01–18 and 20; there is no 19 (see [`CONSOLIDATION-REPORT.md`](CONSOLIDATION-REPORT.md)).
- Source IDs S49–S53 exist even though not all cluster files cite them; all IDs
  are defined in [`research/03-source-index.md`](research/03-source-index.md).
