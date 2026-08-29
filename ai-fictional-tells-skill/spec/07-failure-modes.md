# 07 — Failure Modes

**The central researched failure mode:** anti-AI rewriting itself becoming
recognizable as AI-generated — aggressive paraphrasing, synonym replacement,
randomization, deliberate imperfections, sentence shuffling, or
detector-oriented optimization introducing new artifacts. Each failure mode
below names the evidence and the skill's countermeasure.

## F-1 — Deliberate imperfection ("humanize by dirtying")

- **What.** Inserting errors, typos, informal drift, or "burstiness" to look
  human.
- **Evidence against.** Human variation is structured (register, affect,
  specificity — S02, S37, S41), not noise; error-insertion is a documented
  humanizer behavior that distorts text (S34) and introduces a *new*
  detectable pattern (S35: adversarial rewriting backfires on 4.15% of
  samples). S01: humans do make more errors — but that is a population
  statistic, not a license to simulate them.
- **Countermeasure.** Hard exclusion (`../interventions/02-preservation-constraints.md` §7). Quality
  variance comes from specificity, register contrast, and implication —
  never from injected noise.

## F-2 — Synonym substitution / thesaurus paraphrasing

- **What.** Swapping words to "break the pattern."
- **Evidence against.** Paraphrase-to-evade costs quality by construction
  (S12, S13, S30: obfuscation literature treats quality loss as the explicit
  cost); synonym swaps don't touch any tell's *cause* (K-codes) — they
  relocate the pattern.
- **Countermeasure.** There is no synonym-replacement intervention level.
  Lexical changes must be specificity repairs sourced from story-model facts
  (P01/S03), with the function test passed. The variation audit
  (frameworks/01 §2 Pass B) additionally detects the *generator-side* form —
  referent cycling — whose only correct fix is restoring the repeated
  referent (FR-6: the right word repeated is correct), never adding
  variation.

## F-3 — Sentence shuffling / randomization

- **What.** Reordering sentences or structures for variance.
- **Evidence against.** Structure is meaning (causality, information flow,
  emphasis); shuffling breaks PV-1/PV-7/PV-10 by construction. Human
  variance is *functional* variance (S02: dispersion comes from different
  choices, not scrambled ones).
- **Countermeasure.** All structural changes run the causality audit
  (frameworks/05 §4); randomization is hard-excluded.

## F-4 — Detector-oriented optimization

- **What.** Editing toward a detector's score (either direction).
- **Evidence against.** Detectors are unreliable and gameable (S14), biased
  (Liang et al. 2023; S14's false-positive rates), and their evasion is a
  different problem from literary quality (S12, S13, S35, S36: the
  evasion/quality/cost trade-off is fundamental).
- **Countermeasure.** Detector scores are never an input
  (`../spec/06-scoring.md` §6). The skill's objective is explicit in SKILL.md
  §1.

## F-5 — The "anti-tell tell" (fixing one tell by installing another)

- **What.** P04 fixed by chopping rhythm into fragments; E01 fixed by
  behaviorist opacity; V03 fixed by manufactured quirk; D04 fixed by tic-spam
  dialects; N02/U05 fixed by upgrading the closing aphorism into a subtler
  one (kicker rule, frameworks/05 §3).
- **Evidence.** Each is a *new* template pattern — the same K1/K4 mechanism
  producing a mirrored artifact (no direct measurement; mechanism-level +
  practitioner observation, S44).
- **Countermeasure.** The new-artifact rule (`../interventions/02-preservation-constraints.md` §2):
  every edit re-runs the tell detectors on the changed span; any new
  high-confidence finding → revert.

## F-6 — Death by a thousand fixes (over-editing)

- **What.** Applying every possible fix, flattening the text into a
  checklist-approved surface.
- **Evidence.** Craft-level + the skill's own logic: over-editing removes
  the variance the fixes exist to restore; it also violates the
  minimal-intervention doctrine.
- **Countermeasure.** Cause clustering (`../spec/06-scoring.md` §3), Level 0
  default, the churn rule, and the idempotence invariant (I-6).

## F-7 — Preservation failure (the fix damages the fiction)

- **What.** The classic false positive: a deliberate device "fixed" (an
  authorial motif deleted as L10, a contracted cliffhanger removed as T03, a
  therapeutic register de-explicated as D03).
- **Evidence.** Label-driven judgment inversion (S26) shows how easily
  features get misread; S28 shows readers can't reliably distinguish anyway —
  so damage here is pure loss.
- **Countermeasure.** The genre gate (frameworks/07), the intentionality
  check (interventions/02 §3), the 14-dimension gate, automatic revert.

## F-8 — Calibration drift / model blindness

- **What.** Thresholds calibrated on generator A applied to generator B;
  long-form framework skipped on a 9k-word draft; genre contract missing.
- **Evidence.** Cross-model/decoding differences are measured (S23, S31,
  S37, S29).
- **Countermeasure.** Calibration metadata on every finding; `uncalibrated`
  caps at Level 3; long-form threshold parameterized; genre declared or
  provisional.

## F-9 — Provenance misuse

- **What.** The skill's output used to disguise machine authorship where
  disclosure is required (venue policy, author commitments).
- **Evidence.** Disclosure norms measurably matter (S50: authors don't feel
  ownership of AI text; S51: disclosure affects perception; S44: venues ban
  undisclosed AI).
- **Countermeasure.** The skill is a craft tool with a provenance field and
  an explicit non-deception clause (SKILL.md §1 rule 8); reports carry the
  assistance scope and never remove required disclosures. The skill does not
  police misuse, but it does not enable it silently: reports are structured
  so provenance decisions remain visible.

## F-10 — "Humanness theater" (optimizing perceived humanness)

- **What.** Editing to look human *per se* — the unstated attractor behind
  F-1…F-4.
- **Evidence against.** Humans cannot reliably distinguish AI fiction (S28),
  conversation (S15), or poetry (S27); attribution labels dominate judgment
  (S26); so "humanness" is partly a labeling artifact and optimizing for it
  is optimizing for noise.
- **Countermeasure.** The objective is literary quality (SKILL.md §1); the
  benchmark's metrics (../spec/09-evaluation-benchmark.md) measure function, not indistinguishability.
