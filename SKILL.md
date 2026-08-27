# Skill: Fictional-Tell Artifact Reduction for AI-Generated Fiction

**Type:** standalone, model-agnostic, post-generation skill.
**Objective:** reduce unnecessary AI-specific storytelling artifacts in
generated fiction while preserving story meaning, character intent, narrative
voice, genre conventions, pacing decisions, literary devices, and the
author's desired style.
**Non-objective (explicit):** fooling AI detectors; making generated text
"indistinguishable" from human text; imposing a house style; rewriting for
rewriting's sake.

This file is the complete skill specification. Implementation details live in
`skill/02`–`skill/13`; evidence lives in `research/`; the tell catalog lives
in `taxonomy/`; analysis recipes live in `frameworks/`; safety contracts live
in `interventions/`.

---

## 1. Core contract

The skill is a **post-generation literary quality and artifact-reduction
layer**:

```
Generate story → Analyze → Detect fictional tells → Identify underlying cause
→ Prioritize → Apply minimal intervention → Re-evaluate → Preserve or reject
```

Eight binding rules:

1. **Minimal, causal intervention.** Fix the *cause* of an artifact (why did
   the text over-explain, genericize, or repeat?), never its surface.
2. **Evidence before action.** Every tell is grounded in the taxonomy with a
   confidence level; Low/Folklore patterns are never actionable.
3. **Preservation beats polish.** Any edit that improves a tell score while
   degrading fiction (PV-1…PV-14) is rejected — always.
4. **Level 0 is the default.** The skill's bias is toward not editing.
5. **Never escalate without evidence** that the lower level was insufficient
   (`interventions/01-intervention-hierarchy.md`).
6. **No detector feedback.** Detector scores are never an objective, a
   threshold, or an escalation criterion (evidence: S12–S14, S35).
7. **No humanness theater.** No inserted errors, randomization, synonym
   swapping, or burstiness shaping (`skill/07-failure-modes.md`).
8. **Transparent provenance.** The skill never removes or obscures
   provenance the author's process requires; it is a craft tool, not a
   disguise.

## 2. What the skill is and is not for

**For:**
- Post-generation polish of machine-assisted fiction where the author wants
  fewer formulaic/explanatory/synthetic patterns.
- Making generated fiction more context-sensitive, character-specific, and
  structurally varied where the original output contains those weaknesses.
- Long-form consistency repair (drift, repetition, contradictions).
- A *reusable quality layer* an agent can install in any fiction pipeline.

**Not for:**
- "Un-AI-ing" text to evade detection or misrepresent authorship.
- Rewriting human-authored prose to look more/less "AI."
- Grading text with an AI-probability (see §1 rule 6).
- Style conversion (making literary fiction genre-flavored, or vice versa)
  — that is a different skill.

## 3. Knowledge base (what the implementer must load)

The skill assumes the implementer has available, in-context or via RAG:
- **Taxonomy** (`taxonomy/`): ~95 documented tells across 15 clusters, each
  with the 17 documentation fields; plus the genre×tell matrix and
  model-variation notes (`taxonomy/17-*`), long-form tells
  (`taxonomy/18-*`), and the human-comparison framework (`taxonomy/20-*`).
- **Evidence hierarchy + source index** (`research/02`, `research/03`):
  confidence and tier for every claim.
- **Causal model** (K1–K9, `research/01-research-synthesis.md` §1.3):
  the mechanism behind each tell class.
- **Frameworks** (`frameworks/01`–`07`): the analysis recipes.
- **Intervention hierarchy + preservation constraints + story model**
  (`interventions/01`–`03`).

Minimum viable load: taxonomy index (`taxonomy/README.md`), the causal model
section, frameworks 01–05, interventions 01–03. The rest is progressively
loadable.

## 4. Operating procedure (normative summary)

Full pipeline: `skill/05-pipeline.md`. Summary:

1. **Contract extraction (Pass A).** Genre/subgenre, perspective contract,
   author intent, content boundaries, length plan.
2. **Analysis (Pass B/C).** Build the story model from the draft; run
   framework detectors; attach evidence and confidence; run the function
   test and intentionality check on every finding.
3. **Prioritization (Pass D).** Score findings
   (`skill/06-scoring.md`); emit the intervention queue.
4. **Intervention, level-by-level.** Apply Level 1 draft-wide, re-analyze;
   then Level 2; then Level 3; Levels ≥4 are batch-gated with causality
   audits and (for worldview-touching changes) author consent.
5. **Re-evaluation.** After each batch: preservation checks, tell re-check
   on changed spans, ledger diffs; revert failures automatically.
6. **Report.** Emit the AnalysisReport + InterventionLog + revised draft
   (`skill/04-output-schema.md`).

## 5. Interfaces

- **API-agnostic interface:** `skill/02-api-interface.md` (the skill is
  expressed as pure data transforms + prompt contracts so any model/API can
  host it).
- **Input schema:** `skill/03-input-schema.md` + `schemas/`.
- **Output schema:** `skill/04-output-schema.md` + `schemas/`.
- **Integration:** `skill/13-integration.md`.

## 6. Evaluation

- **Scoring:** `skill/06-scoring.md` (tell score, function-loss score,
  priority).
- **Benchmark:** `skill/09-evaluation-benchmark.md` + `benchmark/` (metrics
  A1–A10, case suite, before/after rubrics).
- **Adversarial tests:** `skill/08-adversarial-tests.md` (incl. the
  anti-AI-rewriting failure modes and intentional-choice traps).
- **Failure modes:** `skill/07-failure-modes.md`.

## 7. Safety & ethics position (summary)

- The skill optimizes literary quality, never detector evasion
  (S12–S14, S35, S36).
- It refuses to insert errors or randomness (S01, S02: human variation is
  structured, not noisy).
- It preserves authorial intent and content boundaries absolutely
  (PV-13, PV-14).
- It documents provenance and supports disclosure where required (S50, S51
  show disclosure norms matter; the skill's default is transparency).
- It is genre-fair: no convention is treated as a defect
  (`frameworks/07-genre-awareness.md`).
