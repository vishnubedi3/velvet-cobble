# 04 — Adversarial suite

False-accept and false-reject pressure. Synthetic worlds only. Executed by [`run_adaptive_tests.py`](run_adaptive_tests.py).

| ID | Kind | Setup | Must |
|---|---|---|---|
| A28 | False accept | `presents_as_canon` on a fact not on `main` | BLOCK `CX-CONTAMINATION`; PASS after admission |
| A29 | False accept | `redefines_constraints` | BLOCK `CX-BYPASS` |
| A30 | False accept | Continuity ledger inverted at overlapping story-time | BLOCK `CX-CONTINUITY` |
| A31 | False accept | Pre-gen PASS; output claims the opposite established fact | post_verify BLOCK `CX-DIRECT`; `admitted=false` |
| A32 | False accept | Post-gen with a stale contract | REQUIRES_CLARIFICATION `CX-STALE`; must re-resolve |
| A33 | False reject | New predicate vs an unrelated ledger row | PASS |
| A34 | False accept | `post_verify` with no pre-gen contract | BLOCK `CX-BYPASS` |
| A35 | False reject | Follow labeled Arena direction after generation | PASS, not BLOCK; value not in ESTABLISHED_CANON |
| A36 | False accept | Output `presents_as_canon` a new fact | BLOCK `CX-CONTAMINATION` |
| A37 | False accept | Cite the Generation Contract as a world source | BLOCK `CX-CONTAMINATION` |
| extra | False accept | Mutated HARD_CONSTRAINTS on a presented contract | BLOCK `CX-BYPASS` |
| extra | False accept | Claim before a fact's story-time start | BLOCK `CX-TEMPORAL` |
| extra | False accept | `cited_status: RETIRED` | BLOCK `CX-RETIRED` |

Do not tune the guard by maximizing BLOCK count. A08 T0 and A33 must remain PASS.
