# velvet-cobble

Historical foundation of the **Samur Empire** — a fictional medieval empire constructed from material conditions and comparative historical reasoning.

- `PROJECT.md` — charter: mission, **absolute boundary (no story writing)**, status taxonomy, operating protocol
- `samur/` — all world material, strictly separated: research (real) / canon (fiction) / hypotheses / questions
- `skills/fiction-writing/` — **Canon Guard** (complete ecosystem; re-resolves live branch state before every generation; locked contract; post-generation canon verification; does not freeze canon)
- `samur/CHANGELOG.md` — canon change log (dependency tracking)

**This repository contains no narrative content.** See `PROJECT.md` §2.
This repository hosts one deliverable:

**`ai-fictional-tells-skill/`** — a standalone, model-agnostic, API-agnostic
skill that detects and minimally reduces recurring "AI fictional tells" in
generated fiction (linguistic, narrative, structural, character, dialogue,
pacing, and storytelling artifacts) without degrading story quality,
character integrity, prose, or authorial intent.

The folder is the complete distributable unit: specification, research and
evidence base, tell taxonomy, detection and intervention frameworks, JSON
Schemas, configuration, tests, examples, evaluation methodology, and
integration documentation. Everything lives inside that one folder; it has
no external dependencies and is intended to be copied into any repository.

- Entry point: [`ai-fictional-tells-skill/README.md`](ai-fictional-tells-skill/README.md)
- Primary specification: [`ai-fictional-tells-skill/SKILL.md`](ai-fictional-tells-skill/SKILL.md)
- Consolidation record: [`ai-fictional-tells-skill/CONSOLIDATION-REPORT.md`](ai-fictional-tells-skill/CONSOLIDATION-REPORT.md)
