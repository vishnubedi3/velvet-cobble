# 2. Evidence Hierarchy

The taxonomy and the skill assign every empirical claim a **tier** and a **confidence**
so that implementers can distinguish genuine, evidence-backed fictional-generation
artifacts from internet folklore about "AI writing." These two scales are used
consistently across all documents.

## 2.1 Evidence tiers

### Tier 0 — Peer-reviewed, fiction-specific empirical studies
Studies that directly measure LLM **fiction** against human fiction (stories written by
both to the same prompts, expert-scored, or stylometrically compared). Tier 0 claims can
be asserted as established behavior.

| ID | Study |
|---|---|
| S02 | Stylometric comparisons of human vs AI creative writing (HSSC 2025) |
| S03 | Beguš, *Experimental Narratives: Human Crowdsourced vs AI Storytelling* (HSSC 2024) |
| S04 | Chakrabarty et al., *Art or Artifice?* TTCW expert evaluation (CHI 2024) |
| S06 | Lucy & Bamman, *Gender and Representation Bias in GPT-3 Generated Stories* (NUSE 2021) |
| S16 | Doshi & Hauser, *Generative AI enhances individual creativity but reduces collective diversity* (Science Advances 2024) |
| S28 | Villanova/JDM reader study of AI vs human short stories (2026) |
| S29 | CAspER character-portrayal comparison (ACL 2026) |
| S42 | GPT-WritingPrompts character-portrayal dataset (2024) |

### Tier 1 — Peer-reviewed empirical, adjacent text domains
Solidly measured but in domains other than fiction (essays, news, reviews, dialogue,
poetry, jokes). Admissible for fiction only where the mechanism plausibly transfers;
always labeled "adjacent-domain."

Examples: S01 (essays), S05 (jokes), S15 (conversation), S17–S19 (academic vocabulary),
S27 (poetry), S37 (news), S38–S39 (dialogue/pragmatics), S49 (persona dialogue).

### Tier 2 — Peer-reviewed systems/benchmarks/theory about generation
Results about generation mechanisms (decoding, long-context behavior, synthetic-data
collapse, detector limits). These ground the **causal model** (K1–K9) but do not by
themselves demonstrate a tell in fiction.

Examples: S09–S14, S20–S23, S30–S36.

### Tier 3 — Practitioner and editor evidence
Systematic observations by domain experts (editors with large submission streams,
professional writers, literary critics). Strong for *existence* of patterns; not
quantified; can over-index on low-effort spam rather than high-effort assisted work.
Always labeled "practitioner."

Examples: S44 (Clarkesworld data and process), S45 (Chiang), S53 (Counter Craft /
Lincoln Michel), S54 (No AI Slop practitioner pattern catalog — nonfiction patterns
adapted as detection procedures, never as word lists), craft literature (Saunders,
Wood, Le Guin, Burroway, Gardner — used only to define the *literary* side of the
comparison).

### Tier 4 — Internet folklore / unverified claims
Claims circulating without measurement (fiction "AI word lists," "AI never uses
contractions," "em-dashes are an AI tell"). Tier 4 items are **excluded** from the core
taxonomy. Where a Tier 4 item is partially supported (e.g., "not just X, but Y"
constructions were spontaneously named by readers in S28), it is documented as
"monitored" with its actual support level and a false-positive warning.

## 2.2 Confidence scale

| Level | Meaning | Evidential bar |
|---|---|---|
| **High** | Established behavior | Tier 0 or multiple Tier 1 studies, mechanism understood |
| **Medium** | Well-supported | Tier 0/1 study + consistent Tier 3 evidence, or Tier 2 mechanism + Tier 3 corroboration |
| **Low** | Plausible, unconfirmed | Only Tier 3, or Tier 2 mechanism without direct observation |
| **Folklore** | Unsupported | Tier 4; excluded from interventions |

Confidence is per-tell, not per-cluster. Two tells in the same file may carry different
confidence levels, and the taxonomy says so explicitly.

## 2.3 Rules of use

1. **Tier alone never justifies an intervention.** A Tier 0 finding justifies a
   *detector heuristic*; an intervention additionally requires (a) a causal explanation
   (K1–K9), (b) an identified instance in the actual text, and (c) passage of the
   preservation constraints (`../interventions/02-preservation-constraints.md`).
2. **Adjacent-domain transfer requires a mechanism argument.** "Fewer epistemic markers
   in essays" (S01) transfers to fiction as "over-assertive narration" only via the
   shared K1/K3 mechanism — which is why the taxonomy records both the source and the
   transfer argument.
3. **Confidence gates escalation.** Level ≥4 interventions (sentence/scene
   reconstruction) require at least Medium confidence in the tell and explicit evidence
   that lower levels were insufficient.
4. **When evidence conflicts, the fiction-specific Tier 0 result wins.** E.g., humans
   cannot distinguish AI stories (S28) does not erase stylometric separability (S02):
   they measure different things (reader judgment vs. distribution statistics). The
   skill therefore uses *literary quality* as its objective, never "human-likeness."
5. **Update discipline.** Tells marked Low/Folklore are excluded from automated action
   and can only be promoted after measurement on a fiction corpus (see
   `../spec/09-evaluation-benchmark.md` §Benchmark extension).
