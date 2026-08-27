# 04 — Output Schema

Machine-readable: `schemas/analysis-report.schema.json` and
`schemas/intervention-request.schema.json`. This file is the normative
human-readable contract.

## 1. `SkillReport` (top-level)

```
SkillReport {
  analysis:        AnalysisReport
  intervention:    InterventionLog
  revised_draft:   Draft'
  story_model:     StoryModel (post-edit)
  rejected:        RejectedEdit[]
  summary:         { applied: n, reverted: m, preserved: k, flagged_intentional: j }
}
```

## 2. `AnalysisReport`

```
AnalysisReport {
  contract:        ContractExtraction      // Pass A result
  story_model:     StoryModel              // interventions/03
  findings:        Finding[]               // Pass B/C result
  observations:    Observation[]           // non-actionable (Low/Folklore/intentional)
  calibration:     Calibration             // baselines + thresholds used
  priority_queue:  Finding[] (sorted)      // Pass D result
}
```

### `Finding`

| Field | Notes |
|---|---|
| `id`, `tell_ids[]` | one finding may cite several taxonomy IDs sharing a cause |
| `spans[]` | quoted draft spans (start/end offsets) |
| `pattern_evidence` | **objective**: counts, distributions, ledger diffs, cluster IDs — never adjectives ("feels flat" is not evidence) |
| `confidence` | `high / medium / low` (evidence hierarchy §2.2) |
| `evidence_refs[]` | source IDs (research/03) |
| `cause` | K1–K9 code + one-line mechanism |
| `function_test` | taxonomy/20 §20.2 result: what the passage does, if anything |
| `intentionality` | `deliberate / accidental / undetermined` + reasoning |
| `proposed_level` | 0–6 (ceiling per tell→level map) |
| `preservation_risks[]` | which PV dimensions the fix would touch |

### `Observation`

Like a Finding, but `actionable: false` with a reason (`low_confidence` /
`folklore` / `intentional` / `contractual` / `uncalibrated`). Observations
are included so the author can see what the skill considered and why it held
back.

### `Calibration`

Which baselines were used (internal/corpus), which thresholds, whether
generator metadata was present; findings computed under `uncalibrated`
conditions are individually marked.

## 3. `InterventionLog`

```
InterventionLog {
  entries: InterventionEntry[]
}
InterventionEntry {
  id, finding_ref, level, spans_before, spans_after,
  rationale: { cause, why_lower_levels_insufficient? (for L≥2) },
  preservation_checks: PVResult[14],   // pass/reject per dimension
  causality_audit?:  CausalityDiff,    // required for L≥4
  reevaluation: { kept | reverted, reason, post_edit_findings[] }
}
```

Every applied edit keeps a full trace from tell → cause → level → diff →
preservation results → post-check. Every rejection (pre- or post-apply) is
logged in `RejectedEdit` with the specific violated constraint.

## 4. Schema-level guarantees

1. **No verdict without evidence.** The validator rejects findings whose
   `pattern_evidence` is not objective.
2. **No edit without checks.** The validator rejects entries missing the 14
   PV results.
3. **Reversibility.** `spans_before/after` are complete enough to
   byte-level revert any entry.
4. **Provenance-neutral.** The report contains no "AI score" and no
   humanness claim of any kind.

## 5. Downstream consumption

- Human author: the summary + observations + rejected list (the report is
  written to be *read*, not just parsed).
- Automation: `revised_draft` + `InterventionLog` + updated `StoryModel`
  feed the next pipeline stage (continuation, long-form state,
  `frameworks/06`).
- Benchmark: `skill/09-evaluation-benchmark.md` consumes Findings + logs to
  compute metrics A1–A10.
