# CANON_ADMISSION_PROTOCOL.md

Generated material does **not** automatically become canon.

```
CANON → GUARD → GENERATION → REVIEW / ADMISSION → UPDATED CANON → GUARD → NEXT GENERATION
```

---

## 1. Proposed vs. admitted

| Material | Where it may live | Canon? |
|---|---|---|
| Guard report / contract | host audit store; `samur/05-quality/` only if that directory already exists on the branch | No |
| Narrative draft / pilot | `samur/narrative/` only if the applicable branch has that location (H-001 working default; confirmed on some session branches, **not** on others) | No |
| Chat output | nowhere durable unless committed as one of the above | No |
| Hypothesis | `samur/03-hypotheses/` | No |
| New question | `samur/04-questions/` | No |
| Admitted world fact | `samur/02-canon/` with `Status: CANON`, changelog, dependencies | **Yes** |

Never intermix narrative prose with `02-canon/`. Never put reports in narrative files.

---

## 2. Admission is explicit

A draft becomes canon only through the project's established workflow on the applicable branch:

1. Evaluate the new claim against current CANON (this skill, kind = worldbuilding or canon_change).
2. If it is a major institution/event, run the 5-step transformation log.
3. Write or revise the canon file(s); set headers.
4. Sweep dependents if high-impact.
5. Changelog entry.
6. Do **not** delete superseded canon; retire it.
7. Commit to the intended branch.

Until step 7 succeeds, the guard must treat the claim as **unadmitted**.

---

## 3. Guard behavior

- **Before admission:** requests may *use* a draft as "what we are trying to write next." They may not *cite* it as world fact. Finding `CX-ADMISSION` if they do.
- **At admission:** the source tree changes. Detect, invalidate, re-resolve.
- **After admission:** subsequent generation must be aware of the new material because it is now in `02-canon/`, not because the old contract mentioned it.

---

## 4. What admission is not

- Passing the guard
- Passing the tell-reduction skill
- User praise of a pilot
- Presence of a file under `samur/narrative/`
- A CHANGELOG note that a pilot was written (that records *activity*, not admission)
- Copying sentences from a chapter into WORLD-MODEL without a canon file

---

## 5. Draft-to-lore feedback (observed project protocol)

Drafting may reveal a genuine need for new lore. That lore is developed in Expansion Space, checked against canon, and persisted in `02-canon/` **if** justified. It is not stuffed into the narrative folder as worldbuilding, and it is not every colorful detail of a chapter.

The guard's job at that moment is ordinary worldbuilding verification plus this admission protocol — not a special narrative backdoor.
