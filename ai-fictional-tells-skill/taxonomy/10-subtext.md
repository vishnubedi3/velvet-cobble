# Taxonomy 10 — Subtext Tells

**Sources for this cluster:** S04, S28, S29, S37, S38, S39.
**Dominant causes:** K3 (explicitness preference), K4 (interpreted fiction in training), K2 (no implication tracking).

> Note on evidence: models can *comprehend* implicature at near-human level (S38:
> GPT-4 94% on implicature MCQ), but *production* defaults to explicitness. The
> subtext tells are therefore generation-stance problems, not comprehension gaps.

---

## U01 — Characters say what they mean

- **Definition.** Dialogue carries literal, complete meaning; characters state
  positions, feelings, and intentions directly instead of implying, deflecting, or
  concealing them.
- **Example pattern.** "I'm asking you to stay because I'm afraid of being alone" —
  where human dialogue would say "You could stay. The couch pulls out."
- **Observable characteristics.** Literal-meaning coverage of scene intent; no
  pragmatic gaps; S28: AI stories state what human characters imply; S38's finding
  that models *can* do implicature makes the production default a stance, not a
  ceiling.
- **Evidence.** S28 (Tier 0), S38 (Tier 1), S37 (Tier 1). Confidence: **Medium-High**.
- **Likely cause.** K3: clarity and helpfulness; a model that implies risks being
  unhelpful.
- **Variation.** Genre: strongest in romance/drama; weakest in noir (templates force
  tough talk, but the *meaning* still leaks out).
- **Severity.** 2. **False-positive risk.** 2 — direct characters exist and are
  legitimate; the tell is the *universal* directness.
- **Effect on quality.** No room for the reader; characters without privacy;
  dialogue without tactics.
- **Recommended mitigation.** Level 3: convert one layer of meaning to implication —
  the character wants something but says something adjacent (offer, complaint,
  deflection) that a reader can decode. Keep each character's directness profile
  (some should stay blunt).
- **Side effects.** Opaque scenes that lose the reader (the implication must be
  decodable).
- **Validation.** Reader decode test (benchmark metric A5).

## U02 — Narrator explains significance

- **Definition.** The narrator tells the reader why something matters, what it
  means, or what to conclude — the interpretive layer added to every significant
  event.
- **Example pattern.** "It was a small gesture, but it meant everything." /
  "Neither of them knew it yet, but the argument would define the rest of their
  marriage."
- **Observable characteristics.** Significance-statements adjacent to events;
  S28's themes-stated-outright; V02 is this tell's voice-side twin.
- **Evidence.** S28 (Tier 0), S04 (Tier 0). Confidence: **High**.
- **Likely cause.** K3 + K4: training text interprets fiction; the model narrates
  from the interpretation.
- **Variation.** Genre: strongest in literary/coming-of-age; weakest in hard-boiled.
- **Severity.** 3. **False-positive risk.** 2 — narrators who interpret are a
  tradition (Dickens, Tolstoy); the tell is the *unearned* interpretation, the
  reflex.
- **Effect on quality.** The story grades its own homework; the reader's role is
  eliminated.
- **Recommended mitigation.** Level 2–3: delete significance-statements where the
  scene carries the meaning; keep them only as deliberate narrator voice
  (author-intent check, PV-13).
- **Side effects.** Loss of warmth in essayistic fiction.
- **Validation.** "Does the scene carry it without the sentence?" test.

## U03 — Explicit thematic statements in-scene

- **Definition.** The theme is spoken inside the fiction — a character articulates
  the story's meaning, or the narration states it at a beat boundary (N02's
  scene-level execution).
- **Example pattern.** "Maybe home isn't a place," she said softly. "Maybe it's the
  people who wait for you."
- **Observable characteristics.** Aphorism-density at act boundaries; mentor
  characters as theme-delivery; S28 (themes outright).
- **Evidence.** S28 (Tier 0), S04 (Tier 0). Confidence: **Medium-High**.
- **Likely cause.** K3 + K4: the theme is available in the model's context (from the
  prompt's genre+theme structure) and gets verbalized.
- **Variation.** Genre: strongest in YA/literary; weakest in absurdist/noir.
- **Severity.** 2. **False-positive risk.** 1.
- **Effect on quality.** The theme becomes product copy; subtext evaporates.
- **Recommended mitigation.** Level 2: cut the statement. Level 3: if the line must
  exist, give it to the *wrong* character at the wrong moment, or let it be
  partially true.
- **Side effects.** Thematic void if the scenes don't carry the theme (then fix
  scenes, not lines).
- **Validation.** Theme-carrier audit (N02's test).

## U04 — Post-action interpretation

- **Definition.** After an action or exchange, the narration decodes it for the
  reader: what the action "really" meant.
- **Example pattern.** He left without looking back. It wasn't anger, she realized —
  it was fear. The telling glance explained immediately.
- **Observable characteristics.** Interpretation directly following enacted beats;
  E02's narrative face; TTCW subtext dimension (S04: forced subtext).
- **Evidence.** S04 (Tier 0: subtext measure — "does subtext enrich or feel
  forced?"), S28 (Tier 0). Confidence: **Medium**.
- **Likely cause.** K3: completeness; each beat must be "understood" before the text
  moves on.
- **Variation.** Genre: strongest in romance/literary; weakest in minimalist
  fiction.
- **Severity.** 2. **False-positive risk.** 2.
- **Effect on quality.** The beat's ambiguity — its life — is spent instantly.
- **Recommended mitigation.** Level 2: delete the decoding; let the action stand.
  Keep decodings that *misdirect* (intended unreliable narration).
- **Side effects.** Beats that read as random without their explanation (then the
  action wasn't specific enough — fix the action).
- **Validation.** Reader inference test: is the intended meaning recoverable from
  the action alone?

## U05 — Full closure; no unresolved meaning

- **Definition.** The text ends with every question answered — not just plot
  (N06) but *meaning*: the reader is handed the completed interpretation.
- **Example pattern.** Final paragraphs that summarize what it all meant, who
  learned what, and how everything is now understood.
- **Observable characteristics.** CAspER: closure is among the least variable
  dimensions (S29); S04 endings; S28 explicitness.
- **Evidence.** S29 (Tier 0), S04 (Tier 0). Confidence: **Medium-High**.
- **Likely cause.** K3: complete answers are preferred; ambiguity is risky.
- **Variation.** Genre: strongest in romance/drama (where some closure is
  contract); most tell-like in literary/horror.
- **Severity.** 2. **False-positive risk.** 3 — readers like closure; the tell is
  the *total* closure, the interpretive surrender.
- **Effect on quality.** Nothing to think about afterward; the story doesn't
  outlive its last page.
- **Recommended mitigation.** Level 2–4: end on an image or event that *implies*
  the meaning; leave the interpretation to the reader. Author-gated; respect genre
  contracts.
- **Side effects.** Confusing endings where closure was the contract.
- **Validation.** Post-read recall test: what does the reader take away vs. what
  the text asserted?

## Monitored / folklore (not acted upon)

| Pattern | Status | Why |
|---|---|---|
| Explicit relationship-dynamics labeling ("their friendship had grown strained") | Monitored | Subsumed by U04/C01 |
| Dramatic irony overuse (reader knows everything early) | Monitored | Unmeasured; overlaps FS01 |
| Lack of conversational implication | (documented) | U01 |
