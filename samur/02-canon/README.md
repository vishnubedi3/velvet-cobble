# Active Canon

The **only** directory whose contents may be cited as Samur fact.

## Promotion rules

Material enters CANON only when:

1. It derives from a transformation log (Phase 2 method) or from explicit material/geographic reasoning (Phase 3), and
2. It passes an internal-consistency check against all existing canon (dependencies listed and verified), and
3. A `CHANGELOG.md` entry records the addition and any dependent updates.

## File template

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

## Retirement

Canon that is invalidated is **never deleted**: status becomes RETIRED with a reason and a changelog entry, and all dependents are reworked in the same commit.
