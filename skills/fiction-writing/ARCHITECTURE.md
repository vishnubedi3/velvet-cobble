# ARCHITECTURE.md

The Canon Guard is a **living verification layer**, not a database of the world.

---

## 1. Layers

```
┌─────────────────────────────────────────────────────────────┐
│  Host (any agent / any model / any language)                │
│  Provides: git (or equivalent branch access), optional llm()│
│            store.put/get for reports                         │
└──────────────────────────┬──────────────────────────────────┘
                           │
┌──────────────────────────▼──────────────────────────────────┐
│  Resolution layer                                           │
│  Discover refs → main = established canon                   │
│  → Arena = current working state (consult aggressively)     │
│  → classify Arena vs main → Current Working Canon Context   │
│  Specified in BRANCH_RELATIONSHIP.md + CANON_RESOLUTION.md  │
└──────────────────────────┬──────────────────────────────────┘
                           │
┌──────────────────────────▼──────────────────────────────────┐
│  Canon State (ephemeral, versioned)                         │
│  Applicable commits + content hashes + extracted constraints│
│  Derived index is a CACHE. Invalidated on source change.    │
│  Specified in CANON_MODEL.md                                │
└──────────────────────────┬──────────────────────────────────┘
                           │
┌──────────────────────────▼──────────────────────────────────┐
│  Verification layer                                         │
│  Direct / indirect / temporal / knowledge / causal /        │
│  branch / ambiguity / unresolved-conflict checks            │
│  Specified in CONFLICT_TAXONOMY.md + spec/02-pipeline.md    │
└──────────────────────────┬──────────────────────────────────┘
                           │
┌──────────────────────────▼──────────────────────────────────┐
│  Decision + Contract                                        │
│  PASS / PASS_WITH_WARNINGS / REQUIRES_CLARIFICATION /       │
│  BLOCK / CANON_CHANGE_REQUIRED                              │
│  Contract is bound to the evaluated Canon State             │
└─────────────────────────────────────────────────────────────┘
```

Generation, review, and admission sit **outside** this diagram. The guard neither generates nor admits.

---

## 2. What is stateful vs. what is not

| Thing | State? | Authority? |
|---|---|---|
| Branch contents at a commit | Live source | **Yes** |
| Canon State object from a run | Derived snapshot of that commit | No — audit record only |
| Derived constraint index | Cache | No |
| Generation Contract | Bound to a Canon State | No — stale when sources change |
| This skill's documents | Rules of derivation | No — not world facts |
| `WORLD-MODEL.md` on a branch | Derived summary **on that branch** | No — loses to `02-canon/` files |

There is no durable fact table inside the skill. If a host keeps an index for speed, it **must** key it by `(branch, commit, path, content_hash)` and drop entries whose hashes no longer match.

---

## 3. Two clocks

This project has **repository time** (commits, changelogs, recovery tags) and **story time** (the world's own chronology, which itself has more than one epistemology — exact era dates vs. deep orders). Architecture must keep them separate:

- Change detection and invalidation use repository time.
- Temporal consistency of a request uses story time.
- A source added at repo-time T can constrain story-time S only according to what the source *claims about S*, not according to when it was written.

---

## 4. Deterministic core vs. model-hosted extraction

**Deterministic (required):** branch inventory, header parsing, status taxonomy, hash comparison, dependency-graph walk, invalidation scope, decision table, contract staleness, admission status.

**Model-hosted (optional):** turning free-text requests and markdown bodies into structured claims; indirect-consistency reading; knowledge-boundary reading. Outputs are *candidates*. Verdicts require the deterministic checks.

The reference core ([`reference/canon_guard.py`](reference/canon_guard.py)) implements the deterministic path over already-structured Canon States. Fixtures supply structured facts so tests do not need an LLM and do not use project lore.

---

## 5. Change and invalidation

```
source hash changes
        ↓
classify change: local | temporal | systemic (high-impact)
        ↓
invalidate affected derived facts and contracts
        ↓
next request re-resolves from sources (not from the old index)
```

Details: [`spec/03-invalidation.md`](spec/03-invalidation.md). High-impact classification is read from the **current** file header (`High-impact:`), not from a list in this skill.

---

## 6. Failure isolation

- If branch discovery fails → do not verify; report host error.
- If live Splash exists but was not inspected → `REQUIRES_CLARIFICATION`.
- If applicable non-splash branch cannot be chosen → `REQUIRES_CLARIFICATION`.
- If a relevant source is unreadable → `REQUIRES_CLARIFICATION`, not a pass on remaining files.
- If the derived index is stale → ignore it; re-resolve.
- If an LLM extraction is malformed → discard it; do not generate from it.

---

## 7. What we deliberately did not build

No database, no vendor SDK, no frozen "current kings" table, no duplicate canon tree, no automatic merge of Arena Splash into `main`, no blanket "Splash is non-canon," no write-back into `02-canon/`. Those would either freeze the world or contaminate it.
