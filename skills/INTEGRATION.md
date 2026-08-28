# Skill Integration Record — `ai-fictional-tells-skill`

Status: INTEGRATED (documented; NOT yet invoked)
Date: 2026-08-26
Recovery point: tag `recovery/pre-skill-integration` (= `bd5da9e`, the last clean Samur-foundation state)

This record documents the integration of the newly-uploaded skill into the Samur
development workflow, per the repository-first rule. It records what the skill is,
where it belongs, how it will be invoked, and its (non-)effect on existing canon.

---

## 1. Skill name

**`ai-fictional-tells-skill`** — "Fictional-Tell Artifact Reduction for AI-Generated Fiction" (v1.0.0, stable, research-backed).

## 2. Location

- **Path:** `skills/ai-fictional-tells-skill/` (consolidated inside the `skills/` directory during the 2026-08-28 full repository restructure; previously at the repository root on `main`).
- **Arrived via:** PR #1 (merged commit `5d3e078` on `main`), from the branch `arena/01a043d5-velvet-cobble`. Moved into `skills/` on the session branch `arena/01a04822-velvet-cobble` during the full restructure.
- **Self-contained:** a zero-dependency distributable folder (60 files: spec, research, taxonomy, frameworks, interventions, schemas, config, tests, examples, benchmark).
- **Entry point:** `skills/ai-fictional-tells-skill/README.md`; **primary spec:** `skills/ai-fictional-tells-skill/SKILL.md`.

## 3. Purpose (what it does / what problem it solves)

A **standalone, model-agnostic, post-generation literary quality and
artifact-reduction layer** for fiction. It detects recurring "AI fictional tells"
(~95 documented tells across prose / narrative-structure / character / dialogue /
description / emotion / pacing / scene / voice / subtext / worldbuilding /
conflict / foreshadowing / humor / action / romance / genre / long-form clusters),
identifies the **cause** of each (causal model K1–K9), and applies **minimal,
preservation-checked interventions** (Levels 0–6, **Level 0 = no edit = the
default**) that reduce those artifacts **without degrading** story meaning,
character integrity, prose, or authorial intent (14 preservation dimensions,
PV-1…PV-14).

**Explicit non-objective:** it is **not** a detector-evasion tool. It never
optimizes toward AI detectors, never inserts errors/randomness to fake "humanness,"
never imposes a house style, and never edits for the sake of editing.

## 4. Intended workflow stage

**The narrative stage — as a post-generation quality layer.** It operates on
**generated narrative prose (story drafts)**, not on canon. It is the full,
formal, research-backed realization of the goal that the project's own
`skills/fiction-writing/anti-patterns.md` draft gestures at ("reduce AI-fiction
patterns"), but it is a *detection + intervention pipeline*, not a static rule list.

The narrative stage is **BLOCKED** (PROJECT.md §2 — no story writing without a
distinct authorizing system command). **The skill is therefore NOT invoked now.**
It is integrated and documented so that, when the narrative stage is authorized
and narrative text is generated, the skill is used fully and correctly (not
bypassed, not reproduced manually).

### How it fits with the existing `skills/fiction-writing/` draft

| Capability | Layer | When |
|---|---|---|
| `skills/fiction-writing/anti-patterns.md` (pre-flight **canon check** + Samur-specific anti-patterns) | **Pre-generation** canon-compliance + generation guard | Before/during generation |
| `ai-fictional-tells-skill` (tell **detection + minimal intervention** pipeline) | **Post-generation** artifact reduction | After a draft (or per chapter, long-form) exists |

The two are **complementary, not redundant**: the pre-flight canon check ensures
the draft is *canon-compliant* (names/institutions/places from the Samur canon —
the DYN-02 name pool, CUL-01 toponymy, `02-canon/`); the skill ensures the draft
is *free of AI tells*. The skill is **canon-agnostic** (it does not validate
canon-compliance); the pre-flight check is **tell-agnostic** (it does not run the
tell pipeline). The skill's `author_intent` (genre, perspective, style_anchors,
content_boundaries, worldview_constraints) is **fed from the Samur canon**, which
is what binds the skill's PV-5 (setting), PV-6 (world rules), PV-13 (thematic
intent), and PV-14 (stylistic intent) preservation dimensions to the Samur world.

## 5. What the skill does to material (classification)

- **Evaluates** — builds the StoryModel, runs the framework detectors, scores findings (objective evidence only, never adjectives).
- **Transforms** — applies **minimal** interventions to the *draft* (Level-ordered; Level 0 = no edit is the default; Level ≥4 batch-gated; worldview-touching edits author-gated).
- **Validates** — runs the 14 preservation checks (PV-1…PV-14), the evidence check, the function test, the intentionality check, and post-edit re-evaluation (auto-revert on failure).
- **Does NOT research** (the research/evidence is pre-baked in `research/`).
- **Does NOT modify canon** (it operates on narrative drafts only).

## 6. Inputs it requires (`SkillInput`, per `spec/03-input-schema.md`)

- `draft` — the story text (the generated narrative draft; optional scene/chapter segmentation).
- `metadata` — generator family/decoding (optional; absence → `uncalibrated`), `prompt_class`, `language` (default `en`), `length_words` (≥10k → long-form framework).
- `author_intent` — **derived from the Samur canon**: `genre`/`subgenre` (medieval empire / historical-epic fantasy), `perspective`, `style_anchors`, `content_boundaries`, `declared_devices`, `worldview_constraints` (the canon's world rules, the dharma/religion, the historical gravity). When absent, intent-sensitive findings are reported `author-consult-required` rather than acted on.
- `analysis_options` — `max_intervention_level` (default 6; **0 = analysis-only**, the conservative choice for a first pass), `confidence_floor_for_action` (default `medium`), `batch_gate`, `author_gate`, `long_form_threshold_words`, `baseline_source`.
- `provenance` — `disclosure_policy`, `assistance_scope` (recorded, never stripped).

## 7. Outputs it produces (`SkillReport`, per `spec/04-output-schema.md`)

- `analysis` (AnalysisReport): contract extraction, StoryModel, findings (each with tell IDs, quoted spans, objective pattern evidence, confidence, K-code cause, function test, intentionality), observations (non-actionable), calibration, priority queue.
- `intervention` (InterventionLog): every applied/rejected edit with level, cause, 14 PV results, causality audit (L≥4), re-evaluation outcome; byte-level revertible.
- `revised_draft` (Draft′).
- `story_model` (post-edit StoryModel).
- `rejected` (RejectedEdit[]).
- `summary` `{applied, reverted, preserved, flagged_intentional}`.

## 8. Dependencies

- **Self-contained knowledge base** (all inside the folder): taxonomy, research + evidence hierarchy + source index, causal model K1–K9, frameworks 01–07, intervention hierarchy + preservation constraints + story model, JSON schemas, config. **Zero runtime dependencies.**
- **To host it**, the skill needs exactly two capabilities (`spec/13-integration.md` §2): an `llm(contract, input) -> JSON` (any provider — **I, the agent, host it by loading the knowledge base and following the prompt contracts C-01…C-04**) and a `store.put/get` (persistence — **the repository**).
- **For the Samur project specifically:** a canon-compliant narrative draft (the output of the authorized narrative stage) + the Samur canon (for the pre-flight canon check and the `author_intent`/PV-5/PV-6/PV-13/PV-14 inputs).
- **Minimum viable knowledge load** (`spec/11-minimal-architecture.md`): SKILL.md + taxonomy index + research/01 §1.3 + frameworks 01–05 + interventions 01–03 + schemas.

## 9. When it should be invoked

**Only when the narrative stage is authorized** (a distinct system command per
PROJECT.md §2) **and a narrative draft exists.** Hook points
(`spec/13-integration.md` §3):
- **Post-generation (default):** run on the completed draft.
- **Per-chapter (long-form):** run after each chapter; persist the StoryModel; feed the state summary back into the continuation context.
- **CI gate (optional):** `analyze`-only (max level 0) as an artifact report; intervention stays author-driven.

It is **not** invoked during Phases 1–5 (worldbuilding) — those produce canon, not
narrative prose, and the skill has no function on canon.

## 10. How its results should be stored

Per `spec/13-integration.md` §6 (provenance/compliance): the `SkillReport`
(AnalysisReport + InterventionLog + revised draft + StoryModel + rejected +
summary) is **stored alongside the narrative draft's version history** so
provenance decisions remain auditable. Working default (per H-001): a
`narrative/` location (a separate repository or `samur/narrative/`), **never
intermixed with `02-canon/`**. Each run's report is versioned with the draft it
revised; the InterventionLog (byte-level revertible) is retained for audit.

## 11. Limitations

- **English-first.** Non-English runs need retuned lexicons; until then findings are marked `uncalibrated` and edits are capped at Level 3. (The Samur narrative will be in English, so this is not currently a constraint.)
- **Level 0 is the default** — the skill's bias is toward *not* editing; a clean draft yields zero edits. It is a *reduction* layer, not a rewrite engine.
- **Canonicity is out of scope.** The skill does not check that names/institutions/places come from the Samur canon — that is the pre-flight canon check's job (`skills/fiction-writing/anti-patterns.md`).
- **It does not generate story.** It is post-generation only; it cannot open the narrative stage or write the draft.
- **Intent-sensitive findings** (worldview-touching, style-anchored) are author-gated or reported `author-consult-required` when `author_intent` is absent — so the canon-derived `author_intent` must be supplied for a full run.
- **No detector scores** are an objective, threshold, or escalation criterion anywhere in the pipeline.

## 12. Effect on existing canon

**None.** The skill operates exclusively on **narrative drafts**, not on canon
files. It **cannot modify** the 16 canon files, the research, the influence
register, or the question log. Its PV-5 (setting) and PV-6 (world rules)
preservation dimensions mean it **protects** the canon-consistency of a narrative
draft (it will not alter an established Samur setting detail or world rule to make
a tell-fix convenient). No existing canon was modified to accommodate this skill,
and none will be.

## 13. Integration actions taken (logged)

1. **Inspected `main`** (fetched; read `origin/main` in full: SKILL.md, README.md, MANIFEST.md, CONFIG.md, glossary, spec/02,03,04,05,11,13, interventions/01,02, taxonomy/README, the tell catalog).
2. **Created a recovery point** — annotated tag `recovery/pre-skill-integration` at `bd5da9e` (the last clean Samur-foundation state) **before** making any integration change.
3. **Repaired the session branch** — a sandbox reset had re-pointed the local branch to the initial commit; verified the working tree was byte-identical to the remote tip (`bd5da9e`, 130 files, empty diff) and re-anchored.
4. **Wrote this integration record** (`skills/INTEGRATION.md`).
5. **Updated `PROJECT.md`** (§2 gate, §5 phases, §6 map) and **`skills/fiction-writing/STATUS.md`** to reference the skill and its stage.
6. **Did NOT invoke the skill** (narrative stage BLOCKED) and **did NOT begin the next worldbuilding stage** (per the instruction).

**Next (when the narrative stage is authorized):** load the skill's minimum viable
knowledge base, supply the canon-derived `SkillInput` (draft + author_intent), run
the pipeline (analyze → prioritize → intervene → re-evaluate → report), store the
SkillReport with the draft's version history, and review the Level ≥4 /
worldview-gated proposals with the author.
