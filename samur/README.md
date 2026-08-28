# Samur Empire — Material Map

All world material lives here. **Strict separation of research (real) and canon (fiction).**

## Directories

| Directory | Status | Contents |
|---|---|---|
| `00-audit/` | — | Repository/workspace audits. Run before major lore work. |
| `01-research/comparative/` | RESEARCH | Historical model register, transformation method, influence register. |
| `01-research/religious-systems/` | RESEARCH | Sanatan, Islam, Judaism, Christianity studied as historical systems. |
| `02-canon/` | CANON | Active canon. Only internally verified material. |
| `03-hypotheses/` | HYPOTHESIS | Working hypotheses with confirm/falsify conditions. |
| `04-questions/` | QUESTION | Open questions with stakes (including negative-space closures). |
| `CHANGELOG.md` | — | Canon change log; dependency tracking. |

## Canon File Naming

`<DOMAIN>-<NN>_<slug>.md` — the ID (e.g. `GEO-01`) is the stable reference handle used in dependency links.

| Prefix | Domain |
|---|---|
| TIM | Timeline / periodization |
| GEO | Geography & environment |
| DEM | Demography, migration, labor supply |
| DYN | Dynastic politics, legitimacy, succession, elite factions |
| ADM | Administration, provincial government |
| ECO | Revenue, currency, trade, agriculture, infrastructure |
| MIL | Military systems, war finance, logistics |
| TEC | Technology and its diffusion |
| REL | Religion and religious institutions |
| CUL | Language, culture, society, historical memory |
| FOR | Foreign powers and geopolitics |
| NS | Historical negative space (why certain things did **not** happen) |

## The -02/-03 Deepening Series

Each domain has a **-01 foundation** file (the structure) and one or more **-02/-03 deepening** files (the fixed parameters — rates, names, dates, sizes) that **resolve question clusters** (the `04-questions/` files). The current canon set (2026-08-26):

| Domain | Foundation | Deepening |
|---|---|---|
| GEO | GEO-01 (the material foundation), GEO-02 (the cities/regions/borders) | GEO-03 (the wind law — the foundational world law) |
| DEM | DEM-01 (the demography) | DEM-02 (the city tiering, the urban/rural split, the sex/age structure, the epidemic complex) |
| CUL | CUL-01 (the culture, the fixed toponymy, the historical memory) | CUL-02 (the languages + scripts, the foreign registers) |
| REL | REL-01 (the Veshna faith, the pluralism) | REL-02 (the corpus, the theology, the temple network, the revivals, the myths, the de-consecrations) |
| DYN | DYN-01 (the founding dynasty), DYN-02 (the dynastic list, the name pool) | DYN-03 (the houses + lineages, the Tarn houses, the Khor clans) |
| ADM | ADM-01 (the administration, the tiered control, the four-law pluralism) | ADM-02 (the 7 central offices, the legal codes, the Tarn tribute governance) |
| ECO | ECO-01 (the economy, the monetization chain) | ECO-02 (the tax rates, the monopoly, the mint, the pepper, the trade partners, the workshops, the irrigation) |
| MIL | MIL-01 (the military, the Khor dependency, the overstretch) | MIL-02 (the army sizes, the cavalry, the navy/marines, the artillery/metallurgy, the guilds, the logistics) |
| TIM | TIM-01 (the periodization, the Kesra Era), TIM-02 (the dated events, the causality) | TIM-03 (the master chronology — the exact KE dates, the successor states, the named reforms/battles), TIM-04 (the world's chronology — the deep timescale, the Kesra Era's position in the deep timescale), TIM-05 (the Pre-Kesra Age — the pre-imperial history, the 5 periods, the Long Night, the founding's preparation), TIM-06 (the Deep Time — the pre-record civilizational history, the strata from at least ~KE −5000, the world's strata), TIM-07 (the World's Deep Chronology — the planetary/biospheric/ecological history beneath the civilizations, the deep strata in orders, the Younging, the landlife, the great-bone), TIM-08 (the Quiet Long — the tens of thousands of years — the Quiet Land's pre-residence, the standing ecosystem without the Orenic kind in the basin), TIM-09 (the Billions of Years — the deepening of the world's own deep physical history: the planet's formation, the ocean's establishment, the landmass's drift [the Long Shifting], the biosphere's origin [ocean life first; landlife later], the standing-state intervals, the character of history changing with the age of the world) |
| FOR | FOR-01 (the foreign powers), FOR-02 (the foreign rulers) | — (the fixed dates are in TIM-03 §8) |
| TEC | TEC-01 (the technology, the dual demand) | — (the workshops' specifics are in ECO-02 §8 + MIL-02 §4) |
| NS | NS-01 (the negative space) | — |

## Canon File Template

```
# <DOMAIN>-<NN> <Title>
Status: CANON
Date: YYYY-MM-DD
Last revised: YYYY-MM-DD
Depends on: [IDs]
Dependents: [IDs]
Sources: [research file / transformation log IDs]
Influence: [influence-register row, if any]
High-impact: yes/no

## Body
## Consequences (immediate / unintended / long-term)
## Open questions raised → [QUESTION IDs]
```

## Status Rules

- Only `02-canon/` is citable as Samur fact.
- RESEARCH never becomes canon by being moved; it is **transformed** via the transformation log, and the influence register keeps the counterpart record.
- A confirmed HYPOTHESIS is promoted (changelog entry); a falsified one is marked RETIRED (changelog entry; file retained, not deleted).
- Invalidated canon is RETIRED, never deleted, and dependents are reworked in the same commit (dependency sweep).
- Every canon change ships with a `CHANGELOG.md` entry.
