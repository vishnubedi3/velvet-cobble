# velvet-cobble — Project Charter

**Project:** The Wind's Record
**Codename:** WINDLAW
**Repository:** `velvet-cobble` (platform-assigned identifier; the project's codename is WINDLAW)
**Agent role:** Autonomous worldbuilding and novel-drafting agent
**Authoritative memory:** this private GitHub repository. Chat is command intake and reporting only.
**Operational directive:** `AGENTS.md` (compulsory — governs all agent operations)
**Session branch:** `arena/01a04822-velvet-cobble`
**Charter date:** 2026-08-26

> **Project identity.** "The Wind's Record" is the name of the complete project. The project encompasses a fictional world with genuine deep time (billions of years of planetary, biospheric, ecological, and civilizational history), the novel that emerges from that world, and the autonomous authoring system that develops both concurrently. The **Samur Empire** is one element within the project's world — a fictional medieval empire constructed from material conditions and comparative historical reasoning. The project is far larger than any single empire within it.

## 1. Mission

Construct a credible, internally coherent fictional medieval empire — the **Samur Empire** — with accumulated institutions, regional differences, demographic pressures, economic constraints, and long-term historical consequences. The world must emerge from **material conditions and comparative historical reasoning**, not from aesthetics, tropes, or convenience.

## 2. Absolute Boundary (narrative-stage governance)

- **Narrative stage is authorized** for the pilot chapter (2026-08-28, per the Sumur Master Authoring Protocol). Chapter One requires explicit user authorization (§23 of the protocol).
- All narrative prose lives in `samur/narrative/` — **never** intermixed with `02-canon/`.
- Quality analysis reports live in `samur/05-quality/` — **never** in `samur/narrative/`.
- Narrative-stage work is governed by: the pre-generation canon guard (`skills/fiction-writing/`), the post-generation artifact-reduction skill (`skills/ai-fictional-tells-skill/`), and the full operational directive in `AGENTS.md`.

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
- **Phase 5.5 — Deep chronology (2026-08-28; continuing):** the world's history beyond the six epochs and the Pre-Kesra Age — **TIM-04** (the deep timescale: the Kesra Era as the most recent slice; the pre-imperial history's existence), **TIM-05** (the Pre-Kesra Age: the attested pre-epoch from the record's horizon ~KE −1200 → KE 0; the 5 periods; the Long Night; the founding's causal structure — **Q-083 RESOLVED**), **TIM-06** (the Deep Time: the pre-record civilizational history from **at least ~KE −5000** — the strata; the world's strata — the world's chronology **deeper than its civilizations**; the record's horizon as a survival horizon), **TIM-07** (the World's Deep Chronology: the planetary/biospheric/ecological history beneath the civilizations — the necessary depth in orders: the planet **billions of years**, the ocean billions [the world's oldest continuous life is the sea's], the landmass billions → the current arrangement [**the Younging**] millions, the wind law's current regime millions, the landlife's current lineages millions [the bār/pell duality as the landlife's answer to the wind law; the **great-bone's** extinction], the current ecosystems [the Quiet Land] hundreds of thousands — the **six epochs are a small portion** of the world's total history; the precise deep dates NOT fixed [no false precision]; the no-Earth rule [no real geological era renamed; no real evolutionary history transplanted; the great-bone a generic deep class] — **Q-084 REFINED**: the relative strata + the orders ESTABLISHED, the precise ages NOT READY), **TIM-08** (the Quiet Long: the **tens of thousands of years** — the Quiet Land's **pre-residence** — the standing ecosystem [the current ecosystem] **without** the Orenic kind in the basin; the current ecosystem stood for the tens of thousands of years before the Orenic kind's residence in the basin [from at least ~KE −5000]; the **order-sequence is now complete** [billions → millions → hundreds of thousands → **tens of thousands** → thousands]; the character of history changes with the age of the world [the millions [ecological] → the tens of thousands [the standing ecosystem without the Orenic kind] → the thousands [civilization-like]]; the Quiet Land divided into its pre-residence [the Quiet Long] + its residence [the thousands of years]; the NOT READYs preserved [the Orenic kind's pre-basin history; the precise timing of the Orenic kind's residence in the basin]), **TIM-09** (the Old Sea: the **world's deepest chronology** — the billions of years beneath the landlife's current lineages **developed, not compressed** — the **Bare World** [the world's first standing state — before the sea; no life; the wind itself], the **Old Sea** [the ocean's billions — the ocean's establishment as the world's first great transition; the **world's first life is the sea's life**; the sea's life as the world's *only* life through the deep middle; the sea endures the Long Shifting], the **Taking of the Land** [the landlife's origin — the life from the sea takes the landmasses, during the Long Shifting], the **Earlier Landlife's Long** [the earlier arrangements' landlife — the great-bone's world — until the Younging's completion]; the **causal continuity** [the world's one life — the sea's line: the ocean's life → the Taking of the Land → the earlier landlife → the current lineages' ancestors → the current lineages]; the character of history changes with the age of the world [physical → oceanic-biological → land-biological → ecological → standing-ecosystem → civilization-like]; no civilizations/kingdoms/wars/rulers/intelligent societies anywhere in the deep; the deep record layer extended [the **stone's sea-shells** — "**the stone remembers the sea**"; the old bone's deeper reading]; the precise deep dates NOT fixed [no false precision]; the no-Earth rule [no Earth geological era renamed; no Earth evolutionary history transplanted; no Earth planetary history reproduced]), **TIM-10** (the Long Shifting: the **landmasses' deep drift** — the world's land-sea arrangements through deep time — the last billions-of-years deep period **developed, not compressed** — the **First Lands** [the earliest enduring arrangements; the first coastlines; no landlife], the **Deep Drift** [the long middle — the slow reassembly; the sea's reshaping; the wind regimes changing — gone; the landlife's era within it], the **Deep Shifts** [the few major reassemblies — the world's own class of deep land-reassembly transitions — each reshaping the arrangements, the sea, the climate, and the landlife], the **Terminal Drift** [the approach to the Younging] → the **Younging** [the current arrangement — the terminal event — preserved]; the **causal continuity** [the sea endures all; the land's substance persists; the landlife is carried by the drift; the **current arrangement is young** — the drift's terminal product — the no-current-assumption rule, realized]; the character of history changes with the age of the world [physical → land-biological → ecological → standing-ecosystem → civilization-like]; no civilizations/kingdoms/wars/rulers/intelligent societies anywhere in the Long Shifting; the deep record layer extended [the **old-land strata** — "**the old land lies under the new**" — the old stone's geological stratum's three visible levels]; the precise deep dates NOT fixed [no false precision]; the no-Earth rule [no Earth plate mechanism; no Pangaea; no named Earth supercontinent/orogeny/rift/subduction]). **Initial expansion gate (2026-08-28):** the full-round expansion + the complete cross-check (PASS) are complete — `00-audit/2026-08-28-initial-cross-check.md` — the **Initial Drafting Gate is READY**; the narrative stage remains gated on the user's explicit authorization (per §2). The project direction it records: the world's civilizational history extends to at least 5,000 years (an established **minimum**, not an upper boundary — the deep chronology continues beneath it, into the world's planetary/biospheric history); the world's chronology is deeper than its civilizations; the six epochs occupy only the position the established canon warrants (the deep canon is built beneath them, not over them); the novel's identity/title is **not named prematurely** (a working designation until the completed work's identity demonstrates the title — original, native to this project). **TIM-03 integration (2026-08-28):** the Master Chronology now anchors the full deep chain — the **deep chronology anchors (TIM-03 §0)**, from the planet's formation to the record's horizon (~KE −1200), as orders + relative order (the precise deep dates NOT fixed — the no-false-precision rule; the in-world epistemology preserved); the master chronology is **one chronology with two epistemologies** (the deep relative + the KE-era exact); **no KE-era fact revised** (the integration is additive — the §1–§11 unchanged).
- **Narrative stage (BLOCKED)** — story writing, authorized **only** by a distinct system command (see §2). Governed by the pre-generation canon guard (`skills/fiction-writing/`) and the post-generation `ai-fictional-tells-skill` (artifact reduction; see `skills/INTEGRATION.md`). The initial expansion gate is complete and certified (`00-audit/2026-08-28-initial-cross-check.md` §4); the drafting constraints in force are recorded there.

## 6. Repository Map

See `AGENTS.md` §6 for the full architectural specification. Summary:

- **`AGENTS.md`** — the central operational directive (compulsory; governs all agent operations).
- **`PROJECT.md`** — this charter (mission, phases, taxonomy).
- **`README.md`** — top-level overview.
- **`samur/`** — the world + the novel:
  - `00-audit/` — repository and workspace audits.
  - `01-research/` — real-world comparative research (active during drafting).
  - `02-canon/` — active canon (34 files; the authoritative world state).
  - `03-hypotheses/` — working hypotheses (active during drafting).
  - `04-questions/` — open questions (87 total).
  - `05-quality/` — narrative quality analysis reports.
  - `narrative/` — the novel (clean prose only; pilot chapter + future chapters).
  - `CHANGELOG.md` — canon change log.
  - `CONTRADICTIONS.md` — active contradictions register.
  - `WORLD-MODEL.md` — authoritative one-page summary.
- **`skills/`** — all agent skills:
  - `fiction-writing/` — pre-generation canon guard.
  - `ai-fictional-tells-skill/` — post-generation artifact reduction (v1.0.0).
  - `INTEGRATION.md` — skill integration record.
- **`ops/`** — operational records:
  - `logs/` — agent operation logs.
  - `recovery/` — recovery point documentation.

## 7. Open Governance Assumptions

- **H-001** — Story text lives in `samur/narrative/`, governed by `skills/fiction-writing/` (pre-generation canon guard) and `ai-fictional-tells-skill` (post-generation artifact reduction), and **never** intermixed with `02-canon/`. Quality analysis reports live in `samur/05-quality/`, **never** in `samur/narrative/`. **Confirmed** (2026-08-28: the narrative stage is authorized for the pilot; the directory structure is established).
