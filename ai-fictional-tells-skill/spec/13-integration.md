# 13 — Integration Instructions (this repository & any model API)

**Goal.** Run this skill inside **the Velvet Cobble / Samur pipeline**, with
any LLM provider, as the post-generation quality layer cooperating with the
Canon Guard. The skill is **project-bound** (`../spec/01-project-binding.md`):
these instructions wire it into *this* repository — they are not a
vendoring guide for other projects (§8).

## 1. What this skill needs in place (all in-repo)

The skill runs from its folder, reading the repository's living documents:

```
ai-fictional-tells-skill/          (this skill: spec/, research/, frameworks/,
                                    interventions/, taxonomy/ incl. 19, schemas/,
                                    tests/, examples/, benchmark/)
PROJECT.md                          (charter — read-only)
samur/02-canon/                     (canon — read-only, resolved live at Stage 0)
samur/00-audit/…cross-check.md      (drafting constraints + gate status — read-only)
skills/canon-guard/                 (anti-patterns, workflow — read-only)
```

Documentation + schemas only: no runtime dependencies, no language
assumptions, **and no writes outside `ai-fictional-tells-skill/` and the
draft under review**.

## 2. Minimal wiring (any model API)

The skill needs exactly two external capabilities:

```
llm(contract: PromptContract, input: JSON) -> JSON     // any provider
store.put(key, bytes) / store.get(key) -> bytes        // any persistence
```

Provider adapters (OpenAI/Anthropic/Gemini/local-vLLM/Ollama) are ~30-line
shims that implement `llm()`. The contracts in `../spec/02-api-interface.md`
§3 define what `llm()` must return (JSON per schema); temperature guidance
is in each contract (analysis: low; reconstruction: moderate). One addition:
the analysis contract's knowledge load now includes the project context and
`taxonomy/19` (§4).

## 3. Where the skill sits in this repository's pipeline

```
author → Canon Guard (canon resolution + Generation Contract) → generator → draft
                                                                                  ↓
                                              skill Stage 0: validate project_context
                                              skill Pass A: canon surface + voice baseline
                                              skill Pass B0/B/C: project tells first, then generic
                                              skill intervene (level-ordered, supremacy laws)
                                                                                    ↓
                                                              revised draft + report
                                                                                    ↓
                                              author review (Level ≥4 proposals, worldview gates)
                                              report-only items → Canon Guard / author workflow
```

Hook points:
- **Post-generation (default):** run the skill on the completed draft
  segment.
- **Per-chapter (long-form):** run after each chapter; persist the
  StoryModel; feed the state summary back into the generator's continuation
  context (frameworks/06 §4 — the strongest prevention for L-tells).
- **CI gate (optional):** run `analyze` only (max level 0) as a
  quality/artifact report in CI; intervention stays author-driven.
- **Editing sessions:** for interactive writing, run Pass B0/B/C on the
  current scene for live findings (latency: one chunked call).

## 4. Loading the project side

- **Stage 0 inputs.** `project_context` (spec/03 §1.1) is assembled by the
  caller: the canon resolution (obtained via the Canon Guard's re-resolution
  — never snapshotted), the Generation Contract reference, the drafting
  constraints reference, and the draft's KE position.
- **Context budgeting.** The knowledge load is large; use the retrieval
  strategy from `../spec/12-advanced-architecture.md` §1 (per-finding
  loading) — providers with small windows should load: the project context +
  `taxonomy/19` (for Pass B0) + taxonomy index + the relevant cluster file +
  interventions/01–02 (≈5–12k tokens per call).
- **JSON discipline.** Contracts include the output schemas; if a provider
  struggles with strict JSON, add a schema-repair pass (deterministic) —
  never accept malformed findings silently (validators are mandatory).
- **Temperature.** Analysis: as low as the provider allows. Re-voicing/
  reconstruction (Levels 3–6): moderate; the skill's edits are *targeted*
  (small spans), so diversity settings matter less than for open-ended
  generation.
- **Model choice.** Any capable model works. Known biases to manage:
  LLM-judge unreliability on creative writing (S04) — the deterministic
  validators do the verdicts; attribution bias (S26) — never ask the model
  to rate "humanness."

## 5. Repository-specific concerns (this repository's)

- **Canon freshness.** A run must resolve canon at Stage 0, not trust a
  cached copy; a canon resolution older than the draft's generation run is
  an `input_rejection` (spec/03 §1.1). When canon changes on the branch,
  checklist T-11's same-commit re-verification applies before the skill
  runs again (A-T31).
- **Read-only neighbors.** The skill reads `PROJECT.md`, `samur/`, and
  `skills/canon-guard/` and never writes them. Its outputs are: the revised
  draft, reports, and files under `ai-fictional-tells-skill/`.
- **Multi-language drafting.** The project's fiction is English-language
  prose about a multilingual world; the language map (CUL-02) is canon, not
  a lexicon calibration surface. Lexicon parameterization remains for the
  skill's own internal detectors only (taxonomy/17 §17.3).
- **Styling/linting.** The skill outputs plain text or markdown; format
  preservation is the pipeline's job — but the skill never mutates anything
  outside the quoted spans (reversibility invariant).

## 6. Compliance & provenance integration

- Wire the skill's `provenance` fields (`../spec/03-input-schema.md` §5) to
  the project's disclosure practices: the skill records assistance scope and
  never strips required disclosures (F-9).
- Reports are stored with the draft's version history so provenance
  decisions remain auditable.

## 7. Upgrade path (minimal → advanced, in this repo)

1. Start with `../spec/11-minimal-architecture.md` (two contracts +
   validators), plus the Stage 0 binding check.
2. Add the deterministic engines one by one (repetition finder first —
   the highest-confidence, lowest-cost win; then ledgers; then voice
   profiler; then skeleton clustering; then the PST checkers — name
   resolution and wind-position are the two cheapest).
3. Add the calibration subsystem when a second generator family is
   introduced.
4. Add the long-form state store when drafts exceed ~10k words.
5. Wire the benchmark harness (PST cases + project traps first) before
   trusting the skill on production chapters.

## 8. Not portable, by design

This skill cannot be vendored into another repository as-is: its intake
requires a Samur `project_context`; its PST catalog encodes this project's
canon (wind law, name pools, faction structures, mysteries); its rubric is
judged against this project's standards; and its supremacy laws make canon
outrank generic craft. **Adapting the methodology to another project means
re-deriving `spec/01` and `taxonomy/19` from that project's own canon and
standards** (and re-validating the generic layer against them) — not copying
this folder. See `../spec/01-project-binding.md` §1 and the skill README's
portability statement.

## 9. Acceptance checklist

- [ ] Adversarial suite (../tests/01-adversarial-suite.md) passes:
      A-T1…A-T31, including the project-binding traps (zero canon mutations,
      zero mystery resolutions).
- [ ] Pipeline invariants I-1…I-7 hold (../spec/05-pipeline.md).
- [ ] P1–P4 preservation metrics at 100% on the benchmark case suite
      (including the PST and project-trap cases).
- [ ] No detector scores anywhere in the pipeline (F-4).
- [ ] Level 0 default respected: a clean human draft receives zero edits.
- [ ] Stage 0 rejects unbound input (no generic fallback) and T-11 is green.
