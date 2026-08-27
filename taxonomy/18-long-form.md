# Taxonomy 18 — Long-Form Consistency Tells

**Sources for this cluster:** S20, S22, S31, S32, S33, S49.
**Dominant causes:** K6 (no persistent memory/state), K2 (no global plan), K1 (diversity decay).

> These tells emerge *with length* and differ in kind from short-form tells: they
> are failures of state, not of style. Detection therefore runs on the story
> model (`interventions/03-story-model.md`), not on prose heuristics.

---

## L01 — Character/voice drift

- **Definition.** Characters' voices, knowledge, and values shift across the
  text: a character sounds different in chapter 20 than chapter 2 without a
  story reason.
- **Observable characteristics.** Stylometric shift per character over chapters;
  persona-consistency failures measured in dialogue (S49: off-the-shelf LLMs
  drift, contradict earlier statements); S32's context-fragmentation finding.
- **Evidence.** S49 (Tier 1, direct), S32 (Tier 2), S33 (survey: character
  consistency = open problem). Confidence: **Medium-High**.
- **Likely cause.** K6: the character's voice profile exists only in the recent
  context window; it decays with distance.
- **Severity.** 2. **False-positive risk.** 1 — the flag is a *deviation from
  the character's own established baseline*, which is objective.
- **Effect on quality.** The reader's model of the character breaks.
- **Recommended mitigation.** Maintain voice profiles in the story model and
  re-anchor each chapter's generation on them (frameworks/06); Level 3 repairs
  drift against the profile.
- **Validation.** Per-character voice-distance over chapters (metric A7).

## L02 — Repeated descriptions & emotional beats

- **Definition.** The same description or emotional beat recurs nearly verbatim:
  the character's grief re-described identically every chapter; the setting
  re-introduced with the same sentences.
- **Observable characteristics.** Near-duplicate passage detection; LongGenBench:
  ~45% of long outputs show significant repetition (S31).
- **Evidence.** S31 (Tier 2, direct). Confidence: **High**.
- **Likely cause.** K6: without state, the generator re-derives the same
  description from the same local cues.
- **Severity.** 3. **False-positive risk.** 1 — near-verbatim recurrence is
  objectively measurable (and *intended* motif repetition is the exception —
  check the motif register, L10).
- **Effect on quality.** Padding, reader fatigue, wasted word count.
- **Recommended mitigation.** Level 2: cut repeats; Level 3: vary the one
  recurrence that earns repetition (the refrain that deepens).
- **Validation.** n-gram/embedding duplicate audit per chapter.

## L03 — Recycled scene skeletons

- **Definition.** Scene blueprints recur across the book (SC05 at book scale):
  the same beat order serving different content.
- **Observable characteristics.** Beat-sequence clustering across chapters;
  S31's repetition; S43's repeated plot elements.
- **Evidence.** S31 (Tier 2), S43 (Tier 0 secondary). Confidence: **Medium-High**.
- **Likely cause.** K6 + K2: the most recent scene skeleton is the most probable
  next skeleton.
- **Severity.** 3. **False-positive risk.** 1.
- **Effect on quality.** Mid-book predictability; chapters blur together.
- **Recommended mitigation.** Level 4: vary beat order per scene purpose, using
  the scene-type ledger (frameworks/06) to avoid adjacency repeats.
- **Validation.** Skeleton-cluster audit.

## L04 — Continuity contradictions

- **Definition.** Facts contradict across the text: names, ages, timelines,
  object states, who-knows-what.
- **Observable characteristics.** Fact-ledger violations; S31's consistency
  degradation across models.
- **Evidence.** S31 (Tier 2, direct). Confidence: **Medium-High**.
- **Likely cause.** K6: early facts fall out of attention (S22: mid-context
  information is worst-used).
- **Severity.** 2. **False-positive risk.** 1.
- **Effect on quality.** Trust collapse: one caught contradiction can break a
  reader's whole investment.
- **Recommended mitigation.** Level 1–2: repair against the story model's fact
  ledger (the correction is usually a word, not a rewrite).
- **Validation.** Automated fact-ledger diff + human spot check.

## L05 — Worldbuilding inconsistency

- **Definition.** World rules drift: magic costs change, geography shifts,
  institutions behave differently (L04's world-scale face).
- **Observable characteristics.** Rule-ledger violations; S31.
- **Evidence.** S31 (Tier 2). Confidence: **Medium**.
- **Likely cause.** K6: world rules aren't held in state.
- **Severity.** 2. **False-positive risk.** 1 — except deliberate soft-magic
  ambiguity; check the world contract (W02).
- **Effect on quality.** The world stops feeling real at the exact point it
  stops being consistent.
- **Recommended mitigation.** Level 1–2 repairs against the rule ledger.
- **Validation.** Rule-ledger diff.

## L06 — Increasing formulaic prose / diversity decay

- **Definition.** Lexical and syntactic diversity declines across the text; late
  chapters reuse early vocabulary and structures at higher rates.
- **Observable characteristics.** Type-token ratio / syntactic-diversity decay
  over chapters; S20 (recursive synthetic training decays diversity — the same
  mechanism operates within one long generation); S31.
- **Evidence.** S20 (Tier 2, direct mechanism), S31 (Tier 2). Confidence:
  **Medium**.
- **Likely cause.** K6 + K1: the generator re-samples its own output
  distribution, which narrows with length.
- **Severity.** 2. **False-positive risk.** 1.
- **Effect on quality.** The book gets blander as it goes — the opposite of
  narrative build.
- **Recommended mitigation.** Generation-level: per-chapter prompts with
  fresh voice anchors; revisionally, Level 1–2 specificity repairs (P01) in
  flagged chapters.
- **Validation.** Diversity curves over chapters (metric A3).

## L07 — Mid-story sag (lost in the middle)

- **Definition.** Middle chapters lose momentum, forget established stakes, and
  re-derive what was already known — the U-shaped attention curve made fiction.
- **Observable characteristics.** Event-density dip mid-text; repeated beats in
  the middle third; S22 (U-shaped recall, 15–25pp degradation mid-context).
- **Evidence.** S22 (Tier 2, direct). Confidence: **Medium-High**.
- **Likely cause.** K6: mid-context information is worst-attended (S22).
- **Severity.** 2. **False-positive risk.** 1.
- **Effect on quality.** The classic long-form failure (T06).
- **Recommended mitigation.** Structural: maintain an always-current story
  state summary (S32's coordinator pattern); Level 4: re-tension the middle from
  the event register.
- **Validation.** Event-density + stakes-recall plot (frameworks/06).

## L08 — Re-recapping established information

- **Definition.** The text re-explains what earlier chapters established:
  backstory re-delivered, relationships re-introduced, rules re-taught.
- **Observable characteristics.** Redundant exposition across chapters (L02's
  exposition face).
- **Evidence.** S31 (Tier 2), practitioner (S44). Confidence: **Medium**.
- **Likely cause.** K6 + K3: the generator doesn't know the reader knows; its
  default is to explain.
- **Severity.** 1. **False-positive risk.** 1.
- **Effect on quality.** Mid-book pacing drag; reader condescension.
- **Recommended mitigation.** Level 2: cut recaps; the story model's
  information register (`interventions/03-story-model.md`) tells you what the
  reader already knows.
- **Validation.** Information-state audit.

## L09 — Timeline drift

- **Definition.** Time becomes inconsistent: distances, durations, and dates
  contradict; days-of-week drift (S31 documents exactly this in diary tasks).
- **Observable characteristics.** Timeline-ledger violations; S31 (temperature/
  temporal consistency failures in long generation).
- **Evidence.** S31 (Tier 2, direct). Confidence: **Medium**.
- **Likely cause.** K6: temporal state isn't tracked.
- **Severity.** 2. **False-positive risk.** 1.
- **Effect on quality.** Continuity breaks (L04's temporal face).
- **Recommended mitigation.** Level 1–2 repairs against the timeline register.
- **Validation.** Timeline-ledger diff.

## L10 — Unintended motif repetition

- **Definition.** Images and phrases recur without design — the same metaphor
  appears six times in different contexts, reading as tic rather than motif.
- **Observable characteristics.** Recurrence without variation or escalation;
  distinct from *intended* motif (which varies and deepens).
- **Evidence.** S31 (Tier 2), practitioner (S44). Confidence: **Medium**.
- **Likely cause.** K6: the generator's probability mass re-lands on its own
  recent images.
- **Severity.** 1. **False-positive risk.** 1 — with the intent check: an
  intended motif is in the motif register.
- **Effect on quality.** Accidental motifs read as lazy echoes (the opposite
  of V04's over-coherence — same mechanism, opposite failure).
- **Recommended mitigation.** Level 2: cut unvaried recurrences; keep
  intentional ones and vary them.
- **Validation.** Motif-register check (intended vs. accidental).

## Monitored / folklore (not acted upon)

| Pattern | Status | Why |
|---|---|---|
| "Models lose coherence after N tokens" as a blanket claim | Monitored | True in distribution (S31) but N is model/setting-specific — measure per setup |
| Automatic full-book regeneration | Rejected | Contradicts minimal-intervention doctrine (see interventions/01) |
