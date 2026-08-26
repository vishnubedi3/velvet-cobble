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
