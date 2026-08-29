# 07 — Failure modes (Canon Guard)

Generator and host failures this ecosystem is built against. Each has a countermeasure that is testable.

| ID | Failure | Countermeasure |
|---|---|---|
| **F-CG-01** | Misread canon | Re-resolve live sources; provenance required; WORLD-MODEL is not authority |
| **F-CG-02** | Forget canon / skip the guard | Binding: every generation request runs the gate; prior PASS is not reusable |
| **F-CG-03** | Merge contradictory sources | No union of `main` and Arena facts; classify |
| **F-CG-04** | Treat provisional as established | `CX-SPLASH-PROPOSED` / `CX-CONTAMINATION` |
| **F-CG-05** | Invent missing information | Mysteries / NOT READY / UNRESOLVED → BLOCK or REQUIRES_CLARIFICATION |
| **F-CG-06** | Resolve ambiguity incorrectly | Ambiguity is not a guessed PASS |
| **F-CG-07** | Impossible knowledge | `CX-KNOWLEDGE` |
| **F-CG-08** | Break chronology | `CX-TEMPORAL` |
| **F-CG-09** | Impossible consequences | `CX-CAUSAL`, dependency walk |
| **F-CG-10** | Treat Arena as established canon | Classification; ESTABLISHED_CANON is `main` only |
| **F-CG-11** | Ignore important Arena development | `CX-WORKING-DIRECTION` warning — not a silent PASS |
| **F-CG-12** | Silently alter established canon | BLOCK or `CANON_CHANGE_REQUIRED` |
| **F-CG-13** | Turn generated text into apparent canon | Admission protocol + contamination layer |
| **F-CG-14** | Follow a stale Generation Contract | `contract_is_stale`; post-gen refuses |
| **F-CG-15** | Generator redefines constraints | Locked contract; `CX-BYPASS` BLOCK |
| **F-CG-16** | Post-gen skipped because pre-gen passed | Lifecycle invariant: both layers |
| **F-CG-17** | False rejection of legitimate expansion | Expansion with no collision is PASS; severity model |
| **F-CG-18** | Over-block because Arena differs | Differing from Arena is not a BLOCK |

Adversarial coverage: [`../tests/04-adversarial-suite.md`](../tests/04-adversarial-suite.md).
