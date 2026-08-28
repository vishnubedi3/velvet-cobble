# Taxonomy 03 — Character-Level Tells

**Sources for this cluster:** S03, S04, S06, S07, S28, S29, S37, S42, S49.
**Dominant causes:** K2 (no decision-model behind characters), K3 (alignment), K4 (template characters), K6 (long-form drift).

---

## C01 — Explicit emotion labeling & explanation

- **Definition.** Characters' inner states are named and explained by the narrator or
  the character, rather than enacted through behavior, perception, and consequence.
- **Example pattern.** "She felt a pang of regret as she realized how much she had
  sacrificed" — three layers of explanation for one observable thing (what she does
  next is absent).
- **Observable characteristics.** Emotion-word + "as she realized/understood/felt"
  constructions; interiority that duplicates what behavior already shows; emotion
  vocabulary density above genre baseline.
- **Evidence.** S28 (themes/emotion stated outright; Tier 0), S37 (LIWC affective
  explicitness, Tier 1), S04 (emotional flexibility 19.4 vs 91.7). Confidence:
  **Medium-High**.
- **Likely cause.** K3 (explicitness preference) + K4 (training on fiction reviews and
  summaries that *name* the emotions the fiction enacts).
- **Variation.** Genre: strongest in romance/literary prompts; weakest in dialogue-led
  crime. Perspective: strongest in close third and first person (the most interior
  modes — and the most damaging place for it).
- **Severity.** 3. **False-positive risk.** 2 — interiority is a legitimate novelistic
  mode; the tell is the *redundant* layer, not interiority itself.
- **Effect on quality.** The reader is told what to feel instead of being given the
  cause; character interiority collapses into captioning.
- **Recommended mitigation.** Level 2–3: replace the explanation with the behavior,
  perception, or speech that would *produce* the emotion; keep one layer of interiority
  where the mode requires it (E01's mitigation is the same fix; both point at the
  redundancy, not the emotion).
- **Side effects.** Over-deletion of interiority yields behaviorist prose (the
  opposite failure); keep the layer that carries new information.
- **Validation.** For each remaining emotion label: what does the scene lose if it's
  removed? (If nothing — it was caption.)

## C02 — Instant backstory/motivation rationalization

- **Definition.** Every behavior is immediately retrofitted with a cause from the
  character's past; motivation is delivered at the moment of action, complete and
  clean.
- **Example pattern.** "She couldn't trust doctors — not since the night her father…"
  supplied at the exact moment a doctor appears.
- **Observable characteristics.** Backstory inserted adjacent to the behavior it
  explains; characters who narrate their own causes; S04: character development scored
  16.7 vs 61.1 by expert writers (weakness includes shallow, functional motivation).
- **Evidence.** S04 (Tier 0), practitioner consensus (S44, S53). Confidence: **Medium**.
- **Likely cause.** K4 (template characters carry template causes) + K3 (explain
  everything).
- **Variation.** Genre: strongest in drama/literary; less in picaresque/action.
  Length: the *same* backstory recurs (→ L02).
- **Severity.** 2. **False-positive risk.** 2 — motivated characters are good craft;
  the tell is motivation *on demand*.
- **Effect on quality.** Characters become case files; mystery (why does she do this?)
  is spent before it earns interest.
- **Recommended mitigation.** Level 2–3: withhold the explanation; let behavior
  precede cause; let the reader ask "why" for a while. If the cause must appear, let
  it arrive late or partially.
- **Side effects.** Unexplained behavior reads as incoherence unless the behavior is
  vivid enough to carry the question.
- **Validation.** Re-read for the moment the reader stops asking "why."

## C03 — Uniform articulate interiority

- **Definition.** All characters — child and elder, thug and professor — think and
  speak with the same articulate, self-aware interior voice; introspection is the
  default mode for every POV.
- **Example pattern.** A dockworker's interior monologue with the syntax and
  abstraction of an essayist; every character knows precisely why they act.
- **Observable characteristics.** Stylometric clustering by *model* rather than by
  character (S02); TTCW perspective/voice flexibility 16.7 vs 72.2 (S04); CAspER
  "coherent, whole, transparent" characters (S29).
- **Evidence.** S02, S04, S29 (Tier 0). Confidence: **Medium-High**.
- **Likely cause.** K1 + K2: one generator, one distribution — no per-character
  language model is actually maintained; "character voice" is generated as content,
  not as constraint.
- **Variation.** Genre: strongest in romance (S29); weakest in ensemble comedy where
  templates force differentiation. Model: varies (S29: Phi > Llama diversity).
- **Severity.** 3. **False-positive risk.** 2.
- **Effect on quality.** Characters collapse into one narrator with name tags; the
  story loses its most powerful differentiator.
- **Recommended mitigation.** Level 3: re-voice dialogue/interiority per character
  from the character's knowledge, priorities, vocabulary, and syntax (frameworks/02
  voice profile). Level 4: differentiate the *thought content* characters can have.
- **Side effects.** Dialect cosplay and tic-spam are worse than uniformity; voice must
  come from cognition, not catchphrases.
- **Validation.** Blind line-attribution test: can a reader say who is thinking
  without name tags? (benchmark metric A7.)

## C04 — Measured, proportionate, rational reactions

- **Definition.** Characters respond to events with calibrated, emotionally literate,
  proportionate reactions — the *right* amount of feeling, expressed constructively.
- **Example pattern.** A bereaved parent processes the loss in three healthy stages
  and articulates them; no one overreacts, underreacts, or reacts *wrongly*.
- **Observable characteristics.** Absence of disproportion; reactions align with
  therapist-model norms; reduced anger/sadness language (S37).
- **Evidence.** S37 (negative affect reduction, Tier 1), S03 (uniform positivity),
  S04 (emotional flexibility). Confidence: **Medium**.
- **Likely cause.** K3 + K7: aligned models are trained toward constructive,
  non-extreme responses; fiction inherits the stance.
- **Variation.** Genre: strongest in domestic/literary; weakest in noir/horror.
- **Severity.** 2. **False-positive risk.** 3 — "measured" is also a legitimate
  characterization choice; only flag *uniform* measuredness across unlike characters.
- **Effect on quality.** Human drama is mostly disproportionate reaction; removing it
  removes conflict, comedy, and tragedy.
- **Recommended mitigation.** Level 3: for one beat, let a character react *wrongly*
  (too much, too little, too late) per their profile — a deliberate, authored choice.
- **Side effects.** Random disproportionality reads as error; it must be motivated by
  character, not inserted for texture.
- **Validation.** Author + expert read; check reaction against the character's
  profile, not against a norm.

## C05 — Polite/constructive conflict between characters

- **Definition.** Disagreements proceed as respectful negotiation: parties state
  positions, acknowledge feelings, seek compromise — conflict without rupture.
- **Example pattern.** A marriage-ending fight that reads like a mediation session;
  every conflict ends with mutual understanding.
- **Observable characteristics.** Hedged opposition ("I hear you, but…"), prompt
  de-escalation, no lasting wounds; dialogue politeness (D06 is the dialogue-side twin).
- **Evidence.** S37 (Tier 1), K3 mechanism; practitioner-strong (S44). Confidence:
  **Medium**.
- **Likely cause.** K3 + K7: helpfulness and safety training make cooperative speech
  the default register.
- **Variation.** Genre: strongest in romance/drama; weakest in crime/noir.
- **Severity.** 2. **False-positive risk.** 2.
- **Effect on quality.** Stakes evaporate; conflict becomes procedure; relationships
  lose friction, which is what fiction lives on.
- **Recommended mitigation.** Level 3–4: let one confrontation break cooperative
  norms — interruption, refusal to engage, wrong response — per character profiles.
- **Side effects.** Forced hostility is as artificial as forced politeness.
- **Validation.** Read the scene for whether either character could walk away hurt.

## C06 — Hyper-consistent characterization; no contradiction

- **Definition.** Characters never act against their stated traits, values, or
  interests; internal contradiction — the normal human condition — is absent.
- **Example pattern.** The honest character is never tempted; the coward is never
  brave; values form a closed system.
- **Observable characteristics.** Trait-behavior entailment with zero violations;
  CAspER: characters "coherent, whole" (S29). (Long-form flips this into drift — L01 —
  which is the *other* failure of the same missing model.)
- **Evidence.** S29 (Tier 0), K2 mechanism. Confidence: **Medium**.
- **Likely cause.** K2: characters are trait-lists, not decision-procedures; the
  generator maximizes trait-consistency, which humans only *aspire* to.
- **Variation.** Genre: strongest in SFF (trait-driven archetypes); weakest in
  literary.
- **Severity.** 2. **False-positive risk.** 3 — consistent characterization is
  *required* craft; the tell is consistency with nothing else (no ambivalence, no
  temptation, no compromise).
- **Effect on quality.** Characters lack interior conflict, which is the engine of
  most fiction.
- **Recommended mitigation.** Level 4: add one trait-vs-trait collision point (duty
  vs. loyalty) from the story model's goal structure; never break traits for shock.
- **Side effects.** Contradiction without structure = characterization error.
- **Validation.** Expert read: does the contradiction feel like a *decision*?

## C07 — Stereotypical demographic rendering

- **Definition.** Characters from marked demographic groups are drawn from
  stereotype distributions: appearance-focused women, family-associated women, exoticized
  minorities — at rates measurably above human baselines.
- **Example pattern.** Gender-swapped prompts shifting story topics and power verbs
  (S06); "almond-shaped eyes" persona descriptions (S07); appearance-word density for
  female protagonists (S42).
- **Observable characteristics.** Topic/appearance/power word distributions by
  perceived character gender (S06 method); markedness asymmetries (S07 method).
- **Evidence.** S06, S07, S42 (all Tier 0/1). Confidence: **High**.
- **Likely cause.** K4: pretraining distributions encode cultural stereotypes;
  fiction templates amplify them (Lucy & Bamman's "male=career/female=family" at 38%).
- **Variation.** Model: reduced in newer/aligned models but not eliminated (S03 notes
  progressive shift in newer models; S42 finds biases persist in current generations).
  Genre: all.
- **Severity.** 3. **False-positive risk.** 1 (under-detection is the bigger risk;
  stereotypes hide in "positive" framing, S07).
- **Effect on quality.** Besides the representational harm: characters become
  demographic exemplars instead of individuals; stories become interchangeable.
- **Recommended mitigation.** Level 3–5: re-derive the character from an individual
  life (specific job, habit, history, priorities) rather than a demographic template;
  audit marked-vs-unmarked descriptions (S07 method) before publication.
- **Side effects.** Diversity-by-checklist is a new stereotype; the fix is
  individuation, not trait-swapping.
- **Validation.** Marked-persona comparison (S07) + expert/sensitivity read.

## C08 — Transparent, theme-vehicle characters

- **Definition.** Characters exist to instantiate positions in the story's argument;
  their traits are legible as "the skeptic," "the believer," and each exists to
  demonstrate the theme (twin of N01 at character scale).
- **Example pattern.** Each secondary character arrives carrying exactly the lesson
  the protagonist needs, then recedes.
- **Observable characteristics.** CAspER: domestic-story characters "represent
  abstract themes"; character function ≈ theme function (S29); S04 character
  development 16.7.
- **Evidence.** S29 (Tier 0), S04. Confidence: **Medium**.
- **Likely cause.** K4 + K2: characters are generated as narrative functions first.
- **Variation.** Genre: strongest in domestic/literary/coming-of-age; weakest in
  farce.
- **Severity.** 2. **False-positive risk.** 2.
- **Effect on quality.** The cast reads as an argument diagram.
- **Recommended mitigation.** Level 4: give one theme-vehicle character a
  non-thematic interest that occasionally derails the scene (see N01).
- **Side effects.** Unintegrated interests read as noise.
- **Validation.** Function audit: can the character be described without naming
  their thematic role?

## Monitored / folklore (not acted upon)

| Pattern | Status | Why |
|---|---|---|
| Trauma résumé / backstory-as-credential | Monitored | Plausible (K4) but unmeasured; fix via C02 |
| Quirk-as-depth (surface tics) | Monitored | Practitioner-common; overlaps C03 |
| Flat secondary characters | Monitored | Subsumed by C08/C03 |
| Artificial vulnerability | Monitored | Subsumed by C01/C02 |
| "Character drift" | (documented) | See L01 — it is the long-form twin |
