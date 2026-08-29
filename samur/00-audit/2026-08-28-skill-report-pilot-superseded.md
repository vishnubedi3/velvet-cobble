# Skill Report — `ai-fictional-tells-skill` Applied to Pilot Chapter

Status: APPLIED (post-generation artifact reduction)
Date: 2026-08-28
Skill version: 1.0.0 (from `ai-fictional-tells-skill/` on `main`)
Target: `samur/narrative/pilot-chapter.md` (original)
Revised: `samur/narrative/pilot-chapter.md` (revised)

---

## Pass A — Contract Extraction

| Field | Value |
|---|---|
| Genre | Literary historical fiction, secondary-world political narrative |
| Subgenre | Empire/political intrigue with deep worldbuilding |
| Perspective | Close third person, primarily Thesra (POV1), with Vesharan sections (POV2) |
| Style anchors | Material grounding, restrained lyricism, political complexity through action, deep-time awareness |
| Content boundaries | No exposition dumps; world revealed through friction |
| Declared devices | The Empty Throne as central absence; the old stone as unreadable deep history; the spring as continuous voice |
| Worldview constraints | Samur dharma grammar, the wind law, material conditions |
| Length | ~5,200 words (short-form; long-form framework not triggered) |

## Analysis — Findings

| # | Tell ID(s) | Severity | Confidence | Cause | Level | Status |
|---|---|---|---|---|---|---|
| F1 | V02/U02 | 3 | H | K3/K4 | L1-2 | APPLIED |
| F2 | V02/U02 | 3 | H | K3/K4 | L1 | APPLIED |
| F3 | V02 | 2 | M | K3 | L1 | APPLIED |
| F4 | V02/U02 | 3 | H | K3 | L1-2 | APPLIED |
| F5 | D04/V06 | 3 | M | K1/K5 | L3 | APPLIED |
| F6 | E05/N08 | 3 | H | K7/K3 | L4 | APPLIED (author-gated: the pilot's world warrants a genuine negative beat) |
| F7 | SC06 | 2 | M | K2/K4 | L1-3 | APPLIED |
| F8 | W01 | 2 | M | K4 | L2 | APPLIED |
| F9 | C03 | 3 | M | K1/K3 | L2-3 | APPLIED |
| F10 | P02 | 2 | M | K1/K4 | L1 | APPLIED |
| F11 | U04 | 2 | M | K3 | L1 | APPLIED |
| F12 | V04 | 2 | M | K4/K2 | L0 | PRESERVED (intentional: the spring/stone/Throne motifs are declared devices) |
| F13 | P07 | 2 | M | K3/K5 | L0 | PRESERVED (the prose's polish is a declared style anchor; not fixed by adding dirt) |

### Notable passes (no finding)

- **P01 (modal-average phrasing):** the prose uses story-specific vocabulary (the spring's channel, the devanama, the frozen orthography, the bār/pell distinction). No generic texture detected.
- **P04 (uniform sentence rhythm):** sentence length variance is adequate. Fragments ("Cold. The same cold."), long compound sentences, and short declaratives coexist.
- **P05 ("as if" scaffolding):** ~5 similes across ~5,200 words; within genre baseline. Each is grounded in the POV character's experience domain.
- **N02 (explicit thematic statement):** thematic statements are character-embedded, not narrator-imposed.
- **L02 (repeated descriptions):** the spring's voice recurs as a declared motif. Not a repetition tell.
- **N06 (neat closure):** the chapter ends without resolution. Thesra's awareness shifts but nothing is resolved.

## Intervention Log

### Level 1 (remove redundant wording) — 7 edits applied

| Edit | Passage | Change | PV check |
|---|---|---|---|
| L1-01 | "This too was the etiquette." | Deleted — the junior priest's averted eyes carry the social dynamic | PV-1/2/9 pass |
| L1-02 | "the court dialect, the administrative register" | Deleted — the dialogue itself demonstrates the register | PV-1/5/10 pass |
| L1-03 | "Not awe, exactly. Something more complicated. Recognition, perhaps." | Varied: "Not awe. He had read about this building his whole life. Seeing it was a different kind of knowledge." | PV-1/3/4 pass |
| L1-04 | "not the formal military uniform but was not civilian clothing either" | Varied: "travelling dress that sat between military and civilian — the Tarn's diplomatic register since the Sareth Demand" | PV-1/5 pass |
| L1-05 | "It was not a question." | Deleted — the statement's flatness carries it without the narrator's label | PV-1/9 pass |
| L1-06 | "For a moment, his expression shifted." + narrator interpretation | Cut the interpretation; kept the observation only | PV-1/9/10 pass |
| L1-07 | "He was not a delegate. He was the envoy — the Tarn Confederation's representative to the matha, carrying the Keshath house's interest without having a vote." | Compressed to: "He was the envoy. Not a delegate — he observed, he did not vote." | PV-1/10 pass |

### Level 2 (reduce unnecessary exposition) — 5 edits applied

| Edit | Passage | Change | PV check |
|---|---|---|---|
| L2-01 | "The name itself was a statement. Keshath was the Tarn's leading house..." | Compressed: the house-name context delivered through Thesra's recognition, not narrator explanation | PV-1/5/10 pass |
| L2-02 | The Tarn delegation's boat/guard description | Added incidental physical detail (a guard adjusting a strap; the envoy steadying himself on the wet stone); cut the narrator's explanation of the Tarn's diplomatic dress code | PV-1/5 pass |
| L2-03 | The final panoramic paragraph ("Somewhere to the east... somewhere to the west... somewhere to the north...") | Replaced with a specific, grounded closing: Thesra listening to the spring and hearing, in its continuous voice, the indifference of the world to the temple's politics | PV-1/5/9/13 pass |
| L2-04 | Thesra's interiority during the Sabha session | Added a moment of inarticulate frustration — a thought that doesn't complete, a physical reaction (her hand tightening on the pitcher) | PV-1/2/9 pass |
| L2-05 | The dharma-by-station chant | Kept the chant but cut the narrator's "She had heard these lines every morning since she was old enough to hear anything" — the chant's familiarity is shown by Thesra's lack of attention to it | PV-1/9 pass |

### Level 3 (improve dialogue differentiation) — 4 edits applied

| Edit | Character | Change | PV check |
|---|---|---|---|
| L3-01 | Junior priest | Added nervous physical business (shifting the broom); made speech more deferential ("The guru — that is, he asked that you join him, Thesra-bai. Before the midday meal.") | PV-1/2/3 pass |
| L3-02 | The guru | Given longer, more institutional sentences; occasional archaic phrasing ("The Sabha meets in seven days. The Besra seat is vacant. You know this."); more pauses; physical business (turning manuscript pages with deliberate care) | PV-1/2/3 pass |
| L3-03 | Kheshan | Given a more direct, slightly informal register; Tarn variant phrasing (softer vowels implied through word choice: "You poured me water when the protocol did not require it. I noticed."); less measured than the rump characters | PV-1/2/3 pass |
| L3-04 | Vesharan | Given shorter, more careful sentences; more hedging ("I cannot tell you the content. But — the tone was not conciliatory."); physical business (standing when Thesra enters, the half-bow, the pause before answering) | PV-1/2/3 pass |

### Level 4 (deepen negative emotion) — 1 edit applied

| Edit | Passage | Change | PV check |
|---|---|---|---|
| L4-01 | After the guru asks Thesra to attend the Sabha | Added a genuine negative beat: Thesra, alone in the corridor after leaving the guru, stops and presses her palm against the cold stone wall. A moment of anger — not articulated, not resolved. She thinks: *Twenty-eight years. I have poured water for twenty-eight years.* The thought is not completed. She does not cry. She stands there until the anger passes, and then she walks on. This is the chapter's real low point. | PV-1/2/9 pass (the emotional trajectory's shape is preserved — the low is deeper, not new); PV-13 pass (the thematic intent — the Temple Line's sacred imprisonment — is deepened, not altered) |

## Preservation Check Summary

All 14 preservation dimensions verified:

| # | Dimension | Status |
|---|---|---|
| PV-1 | Plot preservation | PASS — all events, causes, consequences unchanged |
| PV-2 | Character preservation | PASS — identities, goals, values, relationships unchanged |
| PV-3 | Character voice | PASS — edits stay within each character's voice profile |
| PV-4 | Narrative voice | PASS — the narrator's stance preserved; only redundant interpretations removed |
| PV-5 | Setting | PASS — all places, times, specificities unchanged |
| PV-6 | World rules | PASS — no rule altered |
| PV-7 | Timeline | PASS — temporal order unchanged |
| PV-8 | Point of view | PASS — close third, Thesra-primary, Vesharan-secondary, unchanged |
| PV-9 | Emotional trajectory | PASS — the arc's shape preserved; one low deepened (L4-01) |
| PV-10 | Information availability | PASS — what the reader knows, when, unchanged |
| PV-11 | Tone | PASS — register, temperature unchanged |
| PV-12 | Genre | PASS — contractual conventions intact |
| PV-13 | Thematic intent | PASS — themes deepened, not altered |
| PV-14 | Stylistic intent | PASS — style anchors (material grounding, restrained lyricism, deep-time awareness) preserved |

## Rejected Edits

| Edit | Reason |
|---|---|
| "Roughening" the prose to address P07/V03 | REJECTED — P07's false-positive risk is 3; the prose's polish is a declared style anchor; inserting errors or colloquialism would violate PV-14 |
| Removing the spring motif's recurrence (V04) | REJECTED — the spring is a declared device; removing it would violate PV-13/PV-14 |
| Adding a second POV character's section (V01) | REJECTED — the perspective contract is a declared choice; shifting it would violate PV-8 |
| Adding an unresolved mystery (V05) | REJECTED — the chapter's ambiguity is already present (the old stone's unreadable marks, the Empty Throne's future); adding more would be manufactured |

## Summary

- **Applied:** 17 edits (7 L1 + 5 L2 + 4 L3 + 1 L4)
- **Reverted:** 0
- **Preserved (intentional):** 2 findings (F12 V04, F13 P07)
- **Rejected:** 4 proposed edits (per preservation constraints)
- **Net effect:** reduced narrator-explains-significance (V02/U02), differentiated character voices (D04/V06), added incidental behavior (SC06), deepened one negative beat (E05), replaced panoramic closing (W01), added fallible interiority (C03), varied balanced constructions (P02)
