# 08 — Lifecycle invariants

Normative. Skipping a transition is a failed run.

```
SOURCE BRANCHES → OBSERVATION → RESOLUTION → CLASSIFICATION
 → DEPENDENCY MODEL → REQUEST ANALYSIS → PRE-GENERATION GUARD
 → LOCKED CONTRACT → GENERATION → POST-GENERATION VERIFICATION
 → ADMISSION / REJECTION → UPDATED BRANCH STATE → RE-RESOLUTION
```

| ID | Invariant |
|---|---|
| **L-1** | Pre-generation always runs. A prior PASS is not a skip. |
| **L-2** | The contract is bound to `canon_state_id` + source hashes. |
| **L-3** | The generator cannot mutate the contract. |
| **L-4** | Post-generation uses the **same** Canon State identity as pre-generation. If that identity is stale vs live branches, stop and re-resolve. |
| **L-5** | Post-generation never replaces pre-generation. |
| **L-6** | PASS of either layer does not admit material to `02-canon/`. |
| **L-7** | Arena is classified every time it is live; it is never unlabeled established canon. |
| **L-8** | Local source changes do not force systemic invalidation; high-impact changes do. |

Reference core: `run` (pre) and `post_verify` (post) in [`../reference/canon_guard.py`](../reference/canon_guard.py).

Audit of gaps closed in this expansion: [`13-architectural-audit.md`](13-architectural-audit.md).
