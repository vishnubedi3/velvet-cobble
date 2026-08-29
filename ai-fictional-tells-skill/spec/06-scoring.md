# 06 — Scoring Methodology

**Purpose.** Rank findings so that limited intervention budget goes to the
highest (cause-certainty × story-damage) targets — and so that scoring can
never be gamed into "edit more."

## 1. What is scored

The skill scores **findings** (candidate artifacts with evidence), never
text. There is no paragraph-level "AI score," no document-level score, and no
optimization toward any threshold. Scoring exists only to order the queue.

## 2. Finding score

```
priority = severity_weight
         × confidence_weight
         × function_loss
         − false_positive_penalty
         − intent_protection
```

| Term | Values | Source |
|---|---|---|
| `severity_weight` | 3 / 2 / 1 (taxonomy severity) | taxonomy |
| `confidence_weight` | high 1.0 / medium 0.6 / low 0.2 | evidence hierarchy §2.2 |
| `function_loss` | 0–1. 1 = passage does no work (function test failed hard); 0.3 = partially redundant; 0 = does work (then it's an Observation anyway) | taxonomy/20 §20.2 |
| `false_positive_penalty` | 0 / 0.3 / 0.6 for FPR 1/2/3 | taxonomy |
| `intent_protection` | 0 (no intent match) / 0.5 (possible device) / ∞ (declared device → Observation) | interventions/02 §3 |

**Authority qualifier (`../spec/01-project-binding.md` §2).** The formula
above applies to *empirical* findings. `project_canonical` (PST) findings
are not confidence-weighted: `confidence_weight` is fixed at 1.0 (the
authority is canon, not evidence), the score floor is 1.3 (above the default
queue threshold — a PST finding can never be thresholded into a mere
Observation), and `intent_protection` ∞ applies only where the author's
*declared device* is itself canon-compliant (a declared device that violates
canon is a `report_only: canon workflow` item for the author, not an
editable or ignorable finding). `project_style_rule` findings score as
empirical, capped at Level 2.

Score range: −0.6 … 3.0 (empirical); ≥ 1.3 floor (project_canonical). Queue
threshold default: **1.2** (filters most Low-confidence and high-FPR items
into Observations). The threshold is a parameter, not a quality knob: raising
it reduces edits; lowering it below 0.8 is discouraged (that region is
FPR-dominated). Raising it above 1.3 cannot hide a PST finding.

## 3. Cause clustering (one cause, one problem)

Findings sharing a K-code and a structural locus (same scene, same character,
same ledger) are **merged into one queue item** with a combined rationale.
This prevents death-by-a-thousand-fixes: twenty explicitness findings caused
by one K3 stance are one intervention problem ("narrator's default stance is
interpretive"), fixed with the fewest edits that remove the *stance*, not
twenty parallel deletions.

## 4. Level assignment

Default level = the tell→level ceiling from
`../interventions/01-intervention-hierarchy.md` §1. Downgrade rules:
- confidence `low` → cap at Level 2;
- intent_protection ≥ 0.5 → cap at Level 0/1 (author consultation);
- `uncalibrated` baseline → cap at Level 3;
- preservation-risk count ≥ 3 dimensions → drop one level and require the
  batch gate.

Upgrade requires written evidence of lower-level insufficiency (escalation
rule §2 of interventions/01).

## 5. The re-evaluation score (did the fix work?)

After an applied edit, the *same finding* is re-measured:

```
outcome = { fixed     : cause absent & function test passes & no new tell
          , improved  : cause reduced, residual recorded
          , unchanged : cause still present → revert candidate
          , reverted  : post-check failure (any PV violation)
          }
```

The re-evaluation uses the *framework detectors*, not the scorer: an edit
only "works" if the measurable pattern (repetition count, redundancy, ledger
diff) changed and nothing broke. Scoring cannot declare victory by itself
(see `../spec/09-evaluation-benchmark.md` for the human-side verification).

When all levels are complete, the **final read** (`../spec/05-pipeline.md`
Stage 4b, FR-1…FR-8) runs once over the whole revised draft. FR outcomes are
reported with the run; an FR failure is logged and counted like a reversion
outcome (an M2-class failure in the benchmark), not like a neutral finding.

## 6. Anti-gaming properties

- No global "tell score" exists, so there is nothing to minimize by mass
  editing.
- Editing a passage cannot raise another passage's priority; the queue is
  recomputed from evidence after each level.
- Detector scores never enter any term (S12–S14, S35).
- `unchanged` and `reverted` outcomes are logged and counted in the
  benchmark as failures — the skill is judged on them.

## 7. Project priority in the queue (Samur binding; `../spec/01-project-binding.md` §3.2)

1. **No empirical fix outranks an unresolved project_canonical finding in
   the same span.** Queue order within a span: PST findings first (by their
   own scores), then empirical findings. Rationale: a draft must be right
   about the world before it can be improved as prose — an S-cluster rhythm
   edit to a passage whose wind position is wrong (PST-03) is polishing a
   scene that may have to move or be re-derived.
2. **Downstream re-scoring after a PST fix.** A Level ≥3 PST fix (re-derived
   scene, re-voiced dialogue) can invalidate empirical findings in the same
   span — repetition counts, rhythm measurements, continuity ledgers taken
   against the *old* text. Empirical findings in a PST-fixed span are
   re-detected (not merely re-scored) after the fix; stale findings are
   dropped, new ones enter the queue normally.
3. **Report-only routing is not scoring.** Canon-contradiction findings and
   author-gated PST resolutions never enter the queue regardless of score;
   they are reported (`analysis_report` routing) for the Canon Guard /
   author workflow.
