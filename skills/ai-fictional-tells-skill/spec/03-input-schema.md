# 03 — Input Schema

Machine-readable spec: [`../schemas/skill-input.schema.json`](../schemas/skill-input.schema.json)
(validated at pipeline Stage 0). The output side is
[`../schemas/analysis-report.schema.json`](../schemas/analysis-report.schema.json) and
[`../schemas/intervention-request.schema.json`](../schemas/intervention-request.schema.json),
documented in [`04-output-schema.md`](04-output-schema.md). This file is the normative
human-readable input contract.

## 1. `SkillInput`

| Field | Type | Required | Notes |
|---|---|---|---|
| `draft` | object | yes | `{text: string, segmentation: Segmentation?}` — the story text; optional pre-segmented scenes/chapters (framework 04 §1) |
| `metadata` | object | yes | see §2 |
| `author_intent` | object | no | see §3 — when absent, intent is inferred from the draft only, and intent-sensitive findings are reported as `author-consult-required` instead of acted on |
| `analysis_options` | object | no | thresholds overrides, level cap, batch gating flags (defaults in `../spec/06-scoring.md`) |
| `provenance` | object | no | disclosure requirements (§5) |

## 2. `metadata`

| Field | Required | Notes |
|---|---|---|
| `generator` | no | `{family?, model?, decoding?}` — e.g. `{family: "gpt", decoding: {temperature: 0.7}}`. Used for baseline selection (taxonomy/17 §17.3); absence → `uncalibrated` findings |
| `prompt_class` | no | how the draft was produced: `zero-shot / outlined / iterated / human-assisted / hybrid / unknown`. Prompt class changes which tells are expected (S29) |
| `language` | yes (default `en`) | the skill is English-first; other languages need retuned lexicons (all lexicon-based detectors are parameterized) |
| `length_words` | no | enables long-form framework selection (≳10k → frameworks/06) |

## 3. `author_intent` (the contract the skill must honor)

| Field | Notes |
|---|---|
| `genre` / `subgenre` | required for the genre gate (frameworks/07). Absent → provisional genre + `author-consult-required` on contract-sensitive findings |
| `perspective` | e.g. `close-third`, `first-unreliable`, `omniscient` — the narration contract (PV-8) |
| `style_anchors` | free text: "flat prose", "lyrical", "fragments are deliberate", "the narrator explains — that's the voice". These become PV-14 protections |
| `content_boundaries` | absolute: violence level, sex, harm depictions. Violations are never "fixed" silently; boundaries are absolute (F05/E05 edits respect them) |
| `declared_devices` | deliberate motifs, refrains, structural experiments, ambiguity, moral clarity — pre-registered as intentional (Level 0 protected) |
| `worldview_constraints` | e.g. "the moral ambiguity is the point", "HEA required" — gates N07/F03/E05-class edits (author consent required regardless) |

## 4. `analysis_options` (defaults)

| Option | Default | Notes |
|---|---|---|
| `max_intervention_level` | 6 | lower to 3 for conservative runs; 0 = analysis-only |
| `confidence_floor_for_action` | `medium` | Low-confidence tells are report-only |
| `batch_gate` | `true` | Level ≥4 edits collected and reviewed together |
| `author_gate` | `true` | worldview-touching edits (N07/F03/E05-class) require explicit author consent even when intent fields are absent |
| `long_form_threshold_words` | 10000 | selects frameworks/06 |
| `baseline_source` | `auto` | `internal` (work's own baseline) / `corpus` (genre reference) / `auto` |

## 5. `provenance`

| Field | Notes |
|---|---|
| `disclosure_policy` | how the author handles provenance: `full / venue-required / author-decision`. The skill never removes required disclosures and never adds false ones |
| `assistance_scope` | what the AI contributed (drafting / revision / ideas) — recorded in reports for the author's own records (S50/S51 context) |

## 6. Input validation rules

1. Draft must be plain text (or markdown with explicit paragraph/scene
   markers). Binary/formatting loss is rejected at intake.
2. `author_intent.style_anchors` and `declared_devices` are quoted verbatim
   into every intervention contract (they are the highest-priority
   constraints).
3. Any input field the skill cannot honor (e.g., unsupported language) is
   returned as an explicit `input_rejection`, not silently approximated.
