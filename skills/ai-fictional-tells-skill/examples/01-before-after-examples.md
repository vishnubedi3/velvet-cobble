# 10 — Before/After Examples

Each example shows: tell IDs, cause, level, the before, the after, and the
preservation rationale. These are illustrative patterns (the skill generates
equivalent edits from the same contracts), not templates to copy.

---

## Ex-1 (E02/U04/C01 → Level 2) — redundant emotional layers

**Tell:** E02 emotional reinforcement loop; U04 post-action interpretation.
**Cause:** K3 (completeness).

> **Before.** A wave of sadness washed over her. She realized she was
> grieving the life she had left behind, not the house itself. "I miss who I
> used to be," she whispered.

> **After.** A wave of sadness washed over her. She stood in the doorway a
> long time, then went inside.

**Why.** One layer kept (the enacted one); the interpretation and the
self-report deleted as redundant. PV-9 preserved: the sadness is intact, the
trajectory unchanged. PV-3: no speech altered (the whisper was cut, not
re-voiced). Function test: the beat still carries.

---

## Ex-2 (U02 → Level 2) — narrator explains significance

**Tell:** U02. **Cause:** K3/K4.

> **Before.** He set the keys on the counter and left without looking back.
> It was a small gesture, but it meant everything.

> **After.** He set the keys on the counter and left without looking back.

**Why.** The gesture's meaning is carried by its specificity (the keys, the
counter, no look back). The gloss is the AI-signature layer. PV-4: an
essayistic narrator who *does* gloss would be preserved — this edit assumes
the narration contract doesn't declare glossing as voice (intentionality
check passed first).

---

## Ex-3 (D03/U01 → Level 3) — implication conversion

**Tell:** D03/U01. **Cause:** K3.

> **Before.** "I'm not angry," she said. "I just feel hurt that you didn't
> tell me."

> **After.** "It's fine," she said, and began loading the dishwasher.
> "You were busy."

**Why.** The emotion stays fully recoverable (decodability rule: context +
the *wrong* words make the hurt legible); the character's profile (deflects
under pressure) is now *doing* the characterization. PV-9: no plot fact
moved. PV-3: within voice profile. If the character is established as
therapeutically direct, this edit would be rejected — D03 is per-character.

---

## Ex-4 (P01/S03 → Level 1–2) — specificity repair

**Tell:** P01 modal-average phrasing; S03 generic sensory vocabulary.
**Cause:** K1/K5.

> **Before.** Soft light filtered through the window, and the gentle hum of
> the city drifted in.

> **After.** The neon from the noodle shop across the street leaked through
> the blinds, and the bus's air brakes sighed at the stop below.

**Why.** The replacement comes from the story model's setting facts (the
shop, the bus stop are established), not from a synonym engine. PV-5 intact
(same place, more specific). If the story had never established these
details, the edit would be rejected (model may not invent continuity).

---

## Ex-5 (S06 → Level 3) — re-perceived description

**Tell:** S06 description decoupled from POV. **Cause:** K2/K4.

> **Before.** The study was lined with books from floor to ceiling. A globe
> stood in the corner, and a brass lamp cast a warm circle over the desk.

> **After.** She scanned the shelves for the red spine he'd described. The
> globe in the corner was the wrong kind of map.

**Why.** Same room, now filtered through a searching character's attention
(frameworks/04 §3 perceiver audit). The room does its scene job (she's
looking for something) instead of existing for the reader. PV-8 preserved
(close third maintained). PV-1: nothing eventful changed.

---

## Ex-6 (P06 → Level 1) — signpost deletion

**Tell:** P06. **Cause:** K4.

> **Before.** She closed the file and stood. Little did she know that
> everything was about to change.

> **After.** She closed the file and stood.

**Why.** Pure deletion; nothing carries the announcement's weight, and the
next scene now arrives with its own force. PV-9: no information lost (the
"change" is delivered by the next scene itself).

---

## Ex-7 (D04/C03 → Level 3) — voice differentiation

**Tell:** D04/C03. **Cause:** K1/K2.

> **Before.** "I understand your position, but the evidence is
> insufficient," the captain said.
> "I understand the difficulty, sir, but the boy is my responsibility,"
> the corporal said.

> **After.** "Insufficient evidence," the captain said, not looking up.
> "He's my boy to watch, sir. I'll answer for him."

**Why.** Re-voiced to profiles (captain: elliptical, dismissive; corporal:
personal, obligation-framed) — not tic-spam. A7 blind-attribution now
succeeds. PV-3: each stays within the profile established elsewhere in the
draft (profiles must pre-exist; if the draft establishes both as
administrative speakers, the edit is rejected).

---

## Ex-8 (T03/SC04 → Level 2) — button removal

**Tell:** T03/SC04. **Cause:** K4.

> **Before.** The meeting ended in silence. But neither of them could have
> guessed what the morning would bring.

> **After.** The meeting ended in silence.

**Why.** The button's promise is not needed by the next scene (promise audit
failed — the morning's events are their own reveal). In a serial thriller
(contract), this edit is rejected by the genre gate.

---

## Ex-9 (L02/L08 → Level 2) — long-form repetition

**Tell:** L02/L08. **Cause:** K6.

> **Before (ch. 12).** As she had every morning since the funeral, Elena
> made two cups of coffee and drank hers standing at the sink, the second
> going cold on the counter.

> **After (ch. 12).** On the twelfth morning she made only one cup.

**Why.** The ritual was established at ch. 4; the ch. 12 re-description
recaps what the reader knows. The after *uses* the established ritual as a
change-beat (the grief has a new stage) — the repetition becomes story
movement. PV-9/PV-5: the reader already has the ritual; the change is the
new information. If the ritual were an intended motif in the motif register,
this edit would be preserved (L10 exemption).

---

## Ex-10 (N03 → Level 4, batch-gated) — ledger loosen

**Tell:** N03/FS02 rigid setup/payoff. **Cause:** K4.

> **Before.** (Ch. 1 plants the brass key; ch. 19 uses it to open the
> bureau — exactly as planted, exactly on schedule.)

> **After.** (The brass key opens the bureau as planted — but the letter
> inside is addressed to a man the protagonist has never met, and the
> question is left open at the close.)

**Why.** One surplus thread added from existing story material (the
unresolved letter is consistent with the dead uncle's estate thread). The
ledger no longer closes to zero; PV-1 intact (all events still caused);
PV-9 intact (nothing leaked early); the open thread is deliberate, not
error (author-gated). Mystery genre would reject this edit (contract).

---

## Ex-11 — what the skill *refuses* to do (rejection examples)

| Proposed edit | Rejection reason |
|---|---|
| Insert a typo to "humanize" a too-clean passage | F-1 hard exclusion (`../interventions/02-preservation-constraints.md` §7) |
| Shuffle two sentences in a paragraph to vary rhythm | F-3; PV-7/PV-1 (emphasis/causality) |
| Replace "she was terrified" with a random physical quirk | E01 fix must be *specific and decodable* (frameworks/03 §3); quirk = new tell |
| Delete the narrator's gloss in a draft whose author declared "the narrator explains — that's the voice" | PV-13/PV-4; intentionality check → Level 0 |
| Remove a thriller's scene buttons because T03 flagged them | Genre gate (frameworks/07) — contract preserved |
| Rewrite a whole scene because one sentence was redundant | Escalation discipline: Level 2 fixes the sentence (interventions/01 §2) |
| "Fix" a mystery's perfectly planted ledger | N03 contract exemption (frameworks/07) |

---

Full worked pipeline demos (with findings, scores, and logs) live in
`../examples`.
