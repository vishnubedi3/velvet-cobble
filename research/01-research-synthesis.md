# 1. Research Synthesis

**Scope.** This synthesis covers empirical and practitioner evidence on recurring
"fictional tells" — the linguistic, narrative, stylistic, structural, character,
dialogue, pacing, and storytelling behaviors that make LLM-generated fiction feel
recognizably machine-written. It deliberately excludes generic AI-writing-tell research
as the primary subject; adjacent-domain evidence (essays, news, reviews, dialogue,
poetry) is admitted only where it illuminates fiction and is labeled as such.

**Method.** 40+ sources were reviewed (see `research/03-source-index.md`): peer-reviewed
empirical studies (S01–S29), stylometry and detection research, narrative-generation
literature, computational creativity work, editor/practitioner evidence (S44–S47), and
literary criticism. Every claim below carries a source ID and a confidence marker.
Evidence tiers are defined in `research/02-evidence-hierarchy.md`.

---

## 1.1 The headline problem: what is empirically established

1. **LLM creative writing is stylometrically separable from human writing, and the
   dominant signal is *uniformity*, not error.** Burrows' Delta clustering of short
   stories finds LLM texts (GPT-3.5, GPT-4, Llama 70B) form tight clusters by model,
   while human texts form broad, dispersed clusters — even when humans all answer the
   same prompt (S02). The same "tight-clustering" result appears in stylometric studies
   of essays (S01) and register analysis (S41).

2. **The prose-level signature is statistically average language.** GLTR showed in 2019
   that generated text is composed of words a language model assigns high probability,
   with abnormally low per-word surprise; showing humans this signature raised their
   detection accuracy from 54% to 72% (S10). MAUVE formalizes the same distribution gap
   between human and neural text (S11). This is the causal root of "overly polished,
   generic, uniformly structured prose": generation is a draw from a model of *typical*
   text.

3. **Explicitness is a documented, cross-domain LLM behavior.** Herbold et al. find
   fewer discourse and epistemic markers (hedges of uncertainty) and more nominalization
   in ChatGPT essays (S01). LIWC-based news comparison finds AI text more formal,
   structured, positive, and motivational; human text shows more negative emotion
   (anger, sadness), more length variation, and more informal/personal reference (S37).
   A reader study of short stories found AI stories were rated *more* absorbing and
   higher-quality than published human stories, and the authors attribute part of this to
   the AI stories "stat[ing] their themes outright, rather than leaving readers to infer
   meaning" (S28). Experts scoring fiction with the Torrance Test of Creative Writing
   rate LLM stories 3–10× worse than professional writers on scene-vs-exposition,
   subtext, rhetorical complexity, pacing, endings, voice flexibility, and originality
   (S04).

4. **LLM stories are thematically homogeneous and structurally formulaic.** Beguš'
   comparison of 250 human and 80 GPT-3.5/GPT-4 (+ Llama 3) stories written to the same
   Pygmalion prompts finds LLM narratives formulaic, "follow[ing] an inner structure
   paragraph by paragraph," bereft of local and cultural specificity, and uniformly
   positive with weak turning points; human stories additionally thematize loneliness,
   loss, obsession, serendipity, and violence (S03, S43). LLM personas and stories carry
   measurably higher rates of demographic stereotypes than human-written ones (S06, S07,
   S42).

5. **Repetition and template reuse are real and measurable.** ChatGPT regenerates
   >90% of 1008 requested jokes from a stock of 25 (S05). LongGenBench finds ~45% of
   long outputs exhibit significant repetition (S31). Recursive synthetic-data training
   collapses lexical, syntactic, and semantic diversity — model collapse (S21, S20) —
   and AI-assisted human writers produce stories that are measurably more similar to
   each other than unassisted ones (S16). LLM narratives contain repeated plot elements
   and lower story-level originality than human writing (S43, citing Xu et al. 2025).

6. **Character-level tells are documented, including by genre.** CAspER's 8-dimension
   character-portrayal analysis across model families and genres finds LLM romance
   characters "nearly completely coherent, whole, transparent," domestic-story
   characters literal/theme-representing, and character-type distributions that track
   genre conventions *more* tightly than human writing; Phi generates the most diverse
   characters, Llama the least (S29). GPT-WritingPrompts finds AI female protagonists
   more positive, less aroused, less in control, with more appearance-words than
   male protagonists — mirroring earlier GPT-3 bias results (S42, S06).

7. **Dialogue pragmatics is a weak spot, not dialogue fluency.** GPT-4 reaches
   human-level accuracy at *interpreting* conversational implicature in a sitcom corpus,
   but most models' *explanations* of implicature score low on reasonability (S38).
   Psychologically, ChatGPT's comprehension mirrors humans in 10/12 psycholinguistic
   tasks, but it disfavors shorter words for less informative content — a signature of
   over-explicitness (S39). Off-the-shelf LLMs drift from assigned personas in
   multi-turn role-play (S49).

8. **Long-form generation degrades measurably.** Long-context generation benchmarks show
   degradation of 1.2–47.1% across models (S31); attention "loses" mid-context
   information (U-shaped recall) (S22); story-generation surveys identify coherence,
   character consistency, and diversity as the persistent open problems (S33, S32).
   These are the empirical anchors for long-form tells: drift, recycled scenes,
   mid-story sag, ending compression.

9. **The lexical-tell phenomenon ("delve," "tapestry") is real but domain-specific and
   post-training-induced.** Excess-vocabulary studies show abrupt post-2023 frequency
   spikes of style words in scientific abstracts and peer reviews (S17, S18, S19).
   Experiments implicate RLHF preference data rather than pretraining or architecture:
   raters treat certain words as quality proxies (S19). Fiction-specific "AI word
   lists" circulating online have **no comparable empirical basis** — the phenomenon
   exists, but any fiction word list is folklore until measured on a fiction corpus.

10. **Human readers are poor AI-detectors, and labels drive judgment.** Humans cannot
    reliably distinguish GPT-4 in conversation (54% vs. 67% human baseline, S15) or
    short stories (chance-level identification, S28); AI poetry is judged *more* human
    than human poetry (S27). Both humans (+13.7pp) and AI evaluators (+34.3pp) show
    pro-human attribution bias, and labels cause the *same features* to be evaluated
    oppositely (S26). Conclusion: the skill must target literary quality directly, never
    "perceived humanness," which is partly a labeling artifact.

11. **Automated detectors are unreliable and gameable.** The largest tool tests find
    none reliable; false-positive rates reach 50% (S14). Paraphrasing breaks detectors
    (S12, S13); 19 humanizer tools defeat many detectors while measurably distorting
    text (S34); adversarial paraphrasing guided by detector scores sometimes
    *backfires* — 4.15% of humanized samples become *more* detectable (S35). Humanizing
    has a fundamental quality/cost/evasion trade-off (S36).

12. **Explicitness and positivity biases are aligned-model behaviors.** Reduced anger
    and sadness, more positivity and motivation language appear across GPT-4o, Mistral,
    and Llama news outputs, attributed to alignment (S37). Beguš finds newer models
    *more* progressive on gender/sexuality than both older models and human writers —
    alignment shapes theme and characterization (S03).

---

## 1.2 Cluster-by-cluster findings

### Prose
Established: modal-average phrasing (S10, S11); register drift toward formal/nominalized
language and reduced hedging (S01, S37, S41); lower register variation than humans (S41);
balanced/parallel constructions recognized by readers — "em dashes and sentence
structures such as 'it's not just X, it's Y'" were spontaneously cited as AI markers in
the Villanova reader study (S28). Folklore until measured: fiction "AI word lists,"
em-dash overuse as a standalone marker, contraction avoidance. **Cause:** maximum-likelihood
training over a corpus that over-weights polished, reviewed prose; post-training
preference for "clear" text; low-temperature decoding.

### Narrative structure
Established: formulaic inner structure (S03); low TTCW scores on structural flexibility,
narrative pacing, endings (GPT-4: 19–53% vs. humans' 89–94%) (S04); explicit theme
statement (S28); high setup/payoff regularity and weak turning points (S03, S43);
story-similarity collapse across writers using the same AI (S16). **Cause:** training on
summarized/analyzed fiction (stories + their reviews, retellings, templates) teaches the
*skeleton* of stories; autoregressive generation without a global plan converges on the
most probable skeleton; RLHF rewards "clear, complete" outputs (themes stated, threads
tied).

### Character
Established: demographic stereotypes at rates above human baselines (S06, S07, S42);
transparent, coherent, whole characters — especially in romance (S29); character
development rated weak by expert writers (S04); predictable, alignment-shaped values
(S03). Folklore-adjacent: "trauma résumé" and "quirk-as-depth" — plausible consequences
of template training, but no direct measurement. **Cause:** characters are generated as
summaries of fictional-character descriptions rather than as decision-makers; alignment
flattens moral texture; stereotype-heavy training distributions (S06, S07).

### Dialogue
Established: implicature *comprehension* is near-human in GPT-4 but explanation quality
is poor in most models (S38); models disfavor elliptical/short constructions for
low-information content (S39); persona drift over multi-turn dialogue (S49); expert
ratings of voice flexibility are low (S04). The symmetric, polite, over-explicit
dialogue pattern is heavily corroborated by practitioner evidence (S44) and follows
directly from RLHF helpfulness training and from average-phrasing generation.
**Cause:** dialogue is generated as *maximally informative, cooperative* speech
(Gricean over-compliance); alignment suppresses impoliteness, evasion, and ambiguity.

### Description and worldbuilding
Established: world-building & setting rated far below humans by expert writers
(GPT-4 41.7 vs. 94.4; S04); LLM stories lack local/cultural specificity (S03); AI news
text shows a "visual descriptions" preference (S37). Sensory-checklist and
atmosphere-first description are the strongest practitioner-documented tells (S44);
their mechanism is the average-register drift: description is written in the genre's
*typical descriptive register* rather than from a character's perception. **Cause:**
no embodied/perceptual grounding (S39); template conflation of "setting description"
with genre-atmosphere markers; training on summaries that compress scenes into
sensory lists.

### Emotion
Established: naming/explaining emotion rather than enacting it is the single most
cross-corroborated tell: LIWC studies show AI text uses explicit affective categories
while underproducing the *behavioral* and *negative* correlates (S37); Villanova authors
note theme/emotion stated outright (S28); Beguš finds uniformly positive arcs with weak
turning points (S03, S43); Herbold finds fewer epistemic hedges — emotion is asserted
rather than modulated (S01). Human fiction's six canonical emotional arcs (S08) provide
the comparison baseline: human stories *fall* as often as they rise; aligned LLM fiction
is valence-smoothed. **Cause:** RLHF positivity pressure + explicitness bias +
training on interpreted/reviewed fiction (emotion named in reviews becomes emotion named
in prose).

### Pacing, scenes, voice, subtext
Established via TTCW expert measures (S04): narrative pacing, scene-vs-exposition,
subtext, rhetorical complexity, and voice/perspective flexibility are the *lowest-scoring*
LLM dimensions (GPT-4 passes 8–53% of tests vs. humans' 64–94%). Uniform scene skeletons
follow from the repetition results (S31). Subtext gaps follow from explicitness results
(S28, S38). **Cause:** no global pacing plan (autoregression equalizes scene weight);
explanatory narration is the model's default stance (it is trained to explain);
ambiguity is dispreferred by RLHF raters.

### Conflict, foreshadowing, symbolism
Least directly measured. Supported: sanitized conflict (reduced anger/sadness/aggression,
S37), moral clarity (alignment, S03, S37), premature resolution (weak turning points,
S03, S43), repeated plot elements (S43). Foreshadowing/symbol overuse is **plausible but
unmeasured** — treated as Medium-Low confidence, monitored rather than acted on. **Cause:**
alignment softens antagonists and cruelty; template structures deliver setup/payoff on
schedule.

### Humor
Well established: template reuse (25 jokes, S05); explanatory tendency (S05);
uniform wit is a direct consequence of single-voice generation (S02, S29). Comedy
specifics beyond that are practitioner-level.

### Action, romance
Action: long-context consistency failures (S22, S31) explain spatial drift; sequential
"then, then, then" choreography follows from linear autoregression. Romance: CAspER's
transparent-coherent-whole romance characters (S29) + stereotype results (S06) +
explicitness (S28) are the empirical anchors; pacing/reconciliation tells are
practitioner-level.

### Genre variation
Established: genre *conditions* character type (CAspER, S29); genre identification
models find horror least identified / most confused with other genres (S47);
LLM judges rate Sci-Fi/Fantasy better than coming-of-age (S46). No study yet measures
tell density by genre — the taxonomy's genre matrix is therefore a hypothesis scaffold
with per-cell evidence status, not a claim.

### Long-form
Established: repetition (~45% of long outputs, S31); attention degradation and
lost-in-the-middle (S22); consistency degradation across models (S31); surveys name
coherence/character consistency/diversity as open problems (S33); multi-agent frameworks
exist precisely to compensate for context fragmentation beyond ~10k characters (S32).
**Cause:** no persistent memory; recency-weighted generation re-samples recent
statistics; summarizing context re-introduces compressed, repeated descriptions.

### Model variation
Established: models differ in stylometric tightness (GPT-4 tighter than GPT-3.5; S02),
in character diversity (Phi > Llama; S29), in register flexibility (S41), and in
alignment coloration (GPT-4o "neutral and polished," Llama "more emotionally
expressive"; S37). Decoding strategy measurably changes detectability (S23). Tells
should therefore be treated as *distribution shifts with model-specific tuning*, never
as universal word lists. The skill's thresholds must be recalibratable per model family
and per decoding settings.

### Human comparison (what actually distinguishes natural literary variation)
Human fiction is not "messier" — it is *heterogeneous*: broader stylometric dispersion
(S02), higher register variation (S41), six-way emotional arc diversity including
tragedy (S08), negative affect and anger/sadness (S37), local/cultural specificity
(S03), unresolved meaning (S04 subtext dimension), and idiosyncratic lexical risk.
The tell is not that AI text differs on any single feature; it is that AI text
*clusters* — across runs, prompts, and authors — at the center of every distribution
(S02, S16). The correct intervention target is therefore **variance and specificity**,
never "imperfection."

---

## 1.3 Why these tells emerge: the causal model

Every taxonomy entry is anchored to this causal model (codes reused across the taxonomy):

- **K1 — Maximum-likelihood training.** Pretraining optimizes average next-token
  probability over billions of tokens; fiction outputs regress to the *most typical*
  phrasing, structure, and imagery of the corpus (S10, S11).
- **K2 — Autoregressive generation without global planning or revision.** Prose is
  produced left-to-right with no world model, no pacing plan, no revision pass. Local
  coherence is strong; global structure, economy, and variance are emergent, not
  designed (S31, S32, S33).
- **K3 — RLHF / instruction alignment.** Preference optimization rewards helpful,
  clear, complete, positive, polite, morally legible text. This produces explicitness,
  theme statements, positivity smoothing, sanitized conflict, and cooperative dialogue
  (S03, S19, S37).
- **K4 — Training-data composition.** Fiction training mixes stories with their
  *interpretations* (reviews, essays, retellings, summaries, TVTropes-style catalogs),
  which teaches "story plus explanation" as the default register (S03, S04, S28).
- **K5 — Decoding.** Low-temperature/top-p decoding further concentrates probability
  mass, amplifying K1 uniformity (S23, S09).
- **K6 — No persistent memory.** Continuity is maintained only via context; long-form
  drift, contradictions, and repetition follow from attention limits and recency bias
  (S22, S31, S49).
- **K7 — Safety filtering and refusal training.** Reduces negative affect, violence,
  and morally ambiguous outcomes in fiction (S03, S37).
- **K8 — Evaluator-driven post-training artifacts.** Preference raters reward words
  and patterns treated as quality proxies ("delve" phenomenon), importing evaluator
  biases into style (S19).
- **K9 — Prompt/instruction template behavior.** The model fills a *requested* genre
  template; tells intensify when prompts specify genre tropes (S29, S43).

**Design consequence.** Interventions must remove *causes*, not symptoms: fix a
causally-excessive explanation by letting behavior carry the meaning (K3/K4), not by
synonym-swapping the explanation; break a scene skeleton by restoring the POV
character's perception (K2/K4), not by shuffling sentence order.

---

## 1.4 The anti-AI rewriting failure mode (evidence)

- Paraphrase-to-evade works on detectors but costs quality, and the trade-off is
  fundamental (S12, S13, S36). Recursive paraphrasing slightly degrades quality even in
  the best case (S13); commercial humanizers measurably distort text (S34).
- Detector-guided adversarial rewriting sometimes *backfires*, making text more
  detectable (S35).
- Author-obfuscation research treats quality loss as an explicit *cost* to minimize —
  i.e., the field itself assumes obfuscation degrades text (S30).
- Randomization / deliberate errors / "burstiness shaping" are unsupported as quality
  measures and contradicted by the human-comparison evidence: humans are not uniformly
  error-prone; they are heterogeneous (S02, S41). Inserting errors adds a *new*,
  easily-learned artifact.
- "Humanness theater" also fails the perception research: readers cannot reliably
  distinguish AI fiction regardless (S15, S28), and label-driven bias (S26) means the
  "AI-like" judgment is partly in the label, not the text.

**Therefore:** the skill's interventions are defined and bounded by literary criteria —
clarity, specificity, variance, causality, character-specificity, implication — with
detector scores explicitly excluded from the objective function. See
`skill/07-failure-modes.md`.

---

## 1.5 Implications for the skill (summary)

1. Detect *clusters of tells with a common cause*, not isolated words (taxonomy).
2. Anchor every intervention in the causal model (K1–K9) and the preservation
   constraints (`interventions/02-preservation-constraints.md`).
3. Default to the lowest intervention level that removes the cause
   (`interventions/01-intervention-hierarchy.md`).
4. Never escalate without evidence; never rewrite wholesale.
5. Re-evaluate against the story model (`interventions/03-story-model.md`) and reject
   damaging edits — including edits that merely *move* the AI signature.
6. Keep provenance transparent; do not target detectors (S12–S15, S26, S28).
