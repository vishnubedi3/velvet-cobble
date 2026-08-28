# 04 — Branch awareness (observed, not frozen)

This file records **how to read** the refs this repository has actually used. It is not a promise that the next ref will mean the same thing. Always re-discover.

---

## 1. Observed ref kinds

At the time this skill was specialized, live and historical refs included:

| Pattern | What was observed | Default guard treatment |
|---|---|---|
| `main` (default) | Merged project state via PRs. Worldbuilding foundation. Narrative stage **blocked** in its `PROJECT.md` §2. No `samur/narrative/` directory. Tell-reduction skill at repo root `ai-fictional-tells-skill/`. | Default applicable source **when the request is silent and no live divergence is detected**. Still re-read its charter every time. |
| `arena/<id>-velvet-cobble` | Session / development branches. Some merge to `main` via PR. At least one live session branch has **diverged materially**: different charter wording, optional root `AGENTS.md`, `samur/narrative/`, `samur/05-quality/`, `ops/`, skills moved under `skills/`. | **Not automatically canonical** because it exists. Applicable when the request targets that session. If it diverges from `main` and the request is silent → `REQUIRES_CLARIFICATION`. |
| Merged PR heads | Historical contributions now on `main`. | Not live sources. |
| Closed unmerged PR heads | Abandoned or superseded session work. | Not live sources unless the user names them. |
| `recovery/<operation>` tags | Pre-operation snapshots created before consequential canon or process work. | Historical / rollback / audit only. Never the applicable canon for new generation. |

None of these patterns means "alternate timeline" or "experimental fiction fork" unless the branch's own documents say so. Do not invent that.

---

## 2. What is *not* defined by the project

The project does **not** currently label branches as "canonical timeline A vs B." Session branches are how work is done; `main` is how work is merged. If a future branch *does* declare an alternate timeline, believe **that branch's documents**, and do not merge them with `main`'s canon.

---

## 3. Divergence handling (mandatory)

When two live heads differ in any of:

- `PROJECT.md` §2 (generation authorization)
- presence of `samur/narrative/` or `samur/05-quality/`
- content hashes of `samur/02-canon/`
- skill layout (`ai-fictional-tells-skill/` at root vs under `skills/`)

the guard:

1. Reports the divergence (paths + nature).
2. Refuses to union facts.
3. Evaluates a named branch if the request named one.
4. Otherwise `REQUIRES_CLARIFICATION`.

A fact that exists only on an unmerged session branch is **not** applicable to a `main`-targeted request.

---

## 4. Layout may move; resolution follows the tree

Do not hard-code "the tell skill is at repo root." Resolve:

- `ai-fictional-tells-skill/SKILL.md` if present on the applicable tree
- else `skills/ai-fictional-tells-skill/SKILL.md` if present
- else "tell skill not on this ref" (does not block *this* skill)

Same for optional `AGENTS.md` at repo root: present or not is a property of the ref.

---

## 5. Session branch of the charter line

`PROJECT.md` may contain a `Session branch:` line. That line is **meta** (which session wrote the charter), not world canon, and not automatically the applicable branch for a later request. Observed audits already treat it as non-contradiction. The guard treats it as a hint, not as authority over Git.
