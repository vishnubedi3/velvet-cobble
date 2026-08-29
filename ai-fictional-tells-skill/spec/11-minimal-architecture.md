# 11 — Minimal Implementation Architecture

**Goal.** The smallest conformant implementation that passes the adversarial
suite (../tests/01-adversarial-suite.md) and delivers real value. Everything is expressible as two
prompt contracts + deterministic validators. No fine-tuning, no vector
store, no custom models.

## Components

1. **Two LLM prompt contracts** (per `../spec/02-api-interface.md` §3):
   - `C-02 tell-detect` (analysis), with the taxonomy index
     (`../taxonomy/README.md`), the causal model section (research/01 §1.3),
     frameworks 01–05 loaded as knowledge, and the AnalysisReport schema as
     the output contract.
   - `C-03 intervene-level-N` (a single merged prompt for Levels 1–3;
     Levels 4–6 gated behind a second, more heavily constrained variant),
     with interventions/01–03 loaded.
2. **Deterministic validators** (plain code, ~200 lines):
   - schema validation for findings/edits;
   - evidence check (finding must cite a quoted span + an objective pattern
     count, not an adjective);
   - preservation-check simulator (the 14 PV dimensions as a checklist run
     against the story model + diff);
   - ledger diffs for continuity (string-level: names, dates, objects —
     a minimal fact ledger extracted by `C-01`).
3. **The story model** (`../interventions/03-story-model.md`) — extracted by a
   simplified `C-01` prompt in the minimal build (characters, facts,
   timeline, information-state; voice profiles optional at this tier and
   marked `unknown` when absent; the **narrator voice baseline is required
   even here** — it is cheap (5–8 quoted signals) and the final read depends
   on it).
4. **Orchestrator** (script): stage order, level ordering, batch gate,
   revert logic, final read (Stage 4b) — the pipeline invariants I-1…I-6
   from `../spec/05-pipeline.md`.

## What the minimal build does

- Detects the high-confidence tell clusters (repetition, explicitness,
  continuity, uniformity) with Medium/High confidence only.
- Applies Levels 0–3 fixes; Levels 4+ require the advanced build's
  causality tooling (or author-visible proposals).
- Rejects anything unverifiable (unknown voice profiles → no re-voicing;
  `uncalibrated` → Level ≤3 cap).

## Explicit degradations (acceptable at this tier)

- Low-confidence tells and folklore are report-only (already the rule).
- Genre gate uses the static contract table (frameworks/07 §1) without
  corpus baselines.
- Voice separation (A7) is checked qualitatively, not metrically.
- Long-form ledger is fact-level only (no scene-skeleton clustering).

## Cost model

- Analysis: ~1 LLM call per ~3–5k words (chunked) + 1 aggregation call.
- Intervention: 1 call per queued finding (levels 1–3), batched where
  spans don't interact.
- Total for a 3k-word story: typically 2–5 calls. For a 60k-word draft:
  ~15–25 calls + validator passes.

## Minimum viable load

`../SKILL.md`, taxonomy index, research/01 §1.3, frameworks/01–05,
interventions/01–03, schemas. (≈ 40k tokens of reference material; trims
to ~15k if the taxonomy cluster files are loaded on demand per finding.)
