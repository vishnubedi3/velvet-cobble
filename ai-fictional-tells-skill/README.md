# AI Fictional Tells — Artifact-Reduction Skill

**This folder is the complete, distributable skill.** Everything required to
understand, install, invoke, configure, test, maintain, and integrate the
skill lives inside this folder; nothing inside depends on files outside it.

The skill is a **standalone, model-agnostic, API-agnostic post-generation
layer** for fiction: it detects recurring "AI fictional tells" (linguistic,
narrative, structural, character, dialogue, pacing, and storytelling patterns
that make generated fiction feel machine-written), identifies their causes,
and applies **minimal, preservation-checked edits** that reduce those
artifacts without degrading story quality, character integrity, prose, or
authorial intent.

It is **not** a detector-evasion tool. It never optimizes toward AI
detectors, never inserts errors or randomness to fake "humanness," and never
removes provenance the author's process requires.

- **Primary specification:** [`SKILL.md`](SKILL.md) — start there.
- **Version:** 1.0.0 · **Status:** stable, research-backed · **Format:** documentation + JSON Schemas + prompt contracts (no code, no dependencies).
- **Full inventory:** [`MANIFEST.md`](MANIFEST.md) · **Configuration:** [`CONFIG.md`](CONFIG.md) · **Terminology:** [`glossary.md`](glossary.md).

---

## 1. What's in this folder

| Area | Location | Contents |
|---|---|---|
| **Core skill definition** | [`SKILL.md`](SKILL.md), [`spec/`](spec/) | The skill contract, pipeline, scoring, failure modes, evaluation methodology, minimal/advanced architectures, integration guide |
| **Research & evidence** | [`research/`](research/) | Research synthesis, evidence hierarchy, annotated source index (S01–S53) |
| **Detection framework** | [`frameworks/`](frameworks/), [`taxonomy/`](taxonomy/) | Analysis recipes (detection, character, dialogue, scene, narrative, long-form, genre) + the full tell catalog |
| **Intervention framework** | [`interventions/`](interventions/) | Intervention hierarchy (Levels 0–6), preservation constraints (PV-1…PV-14), story model |
| **Schemas & configuration** | [`schemas/`](schemas/), [`CONFIG.md`](CONFIG.md) | JSON Schemas for input/output/story model; parameter defaults and calibration keys |
| **Tests** | [`tests/`](tests/) | Adversarial suite (23 traps) + static consistency checklist |
| **Examples** | [`examples/`](examples/) | Before/after intervention examples + a full worked pipeline demo |
| **Integration documentation** | [`spec/13-integration.md`](spec/13-integration.md), [`spec/11-minimal-architecture.md`](spec/11-minimal-architecture.md), [`spec/12-advanced-architecture.md`](spec/12-advanced-architecture.md) | Wiring into arbitrary repositories and any LLM provider |
| **Evaluation** | [`spec/09-evaluation-benchmark.md`](spec/09-evaluation-benchmark.md), [`benchmark/`](benchmark/) | Metrics (A1–A7, P1–P5, M1–M4), case suite, harness contract |

## 2. Quick start (5 minutes)

1. **Read** [`SKILL.md`](SKILL.md) — the complete skill contract (binding rules, operating procedure, knowledge base).
2. **Understand the loop** — `Generate → Analyze → Detect tells → Identify cause → Prioritize → Apply minimal intervention → Re-evaluate → Preserve or reject`
   ([`spec/05-pipeline.md`](spec/05-pipeline.md)).
3. **Install** — copy this folder into the host repository (e.g.
   `skills/fictional-tell-reduction/`); wire two capabilities: an `llm()` function and a `store`
   ([`spec/13-integration.md`](spec/13-integration.md) §2).
4. **Invoke** — `analyze(input) → prioritize → intervene → reevaluate → report`, with inputs per
   [`spec/03-input-schema.md`](spec/03-input-schema.md) + [`schemas/skill-input.schema.json`](schemas/skill-input.schema.json).
5. **Configure** — defaults and thresholds in [`CONFIG.md`](CONFIG.md); per-generator calibration per
   [`taxonomy/17-genre-and-model-variation.md`](taxonomy/17-genre-and-model-variation.md) §17.3.
6. **Test** — the adversarial suite ([`tests/01-adversarial-suite.md`](tests/01-adversarial-suite.md)) is the
   acceptance gate; the static checklist ([`tests/02-static-consistency-checklist.md`](tests/02-static-consistency-checklist.md))
   keeps documentation and schemas consistent.

## 3. Binding design rules (abridged — full text in SKILL.md §1)

1. **Minimal, causal intervention** — fix the *cause* of an artifact, never its surface.
2. **Evidence before action** — every tell has a confidence level; Low/Folklore patterns are never actionable.
3. **Preservation beats polish** — any edit that degrades the fiction (PV-1…PV-14) is rejected, always.
4. **Level 0 is the default** — the skill's bias is toward not editing.
5. **Never escalate without evidence** that the lower level was insufficient.
6. **No detector feedback** — detector scores are never an objective, threshold, or escalation criterion.
7. **No humanness theater** — no inserted errors, randomization, synonym swapping, or burstiness shaping.
8. **Transparent provenance** — a craft tool, not a disguise.

## 4. Compatibility & versioning

- **Model-agnostic:** works with any LLM provider via the prompt contracts in
  [`spec/02-api-interface.md`](spec/02-api-interface.md); generator metadata is used only for optional calibration
  ([`taxonomy/17-genre-and-model-variation.md`](taxonomy/17-genre-and-model-variation.md) §17.3) and degrades gracefully when absent.
- **API-agnostic:** the skill is a data-transform pipeline (`analyze / prioritize / intervene / reevaluate / report`)
  with JSON in/out — see [`spec/02-api-interface.md`](spec/02-api-interface.md) §2.
- **Language:** English-first; lexicon-based detectors are parameterized per language and findings are marked
  `uncalibrated` until retuned.
- **Versioning:** `1.0.0`. Taxonomy/schema changes are breaking; pipeline-parameter changes are minor.
  Calibration data is versioned per (model family, decoding, genre) key. Upgrade guidance:
  [`spec/13-integration.md`](spec/13-integration.md) §7.
- **Minimum viable load** for the knowledge base is documented in
  [`spec/11-minimal-architecture.md`](spec/11-minimal-architecture.md).

## 5. Portability guarantees

- Every cross-reference inside this folder is a **file-relative path** that resolves from the
  referencing file's own location (verified by [`tests/02-static-consistency-checklist.md`](tests/02-static-consistency-checklist.md) T-1).
- The folder has **zero runtime dependencies** and no files outside it; the only external
  resources are the cited research sources (web links in [`research/03-source-index.md`](research/03-source-index.md)),
  which are evidence, not dependencies.
- This folder was consolidated from a multi-directory layout; the record of what changed is
  [`CONSOLIDATION-REPORT.md`](CONSOLIDATION-REPORT.md).
