# Framework 03 — Dialogue Analysis Framework

**Purpose.** Detect dialogue-level tells (taxonomy/04), extract conversation
structure, and supply what interventions need to vary rhythm and re-voice
speakers without breaking meaning or characterization.

**Sources:** S02, S04, S28, S29, S37, S38, S39, S49.

## 1. Scene-level conversation extraction

For each dialogue passage, extract:
- **speakers** and their voice profiles (frameworks/02 §3);
- **turn list** with length, completeness, and hedges per turn;
- **topic graph** (what each turn addresses; where topics are dropped,
  evaded, or answered);
- **information ledger** per utterance: what each speaker *knows*, *learns*,
  and *states* (feeds the as-you-know detector and the knowledge-preservation
  checks);
- **conflict state** (cooperative / contested / ruptured) per exchange.

## 2. Dialogue tell detection

| Tell | Detector |
|---|---|
| D01 symmetric turn-taking | turn-length variance ≈ 0; interruption count = 0; unanswered-question count = 0 across unlike scenes |
| D02 as-you-know exposition | utterance-information redundant to *both* speakers' knowledge ledgers ("as you know", "remember when", recaps of shared history) |
| D03 over-explicit emotional speech | "I feel X because Y" density; emotion-word + cause in single turns; zero implicature in emotionally loaded exchanges |
| D04 uniform idiolect | inter-speaker voice-profile distance below threshold (frameworks/02 §3 features). **Project check first (PST-08):** in this project the language map (`samur/02-canon/CUL-02`) defines *legitimate* register differences across speakers — core / Sareth frontier / delta pidgin / Tarn varieties / Veth coastal / Khoric-marked Samur / Voren-interpreted scenes. A D04 finding must be measured within a language, never across the map: cross-language difference is canon texture, not uniformity; *missing* difference where the map requires one is PST-08. |
| D05 over-complete grammar | fragment/ellipsis rate ≈ 0 across all speakers |
| D06 hedged politeness | hedge density in contested turns; acknowledgment-first rate; de-escalation rate |
| D07 explanatory tags | tag-with-interpretation density ("said, voice laced with…"); tag-restates-line redundancy |

## 3. The implicature model (for U01/D03 fixes)

The skill uses a small pragmatic machinery, grounded in S38 (models *can*
decode implicature) and S39 (models over-produce literal meaning):

- **Decodability rule.** An implication may replace an explicit statement only
  if the reader can recover the intended meaning from context + world knowledge
  (test via a paraphrase probe: an independent reader-model must produce the
  intended meaning from the implied version).
- **Character-tactics rule.** The implied form must match the speaker's
  tactics profile (some characters *should* be blunt — U01 is per-character,
  never global).
- **Risk rule.** Implication adds ambiguity; the fix is rejected if the scene
  loses a plot-critical fact (preservation gate PV-9: information
  availability).

## 4. Rhythm variation (for D01/D05/D06 fixes)

The intervention target is *rhythm with meaning*, never randomization:

- **Interruption** encodes power or urgency (higher-status speaker cuts in).
- **Unanswered question** encodes evasion or hierarchy.
- **Ellipsis** encodes intimacy or economy (established speakers skip shared
  ground).
- **Hedge** encodes deference or manipulation (deliberate hedging is a tactic,
  not a tell — D06 flags *uniform* hedging).
- **Silence/beat** encodes weight (a pause before an answer changes it).

Each variation is chosen from the scene's power/goal structure (story model
relationship register), documented in the intervention record, and verified
for decodability (§3).

## 5. Humor beats (for H01–H04 fixes)

- **Stock-joke test.** Transplant test: if the joke works unchanged with the
  names swapped, it's stock (H01) — rebuild from story-local material (the
  world's rules, the characters' blind spots, the scene's specifics).
- **Explanation test.** Any gloss after a comic beat flags H02 — delete the
  gloss, not the beat.
- **Humor-profile test.** Each character's humor type (or absence) must be in
  their voice profile; uniform wit flags H03 — re-voice to profile. The
  *unfunny* character is preserved as unfunny (their seriousness is the joke).

## 6. Preservation checks (binding)

Every dialogue edit is checked against:
- **Knowledge integrity** (PV-9): no fact known only to one speaker may leak;
  no plot-critical information may be lost to implication.
- **Voice integrity** (PV-3): edits must stay within the speaker's profile.
- **Relationship integrity** (PV-2): rhythm changes must match the
  relationship's power/history structure.
- **Scene purpose** (PV-11): a scene whose job is information transfer may not
  be made subtextual past decodability.

## 7. False-positive notes

- Banter-heavy styles are symmetric by design (contract check first).
- Therapeutic registers (therapy scenes, close confidants) are legitimately
  explicit — D03 flags *habit*, not the register.
- "Said" purism is folklore; tag edits follow D07's redundancy test only.
