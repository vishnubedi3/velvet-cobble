# 04 — Branch awareness (observed, not frozen)

This file records **how to read** the refs this repository has actually used. It is not a promise that the next ref will mean the same thing. Always re-discover. Binding relationship rules: [`../BRANCH_RELATIONSHIP.md`](../BRANCH_RELATIONSHIP.md).

---

## 1. Observed ref kinds

At the time this skill was specialized, live and historical refs included:

| Pattern | What was observed | Default guard treatment |
|---|---|---|
| `main` (default) | Merged project state via PRs. Worldbuilding foundation. Narrative stage **blocked** in its `PROJECT.md` §2. No `samur/narrative/` directory. Tell-reduction skill at repo root `ai-fictional-tells-skill/`. | **Canonical baseline.** Default applicable source when the request is silent. Still re-read its charter every time. |
| `arena/<id>-velvet-cobble` (**Arena Splash**) | Session / development branches. Some merge to `main` via PR. At least one live session branch has **diverged materially**: different charter wording, optional root `AGENTS.md`, `samur/narrative/`, `samur/05-quality/`, `ops/`, skills moved under `skills/`. | **Not automatically canon.** Not an independent canonical timeline. Not irrelevant. Inspect against `main` and **classify content**. Do not auto-merge. Do not ignore. Do not treat all Splash equally. Newer Splash does not override `main`. |
| Merged PR heads | Historical contributions now on `main`. | Not live sources. |
| Closed unmerged PR heads | Abandoned or superseded session work. | Not live sources unless the user names them. |
| `recovery/<operation>` tags | Pre-operation snapshots created before consequential canon or process work. | Historical / rollback / audit only. Never the applicable canon for new generation. Not Splash. |

None of these patterns means "alternate timeline" or "experimental fiction fork" unless the branch's own documents say so. Do not invent that.

---

## 2. What is *not* defined by the project

The project does **not** currently label branches as "canonical timeline A vs B." Session branches are how work is done; `main` is how work is merged. If a future branch *does* declare an alternate timeline, believe **that branch's documents**, and do not merge them with `main`'s canon.

Do **not** implement "Arena Splash is non-canon." Splash may clarify, expand, indicate intended direction, or hold proposed / exploratory material.

---

## 3. Splash vs main (mandatory)

When a live `arena/*` head exists:

1. Inspect **current** `main`. Established CANON on `main` is the baseline.
2. Inspect the relevant Splash material.
3. Classify each relevant Splash statement ([`../BRANCH_RELATIONSHIP.md`](../BRANCH_RELATIONSHIP.md) §5).
4. Put only appropriately classified information into the Generation Contract, **labeled by source status**.
5. Re-classify when either side moves. Do not freeze a snapshot class.

A second live head is **not** by itself `REQUIRES_CLARIFICATION`. Uninspected Splash **is** insufficient information (`CX-AMBIGUITY`). Contradictory Splash is a **classified conflict**, not a silent override and not a dismissal.

A fact that exists only on Splash is **not** established `main` canon. It may still be relevant (clarification, extension, intent, proposed, developmental, exploratory, contradictory, or unresolved).

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
