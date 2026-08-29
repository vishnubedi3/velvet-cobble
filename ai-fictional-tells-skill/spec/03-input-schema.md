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
| `project_context` | object | **yes** | §1.1 — the Samur binding (live canon resolution, Generation Contract, drafting constraints, KE position). **Its absence is an `input_rejection`**: the skill is project-bound by design ([`spec/01-project-binding.md`](01-project-binding.md)) and never falls back to a generic mode. |
| `draft` | object | yes | `{text: string, segmentation: Segmentation?}` — the story text; optional pre-segmented scenes/chapters (framework 04 §1) |
| `metadata` | object | yes | see §2 |
| `author_intent` | object | no | see §3 — when absent, intent is taken from the Generation Contract in `project_context` plus the draft; intent-sensitive findings are reported as `author-consult-required` instead of acted on |
| `analysis_options` | object | no | thresholds overrides, level cap, batch gating flags (defaults in `../spec/06-scoring.md`) |
| `provenance` | object | no | disclosure requirements (§5) |

## 1.1 `project_context` (the binding — required, validated at Stage 0)

| Field | Type | Notes |
|---|---|---|
| `binding` | `"samur"` | Literal. Anything else is rejected — there is no other valid binding. |
| `narrative_period_ke` | string | The draft's KE position (default: `"post-KE ~900, the Dhaneshra Period's equilibrium"` per `samur/02-canon/DYN-04` §15). Flashback and deep-time arcs state their position; PST-04's rules are period-sensitive. |
| `canon_resolution` | object | `{method, resolved_at, scope}` — how the live branch state of `samur/02-canon/` was resolved (via the Canon Guard's re-resolution, never a frozen snapshot; [`spec/01-project-binding.md`](01-project-binding.md) §1). |
| `generation_contract_ref` | string | Reference to the Canon Guard Generation Contract the segment was produced under ([`spec/13-integration.md`](13-integration.md) §3). |
| `drafting_constraints_ref` | string | Reference to the drafting constraints in force (`samur/00-audit/2026-08-28-initial-cross-check.md` §4 or its successor). |
| `scene_canon_surface` | array | Optional pre-computed Pass A surface (institutions/places/factions/languages with canon IDs); computed at Pass A when absent. |

Validation (Stage 0): `binding === "samur"`; `canon_resolution` is live (not
older than the draft's generation run); refs resolve in this repository.
Failures are `input_rejection`s — never silent generic operation.

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
2. `project_context` is required and validated per §1.1: wrong or missing
   binding, a stale/frozen canon resolution, or unresolvable refs are
   `input_rejection`s. There is **no generic fallback mode** — the skill is
   bound to this project by design ([`spec/01-project-binding.md`](01-project-binding.md)).
3. `author_intent.style_anchors` and `declared_devices` are quoted verbatim
   into every intervention contract (they are the highest-priority
   constraints), together with the Generation Contract's style and boundary
   fields.
4. Any input field the skill cannot honor (e.g., unsupported language) is
   returned as an explicit `input_rejection`, not silently approximated.
