# `site/` — Reader-Facing Website

**Status:** SCAFFOLD — directory established; implementation not yet begun
**Date:** 2026-08-29
**Scope:** Website development and reader presentation only
**Ownership:** A separate agent (the website agent)
**Relationship to the main project:** Consumer of approved narrative material; not part of the authoring system

---

## Purpose

This directory is the working environment for the reader-facing website where the novel and chapters of *The Wind's Record* will be published. It is a **separate working environment** from the main project.

## Boundary

### What belongs here

- Website source code (HTML, CSS, JavaScript, templates, build tooling)
- UI/UX design decisions and implementation
- Deployment configuration and infrastructure
- Reader-facing presentation of approved narrative material
- Static assets for the website (images, fonts, stylesheets)
- Website-specific documentation (build instructions, deployment guides)

### What does NOT belong here

- **Canon** — the authoritative world state lives in `samur/02-canon/`
- **Lore and worldbuilding** — the world's development lives in `samur/`
- **Research** — comparative historical material lives in `samur/01-research/`
- **Narrative development** — the novel's drafting lives in `samur/narrative/`
- **Quality analysis** — skill reports live in `samur/05-quality/`
- **Agent skills** — the authoring system's skills live in `skills/`
- **Operational records** — agent logs live in `ops/`

This directory is **not** part of the authoring system. It does not participate in the two-space model (Expansion Space / Drafting Space). It does not follow the canon protocol. It is not governed by `AGENTS.md` — it is governed by the website agent's own directives.

## Material Flow

The website may **consume** approved narrative material for publication. The flow is one-directional:

```
samur/narrative/  →  site/  →  published website
   (source)        (build)     (output)
```

- **Source:** `samur/narrative/` contains the canonical prose (the pilot chapter, future chapters).
- **Build:** `site/` transforms the source into reader-facing output (web pages, reading interface).
- **Output:** The published website is the reader's experience.

The website agent must not modify `samur/narrative/` or any other directory outside `site/`. The authoring agent must not modify `site/` or make website implementation decisions.

## Governance

- The **authoring agent** (governed by `AGENTS.md`) develops the world and the novel in `samur/`, `skills/`, and `ops/`.
- The **website agent** (governed by its own directives) develops the website in `site/`.
- The boundary is enforced by directory separation and by the rule that neither agent operates in the other's environment.

## Naming

The directory is named `site/` — the standard, concise, unambiguous name for a website directory in a project repository. It is clearly distinct from:

- `samur/` — the world + the novel
- `skills/` — agent skills
- `ops/` — operational records
