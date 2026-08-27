# Framework 04 — Scene Analysis Framework

**Purpose.** Detect scene-construction tells (taxonomy/07, /08), extract scene
state, and provide the structural information pacing/description interventions
need.

**Sources:** S04, S22, S28, S31, S37, S44.

## 1. Scene segmentation & typing

1. Segment the draft into scenes (time/place/participant changes).
2. Type each scene: `action`, `dialogue`, `interior`, `transition`, `rest`,
   `climax`, `resolution`.
3. Record per scene: purpose (plot / character / world / rhythm), POV, length,
   intensity curve, position in act.

## 2. Scene tell detection

| Tell | Detector |
|---|---|
| SC01 opening triad | opening-type histogram (location+mood+weather first = dominant type) |
| SC02 announced entrances | entry-adjacent emotion labels with causes |
| SC03 stated purpose | purpose-declarations at scene top ("We need to talk about…") |
| SC04 end button | button density at scene ends; promise-vs-delivery of each button |
| SC05 repeated skeleton | beat-sequence clustering across scenes (same order, different content) |
| SC06 no incidental behavior | off-purpose micro-action count ≈ 0 |
| S01–S05 (description) | perceiver audit (§3) + sense-inventory + camera-pan density |
| T01–T05 (pacing) | scene-length variance; setup:climax ratio; intensity monotonicity; quiet-scene count; conflict lifespan |

## 3. Perceiver audit (the master description check — S06)

For every descriptive passage:

1. **Who perceives?** Identify the perceiver (POV character, narrator).
2. **Why now?** Does the perception serve a need (searching, hiding,
   recognizing), a mood-contrast, a world-fact, or rhythm?
3. **Would they?** Does the detail fall inside the character's knowledge and
   attention profile (frameworks/02 §3: what this character notices)?

Passages failing (2) are S06 candidates; passages failing (3) are voice
violations (S05's camera-eye fix target). Remediation re-routes the same
information through the perceiver's purpose — never deletes wholesale unless
the information has no function at all (then Level 2 deletion).

## 4. Scene state register (for A02/A03 and long-form)

Each scene carries a **state record**: participants, positions, held objects,
injuries/damage, weather/time, mood state. The analyzer:

- builds the state ledger per scene from the text;
- detects contradictions *within* a scene (A02) and *across* scenes (A03:
  consequence decay; L04/L09);
- feeds repairs: continuity edits are state corrections (usually one clause),
  not rewrites.

## 5. Beat-structure analysis (for SC05, N05, L03)

Represent each scene as a beat sequence over a small beat vocabulary
(`enter → purpose → conflict → partial resolution → button`, etc.). Cluster
scenes by beat sequence; adjacent or over-represented clusters flag SC05/N05;
long-form adjacency repeats flag L03. Remediation (Level 4) reorders beats
per scene purpose — a conflict-first scene, a button-free scene — chosen from
the scene's dramatic job, not from a randomization.

## 6. Intensity & distance curves (for T01–T04, V01)

Per scene and per act: plot an intensity estimate (stakes × affect ×
pacing-density) and a narrative-distance estimate (interiority depth).
- Flat intensity curve → T01/T04.
- Setup:climax ratio inverted vs. genre norms → T02.
- Button density at scene ends → T03.
- Distance never varies at crisis points → V01.

## 7. Preservation checks (binding)

- Scene purpose (PV-11): no edit may remove the scene's function without a
  replacement that serves it.
- Information availability (PV-9): scene reordering must not leak or strand
  plot facts.
- Genre contract (PV-12): scene buttons/cliffhangers in serial thrillers are
  contractual — the genre gate runs first.
- Perceiver integrity (PV-2/PV-4): re-routed description must stay inside the
  perceiver's profile.

## 8. False-positive notes

- Establishing shots are legitimate in SFF (contract check).
- Slow scenes are legitimate rhythm (T04 flags *inability* to rest, not
  rest itself).
- Over-choreographed blocking is a style in some comedy (only flag against
  the work's own baseline).
