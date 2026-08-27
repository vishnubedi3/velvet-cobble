# 09 — Evaluation Benchmark

**Purpose.** Measure whether the skill *works* — reduces real artifacts
without damaging fiction — and provide the corpus/extensions to validate
(and re-validate) taxonomy claims. Companion to `benchmark/README.md`.

**Design principles.** (1) Judge the intervention, not the prose style.
(2) Use objective metrics where possible (ledgers, distributions, counts);
use human/expert judgment where objectivity ends (craft, voice). (3) Measure
damage explicitly — the benchmark's headline is *preservation*, not edit
count. (4) Detector scores are excluded by policy (F-4). (5) Per S04/S46:
LLM-as-judge ratings of fiction are weakly correlated with expert judgment —
automated rubric scores are triaged, human spot-checks are mandatory for
release decisions.

## 1. Metrics

### Artifact-reduction metrics (did the cause disappear?)

| # | Metric | Method |
|---|---|---|
| A1 | **Redundancy removal rate** | fraction of U02/U04/E02/FS03 findings whose function test now passes (deletion verified by carrier audit, frameworks/05 §3) |
| A2 | **Repetition reduction** | near-duplicate cluster count before/after (frameworks/06 §3, L02/L03/L08) |
| A3 | **Diversity curves** | per-chapter lexical/syntactic diversity slope before/after (S20 method) — improvement ≠ uniform change; local spikes are fine |
| A4 | **Ledger consistency** | contradiction count before/after (L04/L05/L09/A02) |
| A5 | **Reader inference test** | for E01/U01/D03 fixes: independent reader-model (or human) must recover the intended emotion/meaning from the revised span alone |
| A6 | **Structure variance** | scene-type / beat-sequence entropy before/after (SC05/N05/L03); genre-gated |
| A7 | **Voice separation** | blind line-attribution accuracy: a reader (model/human) attributes dialogue/interiority to the correct character before/after (C03/D04/H03) |

### Preservation metrics (was anything damaged?)

| # | Metric | Method |
|---|---|---|
| P1 | **Plot/continuity preservation** | story-model diff: events, causal links, facts, timeline identical after edits (automatic) |
| P2 | **Information-state preservation** | reader-knows / character-knows ledgers identical (automatic) |
| P3 | **Voice preservation** | per-character voice-profile distance before/after below threshold (automatic + human check) |
| P4 | **Intent preservation** | declared devices/motifs/anchors untouched (automatic: spans protected) |
| P5 | **Expert craft judgment** | rubric (below) on before/after pairs, blind, by ≥2 writers/editors |

### Process metrics

| # | Metric | Method |
|---|---|---|
| M1 | **Adversarial suite** | all tests in `skill/08-adversarial-tests.md` pass |
| M2 | **Reversion rate** | edits reverted by post-checks (target: near zero on release cases) |
| M3 | **Edit budget** | median chars changed per 1k words, per level (sanity: Level 1–2 dominant; total < ~8% typical; no quota, but outliers reviewed) |
| M4 | **No-new-tell rate** | edited spans with new high-confidence findings (target: 0) |

## 2. Expert rubric (P5)

Blind before/after pairs rated −2…+2 per dimension by writers/editors:

1. **Plot & causality** — did the story stay the same story?
2. **Character integrity** — do characters still act/sound like themselves?
3. **Voice** — is the narrative voice intact?
4. **Texture & specificity** — did the prose gain or lose life?
5. **Subtext & implication** — did the reader's work change (for the better)?
6. **Genre fit** — does it still honor its contract?
7. **Overall** — is the after better fiction?

Pass: median ≥ 0 on every dimension and no dimension with a negative
expert majority. (This is the decisive gate; automated metrics are
necessary but never sufficient.)

## 3. Case suite

`benchmark/cases/` — constructed pairs spanning:
- **Tell-seeded cases:** drafts injected with known tells (redundant
  interpretation, uniform dialogue, template structure, repeated skeletons,
  ledger contradictions) → the skill must find and fix the *injected*
  artifacts and nothing else (ground-truth edit spans known).
- **Trap cases:** the adversarial traps (A-T1…A-T8) as full drafts.
- **Long-form cases:** 10k+ word drafts with planted drift/repetition/
  contradictions (ground truth via ledger).
- **Genre matrix cases:** one case per genre in the contract table
  (frameworks/07), each with a contractual element that must survive.
- **Human-control cases:** human-written drafts with deliberately
  "AI-looking" devices (balanced prose, closed endings) that must be
  preserved (false-positive measurement).
- **Paired generation cases:** same prompt, multiple generators/decoding
  settings → cross-model calibration cases (taxonomy/17).

## 4. Benchmark extension (taxonomy re-validation)

The taxonomy's Low/Folklore items can only be promoted through this path:
1. Collect a fiction corpus (generated + human, same prompts — the S02/S03
   dataset design).
2. Measure the candidate pattern (frequency distributions, not anecdotes).
3. Report effect sizes with the source-index style citation.
4. Promotion to `actionable` requires Medium confidence per
   `research/02-evidence-hierarchy.md` §2.2.

## 5. Reporting

A benchmark run reports: all metrics, per-case results, human spot-check
notes, and the list of taxonomy claims used (with confidence levels) so that
results stay auditable against the evidence base.
