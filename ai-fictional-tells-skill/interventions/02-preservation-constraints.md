# Preservation Constraints (Semantic & Literary Preservation System)

**Purpose.** Every transformation — at every level — must be evaluated against
these constraints before it is applied, and re-evaluated after. The skill
**rejects** any transformation that improves a supposed AI-tell score while
degrading the actual fiction. This is the binding contract of the skill; the
intervention hierarchy (`../interventions/01-intervention-hierarchy.md`) cannot override it.

## 1. The fourteen preservation dimensions (PV-1 … PV-14)

| # | Dimension | Definition | Violation examples (reject) |
|---|---|---|---|
| PV-1 | **Plot preservation** | Events, causes, consequences unchanged | deleting/altering an event; breaking a causal link; moving a payoff |
| PV-2 | **Character preservation** | Identity, goals, values, history, relationships unchanged | making a character act against established goals without new motivation; erasing history |
| PV-3 | **Character voice** | Edits to speech/interiority stay within the character's voice profile | re-voicing a character toward a generic "quirky" target; flattening a deliberate register |
| PV-4 | **Narrative voice** | The narrator's established stance, distance, and idiosyncrasies are preserved | "correcting" deliberate narrator tics (essayistic glosses, flatness, repetition that is the *voice*) |
| PV-5 | **Setting** | Places, times, and their specificities unchanged | replacing specific setting detail with generic equivalents; moving scenes |
| PV-6 | **World rules** | Magic/tech/social rules and costs unchanged | altering a rule to make a fix convenient; introducing rule contradictions |
| PV-7 | **Timeline** | Temporal order, durations, dates unchanged | reordering that breaks causality; changing durations silently |
| PV-8 | **Point of view** | Perspective, distance, and focalization unchanged (unless the author requested POV work) | shifting close third to omniscient to enable an edit; breaking free indirect style |
| PV-9 | **Emotional trajectory** | The arc's shape, depth, and turning points unchanged | flattening a low; smoothing a deliberate jaggedness; deleting an earned beat |
| PV-10 | **Information availability** | What the reader knows, when, and what characters know, unchanged | leaking future knowledge; cutting a fact the reader needs later; implication that hides plot-critical facts |
| PV-11 | **Tone** | Register, humor level, temperature of the prose unchanged | "roughening" or "polishing" passages; inserting humor into a grave scene |
| PV-12 | **Genre** | Contractual conventions intact | deleting a thriller's scene button; opening a mystery's unplanted solution; breaking a romance HEA |
| PV-13 | **Thematic intent** | The author's declared themes, worldview, and message unchanged | deleting a theme statement the author wants; "fixing" moral clarity the author intends |
| PV-14 | **Stylistic intent** | The author's declared style anchors (plainness, lyricism, fragments, repetition) unchanged | enforcing a house style; "varying" prose the author wants uniform |

## 2. The rejection rule (binding)

> A transformation is applied if and only if **all** fourteen dimensions are
> preserved (or an explicit, author-approved trade-off is recorded in the
> intervention log). Otherwise it is rejected — regardless of how much it
> would lower any tell score.

Additional reject conditions:
- **New-artifact rule.** Reject any edit that introduces another documented
  tell (fixing P04 by inserting errors, fixing E01 by opaque behaviorism).
- **Familiarity rule.** Reject edits that merely make the text *different*;
  the edit must make the identified cause *absent* (the function test must
  now pass).
- **Churn rule.** Reject edits whose only measurable effect is text churn
  (no function gained, no redundancy removed).

## 3. Intentionality: distinguishing deliberate choice from accidental artifact

Before any intervention, every finding passes the intentionality check:

1. **Author-intent consultation.** Explicit author declarations (style
   anchors, content boundaries, device requests) are checked first. If the
   pattern matches a declared intent → preserved (Level 0), recorded as
   intentional.
2. **Story-model consistency.** Does the pattern cohere with the story's own
   established choices (narrator contract, character profiles, genre
   contract)? Deliberate devices are *locally consistent with the work*;
   artifacts are distributional habits that ignore the work's choices.
3. **Function test.** taxonomy/20 §20.2: does the passage do deliberate work
   (carry information, contrast, rhythm, voice)?
4. **Uncertainty → preserve.** If intentionality cannot be determined, the
   skill preserves and reports (Level 0) rather than guessing. Erring
   toward preservation is a design requirement, not a soft preference.

## 4. Causality requirement for structural edits

Any Level ≥4 edit must pass the causality audit (frameworks/05 §4):
the before/after causal chains are compared, and the edit is rejected if any
event loses its cause or consequence, or any character acts on information
they could not have.

## 5. The story model as the enforcement substrate

All checks run against the story model (`../interventions/03-story-model.md`):
the preservation dimensions are its fields. A proposed edit is simulated
against the model; any violated field produces a specific, quotable
rejection reason (e.g., "rejected: violates PV-10 — Maya learns of the
letter at chapter 3; proposed dialogue leaks it at chapter 2").

## 6. Post-edit re-evaluation

After every applied edit (or batch), re-run:
1. the preservation checks on the changed span;
2. the tell detector on the changed span (did the cause disappear? did a
   new tell appear?);
3. the consistency ledgers for the changed span (frameworks/06);
4. the **voice-baseline check**: the edited span must sit inside the draft's
   narrative voice baseline (`03-story-model.md` §Narrative voice baseline).
   A span that now reads "editor" rather than "this draft" fails PV-4/PV-14
   even when no fact, beat, or tone-quarter moved.
Any failure → automatic revert of that edit, logged.

After the last intervention level, the **final read**
(`../spec/05-pipeline.md` Stage 4b, FR-1…FR-7) runs once over the whole
revised draft — including the *cumulative* check that the set of edits has
not converged the draft toward one register or rhythm. Per-edit preservation
does not imply batch preservation; that is what the final read exists to
catch.

## 7. Hard exclusions (never permissible, regardless of score)

- Inserting grammatical errors, typos, or "imperfections" (S01 shows human
  essays have *more* errors, but error-insertion is a humanizer artifact —
  `../spec/07-failure-modes.md` F-1).
- Randomization of word order, sentence order, or synonyms.
- Detector-score-driven edits of any kind (S12–S14, S35).
- Removal of provenance/disclosure where the author's process requires it.
- Any edit to content boundaries the author has set (PV-14 covers style;
  content boundaries are absolute).
