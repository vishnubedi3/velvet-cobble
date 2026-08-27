# Taxonomy 04 — Dialogue-Level Tells

**Sources for this cluster:** S02, S04, S28, S29, S37, S38, S39, S44, S49.
**Dominant causes:** K1 (one distribution, one voice), K3 (cooperative/helpful speech), K4 (explained fiction in training), K2 (no per-speaker model).

---

## D01 — Symmetric turn-taking

- **Definition.** Conversations proceed as clean ping-pong: each utterance gets a
  complete, on-topic, appropriately sized response; no overlaps, lulls, or derailments.
- **Example pattern.** Every question answered; every statement acknowledged; the
  exchange length-ratio stays near 1:1 for pages.
- **Observable characteristics.** Turn-length variance near zero; no interruptions;
  no topic drift; no one leaves a question hanging.
- **Evidence.** Practitioner-strong (S44); mechanism: K1/K3; S38 (models' dialogue
  pragmatics are cooperative-by-default). Confidence: **Medium**.
- **Likely cause.** K3: the model was trained to be a cooperative interlocutor; it
  imports conversational norms for *assistants* into *characters*.
- **Variation.** Genre: strongest in drama/romance; weaker in farce (templates force
  zingers). Perspective: dialogue is dialogue.
- **Severity.** 2. **False-positive risk.** 2 — some styles (Sorkin-esque) are
  symmetric by design; the tell is symmetry *everywhere, regardless of characters*.
- **Effect on quality.** Conversational rhythm is characterization; uniformity erases
  power dynamics, status, urgency, and intimacy.
- **Recommended mitigation.** Level 3: vary turn shape per character and situation —
  allow one unanswered question, one interruption, one non-sequitur, one silence —
  chosen from character profiles (frameworks/03).
- **Side effects.** Random disruption reads as error; disruption must encode
  something (power, evasion, distraction).
- **Validation.** Read the scene for what the *rhythm* says about the relationship.

## D02 — As-you-know exposition

- **Definition.** Characters state information both already know, for the reader's
  benefit — dialogue as delivery mechanism for world/backstory.
- **Example pattern.** "As you know, brother, the Meridian Treaty forbids passage
  after the third moon."
- **Observable characteristics.** Information-with-no-information-function
  utterances; recaps of shared history; "As you know," "Remember when…".
- **Evidence.** Practitioner-strong (S44); mechanism K3/K4; consistent with S28's
  explicitness finding. Confidence: **Medium-High**.
- **Likely cause.** K3 (be informative and clear) + K4 (stories summarized into
  dialogue-shaped info-dumps in training).
- **Variation.** Genre: strongest in SFF (world-heavy) and thriller (backstory-heavy);
  weakest in literary dialogue.
- **Severity.** 3. **False-positive risk.** 2 — exposition through dialogue is a
  legitimate device; the tell is the *as-you-know* frame and the information's
  redundancy.
- **Effect on quality.** The most instantly recognizable dialogue tell; destroys
  verisimilitude and wastes the scene's dramatic energy.
- **Recommended mitigation.** Level 3: convert the information into (a) conflict —
  the speakers *disagree* about the fact; (b) one character's discovery; or (c) an
  oblique reference that lets the reader infer. Or Level 2: cut it if the reader
  already has it.
- **Side effects.** Cutting necessary information starves the reader; conversion to
  conflict can inflate drama.
- **Validation.** Information-audit: is this fact needed by *this* reader at *this*
  moment, and could either speaker omit it without lying?

## D03 — Over-explicit emotional speech

- **Definition.** Characters announce their internal states with precision and
  completeness ("I feel hurt because you didn't come").
- **Example pattern.** Therapy-grade self-report in casual conversation; emotions
  named with their causes attached; no deflection, minimization, or indirection.
- **Observable characteristics.** "I feel X because Y" density; zero reliance on
  implication; S28 (AI stories state what human characters would imply).
- **Evidence.** S28 (Tier 0), S37 (affective explicitness), S38 (models can *parse*
  implicature but default to explicitness in production). Confidence: **Medium-High**.
- **Likely cause.** K3: clarity preference — implicit emotion risks being "unhelpful."
- **Variation.** Genre: strongest in romance/drama; weakest in noir/subtext genres.
- **Severity.** 2. **False-positive risk.** 2 — some characters *are* emotionally
  articulate; that is itself a characterization choice worth preserving.
- **Effect on quality.** Subtext loss; every scene becomes a feelings check-in.
- **Recommended mitigation.** Level 3: keep the emotion, remove the *completeness* —
  let the character say the wrong thing, deflect, understate, or act (see U01, E01).
  Preserve articulate speakers if their articulacy is characterized.
- **Side effects.** Opaque dialogue that loses the beat entirely.
- **Validation.** Reader test: can the reader name the emotion from what's said and
  done (benchmark metric A5)?

## D04 — Uniform idiolect across characters

- **Definition.** All characters share one vocabulary, syntax, and wit level — the
  generator's, not theirs.
- **Example pattern.** A seven-year-old and a judge with identical clause structure
  and lexicon; every character is equally good at banter.
- **Observable characteristics.** No between-character stylometric separation (S02:
  text clusters by model, not by speaker); TTCW voice flexibility 16.7 (S04); CAspER
  transparency (S29).
- **Evidence.** S02, S04, S29 (Tier 0). Confidence: **Medium-High**.
- **Likely cause.** K1 + K2: character voice is generated as content, not maintained
  as a constraint; nothing in autoregression enforces per-speaker distributions.
- **Variation.** Genre: romance highest (S29), ensemble comedy lowest. Model:
  differs (S29).
- **Severity.** 3. **False-positive risk.** 2.
- **Effect on quality.** The cast reads as one mouth; relationships lose texture;
  humor dies (everyone is equally funny — H03).
- **Recommended mitigation.** Level 3: per-character voice profiles from the story
  model (vocabulary, syntax length, hedging, priorities, knowledge, verbal habits —
  frameworks/02 §Voice profile); re-voice only utterances that violate their speaker.
- **Side effects.** Tic-spam; dialect caricature; "quirky" overreach.
- **Validation.** Blind attribution test (metric A7).

## D05 — Over-complete grammatical utterances

- **Definition.** Dialogue in full, well-formed sentences; no fragments, false
  starts, repairs, or ellipsis even where speech would naturally elide.
- **Example pattern.** "I am going to the store. Do you need anything?" — where
  speech would be "Store. Need anything?"
- **Observable characteristics.** Sentence-completeness rate near 100%; Cai et al.:
  models disfavor shorter words for less informative content (S39); Herbold: highest
  language-mastery scores (S01).
- **Evidence.** S39 (Tier 1, psycholinguistic), S01 (Tier 1). Confidence: **Medium**.
- **Likely cause.** K1: complete, grammatical sentences are the most probable
  continuations; K3: clarity.
- **Variation.** Genre: strongest in literary/SFF; weaker in hard-boiled (template
  fragments). Model: varies.
- **Severity.** 2. **False-positive risk.** 3 — many human writers write "clean"
  dialogue; only flag when *all* speakers are complete-sentence speakers.
- **Effect on quality.** Dialogue sounds recited, not spoken; intimacy and status
  cues vanish.
- **Recommended mitigation.** Level 3: per speaker, allow ellipsis and fragments
  where speech economics demand; keep formality for formal characters.
- **Side effects.** Over-chopping produces telegraphic robot-speak (a known
  humanizer failure — see `skill/07-failure-modes.md`).
- **Validation.** Read aloud test.

## D06 — Hedged politeness / cooperative conflict

- **Definition.** Conflict dialogue in which both sides remain respectful, validate
  each other, and converge on understanding (the dialogue-side twin of C05).
- **Example pattern.** "I understand why you did it, and I'm not saying you're wrong,
  but it hurt me." / "I hear you. Can we find a way forward?"
- **Observable characteristics.** Hedge density in confrontations; prompt
  acknowledgment of the other's position; conflict that self-resolves.
- **Evidence.** S37 (cooperative/positive register, Tier 1), K3 mechanism;
  practitioner-strong (S44). Confidence: **Medium**.
- **Likely cause.** K3 + K7: politeness and de-escalation are aligned behaviors.
- **Variation.** Genre: romance/drama strongest; noir weakest (and most tell-like
  there).
- **Severity.** 2. **False-positive risk.** 2.
- **Effect on quality.** Confrontations without rupture are not confrontations.
- **Recommended mitigation.** Level 3: let one speaker refuse the cooperative frame —
  interrupt, mock, stonewall, change the subject — per their profile and the stakes.
- **Side effects.** Forced hostility (see C05).
- **Validation.** Stakes check: did either character risk something in this scene?

## D07 — Explanatory dialogue tags & beats

- **Definition.** Speech attributions and interjected beats that interpret the line
  ("she said softly, her voice laced with regret") rather than leaving the line to do
  the work.
- **Example pattern.** Every line of dialogue accompanied by an emotional gloss; the
  tag restates the line's content.
- **Observable characteristics.** Tag-plus-explanation density; "laced with, tinged
  with, edged with" constructions; beats that decode rather than block.
- **Evidence.** Practitioner (S44); mechanism K3/K4 (interpreted fiction); consistent
  with S28. Confidence: **Medium**.
- **Likely cause.** K4: training data includes annotated/interpreted dialogue;
  K3 prefers the meaning attached.
- **Variation.** Genre: romance/literary strongest; thriller weakest.
- **Severity.** 1. **False-positive risk.** 2.
- **Effect on quality.** Tags fight the lines; rhythm dies; subtext is overwritten.
- **Recommended mitigation.** Level 1–2: delete tags that restate the line; replace
  interpretive beats with physical business only where the scene needs blocking.
- **Side effects.** Dialogue without any beats can float unanchored.
- **Validation.** Read without tags: do the lines still land?

## Monitored / folklore (not acted upon)

| Pattern | Status | Why |
|---|---|---|
| No interruptions ever | Monitored | Subsumed by D01; fix via rhythm variation |
| Symmetric wit (everyone banter-witty) | Monitored | Subsumed by D04/H03 |
| Questions always answered | Monitored | Subsumed by D01 |
| "Said" purism (AI overuses fancy tags) | Folklore | Unmeasured; fancy tags are corpus-dependent, not AI-dependent |
