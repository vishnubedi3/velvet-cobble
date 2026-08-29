# Consolidation Report

This report records how the AI fictional-tells artifact-reduction skill was
consolidated into this single self-contained folder, and the results of the
audit performed on the consolidated result. It is part of the distributable
unit: anyone adopting the skill can see what changed and why.

## 1. What was consolidated

The skill previously lived as 52 files spread across the repository root
(`SKILL.md`, `research/`, `taxonomy/`, `frameworks/`, `interventions/`,
`skill/`, `schemas/`, `benchmark/`, `examples/`) plus a repository-level
`README.md` that described the old layout. All skill content was moved
atomically into **`ai-fictional-tells-skill/`** (this folder). No skill
content was deleted; nothing inside the folder depends on anything outside
it.

## 2. Final folder structure

```
ai-fictional-tells-skill/
├── README.md                     ← ENTRY POINT
├── SKILL.md                      ← primary specification
├── MANIFEST.md                   ← complete file inventory & portability contract
├── CONFIG.md                     ← consolidated configuration definitions
├── glossary.md                   ← canonical terminology
├── CONSOLIDATION-REPORT.md       ← this file
├── spec/                         ← core skill definition (02–13)
│   ├── 02-api-interface.md
│   ├── 03-input-schema.md
│   ├── 04-output-schema.md
│   ├── 05-pipeline.md
│   ├── 06-scoring.md
│   ├── 07-failure-modes.md
│   ├── 09-evaluation-benchmark.md
│   ├── 11-minimal-architecture.md
│   ├── 12-advanced-architecture.md
│   └── 13-integration.md
├── research/                     ← evidence (01 synthesis, 02 hierarchy, 03 sources)
├── frameworks/                   ← detection framework (01–07)
├── interventions/                ← intervention framework (01 hierarchy, 02 preservation, 03 story model)
├── taxonomy/                     ← tell catalog (README + 01–18, 20)
├── schemas/                      ← 4 JSON Schemas (input, analysis output, intervention, story model)
├── tests/                        ← 01 adversarial suite (A-T1…A-T23), 02 static consistency checklist (T-1…T-10)
├── examples/                     ← 01 before/after examples, 02 worked pipeline demo
└── benchmark/                    ← harness contract + cases/ manifest
```

## 3. Entry point

**[`README.md`](README.md)** — it states what the skill is, links
[`SKILL.md`](SKILL.md) as the primary specification, gives a five-minute
quick start (read → understand the loop → install → invoke → configure →
test), summarizes the binding rules, and documents compatibility/versioning
and portability guarantees. [`MANIFEST.md`](MANIFEST.md) is the full
inventory; [`glossary.md`](glossary.md) defines the shared vocabulary.

## 4. What was merged, removed, or reorganized

**Reorganized (moved, content preserved):**
- `skill/02…07, 09, 11…13` → **`spec/`** (renamed: the folder is the skill;
  the subfolder is its specification — the old `skill/skill/…` nesting was
  the ambiguity being removed). Original deliverable numbers kept as
  identifiers.
- `skill/08-adversarial-tests.md` → **`tests/01-adversarial-suite.md`**;
  `skill/10-before-after-examples.md` → **`examples/01-before-after-examples.md`**;
  `examples/worked-example-short-story.md` → **`examples/02-worked-example-short-story.md`**
  — tests and examples now live where users expect them.
- All of `research/`, `taxonomy/`, `frameworks/`, `interventions/`,
  `schemas/`, `benchmark/`, `SKILL.md` moved verbatim into the folder
  (cross-reference paths adjusted, see below).

**Merged/consolidated (new files, no content lost):**
- **`CONFIG.md`** — every parameter that was scattered across spec files
  (analysis options, scoring weights, calibration keys, lexicon config,
  prompt-contract parameters, pipeline parameters) is now defined in one
  place with defaults, ranges, and validation rules.
- **`glossary.md`** — canonical terminology for pipeline stages, levels,
  preservation dimensions, ID schemes (tell IDs, source IDs S01–S53,
  K-codes, F-codes, A-T/T/I/A/P/M codes), and the `S`-prefix
  disambiguation (description tells S01–S06 vs. source IDs S01–S53).
- **`MANIFEST.md`** — complete file inventory doubling as the portability
  contract for the static consistency checks.
- **`tests/02-static-consistency-checklist.md`** — ten static self-checks
  (T-1…T-10) that keep links, schemas, IDs, terminology, numbering,
  manifest coverage, containment, and the entry point honest across
  releases.
- **`schemas/skill-input.schema.json`** — the machine-readable input
  schema, previously only described in prose.
- **`benchmark/cases/README.md`** — case-file manifest and authoring
  template for the benchmark case suite.

**Fixed (defects found during the audit):**
- Duplicate source ID: **S46** pointed at two different works. S46 now
  exclusively denotes "Evaluating Literary Fiction with LLMs" (ACL 2025
  Findings); the Lincoln Michel *Counter Craft* practitioner source is
  **S53**. References updated in `research/02`, `taxonomy/01`, `03`, `05`,
  `17`.
- Stale metric reference: "A1–A10" → **A1–A7, P1–P5, M1–M4** in `SKILL.md`
  and `spec/04`.
- Misleading input-schema pointer in `spec/03` (now points at
  `schemas/skill-input.schema.json` and the output-side schemas correctly).
- `spec/13` vendoring list updated to the final layout.

**Removed:** nothing. The only "removals" were the old repository-root
`README.md`'s skill content, replaced by a pointer to this folder (the
repository no longer hosts skill documentation outside the folder).

**Cross-reference rewrite:** every internal reference (Markdown links and
file-path code tokens) was rewritten to be **relative to the referencing
file's own location** (previously root-relative). Bare directory references
(`frameworks/01`, `taxonomy/17-*`, `skill/02`) were expanded to exact
filenames.

## 5. Audit results (per `tests/02-static-consistency-checklist.md`)

| Check | Result |
|---|---|
| T-1 all internal links resolve (file-relative) | **PASS** (0 broken links) |
| T-2 JSON Schemas valid | **PASS** (4/4) |
| T-3 tell IDs referenced exist in `taxonomy/README.md` | **PASS** (0 unknown) |
| T-4 source IDs referenced exist in `research/03-source-index.md` | **PASS** (0 undefined) |
| T-5 manifest lists exactly the files present | **PASS** (0 orphans, 0 phantoms) |
| T-6 terminology consistent with `glossary.md` | **PASS** (no competing terms found; canonical terms in place) |
| T-7 numbering invariants (spec gaps 01/08/10; taxonomy 01–18+20; A-T1…A-T23; F-1…F-10; PV-1…PV-14; I-1…I-6; A1–A7/P1–P5/M1–M4) | **PASS** |
| T-8 no out-of-folder dependencies | **PASS** (no link escapes the folder; no absolute paths; no old-path remnants) |
| T-9 exactly one entry point (`README.md` → `SKILL.md`) | **PASS** |
| T-10 config consolidation (params cited ↔ defined in CONFIG.md) | **PASS** (all defaults traced to CONFIG.md) |

## 6. Remaining external dependency

**None at run time.** The folder contains no code and loads nothing: it is
documentation, JSON Schemas, and prompt contracts. The only non-local
resources are the cited research links (web URLs in
`research/03-source-index.md` / `research/01-research-synthesis.md`), which
are evidence references, not dependencies — the skill is fully functional
offline. At *implementation* time, the host must supply two capabilities
(an `llm()` function and a store — `spec/13-integration.md` §2), which are
host-provided interfaces, not skill dependencies.

## 7. Portability verdict

**The folder is genuinely portable as a standalone skill.** Evidence:
(1) every internal reference resolves from its own file's location with no
path escaping the folder; (2) the full audit suite passes; (3) the entry
point is self-sufficient for a new reader; (4) the skill remains
model-agnostic and API-agnostic by design (`spec/02-api-interface.md`);
(5) no research depth was dropped — the taxonomy (~95 tells), evidence
hierarchy, causal model, frameworks, intervention hierarchy, preservation
constraints, failure modes, adversarial suite, benchmark, and both
architecture tiers are all present and internally consistent.

## 8. How to re-verify after future changes

Run the checks in [`tests/02-static-consistency-checklist.md`](tests/02-static-consistency-checklist.md)
(T-1…T-10) from the folder root, and the behavioral suite
[`tests/01-adversarial-suite.md`](tests/01-adversarial-suite.md) against any
implementation. Add new files to [`MANIFEST.md`](MANIFEST.md) in the same
commit (T-5), and update [`glossary.md`](glossary.md) before introducing
new terminology (T-6).

---

# Addendum (2026-08-29) — Project Binding (v2.0.0)

**The §7 portability verdict is superseded.** The skill is no longer a
portable standalone skill; it is **bound to this repository's fictional
project (Samur)** and intentionally non-portable. Sections 1–8 above remain
the accurate record of the *consolidation*; this addendum records the
binding pass.

## What changed

| Change | Files |
|---|---|
| **New: the binding contract** — intake requirements (live canon resolution, Generation Contract, drafting constraints, KE position), division of labor with the Canon Guard, three authority classes (`project_canonical` / `empirical` / `project_style_rule`), five supremacy laws, maintenance triggers | `spec/01-project-binding.md` (new; fills the previously empty spec/01 slot) |
| **New: project-tell catalog** — PST-01…PST-10, each with canon citations, project examples, canon-sourced fixes, and a monitored table; S04 mood-weather overridden to PST-03 | `taxonomy/19-project-tells.md` (new; fills the previously empty 19 slot), `taxonomy/05-description.md` (S04 cross-note) |
| **Input requires the binding** — `project_context` required + Stage 0 validation; no generic fallback | `spec/03-input-schema.md` §1/§1.1/§6, `schemas/skill-input.schema.json` |
| **Detection re-ordered** — Pass A builds the scene canon surface + KE position; new Pass B0 (project scan, cheapest-first); transplant test anchored to the canon surface; in-world voice exception | `frameworks/01-detection.md` (rewritten), `spec/05-pipeline.md` Stage 1 |
| **Pipeline hardening** — Stage 0 binding validation; invariant I-7 (binding not bypassable); final-read FR-8 (project re-verification) | `spec/05-pipeline.md` |
| **Scoring** — authority qualifier (PST not confidence-weighted; score floor 1.3; intent protection only for canon-compliant devices); §7 project queue priority + downstream re-detection | `spec/06-scoring.md` |
| **Preservation** — §8 project supremacy laws + conflict-resolution order (content boundaries → project laws → PV → generic craft); F-11 generic-craft override | `interventions/02-preservation-constraints.md`, `spec/07-failure-modes.md` |
| **Output** — `Finding.authority`, canon citations as evidence, `routing: report_only: canon workflow` | `spec/04-output-schema.md`, `schemas/analysis-report.schema.json` |
| **Evaluation** — project-anchored rubric (5 project dimensions gate the pass); PST + project-trap case classes | `spec/09-evaluation-benchmark.md`, `benchmark/README.md` |
| **Tests** — A-T24…A-T31 project-binding traps; T-11 same-commit PST re-verification on canon change | `tests/01-adversarial-suite.md`, `tests/02-static-consistency-checklist.md` |
| **Integration rewritten** — from a vendoring guide ("drop into any codebase") to this-repository wiring + Canon Guard cooperation + non-portability clause | `spec/13-integration.md` |
| **Entry points & docs** — eleven binding rules (was eight); §4 project coupling; §5 portability statement; SKILL §8 maintenance; glossary §6a + numbering updates; MANIFEST; CONFIG §8 non-configurable binding; examples Ex-P1…P3 + project rejections; worked-example scope note | `SKILL.md`, `README.md`, `glossary.md`, `MANIFEST.md`, `CONFIG.md`, `examples/01–02` |
| **Repository docs** — root README deliverable paragraph (portability claim corrected); `skills/README.md` (binding paragraph); `skills/INTEGRATION.md` §15 amendment + inline corrections of now-false claims | outside this folder, minimal |

## New numbering (T-7 update)

- `spec/01` now exists (the binding); gaps remain at 08, 10.
- `taxonomy/19` now exists (project tells); taxonomy is complete 01–20.
- F-1…F-11, A-T1…A-T31, T-1…T-11, I-1…I-7, FR-1…FR-8.

## Superseded portability verdict (replacement for §7)

**The folder is deliberately non-portable.** Evidence: (1) intake requires a
Samur `project_context` and rejects everything else (`input_rejection`;
A-T24; schema `required`) — there is no generic mode; (2) the PST catalog,
examples, and rubric are derived from `samur/02-canon/`, `PROJECT.md`, the
drafting constraints, and the anti-patterns, and cite them; (3) the
supremacy laws make project rules override generic craft, so behavior
differs from any generic implementation by design; (4) external anti-slop
methodology was adapted, not copied (record: `research/03` S54), with no
runtime or structural dependency; (5) the skill must change when the
project's narrative standards change (T-11 same-commit re-verification).
Mechanical facts that still hold: internal references are file-relative and
resolve (T-1); no runtime dependencies; model- and API-agnostic hosting.

## Re-verification

Static suite re-run after the binding pass: T-1 links NONE broken; schemas
valid; ID sets complete (FR 1–8, F 1–11, A-T 1–31, T 1–11, PST 1–10 in the
canonical index); no `velvet-cobble`/absolute paths introduced; `../` chains
inside the folder. Behavioral suites (A-T, benchmark) remain acceptance
gates for any implementation.
