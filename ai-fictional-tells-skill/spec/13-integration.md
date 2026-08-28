# 13 — Integration Instructions (arbitrary repositories & model APIs)

**Goal.** Drop this skill into any codebase that generates fiction, in any
language, with any LLM provider.

## 1. What to vendor

Copy these directories into the host repo (e.g., under `skills/fictional-tell-reduction/`
or `.agent/skills/…`):

```
SKILL.md, README.md, MANIFEST.md, CONFIG.md, glossary.md, CONSOLIDATION-REPORT.md
spec/02 … spec/13
research/01 … 03
frameworks/01 … 07
interventions/01 … 03
taxonomy/README.md + taxonomy/01 … 18, 20
schemas/*.json
tests/01 … 02
examples/01 … 02
benchmark/README.md
```

These are documentation + schemas: no runtime dependencies, no language
assumptions.

## 2. Minimal wiring (any language)

The skill needs exactly two external capabilities:

```
llm(contract: PromptContract, input: JSON) -> JSON     // any provider
store.put(key, bytes) / store.get(key) -> bytes        // any persistence
```

Provider adapters (OpenAI/Anthropic/Gemini/local-vLLM/Ollama) are ~30-line
shims that implement `llm()`. The contracts in `../spec/02-api-interface.md`
§3 define what `llm()` must return (JSON per schema); temperature guidance
is in each contract (analysis: low; reconstruction: moderate).

## 3. Where to hook the skill in a generation pipeline

```
author → [prompt/outline] → generator → draft
                                      ↓
                              skill.analyze(draft, meta)
                                      ↓
                              skill.intervene(queue, story_model)
                                      ↓
                              revised draft + report
                                      ↓
                              author review (Level ≥4 proposals, worldview gates)
```

Hook points:
- **Post-generation (default):** run the skill on the completed draft.
- **Per-chapter (long-form):** run after each chapter; persist the
  StoryModel; feed the state summary back into the generator's continuation
  context (frameworks/06 §4 — the strongest prevention for L-tells).
- **CI gate (optional):** run `analyze` only (max level 0) as a
  quality/artifact report in CI; intervention stays author-driven.
- **Editing sessions:** for interactive writing tools, run Pass B/C on the
  current scene for live findings (latency: one chunked call).

## 4. LLM provider notes

- **Context budgeting.** The knowledge load is large; use the retrieval
  strategy from `../spec/12-advanced-architecture.md` §1 (per-finding
  loading) — providers with small windows should load: taxonomy index +
  the relevant cluster file + interventions/01–02 (≈5–10k tokens per call).
- **JSON discipline.** Contracts include the output schemas; if a provider
  struggles with strict JSON, add a schema-repair pass (deterministic) —
  never accept malformed findings silently (validators are mandatory).
- **Temperature.** Analysis: as low as the provider allows. Re-voicing/
  reconstruction (Levels 3–6): moderate; but note the skill's edits are
  *targeted* (small spans), so diversity settings matter less than for
  open-ended generation.
- **Model choice.** Any capable model works. Known biases to manage:
  LLM-judge unreliability on creative writing (S04) — the deterministic
  validators do the verdicts; attribution bias (S26) — never ask the model
  to rate "humanness."

## 5. Repository-specific concerns

- **Fiction corpora in-repo.** If the host repo contains a fiction corpus,
  use it to build the calibration baselines (benchmark/README §Corpus).
- **Multi-language.** Lexicon-based detectors are parameterized; retune per
  language and mark findings `uncalibrated` until done (taxonomy/17 §17.3).
- **Styling/linting.** The skill outputs plain text or markdown; format
  preservation is the host's job — but the skill never mutates anything
  outside the quoted spans (reversibility invariant).

## 6. Compliance & provenance integration

- If the host has disclosure requirements (venue policies, platform
  rules), wire the skill's `provenance` fields (`../spec/03-input-schema.md`
  §5) to the host's compliance checks: the skill records assistance scope
  and never strips required disclosures (F-9).
- Reports are stored with the draft's version history so provenance
  decisions remain auditable.

## 7. Upgrade path (minimal → advanced)

1. Start with `../spec/11-minimal-architecture.md` (two contracts + validators).
2. Add the deterministic engines one by one (repetition finder first —
   it's the highest-confidence, lowest-cost win; then ledgers; then voice
   profiler; then skeleton clustering).
3. Add the calibration subsystem when the second generator family is
   introduced.
4. Add the long-form state store when drafts exceed ~10k words.
5. Wire the benchmark harness before trusting the skill on production
   fiction.

## 8. Acceptance checklist

- [ ] Adversarial suite (../tests/01-adversarial-suite.md) passes: A-T1…A-T23.
- [ ] Pipeline invariants I-1…I-6 hold (../spec/05-pipeline.md).
- [ ] P1–P4 preservation metrics at 100% on the benchmark case suite.
- [ ] No detector scores anywhere in the pipeline (F-4).
- [ ] Level 0 default respected: a clean human draft receives zero edits.
