# Framework 02 — Character Analysis Framework

**Purpose.** Extract and verify a character model from the draft, detect
character-level tells (taxonomy/03), and supply the per-character information
the intervention system needs so that edits cannot damage character integrity.

**Feeds.** The story model (`../interventions/03-story-model.md`) — the character
analysis is one of its components. **Sources:** S04, S06, S07, S29, S42, S49.

## 1. Character model extraction

For each named character, extract a **CharacterRecord**:

| Field | Contents | How extracted |
|---|---|---|
| `id`, `name` | identity | direct |
| `role` | protagonist/antagonist/secondary/utility | function in plot |
| `goals` | wanted things, with priority order | scenes where the character *chooses* |
| `values` | principles actually cost something when kept | decision points |
| `knowledge` | what the character knows at each chapter (for information-audit) | dialogue + interiority |
| `voice_profile` | vocabulary range, sentence length, hedging, formality, verbal habits, humor profile | all speech/interiority by that character (see §3) |
| `blind_spots` | what the character is wrong about | contradiction between stated and shown |
| `relationships` | per other character: history, power, what each wants from the other | interaction scenes |
| `history` | backstory *as established in the text* | flashbacks + exposition |
| `demographic_markers` | how the text marks (or doesn't) gender/race/etc. | for the stereotype audit (§4) |
| `arc` | trait-state at act boundaries | change detection |

## 2. Character-level tell detection

Map to taxonomy/03:

| Tell | Detector |
|---|---|
| C01 emotion labeling | emotion-lexicon + "felt/realized/as"-cause patterns adjacent to behavior; redundancy check against enacted beats |
| C02 instant backstory | backstory-position vs. the behavior it explains (adjacent = flag) |
| C03 uniform interiority | cross-character voice-profile similarity (embeddings + features); all-articulate check |
| C04 measured reactions | reaction-appropriateness deviation from *the character's own profile* (not from a norm) |
| C05 polite conflict | hedge density in confrontations; cooperative-frame adoption rate |
| C06 hyper-consistency | trait-behavior entailment violations = 0 across the draft (and no temptation/compromise beats) |
| C07 stereotypes | §4 audit |
| C08 theme vehicles | function audit: can the character be described without naming their thematic role? |

## 3. Voice profile (feeds D04, C03, H03 interventions)

Build per-character features from their *own* utterances and interiority only:
- **Lexical:** content-word favorites; taboo words (never/always used); register.
- **Syntactic:** mean sentence length + variance; fragment use; question use;
  hedge density.
- **Pragmatic:** how they ask, evade, concede, interrupt; humor type or none.
- **Cognitive:** what they notice (concrete/abstract; people/objects);
  planning horizon; self-awareness level.

The tell D04 = low inter-character distance on these features. The
intervention (Level 3) re-voices *only* utterances that violate their own
speaker's profile, toward the profile — never toward a generic "quirky" target.

## 4. Stereotype audit (C07 — the one High-confidence character tell)

Run the Marked Personas–style comparison (S07) on the draft's own characters:

1. List characters and their demographic markers.
2. Extract appearance/family/power/agency word associations per character
   (Lucy & Bamman's dependency method, S06).
3. Compare: are marked characters systematically associated with
   appearance/family while unmarked ones get agency/intellect?
4. Check "positive stereotyping" (S07: stereotypes hide in positive framing —
   exoticizing, essentializing).
5. Output: per-character stereotype-risk flags with quoted evidence.

Remediation (Level 3–5) = **individuation**, not trait-swapping: re-derive the
character from a specific life (job, habit, history, priorities) so the
demographic template stops being the generator's only information source.

## 5. Character integrity checks (used by the preservation gate)

Every proposed edit touching a character is checked against:
- the character's goals/values (does the edit make them act against
  themselves without motivation?);
- their knowledge (does the edit leak information they shouldn't have?);
- their voice profile (does the edit break their register?);
- their relationships (does the edit erase established history?);
- their arc state (does the edit jump a stage?).

See `../interventions/02-preservation-constraints.md` (PV-2, PV-3) for the
binding version of these checks.

## 5a. Faction-portrayal integrity (project check — feeds PST-05)

In this project, characters are embedded in **canon-documented factions**
(houses, clans, the matha's wings and factions, the social factions), and
an unacceptable faction portrayal is defined *by canon*, not by taste: a
faction rendered as a single-minded bloc ("the temple decreed", "the clans
agreed") erases the documented fault lines that are the story's engine.
The character layer therefore audits collective-attribution verbs and
intra-faction disagreement against the faction's canon entry
(`../taxonomy/19-project-tells.md` PST-05; authority
`project_canonical`). Fixes re-attribute actions to the documented
sub-faction, house, office, or faction interest — never to a generic
dissenter. The flip side is protected by the intentionality check: a
faction *character* voicing its bloc's official line is characterization,
not a monolith tell; the tell is the *narration* collapsing the faction.

## 6. False-positive notes

- Articulate characters exist (a professor should be articulate); C03 flags
  *uniformity*, not articulacy.
- Consistency is craft (C06 flags consistency-with-nothing-else).
- Persona drift in long text is L01, not a short-form tell — run the long-form
  framework for drafts > ~10k words.
