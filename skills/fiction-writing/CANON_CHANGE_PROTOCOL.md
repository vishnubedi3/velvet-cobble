# CANON_CHANGE_PROTOCOL.md

If the user deliberately wants an outcome that contradicts currently applicable canon, **do not silently overwrite**.

This protocol is the guard's interface to the project's own change machinery. It does not replace `PROJECT.md` §4, `samur/CHANGELOG.md`, or dependency sweeps. It requires them.

---

## 1. Entry

A verification ends in `CANON_CHANGE_REQUIRED` when:

- the request sets `explicit_canon_change: true`, or
- the user states that established canon should change, or
- the only way to honor the request is to alter a CANON fact

A BLOCK that the user then re-issues as an explicit change becomes this protocol. A BLOCK that the user does not re-issue stays a BLOCK.

---

## 2. Identify

Before any write:

1. **Affected current canon** — documents and sections (live paths, not memory).
2. **Downstream dependents** — walk current `Dependents` / reverse `Depends on`. If any affected file is `High-impact: yes`, treat the change as **systemic** until proven local.
3. **Branch state being changed** — which ref will receive the edit. Do not edit a different branch than the one evaluated.
4. **Affected chapters or drafts** — if `samur/narrative/` exists on that branch, list drafts whose contracts cited the old hashes. Those contracts become stale.
5. **Scope** — `local` (single fact, no high-impact, dependents empty or purely documentary), `temporal` (a dated event / reign / era bound), or `systemic` (world-law, geography, succession, currency, core religion, calendar, or a high-impact header).
6. **Open contradictions** — whether this change would resolve or worsen an active `CONTRADICTIONS.md` item.

---

## 3. Require the project's mechanism

On this project, an authorized canon change must (per the live charter / `samur/README.md`):

- keep Status, provenance, dependency links
- add a `CHANGELOG.md` entry (affected + dependents)
- run a dependency sweep in the same change if high-impact
- use a transformation log when the change is a major institution/event (5-step method in `samur/01-research/comparative/README.md`)
- retire rather than delete invalidated canon
- not resolve deliberate mysteries unless the change *is* an explicit mystery-resolution authorized as such
- create a recovery point **before** the write if the project's current operating protocol requires it (observed on this repo as `recovery/<operation>` tags)

If a future branch specifies a different mechanism, follow **that branch's** documents. If no mechanism exists on a branch, **do not invent canon anyway**. Emit a structured `CanonChangeProposal` ([`schemas/canon-change-proposal.schema.json`](schemas/canon-change-proposal.schema.json)) and wait.

---

## 4. Proposal shape

```
CanonChangeProposal
  target_branch
  evaluated_canon_state_id
  requested_outcome
  affected_sources[]
  dependents[]
  scope: local | temporal | systemic
  mystery_impact: none | extends-structure | would-resolve (forbidden unless explicit)
  required_project_steps[]
  recovery_point_required: bool
  invalidation_plan
```

The proposal is not itself a change.

---

## 5. After an authorized change lands

1. Detect the source change (hashes).
2. Invalidate affected derived state ([`spec/03-invalidation.md`](spec/03-invalidation.md)).
3. Re-resolve.
4. Future generation requests use the new Canon State.
5. Historical PASS records remain historical.

Do not mutate old Generation Contracts. Mark them stale.
