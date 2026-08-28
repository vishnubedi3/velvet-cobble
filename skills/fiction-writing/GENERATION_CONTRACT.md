# GENERATION_CONTRACT.md

A Generation Contract is permission to generate **against one evaluated Canon State**. It is not a replacement for the branches. It is not durable canon.

Schema: [`schemas/generation-contract.schema.json`](schemas/generation-contract.schema.json).

---

## 1. When it exists

Emitted only with `PASS` or `PASS_WITH_WARNINGS`. Other decisions emit no contract.

---

## 2. Required fields

| Field | Content |
|---|---|
| `canon_state_id` | Identity of the evaluated Canon State |
| `branch_context` | Applicable branch, commit, and any reported divergence (not mixed in) |
| `evaluated_at` | Timestamp |
| `must_remain_unchanged` | Constraints the generation must not alter (with provenance) |
| `character_constraints` | From currently applicable sources only |
| `relationship_constraints` | Idem |
| `timeline_constraints` | Story-time bounds; epistemology (exact / range / order) |
| `knowledge_constraints` | Who knows what at the requested story-time; in-world vs author-level |
| `location_constraints` | Idem |
| `political_faction_constraints` | Idem |
| `causal_constraints` | Chains that must not be inverted |
| `world_rules` | Currently applicable high-impact laws (resolved live — do not paste a frozen law list into the skill) |
| `permitted_creative_space` | What may be invented (OPEN narrative details, texture, unnamed extras within pools) |
| `warnings` | Non-blocking issues |
| `uncertainties` | Known unknowns, mysteries that must stay mysterious, NOT READY items |
| `forbidden_assumptions` | Negative space; research-as-canon; draft-as-canon; false precision; Earth-transplant if the live charter forbids it |
| `authorized_changes` | Empty unless a completed canon-change protocol listed them |

Every constraint in the contract must be traceable to a source document on the applicable branch. If a constraint cannot be sourced, it does not belong in the contract.

---

## 3. Compactness

The contract is a **filter**, not an encyclopedia. Do not dump the world into it. Include only constraints that the request could violate.

---

## 4. Staleness

A contract is **stale** when any contributing content hash, commit, or applicable branch no longer matches. Stale contracts must not be fed to a generator. The host re-runs the guard.

Tests: [`tests/01-adaptive-suite.md`](tests/01-adaptive-suite.md) scenario 13.

---

## 5. Downstream use

The generator (whatever model) receives:

- the user request
- this contract
- (optionally) the relevant source excerpts, not a skill-owned factbook

The post-generation tell skill may receive `author_intent` derived from the contract's world-rules and style constraints. That is input to a different skill, not a second canon.

---

## 6. What the contract must never say

- "These facts are now the canon."
- "Future chapters may skip the guard."
- "Draft D is admitted."
- Any fact whose source hash was not part of this Canon State.
