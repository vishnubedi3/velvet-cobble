# AGENTS.md — Hosting the Pre-Generation Canon Guard

This file tells an agent how to **host** this skill. It is not the repository's world charter. It is not a copy of any branch's operational novel-authoring protocol. Those live in the project (`PROJECT.md`, and `AGENTS.md` at repo root **if that file exists on the applicable branch** — it may not).

---

## 1. When to invoke

Invoke this skill **before every generation operation**, including:

- narrative prose (chapters, scenes, pilots), if the applicable branch permits it
- worldbuilding that would add, revise, or retire CANON
- filling an OPEN narrative-detail question
- any request that implies a fact about the world

Do not invoke the post-generation tell-reduction skill as a substitute. Do not skip the guard because a previous request passed.

If the applicable branch's charter currently forbids the requested kind of generation, the guard's decision is **BLOCK**. Extra `arena/*` heads are **not** a reason to skip the guard or to treat Splash as established canon. Inspect Splash, classify it against `main`, and label source status. That is a correct result, not a reason to bypass the skill.

---

## 2. Pre-action obligations

1. Discover live Git refs (local and remote heads, recovery tags). Do not assume the ref list you saw last session is complete.
2. Read the **applicable branch's** `PROJECT.md` (charter), `samur/README.md` (material map), and — only if present on that branch — root `AGENTS.md`.
3. Do not use this skill folder as a fact cache.
4. Do not generate first and verify afterwards.

---

## 3. How to run (any model)

Minimum:

1. Build a `GenerationRequest` ([`schemas/generation-request.schema.json`](schemas/generation-request.schema.json)).
2. `resolve_branches` → `resolve_canon` → `verify` → `decide` → `contract`.
3. Persist the `VerificationReport` where the host stores quality/audit records. On this project, **if** the applicable branch has `samur/05-quality/`, put canon-guard reports there. If it does not, do **not** invent that directory as a side effect of a verification; store the report with the host's audit log and record the path in the report. Never write reports into `samur/02-canon/` or into narrative prose files.
4. If the decision is not PASS / PASS_WITH_WARNINGS, **do not generate**.

LLM-hosted extraction (optional) uses prompt contracts C-CG-01…C-CG-04 in [`spec/01-interfaces.md`](spec/01-interfaces.md). Deterministic validators still own the verdict.

---

## 4. What an agent must never do while hosting this skill

- Commit generated lore into `samur/02-canon/` as part of "running the guard."
- Update `WORLD-MODEL.md` because a request passed.
- Close a QUESTION because a draft answered it.
- Copy facts from canon files into `SKILL.md` or into a "current facts" cheat sheet inside this package.
- Evaluate against a recovery tag unless the request is an explicit historical audit.
- Merge two diverged session branches to get a "complete" canon.

---

## 5. After generation

Generated output is **proposed**. Admission is [`CANON_ADMISSION_PROTOCOL.md`](CANON_ADMISSION_PROTOCOL.md). If the project later accepts material into a canonical source, the next guard run must re-resolve that source. The previous contract is then potentially stale.

---

## 6. Complement, don't duplicate

- Prose anti-patterns: [`anti-patterns.md`](anti-patterns.md) — craft rules, not world facts.
- Tell reduction: the post-generation skill on the applicable branch.
- Worldbuilding protocol: the applicable branch's `PROJECT.md` §4 (transformation logs, changelog, dependency sweeps). This skill checks that a worldbuilding request **respects** that protocol; it does not replace it.
