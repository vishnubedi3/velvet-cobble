# Taxonomy 15 — Action Tells

**Sources for this cluster:** S22, S31, S37, S44.
**Dominant causes:** K2 (linear rendering, no spatial model), K6 (continuity loss), K7 (consequence softening).

---

## A01 — Sequential choreography ("then, then, then")

- **Definition.** Action rendered as an ordered list of moves — sequential
  coordination with no simultaneity, no cause-mixing, no chaos.
- **Example pattern.** "He ducked. Then he rolled. Then he grabbed the knife. Then
  he lunged." Every motion in sequence, evenly weighted.
- **Observable characteristics.** Sequential-connector density in action
  passages; one motion per sentence; no overlap or interruption.
- **Evidence.** Practitioner (S44); mechanism K2 (autoregression renders one
  event per step). Confidence: **Medium**.
- **Likely cause.** K2: linear generation has no spatial scene model; it narrates
  events in the order generated, not the order experienced.
- **Variation.** Genre: strongest in thriller/action; weakest in literary (where
  action is elided).
- **Severity.** 2. **False-positive risk.** 2 — clean sequential action is a
  legitimate style (Crichton); the tell is the *list* without hierarchy.
- **Effect on quality.** Action loses speed (lists are slower than simultaneity);
  the fight reads like a manual.
- **Recommended mitigation.** Level 3: compress and overlap — subordinate some
  motions to others, let cause and effect interleave, weight only the
  story-critical beats. Level 2: cut connective tissue.
- **Side effects.** Muddied choreography where clarity was needed.
- **Validation.** Read-aloud pace test; beat-weight audit.

## A02 — Spatial/continuity inconsistency

- **Definition.** Action breaks spatial and physical continuity: positions,
  objects, injuries, and who-is-where drift within a scene (the action-specific
  face of long-form continuity loss).
- **Example pattern.** The gun drops, then is fired two lines later; the
  character's left hand is pinned, then she grabs with it; doorways multiply.
- **Observable characteristics.** Contradictory physical state within scenes;
  S31's consistency degradation; S22's lost-in-the-middle (scene state is
  mid-context information).
- **Evidence.** S31 (Tier 2, direct), S22 (Tier 2). Confidence: **Medium-High**.
- **Likely cause.** K6: no persistent scene-state; the model tracks recent
  sentences, not the scene's physics.
- **Variation.** Genre: strongest in action/combat (most state to track);
  weakest in static scenes. Length: worsens with scene length.
- **Severity.** 2. **False-positive risk.** 1.
- **Effect on quality.** Action loses believability; readers catch the
  impossible move and the scene breaks.
- **Recommended mitigation.** Level 2–5: repair against an explicit scene-state
  register (who holds what, where everyone is, what's broken —
  `interventions/03-story-model.md` §Scene state); the fix is a state
  correction, not a rewrite.
- **Side effects.** Over-specifying positions reads as choreography notes.
- **Validation.** State-timeline audit of the scene (frameworks/04 §Scene state).

## A03 — No physical consequence persistence

- **Definition.** Violence has no lasting physics: injuries vanish, damage is
  forgotten, adrenaline never crashes — the body resets after each beat.
- **Example pattern.** The hero takes a blow to the head and thinks clearly two
  paragraphs later; the burned hand pours tea next chapter.
- **Observable characteristics.** Consequence-decay between scenes; S37's
  softened negative affect (Tier 1 adjacent); K7 mechanism.
- **Evidence.** S37 (Tier 1), mechanism K7/K2. Confidence: **Medium**.
- **Likely cause.** K7 (softened consequences) + K2 (no body-state tracking).
- **Variation.** Genre: strongest in thriller/action; weakest in medical/literary
  realism.
- **Severity.** 2. **False-positive risk.** 2.
- **Effect on quality.** Stakes die: if injuries don't persist, danger doesn't
  either.
- **Recommended mitigation.** Level 3: carry one consequence forward (the limp,
  the ache, the broken tool) into later scenes via the story model's state
  register.
- **Side effects.** Injury-accounting that drags the pace (fix the *story-critical*
  consequences, not every bruise).
- **Validation.** Consequence-ledger audit across scenes.

## A04 — Escalation-only action; no fumbles/lulls

- **Definition.** Action scenes escalate monotonically: every beat outdoes the
  last, nobody fumbles, nothing goes wrong in the wrong way, no lull for breath.
- **Example pattern.** The fight starts at 60% intensity and climbs to 100% with
  no drops; no slip, no misfire, no hesitation.
- **Observable characteristics.** Intensity monotonicity; absence of error;
  F01's action-side face.
- **Evidence.** Practitioner (S44); mechanism K3 (competence bias). Confidence:
  **Low** — monitor, do not act automatically.
- **Likely cause.** K3: the model's characters are competent by default; K2 can't
  plan a rhythm with drops.
- **Variation.** Genre: strongest in thriller; weakest in comedy-action.
- **Severity.** 1. **False-positive risk.** 3 — competence porn is a genre
  (Reacher); the tell is the *default*, not the style.
- **Effect on quality.** Action without risk of failure; tension flattens.
- **Recommended mitigation.** Level 3 (author-gated): one fumble or lull where it
  raises stakes (the jammed gun, the wrong turn).
- **Side effects.** Inserted clumsiness reads as character assassination.
- **Validation.** Author-intent check (PV-13).

## Monitored / folklore (not acted upon)

| Pattern | Status | Why |
|---|---|---|
| Repetitive motion verbs (whirled, spun, lunged) | Monitored | Subsumed by P01; fix = Level 1 specificity |
| Cinematic slow-mo excess | Monitored | Overlaps S05/A01 |
| Unrealistic reaction timing (reflection mid-fight) | Monitored | Overlaps A03/C03 |
| Moral commentary inside action | Monitored | Overlaps U04/N07 |
