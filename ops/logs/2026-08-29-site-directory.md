# Operations Log — 2026-08-29 — `site/` Directory Creation

## Action
Created a separate top-level directory (`site/`) for the reader-facing website where the novel and chapters will be published. The directory is a separate working environment from the main project, owned by a separate agent (the website agent), not the authoring agent.

## Recovery Point
`recovery/pre-site-directory` — created at HEAD before any changes.

## Area Affected
- **New directory:** `site/` — reader-facing website environment (separate scope and ownership)
- **New file:** `site/README.md` — describes the directory's scope, ownership, boundary rules, material flow, and governance
- **Updated:** `AGENTS.md` §6 (Repository Architecture) — added `site/` to the top-level structure, separation rules, and README requirement
- **Updated:** `PROJECT.md` §6 (Repository Map) — added `site/` entry
- **Updated:** `README.md` (Repository Structure table) — added `site/` row
- **Updated:** `ops/recovery/REGISTER.md` — added two new recovery points (pre-site-directory, pre-skill-rerun)

## Design Decisions

### Naming
- **`site/`** — the standard, concise, unambiguous name for a website directory. Clearly distinct from `samur/` (the world), `skills/` (agent skills), and `ops/` (operations).

### Boundary
- The website directory is a **separate environment**, not part of the authoring system's two-space model.
- The authoring agent must not operate in `site/` or make website implementation decisions.
- The website agent must not operate outside `site/` or modify the main project's files.
- Material flow is one-directional: `samur/narrative/` → `site/` → published website.

### Documentation
- The `site/README.md` explicitly states what belongs and what does not belong in the directory.
- AGENTS.md §6.2 (Separation Rules) now includes a rule for `site/`.
- The boundary is enforced by directory separation and ownership rules.

## Verification
- Repository structure inspected before changes.
- Recovery point created before any modifications.
- All three architecture documents updated consistently.
- No canon files modified. No narrative files modified.
