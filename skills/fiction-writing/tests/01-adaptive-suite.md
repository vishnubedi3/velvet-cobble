# 01 — Adaptive suite

Fixtures: [`../fixtures/adaptive/suite.json`](../fixtures/adaptive/suite.json). Worlds are synthetic (Helwick / Lia / HousePell). No project lore.

Each scenario evaluates the **same kind of request** against T0 and T1 source states. The engine must be able to change its mind. Arena tests distinguish **canonical truth**, **current authorial direction**, and **unfinished development**.

| ID | Change in the sources | T0 | T1 |
|---|---|---|---|
| A01 | Character later established dead | PASS (alive) | BLOCK |
| A02 | Marriage ends | PASS | BLOCK |
| A03 | Character learns a secret | BLOCK (knowledge) | PASS |
| A04 | Alliance switches | PASS | BLOCK |
| A05 | Location moves | PASS | BLOCK |
| A06 | Battle winner revised | PASS | BLOCK |
| A07 | Treaty precludes a war | PASS | BLOCK (causal) |
| A08 | New person admitted with a different role | PASS (expansion) | BLOCK |
| A09 | Arena **clarifies** `main` | PASS | PASS |
| A10 | Capital moves | PASS | BLOCK |
| A11 | Authorized canon change restores a life | BLOCK | PASS |
| A12 | Draft cited as canon, then admitted | BLOCK (admission) | PASS |
| A13 | Compatible edit, hashes move | PASS + live contract | PASS + **stale** contract |
| A14 | High-impact source hash changes | PASS | PASS + **systemic** invalidation |
| A15 | Non-high-impact source hash changes | PASS | PASS + **local** invalidation |
| A16 | Arena **contradicts** `main` | PASS | PASS_WITH_WARNINGS (`CONFLICTS`) |
| A17 | Proposed Arena treated as established, then admitted | REQUIRES_CLARIFICATION | PASS (`CONFIRMS_CANON`) |
| A18 | Continue Arena storyline (developmental, labeled) | BLOCK (main charter) | PASS_WITH_WARNINGS (`PROVISIONAL`) |
| A19 | `main` incorporates Arena material | PASS_WITH_WARNINGS (`PROPOSED`) | PASS (`CONFIRMS_CANON`) |
| A20 | Exploratory Arena alternate vs `main` | PASS | PASS (not ESTABLISHED) |
| A21 | Unresolved Arena overlaps the request | PASS | REQUIRES_CLARIFICATION |
| A22 | Follow Arena **intended** storyline without violating `main` | PASS | PASS (`AUTHORIAL_DIRECTION`) |
| A23 | Compatible with `main` but **ignores** strong Arena direction | PASS | PASS_WITH_WARNINGS |
| A24 | Arena **retcon** proposal | PASS | PASS_WITH_WARNINGS (`RETCON_PROPOSAL`) |
| A25 | Arena development **abandoned** | PASS_WITH_WARNINGS | PASS (no longer controls) |
| A26 | Competing Arena directions | PASS | REQUIRES_CLARIFICATION |
| A27 | Arena direction **changes** after a prior check | PASS | PASS_WITH_WARNINGS |
| A28 | Generated claim `presents_as_canon` | BLOCK `CX-CONTAMINATION` | PASS after admission |
| A29 | Generator `redefines_constraints` | PASS | BLOCK `CX-BYPASS` |
| A30 | Continuity ledger inverted | PASS | BLOCK `CX-CONTINUITY` |
| A33 | Expansion of a different predicate vs ledger | PASS | PASS (false-reject pressure) |

Adversarial extras (A31–A37): [`04-adversarial-suite.md`](04-adversarial-suite.md).

Pass criteria: all rows green under `run_adaptive_tests.py`.
