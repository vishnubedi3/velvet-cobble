# velvet-cobble — AI Fictional Tells: Research & De-Artifacting Skill

A research-backed, standalone, model-agnostic specification for detecting and reducing
the recurring linguistic, narrative, and structural artifacts ("fictional tells") that
make language-model fiction feel recognizably machine-written — **without degrading
story quality, character integrity, prose quality, or authorial intent.**

This repository is not a detector-evasion toolkit. It deliberately does **not** optimize
against AI detectors, and it does not claim to make generated text "indistinguishable
from human writing." Its objective is narrower and stronger:

> Reduce unnecessary AI-specific storytelling artifacts while preserving story meaning,
> character intent, narrative voice, genre conventions, pacing decisions, literary
> devices, and the author's desired style.

The skill is designed as a **post-generation literary quality and artifact-reduction
layer**: `Generate story → Analyze → Detect fictional tells → Identify underlying cause →
Prioritize → Apply minimal intervention → Re-evaluate → Preserve or reject.`

---

## Repository map

### Research (evidence)
| Path | Contents |
|---|---|
| [`research/01-research-synthesis.md`](research/01-research-synthesis.md) | Full synthesis: what the literature shows per tell-cluster, what is folklore, and the causal model of *why* tells emerge. |
| [`research/02-evidence-hierarchy.md`](research/02-evidence-hierarchy.md) | Five-tier evidence hierarchy and rules for weighting claims. |
| [`research/03-source-index.md`](research/03-source-index.md) | Annotated source index (S01–S47) used by every other document. |

### Taxonomy (the tells)
| Path | Contents |
|---|---|
| [`taxonomy/README.md`](taxonomy/README.md) | Master index: every tell, one line each, with confidence, severity, and false-positive risk. |
| [`taxonomy/01-prose.md`](taxonomy/01-prose.md) … [`taxonomy/18-long-form.md`](taxonomy/18-long-form.md) | Full per-tell documentation: definition, example pattern, observable characteristics, evidence, cause, cross-model/genre/perspective/length variation, severity, false-positive risk, effect on quality, mitigation, side effects, validation. (Genre and model variation are combined in `taxonomy/17-genre-and-model-variation.md`; there is no file 19.) |
| [`taxonomy/20-human-comparison.md`](taxonomy/20-human-comparison.md) | The human-writing comparison framework and the eight good-vs-AI-like contrasts. |

### Analysis frameworks
| Path | Contents |
|---|---|
| [`frameworks/01-detection.md`](frameworks/01-detection.md) | Fiction-specific detection framework (process + evidence-gathering, not a detector). |
| [`frameworks/02-character-analysis.md`](frameworks/02-character-analysis.md) | Character-model extraction and analysis. |
| [`frameworks/03-dialogue-analysis.md`](frameworks/03-dialogue-analysis.md) | Dialogue analysis. |
| [`frameworks/04-scene-analysis.md`](frameworks/04-scene-analysis.md) | Scene construction analysis. |
| [`frameworks/05-narrative-analysis.md`](frameworks/05-narrative-analysis.md) | Narrative/structure analysis. |
| [`frameworks/06-long-form-consistency.md`](frameworks/06-long-form-consistency.md) | Long-form consistency framework. |
| [`frameworks/07-genre-awareness.md`](frameworks/07-genre-awareness.md) | Genre-aware analysis. |

### Interventions
| Path | Contents |
|---|---|
| [`interventions/01-intervention-hierarchy.md`](interventions/01-intervention-hierarchy.md) | Levels 0–6, escalation rules, never-escalate-without-evidence rule. |
| [`interventions/02-preservation-constraints.md`](interventions/02-preservation-constraints.md) | The 14 preservation dimensions + rejection rules. |
| [`interventions/03-story-model.md`](interventions/03-story-model.md) | The structural story representation used to catch damage. |

### The skill itself
| Path | Contents |
|---|---|
| [`SKILL.md`](SKILL.md) | **Entry point.** The complete standalone skill specification. |
| [`skill/02-api-interface.md`](skill/02-api-interface.md) | API-agnostic interface. |
| [`skill/03-input-schema.md`](skill/03-input-schema.md) | Input schema. |
| [`skill/04-output-schema.md`](skill/04-output-schema.md) | Output schema. |
| [`skill/05-pipeline.md`](skill/05-pipeline.md) | Processing pipeline. |
| [`skill/06-scoring.md`](skill/06-scoring.md) | Scoring methodology. |
| [`skill/07-failure-modes.md`](skill/07-failure-modes.md) | Failure modes, incl. anti-AI rewriting becoming its own tell. |
| [`skill/08-adversarial-tests.md`](skill/08-adversarial-tests.md) | Adversarial test suite. |
| [`skill/09-evaluation-benchmark.md`](skill/09-evaluation-benchmark.md) | Evaluation benchmark. |
| [`skill/10-before-after-examples.md`](skill/10-before-after-examples.md) | Before/after intervention examples. |
| [`skill/11-minimal-architecture.md`](skill/11-minimal-architecture.md) | Minimal implementation architecture. |
| [`skill/12-advanced-architecture.md`](skill/12-advanced-architecture.md) | Advanced implementation architecture. |
| [`skill/13-integration.md`](skill/13-integration.md) | Integration into arbitrary repositories and model APIs. |

### Machine-readable artifacts
| Path | Contents |
|---|---|
| [`schemas/story-model.schema.json`](schemas/story-model.schema.json) | Story model JSON Schema. |
| [`schemas/analysis-report.schema.json`](schemas/analysis-report.schema.json) | Analysis report JSON Schema. |
| [`schemas/intervention-request.schema.json`](schemas/intervention-request.schema.json) | Intervention request/result JSON Schema. |
| [`benchmark/README.md`](benchmark/README.md) | Benchmark design, metrics, and case suite. |
| [`examples/`](examples/) | Worked before/after examples. |

---

## Design principles (non-negotiable)

1. **Minimal, causal intervention.** The skill removes *causes of artifacts*, not
   artifact-shaped words. It never paraphrases for the sake of paraphrasing.
2. **Evidence over folklore.** Lexical "AI word lists" are excluded unless tied to a
   documented behavioral pattern. Confidence levels are attached to every claim.
3. **Preservation beats polish.** A transformation that lowers a tell score but damages
   plot, character, voice, world rules, or intent is rejected — always.
4. **No detector optimization.** Statistical detectors are unreliable (Weber-Wulff et al.
   2023), easily evaded by paraphrasing (Sadasivan et al. 2023; Krishna et al. 2023),
   and biased (Liang et al. 2023). Optimizing toward them produces new, worse artifacts.
5. **No "humanness theater."** Deliberately inserted errors, randomness, or "burstiness
   shaping" degrade literature and introduce new machine-recognizable artifacts.
6. **Transparent provenance.** Where provenance matters, disclose it. The skill exists
   to make machine-assisted fiction better fiction, not to misrepresent authorship.
7. **Model-agnostic.** The skill is a process specification + knowledge base. Any
   capable model can implement it against any generator.

## How to implement this skill

A developer or agent can implement the skill in an arbitrary repository by following
[`SKILL.md`](SKILL.md) (the contract) and [`skill/13-integration.md`](skill/13-integration.md)
(the wiring). Minimal viable implementation: one analysis prompt, one intervention
prompt, the story model, and the preservation checklist — everything else is an
incremental upgrade.
