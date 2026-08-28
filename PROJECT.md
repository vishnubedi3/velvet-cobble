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
- Narrative-stage authorization, if it arrives, is validated against this clause and gated by the narrative-stage capabilities: the **pre-generation canon guard** (`skills/fiction-writing/`) and the **post-generation artifact-reduction skill** (`ai-fictional-tells-skill`, on `main`; integrated per `skills/INTEGRATION.md`).

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
- **Phase 5.5 — Deep chronology (2026-08-28; continuing):** the world's history beyond the six epochs and the Pre-Kesra Age — **TIM-04** (the deep timescale: the Kesra Era as the most recent slice; the pre-imperial history's existence), **TIM-05** (the Pre-Kesra Age: the attested pre-epoch from the record's horizon ~KE −1200 → KE 0; the 5 periods; the Long Night; the founding's causal structure — **Q-083 RESOLVED**), **TIM-06** (the Deep Time: the pre-record civilizational history from **at least ~KE −5000** — the strata; the world's strata — the world's chronology **deeper than its civilizations**; the record's horizon as a survival horizon), **TIM-07** (the World's Deep Chronology: the planetary/biospheric/ecological history beneath the civilizations — the necessary depth in orders: the planet **billions of years**, the ocean billions [the world's oldest continuous life is the sea's], the landmass billions → the current arrangement [**the Younging**] millions, the wind law's current regime millions, the landlife's current lineages millions [the bār/pell duality as the landlife's answer to the wind law; the **great-bone's** extinction], the current ecosystems [the Quiet Land] hundreds of thousands — the **six epochs are a small portion** of the world's total history; the precise deep dates NOT fixed [no false precision]; the no-Earth rule [no real geological era renamed; no real evolutionary history transplanted; the great-bone a generic deep class] — **Q-084 REFINED**: the relative strata + the orders ESTABLISHED, the precise ages NOT READY), **TIM-08** (the Quiet Long: the **tens of thousands of years** — the Quiet Land's **pre-residence** — the standing ecosystem [the current ecosystem] **without** the Orenic kind in the basin; the current ecosystem stood for the tens of thousands of years before the Orenic kind's residence in the basin [from at least ~KE −5000]; the **order-sequence is now complete** [billions → millions → hundreds of thousands → **tens of thousands** → thousands]; the character of history changes with the age of the world [the millions [ecological] → the tens of thousands [the standing ecosystem without the Orenic kind] → the thousands [civilization-like]]; the Quiet Land divided into its pre-residence [the Quiet Long] + its residence [the thousands of years]; the NOT READYs preserved [the Orenic kind's pre-basin history; the precise timing of the Orenic kind's residence in the basin]), **TIM-09** (the Billions of Years: the deepening of the world's own deep physical history — developed **more than a summary** [the no-compression rule] — the planet's formation [the Formative Deep], the ocean's establishment [a large warm sea — the known sea's ancestor], the landmass's drift [the Long Shifting — the landmass drifts into its current position relative to the ocean, producing the Sareth wall, the Oren's current course, the delta, the coast, the steppe — the current arrangement [the Younging] is the Long Shifting's terminal event], the biosphere's origin [**ocean life first** — billions of years — the world's oldest continuous life; **landlife later** — millions of years]; the **standing-state intervals** [the no-constant-activity rule — the billions of years contain immense stretches in which little relevant change occurs]; the **character of history changes with the age of the world** [the billions of years [planetary/oceanic/geological/biological] → the millions of years [geological/ecological] → the hundreds of thousands of years [ecological] → the tens of thousands of years [the standing ecosystem] → the thousands of years [civilization-like] — the no-intelligence-throughout rule]; the **world's own "plate tectonics" equivalent is a deep unknown** [the no-Earth rule — the no named plate mechanism]; the NOT READYs preserved [the precise deep dates; the specific mechanism of the landmass's drift; the deep sea's life]). **Initial expansion gate (2026-08-28):** the full-round expansion + the complete cross-check (PASS) are complete — `00-audit/2026-08-28-initial-cross-check.md` — the **Initial Drafting Gate is READY**; the narrative stage remains gated on the user's explicit authorization (per §2). The project direction it records: the world's civilizational history extends to at least 5,000 years (an established **minimum**, not an upper boundary — the deep chronology continues beneath it, into the world's planetary/biospheric history); the world's chronology is deeper than its civilizations; the six epochs occupy only the position the established canon warrants (the deep canon is built beneath them, not over them); the novel's identity/title is **not named prematurely** (a working designation until the completed work's identity demonstrates the title — original, native to this project).
- **Narrative stage (BLOCKED)** — story writing, authorized **only** by a distinct system command (see §2). Governed by the pre-generation canon guard (`skills/fiction-writing/`) and the post-generation `ai-fictional-tells-skill` (artifact reduction; see `skills/INTEGRATION.md`). The initial expansion gate is complete and certified (`00-audit/2026-08-28-initial-cross-check.md` §4); the drafting constraints in force are recorded there.

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
- `skills/fiction-writing/` — narrative-phase skill (draft; pre-generation canon guard + gate for any future story work).
- `skills/INTEGRATION.md` — integration record for the `ai-fictional-tells-skill` (post-generation artifact-reduction; the skill folder itself is on `main` at `ai-fictional-tells-skill/`).

## 7. Open Governance Assumptions

- **H-001** — If the narrative stage is later authorized, story text will live in a dedicated location (working default: a separate repository or `samur/narrative/`), governed by `skills/fiction-writing/`, and **never** intermixed with `02-canon/`. Awaiting user confirmation; does not block Phases 1–5.
