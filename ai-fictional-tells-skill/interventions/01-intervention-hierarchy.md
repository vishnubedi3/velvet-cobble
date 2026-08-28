# Intervention Hierarchy (Levels 0–6)

**Purpose.** Guarantee that artifact reduction is minimal and causal: the skill
never rewrites every passage, never escalates without evidence, and never
prefers a bigger edit when a smaller one removes the cause.

## 1. The levels

### Level 0 — No intervention
The finding is recorded and preserved as-is.
**Applies when:** the flagged pattern is (a) a contractual genre element,
(b) an authorial device, (c) Low/Folklore confidence, (d) the only fix
available would damage any preservation dimension, or (e) the pattern's
function test (taxonomy/20 §20.2) passes.
**Rule.** Level 0 is the default. The skill's bias is toward *not* editing.

### Level 1 — Remove redundant wording
Delete or simplify redundant words, phrases, and repetitions within a
sentence or short span. No information, structure, or voice change.
**Applies to:** P06 signposts, D07 redundant tags, E02 duplicate layers,
FS03 glosses, U02/U04 duplicate interpretations, L02/L08 repeats, P04 rhythm
via punctuation only (splitting/joining without rephrasing).
**Constraint.** The edit must not change any fact, beat, or tone. If
deletion would leave a beat unreadable, Level 1 is insufficient by
definition.

### Level 2 — Reduce unnecessary exposition
Remove or condense redundant *explanatory* passages — narration that
duplicates what scenes, behavior, or dialogue already carry.
**Applies to:** N02/U03 theme statements whose carriers exist; W01
exposition blocks whose information is unused; S06 functionless description;
C01/E01 redundant emotion layers; recaps (L08).
**Constraint.** Exposition is "unnecessary" only if the function test
confirms the carriers do the work (frameworks/05 §3 vacancy check). If the
carriers are weak, Level 2 is not permitted — the correct level is 5/6
(fix the scene) or Level 0.

### Level 3 — Improve dialogue differentiation / local specificity
Re-voice or re-specificize *local* passages without touching structure:
per-character voice (D04, C03, H03), specificity repairs (P01, S03, W05),
rhythm variation within an exchange (D01/D05/D06), implication conversion
(U01, D03), consequence carry-forward (A03, R03).
**Applies to:** voice/register/specificity tells whose fix is local.
**Constraint.** Re-voicing is bound to the character's voice profile
(frameworks/02 §3); implication must pass the decodability rule
(frameworks/03 §3); no plot fact may move or vanish (PV-9).

### Level 4 — Correct repetitive narrative structures
Vary *repeating* structural patterns: scene skeletons (SC05, L03),
conflict-cycle type (N05, F01), button saturation (T03/SC04), ledger
rigidity (N03/FS02), arc smoothing (N08), milestone ladders (R02), theme
saturation (V04, N01), quiet-scene absence (T04).
**Applies to:** structural tells — and *only* when the repetition is
measured (ledger/cluster evidence), not suspected.
**Constraint.** Requires: (a) the repetition evidence; (b) proof that
Levels 1–3 can't remove the cause (repetition is not a wording problem);
(c) causality audit (frameworks/05 §4); (d) genre gate (frameworks/07);
(e) for worldview-touching changes (N07, F03, E05): author consent.

### Level 5 — Reconstruct affected sentences or paragraphs
Rewrite a bounded passage (≤ a few sentences / one paragraph) whose
problem cannot be fixed by deletion, substitution, or local variation —
e.g., a paragraph whose rhythm contradicts its content (P04), a beat that
must be *enacted* rather than stated (E01 when the enactment needs new
material), a description that must be re-perceived (S06).
**Constraint.** The rewrite must be justified sentence-by-sentence in the
intervention record: what was preserved, what changed, why smaller levels
failed. The passage's information content is invariant (PV-9).

### Level 6 — Reconstruct a scene (or larger unit)
Rebuild a scene whose *structure* fails — theme-carrier absence (N01/N02
vacancy), climax compression (T02), sanitized stakes (F05), missing
consequence (A03 at scene scale).
**Constraint.** Only when the analysis demonstrates that Levels 1–5 cannot
solve the problem *and* the scene's function (frameworks/04 §7) is
re-served by the reconstruction. Author consent required.

## 2. Escalation rules

1. **Start at the lowest plausible level for the cause.** The mapping
   tell→level above is a *ceiling*, not a target.
2. **Never escalate without evidence of insufficiency.** An escalation must
   cite: (a) what was attempted at the lower level, (b) why it failed
   (function still absent / cause still present), (c) what the higher level
   will do differently.
3. **One pass per level, whole draft per pass.** Apply all Level-1 fixes
   draft-wide, re-analyze, then Level-2, etc. This ordering prevents
   over-editing: many "Level-4-looking" problems disappear once Levels 1–3
   remove the redundancy that was making structure visible.
4. **Level 0 re-check after every level.** Fixes change the text; a
   preserved pattern may now be redundant (re-flag) or a fixed one may
   reveal authorial intent (revert).
5. **Structural edits are batch-gated.** All Level ≥4 proposals are
   collected and reviewed together (they interact through the causal chain)
   before any is applied.

## 3. Anti-mechanical guardrails

- **No transformation quotas.** The skill has no target number of edits; a
  clean draft yields Level 0.
- **No style enforcement.** The hierarchy removes *causes of artifacts*,
  never imposes a style ("more literary," "more concrete") on passages that
  pass the function test.
- **No detector feedback.** Detector scores are never an escalation
  criterion (S12–S14, S35).
- **No word-list substitutions.** Synonym replacement is not an intervention
  level; specificity edits cite story-model facts as their source.

## 4. Logging

Every applied edit is logged with: level, tell ID(s), passage span, cause
(K-code), the function test result, the preservation check results
(interventions/02), and the re-evaluation outcome (improved / unchanged /
reverted). The log is part of the skill's output (schema:
`../schemas/intervention-request.schema.json`).
