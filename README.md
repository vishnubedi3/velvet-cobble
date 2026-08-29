# velvet-cobble

Historical foundation of the **Samur Empire** — a fictional medieval empire constructed from material conditions and comparative historical reasoning.

- `PROJECT.md` — charter: mission, **absolute boundary (no story writing)**, status taxonomy, operating protocol
- `samur/` — all world material, strictly separated: research (real) / canon (fiction) / hypotheses / questions
- `skills/canon-guard/` — **Canon Guard** (complete ecosystem; re-resolves live branch state before every generation; locked contract; post-generation canon verification; does not freeze canon)
- `samur/CHANGELOG.md` — canon change log (dependency tracking)

**This repository contains no narrative content.** See `PROJECT.md` §2.
This repository hosts one deliverable:

**`ai-fictional-tells-skill/`** — a model-agnostic, API-agnostic
post-generation skill that detects and minimally reduces recurring
"AI fictional tells" in this project's generated fiction (linguistic,
narrative, structural, character, dialogue, pacing, and storytelling
artifacts — plus the project's own known failure modes) without degrading
story quality, character integrity, prose, authorial intent, or canon.

The folder is the complete unit: specification, research and evidence base,
tell taxonomy (generic + project-specific), detection and intervention
frameworks, JSON Schemas, configuration, tests, examples, evaluation
methodology, and integration documentation. It has no runtime dependencies,
but it is **purpose-built for this repository's fictional project and is not
portable**: it validates a Samur project binding at intake (rejecting
unbound input instead of running generically), derives its project tells
from `samur/02-canon/` and the project's narrative standards, gives project
rules priority over generic craft, and may require updates when those
standards change. Adapting the methodology elsewhere means re-deriving it
from that project's own canon — not copying this folder (see
[`ai-fictional-tells-skill/README.md`](ai-fictional-tells-skill/README.md) §5).

- Entry point: [`ai-fictional-tells-skill/README.md`](ai-fictional-tells-skill/README.md)
- Primary specification: [`ai-fictional-tells-skill/SKILL.md`](ai-fictional-tells-skill/SKILL.md)
- Project binding: [`ai-fictional-tells-skill/spec/01-project-binding.md`](ai-fictional-tells-skill/spec/01-project-binding.md)
- Consolidation record: [`ai-fictional-tells-skill/CONSOLIDATION-REPORT.md`](ai-fictional-tells-skill/CONSOLIDATION-REPORT.md)
