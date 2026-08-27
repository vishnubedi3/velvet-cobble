# Taxonomy 08 — Scene Construction Tells

**Sources for this cluster:** S04, S28, S29, S31, S37, S44.
**Dominant causes:** K4 (template scene skeletons), K2 (no scene-purpose planning), K3 (explicit scene logic), K6 (skeleton recycling in long form).

---

## SC01 — Formulaic opening: location+mood+weather triad

- **Definition.** Scene openings execute the same establishing sequence — place,
  atmosphere, weather — in the same order, before character or action (S01's
  structural face).
- **Example pattern.** "The village square was quiet in the pale morning light. A
  cold wind moved through the market stalls." — for the nth scene.
- **Observable characteristics.** Opening-type histogram with one dominant type;
  TTCW scene-vs-exposition 50.0 vs 91.7 (S04).
- **Evidence.** S04 (Tier 0), practitioner (S44). Confidence: **Medium**.
- **Likely cause.** K4 + K2: the "establishing shot" is the corpus's default scene
  opener.
- **Variation.** Genre: strongest in SFF/romance; weakest in dialogue-led.
- **Severity.** 2. **False-positive risk.** 1.
- **Effect on quality.** Scenes blur together; every entry reads the same.
- **Recommended mitigation.** Level 3–4: vary opening types by scene purpose
  (action-first, dialogue-first, in medias res, perception-first); keep establishing
  shots where rhythm needs the breath.
- **Side effects.** Forced variation reads as jumpiness.
- **Validation.** Opening-type diversity audit (frameworks/04).

## SC02 — Characters enter with emotional state announced

- **Definition.** Characters arrive in a scene pre-explained: their mood and its
  cause stated at or before entry, so the scene can be read as its own summary.
- **Example pattern.** "Mara entered, still angry about the morning's argument" —
  the scene then demonstrates the anger that was just announced.
- **Observable characteristics.** Entry-adjacent emotion labels (C01 at scene
  boundary); S28's explicitness; S37's affective categories.
- **Evidence.** S28 (Tier 0), S37 (Tier 1). Confidence: **Medium**.
- **Likely cause.** K3 (clarity) + K4 (scene summaries in training).
- **Variation.** Genre: strongest in drama/romance.
- **Severity.** 2. **False-positive risk.** 2.
- **Effect on quality.** The scene's dramatic question is answered before it's
  asked; entrances lose surprise.
- **Recommended mitigation.** Level 2–3: cut the announcement; let the entrance and
  behavior reveal the state (or mislead about it — better).
- **Side effects.** Unexplained moods read as inconsistency when behavior doesn't
  carry them.
- **Validation.** Blind-read: can the reader infer the state from the scene alone?

## SC03 — Scene purpose explicitly stated

- **Definition.** Characters or narrator announce what the scene is for ("We need
  to talk about the inheritance", "This meeting would decide everything").
- **Example pattern.** Purpose-declarations at scene tops; scenes that behave
  exactly as advertised.
- **Observable characteristics.** Stated-intent sentences early in scenes; S04's
  scene-vs-exposition gap; U03's twin at scene scale.
- **Evidence.** S04 (Tier 0), S28 (Tier 0). Confidence: **Medium**.
- **Likely cause.** K3: stated purpose = clarity; K4: summaries state purposes.
- **Variation.** Genre: strongest in drama/thriller; weakest in absurdist.
- **Severity.** 2. **False-positive risk.** 2 — characters sometimes *do* announce
  agendas (and lying about agendas is a great device).
- **Effect on quality.** No discovery; the scene cannot surprise its own characters.
- **Recommended mitigation.** Level 2: delete the announcement. Level 3 (better):
  let the stated purpose and the actual purpose *diverge* — the scene's real job
  happens underneath.
- **Side effects.** Unanchored scenes where the reader loses the thread.
- **Validation.** Purpose/behavior mismatch check (is the scene doing what it says
  it's doing? It shouldn't always).

## SC04 — Manufactured scene-end button

- **Definition.** Scene closes with a tension-flavored sentence or cliffhanger hook
  whether or not the scene's content produces one (T03's construction-side twin).
- **Example pattern.** "She closed the door, unaware that it would be the last time
  she ever saw it."
- **Observable characteristics.** Button density near 100%; buttons whose promise
  exceeds the next scene.
- **Evidence.** Practitioner (S44); TTCW endings (S04). Confidence: **Medium**.
- **Likely cause.** K4: episodic template exits.
- **Variation.** Genre: thriller/YA strongest.
- **Severity.** 2. **False-positive risk.** 2.
- **Effect on quality.** Button fatigue (see T03).
- **Recommended mitigation.** Level 2: cut buttons that don't pay; end on image,
  action, or implication where appropriate.
- **Side effects.** Momentum loss in serial fiction.
- **Validation.** Payoff-rate audit.

## SC05 — Repeated scene skeleton across chapters

- **Definition.** The same scene blueprint recurs (entry → purpose → mild conflict →
  partial resolution → button), differing only in content — most visible in long
  texts.
- **Example pattern.** Every conversation scene: greeting, topic, one disagreement,
  agreement-to-disagree, exit line.
- **Observable characteristics.** Skeleton n-gram / beat-sequence repetition;
  LongGenBench: ~45% of long outputs show significant repetition (S31).
- **Evidence.** S31 (Tier 2, direct), S43 (repeated plot elements). Confidence:
  **Medium-High**.
- **Likely cause.** K2 + K6: without scene-level planning, the generator re-samples
  its own most recent structure.
- **Variation.** Genre: strongest in romance/drama; masked in action (varied set
  pieces).
- **Severity.** 3. **False-positive risk.** 1.
- **Effect on quality.** The reader can predict the shape of every scene by chapter
  three.
- **Recommended mitigation.** Level 4: vary beat order per scene purpose
  (frameworks/04); in long form, maintain a scene-type ledger to avoid adjacency
  repeats (frameworks/06).
- **Side effects.** Over-engineering scene variety reads as chaos.
- **Validation.** Beat-sequence clustering over the draft.

## SC06 — Lack of incidental behavior/business

- **Definition.** Characters never do anything unrelated to the scene's purpose: no
  eating, fidgeting, waiting, working, or drifting — action is always plot-relevant.
- **Example pattern.** A kitchen conversation with no one touching food; characters
  who stand still and emote.
- **Observable characteristics.** Zero off-purpose micro-actions; no "business"
  blocking; S03's lack of incidental specificity.
- **Evidence.** S03 (Tier 0), practitioner (S44). Confidence: **Medium**.
- **Likely cause.** K3: unneeded content is pruned by preference; K4: summaries
  keep only plot actions.
- **Variation.** Genre: strongest in literary/drama; weakest in farce.
- **Severity.** 2. **False-positive risk.** 2.
- **Effect on quality.** Scenes feel staged; characters seem to exist only when
  useful; verisimilitude thins.
- **Recommended mitigation.** Level 3: add one character-specific incidental action
  per scene (from the character profile: what *this* person does with their hands)
  — chosen, not random.
- **Side effects.** Action-without-meaning noise.
- **Validation.** Read for physical presence: could the scene be staged in an empty
  room? It shouldn't feel that way.

## Monitored / folklore (not acted upon)

| Pattern | Status | Why |
|---|---|---|
| Over-choreographed gestures (every sentence a movement) | Monitored | Subsumed by SC06/S05 |
| Camera panning within scenes | (documented) | See S05 |
| Formulaic time transitions | Monitored | See Pacing monitored table |
| "Characters explicitly stating the scene's purpose" | (documented) | SC03 |
