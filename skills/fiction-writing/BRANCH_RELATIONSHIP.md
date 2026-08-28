# BRANCH_RELATIONSHIP.md

How `main` and Arena relate. Re-evaluate on every request. Do not freeze a piece of Arena content as one class forever.

---

## 1. The model (binding)

```
MAIN                         = Canonical baseline
                               Established canon

ARENA / ARENA SPLASH         = Current working / authoring state
                               Not automatically established canon
                               The most important live source for
                               current creative direction

MAIN + RELEVANT ARENA
DEVELOPMENT                  = Canon interpretation for this request
                               = Current Working Canon Context
```

**Wrong:** `main` = canon, Arena = non-canon.
**Wrong:** Arena is established canon because it is the current working branch, or because it is newer.
**Right:** `main` is the default established canon. Arena is the author's live workspace. Arena content is **canon-relevant development** whose status is resolved at the content level.

Do not select one branch and ignore the other.
Do not mechanically merge them.
Do not treat branch names as sufficient evidence of canon status.

Two questions, always:

1. Is this request consistent with **established canon** (`main`)?
2. Is this request consistent with the author's **current working direction** (Arena)?

A PASS is not earned merely by not contradicting `main`. Ignoring strong current Arena development is a finding. Differing from Arena is not automatically a BLOCK — Arena is a working branch; creative development remains possible.

---

## 2. What "Arena" is in this repository

The project has no git ref literally named `Arena` or `Arena Splash`. Observed current working heads are **`arena/*` session branches** (and any future unmerged session head playing that role).

| Ref | Role | Default treatment |
|---|---|---|
| `main` (default / `origin/HEAD`) | Merged project state | **Established canonical baseline.** Historical events, character facts, relationships, world rules, timeline, consequences, terminology — unless a live project rule says otherwise. |
| `arena/*` (Arena) | **Current working branch** | Consult **aggressively** for current direction, developing storyline, clarifications, and intended future canon. Classify every relevant statement against `main`. Not automatic canon. |
| `recovery/*` | Pre-operation snapshots | Historical / rollback only. Not Arena, not live canon. |
| Merged PR heads | Already on `main` | Not a separate source. |

A newer Arena commit does **not** override `main` merely by being newer. Repository time ≠ canon replacement.

If a future branch's own documents declare a different role (e.g. an explicit alternate timeline), believe **those documents**.

Both branches evolve. When `main` changes, re-evaluate Arena against the new baseline. When Arena changes, previous direction does not automatically control.

---

## 3. What Arena material *may* be

Arena is where the author is actively writing. It may contain new chapters, scenes, characters, events, explanations, clarifications, storyline developments, future events, revised interpretations, proposed canon, experimental material, temporary drafts, abandoned ideas, and other working material.

The guard's questions are:

> What is established canon?
> What is the author currently developing?
> What does this Arena material mean relative to `main`?

Those are different questions. Keep them different.

---

## 4. Resolution order (every request)

1. Inspect the **current** state of `main` (established canon).
2. Inspect **current** relevant Arena material (working state). Consult it; do not skip it because the request did not name `arena/*`.
3. Classify each relevant Arena statement against `main` ([§5](#5-content-level-classification)).
4. Build a **Current Working Canon Context** ([§7](#7-current-working-canon-context)): established canon + classified Arena + conflicts + apparent current direction.
5. Answer **both** decision questions ([§8](#8-the-two-questions)).
6. Put **labeled** information into the Generation Contract. Never mix unlabeled Arena drafts into established canon.

Details: [`CANON_RESOLUTION.md`](CANON_RESOLUTION.md).

---

## 5. Content-level classification

Classify each relevant Arena statement against current `main`. Re-classify when either side changes. Do not force a class when the evidence is weaker than the label.

| Class | Meaning | Established fact? | Working direction? |
|---|---|---|---|
| **CONFIRMS_CANON** | Repeats or reinforces `main` | Yes — sourced to `main` | Corroboration |
| **CLARIFIES_CANON** | Explains or makes explicit something on `main` without replacing it | Yes, as labeled clarification | Improves understanding of `main` |
| **EXTENDS_CANON** | Compatible new information along an established line; not yet on `main` | No | Yes — current development |
| **DEVELOPS_INTENDED_CANON** | Appears to be the author's current intended direction; not yet established | No | **Yes — strong direction** |
| **PROPOSED_CANON** | Offered as a candidate addition or change | No | Provisional |
| **DEVELOPMENTAL** | Working material; status not established | No | Provisional |
| **EXPLORATORY** | Explores possibilities rather than a definitive direction | No | Not the timeline |
| **CONTRADICTS_CANON** | Conflicts with established `main` at overlapping story-time | No | **Conflict.** Do not silently incorporate |
| **RETCON_PROPOSAL** | Appears to intentionally revise established canon; not yet integrated | No | **Conflict / change.** `CANON_CHANGE_REQUIRED` only if the user wants the change |
| **ABANDONED_OR_SUPERSEDED** | Repository evidence that this is no longer current direction | No | Must not control generation |
| **UNRESOLVED** | Relationship to `main` cannot be determined reliably | No | Open question |

Signals (use when present; do not invent certainty):

- File location and `Status:` on **that** tree (`02-canon/` vs `narrative/` vs `03-hypotheses/` vs `05-quality/`)
- Changelog / admission records that point at the same claim on `main`
- Explicit authorial notes, question status, contradiction-register entries
- Consistency with `main` (compatible clarification vs incompatible replacement)
- High-impact headers (an extension that would smuggle a world-law is not a quiet clarification)
- Later Arena commits superseding earlier ones on the same working head

Where intent is unclear → `UNRESOLVED`, not a guessed `CONFIRMS_CANON`.

---

## 6. Conflict outcomes (do not silently resolve)

| Reading | Guard |
|---|---|
| Arena confirms `main` | `CONFIRMS_CANON` |
| Arena clarifies `main` | `CLARIFIES_CANON` — use it to understand `main` |
| Arena extends `main` | `EXTENDS_CANON` — working development, not yet historical on `main` |
| Arena is current intended direction | `DEVELOPS_INTENDED_CANON` — inform generation; do not present as established |
| Arena proposes an addition | `PROPOSED_CANON` |
| Arena proposes a retcon | `RETCON_PROPOSAL` — flag; `main` remains baseline until integration |
| Arena contradicts `main` | `CONTRADICTS_CANON` — classify; do not pick Arena because it is newer |
| Arena is abandoned / superseded | `ABANDONED_OR_SUPERSEDED` — do not let it control |
| Competing Arena directions | `UNRESOLVED` / `REQUIRES_CLARIFICATION` |
| `main` remains authoritative for established facts | Default whenever Arena would *replace* an established fact without integration |

Only an **explicit or sufficiently supported canon integration** (admission onto `main` via the project's changelog / transformation / dependency-sweep process) causes Arena development to replace established `main` canon.

---

## 7. Current Working Canon Context

This is **not** established canon. It is the interpretation object for one request:

- **A.** Established canon from `main`
- **B.** Relevant Arena developments (classified)
- **C.** Status of each Arena development
- **D.** Unresolved conflicts between the two
- **E.** Apparent current authorial direction, where sufficiently supported

The generator must see both "what is canon?" and "what is the author currently developing?"

---

## 8. The two questions

| | Question | Typical outcomes |
|---|---|---|
| Q1 | Consistent with established canon (`main`)? | Violation → `BLOCK` or `CANON_CHANGE_REQUIRED` |
| Q2 | Consistent with current working direction (Arena)? | Strong ignore / diverge from intended or provisional → `PASS_WITH_WARNINGS`; competing directions → `REQUIRES_CLARIFICATION` |

Combined:

| Q1 | Q2 | Decision |
|---|---|---|
| Violates `main` | (any) | `BLOCK` (or `CANON_CHANGE_REQUIRED` if explicit) |
| Safe vs `main` | Follows current direction (or none relevant) | `PASS` |
| Safe vs `main` | Diverges from / ignores strong or provisional Arena development | `PASS_WITH_WARNINGS` |
| Safe vs `main` | Arena direction genuinely ambiguous | `REQUIRES_CLARIFICATION` |
| Insufficient information (uninspected Arena, unresolved overlap) | | `REQUIRES_CLARIFICATION` |

Do **not** automatically BLOCK a request merely because it differs from Arena.
Do **not** PASS a request merely because it does not contradict `main`.

---

## 9. Generation Contract bands

| Band | Content |
|---|---|
| **ESTABLISHED_CANON** | From `main` |
| **CURRENT_WORKING_DEVELOPMENT** | Arena extensions and live storyline, labeled |
| **CANON_CLARIFICATIONS** | Arena explanations of `main` |
| **AUTHORIAL_DIRECTION** | Strongly supported current development that should influence generation |
| **PROVISIONAL** | Working / proposed / exploratory — not established; use only if the request permits working material |
| **CONFLICTS** | `main` vs Arena differences requiring attention |
| **OPEN_QUESTIONS** | Intent cannot be determined reliably |

Downstream:

- **ESTABLISHED CANON** — use as factual project canon.
- **CURRENT AUTHORIAL DEVELOPMENT** — use as current story direction where appropriate.
- **PROVISIONAL** — use only if the request explicitly permits working material.
- **CONFLICT** — do not silently incorporate.

This prevents ignoring Arena (generating from old `main` while the author has moved) and prevents canonizing unfinished Arena drafts.

---

## 10. Adaptation

Arena is continuously written. `main` may also evolve through deliberate canon updates.

- New Arena developments become available on the next resolve.
- Superseded Arena developments must not automatically control.
- New contradictions, character states, timeline facts, relationships, and storyline direction must be recognized.
- When `main` changes: invalidate stale derived state; re-classify Arena against the new baseline.

Previous classifications are evidence, not identity. Hash change on either side → re-resolve. Do not permanently extract Arena into a frozen representation.

---

## 11. Final principle

`main` is the canonical foundation.
Arena is the living workspace where the author currently develops the project.
Arena content is evidence of current authorial development, not automatic canon.
Canon resolution determines which Arena developments are authoritative, clarifying, intended, provisional, exploratory, contradictory, retcon, abandoned, or unresolved.
Generation uses established canon from `main` while incorporating relevant, **appropriately classified** current Arena development.

Protect established canon. Stay synchronized with the author's current working storyline. Do not freeze the project.
