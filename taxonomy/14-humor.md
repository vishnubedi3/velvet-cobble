# Taxonomy 14 — Humor Tells

**Sources for this cluster:** S02, S05, S44.
**Dominant causes:** K1 (stock jokes are highest-probability humor), K4 (joke templates), K3 (explain the joke), K2 (no comedic timing model).

> The strongest empirical anchor in this cluster is S05: >90% of 1008 ChatGPT
> jokes were the same 25 jokes. Template reuse is measured; the subtler tells
> (timing, register) are mechanism- and practitioner-level.

---

## H01 — Stock template jokes/beats

- **Definition.** Humor is drawn from a small stock of templates (structures,
  punchline shapes, comic scenarios) rather than generated for the scene.
- **Example pattern.** The same "I asked for X, I got Y" shape recurring; jokes
  that exist independent of the story's world and characters.
- **Observable characteristics.** Joke-shape reuse across outputs (S05's direct
  measurement); humor that could be transplanted to any story unchanged.
- **Evidence.** S05 (Tier 1, direct). Confidence: **High**.
- **Likely cause.** K1 + K4: canonical jokes are the most probable humor
  continuations.
- **Variation.** Genre: strongest in comedy prompts; weakest in literary irony.
- **Severity.** 2. **False-positive risk.** 1.
- **Effect on quality.** Jokes land as citations, not comedy; nothing is funny
  *here* because everything was funny *everywhere*.
- **Recommended mitigation.** Level 3–4: rebuild the joke from *this* story's
  material (character blindness, world rules, scene context) — the comic beat
  must reference what only this story knows. See `frameworks/03` §Humor beats.
- **Side effects.** Over-contextual jokes nobody outside the scene gets (fine in
  fiction — it's not a stand-up set).
- **Validation.** Transplant test: does the joke still work with the names
  changed? If yes, it's a stock joke.

## H02 — Explanatory humor

- **Definition.** The text explains its jokes: punchlines are decoded, irony is
  flagged, wit is followed by interpretation.
- **Example pattern.** A character's dry remark, then the narrator noting how dry
  it was; S05: ChatGPT "accurately explains valid jokes" — explanation is the
  model's native comedic register.
- **Observable characteristics.** Joke + gloss pairs; hedged humor ("she joked,
  though there was truth in it"); humor that doesn't trust itself.
- **Evidence.** S05 (Tier 1: explanation competence = explanation habit), S28
  explicitness. Confidence: **Medium**.
- **Likely cause.** K3: clarity preference; the model learned humor partly from
  joke-*explanation* corpora.
- **Variation.** Genre: strongest in narrator-heavy comedy; weakest in deadpan.
- **Severity.** 2. **False-positive risk.** 1.
- **Effect on quality.** Explained humor isn't humor; the beat dies at birth.
- **Recommended mitigation.** Level 2: delete the gloss; let the remark stand.
- **Side effects.** Beats that read as accidental if the humor is too subtle
  (then sharpen the joke, not the gloss).
- **Validation.** Laugh-without-caption read.

## H03 — Uniform wit across characters

- **Definition.** Every character is equally funny, in the same way: the same
  irony level, the same timing, the same comic register — the model's wit
  distributed across the cast.
- **Example pattern.** The stoic, the child, and the buffoon all deliver the same
  flavor of dry one-liner; D04's comic face.
- **Observable characteristics.** No between-character humor-profile variation;
  S02's single-voice clustering; S05's single joke-stock.
- **Evidence.** S02 (Tier 0), S05 (Tier 1). Confidence: **Medium**.
- **Likely cause.** K1 + K2: one generator, one sense of humor.
- **Variation.** Genre: strongest in comedy/rom-com; weakest in farce (templates
  force differentiation).
- **Severity.** 2. **False-positive risk.** 2.
- **Effect on quality.** Comedy dies on the page: humor is character-specific
  (what each person finds funny *is* their personality).
- **Recommended mitigation.** Level 3: assign humor profiles per character (who
  jokes, who doesn't, who puns, who deadpans, who is *never* funny — the
  unfunny character is the funniest asset) from the story model's voice profiles.
- **Side effects.** Joke-quota distribution reads mechanical.
- **Validation.** Blind attribution test (metric A7).

## H04 — No comedic timing variance

- **Definition.** Comic beats lack timing: no failed jokes, no pauses, no
  anti-climax, no beats that land wrong on purpose — the rhythm of comedy is
  absent.
- **Example pattern.** Every joke lands, at the same place in the exchange, with
  the same setup length; no one ever bombs.
- **Observable characteristics.** Perfect joke-success rate; uniform setup length;
  absence of comedic silence (D01's comic face).
- **Evidence.** Mechanism (K2: no timing model; K3: no failed communication);
  practitioner (S44). Confidence: **Low** — monitor, do not act automatically.
- **Likely cause.** K2 + K3: timing is a global variable the generator doesn't
  track; failed jokes are "unhelpful."
- **Variation.** Genre: comedy strongest; deadpan weakest.
- **Severity.** 1. **False-positive risk.** 3 — many comic styles are
  precision-timed by design.
- **Effect on quality.** Comedy without risk; the reader stops trusting the
  timing because it never surprises.
- **Recommended mitigation.** Level 3 (only on author request): let one joke fail
  or land late — the failure itself must mean something (character, mood).
- **Side effects.** Forced bathos.
- **Validation.** Author-intent check (PV-13).

## Monitored / folklore (not acted upon)

| Pattern | Status | Why |
|---|---|---|
| Generic irony/sarcasm markers ("Oh, wonderful.") | Monitored | Overlaps H01; frequency unmeasured |
| Repeated punchline structures | Monitored | Subsumed by H01 |
| Pun/simile default humor | Monitored | Overlaps H01/P05 |
| Inability to sustain comedic registers in long form | Monitored | Overlaps L06 |
