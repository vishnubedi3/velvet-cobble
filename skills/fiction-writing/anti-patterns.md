# Anti-Pattern Rules (DRAFT)

Rules for reducing AI-fiction patterns in narrative output. Created 2026-08-26 as a **draft skeleton** because no skill existed in the repository. An authoritative skill, if provided, takes precedence; this file is then merged, not replaced.

## Prose tics

- Weather/light as mood shorthand at scene openings (banned unless functionally loaded).
- Tricolon overuse ("not X, not Y, but Z").
- "As if" similes more than once per page.
- Default adverb-verb crutches (slowly, gently, quietly as unexamined modifiers).
- Double-explained metaphor: the image plus a second sentence restating it.
- Recycled motifs (the same ash/bell/rain image reused across scenes).
- Em-dash/ellipsis dependence as substitute for voice.

## Structure and plot

- Coincidence as plot engine (right place, right person resolving tension). Allowed at most once per major arc, flagged in the scene plan.
- Convenient amnesia / conveniently forgotten facts to advance a scene.
- Symmetry addiction: matched twins of names, fates, or roles without causal reason.
- Exposition dumps: characters explaining shared knowledge; world information must arrive through friction (conflict, transaction, error).
- Elder-wisdom trope: every elder wise, every young person ignorant.
- Villain monologue; antagonists must have plans that do not depend on explaining them to the protagonist.
- Unearned resolution: tension released without cost, consequence, or lingering damage.
- Every conflict resolved within the scene that introduced it.

## Language and anachronism

- Modern vocabulary/idiom in dialogue or thought (per-era audit list to be built from `02-canon/CUL*`).
- Default "translationese" (stiff, parabolic dialogue) where a natural register is available.
- Uniform register: all characters sharing one rhythm and vocabulary class.

## World integration

- **Canon violation is fatal.** Before drafting, cross-check every referenced institution, place, name, and custom against `samur/02-canon/`; if absent or contradictory, file a QUESTION — do not improvise.
- Names come from canon name pools (to be defined in CUL files); no invented names without a pool entry.
- Narrative must not introduce new high-impact facts (geography, law, succession) — those are canon-level and go through the Phase 2/4 method.

## Pre-flight checklist (per scene/chapter, once the narrative stage is open)

1. Canon check: every named institution, place, and custom exists in `02-canon/`.
2. Coincidence audit: at most one, flagged.
3. Tic scan: weather-opening, tricolons, "as if" count, motif reuse.
4. Anachronism scan against the era vocabulary list.
5. Consequence ledger: does the scene end with a cost or constraint the next scene must inherit?
