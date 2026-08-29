# Taxonomy 09 — Narrative Voice Tells

**Sources for this cluster:** S02, S03, S04, S28, S37, S41.
**Dominant causes:** K1 (one distribution = one voice), K3 (explanatory stance), K5 (polish), K2 (no distance control).

---

## V01 — Uniform narrative distance

- **Definition.** The narrator's distance from the character — from inside the skull
  to omniscient overview — never varies; the zoom is fixed.
- **Example pattern.** Every emotional beat narrated from the same middle distance;
  no sudden closeness at crisis, no wide pull-back at chapter turns.
- **Observable characteristics.** TTCW perspective/voice flexibility 16.7 vs 72.2
  (S04); stylometric uniformity (S02); absence of distance shifts.
- **Evidence.** S04 (Tier 0), S02 (Tier 0). Confidence: **Medium**.
- **Likely cause.** K2: distance is a global rhetorical variable the generator never
  tracks; K1 picks the corpus's typical distance and stays.
- **Variation.** Genre: strongest in literary (where distance play is the norm in
  human work); weakest in pulp (which is legitimately fixed).
- **Severity.** 2. **False-positive risk.** 2 — fixed distance is a valid, even
  fashionable choice; the tell is the *unintended* fixity.
- **Effect on quality.** The most powerful rhetorical tool in prose — zoom — is
  unused; crises don't feel closer, epilogues don't feel wider.
- **Recommended mitigation.** Level 4: shift distance deliberately at one structural
  point (closer at the emotional turn, wider at the chapter close) per the story
  model's scene purposes. Author-gated.
- **Side effects.** Erratic zoom is worse than no zoom.
- **Validation.** Distance audit at crisis points (frameworks/04 §Distance).

## V02 — Explanatory narrator / authorial interpretation

- **Definition.** The narrator interprets events for the reader: what they mean,
  why they matter, what to feel about them — the essay voice inside the story.
- **Example pattern.** "It was, she would later understand, the moment everything
  changed" / "The silence said more than words ever could."
- **Observable characteristics.** Interpretation sentences adjacent to events
  (U02/U04's voice-side twin); weight annotations that grade the beat inline ("It
  was nothing, and yet it was everything"; practitioner-cataloged for AI nonfiction,
  S54); S28's themes-stated-outright; TTCW rhetorical complexity 11.1 vs 88.9 (S04).
- **Evidence.** S28 (Tier 0), S04 (Tier 0). Confidence: **High**.
- **Likely cause.** K3 + K4: the model's default register is explanation (it was
  trained on interpreted text and rewarded for clarity).
- **Variation.** Genre: strongest in literary/coming-of-age; weakest in hard-boiled.
  Perspective: strongest in omniscient/close-third narrator.
- **Severity.** 3. **False-positive risk.** 2 — essayistic narrators (Saunders,
  Tolstoy) are a tradition; the tell is the *reflex*, not the mode.
- **Effect on quality.** The reader is managed; trust in their intelligence is
  withheld; the fiction feels narrated at, not experienced with.
- **Recommended mitigation.** Level 2–3: delete interpretations that duplicate what
  the scene shows; keep them only where the narrator's voice *is* the fiction
  (verify against authorial intent — preservation constraint PV-13).
- **Side effects.** Over-cutting the narrator's voice flattens literary style.
- **Validation.** For each interpretation: what does the reader lose if it goes?

## V03 — Generic polish; absence of idiosyncrasy

- **Definition.** The prose is competent, smooth, and anonymous: no distinctive
  tics, no risky syntax, no personality — a style that could belong to anyone and
  therefore to a model.
- **Example pattern.** The whole manuscript could be a house-style brochure;
  nothing in it would identify the author.
- **Observable characteristics.** Stylometric clustering by model, dispersion among
  humans (S02); register uniformity (S41); MAUVE distribution gap (S11).
- **Evidence.** S02 (Tier 0), S41 (Tier 1), S11. Confidence: **High**.
- **Likely cause.** K1 + K5: generation draws from the center of the distribution;
  idiosyncrasy lives in the tails, which decoding truncates.
- **Variation.** Genre: all; strongest in "prestige" registers. Model: all measured
  models (S02).
- **Severity.** 3. **False-positive risk.** 3 — deliberately plain or polished
  styles (Carver, Ishiguro) are legitimately anonymous-looking; the tell is
  *statistical*, best caught at corpus level, not sentence level.
- **Effect on quality.** No voice = no author; the prose is readable and forgettable.
- **Recommended mitigation.** This tell is fixed at the *generation* level (prompt
  voice-specs, author style anchors, temperature) more than at the revision level;
  revisionally, Level 5 rebuilds only where the author requests voice work. Do not
  "roughen" text to fake voice (see `../spec/07-failure-modes.md`).
- **Side effects.** Manufactured quirk is a new tell.
- **Validation.** Corpus-level Delta/MAUVE comparisons, never single-sentence
  judgments.

## V04 — Thematic coherence overreach

- **Definition.** The narrator forces every element into the theme: images echo,
  motifs recur, and coincidences all "mean" — the story is over-aligned with its own
  thesis.
- **Example pattern.** Three different characters independently use bird imagery;
  the weather, the objects, and the subplot all rhyme with the theme.
- **Observable characteristics.** Motif saturation; every detail interpretable as
  thematic; S03's formulaic inner structure; Beguš's lack of incidental material.
- **Evidence.** S03 (Tier 0), S04 (originality-theme 19.4 vs 75.0). Confidence:
  **Medium**.
- **Likely cause.** K4: the theme-first skeleton (N01) propagates coherence downward
  to every detail; K2 can't hold a non-thematic element in mind.
- **Variation.** Genre: strongest in literary/coming-of-age; weakest in farce.
- **Severity.** 2. **False-positive risk.** 2.
- **Effect on quality.** Over-coherence reads as contrivance; the world shrinks to
  the argument.
- **Recommended mitigation.** Level 4: prune the weakest echo or let one element
  *refuse* the theme (see N01). Author-gated.
- **Side effects.** Thematic incoherence where coherence was the point.
- **Validation.** Motif audit: which echoes earn their keep?

## V05 — Absence of controlled ambiguity

- **Definition.** The text never withholds: no open questions, no unreliable
  narration, no productive uncertainty — everything resolves into clarity.
- **Example pattern.** Even the "mysterious" character is eventually explained;
  ambiguous endings are rare and, when present, feel appended.
- **Observable characteristics.** CAspER: closure is among the least variable
  dimensions (S29); TTCW subtext dimension (S04); S28 explicitness.
- **Evidence.** S29 (Tier 0), S04 (Tier 0), S28 (Tier 0). Confidence: **Medium-High**.
- **Likely cause.** K3: clarity preference; unresolved meaning is "unhelpful."
- **Variation.** Genre: strongest in mystery/literary (ironic, since both live on
  withheld meaning); weakest in cozy.
- **Severity.** 2. **False-positive risk.** 3 — many genres and readers *want*
  resolution; ambiguity must be earned and intended.
- **Effect on quality.** No interpretive space; the story is consumed, not lived
  with.
- **Recommended mitigation.** Level 4: keep one question genuinely unanswered (not
  a cliffhanger — an ambiguity), where the genre permits. Author-gated.
- **Side effects.** Cheap ambiguity reads as the author not knowing the answer.
- **Validation.** Author-intent check first (PV-13); then reader retention test.

## V06 — Register monotony across narration/dialogue/thought

- **Definition.** Narration, dialogue, and interior monologue share one register;
  mode shifts don't change the voice.
- **Example pattern.** The character's thoughts, their speech, and the narrator's
  sentences are interchangeable in formality and diction.
- **Observable characteristics.** ChatGPT shows far less register variation than
  humans (S41); formality across modes (S37).
- **Evidence.** S41 (Tier 1), S37 (Tier 1). Confidence: **Medium**.
- **Likely cause.** K1: one distribution for all modes; K5 smooths differences.
- **Variation.** Genre: strongest in literary; weakest in voice-driven genres.
- **Severity.** 2. **False-positive risk.** 2.
- **Effect on quality.** The characters' minds and the narrator's voice blur;
  interiority loses its privacy (P07's voice-side twin).
- **Recommended mitigation.** Level 3: differentiate interiority from narration
  (looser, more partial, more fallible) and both from speech, per the story model's
  voice profiles.
- **Side effects.** Forced informality.
- **Validation.** Register-contrast audit (frameworks/07).

## Monitored / folklore (not acted upon)

| Pattern | Status | Why |
|---|---|---|
| Repetitive rhetorical patterns (anaphora, triads) | Monitored | Subsumed by P02/P04 |
| Predictable metaphor selection | Monitored | Subsumed by P05 |
| Recap/summary voice ("the days passed…") | Monitored | Practitioner-common; overlaps U04/T02 |
| "Lack of controlled ambiguity" as style mandate | (documented) | V05; never a blanket rule |
