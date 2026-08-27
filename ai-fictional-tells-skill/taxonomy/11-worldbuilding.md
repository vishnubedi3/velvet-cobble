# Taxonomy 11 — Worldbuilding Tells

**Sources for this cluster:** S03, S04, S28, S44.
**Dominant causes:** K4 (encyclopedic/template lore), K3 (complete explanations), K2 (no world-state model), K1 (generic detail).

---

## W01 — Encyclopedia exposition blocks

- **Definition.** World information delivered in undramatized paragraphs — history,
  systems, geography — that pause the story to brief the reader.
- **Example pattern.** Three paragraphs on the guild system the moment the guild is
  mentioned; the "lore dump" at first contact with any new element.
- **Observable characteristics.** Information-dense non-scenic paragraphs; TTCW
  scene-vs-exposition 50.0 vs 91.7 (S04); world-building score 41.7 vs 94.4 (S04).
- **Evidence.** S04 (Tier 0), practitioner (S44). Confidence: **Medium-High**.
- **Likely cause.** K4: encyclopedic text (wiki-style lore) is abundant in training;
  K3: completeness preference.
- **Variation.** Genre: strongest in SFF; weakest in contemporary realism (least
  lore to dump).
- **Severity.** 2. **False-positive risk.** 2 — SFF legitimately briefs readers;
  the tell is the *block*, not the information.
- **Effect on quality.** Pacing stalls (T02's fuel); the world is read, not
  inhabited.
- **Recommended mitigation.** Level 3–4: redistribute the information — through
  conflict (D02's conversion), through a character's need, or through implication;
  cut what the story never uses (Level 2).
- **Side effects.** Information starvation; readers lost in the world.
- **Validation.** Information-audit: when is each fact *used*, and could the reader
  infer it?

## W02 — Artificial completeness; over-explained systems

- **Definition.** Systems (magic, technology, economics) are fully specified and
  explained — rules, limits, costs — whether or not the story needs the spec.
- **Example pattern.** The magic system's five laws, stated and enforced; the
  currency's exchange rates; a world with no unexplained corners.
- **Observable characteristics.** System-spec density; explanations that exceed
  story use; S04 world-building gap.
- **Evidence.** S04 (Tier 0), practitioner (S44). Confidence: **Medium**.
- **Likely cause.** K3 (explain everything) + K4 (systems explained in training
  wikis) + K2 (no selective world-state).
- **Variation.** Genre: strongest in hard SF and systems-fantasy (where it is
  *partly* a genre contract — hard SF readers want the spec).
- **Severity.** 2. **False-positive risk.** 2.
- **Effect on quality.** The world becomes a rulebook; wonder and mystery die;
  every element is legible, so nothing is interesting.
- **Recommended mitigation.** Level 2: cut spec that no scene uses. Level 3:
  re-express one system through its *consequences* rather than its rules.
  Respect hard-SF contracts (PV-12).
- **Side effects.** Unexplained systems that feel arbitrary in hard SF.
- **Validation.** Use-audit: which rules does the plot actually invoke?

## W03 — Worldbuilding-as-creativity-signal

- **Definition.** Invented detail exists to demonstrate inventiveness — the story
  performs worldbuilding instead of using it.
- **Example pattern.** A lovingly described floating bazaar that no scene needs;
  five invented creatures where one would do; lore that never touches the plot.
- **Observable characteristics.** Detail whose only function is being fantastical;
  Beguš's lack of *local* specificity (S03: generic rather than grounded fantasy);
  Doshi's similarity finding (S16: AI "novelty" is uniform).
- **Evidence.** S03 (Tier 0), S16 (Tier 0), S04 (Tier 0). Confidence: **Medium**.
- **Likely cause.** K4: "creative" prompts and texts train detail-as-performance;
  K3 rewards visible effort.
- **Variation.** Genre: strongest in fantasy; weakest in minimal literary.
- **Severity.** 2. **False-positive risk.** 2 — decorative worldbuilding is a
  beloved tradition (Vance, Mieville); the tell is decoration *without texture*.
- **Effect on quality.** The world reads as a portfolio piece, not a place;
  details don't compound.
- **Recommended mitigation.** Level 2–3: connect one invented element to a
  character's daily use of it (the bazaar's *smell* at dawn for a vendor who works
  there); cut the rest. Specificity beats novelty.
- **Side effects.** Flattening genuinely decorative styles.
- **Validation.** For each invented element: does any character *use* it, or only
  the narrator?

## W04 — No lived-in messiness/illegibility

- **Definition.** The world is too legible: everything works as designed, nothing
  is broken, deprecated, contradictory, or locally irrational.
- **Example pattern.** The city's transit runs on time; the ancient temple's
  layout makes sense; no institution has legacy quirks.
- **Observable characteristics.** Absence of inconsistency-by-design; S03's
  uniformity; the model's own consistency bias (C06 at world scale).
- **Evidence.** S03 (Tier 0), mechanism K2. Confidence: **Medium**.
- **Likely cause.** K2: the generator maintains no world-state, so it can't hold
  *designed* inconsistencies — only uniform templates.
- **Variation.** Genre: strongest in SFF; weakest in satire (which templates make
  messy).
- **Severity.** 2. **False-positive risk.** 3 — legible worlds are a valid
  aesthetic; the tell is legibility *everywhere*.
- **Effect on quality.** The world feels constructed rather than inherited;
  history's grime is missing.
- **Recommended mitigation.** Level 4: introduce one designed inconsistency (a
  defunct law still enforced, a god nobody worships anymore) where it enriches the
  story. Author-gated.
- **Side effects.** Random contradictions read as errors, not texture.
- **Validation.** Distinguish designed from accidental inconsistency (frameworks/06
  distinguishes exactly this).

## W05 — Cultural/geographic nonspecificity

- **Definition.** Settings lack local specificity: places could be anywhere,
  cultures are generic, and the story's geography is interchangeable.
- **Example pattern.** A "market" with no cuisine, language, or economy; a
  "village" that could be in any country; Beguš: LLM stories "bereft of local and
  cultural specificity" (S03).
- **Observable characteristics.** Absence of place-anchoring detail; S03's direct
  finding.
- **Evidence.** S03 (Tier 0, direct). Confidence: **Medium-High**.
- **Likely cause.** K1: the most probable "place" description is the generic one;
  K4: training summaries strip local detail.
- **Variation.** Genre: strongest in realism/literary (where it's most damaging);
  weakest in SFF (which invents places anyway).
- **Severity.** 2. **False-positive risk.** 1.
- **Effect on quality.** Settings are stage flats; the fiction loses its texture
  and, for realism, its credibility.
- **Recommended mitigation.** Level 2–3: re-ground one location per scene in
  specific, story-model-anchored detail (what's *sold* there, what it *smells*
  like, what's in the gutter) — from world facts, not invented on the spot.
- **Side effects.** Detail-dumping (see S02).
- **Validation.** "Could this scene happen anywhere?" test.

## Monitored / folklore (not acted upon)

| Pattern | Status | Why |
|---|---|---|
| Generic invented terminology (X-crystal, Y-guild) | Monitored | Subsumed by W03/P01; naming is fixable at Level 1–2 |
| Uniform naming conventions | Folklore-adjacent | Unmeasured; plausibly a K1 artifact but low harm |
| Lore dumps | (documented) | W01 |
| Over-explained magic systems ("Sanderson-lite") | (documented) | W02 |
