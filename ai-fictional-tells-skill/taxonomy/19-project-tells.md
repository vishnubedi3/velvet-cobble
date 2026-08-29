# Taxonomy 19 — Project Tells (Samur-specific, PST-01…PST-10)

**Authority class:** `project_canonical` (`../spec/01-project-binding.md` §2).
These tells are **normative**: each encodes a rule this project has already
established (charter, canon, drafting constraints, anti-patterns), so a PST
finding is actionable on identification of an instance — no empirical
confidence weighting applies, only the standard function test,
intentionality check, and preservation gate. "Evidence" for a PST finding
cites the canon ID / project document that establishes the rule, plus the
quoted span. IDs are `PST` + number; they never appear in the S-source
namespace.

**Canon is the single source of truth.** This file encodes only the
*narrative-prose* consequence of each rule and cites where the rule lives.
Where this file and `samur/02-canon/` disagree, canon wins and this file is
defective (maintenance trigger, `../spec/01-project-binding.md` §5; checked
by T-11). All canon references are relative to the repository root
(`spec/01` §1).

**Default narrative position:** the Dhaneshra Period's equilibrium,
post-KE ~900 (`samur/02-canon/DYN-04` §15) — five polities, the two-wing
matha, the Empty Throne, the four claims. Period-sensitive entries say so.

---

## PST-01 — Renamed-history transplant

- **Definition.** An institution, scene, or faction rendered as a lightly
  renamed scene from one of this project's six comparative models or four
  religious systems — the Earth counterpart's *surface* reproduced where the
  transformation log built a Samur institution with its own causal logic.
  The project's influence-control rule is the rule here: a Samur element
  that is merely a renamed historical counterpart is a redesign candidate;
  in prose it is a tell.
- **Example pattern.** A court scene that is a Mughal durbar with Samur
  names — the audience ceremony, the honorific formulas, the poetic
  prestation — while the canon's court is the **dual structure** (the King +
  the Shreshtha, the matha as sanctioner — `samur/02-canon/DYN-01` §3); a
  "residency" scene with a Phre official playing a British Resident beat for
  beat (the Phre is a chartered company bounded to the delta — NS-01 §5);
  a Maratha-style tribute raid scene standing in for the **Tarnesh fourth**
  (`samur/02-canon/ADM-02` §3).
- **Observable characteristics.** The prose's institutional detail matches
  the *influence-register counterpart* (see
  `samur/01-research/comparative/README.md`) more closely than it matches
  the canon file it should instantiate; the transformation log's divergences
  (what the Samur version does *differently*) are absent from the prose.
- **Authority.** PROJECT.md §4 (influence control); the influence register;
  the transformation logs.
- **Likely cause.** K1/K9 — the generator reproduces the high-probability
  Earth-historical scene (Mughal court, colonial residency, steppe horde)
  rather than the lower-probability Samur institution.
- **Severity.** 3. **FPR.** 2 — convergent detail is possible (the models
  were chosen because they fit); the tell is counterpart-detail *without*
  the canon's divergences, not resemblance alone.
- **Effect.** Destroys the project's core claim — a world built from
  material conditions, not renamed aesthetics. Readers with the models in
  hand see the costume.
- **Mitigation.** Level 3–5: re-derive the scene's institutional behavior
  from the canon file the scene invokes (the dual structure, the four-law
  pluralism, the tribute terms); the institution's *friction* must come from
  the Samur version's own fault lines (matha–court, houses, wings).
- **Side effects.** Over-divergence for its own sake is a new artificiality;
  the fix is fidelity, not novelty.
- **Validation.** Re-read against the transformation log: does every
  load-bearing detail now trace to the Samur side of the log?

## PST-02 — Exotica / Orientalist surface

- **Definition.** Sensory and atmospheric prose drawing on generic
  "Eastern empire" imagery — spice-scented air, jewel-toned silks, incense
  veils, mystical portents — instead of this world's own material
  specificity (canal mud, tally-knots, the wind season, iron tolls, the
  weirs). The stereotype tell (C07/S07) specialized to this project, whose
  material is built from South Asian and Islamicate historical models and
  is therefore maximally exposed to the exoticizing register.
- **Example pattern.** "The air hung thick with cardamom and destiny as the
  emperor's procession wound through streets of silk and gold" — a passage
  that could open any generic Eastern-fantasy novel, naming nothing that
  `samur/02-canon/GEO-01`/`02` establish (the Oren, the bār canals, the
  toll crossings, the seven regions' actual textures).
- **Observable characteristics.** Fails the project transplant test
  (`../frameworks/01-detection.md` §2 Pass C): the span could open a scene
  in any invented Orient while the story-model's canon surface (region,
  town, season, institution) goes unused; sensory vocabulary from the
  exoticizing register rather than from the world's own economy (grain,
  silver, horses, pepper *as a Vethra monopoly*, not ambient spice).
- **Authority.** PROJECT.md §1 (material conditions, not aesthetics); S03/S07
  (genericity/exoticizing, empirical corroboration).
- **Likely cause.** K1/K4 — "eastern empire" is a high-probability template
  distribution the generator falls into when the prompt says "empire,
  temple, medieval."
- **Severity.** 3. **FPR.** 2 — the world does have temples, pepper, and
  festivals; the tell is the *generic* exotic register, not the presence of
  the world's own wealth.
- **Effect.** Replaces a constructed world with a genre costume; the
  specific damage is representational — the project's cultures become
  scenery.
- **Mitigation.** Level 1–3: replace the generic image with the
  story-model's specific material (which canal, which toll, which season of
  the wind), sourced from the canon surface resolved at Pass A. Never
  synonym-swap; source from canon.
- **Side effects.** Over-correction into driness; keep the earned image.
- **Validation.** Does the revised span identify *this* world (a reader
  with GEO-01/02 in hand could place it), not any world?

## PST-03 — Wind-law blindness

- **Definition.** Weather, season, river, or campaign logistics written
  against the **wind law** (`samur/02-canon/GEO-03`): rain in the land-wind
  months (7–12); Oren flood-stage navigation in the low-water season; a
  campaign in the wet season without the flood-stage constraint; famine
  without the failed-wind chain; or weather deployed as pure mood — banned
  outright by this project's anti-patterns, because in this world weather is
  the calendar, the agriculture, the military season, and the famine engine.
- **Example pattern.** "Storm clouds gathered as she made her decision"
  (mood-weather, wind-position unmoored); a river battle at low water in
  which the fleet maneuvers freely; a delta famine with a stated political
  cause and no wind failure.
- **Observable characteristics.** The scene's wind-season position is
  untraceable or contradictory (sea-wind months 1–6: rain, Oren flood,
  sowing; land-wind months 7–12: dry, low Oren, campaign season); weather
  changes beat-synchronized with interior states (the generic S04 signature)
  *in a world where the weather is a law, not a mirror*; the
  famine→debt→revolt chain invoked without its climatic driver.
- **Authority.** `samur/02-canon/GEO-03` (the wind regime, the Oren
  hydrology, the famine truce); the anti-patterns' weather-opening ban;
  TIM-01 (the year begins with the first sea-wind).
- **Likely cause.** K2/K4 — no world-state model; the generator writes
  temperate-zone default weather and mood-weather templates, ignoring the
  foundational law the prompt never restates.
- **Severity.** 3. **FPR.** 1 — the wind law is a high-impact canon fact;
  contradictions are checkable, not vibes.
- **Effect.** Breaks the world's foundational law — equivalent to a
  Midsummer snowfall in a realist novel — and wastes the project's best
  structural resource (weather as plot).
- **Mitigation.** Level 1–2: state corrections (month/wind/river-stage);
  Level 3–4: re-derive the scene's logistics from the season (move the
  campaign, re-anchor the navigation, let the failed wind *cause* the
  famine). Mood-weather: delete or load the weather with its canonical
  function (an oncoming land-wind is a deadline; a weak sea-wind is dread).
- **Side effects.** Weather-as-infodump; the correction is position and
  consequence, not meteorological exposition.
- **Validation.** Wind-position audit: every scene's season, river stage,
  and campaign logic traceable to GEO-03's regime.

## PST-04 — In-world epistemology violation (false precision / forbidden knowledge)

- **Definition.** The narration or a character asserts what this world
  cannot know: exact deep-time dates (the deep is **strata + relative
  order**, never dates — the no-false-precision rule); pre-horizon history
  (before ~KE −1200, the record's horizon) narrated as settled fact; the
  historian's truth spoken where only the in-world **imperfect memory**
  exists (the founding myth, the golden-age glorification, the decline and
  loss framings — `samur/02-canon/CUL-01` §5); or a NOT READY matter fixed
  in prose (Q-084's absolute ages; the deep's named agents).
- **Example pattern.** "Four thousand years before the empire, the
  Veshna stratum rose" (a false date — the strata are reconstruction
  ranges, in-world unknowable); a Dhaneshra-era character explaining the
  Stress-era fiscal overstretch with a modern historian's causal clarity;
  narration asserting the founding's material causes (the chokepoint, the
  absorption) as common knowledge — in-world, that knowledge is *distorted*
  by the founding myth and the consecration legend.
- **Observable characteristics.** Precision the in-world record cannot
  carry; analytic vocabulary from the canon documents (not from any
  in-world voice) leaking into narration; characters knowing what only the
  *authoritative record's* negative space preserves; the four memory layers
  (REL-02 §7 myths) flattened into one true account.
- **Authority.** `samur/02-canon/TIM-05`/`06`/`07` (the record's horizon;
  the strata; the no-false-precision rule); `samur/02-canon/CUL-01` §5 (the
  imperfect memory); the cross-check's protocol rules (no partial
  resolution of NOT READY matters).
- **Likely cause.** K3/K4 — the model was trained on the *analysis* of
  history, not its in-world remembering; the canon documents themselves
  (with their exact KE dates and causal chains) are in the generator's
  context and leak into the prose verbatim-in-stance.
- **Severity.** 3. **FPR.** 2 — the narration contract decides: an
  omniscient *chronicle* voice may carry epoch-level truth where canon
  permits; what no voice may carry is false precision and the deep's
  settled detail. (See the in-world voice exception, `spec/01` §3.4.)
- **Effect.** Collapses the project's epistemology — the gap between what
  happened and what the world remembers is one of the novel's engines
  (Q-077's substrate); a narration that knows everything spends it.
- **Mitigation.** Level 2–3: reduce the precision to the world's register
  ("older than the record", "the old time when the nights came too fast" —
  the world's own deep-time reckoning); re-attribute analytic truth to an
  in-world bearer with a source (a Beshara record, a temple tradition) or
  to the distorted memory layer it belongs to.
- **Side effects.** Over-mystification; the fix is the *correct* epistemic
  register, not vagueness everywhere.
- **Validation.** For each assertion: who in-world knows this, from what
  source, at this KE date? No answer → the assertion is PST-04.

## PST-05 — Faction monolith

- **Definition.** Any of this project's factions, houses, clans, wings, or
  polities portrayed as a single-minded bloc: "the matha" speaking with one
  voice, "the Khor" riding as one horde, "the empire"/"the rump" acting as
  one actor, a Tarn house without internal politics. The canon's every
  faction is internally structured — the faction *is* its fault lines.
- **Example pattern.** "The Veshna matha had decreed…" (the matha has two
  wings — the Veshna apex and the Tarn renewal — plus the conciliar,
  pragmatist, dynastic-patronage, and apex-neutrality factions:
  `samur/02-canon/DYN-04` §10); "the Khor wanted war" (four clans —
  Kheshur the assembly-senior largest, Ghoranur the horse-breeders, Zhanur
  the raiders, Marenur the traders — with a seasonal assembly:
  `samur/02-canon/DYN-03` §6); "the merchants of Besra" as one interest
  (the shahukar debt chain cuts both ways — ECO-01/02).
- **Observable characteristics.** Collective attribution verbs ("the temple
  demanded", "the clans agreed") where the canon documents divergent
  internal interests; intra-faction disagreement count ≈ 0 across a draft
  whose factions all have documented fault lines; the C06 (hyper-consistency)
  and C08 (theme-vehicle) generic tells, but with the *canon's* internal
  structure as the reference rather than a generic "real people disagree"
  norm.
- **Authority.** `samur/02-canon/DYN-03` (houses/clans), `DYN-04` §10 (the
  matha's factions), `REL-01` §4 (orthodoxy vs. revival; varna vs. jati;
  matha vs. regional temples), `CUL-01` §4 (the five factions' texture),
  FOR-01/02 (the powers' own politics).
- **Likely cause.** K2/K4 — factions are generated as named collectives
  (summary-level entities) rather than as the decision procedures the canon
  defines; "empire factions" template distributions are monoliths.
- **Severity.** 3. **FPR.** 1 — the canon's internal structures are
  documented; the check is against them, not against taste.
- **Effect.** Erases the project's actual plot material: the succession
  fault line, the matha's split, the clans' assembly politics, the
  houses' rivalry ARE the story; a monolith draft has no engine.
- **Mitigation.** Level 3–5: re-derive the speaking/acting faction's
  internal position from its canon fault lines; attribute the action to a
  sub-faction, house, or office with the documented interest; let another
  documented interest dissent. The five social factions (peasants,
  merchants, chiefs, military, court — CUL-01 §4) have texture, not unity.
- **Side effects.** Mechanical dissent (a token objector per scene) is a
  new template; the dissent must come from the canon's documented lines.
- **Validation.** For each collective action: which documented sub-faction
  drives it, and which documented interest resists?

## PST-06 — Template-empire framing

- **Definition.** The narrative adopting a generic fantasy-history frame
  for the Samur: evil-empire tyranny, decadent-decline porn, noble-rebel
  romance, the great-man theory of fragmentation ("the betrayal/famine/
  usurper brought the empire down"), or empire-as-stage-set where politics
  is scenery. The project's history is an interaction of long root causes
  with late triggers — a *process*, not a villain's arc.
- **Example pattern.** A Fragmentation-scene that pins the collapse on one
  usurper's ambition; a stress-era scene framed as moral decay ("the
  empire had grown soft"); a rebel-band viewpoint whose legitimacy framing
  is modern-national rather than the world's four-claims/factional
  legitimacy.
- **Observable characteristics.** Single-cause explanations of documented
  multi-cause processes; morality-of-decline framing where the canon gives
  fiscal-military-demographic mechanics; legitimacy talked about in
  modern-nation terms instead of consecration/office/lineage claims.
- **Authority.** `samur/02-canon/TIM-01` §4 (root causes vs. triggers);
  PROJECT.md §1; NS-01 (the negative spaces — what did not happen — as the
  anti-template).
- **Likely cause.** K4/K9 — "rise and fall of empires" narration and
  fantasy-rebellion templates are high-probability story shapes.
- **Severity.** 2. **FPR.** 3 — *characters* may hold decline theories,
  single-cause blames, and rebellion framings in-world (they are period
  beliefs); the tell is the *narration's* frame adopting them as truth, or
  the story structure enforcing them against the canon's mechanics.
- **Effect.** Replaces a constructed historical machine with a genre
  morality play.
- **Mitigation.** Level 4–6, author-gated: re-anchor the frame — let
  single-cause stories be *in-world* theories held by factions; restore the
  interacting-pressures reality in what the narration shows, if not what
  characters claim.
- **Side effects.** Lecture-history (W01 with PST clothes); the fix is
  dramatized causation, not exposition of TIM-01.
- **Validation.** Frame audit: whose theory is the decline story? If the
  narration's own: reframe. If a faction's: legitimate.

## PST-07 — Modern-sensibility transposition

- **Definition.** Twenty-first-century idioms, moral frames, psychological
  registers, or social logics in dialogue or interiority: therapy-speak
  ("closure", "boundaries", "my truth"), meritocratic-career framing,
  romantic-love marriage defaults, national identity, rights language,
  modern time-discipline. The world's own institutions — dharma by station
  and stage of life, the varna framework contested *from within*, the
  consecration legitimacy, jati negotiation, the four-law pluralism — are
  the measure of what a person here can want and how they can say it.
- **Example pattern.** "She deserved a life of her own choosing, and no
  temple was going to take that from her" (a modern autonomy frame where
  the world offers station-dharma, revival devotion, house interest, or
  faction claim — all of which are *this world's* engines of
  self-assertion); a grief scene processed in therapy stages.
- **Observable characteristics.** Vocabulary anachronism (the
  anti-patterns' per-era audit list, anchored to CUL-01/02); moral frames
  with no in-world institution behind them; emotional processing that
  follows modern-psychology templates (the generic C04/E04 tells, judged
  against canon values rather than "medieval realism" at large).
- **Authority.** `skills/canon-guard/anti-patterns.md` (the anachronism
  rules); `samur/02-canon/REL-01` (dharma/varna/jati), `CUL-01` (the
  social orders), ADM-01 §5 (the four laws).
- **Likely cause.** K3/K7 — alignment-era moral and psychological defaults
  installed as "universal" by the generator.
- **Severity.** 3. **FPR.** 2 — the world has dissent, reformers, and the
  revival's anti-hierarchical strand (REL-01 §4); the tell is the *modern*
  frame, not defiance itself. In-world defiance has in-world shapes.
- **Effect.** Breaks the historical mind; the characters become modern
  cosplayers, and the world's real conflicts (station against station,
  house against temple, wing against wing) become unactable.
- **Mitigation.** Level 3–5: re-derive the want/objection from the world's
  documented repertoires (dharma interpretation, revival devotion, house
  obligation, assembly speech, the courts of the four laws); keep the
  defiance, change its grammar.
- **Side effects.** Period-pastiche stiltedness ("translationese" — also
  banned by the anti-patterns); the register target is natural speech
  *within* the world's registers, not stiff archaism.
- **Validation.** Anachronism audit against the CUL-anchored list; can the
  sentiment be restated using only the world's institutions? If not, it
  may be genuinely anachronistic — or the seed of a QUESTION for the author.

## PST-08 — Language-map flattening

- **Definition.** Dialogue and POV ignoring **who speaks what**: Khor
  characters conversing in fluent core-Samur idiom (Khoric is a separate
  family — oral, agglutinative, no th/gh clusters, richer vowels; its
  speakers' Samur is a marked accent); Samur officials reading Phre
  sea-script documents directly (they depend on **Voren interpreters** —
  CUL-02 §7's knowledge dependency); Voren scenes without the delta
  pidgin; the Veshna sacred register (frozen orthography, ritual sounds)
  used casually; universal literacy where the world runs on oral oath,
  knot-tally, and tally-mark.
- **Example pattern.** A Kheshur clan-leader delivering polished
  subordinate-clause Samur in assembly debate; a Beshara clerk quoting a
  Phre charter at sight; two delta smugglers speaking core-dialect Samur
  with no pidgin trace.
- **Observable characteristics.** Cross-language scenes without
  interpretation friction where the canon records dependency (the Voren
  interpreters); no register differentiation across the language map
  (core / Sareth frontier / delta pidgin / Tarn varieties / Veth coastal /
  Khoric / Phreic); the D04/C03 uniformity tells with the canon's language
  map as the differentiation reference.
- **Authority.** `samur/02-canon/CUL-02` (the families, scripts, registers,
  functional map); CUL-01 §2 (the dialects).
- **Likely cause.** K1/K2 — one generator, one idiolect; the language map
  is context the model must be reminded of per scene.
- **Severity.** 2. **FPR.** 2 — some characters genuinely are bilingual
  (the court, the Voren merchants); the tell is the *flattened map*, not
  any single fluent speaker. Bilingualism must be established, not
  assumed.
- **Effect.** Loses the world's communication texture and its documented
  frictions (the interpreters are a plot asset); every scene sounds like
  the core court.
- **Mitigation.** Level 3: re-voice per the functional language map — the
  accent/markers the canon supports (Khoric syntax in Samur speech;
  pidgin in Voren trade talk), interpretation as an on-page beat where the
  dependency exists. Never dialect caricature (D04's constraints hold).
- **Side effects.** Phonetic-spelling minstrelsy; markers must be
  syntactic/lexical and canon-sourced, not eye-dialect.
- **Validation.** Language-map audit: for each scene, which languages are
  in play, who bridges them, and where does the friction show?

## PST-09 — Name-register violation

- **Definition.** Personal or place names outside the canon pools and
  registers: invented personal names with no pool entry (the DYN-02 §1
  name-pool rule is absolute for the narrative); wrong name-class
  morphology (Khoric -ur/-an suffixes or cluster-shapes on Samur names;
  Samur -esh/-ath on Phre characters; Phreic -an/-or without the
  no-aspirate phonology); toponym variants of the fixed register ("Kesram",
  "the Veshran river" for the Oren); Earth-name calques.
- **Example pattern.** "Rajendra Vessamin, a merchant of the delta" — no
  pool entry, mixed morphology; a new garrison town invented for scene
  convenience (the toponymic register is fixed — CUL-01 §6).
- **Observable characteristics.** Names not resolvable against DYN-02 §1
  (place-doubling class; the -an/-ar class; the -esh/-ath class) or CUL-02
  §3 (the Khoric register) or CUL-01 §6 (the fixed toponyms); morphology
  that crosses the language families.
- **Authority.** `samur/02-canon/DYN-02` §1 (the name-pool rule); CUL-01 §6
  (the fixed toponymy); CUL-02 (the foreign registers).
- **Likely cause.** K1/K9 — name generation from generic fantasy-phone
  distributions rather than the pool in context.
- **Severity.** 2. **FPR.** 1 — mechanical, checkable against the pools.
- **Effect.** Corrodes the onomastic system — the registers encode the
  world's language history; wrong names are quietly world-breaking.
- **Mitigation.** Level 1: restore a pool name or the established
  toponym. If the character is *new* (the narrative stage creates
  characters within the pool), the fix selects from the pool — the skill
  never coins names (coining goes to the author/canon workflow).
- **Side effects.** Name collision if restoration picks an established
  historical bearer; check DYN-02/DYN-03 for the name's existing holders.
- **Validation.** Every name in the revised span resolves to a pool entry
  or an established toponym.

## PST-10 — Mystery consumption

- **Definition.** The narrative spending a deliberate mystery or a NOT
  READY matter as a plot coupon: the hidden history (Q-077) deployed as a
  reveal-twist; the Kesra Charter's text (Q-078) quoted, summarized, or
  dramatically exposed; the distant western partner (Q-076) named or
  arriving; a NOT READY detail (Q-084's absolute ages; the deep's named
  agents; the Orenic kind's pre-basin history) fixed as fact to serve a
  scene.
- **Example pattern.** The guru produces the Charter and a key passage is
  quoted; a western ship appears and its port is named; "beneath the
  chronicle lay the truth the temple had buried" — followed by the truth
  being stated.
- **Observable characteristics.** Resolution events attached to the
  protected list; unresolvable-by-design questions given answers;
  escalating-promise structures that can only pay off by consuming the
  mystery (a twist audit: what does this arc's promise require the reveal
  to be?).
- **Authority.** The cross-check §1/§4 (the deliberate mysteries as the
  narrative's built-in hidden layers: **draw on, never resolve**; the NOT
  READY matters' constraints); `samur/02-canon/REL-02` §7 (the memory
  layers' structure), TIM-05/06 (the horizon).
- **Likely cause.** K3/K4 — RLHF closure preference plus training on
  twist-reveal story templates; an open question in context reads as a
  Chekhov's gun to the generator.
- **Severity.** 3. **FPR.** 2 — *approaching* the mysteries, partial
  glimpses, contradictory traditions, and in-world speculation are exactly
  the intended use; the tell is resolution (an answer the canon
  refuses to give).
- **Effect.** Irreversibly spends the project's deepest narrative capital;
  this is the one tell where a single edit (or scene) can do damage no
  later revision can undo — the reader cannot un-read the reveal.
- **Mitigation.** Level 2–4: convert the reveal to an approach — a
  tradition that disagrees, a record that stops, an arrival that is
  glimpsed and unnamed, an answer that the scene's interests *would*
  distort. Author-gated in all cases; if the author is resolving a mystery
  deliberately, that is a canon change (the QUESTION/changelog workflow),
  not a prose edit.
- **Side effects.** Coy withholding that reads as tease; the approach must
  carry its own scene value.
- **Validation.** Mystery audit: for each protected item touched, does the
  revised span leave the canon's answer-space exactly as open as canon
  leaves it?

---

## Monitored (project context; not acted on beyond reporting)

| Pattern | Status | Why |
|---|---|---|
| Canon contradiction as such | **Report-only here** | Canon repair belongs to the Canon Guard / author workflow (`spec/01` §1); this skill flags, never fixes |
| Wrong epoch texture (a Founding-era custom in a Dhaneshra scene) | Monitored | Usually a canon-accuracy matter first (report); prose-level texture fixes apply only where the canon permits the custom's survival |
| Placeholder-scale errors (a distance a horse cannot cover in the stated time) | Monitored | Continuity-family (L09/A02) with canon anchors; repair against the story model's timeline ledger |
