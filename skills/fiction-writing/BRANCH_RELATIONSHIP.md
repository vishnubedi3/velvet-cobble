# BRANCH_RELATIONSHIP.md

How `main` and Arena Splash relate. Re-evaluate on every request. Do not freeze a piece of Splash content as one class forever.

---

## 1. The rule (binding)

```
MAIN            = Default canonical baseline
ARENA SPLASH    = Not automatically canon
                  Not an independent canonical timeline by default
                  Not irrelevant
                  = Canon-relevant authorial development
```

**Wrong:** "Arena Splash is non-canon."
**Wrong:** "Arena Splash is canon because it exists / is newer."
**Right:** "Arena Splash is not automatically canon, but its contents are potentially canon-relevant and may establish, clarify, or expand canon when supported by authorial intent and the project's integration process."

Branch membership alone never determines canon status. Content plus relationship to `main` does.

Do not automatically merge Splash into `main`.
Do not automatically ignore Splash.
Do not treat all Splash content equally.

---

## 2. What "Arena Splash" is in this repository

The project has no git ref literally named `Arena Splash`. Observed authoring/development heads are **`arena/*` session branches** (and any future unmerged session head the host can show is playing that role).

| Ref | Role | Default treatment |
|---|---|---|
| `main` (default branch / `origin/HEAD`) | Merged project state | **Canonical baseline.** Established CANON on `main` is established canon unless a more specific live project rule says otherwise. |
| `arena/*` (Arena Splash) | Authoring and development | **Non-canonical-by-default.** Inspect for relationship to `main`. Classify content. |
| `recovery/*` | Pre-operation snapshots | Historical / rollback only. Not Splash, not live canon. |
| Merged PR heads | Already on `main` | Not a separate source. |

A newer Splash commit does **not** override `main` merely by being newer. Repository time ≠ canon replacement.

If a future branch's own documents declare a different role (e.g. an explicit alternate timeline), believe **those documents**. Do not invent that role for ordinary `arena/*` heads.

---

## 3. What Splash material *may* be

Splash content may:

- clarify existing canon
- expand existing canon
- establish intended canon direction
- provide a stronger explanation of something already on `main`
- contain future canon
- contain proposed canon
- contain exploratory or provisional material
- contradict `main`
- remain unresolved

The guard's question is not only "is this canon?" It is:

> What does this material establish, clarify, develop, or propose about the author's canon?

---

## 4. Resolution order (every request)

1. Inspect the **current** state of `main`.
2. Identify relevant **established** canon on `main`.
3. Inspect relevant Arena Splash material where it provides additional context, clarification, development, or intended storyline.
4. **Classify** that Splash material ([§5](#5-content-level-classification)).
5. Distinguish established canon from proposed / developmental material.
6. Put **only appropriately classified** information into the Generation Contract, **labeled by source status**.

Details: [`CANON_RESOLUTION.md`](CANON_RESOLUTION.md).

---

## 5. Content-level classification

Classify each relevant Splash statement against current `main`. Re-classify when either side changes.

| Class | Meaning | In the contract as established fact? |
|---|---|---|
| **CONFIRMED_CANON** | Same claim already established on `main` (Splash restates it) | Yes — sourced to `main`; Splash is corroboration |
| **CANON_CLARIFICATION** | Explains, disambiguates, or strengthens something on `main` without replacing it | Yes, as clarification of `main`, labeled |
| **CANON_EXTENSION** | Compatible new development along an established line; not yet on `main` | No. Labeled extension. Do not present as already-historical on `main` |
| **AUTHORIAL_INTENT** | Strong indication of intended direction / future storyline; not established | No. Labeled intent |
| **PROPOSED_CANON** | Offered as a candidate fact; awaiting integration | No. Labeled proposed |
| **DEVELOPMENTAL** | Authoring work (draft, pilot, quality notes, scaffolding) | No. Storyline context only if the request continues Splash |
| **EXPLORATORY** | Alternative / experiment; not the intended replacement | No. Must not be treated as the timeline |
| **CONTRADICTORY** | Incompatible with established `main` at overlapping story-time | No. **Conflict.** Do not silently pick Splash over `main` |
| **UNRESOLVED** | Relationship to `main` cannot be determined reliably | No. Preserve uncertainty |

Signals (use when present; do not invent certainty):

- File location and `Status:` on **that** tree (`02-canon/` vs `narrative/` vs `03-hypotheses/` vs `05-quality/`)
- Changelog / admission records that point at the same claim on `main`
- Explicit authorial notes, question status, contradiction-register entries
- Consistency with `main` (compatible clarification vs incompatible replacement)
- High-impact headers (an extension that would smuggle a world-law is not a quiet clarification)

Where intent is unclear → `UNRESOLVED`, not a guessed `CONFIRMED_CANON`.

---

## 6. Conflict outcomes (do not silently resolve)

When Splash disagrees with `main`:

| Reading | Guard |
|---|---|
| Splash clarifies `main` (compatible) | `CANON_CLARIFICATION` — use it to improve understanding |
| Splash proposes an extension | `CANON_EXTENSION` / `PROPOSED_CANON` |
| Splash contains a future development | `AUTHORIAL_INTENT` |
| Splash proposes a retcon | `CONTRADICTORY` + `CANON_CHANGE_REQUIRED` only if the user explicitly wants the change |
| Splash contains an unresolved contradiction | `CONTRADICTORY` / `UNRESOLVED` — flag; `main` remains baseline |
| `main` remains authoritative | Default whenever Splash would replace an established fact without integration |

Only an **explicit or sufficiently supported canon integration** (admission onto `main` via the project's changelog / transformation / dependency-sweep process) causes Splash development to replace established `main` canon.

---

## 7. Generation behavior

**From `main` alone** (no relevant Splash, or Splash empty for this request): use established `main` canon.

**From `main` with relevant Splash context** (the default when live `arena/*` heads exist):

- Baseline = established `main` canon
- Add Splash according to class ([§5](#5-content-level-classification))
- Do **not** present `PROPOSED_CANON`, `AUTHORIAL_INTENT`, `DEVELOPMENTAL`, or `EXPLORATORY` as established historical fact
- `CANON_CLARIFICATION` may be used to understand `main` better
- `CONTRADICTORY`: record the conflict; do not convert Splash into canon

**Explicit continuation of a Splash storyline** (`continue_splash_storyline` or target ref is a Splash head):

- Splash is the **authoring context**
- Still label every constraint's status
- Still do not treat proposed/developmental Splash as established `main` canon
- If the continuation would *establish* something inconsistent with `main`, **flag it** (`REQUIRES_CLARIFICATION` or `CANON_CHANGE_REQUIRED`) — do not silently promote

---

## 8. Adaptation

As the author writes:

- Splash may develop new material
- `main` may incorporate it (then reclassify toward `CONFIRMED_CANON`)
- Splash may clarify previously ambiguous `main`
- `main` may establish a different outcome (Splash may become `CONTRADICTORY` or abandoned intent)
- Provisional Splash may become canonical — **only after integration onto `main`**
- Intended material may be abandoned

Previous classifications are evidence, not identity. Hash change on either side → re-resolve.

---

## 9. Final principle

Protect the canon. Understand the author's evolving development. Do not collapse those two jobs into a branch label.
