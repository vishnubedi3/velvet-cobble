# 13 — Architectural audit

Audit of the working-branch Canon Guard **before** the ecosystem expansion, and what this package changed. The concept is unchanged: `main` is the established baseline; Arena is classified working state; generated text is proposed until admitted.

No Fishnet skill exists in this repository. Transfer was from [`ai-fictional-tells-skill/`](../../../ai-fictional-tells-skill/SKILL.md) *design* properties only (defense in depth, evidence, preservation, failure modes, generator independence). Tell taxonomy was not copied.

---

## Weaknesses found (pre-expansion)

| ID | Weakness | Risk | Fix |
|---|---|---|---|
| W1 | No `post_verify`. Pipeline treated generation as outside the skill with no second canon check. | False accept: output contradicts after a pre-gen PASS | `post_verify`; lifecycle I-9; A31 |
| W2 | Contract not locked; generator could theoretically rewrite constraints | Bypass | `locked` + `lock_hash`; `contract_was_mutated`; A29 / mutated-contract test |
| W3 | No hard vs soft vs direction vs provisional vs forbidden bands | Generator treats working material as extra established facts | `constraint_bands`; [`layers/constraint-bands.md`](../layers/constraint-bands.md) |
| W4 | Contamination only as `CX-ADMISSION` (`uses_unadmitted_as_canon`) | Draft/contract presented as established | `CX-CONTAMINATION`; A28, A36, A37 |
| W5 | No continuity ledger | Chapter-to-chapter state inversion missed if not already on `main` | Explicit ledger + `CX-CONTINUITY`; A30. Not auto-built from `main` (that is `CX-DIRECT`) |
| W6 | `CX-STALE` documented, never emitted | Stale post-gen could be honored | `post_verify` emits `CX-STALE`; A32 |
| W7 | `CX-TEMPORAL` documented, never emitted | Future-as-present claims PASSed | Narrow check: same value before `story_time_start` |
| W8 | `CX-RETIRED` documented; citations used `CX-AUTHORITY` | Retired treated as a guess rather than a block | `cited_status: RETIRED` → `CX-RETIRED` BLOCK |
| W9 | `working_canon_context` required on the contract, omitted by `make_contract` | Downstream merge risk | Emitted on every contract |
| W10 | Request/report schemas `additionalProperties: false` omitted engine fields | Hosts dropping valid flags | Schemas extended |
| W11 | `permitted_creative_space` schema said objects; engine emits strings | Schema lie | `string \| object` |
| W12 | SKILL/pipeline described a pre-generation-only skill | Hosts skip post-gen | Binding rules 13–14; pipeline stages 7–8 |
| W13 | Glossary still said CANONICAL / AUTHORIAL_INTENT | Drift vs ESTABLISHED_CANON bands | Glossary updated |
| W14 | Findings lacked severity *bands* | Harmless expansion vs serious contradiction looked alike | `band` on every finding; [`SEVERITY.md`](../SEVERITY.md) |

---

## Weaknesses accepted (not overbuilt)

| ID | Item | Why left |
|---|---|---|
| A1 | Full story-time graph / era algebra | Project dating epistemologies are re-read live; fixtures cover ordinal windows |
| A2 | Persistent chapter ledger in git | Host-owned cache; skill must not write `02-canon/` |
| A3 | Protocol §2 lists CX-AMBIGUITY before CX-BRANCH; engine BLOCK classes win if both fire | Matches A18 (charter BLOCK). Uninspected-splash-only still clarifies |
| A4 | Optional LLM extraction unhosted | Deterministic core is the verdict; C-CG-01…04 remain prompt contracts |
| A5 | Continuity vs `main` facts not auto-duplicated as `CX-CONTINUITY` | Would noisily clone every `CX-DIRECT` |

---

## Invariants re-checked after the fix

- A01–A27 still green (working-branch model not replaced).
- A08 T0 / A33 expansion still PASS (false-reject pressure).
- Arena following (A22, A35) is not a BLOCK.
- Differing from Arena is not a BLOCK (A23 remains PASS_WITH_WARNINGS).
- Newer Arena does not enter ESTABLISHED_CANON.
- `samur/02-canon/` untouched by this package.
- `post_verify` never emits a contract and never sets `admitted: true`.
