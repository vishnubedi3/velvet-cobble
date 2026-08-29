# MANIFEST — Complete Folder Inventory

Every file in this skill, what it contains, and what it depends on.
This is the authoritative inventory; it doubles as the portability contract:
anything referenced by the skill must appear here (verified by
[`tests/02-static-consistency-checklist.md`](tests/02-static-consistency-checklist.md) T-4/T-5).

## Root

| File | Contents |
|---|---|
| [`README.md`](README.md) | **Entry point.** What the skill is, quick start, structure map, binding rules, compatibility/versioning, portability guarantees. |
| [`SKILL.md`](SKILL.md) | **Primary specification.** The complete skill contract: objective, binding rules, scope, knowledge base, operating procedure, interfaces, evaluation, safety/ethics position. |
| [`CONFIG.md`](CONFIG.md) | Configuration definitions: every parameter, default, calibration key, precedence, and validation rule. |
| [`glossary.md`](glossary.md) | Canonical terminology: pipeline stages, levels, dimensions, tell-ID and source-ID schemes, K-codes, terms that must not drift between files. |
| [`MANIFEST.md`](MANIFEST.md) | This file. |
| [`CONSOLIDATION-REPORT.md`](CONSOLIDATION-REPORT.md) | Record of the consolidation: what was merged/moved/removed, audit results, portability verdict. |

## Core skill definition

| File | Contents |
|---|---|
| [`spec/02-api-interface.md`](spec/02-api-interface.md) | API-agnostic interface: the five pure functions, prompt contracts (C-01…C-04), generator/analyzer independence, hosting contract. |
| [`spec/03-input-schema.md`](spec/03-input-schema.md) | Normative input contract (`SkillInput`: draft, metadata, author_intent, analysis_options, provenance). Machine-readable: [`schemas/skill-input.schema.json`](schemas/skill-input.schema.json). |
| [`spec/04-output-schema.md`](spec/04-output-schema.md) | Normative output contract (`SkillReport`, `AnalysisReport`, `Finding`, `InterventionLog`). Machine-readable: [`schemas/analysis-report.schema.json`](schemas/analysis-report.schema.json), [`schemas/intervention-request.schema.json`](schemas/intervention-request.schema.json). |
| [`spec/05-pipeline.md`](spec/05-pipeline.md) | The processing pipeline (Stages 0–5) and the ordering invariants I-1…I-6. |
| [`spec/06-scoring.md`](spec/06-scoring.md) | Scoring methodology: finding priority formula, cause clustering, level assignment, re-evaluation outcomes, anti-gaming properties. |
| [`spec/07-failure-modes.md`](spec/07-failure-modes.md) | The ten failure modes F-1…F-10, including the researched anti-AI-rewriting failure mode, with evidence and countermeasures. |
| [`spec/09-evaluation-benchmark.md`](spec/09-evaluation-benchmark.md) | Evaluation & validation methodology: metrics A1–A7 (artifact reduction), P1–P5 (preservation), M1–M4 (process), expert rubric, taxonomy re-validation path. |
| [`spec/11-minimal-architecture.md`](spec/11-minimal-architecture.md) | Minimal implementation architecture: two prompt contracts + deterministic validators; cost model; minimum viable knowledge load. |
| [`spec/12-advanced-architecture.md`](spec/12-advanced-architecture.md) | Advanced implementation architecture: RAG knowledge layer, deterministic analysis engines, intervention engine, calibration subsystem, long-form subsystem, evaluation harness, hardening. |
| [`spec/13-integration.md`](spec/13-integration.md) | Integration documentation for arbitrary repositories and model APIs: vendoring, wiring, hook points, provider notes, compliance/provenance, upgrade path, acceptance checklist. |

## Research & evidence

| File | Contents |
|---|---|
| [`research/01-research-synthesis.md`](research/01-research-synthesis.md) | Full research synthesis: per-cluster findings with source IDs and confidence, the causal model K1–K9, and the anti-AI-rewriting evidence. |
| [`research/02-evidence-hierarchy.md`](research/02-evidence-hierarchy.md) | The five evidence tiers (Tier 0 fiction-specific → Tier 4 folklore), the confidence scale, and the rules of use. |
| [`research/03-source-index.md`](research/03-source-index.md) | Annotated source index S01–S53 (citations, links, what each establishes). The single source of truth for source IDs. |

## Detection framework

| File | Contents |
|---|---|
| [`frameworks/01-detection.md`](frameworks/01-detection.md) | Fiction-specific detection framework: principles, the four passes, false-positive guardrails, output contract. |
| [`frameworks/02-character-analysis.md`](frameworks/02-character-analysis.md) | Character model extraction, character tell detectors, voice profiles, stereotype audit, integrity checks. |
| [`frameworks/03-dialogue-analysis.md`](frameworks/03-dialogue-analysis.md) | Dialogue tell detectors, the implicature model, rhythm-variation rules, humor beats, preservation checks. |
| [`frameworks/04-scene-analysis.md`](frameworks/04-scene-analysis.md) | Scene segmentation/typing, scene tell detectors, perceiver audit, scene-state register, beat-structure analysis, intensity/distance curves. |
| [`frameworks/05-narrative-analysis.md`](frameworks/05-narrative-analysis.md) | Structure extraction, narrative tell detectors, theme audit, causality audit, structural variance library. |
| [`frameworks/06-long-form-consistency.md`](frameworks/06-long-form-consistency.md) | Long-form ledgers and audits (L01–L10), generation-side prevention, revision-side remediation. |
| [`frameworks/07-genre-awareness.md`](frameworks/07-genre-awareness.md) | Genre contract table, the genre gate, genre declaration rules, genre-sensitive measurement. |

## Tell catalog (taxonomy)

| File | Contents |
|---|---|
| [`taxonomy/README.md`](taxonomy/README.md) | Master index: every tell with confidence/severity/false-positive risk; reading guide for entries. |
| [`taxonomy/01-prose.md`](taxonomy/01-prose.md) | Prose-level tells P01–P07 (modal-average phrasing, balanced syntax, register inflation, uniform rhythm, decorative figurative density, signposting, over-polish). |
| [`taxonomy/02-narrative-structure.md`](taxonomy/02-narrative-structure.md) | Narrative-level tells N01–N08 (story-as-argument, explicit theme, setup/payoff symmetry, default template, repeating conflict cycles, neat closure, moral clarity, valence smoothing). |
| [`taxonomy/03-character.md`](taxonomy/03-character.md) | Character-level tells C01–C08 (emotion labeling, instant backstory, uniform interiority, measured reactions, polite conflict, hyper-consistency, stereotypes, theme vehicles). |
| [`taxonomy/04-dialogue.md`](taxonomy/04-dialogue.md) | Dialogue-level tells D01–D07 (symmetric turn-taking, as-you-know exposition, over-explicit emotional speech, uniform idiolect, over-complete grammar, hedged politeness, explanatory tags). |
| [`taxonomy/05-description.md`](taxonomy/05-description.md) | Description-level tells S01–S06 (atmosphere-first opens, sensory checklists, generic sensory vocabulary, mood-signaling weather, camera framing, POV-decoupled description). |
| [`taxonomy/06-emotion.md`](taxonomy/06-emotion.md) | Emotional tells E01–E05 (naming vs. enacting, reinforcement loops, manufactured intensity, predictable progression, positivity smoothing). |
| [`taxonomy/07-pacing.md`](taxonomy/07-pacing.md) | Pacing tells T01–T06 (uniform rhythm, setup-heavy openings, manufactured scene-end tension, no quiet variation, premature resolution, long-form sag). |
| [`taxonomy/08-scene-construction.md`](taxonomy/08-scene-construction.md) | Scene-construction tells SC01–SC06 (formulaic openings, announced entrances, stated purpose, manufactured buttons, repeated skeletons, no incidental behavior). |
| [`taxonomy/09-narrative-voice.md`](taxonomy/09-narrative-voice.md) | Narrative-voice tells V01–V06 (uniform distance, explanatory narrator, generic polish, thematic overreach, no ambiguity, register monotony). |
| [`taxonomy/10-subtext.md`](taxonomy/10-subtext.md) | Subtext tells U01–U05 (characters say what they mean, narrator explains significance, in-scene theme statements, post-action interpretation, full closure). |
| [`taxonomy/11-worldbuilding.md`](taxonomy/11-worldbuilding.md) | Worldbuilding tells W01–W05 (encyclopedia exposition, artificial completeness, creativity-signal worldbuilding, no lived-in messiness, nonspecificity). |
| [`taxonomy/12-conflict-tension.md`](taxonomy/12-conflict-tension.md) | Conflict tells F01–F05 (predictable escalation, artificial misunderstanding, moral flattening, premature resolution, sanitized conflict). |
| [`taxonomy/13-foreshadowing-symbolism.md`](taxonomy/13-foreshadowing-symbolism.md) | Foreshadowing/symbolism tells FS01–FS03 (signposted foreshadowing, rigid setup/payoff, explained symbols). |
| [`taxonomy/14-humor.md`](taxonomy/14-humor.md) | Humor tells H01–H04 (stock templates, explanatory humor, uniform wit, no timing variance). |
| [`taxonomy/15-action.md`](taxonomy/15-action.md) | Action tells A01–A04 (sequential choreography, spatial inconsistency, no consequence persistence, escalation-only). |
| [`taxonomy/16-romance-relationships.md`](taxonomy/16-romance-relationships.md) | Romance/relationship tells R01–R04 (instant transparency, milestone checklist, residue-free reconciliation, over-explained feelings). |
| [`taxonomy/17-genre-and-model-variation.md`](taxonomy/17-genre-and-model-variation.md) | Genre × tell-cluster matrix with evidence markers; model-family variation; calibration consequences. |
| [`taxonomy/18-long-form.md`](taxonomy/18-long-form.md) | Long-form tells L01–L10 with ledger-based detectors and mitigations. |
| [`taxonomy/20-human-comparison.md`](taxonomy/20-human-comparison.md) | Human literary writing comparison: what human fiction actually is, the eight good-vs-AI-like contrasts, rejected definitions. |

## Intervention framework

| File | Contents |
|---|---|
| [`interventions/01-intervention-hierarchy.md`](interventions/01-intervention-hierarchy.md) | Levels 0–6 with applicability, constraints, escalation rules, anti-mechanical guardrails, logging. |
| [`interventions/02-preservation-constraints.md`](interventions/02-preservation-constraints.md) | The preservation system: PV-1…PV-14, the rejection rule, intentionality checks, causality requirement, hard exclusions. |
| [`interventions/03-story-model.md`](interventions/03-story-model.md) | The structural story representation: characters, goals, relationships, voice, setting, world rules, timeline, events, perspective, scenes, emotion, conflicts, themes, motifs, foreshadowing, information state — and how it identifies damage. Machine-readable: [`schemas/story-model.schema.json`](schemas/story-model.schema.json). |

## Schemas

| File | Contents |
|---|---|
| [`schemas/skill-input.schema.json`](schemas/skill-input.schema.json) | JSON Schema for the top-level input (`SkillInput`). |
| [`schemas/analysis-report.schema.json`](schemas/analysis-report.schema.json) | JSON Schema for analysis output (`AnalysisReport`, findings, observations, calibration). |
| [`schemas/intervention-request.schema.json`](schemas/intervention-request.schema.json) | JSON Schema for intervention proposals and log entries (preservation results, causality audit, outcomes). |
| [`schemas/story-model.schema.json`](schemas/story-model.schema.json) | JSON Schema for the story model (the preservation-check substrate). |

## Tests

| File | Contents |
|---|---|
| [`tests/01-adversarial-suite.md`](tests/01-adversarial-suite.md) | 23 adversarial tests (A-T1…A-T23): intentional-choice traps, continuity traps, new-artifact traps, detector-independence traps, escalation-discipline traps; pass criteria. |
| [`tests/02-static-consistency-checklist.md`](tests/02-static-consistency-checklist.md) | 10 static self-checks (T-1…T-10): links, schema validity, tell-ID/source-ID consistency, terminology, numbering, manifest coverage, entry points. |

## Examples

| File | Contents |
|---|---|
| [`examples/01-before-after-examples.md`](examples/01-before-after-examples.md) | 12 before/after intervention examples (with tell IDs, cause, level, preservation rationale — incl. the kicker rule and referent-cycling restoration) + rejection examples. |
| [`examples/02-worked-example-short-story.md`](examples/02-worked-example-short-story.md) | A compressed end-to-end pipeline run on a 900-word story excerpt: input, findings, priority, edits, one rejected proposal, report. |

## Evaluation material

| File | Contents |
|---|---|
| [`benchmark/README.md`](benchmark/README.md) | Benchmark harness contract, case inventory, ground-truth discipline, calibration corpus procedure. |
| [`benchmark/cases/README.md`](benchmark/cases/README.md) | Case-file manifest and authoring template (files added per repository; not required for the skill to function). |

## External resources (evidence only, not dependencies)

The only non-local resources are the cited literature: web links in
[`research/03-source-index.md`](research/03-source-index.md) and [`research/01-research-synthesis.md`](research/01-research-synthesis.md).
They document the evidence base; no file in this folder is loaded or fetched
by the skill at run time. The skill is fully functional offline.
