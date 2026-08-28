# 01 — Adaptive suite

Fixtures: [`../fixtures/adaptive/suite.json`](../fixtures/adaptive/suite.json). Worlds are synthetic (Helwick / Lia / HousePell). No project lore.

Each scenario evaluates the **same kind of request** against T0 and T1 source states. The engine must be able to change its mind.

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
| A09 | Arena Splash appears as a **clarification** of `main` | PASS | PASS (not REQUIRES_CLARIFICATION) |
| A10 | Capital moves | PASS | BLOCK |
| A11 | Authorized canon change restores a life | BLOCK | PASS |
| A12 | Draft cited as canon, then admitted | BLOCK (admission) | PASS |
| A13 | Compatible edit, hashes move | PASS + live contract | PASS + **stale** contract |
| A14 | High-impact source hash changes | PASS | PASS + **systemic** invalidation |
| A15 | Non-high-impact source hash changes | PASS | PASS + **local** invalidation |
| A16 | Splash **contradicts** `main`; request stays on `main` | PASS | PASS_WITH_WARNINGS (`CONFLICT`) |
| A17 | Proposed Splash treated as established, then admitted on `main` | REQUIRES_CLARIFICATION | PASS (`CONFIRMED_CANON`) |
| A18 | Continue Splash storyline (developmental, labeled) | BLOCK (main charter) | PASS_WITH_WARNINGS (`PROPOSED`) |
| A19 | `main` incorporates Splash material | PASS (`PROPOSED_CANON`) | PASS (`CONFIRMED_CANON`) |
| A20 | Exploratory Splash alternate vs `main` | PASS | PASS (exploratory not CANONICAL) |
| A21 | Unresolved Splash overlaps the request | PASS | REQUIRES_CLARIFICATION |

Pass criteria: all rows green under `run_adaptive_tests.py`. A static-only contradiction detector is not enough: A03, A09, A11, A12, A13, A14, A15, A16–A21 fail unless the guard is adaptive **and** classifies Splash rather than merging or ignoring it.
