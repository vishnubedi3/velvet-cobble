# Taxonomy 06 — Emotional Tells

**Sources for this cluster:** S03, S04, S08, S28, S37, S43.
**Dominant causes:** K3 (explicitness, positivity), K4 (interpreted emotion in training), K7 (affect sanitization).

---

## E01 — Naming emotion rather than enacting it

- **Definition.** Emotional states are asserted by name (fear, regret, longing)
  instead of communicated through action, behavior, implication, physical reaction,
  dialogue, or subtext.
- **Example pattern.** "She was terrified." as a complete beat — where the scene
  could show the locked door checked twice, the shallow breath, the lie she tells.
- **Observable characteristics.** Emotion-lexicon density; emotion words where
  behavior is absent; S28: AI stories state what humans imply; S37: AI text uses
  explicit affective categories.
- **Evidence.** S28 (Tier 0), S37 (Tier 1), S04 (emotional flexibility). Confidence:
  **High** — the single most cross-corroborated emotional tell.
- **Likely cause.** K3 + K4: the model learned emotion vocabulary from texts that
  *interpret* fiction; alignment rewards stating the state.
- **Variation.** Genre: all; strongest in romance/literary. Perspective: strongest in
  close third / first person. Model: varies (Llama more affectively expressive, S37).
- **Severity.** 3. **False-positive risk.** 2 — direct statement is a legitimate
  register (fairy tale, essayistic fiction); the tell is the *habit*, not the device.
- **Effect on quality.** The reader receives the conclusion instead of the evidence;
  fiction's core transaction — feeling *with* — is short-circuited.
- **Recommended mitigation.** Level 2–3: replace the label with the behavior,
  perception, speech, or implication that would produce it; keep the label only where
  it adds a layer (contrast between felt and shown is itself information).
- **Side effects.** Over-conversion to behavior yields filmed-theater prose;
  interiority is not the enemy, redundancy is.
- **Validation.** Reader-emotion test: does the reader report the intended emotion
  from the revised beat alone (benchmark metric A5)?

## E02 — Emotional reinforcement loops

- **Definition.** One emotion delivered three ways in sequence: felt, then named,
  then explained, then discussed in dialogue — the same beat layered four deep.
- **Example pattern.** "A wave of sadness washed over her. She realized she was
  grieving the life she'd left behind. 'I miss who I used to be,' she whispered."
- **Observable characteristics.** Emotion event → narrator interpretation → character
  self-report chains; no single layer trusted to carry the beat.
- **Evidence.** Mechanism (K3/K4); S04 (emotional flexibility); S28 (explicitness).
  Confidence: **Medium**.
- **Likely cause.** K3: completeness preference — each layer is "clarity insurance."
- **Variation.** Genre: romance/drama strongest. Perspective: close POV strongest.
- **Severity.** 2. **False-positive risk.** 1.
- **Effect on quality.** Emotional beats inflate into bullet points; rhythm dies;
  the reader is triple-told.
- **Recommended mitigation.** Level 2: keep exactly one layer — the one that carries
  new information (usually the enacted one); cut the rest.
- **Side effects.** Cutting the wrong layer leaves the beat ambiguous where clarity
  was intended.
- **Validation.** Layer audit per emotional beat.

## E03 — Manufactured intensity; no flat affect

- **Definition.** Every moment is weighted with significance; the text never permits
  neutrality, boredom, or flatness — everything "means something."
- **Example pattern.** Making coffee narrated with portent; every object "seeming to
  remember"; zero scenes where nothing much happens and that's the point.
- **Observable characteristics.** Absence of zero-affect passages; motivational
  language bias (S37); everything thematic (V04).
- **Evidence.** S37 (Tier 1: motivational/positive bias), S03 (uniformly positive).
  Confidence: **Medium**.
- **Likely cause.** K3: helpful outputs avoid "pointless" content; K4: training
  summaries retain only what "mattered."
- **Variation.** Genre: strongest in literary/coming-of-age; weakest in deadpan
  registers.
- **Severity.** 2. **False-positive risk.** 3 — intensity is a style, not a defect;
  flag only when the work's own register shows it can't rest.
- **Effect on quality.** Constant significance = no significance; contrast dies;
  pacing flattens (T04's emotional face).
- **Recommended mitigation.** Level 4: restore one flat passage where the story's
  rhythm needs a rest; let the neutral scene earn its place by contrast. Author-gated.
- **Side effects.** Inserted banality reads as padding.
- **Validation.** Read the surrounding arc for contrast value.

## E04 — Predictable emotional progression

- **Definition.** Emotion proceeds along the canonical arc — hurt → understanding →
  growth — on schedule, without regressions, plateaus, or wrong turns.
- **Example pattern.** The same five-beat grief ladder in every arc; each emotion
  slotting into the next stage exactly once.
- **Observable characteristics.** Stage-sequence regularity across arcs; no
  emotional backsliding; S03: weak turning points (the arcs don't *turn*, they
  proceed).
- **Evidence.** S03 (Tier 0), S43. Confidence: **Medium**.
- **Likely cause.** K4: the canonical arc is the corpus's most probable emotion
  sequence; K2 prevents deviation.
- **Variation.** Genre: strongest in drama/romance; weakest in absurdist/literary.
- **Severity.** 2. **False-positive risk.** 1.
- **Effect on quality.** Emotional predictability is plot predictability; readers
  stop investing in turns that never come.
- **Recommended mitigation.** Level 4: reorder or repeat one stage — a regression
  after insight, a plateau that doesn't resolve — per the character's profile.
- **Side effects.** Arbitrary regression reads as characterization error.
- **Validation.** Arc-stage audit vs. human six-arc baseline (S08).

## E05 — Positivity/valence smoothing; reduced anger & sadness

- **Definition.** Negative affect is globally reduced; anger, sadness, and despair
  are softened, brief, or converted to "bittersweet"; endings skew positive.
- **Example pattern.** The tragedy ends with quiet hope; the rage scene resolves in
  forgiveness within paragraphs; sustained despair never survives a chapter.
- **Observable characteristics.** LIWC negative-emotion categories reduced (S37);
  uniformly positive arcs with weak lows (S03, S43); human baseline shows real falls
  and sustained negatives (S08, S37).
- **Evidence.** S37 (Tier 1), S03 (Tier 0), S43. Confidence: **High**.
- **Likely cause.** K7 + K3: safety/refusal training and helpfulness preference
  suppress negative affect — the alignment layer, not the language model.
- **Variation.** Genre: horror/tragedy prompts partially override; never fully.
  Model: Llama more expressive (S37); GPT-4o most smoothed (S37).
- **Severity.** 3. **False-positive risk.** 2 — genre contracts (cozy, romance)
  legitimately require positivity; the tell is the *default* where the contract
  doesn't demand it.
- **Effect on quality.** Stakes are unearned if the fall is never real; tragedy,
  horror, and grief fiction are structurally impossible at full intensity.
- **Recommended mitigation.** Level 4–5: deepen and *sustain* one negative beat —
  let the anger or grief last a full scene without compensation; restore the ending's
  tone to the story's contract. Author-gated.
- **Side effects.** Gratuitous darkness; breaking genre contracts.
- **Validation.** Hedonometer-style arc plot vs. genre baseline (frameworks/05).

## Monitored / folklore (not acted upon)

| Pattern | Status | Why |
|---|---|---|
| Physical-cliché catalog (heart raced, breath caught, stomach dropped) | Monitored | Subsumed by E01 (the cliché is the label's enactment); fix = specific behavior |
| Tears/crying as default marker | Monitored | Frequency unmeasured; overlaps E04 stage-ladder |
| Moralizing interior monologue ("She realized that…") | Monitored | Subsumed by U04/N02 |
| "Show don't tell" as a mechanical rule | **Rejected as rule** | Craft doctrine, contested by practitioners; the skill converts only *redundant* tells, never enforces a style |
