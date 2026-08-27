# 02 — API-Agnostic Interface

**Goal.** The skill must run against any generator and any analyzer model,
with no vendor-specific assumptions. This file defines the *shape* of the
skill as pure functions over data; `skill/11`/`12` map the shapes onto
minimal/advanced implementations.

## 1. Design stance

The skill is a **data-transform pipeline**, not a specific model prompt. Every
step is a function with JSON in / JSON out. Where a step needs a language
model (analysis heuristics, re-voicing, reconstruction), the step is
expressed as a **prompt contract**: inputs, knowledge load, instructions,
and a JSON output schema — implementable by any capable LLM through any
hosting API. No step depends on a vendor feature (no tool-calling
requirements; tool calls are an optimization, not a dependency).

## 2. Functional interface

```
skill =
  { analyze:      AnalyzeInput  -> AnalysisReport
  , prioritize:   AnalysisReport -> InterventionQueue
  , intervene:    InterventionQueue x StoryModel x Draft -> InterventionLog x Draft'
  , reevaluate:   InterventionLog x Draft' -> RejectedReverts x AnalysisReport'
  , report:       all-of-the-above -> SkillReport
  }
```

All five functions are **pure** (same inputs → same outputs). State is passed
explicitly: the StoryModel and Draft travel with every call. This makes the
skill testable, cacheable, and hostable anywhere.

## 3. Prompt contracts (where an LLM is needed)

Each contract has: `id`, `role`, `knowledge` (which documents are loaded),
`input_schema`, `output_schema`, `quality_checks` (validators that run on the
output), `temperature_guidance`, and `fallback` (what to do on schema
failure).

### C-01 `story-model-extract`
- In: draft + contract metadata. Out: StoryModel (fields from
  `interventions/03-story-model.md`). Knowledge: frameworks 02/04/05/06.
- Quality checks: every field cites a draft span; unknown fields marked
  `unknown`; no invented facts (checker: each fact must appear in the draft).
- Fallback: field-level retry; unresolved fields stay `unknown`.

### C-02 `tell-detect`
- In: draft + StoryModel + genre contract. Out: findings (schema:
  AnalysisReport.findings). Knowledge: taxonomy + evidence hierarchy.
- Quality checks: every finding has tell ID, quoted span, pattern evidence
  (a count/distribution/ledger-violation — not an adjective), confidence,
  K-code, function-test result, intentionality verdict.
- Fallback: findings failing the evidence check are demoted to
  `observations` (non-actionable).

### C-03 `intervene-level-N` (one contract per level, N=1…6)
- In: draft span + finding + StoryModel + level instructions
  (`interventions/01`). Out: proposed edit(s) with a per-sentence rationale.
- Quality checks: the edit passes all 14 preservation checks (simulated
  against the StoryModel); no new tell introduced (re-run C-02 on the span);
  minimality check (diff size ≤ expected for the level).
- Fallback: rejected proposals return to the queue at a lower level or
  Level 0.

### C-04 `reevaluate`
- In: applied edits + StoryModel. Out: per-edit verdicts
  (`kept`/`reverted`) with reasons, updated StoryModel, updated findings.

## 4. Generator independence

The skill treats the draft as a black-box artifact: it never requires
generator logprobs, model IDs, or API access to the generating model. Where
available, generator metadata (model family, decoding settings, prompt class)
is recorded in the input metadata and used to select calibration baselines
(`taxonomy/17` §17.3) — but absence of metadata degrades gracefully
(generic baselines + `uncalibrated` flags on findings).

## 5. Analyzer-model independence

- All thresholds are expressed as *parameters* (defaults in
  `skill/06-scoring.md`), recalibratable per analyzer model.
- Analyzer self-bias is explicitly handled: the skill's LLM-as-judge
  distrust rule (S04: LLM judges correlate poorly with experts on creative
  writing; S26: attribution bias in AI evaluators) means C-02/C-04 outputs
  are treated as *evidence*, never as verdicts. Verdicts require passing the
  framework's objective checks (ledger diffs, distributions, function
  tests).
- The `quality_checks` in each contract are deterministic validators (code),
  not model opinions.

## 6. Hosting contract

An implementer must provide:
1. `llm(prompt_contract, input_json) -> output_json` — any LLM endpoint.
2. Deterministic validators for the schemas (`schemas/`).
3. Storage for Draft + StoryModel + logs (any store).

Everything else is provided by this repository.
