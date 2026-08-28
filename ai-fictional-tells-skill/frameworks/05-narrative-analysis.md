# Framework 05 — Narrative Analysis Framework

**Purpose.** Detect narrative-level tells (taxonomy/02, /10, /12, /13), extract
the plot/tension/theme structure, and provide what structural interventions
need to vary beats without breaking causality.

**Sources:** S03, S04, S08, S16, S28, S29, S43.

## 1. Structure extraction

1. **Event register.** Extract plot events; link them causally (A→B where the
   text makes A cause B).
2. **Conflict register.** Per event: conflict type (physical / social /
   informational / internal), participants, lifespan (open→closed position).
3. **Theme register.** Candidate themes (from the prompt, repeated abstract
   vocabulary, and beat functions); for each theme, its carriers (scenes,
   objects, characters).
4. **Setup/payoff ledger.** Plants and their payoffs, with positions.
5. **Valence arc.** Sentiment trajectory (S08's hedonometer method, on any
   lexicon) plotted against the six human arc shapes as baseline reference —
   *not* as a target.

## 2. Narrative tell detection

| Tell | Detector |
|---|---|
| N01 story-as-argument | every scene's function reduces to theme-carrying; zero non-thematic events |
| N02/N03/U03 explicit theme | abstract-meaning statements near act boundaries; aphorism density |
| N03/FS02 ledger rigidity | setup/payoff ledger closes exactly; no surplus plants; payoffs at template positions |
| N04 default template | act boundaries at canonical positions; quest-shape detection |
| N05/F01/F04 conflict cycles | conflict-type histogram + lifespan distribution (repeated type = flag; minimal lifespans = F04) |
| N06 neat closure | resolution inventory == thread inventory |
| N07/F03 moral clarity | moral-remainder check: any unjust outcome? any comprehensible antagonist interest? |
| N08 valence smoothing | arc never falls below genre baseline depth; lows are brief and compensated |
| F02 artificial misunderstanding | conflict-causes audit: information asymmetries that one sentence would resolve |
| F05 sanitized conflict | consequence audit: costs stated vs. shown and persistent |

## 3. Theme audit (for N01/N02/V04/U03)

For each candidate theme:
- **Carrier map.** Which scenes/behaviors actually carry it (vs. which
  *state* it)?
- **Redundancy check.** Statements whose carrier-scenes already do the work →
  deletion candidates (Level 2).
- **Saturation check (V04).** Echo-count of the theme's imagery; saturation
  above the work's own baseline → prune the weakest echo (Level 4).
- **Vacancy check.** If statements are cut and *no* scene carries the theme,
  the fix is scene-level (Level 5–6), not re-adding the statement.

## 4. Causality audit (for F01/F02/F04 and any structural edit)

Before any beat is moved, inserted, or deleted:
1. Verify the causal chain still holds (every event has a cause and a
   consequence in the text).
2. Verify information flow (PV-9: no future knowledge leaks; nothing needed
   later is deleted).
3. Verify stakes integrity (PV-5/PV-8: the edit must not deflate the
   emotional trajectory).
Structural edits are logged with the causal chain they touched
(`../interventions/02-preservation-constraints.md` §Causality).

## 5. Structural variance library (for N01–N05, R02, FS02 remediation)

The skill offers *authored* structural options, never randomization:

| Fix | Option |
|---|---|
| N01/N04 default skeleton | non-thematic subplot; in-medias-res opening; delayed inciting event; asymmetric act weights |
| N03/FS02 rigid ledger | one surplus plant; one payoff through an unplanted route (exempt: mystery) |
| N05/F01 ladder | change conflict *kind* at one rung (physical→social→internal→informational) |
| N06 closure | one implied (not stated) resolution; one open thread (genre-gated) |
| N08 valence smoothing | one sustained negative beat; incomplete recovery (author-gated) |
| R02 milestone ladder | one off-ladder beat (plateau / backward step / parallel thread) |

Each option must pass the causality audit (§4) and the preservation gate.

## 6. Preservation checks (binding)

- Plot preservation (PV-1), emotional trajectory (PV-5), theme intent
  (PV-13), genre contract (PV-12), world rules (PV-6), information
  availability (PV-9) — see interventions/02.
- No structural edit may be made at Levels 0–3; structure changes start at
  Level 4 and require author consent for worldview-touching changes (N07/F03).

## 7. False-positive notes

- Tight, thematically coherent novels are a human tradition (V04 flags
  *over-coherence*, measured as echo saturation, not coherence itself).
- Mystery/romance contracts override N03/N06 flags (genre gate first).
- Valence arcs vary by genre — the baseline for "too positive" is the
  genre's own distribution, not the six-arc average.
