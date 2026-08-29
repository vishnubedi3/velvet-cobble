# Worked Example — Full Pipeline Demo (short story excerpt)

A compressed end-to-end run on a 900-word generated opening, showing the
pipeline's stages, evidence, decisions, and one rejection. Verbatim excerpts
are invented for the demo (not from any published work).

## Input

```json
{
  "draft": { "text": "<900-word generated story opening: a woman returns to her
    hometown after her mother's death; scenes: train, station, house>" },
  "metadata": { "generator": { "family": "generic", "decoding": { "temperature": 0.7 } },
                "prompt_class": "zero-shot", "language": "en", "length_words": 900 },
  "author_intent": { "genre": "literary", "subgenre": null,
    "perspective": "close-third, single POV (Elena)",
    "style_anchors": [], "declared_devices": ["the broken clock on the mantel is
    a deliberate motif"], "content_boundaries": [], "worldview_constraints": [] },
  "analysis_options": { "max_intervention_level": 3, "author_gate": true }
}
```

## Stage 1 — Analyze (findings, abridged)

| # | Tell | Span (abridged) | Evidence | Conf | Cause | Intentionality | Level |
|---|---|---|---|---|---|---|---|
| F1 | U02/E02 | "It was, she would later understand, the moment everything changed." | 1 of 2 significance-statements duplicating an enacted beat | Medium | K3 | accidental | 2 |
| F2 | E01 | "A wave of sadness washed over her. She realized she was grieving the life she'd left behind, not the house itself." | 3-layer emotion beat; behavior absent | Medium | K3/K4 | accidental | 2 |
| F3 | S06/S01 | "The rain fell in silver sheets over the sleeping town. Neon signs flickered…" (scene 1 open, no perceiver, no function beyond mood) | opening-type histogram: 3/3 scenes open atmosphere-first; 0 functional references | Medium | K4 | accidental | 3 |
| F4 | D03 | "'I feel hurt that you didn't tell me,' she said." | emotion+cause stated; speaker profile elsewhere deflects | Medium | K3 | accidental | 3 |
| F5 | L10? / intended | "The clock on the mantel had stopped at 4:07 again." (repeats 3×, varying) | **motif register: declared device** | — | — | deliberate | 0 |

## Stage 2 — Priority

F2 (sev 3 × conf 0.6 × fn-loss 1 − fpr 0.3) = 1.5 →
F1 (3×0.6×1−0.3) = 1.5 →
F4 (2×0.6×1−0.3) = 0.9 → below threshold 1.2 → **Observation** (reported, not edited — a
single over-explicit line in a 900-word draft doesn't clear the bar, and the
speaker's profile makes it marginal).
F3 (2×0.6×1−0.3) = 0.9 → Observation. F5 → Observation (intentional).

Queue: [F1, F2]. Two edits, both Level 2. Max level option (3) never used.

## Stage 3 — Edits

**F1 → Level 2 (delete significance-statement).**
Before: `It was, she would later understand, the moment everything changed.`
After: *(span removed; following paragraph now carries the transition.)*
Preservation: all 14 pass. Re-eval: fixed (U02 detector clean on span).

**F2 → Level 2 (keep one layer).**
Before: `A wave of sadness washed over her. She realized she was grieving the
life she had left behind, not the house itself.`
After: `A wave of sadness washed over her.` *(the enacted layer follows in the
next paragraph — the doorway hesitation — and now does the work alone.)*
Preservation: all pass; PV-9 verified (sadness intact, arc unchanged).
Re-eval: fixed.

**Rejected proposal (logged):** the queue also proposed converting the train
scene's mood-sentence into an implication about the inheritance. Rejected:
**PV-10** — the reader would learn of the will's existence two scenes early;
the letter is Elena's discovery beat.

## Stage 5 — Report excerpt

```
summary: { applied: 2, reverted: 0, preserved: 3, flagged_intentional: 1 }
what_changed: [
  "L2 · U02/E02 · 'It was, she would later understand…' — deleted the significance-statement; the following paragraph carries the transition",
  "L2 · E01 · 'She realized she was grieving…' — kept the enacted layer; cut the interpretation"
]
observations: [F3 (below threshold), F4 (below threshold), F5 (intentional motif)]
rejected: [PV-10 proposal]
revised_draft: <draft with 2 spans changed>
```

Final read (Stage 4b): FR-1 pass (both edited spans sit inside the draft's
voice baseline — sparse, declarative, low-adjective); FR-2 pass (two deletions
do not converge register); FR-3 pass (2 spans / 900 words); FR-4 pass; FR-5
pass (no new findings on re-analysis); FR-6 pass; FR-7 pass.

**What this demo shows:** the skill edited 2 sentences out of 900 words,
fixed two K3-cause artifacts, protected a declared motif, left marginal
findings alone, and rejected its own proposed edit on preservation grounds.
