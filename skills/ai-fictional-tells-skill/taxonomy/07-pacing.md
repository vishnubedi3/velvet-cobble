# Taxonomy 07 — Pacing Tells

**Sources for this cluster:** S03, S04, S22, S31, S37, S43.
**Dominant causes:** K2 (no global pacing plan), K3 (immediate resolution), K6 (long-form degradation).

---

## T01 — Uniform scene/beat rhythm

- **Definition.** Scenes and beats arrive at regular intervals of similar length and
  intensity — metronomic pacing with no acceleration, dilation, or rest.
- **Example pattern.** Every chapter: one scene, ~800 words, one emotional peak at
  the same position; the manuscript's beat histogram is a spike.
- **Observable characteristics.** Low variance in scene length and in
  peak-position; TTCW narrative-pacing score 52.8 vs 94.4 (S04); ~45% repetition in
  long outputs (S31).
- **Evidence.** S04 (Tier 0), S31 (Tier 2). Confidence: **Medium**.
- **Likely cause.** K2: autoregression has no pacing plan; scene "sizes" converge on
  the corpus's typical length.
- **Variation.** Genre: strongest in romance/thriller (template lengths); literary
  least.
- **Severity.** 2. **False-positive risk.** 1.
- **Effect on quality.** Pacing is emphasis; uniformity means nothing is emphasized.
- **Recommended mitigation.** Level 4: vary one scene's length and peak position to
  match its dramatic function (short punch scene vs. long slow burn) — from the story
  model's scene-purpose register, not randomly.
- **Side effects.** Length-shuffling without function reads as padding/truncation.
- **Validation.** Beat-histogram comparison pre/post (frameworks/04).

## T02 — Setup-heavy openings, rushed climax

- **Definition.** Investment is front-loaded (world, backstory, stakes) while the
  climax and resolution are compressed — the inverse of most effective drama.
- **Example pattern.** Three chapters of setup, one paragraph of climax, one page of
  denouement; Beguš: weak turning points (S03); TTCW narrative-ending 19.4 vs 91.7
  (S04).
- **Observable characteristics.** Setup:climax length ratio inverted vs. genre
  norms; climax beats summarized rather than rendered.
- **Evidence.** S03, S04 (Tier 0), S43. Confidence: **Medium**.
- **Likely cause.** K2 + K6: generation budget spent early (context fills with
  setup); the ending is written when context pressure is highest; K3 wants it
  resolved cleanly.
- **Variation.** Genre: strongest in SFF (setup-heavy) and thriller (climax-denied);
  less in slice-of-life.
- **Severity.** 2. **False-positive risk.** 2.
- **Effect on quality.** The promised payoff is skimped; anticlimax.
- **Recommended mitigation.** Level 4–6: expand the climax from the story model's
  event register — render (scene) what is currently summarized (summary). Cut setup
  only if redundant with later information (Level 2).
- **Side effects.** Inflation of climax into padded spectacle.
- **Validation.** Ratio check vs. genre baseline + reader payoff judgment.

## T03 — Manufactured scene-end tension beats

- **Definition.** Scenes close on a manufactured tension hook — a portentous
  sentence or mini-cliffhanger — regardless of whether the scene earned it.
- **Example pattern.** Every scene ends with "But she had no idea what was waiting
  for her" or an ominous cut; genuine tension and false tension are indistinguishable.
- **Observable characteristics.** Hook-density at scene ends near 100%; hooks that
  promise more than the next scene delivers.
- **Evidence.** Practitioner-strong (S44); mechanism K4 (serial-fiction templates).
  Confidence: **Medium**.
- **Likely cause.** K4: episodic/click-driven corpus structure teaches
  cliffhanger-buttons as the default scene exit.
- **Variation.** Genre: strongest in thriller/YA; weakest in literary.
- **Severity.** 2. **False-positive risk.** 2 — serial fiction legitimately buttons
  scenes; the tell is the *uniform* button.
- **Effect on quality.** False tension trains the reader to discount real tension;
  scene exits become noise.
- **Recommended mitigation.** Level 2: delete buttons where the next scene's content
  doesn't need them; let scenes end on action, image, or implication instead.
  Preserve genuine cliffhangers (contract: serial thriller).
- **Side effects.** Scenes that end too soft lose momentum where momentum is the
  contract.
- **Validation.** End-type audit: what fraction of buttons pay off?

## T04 — No quiet variation; intensity floor

- **Definition.** The story never goes quiet: no rest scenes, no low-stakes texture,
  no breathing room — a constant moderate hum of significance (E03's pacing face).
- **Example pattern.** Between the funeral and the heist, no scene where someone
  simply buys groceries or argues about nothing.
- **Observable characteristics.** Absence of low-intensity scenes; every scene has a
  goal and stakes; S37's motivational register bias.
- **Evidence.** S37 (Tier 1), S03 (Tier 0). Confidence: **Medium**.
- **Likely cause.** K3: "unnecessary" content is dispreferred; K4: summaries keep
  only what mattered.
- **Variation.** Genre: strongest in literary/coming-of-age prompts (ironic but
  true); weakest in pulp registers that never rest anyway.
- **Severity.** 2. **False-positive risk.** 3 — tight plot-forward fiction
  legitimately never rests; the tell is the *inability* to rest when the story
  would benefit.
- **Effect on quality.** Contrast loss (see E03); characters never exist outside
  plot; the world feels like a stage.
- **Recommended mitigation.** Level 4: insert or restore one quiet scene that
  *deepens character* (not plot) — author-gated.
- **Side effects.** Padding.
- **Validation.** Scene-intent audit: any scene whose purpose is character, not
  plot?

## T05 — Premature resolution / fast reconciliation

- **Definition.** Conflicts resolve at the first opportunity: misunderstandings
  cleared instantly, wounds healed in a scene, confrontations settled in one
  exchange.
- **Example pattern.** The betrayal is forgiven by next chapter; the standoff ends
  with mutual understanding; nothing festers.
- **Observable characteristics.** Conflict-lifespan distribution skewed to minimum;
  S03's weak turning points; F04 is the conflict-side twin.
- **Evidence.** S03 (Tier 0), S43. Confidence: **Medium**.
- **Likely cause.** K3: the model prefers resolved states; unresolved tension is
  "unhelpful."
- **Variation.** Genre: strongest in romance/drama; weakest in noir/serial.
- **Severity.** 2. **False-positive risk.** 1.
- **Effect on quality.** No accumulating pressure; drama evaporates on contact.
- **Recommended mitigation.** Level 4: defer one resolution past its first
  opportunity; let the reconciliation be partial (see R03).
- **Side effects.** Drawn-out conflict without stakes = melodrama.
- **Validation.** Conflict-lifespan audit vs. genre norms.

## T06 — Long-form sag + ending compression

- **Definition.** In long texts: middle sections lose momentum and drift (lost
  information, repeated beats), while endings accelerate into compressed summary.
- **Example pattern.** Chapters 10–18 repeat themes without advancing; the final
  act runs at double speed.
- **Observable characteristics.** U-shaped attention (S22); repetition in long
  outputs (S31: ~45%); degradation across models 1.2–47.1% (S31).
- **Evidence.** S22, S31 (Tier 2, direct long-form measurements); S32 (context
  fragmentation >10k chars). Confidence: **Medium-High**.
- **Likely cause.** K6: mid-context information is least attended; recency bias
  makes the model re-sample recent patterns; context pressure compresses endings.
- **Variation.** Model: varies (S31). Genre: all long forms.
- **Severity.** 2. **False-positive risk.** 1.
- **Effect on quality.** The classic long-form failure: a book that runs out of
  middle and then out of room.
- **Recommended mitigation.** Structural: generate with a maintained story model
  (outline + state, `../interventions/03-story-model.md`); Level 4: re-expand compressed
  endings from the event register; Level 2: cut repeated beats in the sag.
- **Side effects.** Patchwork fixes without a state model reintroduce the sag.
- **Validation.** Long-form consistency audit (frameworks/06) + event-density plot.

## Monitored / folklore (not acted upon)

| Pattern | Status | Why |
|---|---|---|
| Artificial cliffhangers per se | Monitored | Subsumed by T03 |
| Flat event density | Monitored | Overlaps T01 |
| Formulaic time transitions ("Hours later…", "The next morning…") | Monitored | Low harm; fix = Level 1 variation |
