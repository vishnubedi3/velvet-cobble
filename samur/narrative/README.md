# `narrative/` — The Novel

This directory is the canonical location for all narrative prose: the pilot chapter and all future novel chapters. It contains **only clean, reader-facing prose** — no reports, no analysis outputs, no lore documents.

## Purpose

The narrative folder holds the novel. The world (`02-canon/`) holds the lore. The quality folder (`05-quality/`) holds the analysis. These three are separate by design:

- **`02-canon/`** — the world's authoritative state (the load-bearing facts).
- **`narrative/`** — the novel's prose (the reader's experience).
- **`05-quality/`** — the quality analysis (the craft substrate).

Draft material in this folder is **not canon**. New lore that emerges during drafting is evaluated against established canon, integrated through the standard process, and persisted in `02-canon/` — never forced into the narrative folder as worldbuilding.

## Contents

| File | What it is |
|---|---|
| `pilot-chapter.md` | The pilot chapter (revised after `ai-fictional-tells-skill` post-generation pass). Status: PILOT — not canon, not Chapter One. A complete narrative artifact for user review. |

## Naming convention

- **Pilot:** `pilot-chapter.md`
- **Chapters:** `ch<NN>-<slug>.md` — e.g., `ch01-the-spring.md`, `ch02-the-passes.md`. The number is the chapter's position in the novel's sequence; the slug is a short descriptive identifier.

## Governance

- Story text is governed by `skills/fiction-writing/` (the pre-generation canon guard) and `ai-fictional-tells-skill` (the post-generation artifact-reduction layer). Integration documented at `skills/INTEGRATION.md`.
- The pre-flight canon check runs before every chapter. The post-generation skill pass runs after every chapter. Reports are persisted in `05-quality/`.
- The novel's identity is an interconnected lattice — not forced into a single central premise. The title is not named prematurely (it emerges from the completed work's identity).
- Chapter One requires explicit user authorization (§23 of the Sumur Master Authoring Protocol). The pilot is not Chapter One.

## Relationship to canon

The narrative uses the current canonical world state but does not freeze it. Drafting and world development operate concurrently (Expansion Space + Drafting Space). When drafting reveals a legitimate requirement for new worldbuilding, the lore is developed in `02-canon/`, verified, and persisted — then the narrative draws on it naturally.
