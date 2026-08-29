# Benchmark — Case Suite & Harness

Companion to `../spec/09-evaluation-benchmark.md` (metrics A1–A7, P1–P5,
M1–M4). This directory holds the case suite; the harness is described here so
implementations can be compared apples-to-apples.

## Harness contract

1. **Inputs:** case draft + a **valid Samur `project_context`** (spec/03
   §1.1 — every case runs bound; unbound-input rejection itself is tested by
   A-T24) + `SkillInput` metadata (genre, intent fields,
   analysis options) + optional ground-truth spans (for seeded cases;
   for PST cases: the canon citation the seeded violation breaks).
2. **Run:** the skill end-to-end with the case's options.
3. **Compare:** compute metrics per the case's metric set; check the
   adversarial pass criteria (../tests/01-adversarial-suite.md).
4. **Human layer:** P5 rubric on before/after pairs (blind, ≥2 raters) —
   the **project-anchored rubric** (spec/09 §2): project dimensions gate
   the pass.
5. **Output:** per-case JSON + summary (see `../schemas` for report shapes).

## Case inventory

| Case | Type | What it tests |
|---|---|---|
| `pst-*` (one per PST) | **project case** | PST-01…PST-10 detection with canon citation + canon-sourced fix that introduces no new canon (spec/09 §3) |
| `project-trap-*` | **project trap** | canon-compliant spans that look like generic tells (distorted chronicle memory, repeated office names, language-map register difference, approached mystery, NS-01 texture) — zero mutations |
| `seeded-redundancy` | tell-seeded | U02/E02/FS03 detection + Level 2 deletion + carrier audit |
| `seeded-uniform-dialogue` | tell-seeded | D01/D04/D06 detection + Level 3 re-voicing + A7 voice separation |
| `seeded-template-structure` | tell-seeded | N04/R02 detection + Level 4 variance + causality audit |
| `seeded-ledger-breaks` | tell-seeded (long-form) | L04/L05/L09/A02 detection + Level 1–2 state corrections |
| `seeded-skeleton-recycle` | tell-seeded (long-form) | L03/SC05 + Level 4 beat reorder |
| `trap-*` (A-T1…A-T8) | adversarial | intentionality/contract preservation (zero edits) |
| `binding-trap-*` (A-T24…A-T31) | adversarial (project) | rejection/report-only/preservation under the binding; zero canon mutations, zero mystery resolutions |
| `genre-*` (fantasy, sf, mystery, thriller, horror, romance, literary, historical, comedy, drama, ya, short, novel) | genre matrix | contract survival (frameworks/07) |
| `human-control-*` | false-positive | deliberate devices preserved; findings → Observations |
| `calibration-*` | cross-model | per-generator baselines (taxonomy/17 §17.3) |
| `longform-*` | long-form | frameworks/06 ledgers + sag detection |

## Ground truth discipline

Seeded cases define exact planted spans + the minimal correct fix class
(level, not wording — the skill may fix differently as long as the function
is restored and nothing else changes). Scoring rewards: finding the plant,
fixing at ≤ the expected level, touching nothing outside the plant's causal
neighborhood. Penalties: missed plants, edits outside the neighborhood,
fixes that pass the tell check but fail preservation (P1–P4).

## Corpus for calibration

Implementers should build a small calibration corpus per generator used:
N≈20 short stories from the same prompt class, human + generated, to set
repetition/uniformity/explicitness thresholds (the S02/S03 dataset design,
scaled down). `calibration-*` cases exist to verify this procedure, not to
replace it.
