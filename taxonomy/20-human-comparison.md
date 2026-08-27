# Taxonomy 20 — Human Literary Writing Comparison Framework

**Purpose.** The skill must not define "human writing" as bad grammar, randomness,
or imperfection. This file defines the *actual* empirical distinctions between
natural literary variation and model-generated regularity, and the eight
contrasts the skill uses to separate deliberate literary choices from synthetic
repetition. It is the normative backbone for the preservation constraints
(`interventions/02-preservation-constraints.md`).

## 20.1 What the evidence says human fiction actually is

- **Heterogeneous, not messy.** Human texts disperse across stylometric space;
  LLM texts cluster tightly by model (S02). Human variation is *structured*
  diversity (author, era, register, genre), not noise.
- **Register-varied.** Humans shift register across modes (narration vs.
  dialogue vs. thought) and across texts; ChatGPT shows very limited register
  variation (S41).
- **Affectively complete.** Human fiction contains anger, sadness, and sustained
  negative arcs in proportion to its genre (S37); its emotional arcs span six
  shapes, half of them net-negative (S08).
- **Specific and local.** Human stories are anchored in local, cultural,
  concrete specificity; LLM stories are "bereft of local and cultural
  specificity" (S03).
- **Interpretively open.** Human fiction leaves work for the reader: subtext,
  ambiguity, unresolved meaning (S04's subtext dimension; S29's closure finding
  vs. human variability).
- **Risk-taking at the level of choice.** Human prose takes lexical and
  structural risks that no distribution center would choose (S10's surprisal
  gap, S11's distribution gap). The difference is *choice under uncertainty*,
  not error.

**Consequence.** The skill's quality objective is variance-with-function:
*specificity* (P01, W05), *register contrast* (V06, P07), *affective range*
(E05), *interpretive space* (U01–U05, V05), and *deliberate structural
deviation* (N01–N04) — never inserted error.

## 20.2 The eight contrasts (with false-positive warnings)

These contrasts are applied **case-by-case, with intent verification**, never as
style rules.

### 1. Good writing vs. AI-like writing
- Good writing: choices that carry information (specificity, rhythm, omission).
- AI-like: choices that carry no information (modal-average phrasing, decorative
  imagery, interpretive gloss).
- Test: *what does this choice add that its alternatives would not?* If the
  answer is "nothing," it's decoration; if "the story's facts/voice/rhythm,"
  it's writing.
- False positive: minimalist styles add little *lexically* but much
  *rhythmically* — judge at the level the style works at.

### 2. Deliberate literary convention vs. synthetic repetition
- Convention: a device used *for this story's reasons* (a chorus, a repeated
  image that deepens, a genre-required beat).
- Synthetic repetition: the same device appearing because it's the most probable
  next thing (S31's 45%, S05's 25 jokes).
- Test: *does the repetition vary, and does it accrue?* Intended repetition
  escalates or transforms; synthetic repetition is identical each time.
- False positive: minimalism and oral-style fiction repeat by design — check
  the variation *within* the repetition.

### 3. Clear prose vs. over-explanation
- Clear prose: the reader can infer everything intended from what's given.
- Over-explanation: the text supplies the inference itself (U02, U04, E02,
  S28's themes-stated-outright).
- Test: *delete the explanatory layer — does the clarity survive?* If yes, it
  was over-explanation.
- False positive: some readers *need* the layer; accessibility is an authorial
  goal. Intent check (PV-13) decides.

### 4. Strong structure vs. mechanical structure
- Strong structure: the skeleton is load-bearing but not visible; beats arrive
  causally, not by formula (N01's contrast).
- Mechanical structure: the skeleton shows (three-act ladder, milestone
  checklist, setup/payoff ledger on schedule).
- Test: *can each beat be predicted from the template alone?* If yes — and the
  genre doesn't require it — the structure is mechanical.
- False positive: genre contracts (mystery's ledger, romance's ladder) — the
  genre gate (frameworks/07) exempts contractual beats.

### 5. Rich description vs. decorative description
- Rich: description that is *perceived* — filtered through a character's
  attention, carrying need and history (S06's fix direction).
- Decorative: description that is *narrated* — inventory, atmosphere, and
  camera pans with no perceiver (S01–S05).
- Test: *whose perception is this, and why now?* No answer = decoration.
- False positive: omniscient and essayistic fiction legitimately describes
  without a perceiver — the work's own narration contract decides.

### 6. Emotional clarity vs. emotional overstatement
- Clarity: the reader knows what the character feels because the causes are
  specific and enacted.
- Overstatement: the text asserts intensity it hasn't earned (E01, E03) —
  "manufactured intensity."
- Test: *is the intensity earned by the scene's specificity, or asserted by its
  vocabulary?* Earned = keep; asserted = strip to the earned level.
- False positive: high-intensity genres (melodrama, epic) — genre gate.

### 7. Coherence vs. excessive neatness
- Coherence: every element is *consistent with* the story's logic.
- Neatness: every element is *explained by* the story's logic (N03, N06, U05,
  W02 — the ledger balanced to zero).
- Test: *is there anything in the story that isn't accounted for?* Human
  fiction tolerates — needs — some unaccounted surplus; the tell is the
  perfectly closed account.
- False positive: puzzle fiction legitimately closes the account — genre gate.

### 8. Stylistic consistency vs. stylistic uniformity
- Consistency: one *voice* — recognizable across the work, varying with
  register and content (a single author's range).
- Uniformity: one *distribution* — the same surface everywhere, no range
  (S02's tight clusters, S41's register monotony).
- Test: *does the voice modulate with its material?* A consistent voice
  modulates; a uniform one cannot.
- False positive: deliberately flat styles (Carver, Ishiguro) — the
  modulation is subtle, not absent. Judge at the work's own grain.

## 20.3 Operationalizing the contrasts

The detection frameworks use these tests as **verification gates**, not as
sentence-level style checks:

1. A tell flag (taxonomy) proposes a *candidate* problem.
2. The relevant contrast asks *whether the passage is doing deliberate work*.
3. The intentionality check (`interventions/02-preservation-constraints.md`
   §Intentionality) consults author intent + story model.
4. Only passages failing both are intervention candidates — and the
   intervention is the minimal one that restores the function (information,
   specificity, implication, variance), never the maximal one that "fixes
   style."

## 20.4 What this framework deliberately rejects

- "Human writing = errorful writing" (contradicted by S01: human essays are
  *less* polished but structurally freer; the freedom is the feature, not the
  error).
- "Add imperfection for realism" (a new artifact; see
  `skill/07-failure-modes.md` §F-1).
- "Randomize for burstiness" (rejected: detector-oriented optimization; S12–S14,
  S35).
- "Optimize toward reader-side indistinguishability" (S15, S26, S28: readers
  can't tell anyway, and labels drive judgment — the objective is literary
  quality, not deception).
