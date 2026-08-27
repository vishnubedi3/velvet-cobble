# Taxonomy 02 — Narrative-Level Tells

**Sources for this cluster:** S03, S04, S16, S28, S29, S37, S43.
**Dominant causes:** K2 (no global plan), K4 (template/interpretee training data), K3 (RLHF explicitness/closure).

---

## N01 — Story-as-argument (theme→beats→moral skeleton)

- **Definition.** The story is generated as the *proof* of a theme: events are
  selected to instantiate a thesis, then the thesis is restated — the essay structure
  wearing fiction's clothes.
- **Example pattern.** Prompt "a story about grief" yields: inciting loss → three
  escalating grief-behaviors → epiphany → acceptance, each beat visibly serving the
  thesis, in order.
- **Observable characteristics.** Every scene "advances the theme"; no digressions;
  events interpretable as arguments; Beguš's "inner structure followed paragraph by
  paragraph" (S03).
- **Evidence.** S03 (High, Tier 0), S04 (originality-in-theme 19.4 vs 75.0), S28
  (themes stated outright), S43. Confidence: **High**.
- **Likely cause.** K4: training contains stories *and* their interpretations; the
  model writes from the interpretation. K2: without a plan, the highest-probability
  plan is the theme's canonical beats.
- **Variation.** Genre: strongest in literary/realist prompts, weakest in episodic
  adventure. Perspective: all. Length: strengthens with length (each chapter proves
  the theme again).
- **Severity.** 3. **False-positive risk.** 1.
- **Effect on quality.** Predictability; story as lecture; no surplus life (the
  digressions, contradictions, and unrelated events that make fiction feel true).
- **Recommended mitigation.** Structural, not sentence-level: introduce one
  non-thematic element the story must *accommodate* (a character who doesn't fit the
  thesis, an event that resists interpretation), then re-derive beats causally
  (frameworks/05). Level 4–6 territory; requires author consent.
- **Side effects.** Random insertion of noise breaks coherence; the non-thematic
  element must be *integrated*, not bolted on.
- **Validation.** Expert read: can each scene be replaced by its thesis sentence
  without loss? If yes, the skeleton is still showing.

## N02 — Explicit thematic statement

- **Definition.** The theme is stated in so many words by narrator or character
  ("Grief, she understood now, was not an enemy but a teacher").
- **Example pattern.** Closing paragraphs that summarize the story's meaning; a
  mentor character whose speech is the theme; the narrator announcing what "this was
  really about."
- **Observable characteristics.** Abstract nouns of meaning (lesson, understood,
  realized, meant) clustered near act boundaries; Villanova authors: AI stories
  "stated their themes outright" (S28).
- **Evidence.** S28 (Tier 0), S04 (rhetorical complexity 11.1 vs 88.9), S03.
  Confidence: **Medium-High**.
- **Likely cause.** K3 (completeness preference — a story that explains itself scores
  as "clear") + K4.
- **Variation.** Genre: literary/coming-of-age strongest; hard-boiled/absurdist
  weakest. Perspective: narrator voice dominant.
- **Severity.** 3. **False-positive risk.** 1.
- **Effect on quality.** The single most-quoted AI-fiction marker (S28); converts
  experience into summary; denies the reader the interpretive work that creates
  absorption (which, paradoxically, S28 shows readers reward — explicitness is popular
  but it is exactly what makes the text *feel* generated).
- **Recommended mitigation.** Level 2–3: delete the statement; verify the scenes
  already carry the theme (they do — the statement is usually redundant). Keep it
  only when the author intends an essayistic narrator.
- **Side effects.** If the scenes are weak, deleting the statement leaves the theme
  uncarried — then the fix is scene work (Level 5–6), not re-adding the statement.
- **Validation.** Reader paraphrase test: can an independent reader state the theme
  without the statement? (See `../spec/09-evaluation-benchmark.md`.)

## N03 — Perfect setup/payoff symmetry

- **Definition.** Every planted element pays off; every payoff was planted; the
  ledger balances exactly.
- **Example pattern.** The knife in chapter 1 is the murder weapon; the offhand
  allergy is the climax's hinge; no plant goes unfired, no payoff is unplanted.
- **Observable characteristics.** Plot-element ledger with zero residues; no
  Chekhov's gun left on the wall; no payoff that arrives unheralded.
- **Evidence.** S03 (formulaic structure), S43 (repeated plot elements / low
  originality), S04 (structural flexibility 19.4). Mechanism-level; direct measurement
  pending. Confidence: **Medium**.
- **Likely cause.** K4 (writing-advice corpora teach setup/payoff) + K3 (complete
  resolution) + K2 (planting is easy, subverting is hard).
- **Variation.** Genre: mystery/thriller highest (and most legitimate there);
  literary lowest. Length: strengthens with length (long-form ledgers get tidier).
- **Severity.** 2. **False-positive risk.** 2 — craft-conscious humans also balance
  ledgers; the tell is *perfect* balance plus nothing else.
- **Effect on quality.** Clockwork predictability; no surplus, no life, no loose
  threads that make a world feel larger than the plot.
- **Recommended mitigation.** Level 4: allow one small element to remain unresolved
  or unechoed — deliberately, and only if it enriches texture (frameworks/05).
  Not applicable in mystery, where the ledger is the genre contract.
- **Side effects.** Dropped threads read as error if not artfully placed.
- **Validation.** Expert read for "did the loose end read as intent or accident?"

## N04 — Default clean three-act/quest template

- **Definition.** Unprompted convergence on the same act skeleton: equilibrium →
  inciting event → rising trials → crisis → climax → tidy denouement, often with a
  literal journey or quest.
- **Example pattern.** "A young [X] must [Y] to save [Z]" executed beat for beat.
- **Observable characteristics.** Act boundaries detectable by formula; climax at the
  expected 80–90% position; Beguš: structure "paragraph by paragraph" (S03).
- **Evidence.** S03 (High), S43, S16 (similarity across stories). Confidence: **Medium**.
- **Likely cause.** K4: the quest/three-act template is the corpus's most probable
  story shape; K2 prevents deviation.
- **Variation.** Genre: fantasy/adventure strongest; literary/short strongest
  deviations in human work, least in AI work.
- **Severity.** 2. **False-positive risk.** 2 — the three-act shape describes most
  competent human stories too; the tell is the *default*, not the shape.
- **Effect on quality.** Sameness across all outputs; absence of structural ambition.
- **Recommended mitigation.** Structural-level: author decides the skeleton first
  (the skill supplies skeleton *options* derived from the story model, not prose
  fixes). Level 4–6 only.
- **Side effects.** Experimental structures without craft = incoherence.
- **Validation.** Structure-diversity check across a run-set (S16-style embedding
  similarity).

## N05 — Repeating conflict cycles

- **Definition.** The same conflict shape recurs (misunderstanding → confrontation →
  temporary resolution), escalating in magnitude but not in kind.
- **Example pattern.** Three successive "she stormed out" beats; every obstacle is a
  misunderstanding; reconciliation scenes mirror each other.
- **Observable characteristics.** Beat-pattern repetition; Xu et al. 2025: repeated
  plot elements in LLM narratives (via S43).
- **Evidence.** S43 (Tier 0 secondary), S31 (repetition in long outputs). Confidence:
  **Medium**.
- **Likely cause.** K2: without a stateful plot memory the generator re-samples its
  own recent patterns; K4 template conflicts.
- **Variation.** Genre: romance/drama strongest; thriller masks it with escalation.
  Length: worsens with length (→ L02/L03).
- **Severity.** 2. **False-positive risk.** 1.
- **Effect on quality.** Conflict fatigue; characters seem stuck in a loop.
- **Recommended mitigation.** Level 4: vary the conflict *type* (external vs internal
  vs relational) per cycle per the story model's conflict register
  (`../interventions/03-story-model.md`).
- **Side effects.** Inserting random new conflicts breaks causality.
- **Validation.** Cycle-shape audit over the whole draft.

## N06 — Neat closure; all threads tied

- **Definition.** Endings that resolve every thread, heal every relationship, and
  return every character to a settled state.
- **Example pattern.** Final chapter: villain defeated, couple united, sidekick
  promoted, town rebuilt, last line of quiet hope.
- **Observable characteristics.** Resolution inventory = thread inventory; CAspER:
  closure is one of the least variable dimensions across regenerations (S29).
- **Evidence.** S29 (closure stability), S04 (narrative-ending 19.4 vs 91.7), S03
  (positive endings). Confidence: **Medium**.
- **Likely cause.** K3 (completeness/satisfaction preference) + K4 (canonical
  endings).
- **Variation.** Genre: strongest in romance/cozy; legitimate there. Weakest in
  literary/horror human work — and most tell-like in those genres.
- **Severity.** 2. **False-positive risk.** 2 — genre contracts *require* closure.
- **Effect on quality.** The ending feels administered rather than arrived at.
- **Recommended mitigation.** Level 4: convert one resolution from *stated* to
  *implied* (or leave one genuinely open) where genre permits. Do not touch mystery
  payoffs or romance HEA contracts.
- **Side effects.** Breaking genre contracts costs readers, not gains them.
- **Validation.** Genre-contract check first (frameworks/07), then reader reaction.

## N07 — Moral clarity / didactic resolution

- **Definition.** The story's moral universe is legible: right and wrong are
  unambiguous, wrongdoing is punished or redeemed, the lesson is available.
- **Example pattern.** Antagonist's cruelty is unmotivated evil; protagonist's flaws
  are sympathetic and overcome; the ending distributes justice exactly.
- **Observable characteristics.** No moral remainder; no sympathetic villain without
  redemption arc; Beguš: newer models' progressive-value alignment (S03); reduced
  negative affect (S37).
- **Evidence.** S03, S37 (High, Tier 0/1). Confidence: **Medium-High**.
- **Likely cause.** K3 + K7: alignment makes the model morally legible by design.
- **Variation.** Genre: strongest in fantasy/YA; weakest in noir/literary (and most
  tell-like there). Model: stronger in heavily-aligned models.
- **Severity.** 2. **False-positive risk.** 1.
- **Effect on quality.** Fiction flattens into fable; villains become furniture;
  tragedy becomes impossible.
- **Recommended mitigation.** Level 3–5: give one antagonist an interest that
  conflicts with the protagonist's without being *evil*; allow one unjust outcome.
  Author-gated (this touches worldview; see preservation constraints).
- **Side effects.** Forced moral ambiguity reads as posturing.
- **Validation.** Expert + author review (author intent is authoritative here).

## N08 — Valence-smoothed emotional arc

- **Definition.** The story's sentiment trajectory is uniformly positive or
  shallowly oscillating, lacking the deep falls of human arcs (tragedy, man-in-a-hole
  are underrepresented).
- **Example pattern.** Comforting endings after mild, quickly-repaired lows; Beguš:
  "uniformly positive stories with weak turning points" (S03/S43).
- **Observable characteristics.** Hedonometer-style arc (S08 method) that stays above
  the midline; lows are brief and immediately compensated.
- **Evidence.** S03 (High), S43 (Tian et al. 2024), S37, baseline S08 (human arcs are
  six-shaped with real falls). Confidence: **Medium-High**.
- **Likely cause.** K3 + K7: positivity preference and refusal training suppress
  sustained negative affect.
- **Variation.** Genre: horror/tragedy prompts only partially override the bias.
  Model: varies (Llama more emotionally expressive, S37).
- **Severity.** 3. **False-positive risk.** 2 — some genres are intentionally
  uplifting.
- **Effect on quality.** Weak stakes (the reader never believes the fall will stick);
  no catharsis; tonal sameness.
- **Recommended mitigation.** Level 4–5: deepen one turning point — let a loss land
  and *stay* for a scene, and let recovery be incomplete. Author-gated.
- **Side effects.** Gratuitous misery is not tragedy.
- **Validation.** Arc plot vs. genre baseline (frameworks/05).

## Monitored / folklore (not acted upon)

| Pattern | Status | Why |
|---|---|---|
| "Excessive symmetry" as a blanket diagnosis | Monitored | Subsumed by N03; needs a ledger, not vibes |
| Artificial foreshadowing | Folklore-adjacent | Moved to FS01; unmeasured |
| "The journey continues" endings | Monitored | Template phrase; low harm; fix = delete if cliché |
| Absence of subplots/digressions | Monitored | Subsumed by N01; subplot addition is structural and author-gated |
