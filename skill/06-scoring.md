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

Score range: −0.6 … 3.0. Queue threshold default: **1.2** (filters most
Low-confidence and high-FPR items into Observations). The threshold is a
parameter, not a quality knob: raising it reduces edits; lowering it below
0.8 is discouraged (that region is FPR-dominated).

## 3. Cause clustering (one cause, one problem)

Findings sharing a K-code and a structural locus (same scene, same character,
same ledger) are **merged into one queue item** with a combined rationale.
This prevents death-by-a-thousand-fixes: twenty explicitness findings caused
by one K3 stance are one intervention problem ("narrator's default stance is
interpretive"), fixed with the fewest edits that remove the *stance*, not
twenty parallel deletions.

## 4. Level assignment

Default level = the tell→level ceiling from
`interventions/01-intervention-hierarchy.md` §1. Downgrade rules:
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
(see `skill/09-evaluation-benchmark.md` for the human-side verification).

## 6. Anti-gaming properties

- No global "tell score" exists, so there is nothing to minimize by mass
  editing.
- Editing a passage cannot raise another passage's priority; the queue is
  recomputed from evidence after each level.
- Detector scores never enter any term (S12–S14, S35).
- `unchanged` and `reverted` outcomes are logged and counted in the
  benchmark as failures — the skill is judged on them.
