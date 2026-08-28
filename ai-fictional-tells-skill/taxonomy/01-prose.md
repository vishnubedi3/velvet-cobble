# Taxonomy 01 — Prose-Level Tells

**Sources for this cluster:** S01, S02, S09, S10, S11, S19, S28, S37, S41.
**Dominant causes:** K1 (maximum-likelihood training), K3 (RLHF), K5 (decoding), K8 (evaluator-driven style).

> Caveat: empirical prose-level evidence is strongest for adjacent domains (essays, news).
> Transfers to fiction are labeled with their mechanism. Fiction word lists (Tier 4) are
> excluded; see "Monitored / folklore" at the end.

---

## P01 — Modal-average phrasing

- **Definition.** Word choices cluster at the *most probable* continuation at every
  position, producing text with abnormally low per-word surprise and no lexical risk.
- **Example pattern.** Where a human might write "the stove's pilot light had gone out
  again," the tell produces "the stove was broken"; the statistically typical verb/noun
  pairing wins over the specific one.
- **Observable characteristics.** Low per-word surprisal (GLTR signature, S10); text
  hugs the center of the generator's distribution; MAUVE gap between passage and human
  reference distributions (S11); rare words avoided even when apt.
- **Evidence.** S10 (high), S11 (high), S09. Tier 2 mechanism + Tier 0 stylometric
  clustering (S02). Confidence: **High** (mechanism; surface manifestation varies by model).
- **Likely cause.** K1 + K5. MLE training maximizes average probability; sampling
  truncation removes the tail where specificity lives.
- **Variation.** Cross-model: yes in degree (S02 cluster tightness). Genre: stronger in
  high-template genres (thriller, romance) than literary. Perspective: stronger in
  omniscient narration than in strongly-voiced first person. Length: stable.
- **Severity.** 3. **False-positive risk.** 2 — concise human prose also avoids rare words.
- **Effect on quality.** Generic texture; every story sounds like every other story;
  specificity (the main carrier of voice) is lost.
- **Recommended mitigation.** Level 1–2: replace generic noun/verb pairings with the
  *story-specific* one (the exact object, verb, register the scene demands). Do not
  thesaurus-swap; the replacement must come from scene knowledge (S06 framework:
  world facts), not from a synonym engine.
- **Side effects.** Synonym injection = new artificiality; over-specifying destroys
  deliberate plainness (Hemingway-effect). Only repair where specificity adds
  information the scene needs.
- **Validation.** Human A/B: does the revision name things the story has established?
  Surprisal delta should be moderate, not cosmetic.

## P02 — Balanced/parallel sentence architecture

- **Definition.** Recurring symmetric constructions: tricolons, "not X, but Y",
  "X, and yet Y", paired antitheses — deployed far above natural frequency.
- **Example pattern.** "It was not fear that stopped her, but something older."
  "The room was silent, the city was not, and between them lay everything she'd lost."
- **Observable characteristics.** Cadence repetition across paragraphs; the
  "not X, but Y" frame (readers in S28 spontaneously cite it as an AI marker);
  rule-of-three abuse; rhetorical balance where prose needs asymmetry.
- **Evidence.** S28 (reader-cited marker), S41 (content-word/structural uniformity),
  S10 (template probability mass). Tier 1+0; the pattern itself is distributionally
  plausible but not yet fiction-measured. Confidence: **Medium**.
- **Likely cause.** K1 (balanced constructions are high-probability rhetorical frames)
  + K4 (training on polished, persuasive prose and essays).
- **Variation.** Genre: stronger in fantasy/romance ("epic" register). Perspective:
  stronger in third-person narration. Model: measurable differences likely; unmeasured.
- **Severity.** 2. **False-positive risk.** 2 — many human stylists love antithesis.
- **Effect on quality.** Metronomic prose; rhetorical cadence becomes wallpaper;
  emphasis is diluted because everything is emphasized.
- **Recommended mitigation.** Level 2: break the pattern where it repeats (vary one
  instance; let one stand). Level 3: replace with asymmetric syntax. Never remove all
  balance — occasional antithesis is craft.
- **Side effects.** Artificial "roughening" (chopped syntax) is itself a tell.
- **Validation.** Count per 1k words vs. the author's baseline; flag clusters, not singles.

## P03 — Register inflation (nominalization, formal drift, few hedges)

- **Definition.** Systematic drift toward formal, abstract, nominalized prose with
  reduced epistemic hedging ("maybe, perhaps, seemed").
- **Example pattern.** "The realization of her failure brought about a reconsideration
  of her options" for "She'd failed; she had to rethink."
- **Observable characteristics.** Nominalization density above the corpus baseline
  (S01); fewer modals/epistemic markers (S01); "not only… but also", "furthermore"-style
  connectives in narration; abstraction where concreteness is available.
- **Evidence.** S01 (essays: more nominalizations, fewer discourse/epistemic markers),
  S37 (more formal, more structured), S41 (less register variation). Adjacent-domain
  transfer via K1/K3 mechanism. Confidence: **High** in essays; **High** for fiction via
  the shared mechanism, with fiction-specific measurement still pending.
- **Likely cause.** K1 (formal/academic prose is overrepresented in high-probability
  text) + K3 (clear/complete preference) + K8 (raters reward "sophisticated" words).
- **Variation.** Genre: stronger in SFF/literary prompts; weaker in dialogue-heavy YA.
  Perspective: stronger in narrator voice than character voice. Model: GPT-4o most
  "neutral/polished" (S37).
- **Severity.** 2. **False-positive risk.** 2 — literary fiction is allowed formality;
  the tell is *drift from the work's own register*, not formality itself.
- **Effect on quality.** Distance between narrator and material; intellectualized
  emotion; same-register monotony.
- **Recommended mitigation.** Level 1–2: re-verbalize nominalizations where action is
  stronger; restore hedges where the narrator genuinely doesn't know. Compare against
  the work's own register baseline, not an external style guide.
- **Side effects.** Over-concretizing loses legitimate abstraction; removing every
  hedge produces over-assertive narration (the opposite tell).
- **Validation.** Register consistency check vs. authorial baseline (frameworks/07).

## P04 — Uniform sentence rhythm / low length variance

- **Definition.** Sentence lengths and clause counts vary less than in human fiction;
  paragraphs share one size; cadence never breaks.
- **Example pattern.** 12–18-word declaratives in sequence; every paragraph 3–5
  sentences; no one-word paragraphs, no 90-word sentences, no fragments.
- **Observable characteristics.** Low variance in sentence length distributions vs.
  reference corpora (MAUVE-style comparison, S11); stylometric tightness (S02);
  absence of rhythm contrast.
- **Evidence.** S02 (tight clustering = distributional regularity), S11, S41.
  Confidence: **Medium**.
- **Likely cause.** K1 + K5: decoding toward typical length/register; no prosodic
  planning (K2).
- **Variation.** Genre: least visible in SFF (long descriptive sentences expected),
  most visible in thriller/literary. Perspective: stronger in narration than dialogue.
- **Severity.** 2. **False-positive risk.** 2 — some styles are deliberately even.
- **Effect on quality.** Rhythm is meaning; uniform rhythm flattens tension,
  emphasis, and voice.
- **Recommended mitigation.** Level 1: punctuation-level variation only where emphasis
  is missing (splitting/joining). Level 5 (rare): rebuild a passage whose rhythm
  contradicts its content (short sentences for action, long for drift).
- **Side effects.** Rhythm-shuffling without semantic reason = cosmetic churn.
- **Validation.** Length-variance delta + human "does emphasis land?" check.

## P05 — Decorative figurative density ("as if" scaffolding)

- **Definition.** Metaphor/simile supplied as decoration at a rate that exceeds the
  scene's need, often with the same scaffolding ("as if", "like a", "a kind of").
- **Example pattern.** "Her anger was like a storm gathering at the edge of the
  horizon" — imagery that restates the emotion without adding perception.
- **Observable characteristics.** Figurative language per 1k words above genre
  baseline; similes that explain rather than reveal; imagery ungrounded in the POV
  character's experience domain.
- **Evidence.** S04 (literary-devices score 36.1 vs 88.9 human — the gap includes
  device *aptness*), practitioner consensus (S44, S53). Confidence: **Medium**.
- **Likely cause.** K4: training fiction + its reviews teaches "good prose = decorated
  prose"; K1 selects stock images.
- **Variation.** Genre: stronger in romance/fantasy/literary prompts; weaker in
  hard-boiled registers. Perspective: stronger in narrator voice.
- **Severity.** 2. **False-positive risk.** 2 — lyricism is legitimate.
- **Effect on quality.** Metaphor inflation devalues the good metaphors; imagery
  detaches from perception.
- **Recommended mitigation.** Level 2–3: remove only metaphors that add nothing beyond
  their literal meaning; keep any that (a) carry information, (b) belong to the POV
  character's world, or (c) earn their place by contrast.
- **Side effects.** Over-pruning yields flat, untextured prose.
- **Validation.** For each kept metaphor: name the information it adds. If none, it
  was decorative.

## P06 — Explanatory transitions & signposting

- **Definition.** Narratorial interjections that pre-announce or underline what is
  about to happen / what just happened.
- **Example pattern.** "Little did she know…", "What happened next would change
  everything", "And then everything changed."
- **Observable characteristics.** Cliffhanger-as-transition stock phrases; endings
  that "button" paragraphs; meta-commentary on narrative significance.
- **Evidence.** Practitioner-strong (S44; S53); consistent with N01/N02 mechanism
  (S28). Tier 3. Confidence: **Medium**.
- **Likely cause.** K4: template phrases from genre/fan fiction corpora are
  high-probability continuations; K3 rewards "clear" signposting.
- **Variation.** Genre: thriller/YA strongest. Perspective: almost exclusively
  narrator voice.
- **Severity.** 2. **False-positive risk.** 1.
- **Effect on quality.** Steals the event's power before it happens; reader never
  experiences surprise.
- **Recommended mitigation.** Level 2: delete the signpost; let the next event speak.
- **Side effects.** None beyond losing a rhythm device the author may have wanted
  (rarely, in literary fiction, signposting is ironic — check intent).
- **Validation.** Re-read for surprise retention.

## P07 — Over-polish / register monotony

- **Definition.** Zero friction anywhere: no ungainly but expressive sentences, no
  colloquial leakage, no tonal modulation — the text reads as a single smoothing pass.
- **Example pattern.** A funeral scene and a marketplace scene in the same register;
  narration, interior monologue, and dialogue all equally "clean."
- **Observable characteristics.** Absence of register contrast (S41: ChatGPT shows far
  less register variation than humans); formality across all modes (S37).
- **Evidence.** S41, S37, S02. Confidence: **Medium**.
- **Likely cause.** K3 (polish preference) + K5 (low-temperature smoothness) + K2
  (no revision means no leftover texture — human texture partly comes from *revision
  choices*, not errors).
- **Variation.** Strongest in default settings; reduced with temperature/prompting.
- **Severity.** 2. **False-positive risk.** 3 — "clean prose" is a legitimate and
  popular style; this tell must never be fixed by adding dirt.
- **Effect on quality.** Monotone voice; no contrast between registers; flat affect.
- **Recommended mitigation.** Level 2: modulate register where *content* demands it
  (character speech vs. narration vs. interiority). Never insert errors (see
  `../spec/07-failure-modes.md`).
- **Side effects.** Forced colloquialism is worse than polish.
- **Validation.** Register-contrast audit per scene purpose (frameworks/07).

## Monitored / folklore (not acted upon)

| Pattern | Status | Why |
|---|---|---|
| Em-dash density as an AI tell | **Monitored** (partial support: S28 readers cite em-dashes; unmeasured) | Dash use varies by model/finetune and by human cohort; measure per corpus before use |
| "AI never uses contractions" | Folklore | Contradicted by direct generation tests; unsupported |
| Fiction "AI word lists" (tapestry, testament, etc.) | Folklore for fiction | S17–S19 measured academic text only; no fiction corpus measurement exists |
| Rhetorical-question narration | Folklore-adjacent | Plausible (K4) but unmeasured |
| Adjective stacking per se | Monitored (partial: S41 content-word density) | Many human styles stack adjectives deliberately |
