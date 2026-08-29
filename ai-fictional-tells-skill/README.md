# AI Fictional Tells — Artifact-Reduction Skill (Samur-bound)

**This skill is purpose-built for this repository and its fictional project
(the Samur novel).** It is a post-generation quality layer for *this
project's* generated fiction: it detects recurring "AI fictional tells" —
including this project's own known failure modes — identifies their causes,
and applies **minimal, preservation-checked edits** that reduce the
artifacts without degrading story quality, character integrity, prose,
authorial intent, **canon, or the project's registers and voice**.

It is **not portable, by design.** See §5.

It is **not** a detector-evasion tool. It never optimizes toward AI
detectors, never inserts errors or randomness to fake "humanness," and never
removes provenance the author's process requires.

- **Primary specification:** [`SKILL.md`](SKILL.md) — start there.
- **The binding:** [`spec/01-project-binding.md`](spec/01-project-binding.md) — why this skill cannot run elsewhere.
- **Version:** 2.0.0 · **Status:** stable, project-bound · **Format:** documentation + JSON Schemas + prompt contracts (no code, no runtime dependencies).
- **Full inventory:** [`MANIFEST.md`](MANIFEST.md) · **Configuration:** [`CONFIG.md`](CONFIG.md) · **Terminology:** [`glossary.md`](glossary.md).

---

## 1. What's in this folder

| Area | Location | Contents |
|---|---|---|
| **Core skill definition** | [`SKILL.md`](SKILL.md), [`spec/`](spec/) | The skill contract, **the project binding (spec/01)**, pipeline, scoring, failure modes, evaluation methodology, minimal/advanced architectures, integration guide |
| **Project tells** | [`taxonomy/19-project-tells.md`](taxonomy/19-project-tells.md) | PST-01…PST-10: the Samur-specific tells, each derived from canon with citations (wind law, name registers, faction structures, epistemic limits, protected mysteries) |
| **Research & evidence** | [`research/`](research/) | Research synthesis, evidence hierarchy, annotated source index (S01–S54) |
| **Detection framework** | [`frameworks/`](frameworks/), [`taxonomy/`](taxonomy/) | Analysis recipes (detection, character, dialogue, scene, narrative, long-form, genre) + the generic tell catalog |
| **Intervention framework** | [`interventions/`](interventions/) | Intervention hierarchy (Levels 0–6), preservation constraints (PV-1…PV-14 **+ the project supremacy laws**), story model |
| **Schemas & configuration** | [`schemas/`](schemas/), [`CONFIG.md`](CONFIG.md) | JSON Schemas for input/output/story model (`project_context` required); parameter defaults and calibration keys |
| **Tests** | [`tests/`](tests/) | Adversarial suite (31 traps, incl. the 8 project-binding traps) + static consistency checklist (T-1…T-11, incl. canon-change re-verification) |
| **Examples** | [`examples/`](examples/) | Before/after intervention examples (generic + project) + a full worked pipeline demo |
| **Integration documentation** | [`spec/13-integration.md`](spec/13-integration.md), [`spec/11-minimal-architecture.md`](spec/11-minimal-architecture.md), [`spec/12-advanced-architecture.md`](spec/12-advanced-architecture.md) | Wiring into **this repository's** pipeline with any LLM provider |
| **Evaluation** | [`spec/09-evaluation-benchmark.md`](spec/09-evaluation-benchmark.md), [`benchmark/`](benchmark/) | Metrics (A1–A7, P1–P5, M1–M4), PST + project-trap case suites, project-anchored rubric, harness contract |

## 2. Quick start (5 minutes)

1. **Read** [`SKILL.md`](SKILL.md) — the complete skill contract (the eleven
   binding rules, operating procedure, knowledge base).
2. **Understand the loop** — `Generate (Canon Guard contract) → Analyze
   (project tells first) → Detect → Identify cause → Prioritize (project
   before generic) → Apply minimal intervention → Re-evaluate → Preserve or
   reject` ([`spec/05-pipeline.md`](spec/05-pipeline.md)).
3. **Assemble the binding** — every run requires a `project_context` (live
   canon resolution, Generation Contract, drafting constraints, KE
   position); without it the skill rejects the input
   ([`spec/03-input-schema.md`](spec/03-input-schema.md) §1.1).
4. **Invoke** — `analyze(input) → prioritize → intervene → reevaluate →
   report`, with inputs per [`spec/03-input-schema.md`](spec/03-input-schema.md)
   + [`schemas/skill-input.schema.json`](schemas/skill-input.schema.json).
5. **Configure** — defaults and thresholds in [`CONFIG.md`](CONFIG.md); the
   binding itself is not configurable (§8).
6. **Test** — the adversarial suite ([`tests/01-adversarial-suite.md`](tests/01-adversarial-suite.md))
   is the acceptance gate; the static checklist
   ([`tests/02-static-consistency-checklist.md`](tests/02-static-consistency-checklist.md))
   keeps documentation, schemas, **and canon citations** consistent.

## 3. Binding design rules (abridged — full text in SKILL.md §1)

1. **Project binding** — Samur `project_context` or rejection; no generic mode.
2. **Project tells before generic tells** — the PST scan runs first and
   outranks generic findings in the same span.
3. **Project rules beat generic craft** — canon, canon-fixed registers, and
   drafting constraints win over any generic correction.
4. **Minimal, causal intervention** — fix the *cause* of an artifact, never its surface.
5. **Evidence before action** — generic tells carry confidence; project
   tells carry canon citations (their authority, not confidence, makes them
   actionable).
6. **Preservation beats polish** — any edit that degrades the fiction
   (PV-1…PV-14) or violates the supremacy laws is rejected, always.
7. **Level 0 is the default** — the skill's bias is toward not editing.
8. **Never escalate without evidence** that the lower level was insufficient.
9. **No detector feedback, no humanness theater** — no detector scores, no
   inserted errors, randomization, or synonym swapping.
10. **Detect-and-report on canon breaks** — canon contradictions go to the
    Canon Guard / author workflow; this skill never edits canon or resolves
    a protected mystery.
11. **Transparent provenance** — a craft tool, not a disguise.

## 4. Project coupling (what "Samur-bound" means concretely)

- **Tells:** ten project tells (PST-01…PST-10) encode this project's
  narrative rules as detectors — e.g. weather written against the wind law,
  names outside the canon pools, factions without their documented fault
  lines, deep-time precision the in-world record cannot carry, the
  deliberate mysteries resolved. Full catalog with citations:
  [`taxonomy/19-project-tells.md`](taxonomy/19-project-tells.md).
- **Corrections:** specificity repairs source from the resolved canon
  surface; register fixes respect the language map; the skill never coins
  names, never invents canon, never adds high-impact facts.
- **Evaluation:** the expert rubric is judged against this project's
  standards (canon fidelity, project registers, in-world epistemology,
  mystery preservation, faction integrity) before generic craft dimensions
  ([`spec/09-evaluation-benchmark.md`](spec/09-evaluation-benchmark.md) §2).
- **Workflow:** Stage 0 validates the binding; canon-contradiction findings
  are report-only for the Canon Guard; the default narrative position is
  the Dhaneshra Period's equilibrium (post-KE ~900).

## 5. Portability statement (read before copying)

**Do not copy this skill into another project.** It is not a general
AI-writing detector, not a reusable quality layer, and not a standalone
implementation of any external anti-slop methodology:

- Its intake **requires** a Samur `project_context`; anything else is an
  `input_rejection` — there is no generic mode.
- Its project tells, examples, corrections, and rubric are derived from
  this repository's canon (`samur/02-canon/`), charter (`PROJECT.md`),
  drafting constraints, anti-patterns, and workflow. Copied elsewhere they
  would produce false positives by design (another project's names would
  be "name-register violations"; its seasons would be "wind-law breaches").
- Its behavior **depends on project context that can change**: canon and
  narrative-standards changes may require skill changes — the same-commit
  re-verification rule (T-11, [`spec/01-project-binding.md`](spec/01-project-binding.md) §5)
  exists for exactly this.
- External methodology (the "No AI Slop" skill) was **studied and adapted,
  not copied**: its evaluation checks and process discipline were
  fiction-specialized into this skill; its word lists and nonfiction
  heuristics were deliberately not imported (the adaptation record is
  `research/03-source-index.md`, source S54). There is no runtime or
  structural dependency on that repository.
- **Adapting the methodology to another project** means re-deriving
  `spec/01` and a project-tell catalog from *that* project's own canon and
  standards, then re-validating the generic layer against them — not
  vendoring this folder ([`spec/13-integration.md`](spec/13-integration.md) §8).

What *is* true of the folder mechanically: cross-references are
file-relative and resolve from the referencing file's location (T-1), and
there are zero runtime dependencies — the skill is documentation + schemas
that read this repository's documents.

## 6. Compatibility & versioning

- **Model-agnostic:** works with any LLM provider via the prompt contracts
  in [`spec/02-api-interface.md`](spec/02-api-interface.md); generator
  metadata is used only for optional calibration
  ([`taxonomy/17-genre-and-model-variation.md`](taxonomy/17-genre-and-model-variation.md)
  §17.3) and degrades gracefully when absent.
- **API-agnostic:** the skill is a data-transform pipeline (`analyze /
  prioritize / intervene / reevaluate / report`) with JSON in/out — see
  [`spec/02-api-interface.md`](spec/02-api-interface.md) §2.
- **Repository-bound:** the pipeline requires this repository's documents at
  Stage 0; the binding is not configurable
  ([`CONFIG.md`](CONFIG.md) §8).
- **Versioning:** `2.0.0` (1.x → 2.0: project binding added; input schema
  gained required `project_context` — breaking). Canon/schema changes are
  breaking; pipeline-parameter changes are minor. Calibration data is
  versioned per (model family, decoding, genre) key. Upgrade guidance:
  [`spec/13-integration.md`](spec/13-integration.md) §7.
- **Minimum viable load** for the knowledge base is documented in
  [`spec/11-minimal-architecture.md`](spec/11-minimal-architecture.md).

## 7. Consolidation record

This folder was consolidated from a multi-directory layout and then bound
to the Samur project; the record of what changed is
[`CONSOLIDATION-REPORT.md`](CONSOLIDATION-REPORT.md).
