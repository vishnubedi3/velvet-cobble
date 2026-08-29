# Operations Log — 2026-08-29 — `site/` Independent Project Scaffold

## Action
Created the independent project scaffold inside `site/` — the foundational files that the future website agent will need to begin its own work. Added the permanent boundary directive to the root `AGENTS.md` (§6.5).

## Recovery Point
`recovery/pre-site-scaffold`

## Files Created (inside `site/`)
- `site/AGENTS.md` — empty scaffold (reserved for website agent's operational directives)
- `site/PROJECT.md` — empty scaffold (reserved for website agent's project charter)
- `site/README.md` — minimal (establishes independence and the one practical relationship)
- `site/.gitignore` — basic build output patterns (non-stack-specific)

## Files Modified (root project)
- `AGENTS.md` — §6.5 "Website Directory Isolation" added (permanent boundary directive)
- `ops/recovery/REGISTER.md` — new recovery point documented

## Boundary Directive
The root `AGENTS.md` now contains an explicit, permanent directive (§6.5) that the authoring agent must not operate in, reference, inspect, or acknowledge `site/` during normal authoring work. The only permitted interaction is making approved narrative material available in `samur/narrative/` for the website agent to consume.

## No Assumptions Made
No tech stack, framework, deployment target, directory structure, or governance model was assumed or imposed. The website agent will define everything independently.
