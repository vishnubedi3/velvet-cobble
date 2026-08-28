# 2026-08-28 — Full Repository Restructure

**Action:** Complete organizational restructure of the repository into a coherent, maintainable project hierarchy.
**Recovery point:** `recovery/pre-full-restructure`
**Area affected:** Repository architecture (top-level structure, skills consolidation, ops folder creation, AGENTS.md creation, README additions)
**Canon effect:** None. No canon files modified.

## What was done

1. **Created `AGENTS.md`** — the compulsory central operational directive file. Contains all user-established directives (the two-space model, the per-chapter authoring cycle, the canon status taxonomy, the originality protocol, the recovery point discipline, the autonomous authorial judgment rules, the no-artificial-productivity rule) plus additional directives required by the project's current state (repository architecture rules, separation rules, naming conventions, README requirements, narrative quality standards, pre-flight and post-generation pipeline, logging requirements, active research/hypothesis continuation during drafting, the current execution state).

2. **Moved `ai-fictional-tells-skill/`** from the repository root into `skills/ai-fictional-tells-skill/` — consolidating all agent skills under one directory.

3. **Created `ops/`** — dedicated operational records directory with `logs/` (agent operation logs) and `recovery/` (recovery point documentation) subfolders.

4. **Created `skills/README.md`** — documents the skills directory's purpose, contents, invocation rules, and relationships.

5. **Created `ops/README.md`** — documents the operational records directory's purpose, contents, rules, and relationships.

6. **Updated `PROJECT.md`** — §6 Repository Map updated to reflect the new structure (skills consolidated, ops added, AGENTS.md referenced); §2 updated to reference AGENTS.md as the central operational directive.

7. **Updated top-level `README.md`** — reflects the new structure with AGENTS.md as the entry point.

8. **Created this log entry** (`ops/logs/2026-08-28-full-restructure.md`).

## Verification

- All existing files preserved (no deletions; `git mv` for the skill folder, `mkdir` for new directories).
- The `samur/` internal structure unchanged (00-audit through 05-quality + narrative + CHANGELOG + CONTRADICTIONS + WORLD-MODEL + README).
- The canon files (34) unchanged.
- The narrative folder (`samur/narrative/pilot-chapter.md`) unchanged.
- The quality folder (`samur/05-quality/skill-report-pilot.md`) unchanged.
- Recovery point `recovery/pre-full-restructure` created before any changes.
