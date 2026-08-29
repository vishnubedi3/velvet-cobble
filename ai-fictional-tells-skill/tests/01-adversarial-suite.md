# 08 — Adversarial Test Suite

Tests designed to break the skill. A conformant implementation must pass
these (they are part of the benchmark, `../spec/09-evaluation-benchmark.md`).
Each test names the failure mode it targets (F-#, `../spec/07-failure-modes.md`).

## Intentional-choice traps (the skill must NOT edit)

| # | Trap | Correct behavior |
|---|---|---|
| A-T1 | A literary draft with a deliberately essayistic narrator (interpretive glosses everywhere, author declares "the narrator explains — that's the voice"). | U02/V02 findings → Observations (`intentional`), zero edits. |
| A-T2 | A mystery with a perfectly closed setup/payoff ledger, solution fairly planted. | N03/FS02 → contract gate → Observations. Zero structural edits. |
| A-T3 | A romance following the HEA ladder exactly, author declares genre intent. | R02 → contract gate → Observations. |
| A-T4 | A serial thriller whose every scene ends on a button (contract). | T03/SC04 → contract gate. |
| A-T5 | A hard-SF story with heavy system specs (contract). | W02 → contract gate. |
| A-T6 | A Carver-style flat, polished, "anonymous" voice. | V03 → must *not* be "fixed" by quirk injection. Observation-level only. |
| A-T7 | A child character who is deliberately inarticulate *and* an adult who is deliberately articulate — in the same draft. | C03 must not trigger (inter-character distance is large); D04 must not re-voice either toward the middle. |
| A-T8 | An intended motif (repeats 6×, varying and deepening) + an accidental near-duplicate description (repeats 3× verbatim) in the same draft. | L10 protects the motif; L02 fixes only the verbatim duplicates. |

## Continuity traps (the skill must NOT break)

| # | Trap | Correct behavior |
|---|---|---|
| A-T9 | Draft where "the letter" is discovered in ch. 3; a proposed U01 edit makes ch. 1 dialogue imply it. | Edit rejected: PV-10 violation, quoted evidence. |
| A-T10 | Draft with a causal chain A→B→C; a proposed SC05 beat reorder moves B before A. | Rejected by causality audit (PV-1/PV-7). |
| A-T11 | An E01 edit that replaces "she was terrified" with behavior implying *despair*, conflicting with the ch. 8 arc state (hope). | Rejected: PV-9 (emotional trajectory). |
| A-T12 | An L04 repair that "fixes" a name by changing the *later* occurrence, contradicting the earlier letter. | Rejected: repair must target the earlier span (story-model check). |

## New-artifact traps (the skill must not install artifacts)

| # | Trap | Correct behavior |
|---|---|---|
| A-T13 | P04 finding on a rhythmic passage. | If edited at all: punctuation-level only; if the edit produces fragment-chopping, the new-artifact rule reverts it. |
| A-T14 | V03 finding on flat voice. | Any edit introducing tics/quirk is reverted by the new-artifact rule. |
| A-T15 | E01 fix that produces opaque behaviorism (reader can't decode). | Fails the decodability rule (frameworks/03 §3) → rejected. |
| A-T16 | D04 fix that re-voices a character via dialect tic-spam. | Fails voice-profile check → rejected. |

## Detector-independence traps

| # | Trap | Correct behavior |
|---|---|---|
| A-T17 | Run the skill with a detector score supplied as input metadata. | Score ignored; logged as out-of-scope. No behavioral change. |
| A-T18 | Run the skill twice on the same draft (idempotence). | Second run applies no Level ≥3 edits; Level 1–2 must re-pass evidence. |
| A-T19 | Feed a draft that is *entirely fine* (human-written, no tells). | Report contains findings only below threshold; zero edits; summary shows preserved = all. |
| A-T20 | Feed a draft with heavy tells and `max_intervention_level: 0`. | Analysis-only: report complete, draft byte-identical. |

## Escalation-discipline traps

| # | Trap | Correct behavior |
|---|---|---|
| A-T21 | A finding whose proposed fix jumps straight to Level 5 with no lower-level attempt. | Rejected by pipeline invariant I-1; logged. |
| A-T22 | A Level 4 batch that includes a worldview-touching edit (N07/F03) without author consent. | Rejected (author gate); item returned as `author-consult-required`. |
| A-T23 | An edit whose diff exceeds the level's minimality expectation without per-sentence rationale. | Rejected by the C-03 quality checks. |

## Project-binding traps (the skill is Samur-bound; `spec/01-project-binding.md`)

| # | Trap | Correct behavior |
|---|---|---|
| A-T24 | Run with `project_context` missing, `binding: "other"`, or a frozen/stale canon resolution. | `input_rejection` naming the failed field; **no analysis output, no generic fallback** (invariant I-7). |
| A-T25 | A PST finding (e.g. PST-03 wind-law) and a generic finding (S02 rhythm) in the same span; queue order tested. | PST first; the rhythm edit is not applied before the wind fix resolves (spec/06 §7); if re-detection after the fix drops the rhythm finding, it is dropped. |
| A-T26 | A generic "fix" that violates the binding: replacing a repeated office name (Shreshtha/Dhresh/Beshara) with referent cycling; varying a canon-frozen register; "enriching" a plain author-declared span; inventing a named pass for specificity. | Edit rejected under interventions/02 §8 (F-11); logged with the violated law; finding re-routed (author/canon workflow where applicable). |
| A-T27 | A draft that contradicts canon (an extra founding-era institution surviving to post-KE 900; a consecrated King in the Dhaneshra Period). | Finding reported `report_only: canon workflow`; **no edit to samur/, no QUESTION filed, no prose edit that rewrites canon to match the draft**. |
| A-T28 | An edit that resolves a protected mystery (quotes the Kesra Charter, names the western partner) or fixes a NOT READY detail by asserting it. | Rejected (PST-10; law 4); converted to an approach or author-gated; never applied silently. |
| A-T29 | A coined name offered as a PST-09 "fix"; a new high-impact fact smuggled in by a Level 4 rewrite. | Rejected (laws 2–3: no coining, no new high-impact facts); the fix restores a pool name or returns author-gated. |
| A-T30 | Canon-compliant spans that look like generic tells: a chronicle's distorted founding myth; register differences across the language map; an approached (not resolved) mystery; deliberate NS-01 "what didn't happen" texture. | Preserved: in-world voice exception (spec/01 §3.4), language-map protected differences, PST-10's FPR note, function test. Zero mutations. |
| A-T31 | Canon changes on the branch (a name-pool update, a new NOT READY item) without a skill update in the same commit. | Detected by the static check T-11; the run refuses drafts generated under the newer canon until re-verification passes. |

## Pass criteria

- Traps A-T1…A-T8: zero text mutations.
- Traps A-T9…A-T12: rejected edits with the correct cited constraint.
- Traps A-T13…A-T16: revert-or-reject.
- Traps A-T17…A-T20: behavior as specified.
- Traps A-T21…A-T23: rejection with correct reason.
- Traps A-T24…A-T31: rejection/report-only/preservation as specified — in
  particular, **zero canon mutations and zero mystery resolutions across the
  entire suite**.
Any failure is a blocking defect for the implementation.
