# Fiction-Writing Skill — Status

- **2026-08-26 audit finding:** no fiction-writing skill exists in this repository. The Phase 1 instruction assumed one; nothing was present to read, preserve, or organize.
- **This directory is a draft foundation, not an authoritative skill.**
- **Gate:** the narrative stage is **BLOCKED**. It opens only on an explicit, distinct system command, and only after this skill is complete and loaded.
- **If an authoritative skill is provided** (repository path, URL, or text): merge it into this directory, preserve its rules, reconcile — never blindly overwrite — with the draft anti-patterns, and record the merge in `samur/CHANGELOG.md`.

## Contents

- `anti-patterns.md` — draft rules for reducing AI-fiction patterns (DRAFT).

## Scope and dependencies

- This skill governs **narrative prose only**. It does not govern canon, research, or worldbuilding documents (those follow `PROJECT.md` §4).
- The skill depends on `samur/02-canon/` being the sole source of world facts during the narrative stage (pre-flight canon checks in `anti-patterns.md`).

## Relationship to `ai-fictional-tells-skill` (integrated 2026-08-26)

A complete, research-backed **post-generation** artifact-reduction skill —
`ai-fictional-tells-skill` (v1.0.0) — was uploaded to `main` at
`ai-fictional-tells-skill/`. It is the full detection + minimal-intervention
pipeline that this draft's "reduce AI-fiction patterns" goal gestures at. The two
are **complementary layers of the narrative stage**, not redundant:

- **This draft (`skills/fiction-writing/`)** = the **pre-generation** layer: the
  pre-flight **canon check** (names/institutions/places must come from the Samur
  canon) + the Samur-specific anti-pattern generation guard. It is **canon-aware,
  tell-agnostic**.
- **`ai-fictional-tells-skill`** = the **post-generation** layer: it detects AI
  tells in a generated draft and applies minimal, preservation-checked edits. It
  is **canon-agnostic, tell-aware** (its PV-5/PV-6 preservation protects setting
  and world rules, but it does not validate canon-compliance).

Full integration record — purpose, stage, inputs/outputs, dependencies,
invocation, storage, limitations, and canon effect — is in
[`skills/INTEGRATION.md`](INTEGRATION.md). The narrative stage remains
**BLOCKED**; neither layer is invoked until a distinct system command authorizes
it. When it does, this draft runs **before** generation (canon guard) and the
tell-reduction skill runs **after** generation (artifact reduction).
