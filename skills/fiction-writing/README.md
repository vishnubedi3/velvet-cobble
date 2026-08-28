# Pre-Generation Canon Guard

**This folder is the complete, distributable skill** for this repository's pre-generation canon verification layer.

It is **standalone and model-agnostic**: documentation, JSON Schemas, prompt contracts, a deterministic reference core, fixtures, and tests. It has no runtime vendor dependencies. It does **not** contain a copy of the world's facts.

The skill continuously determines the current relevant canon from the **current state of the project's branches** and uses that state to verify every new generation request **before generation begins**.

- **Primary specification:** [`SKILL.md`](SKILL.md) — start there.
- **Agent hosting notes:** [`AGENTS.md`](AGENTS.md)
- **Version:** 1.0.0 · **Status:** active · **Format:** documentation + JSON Schemas + reference core (Python, optional).

---

## 1. What's in this folder

| Area | Location | Contents |
|---|---|---|
| **Core skill definition** | [`SKILL.md`](SKILL.md), [`ARCHITECTURE.md`](ARCHITECTURE.md) | Binding contract and runtime architecture |
| **Canon mechanics** | [`CANON_MODEL.md`](CANON_MODEL.md), [`CANON_RESOLUTION.md`](CANON_RESOLUTION.md) | Living Canon State; how to resolve it from branches |
| **Verification** | [`CONFLICT_TAXONOMY.md`](CONFLICT_TAXONOMY.md), [`DECISION_PROTOCOL.md`](DECISION_PROTOCOL.md), [`GENERATION_CONTRACT.md`](GENERATION_CONTRACT.md) | Findings, decisions, contracts |
| **Evolution** | [`CANON_CHANGE_PROTOCOL.md`](CANON_CHANGE_PROTOCOL.md), [`CANON_ADMISSION_PROTOCOL.md`](CANON_ADMISSION_PROTOCOL.md), [`spec/03-invalidation.md`](spec/03-invalidation.md) | Intentional change; admission; stale-state handling |
| **Project specialization** | [`spec/04-branch-awareness.md`](spec/04-branch-awareness.md), [`spec/05-project-specialization.md`](spec/05-project-specialization.md) | Observed branch roles and source layout — *how to read*, not a fact dump |
| **Interfaces** | [`spec/01-interfaces.md`](spec/01-interfaces.md), [`spec/02-pipeline.md`](spec/02-pipeline.md), [`schemas/`](schemas/) | Portable operations and JSON contracts |
| **Reference core** | [`reference/canon_guard.py`](reference/canon_guard.py) | Deterministic engine over structured Canon States (for tests) |
| **Tests & fixtures** | [`tests/`](tests/), [`fixtures/`](fixtures/) | Adaptive property suite; synthetic worlds only |
| **Preserved draft rules** | [`anti-patterns.md`](anti-patterns.md), [`STATUS.md`](STATUS.md) | Prose anti-patterns (not canon); status of this directory |

---

## 2. Quick start

1. Read [`SKILL.md`](SKILL.md).
2. Before generating anything, run the 15-step gate in [`spec/02-pipeline.md`](spec/02-pipeline.md).
3. Resolve sources from the applicable **current** branch heads — never from this folder's text.
4. Emit a decision. If permitted, emit a Generation Contract bound to the evaluated commits/hashes.
5. After generation, do **not** treat the output as canon. Follow [`CANON_ADMISSION_PROTOCOL.md`](CANON_ADMISSION_PROTOCOL.md).
6. After any source change, invalidate derived state ([`spec/03-invalidation.md`](spec/03-invalidation.md)) and re-resolve next time.

Run the adaptive tests (synthetic fixtures, no project lore):

```
python3 skills/fiction-writing/tests/run_adaptive_tests.py
```

---

## 3. What this skill refuses to do

- Copy `samur/02-canon/` (or any branch's fictional contents) into this package.
- Snapshot today's facts as permanently correct.
- Treat `main` and live `arena/*` session branches as the same canon if they have diverged.
- Treat `recovery/*` tags as live sources.
- Treat `WORLD-MODEL.md` as winning a disagreement with a canon file.
- Treat research, hypotheses, open questions, pilots, or quality reports as CANON.
- Resolve a deliberate mystery because a generation request finds it convenient.

---

## 4. Portability

- All in-package links are file-relative.
- The only external resource the skill needs at run time is **the project's current branches**.
- Hosts may implement the pipeline with any LLM, or with none (structured claims + the reference core).
- Terminology is in [`glossary.md`](glossary.md). Configuration knobs are in [`CONFIG.md`](CONFIG.md). Inventory is in [`MANIFEST.md`](MANIFEST.md).
