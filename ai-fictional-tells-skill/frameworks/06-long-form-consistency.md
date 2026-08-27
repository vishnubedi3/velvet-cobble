# Framework 06 — Long-Form Consistency Framework

**Scope.** Drafts ≳ 10k words (where context-fragmentation and state-loss
effects measurably begin, S22/S32). Detects taxonomy/18 (L01–L10) and feeds
the long-form parts of the story model.

**Sources:** S20, S22, S31, S32, S33, S49.

## 1. The state-first principle

Long-form tells are **state failures**, not style failures. The framework's
first job is therefore to build and maintain the story state
(`../interventions/03-story-model.md`) — characters, facts, world rules,
timeline, reader-information — and to check the draft against it. Style
analysis runs second.

## 2. Ledgers and audits

| Ledger | Contents | Audit |
|---|---|---|
| Fact ledger | names, ages, dates, places, object states | contradiction diff (L04) |
| Timeline ledger | event timestamps, durations, day-of-week | drift/contradiction (L09) |
| World-rule ledger | magic/tech/social rules + costs | consistency (L05); note deliberate soft-magic ambiguity (W02 exempt) |
| Character-state ledger | injuries, debts, objects held, promises | consequence persistence (A03), contradiction (L04) |
| Voice ledger | per-character voice profiles by chapter | drift detection (L01): per-chapter voice distance from the character's baseline |
| Scene-type ledger | scene skeletons by chapter | adjacency/over-representation (L03), skeleton recycling |
| Motif register | intended recurring images (with variation pattern) | distinguishes intended motif from accidental repetition (L10 vs. V04) |
| Reader-information register | what the reader has been told, when | re-recap detection (L08); information-leak checks |

## 3. Long-form tell detection

| Tell | Detector |
|---|---|
| L01 voice/character drift | voice-ledger distance spikes without story cause |
| L02 repeated beats/descriptions | near-duplicate passage clusters (n-gram/embedding); beat-recurrence |
| L03 recycled skeletons | scene-type adjacency repeats; cluster over-representation |
| L04 contradictions | fact/timeline/state diffs |
| L05 world inconsistency | rule-ledger diffs |
| L06 formulaic decay | per-chapter diversity curves (TTR, syntactic diversity, S20 method) |
| L07 mid-story sag | event-density dip + stakes-recall failure in middle third (S22 position effect) |
| L08 recaps | reader-information register: passages re-stating established facts |
| L09 timeline drift | timeline-ledger diffs |
| L10 unintended motifs | motif-register misses: recurrences without variation/escalation |

## 4. Generation-side prevention (preferred to revision)

Most L-tells are cheaper to *prevent* than to *fix*:

1. **State-carrying context.** Each generation segment (chapter/scene) is
   conditioned on a compact, current story-state summary (the S32 coordinator
   pattern) — facts, voice anchors, unresolved threads, upcoming payoffs.
2. **Voice anchors.** Per-character voice profiles ride in the context for
   every segment (L01 prevention).
3. **No-recursion discipline.** The segment's output is never used as its own
   primary context without the state summary (diversity decay, S20).
4. **Mid-context care.** Critical continuity facts are placed at segment
   *edges*, not middles (S22).

## 5. Revision-side remediation

| Tell | Fix (level) |
|---|---|
| L02, L08, L10 (repetition family) | Level 2 cut; Level 3 vary the one recurrence that earns it |
| L04, L05, L09 (contradiction family) | Level 1–2 state corrections against the ledger (word/clause edits) |
| L01 (drift) | Level 3 re-voice against the character's baseline profile |
| L03 (skeletons) | Level 4 beat-order variation per scene purpose |
| L06 (decay) | Level 1–2 specificity repairs (P01) in flagged chapters |
| L07 (sag) | Level 4 re-tensioning from the event register (cut repeats, re-raise stakes) |

All fixes are logged against the ledger they corrected.

## 6. Preservation checks (binding)

- No contradiction repair may *introduce* a new contradiction (diff the
  ledger both ways).
- No cut may strand a fact the reader needs later (PV-9).
- No skeleton change may break the causal chain (frameworks/05 §4).
- Intended motifs (in the motif register) are preserved even when they look
  like L10 candidates.

## 7. False-positive notes

- Intended refrain/motif ≠ L10 (motif register decides).
- "Lost in the middle" is measured in QA-style tasks (S22); in fiction it
  manifests as L07/L08 — treat the transfer as mechanism-grounded, not
  point-identical.
- Per-model degradation differs (S31): calibrate thresholds per generator.
