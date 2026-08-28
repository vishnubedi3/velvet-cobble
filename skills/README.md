# `skills/` — Agent Skills

This directory contains all agent skills used in the project's narrative pipeline. Skills are standalone, model-agnostic tools that operate on narrative drafts — they are **not** canon, not research, and not narrative prose.

## Contents

| Directory / File | What it is |
|---|---|
| `fiction-writing/` | Pre-generation canon guard + generation gate. Runs before every chapter to verify canon compliance. |
| `ai-fictional-tells-skill/` | Post-generation artifact-reduction skill (v1.0.0). Runs after every chapter to detect and minimally reduce AI fictional tells. Complete distributable unit (spec, taxonomy, frameworks, interventions, schemas, tests, examples). |
| `INTEGRATION.md` | Integration record documenting how the two skills fit together in the narrative pipeline, their invocation rules, and their effect on canon. |

## Invocation Rules

- Skills operate on **narrative drafts only** (`samur/narrative/`). They do not operate on canon files, research, or hypotheses.
- The pre-generation canon guard (`fiction-writing/`) runs **before** every chapter.
- The post-generation artifact reduction (`ai-fictional-tells-skill/`) runs **after** every chapter.
- Skill reports are persisted in `samur/05-quality/`, never in `samur/narrative/`.
- Skills are **canon-agnostic** (they do not validate canon-compliance — that is the pre-flight guard's job) and **tell-agnostic** (the pre-flight guard does not run the tell pipeline).
- Neither skill modifies canon. Their PV-5/PV-6 preservation protects the canon-consistency of a narrative draft.

## Relationship to Other Directories

- `samur/narrative/` — the prose the skills operate on
- `samur/05-quality/` — where skill reports are persisted
- `samur/02-canon/` — the world state the pre-flight guard checks against
- `AGENTS.md` §7 — the narrative quality standards that govern skill invocation
