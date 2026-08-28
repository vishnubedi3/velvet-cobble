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
