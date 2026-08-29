# Skill: Fictional-Tell Artifact Reduction — Samur Novel Pipeline

**Type:** project-bound, model-agnostic, post-generation skill.
**Objective:** reduce AI-specific storytelling artifacts in **Samur novel
drafts** while preserving story meaning, character intent, narrative voice,
genre conventions, pacing decisions, literary devices, the author's desired
style — and, above all, **the project's canon, registers, and fictional
logic**.
**Non-objective (explicit):** fooling AI detectors; making generated text
"indistinguishable" from human text; imposing a house style; rewriting for
rewriting's sake; being portable.

**This skill is bound to the Velvet Cobble repository and its fictional
project (Samur).** It is not a general AI-writing detector, not a reusable
quality layer for other fiction pipelines, and not a standalone
implementation of any external anti-slop methodology. Its tells, examples,
corrections, and evaluation criteria are derived from this project's
charter, canon (`samur/02-canon/`), drafting constraints, anti-patterns,
name registers, and workflow. Copied into another project it would produce
false positives by design (it would flag that project's names as
name-register violations and its seasons as wind-law breaches); run without
its project context it refuses (`input_rejection`) rather than guess. The
binding contract is `spec/01-project-binding.md`.

This file is the skill's entry point. Implementation details live in
`spec/02-api-interface.md`–`spec/13-integration.md`; evidence lives in `research`;
the tell catalogs live in `taxonomy`; analysis recipes live in `frameworks`;
safety contracts live in `interventions`.

---

## 1. Core contract

The skill is a **post-generation literary quality and artifact-reduction
layer for this project's novel drafts**:

```
Generate story (Canon Guard contract) → Analyze → Detect project tells first,
then generic tells → Identify underlying cause → Prioritize (project before
generic) → Apply minimal intervention → Re-evaluate → Preserve or reject
```

Eleven binding rules:

1. **Project binding.** The skill runs only on Samur drafts with a valid
   `project_context` (live canon resolution, Generation Contract, drafting
   constraints, KE position). No binding → `input_rejection`; there is no
   generic mode (`spec/01-project-binding.md`).
2. **Project tells before generic tells.** The ten Samur-specific tells
   (PST-01…PST-10, `taxonomy/19-project-tells.md`) are scanned first
   (Pass B0), score above the empirical threshold floor, and outrank
   generic findings in the same span: a draft must be right about the world
   before it can be improved as prose (`spec/06-scoring.md` §7).
3. **Project rules beat generic craft.** Where a generic correction
   conflicts with canon, a canon-fixed register, the drafting constraints,
   or the author's declared style, the project wins and the correction is
   reformulated or dropped (`interventions/02-preservation-constraints.md` §8;
   failure mode F-11).
4. **Minimal, causal intervention.** Fix the *cause* of an artifact (why did
   the text over-explain, genericize, or repeat?), never its surface.
5. **Evidence before action.** Every generic tell is grounded in the
   taxonomy with a confidence level; Low/Folklore patterns are never
   actionable. Project-canonical tells are grounded in canon citations
   (their authority class, not confidence, makes them actionable).
6. **Preservation beats polish.** Any edit that improves a tell score while
   degrading fiction (PV-1…PV-14) — or violating the project supremacy laws —
   is rejected — always.
7. **Level 0 is the default.** The skill's bias is toward not editing.
8. **Never escalate without evidence** that the lower level was insufficient
   (`interventions/01-intervention-hierarchy.md`).
9. **No detector feedback, no humanness theater.** Detector scores are never
   an objective, threshold, or escalation criterion (S12–S14, S35); no
   inserted errors, randomization, synonym swapping, or burstiness shaping
   (`spec/07-failure-modes.md`).
10. **Detect-and-report on canon breaks.** Where the draft contradicts
    canon, or a fix would require changing canon, coining names, adding
    high-impact facts, or resolving a deliberate mystery (Q-076/077/078) or
    a NOT READY matter, the skill *reports* to the Canon Guard / author
    workflow (`spec/13-integration.md` §4). It never edits `samur/`, never
    files QUESTIONs on canon content, and never "fixes" canon to match a
    draft.
11. **Transparent provenance.** The skill never removes or obscures
    provenance the author's process requires; it is a craft tool, not a
    disguise.

## 2. What the skill is and is not for

**For:**
- Post-generation polish of **Samur novel drafts** generated under the
  project's Generation Contract, where the author wants fewer
  formulaic/explanatory/synthetic patterns *and* project-faithful prose.
- Catching the project's known AI failure modes: renamed-history transplants,
  exotica, wind-law blindness, false deep-time precision, faction monoliths,
  template-empire framing, modern sensibilities, flattened language map,
  name-register drift, mystery consumption.
- Long-form consistency repair (drift, repetition, contradictions) within
  prose-internal continuity.
- One quality layer inside **this repository's** fiction pipeline,
  cooperating with the Canon Guard (`spec/13-integration.md`).

**Not for:**
- Any other project's fiction (no portability, by design).
- "Un-AI-ing" text to evade detection or misrepresent authorship.
- Rewriting human-authored prose to look more/less "AI."
- Grading text with an AI-probability (see §1 rule 9).
- Canon repair, canon creation, or QUESTION adjudication — the Canon Guard
  workflow owns those; this skill is a detector/reporter there.
- Style conversion (making literary fiction genre-flavored, or vice versa).

## 3. Knowledge base (what the implementer must load)

The skill assumes the implementer has available, in-context or via RAG:

- **The project context (mandatory).** The charter (`PROJECT.md`), the live
  canon resolution for the draft's KE position (default: the Dhaneshra
  Period's equilibrium, post-KE ~900), the Generation Contract, the
  drafting constraints (`samur/00-audit/2026-08-28-initial-cross-check.md`
  §4), the anti-patterns (`skills/canon-guard/anti-patterns.md`), and the
  influence register + transformation logs — as captured in
  `spec/01-project-binding.md` and validated at Stage 0.
- **Project tells** (`taxonomy/19-project-tells.md`): PST-01…PST-10, each
  with canon citations, Samur-specific examples, and canon-sourced fixes.
- **Taxonomy** (`taxonomy`): the generic clusters (~95 documented tells
  across 15 clusters, each with the 17 documentation fields); plus the
  genre×tell matrix and model-variation notes
  (`taxonomy/17-genre-and-model-variation.md`), long-form tells
  (`taxonomy/18-long-form.md`), and the human-comparison framework
  (`taxonomy/20-human-comparison.md`).
- **Evidence hierarchy + source index** (`research/02-evidence-hierarchy.md`,
  `research/03-source-index.md`): confidence and tier for every claim.
- **Causal model** (K1–K9, `research/01-research-synthesis.md` §1.3):
  the mechanism behind each tell class.
- **Frameworks** (`frameworks/01-detection.md`–`07`): the analysis recipes.
- **Intervention hierarchy + preservation constraints + story model**
  (`interventions/01-intervention-hierarchy.md`–`03`).

Minimum viable load: `spec/01-project-binding.md`, the project context it
requires, taxonomy index (`taxonomy/README.md`) + `taxonomy/19`, the causal
model section, frameworks 01–05, interventions 01–03. The rest is
progressively loadable.

## 4. Operating procedure (normative summary)

Full pipeline: `spec/05-pipeline.md`. Summary:

1. **Stage 0 — binding validation.** Validate `project_context`; on failure,
   reject the input (no generic fallback).
2. **Contract extraction (Pass A).** Project context → scene canon surface;
   genre/subgenre, perspective contract, author intent, content boundaries,
   length plan — and the draft's own **narrative voice baseline** (the
   positive inventory of voice signals the skill must preserve;
   `frameworks/01-detection.md` §2 Pass A).
3. **Project scan (Pass B0).** The ten PST checks, cheapest first
   (`taxonomy/19-project-tells.md`); canon-cited findings;
   report-only routing for canon contradictions.
4. **Analysis (Pass B/C).** Build the story model from the draft; run the
   generic framework detectors (repetition & variation audit, metadiscourse
   scan, transplant test for genericity — anchored to the canon surface);
   attach evidence and confidence/authority; run the function test and
   intentionality check on every finding.
5. **Prioritization (Pass D).** Score findings (`spec/06-scoring.md`);
   project findings hold queue priority in their spans; emit the
   intervention queue.
6. **Intervention, level-by-level.** Apply Level 1 draft-wide, re-analyze;
   then Level 2; then Level 3; Levels ≥4 are batch-gated with causality
   audits and (for worldview-touching changes) author consent. Every edit
   passes the project supremacy laws
   (`interventions/02-preservation-constraints.md` §8).
7. **Re-evaluation.** After each batch: preservation checks, tell re-check
   on changed spans, ledger diffs, voice-baseline check; revert failures
   automatically. After the last level: the mandatory **final read**
   (FR-1…FR-8, `spec/05-pipeline.md` Stage 4b) — including the cumulative
   check that the edits, as a set, have not converged the draft toward one
   register or rhythm, and the project re-verification (FR-8: canon intact,
   registers intact, mysteries as open as canon leaves them).
8. **Report.** Emit the AnalysisReport + InterventionLog + revised draft,
   with the author-facing **what changed** list
   (`spec/04-output-schema.md`), and report-only items routed to the Canon
   Guard workflow.

## 5. Interfaces

- **Project binding:** `spec/01-project-binding.md` (authority classes,
  supremacy laws, maintenance triggers).
- **API-agnostic interface:** `spec/02-api-interface.md` (the skill is
  expressed as pure data transforms + prompt contracts so any model/API can
  host it — *within this project's pipeline*).
- **Input schema:** `spec/03-input-schema.md` + `schemas` (`project_context`
  required).
- **Output schema:** `spec/04-output-schema.md` + `schemas`.
- **Integration (Canon Guard cooperation):** `spec/13-integration.md`.

## 6. Evaluation

- **Scoring:** `spec/06-scoring.md` (tell score, function-loss score,
  priority; PST authority qualifier and queue priority).
- **Final read:** `spec/05-pipeline.md` Stage 4b (FR-1…FR-8) — the self-check
  every run performs on its own revised draft (voice recognition, no
  cumulative convergence, proportionality, strong-sentence audit, no new
  tells incl. cosmetic variation, right-word-repeated, report completeness,
  project re-verification). FR failures are release-blocking in the
  benchmark.
- **Benchmark:** `spec/09-evaluation-benchmark.md` + `benchmark` (metrics
  A1–A7, P1–P5, M1–M4, case suite incl. PST cases and project traps,
  before/after rubrics — project-anchored, judged against this project's
  standards).
- **Adversarial tests:** `tests/01-adversarial-suite.md` (incl. the
  anti-AI-rewriting failure modes, intentional-choice traps, and the
  project-binding traps A-T24…A-T31).
- **Static checks:** `tests/02-static-checks.md` (incl. T-11 same-commit PST
  re-verification on canon change).
- **Failure modes:** `spec/07-failure-modes.md` (F-1…F-11).

## 7. Safety & ethics position (summary)

- The skill optimizes literary quality *as this project defines it*, never
  detector evasion (S12–S14, S35, S36).
- It refuses to insert errors or randomness (S01, S02: human variation is
  structured, not noisy).
- It preserves authorial intent and content boundaries absolutely
  (PV-13, PV-14) — and the project's canon absolutely (supremacy law 1).
- It documents provenance and supports disclosure where required (S50, S51
  show disclosure norms matter; the skill's default is transparency).
- It is genre-fair: no convention is treated as a defect
  (`frameworks/07-genre-awareness.md`) — and world-fair: no canon is treated
  as a stylistic preference.

## 8. Maintenance (when the skill must change)

The skill is derived from the project's living documents. When canon, the
charter, the drafting constraints, the anti-patterns, or the Generation
Contract change, the skill must be re-verified in the same commit
(`spec/01-project-binding.md` §5; checklist T-11). A skill that lags its
canon is defective, not merely stale.
