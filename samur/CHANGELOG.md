# Canon Change Log

One entry per canon change (add / revise / retire), newest first. Each entry records: date, affected files, dependent files updated (or flagged), reason, and — for high-impact changes — the dependency-sweep notes.

## 2026-08-26

- **Phase 4 begins — DYN-01 (The Founding Dynasty).**
  - Added `02-canon/DYN-01_founding_dynasty.md` (CANON, high-impact): the **material founding** (the Samur's position at the Sareth/Oren/bār junction — control of the chokepoint + the fiscal base, not a purely military conquest); the **unification** (absorbing the chiefs into a revenue-military system, controlling the Oren, co-opting the Veshna temple); the **dual founding structure** — **the King (the House of Kesra, the legitimacy) + the Shreshtha (the prime-ministerial/regent office, the power — a salaried, non-hereditary office)** with **the temple (the Veshna matha) as the sanctioner** (the consecration, the arbitrator/kingmaker); the **qualified elective-hereditary succession** (a **three-way contest**: the house, the Shreshtha, the temple — the "eldest vs. the most worthy" fault line); the **five elite factions** (the dynasty, the Shreshtha, the temple, the chiefs, the merchant/bankers); the **composite legitimacy** (the heartland + the temple + the military + the fiscal base); the **founding-status dual elite** (the founding Samur vs. the absorbed chiefs — by founding status, not ethnicity).
  - Transformation log: `transformations/DYN-01.md`. **Influence Register:** DYN-01 row added; drift check passed (the dual structure is a *founding feature*, the temple is the *sanctioner*, the dual elite is by *founding status*, the succession is a *three-way contest*).
  - **Questions:** Q-012 (the founding Shreshtha), Q-013 (the consecration mechanism), Q-014 (the royal house size), Q-015 (the chiefs' initial districts).
  - Dependency sweep: GEO-01/GEO-02/DEM-01 unchanged (DYN-01 depends *on* them; no contradiction). No canon revised or retired.
  - **Named entities (provisional, to be fixed in CUL-01):** **Kesra I** (the founding king; the capital **Kesra** bears his name), the **House of Kesra** (the royal house), the **Shreshtha** (the prime-ministerial/regent office), the **Veshna matha** (the temple / the priestly council).
  - **Phase 4 status:** DYN-01 (the dynasty structure) done. Next: **TIM-01** (the periodization — founding / expansion / high empire / decline / fragmentation) and the remaining Phase 4 domains (ADM-01, ECO-01, MIL-01, REL-01, CUL-01, FOR-01, TEC-01).

- **Phase 3 continued — GEO-02 (cities/regions/borders) + DEM-01 (demography).**
  - Added `02-canon/GEO-02_cities_regions_borders.md` (CANON, high-impact): the **seven regions** under **direct / garrison / tribute (+ port) control**; the **eight cities**, each justified (Kesra — capital at river + mountain in the bār core; Veshna — temple city; Besra — grain market / fiscal hub; Threna — main-pass fortress; Gheshar — second-pass waystation; Keshkhor — northern horse emporium; Voren — delta port / maritime hub; Kesveth — Veth port); the **three Sareth passes** (Thren / Vesh / Ghul Gates — defense and trade separated by pass); the **four border kinds** (wall / open steppe / tribute plain / contested coast). **Key structural tension:** the political capital (Kesra) and the economic/maritime hub (Voren) are *different cities* — the economic center of gravity sits at the coast.
  - Added `02-canon/DEM-01_demography.md` (CANON, high-impact): population **~25–40 million** (plausible range, calibrated to Mughal/Qing scale); **~70–80% concentrated in the bār core + pell coast** on ~50% of the land; the **borders thin** (small, expensive garrison); migration corridors (the Oren highway; the Sareth passes; the Khor pastoral mobility); the **famine → debt → revolt chain** tied to the failed wind (Q-004); the **river/sea epidemic** (once in a generation or two); the **cyclical labor supply** as a root-cause input to the Phase 5 decline.
  - Transformation logs: `transformations/GEO-02.md`, `transformations/DEM-01.md`. **Influence Register:** GEO-02 and DEM-01 rows added; drift checks passed (GEO-02: capital ≠ maritime hub + four-kind border; DEM-01: wind-dependent labor supply interacting with the three-front overstretch).
  - **Questions:** Q-001 **RESOLVED** → GEO-02 §3 (three main passes). New: Q-006 (city size/tiering), Q-007 (ethnic/linguistic composition), Q-008 (Tarn practical control, refines Q-003), Q-009 (urban/rural split), Q-010 (sex/age structure), Q-011 (plague nature).
  - Dependency sweep: GEO-01 unchanged (GEO-02/DEM-01 depend *on* it; no contradiction found in cross-check). No canon revised or retired.
  - **Phase 3 status: material/geographic + demographic foundation COMPLETE.** Phase 4 (institutional & historical architecture) is unblocked: DYN-01, ADM-01, ECO-01, MIL-01, REL-01, CUL-01, FOR-01, TEC-01, TIM-01.

- **Phase 3 begins — first canon: GEO-01 (Material & Geographic Foundation).**
  - Added `02-canon/GEO-01_material_geographic_foundation.md` — **the first CANON file** (root domain; `High-impact: yes`). Defines: Veshran; the Oren watershed (Khel/Tarn; the delta mouth as chokepoint + reverse-invasion axis); the Sareth west wall + passes (Q-001); the bār/pell dual-crop core–periphery food divide; the resource-scarcity map (horses=north, iron/timber=west, silver=north+west, salt, coastal goods); the natural barriers; the seasonal wind (wet/dry; the military and fiscal calendar); and the six strategic consequences (three-front condition, standing frontier, tributary-east fragmentation site, monetization chain, the Vethra "too big" neighbor, the Phre chartered-company delta access).
  - Ran the 5-step transformation: `01-research/comparative/transformations/GEO-01.md` (new `transformations/` directory; method note added to the comparative README).
  - **Influence Register:** first row added (GEO-01). Drift check passed — the load-bearing difference is that the scarce resources lie on *several different borders* (no single dominant frontier), unlike the Mughal/Qing.
  - **New open questions:** Q-001 (Sareth passes), Q-002 (Khor structure), Q-003 (Tarn plain polity), Q-004 (wind variability), Q-005 (Veth pepper) — entries recorded in `04-questions/`.
  - **Named entities introduced (provisional, to be fixed in CUL-01):** Veshran (continent); the Oren (great river), the Khel, the Tarn (tributaries); the Sareth (west wall); the Khor (north steppe); the Veth shore; **Vethra** (the compact southern state); **the Phre** (the distant maritime power); **bār** / **pell** (the two staple grains); the Samur (founding people / upper Oren plateau heartland).
  - Dependency sweep: none yet (GEO-01 is the root; dependents not yet written). No canon revised or retired.

- **Phase 2 — comparative research (mechanism libraries).** Added RESEARCH files for the six required historical models and four required religious systems:
  - `01-research/comparative/`: `mughal.md`, `vijayanagara.md`, `maratha.md`, `mysore.md`, `british.md`, `qing.md`.
  - `01-research/religious-systems/`: `sanatan.md`, `islam.md`, `judaism.md`, `christianity.md`.
  - Each file: material foundation → institutions → mechanisms → unintended consequences → **mechanisms available for Samur transformation** (§5). Memory-based; load-bearing figures/dates flagged **[verify]**.
  - Updated both register READMEs to **DRAFT v1** with the extracted-mechanism index.
  - Canon created: **none** (research is not canon by location change; no transformation log run yet). Dependencies swept: none.
  - **Influence Register** remains empty — it populates as the first *transformation logs* are run (Phase 3 material/geographic foundation is the first target, since all other domains depend on it).

- **Phase 1 scaffold.** Added `PROJECT.md`, `samur/` directory tree (audit, research registers, canon/hypothesis/question directories, this changelog), `skills/fiction-writing/` draft, updated root `README.md`.
  - Canon created: none. Dependencies swept: none.
  - Audit record: `samur/00-audit/2026-08-26-phase1-repository-audit.md`.
  - Key finding: repository contained only `README.md`; no pre-existing canon, research, or fiction-writing skill. Skill gate for the narrative stage: BLOCKED (draft foundation committed; completion required before any narrative work).
