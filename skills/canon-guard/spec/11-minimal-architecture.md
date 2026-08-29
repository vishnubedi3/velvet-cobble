# 11 — Minimal architecture

Enough to host the ecosystem without an LLM.

Required:

- Git (or equivalent) to read current `main` and `arena/*` trees
- Structured `GenerationRequest` claims
- [`../reference/canon_guard.py`](../reference/canon_guard.py): `run`, `post_verify`, `classify_splash_material`, `detect_changes`, `contract_is_stale`, `admit`

Not required: vendor SDK, database, copied canon, frozen fact table.

Minimum knowledge load: `SKILL.md`, `BRANCH_RELATIONSHIP.md`, `DECISION_PROTOCOL.md`, `GENERATION_CONTRACT.md`, `TRUST.md`, `ECOSYSTEM.md`.
