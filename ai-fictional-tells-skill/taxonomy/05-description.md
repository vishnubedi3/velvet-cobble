# Taxonomy 05 — Description-Level Tells

**Sources for this cluster:** S03, S04, S10, S37, S41, S44, S53.
**Dominant causes:** K4 (template description), K1 (generic vocabulary), K2 (no perceptual grounding), K3 (mood-signaling clarity).

---

## S01 — Atmosphere-first setting blocks at scene open

- **Definition.** Scenes open with a self-contained atmospheric paragraph that
  establishes place and mood before any character action — the "establishing shot"
  default.
- **Example pattern.** "The rain fell in silver sheets over the sleeping city. Neon
  signs flickered…" (two more mood sentences) before anyone does anything.
- **Observable characteristics.** Location+mood in the first 1–3 sentences of most
  scenes; description exists before anyone perceives it.
- **Evidence.** Practitioner-strong (S44; S53 — AI-assisted authors reportedly
  delegate exactly this: "the boring parts like description and setting"); TTCW
  scene-vs-exposition gap (S04: 50.0 vs 91.7). Confidence: **Medium**.
- **Likely cause.** K4: template scene structure ("set the scene first") + K1
  (atmosphere vocabulary is high-probability prose).
- **Variation.** Genre: strongest in fantasy/romance; weakest in dialogue-led
  fiction. Perspective: strongest in omniscient; weaker in close first person
  (but still present).
- **Severity.** 2. **False-positive risk.** 2 — establishing shots are legitimate
  craft, especially in SFF; the tell is the *unvarying* default + mood-first order.
- **Effect on quality.** Every scene starts the same way; the reader is told the mood
  instead of discovering it through action.
- **Recommended mitigation.** Level 3–4: re-anchor the opening in the POV character —
  perception, need, or action first; fold the atmosphere into what the character
  notices (S06). Keep deliberate establishing shots when they serve rhythm (e.g.,
  after a cliffhanger, as a breath).
- **Side effects.** Deleting scene-setting wholesale leaves ungrounded scenes.
- **Validation.** Count scene-open types across the draft; the fix is variance +
  function, not deletion.

## S02 — Sensory checklist triads

- **Definition.** Description proceeds through the senses by rote — sight, then
  sound, then smell/touch — as if completing a rubric.
- **Example pattern.** "The bakery smelled of cinnamon. Somewhere a bell chimed. The
  counter was warm under her palm." (three senses, one each, in order).
- **Observable characteristics.** Multi-sense coverage per description block with
  uniform distribution; sense words clustering at regular positions.
- **Evidence.** Practitioner-strong (S44); mechanism K4 (scenes summarized into
  sensory lists in training); no direct measurement. Confidence: **Medium**.
- **Likely cause.** K4: the corpus's scene summaries enumerate senses; the model
  reproduces the enumeration.
- **Variation.** Genre: strongest in romance/literary; weakest in minimal styles.
- **Severity.** 2. **False-positive risk.** 1.
- **Effect on quality.** Perception becomes inventory; the reader's sensorium is
  managed instead of engaged.
- **Recommended mitigation.** Level 2: keep the one sense that matters to the
  character in the moment; cut the completists. Level 3: chain perception to action
  (smell noticed *because* of the act).
- **Side effects.** Sensory-richness loss where immersion needs it.
- **Validation.** For each sense-mention: whose perception is it and why now?

## S03 — Generic sensory vocabulary

- **Definition.** Atmosphere rendered in the corpus's most common sensory words —
  soft light, gentle hum, distant murmur, crisp air — with no specific referents.
- **Example pattern.** "Soft light filtered through the window, and the gentle hum of
  the city drifted in."
- **Observable characteristics.** Modal-average adjectives (S10 mechanism); no
  concrete objects; light/hum/breeze clichés.
- **Evidence.** S10/S11 mechanism (High, Tier 2) + practitioner (S44). Confidence:
  **Medium**.
- **Likely cause.** K1: these are the highest-probability sensory continuations;
  K5 amplifies.
- **Variation.** Genre: all; strongest in romance/fantasy.
- **Severity.** 2. **False-positive risk.** 2 — quiet domestic scenes legitimately
  use quiet words; the tell is *unspecific* quiet words (which light? which hum?).
- **Effect on quality.** Settings become interchangeable; the story could happen
  anywhere (twin of W05).
- **Recommended mitigation.** Level 1–2: replace with the *specific* instance (the
  fluorescent tube's buzz, the particular window) from story-model world facts. This
  is P01 applied to description.
- **Side effects.** Over-specificity (brand-name cataloguing) is a different failure.
- **Validation.** Does the revised description identify *this* place, not any place?

## S04 — Mood-signaling environment/weather

- **Definition.** Environment mirrors and announces emotion — rain for grief, dawn
  for hope — the pathetic fallacy used as automatic mood caption.
- **Example pattern.** The moment she decides to leave, the storm breaks.
- **Observable characteristics.** Weather/emotion co-occurrence at beat boundaries;
  environment changing exactly when interior states change.
- **Evidence.** Practitioner (S44); mechanism K4; S03's "no local specificity" is the
  adjacent finding. Confidence: **Medium** (I'd flag Low-Medium; monitored — see below).
- **Likely cause.** K4: the pathetic fallacy is a canonical taught device and a
  template default.
- **Variation.** Genre: strongest in romance/literary; ironic counter-use (sunshine
  for horror) is rare in generated text.
- **Severity.** 1. **False-positive risk.** 3 — the pathetic fallacy is a respected
  device; it is only a tell by frequency and automaticity.
- **Effect on quality.** At frequency, the device reads as machinery; emotion is
  double-coded.
- **Recommended mitigation.** Level 2 only at high frequency: remove or *invert* one
  instance. Inversion must be authored, not randomized.
- **Side effects.** Over-inversion becomes its own tic.
- **Validation.** Frequency count vs. genre baseline.

> **Project override (this repository).** S04's normal treatment (soft,
> frequency-gated, FPR-3) is **superseded here**: mood-weather is banned
> outright as **PST-03** (`../19-project-tells.md`), because in this
> project's world the weather is structural — the wind law is calendar,
> agriculture, military season, and famine engine (`samur/02-canon/GEO-03`).
> Findings route as PST-03 with `authority: project_canonical`, and the
> fix loads the weather with its canonical function rather than merely
> deleting the mirror.

## S05 — Camera-movement visual framing

- **Definition.** Narration moves like a camera — panning across the room, tracking
  gazes ("her eyes moved to the window"), framing shots — instead of following a
  perceiving mind.
- **Example pattern.** "His gaze fell on the letter. It swept the room, past the
  empty chair, to the door." Repeated "eyes moved/fell/swept/traveled."
- **Observable characteristics.** Gaze verbs with object-of-gaze as grammatical
  subject; sequential visual inventory; AI news text shows a visual-description
  preference (S37).
- **Evidence.** S37 (Tier 1, visual-description preference), practitioner (S44).
  Confidence: **Medium**.
- **Likely cause.** K4: film-derived description templates dominate genre corpora;
  K2: no embodied perceiver to anchor the description.
- **Variation.** Genre: strongest in thriller/action; weakest in essayistic fiction.
- **Severity.** 2. **False-positive risk.** 2.
- **Effect on quality.** The prose watches the scene instead of living it; the POV
  character becomes a camera.
- **Recommended mitigation.** Level 2–3: re-root the same information in the
  character's noticing — attention has *reasons* (why does the gaze go there?), and
  adding the reason converts camera into perception.
- **Side effects.** Over-psychologizing every glance (→ C01).
- **Validation.** POV-consistency audit (frameworks/04 §Perspective filter).

## S06 — Description decoupled from POV purpose

- **Definition.** Description that serves no character, no story function, and no
  rhythm — included because scenes "need description" (the master-tell of this
  cluster; S01–S05 are its faces).
- **Example pattern.** A paragraph of furniture inventory in the middle of a
  confrontation; world detail narrated by a character who would never notice it.
- **Observable characteristics.** Description with zero downstream function; details
  that could be deleted without loss (the N03 twin at prose scale); S03's specificity
  gap (Beguš); S04's world-building gap (41.7 vs 94.4).
- **Evidence.** S03, S04 (Tier 0), S53 (delegated-description observation).
  Confidence: **Medium-High**.
- **Likely cause.** K4 (description as checklist item) + K2 (no perceiver).
- **Variation.** Genre: all; strongest in SFF. Perspective: worst in close POV.
- **Severity.** 3. **False-positive risk.** 2 — atmosphere *is* function in some
  fiction (the setting as character); check the work's own contract.
- **Effect on quality.** Dead weight; pace sinks; the reader skims.
- **Recommended mitigation.** Level 2: delete functionless blocks. Level 3: re-route
  surviving description through the POV character's purpose (what would they notice
  *for a reason*?).
- **Side effects.** Over-pruning atmosphere from atmospheric fiction.
- **Validation.** Function test per block: perception, mood-contrast, world-fact,
  rhythm, or cut.

## Monitored / folklore (not acted upon)

| Pattern | Status | Why |
|---|---|---|
| Personified inanimate objects ("the walls seemed to whisper") | Monitored | Common in genre fiction by humans too; frequency unmeasured |
| Describing the obvious ("she opened the door with her hand") | Monitored | Practitioner-common; overlaps S06/P01 |
| Adjective stacking | Monitored | Partial support (S41 content-word density); many styles stack deliberately |
| "As if" simile scaffolding | (documented) | See P05 |
