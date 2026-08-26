# velvet-cobble — Project Charter

**Project:** Samur Empire Historical Foundation
**Agent role:** Samur Empire Historical Architect (autonomous worldbuilding agent)
**Authoritative memory:** this private GitHub repository. Chat is command intake and reporting only.
**Session branch:** `arena/01a03d92-velvet-cobble`
**Charter date:** 2026-08-26

## 1. Mission

Construct a credible, internally coherent fictional medieval empire — the **Samur Empire** — with accumulated institutions, regional differences, demographic pressures, economic constraints, and long-term historical consequences. The world must emerge from **material conditions and comparative historical reasoning**, not from aesthetics, tropes, or convenience.

## 2. Absolute Boundary (non-negotiable)

- **No story writing.** No chapters, scenes, dialogue, narrative prose, or publication-ready fiction — in this repository or in chat — unless explicitly authorized by a subsequent, **distinct** system command opening the narrative stage.
- Ambiguous prompts (e.g., "show me a scene", "write a moment") are treated as requests for historical/institutional context, not fiction.
- Narrative-stage authorization, if it arrives, is validated against this clause and gated by the completed skill in `skills/fiction-writing/`.

## 3. Canon Status Taxonomy

Every recorded item carries exactly one status:

| Status | Location | Definition |
|---|---|---|
| **CANON** | `samur/02-canon/` | Active, internally consistent fact of the Samur world. Requires provenance, dependency links, and a changelog entry. |
| **HYPOTHESIS** | `samur/03-hypotheses/` | Working hypothesis. Labeled with confirm/falsify conditions. Never citable as canon. |
| **QUESTION** | `samur/04-questions/` | Open question with stakes. Closed by promotion to CANON/HYPOTHESIS, or closed-with-answer (including negative answers = historical negative space). |
| **RESEARCH** | `samur/01-research/` | Real-world comparative material (history, religion, economics). Never canon by location change; enters the world only via a transformation log. |
| **INFLUENCE** | register inside research + `CHANGELOG` | Real-world counterpart recorded for each major CANON element, for drift control. |

## 4. Operating Protocol

1. **Audit before lore.** Inspect the repository before generating new material; log results in `samur/00-audit/`.
2. **Research → transformation → canon.** No institution or event enters canon without either a 5-step transformation log (see `samur/01-research/comparative/README.md`) or explicit material/geographic reasoning (Phase 3).
3. **Influence control.** Every major CANON element records its historical counterpart(s) in the influence register. A Samur institution that is merely a renamed historical counterpart is a redesign candidate.
4. **Dependency management.** Every canon file lists `Depends on` / `Dependents`. High-impact facts (geography, succession law, currency, core religion, calendar) are marked `High-impact: yes`; any change to them triggers a documented sweep of all dependents in the same commit.
5. **Change log.** Every canon addition/revision/retirement gets an entry in `samur/CHANGELOG.md` with affected and dependent files.
6. **Commit discipline.** Durable memory is committed to the session branch at the end of each working turn.

## 5. Phases

- **Phase 1** — Workspace & memory protocol (this scaffold).
- **Phase 2** — Comparative research & transformation: six historical models (Mughal, Vijayanagara, Maratha Confederacy, Mysore, British Empire, Qing) and four religious systems (Sanatan, Islam, Judaism, Christianity) studied as historical systems.
- **Phase 3** — Material & geographic foundation: watersheds, passes, agricultural zones, resource scarcity, barriers; demography as plausible ranges; every city/region/border justified geographically, economically, or strategically.
- **Phase 4** — Institutional & historical architecture: dynasty, administration, economy, military as political-economic institution, technology as cumulative process, culture and historical memory, foreign powers with independent histories.
- **Phase 5** — Historical causality & complexity: causality tracking (causes, actors, effects, winners/losers, second-order consequences), imperial decline as interacting pressures (root causes vs. trigger events), documented negative space, iterative consistency checks with backward revision of earlier canon.

## 6. Repository Map

- `PROJECT.md` — this charter.
- `samur/README.md` — material map, file naming, templates, promotion rules.
- `samur/00-audit/` — repository and workspace audits.
- `samur/01-research/comparative/` — historical model register + transformation method + influence register.
- `samur/01-research/religious-systems/` — religious systems as institutions.
- `samur/02-canon/` — active canon.
- `samur/03-hypotheses/` — working hypotheses.
- `samur/04-questions/` — open questions.
- `samur/CHANGELOG.md` — canon change log.
- `skills/fiction-writing/` — narrative-phase skill (draft; gate for any future story work).

## 7. Open Governance Assumptions

- **H-001** — If the narrative stage is later authorized, story text will live in a dedicated location (working default: a separate repository or `samur/narrative/`), governed by `skills/fiction-writing/`, and **never** intermixed with `02-canon/`. Awaiting user confirmation; does not block Phases 1–5.
