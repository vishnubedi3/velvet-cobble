# The Story Model (Structural Representation)

**Purpose.** The skill's representation of everything that must be preserved —
the substrate against which every proposed edit is checked for continuity and
character damage. It is *built from the draft* (never imposed on it), updated
after every applied edit, and carried in the analysis/intervention pipeline
state.

**JSON Schema:** `../schemas/story-model.schema.json`.

## 1. Components

### Characters (→ frameworks/02)
Per character: id, role, goals, values, knowledge-at-chapter, voice profile,
blind spots, relationships (with history, power, and wants per pair),
backstory-as-established, demographic markers, arc state at act boundaries.

### Setting & world (→ frameworks/04, /05)
Locations with their specificities; world-rule ledger (magic/tech/social
rules + costs); cultural anchors; the distinction between *established* rules
and open/unexplained corners (deliberate mystery is a feature — W02's
contract).

### Timeline
Event timestamps; durations; the causal event graph (A→B links); act
boundaries.

### Plot events
Event register with causes/consequences; setup/payoff ledger; conflict
register (type, participants, lifespan); thread inventory (open/closed).

### Narrative perspective & distance
POV mode per scene; narration contract (omniscient / close / unreliable);
distance policy (where the zoom changes, if anywhere); narrator quirks that
are *voice*, not artifacts (PV-4).

### Narrative voice baseline (→ frameworks/01 §2 Pass A)
5–8 voice signals observed in the draft — diction range, cadence, syntax
habits, tonal temperature, imagery domain, register shifts between modes —
each with an evidence span. This is the **positive inventory**: what every
intervention must leave intact (PV-4/PV-14) and what the final read checks
edited spans against (`../spec/05-pipeline.md` Stage 4b). Distinct from
per-character `voice_profile`s (frameworks/02 §3): the baseline describes the
narrator/author voice; the profiles describe speakers. Marked `unknown` for
drafts too short to show a baseline; never invented, never imported from a
style guide. Conflicts with a declared style anchor are reported to the
author, never adjudicated by the skill.

### Scene boundaries (→ frameworks/04)
Scene list with type, purpose, POV, state record (positions, objects,
injuries, mood), beat sequence, position in act.

### Emotional state
Per character at scene boundaries; the work's valence arc; deliberate
jaggedness markers (PV-9 protects these).

### Conflicts
Open/closed conflicts with lifespans and types (frameworks/05).

### Themes & motifs
Theme register with carriers; motif register with intended recurrence
patterns (variation/escalation) — distinguishes intended from accidental
repetition (L10 vs. V04).

### Foreshadowing
Plant/payoff ledger with positions and kinds (fair vs. signposted).

### Information state
Two ledgers: **reader-knows** (what the reader has been told, when) and
**character-knows** (per character, per chapter). PV-10 enforcement runs
here; L08 recaps and U01 implication conversions are checked here.

## 2. Construction & maintenance

1. **Build** the model during the analysis pass (frameworks 01–07), from
   the draft only. Fields not present in the draft are marked `unknown`
   (the skill must never *invent* continuity to fill gaps).
2. **Update** after every applied edit batch: changed spans are re-extracted
   and the model diffed. The diff itself is logged.
3. **Verify** before any Level ≥4 edit: the proposed change is simulated
   against the model (what would the model look like after the edit?) and
   any violated field yields a rejection with the specific field and
   evidence (preservation constraints §5).

## 3. How the model identifies damage

| Proposed edit | Model check | Example rejection |
|---|---|---|
| Re-voice a character's line (D04 fix) | voice profile distance | "Deviation from Mara's profile (fragments, no hedging) exceeds threshold; re-voice rejected" |
| Convert emotion statement to behavior (E01 fix) | emotional state at scene boundary + trajectory | "Enacted beat implies despair at scene 7, conflicting with established hope at scene 8 (PV-9)" |
| Delete a theme statement (N02 fix) | theme carrier map | "No carrier remains for theme 'grief as inheritance' (frameworks/05 vacancy check) — Level 2 insufficient; require Level 5 carrier scene or preserve" |
| Vary a scene skeleton (SC05 fix) | causal event graph + information ledgers | "Beat reorder leaks Maya's letter to the reader at chapter 2 (PV-10)" |
| Repair a contradiction (L04 fix) | fact ledger | "Changing the lighthouse keeper's name to 'Arne' contradicts chapter 5's letter (PV-1); correct repair is chapter 7's 'Anders'" |
| Cut a repeated description (L02 fix) | reader-information + motif register | "Passage is in the motif register (intended recurrence, varies) — preserve (L10 exemption)" |

## 4. The model is *descriptive*, not prescriptive

The story model records what the draft establishes. It contains no opinion
about what the story *should* be. All normative judgment lives in the
preservation constraints and the taxonomy's function tests; the model only
supplies the facts those judgments need. This separation is what allows the
skill to distinguish an intentional literary choice from an accidental model
artifact without imposing a style.
