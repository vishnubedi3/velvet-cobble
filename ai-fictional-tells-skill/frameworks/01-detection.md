# Framework 01 — Fiction-Specific Detection Framework

**What this is.** A process for *finding candidate tells* in a **Samur
narrative draft** and attaching evidence to each finding. It is explicitly
**not** an AI detector: it produces no "AI score," it is not adversarial,
and it never substitutes for the preservation gate. It is also not portable:
every pass below loads this project's context (`../spec/01-project-binding.md`)
and the project-tell catalog (`../taxonomy/19-project-tells.md`); run without
them it refuses rather than guesses.

**What this is not.** No statistical detector (S12–S14: unreliable, gameable,
biased); no single-sentence classifier (S02: the signal is distributional); no
"vibe check" (S26: label bias contaminates judgment); no canon-free style pass
(canon accuracy is this project's frame, not an optional extra).

## 1. Detection principles

1. **Detect patterns, not words.** A lexical item is flagged only as part of a
   documented behavioral pattern (taxonomy), never from a list.
2. **Detect causes, not symptoms.** Multiple flags sharing one cause (K1–K9)
   are one finding; the finding names the cause.
3. **Detect against baselines.** Uniformity/explicitness are defined relative
   to (a) the work's own internal baseline, (b) the genre contract, and (c)
   **this project's canon and registers** — never against an external "human
   norm."
4. **Capture the voice before judging it.** Pass A records the draft's own
   **narrative voice baseline** (§2 Pass A) — the positive inventory of what
   this draft *is* — before any tell is scanned for. Every uniformity finding
   is a deviation from that baseline, and every intervention must leave that
   baseline intact (PV-4/PV-14). The skill knows what to preserve before it
   decides what to reduce.
5. **The project contract outranks generic craft.** Where a generic detection
   heuristic and a project rule (canon, drafting constraint, anti-pattern,
   name register) disagree, the project rule decides
   (`../spec/01-project-binding.md` §3). Detection runs project tells first
   (§2 Pass B0) for exactly this reason: a draft must be right about the world
   before it can be improved as prose.
6. **Evidence before severity.** Every finding carries source IDs (empirical
   class) or canon/project citations (project class) plus a confidence level
   or an authority class (see `../research/02-evidence-hierarchy.md`).
   Low-confidence empirical tells are reported but cannot drive edits above
   Level 2.
7. **Explicitness about limits.** Where evidence is practitioner-only or
   adjacent-domain, the finding says so.

## 2. The detection pass structure

### Pass A — Establish the contract (prerequisite)
Before scanning for tells, extract:
- **The project context** (required at intake, `../spec/01-project-binding.md`
  §1): the live canon resolution (never frozen), the Generation Contract,
  the drafting constraints in force, and the draft's **KE position**
  (default: the Dhaneshra Period's equilibrium, post-KE ~900). From the canon
  resolution, build the **scene canon surface**: the institutions, places,
  factions, languages, and name registers the touched spans invoke — each
  with its canon ID. This surface is what PST detectors check against and
  what generic detectors use as their specificity anchor.
- Genre + subgenre (and which conventions are **contractual** — frameworks/07).
- Perspective and narration contract (omniscient? close third? unreliable?
  in-world chronicle? — decides PST-04's exceptions, `spec/01` §3.4).
- Authorial intent statements (style anchors, content boundaries, deliberate
  devices — from the Generation Contract and `author_intent`).
- Length/segment plan.
- **The narrative voice baseline.** 5–8 concrete voice signals observed *in
  the draft* — diction range, cadence (sentence-length behavior and where it
  breaks), syntax habits (fragments? left-branching? "and"-chaining?),
  tonal temperature, imagery domain, register shifts between narration /
  dialogue / interiority — each with a quoted evidence span. Examples of a
  usable signal: "narration never contracts, dialogue always does";
  "metaphors stay inside the irrigation-works domain"; "scenes open
  mid-action, never with place". This baseline:
  - is the reference all uniformity findings are measured against (and the
    reference the final read checks edited spans against — `../spec/05-pipeline.md`
    Stage 4b);
  - is **distinct from per-character voice profiles** (frameworks/02 §3):
    it describes the narrator/author voice, not the speakers;
  - includes the project's registers as *protected differences* — the
    language map's legitimate variation (`samur/02-canon/CUL-02`) is not a
    D04 finding;
  - conflicts with a declared style anchor → the affected findings are
    reported `author-consult-required`, never resolved by the skill;
  - is marked `unknown` for drafts too short to show one (~< 500 words);
    uniformity findings in that draft are flagged `uncalibrated`. Never
    invented, never imported from a style guide.

Without Pass A, every subsequent flag risks false positives (a romance HEA is
not N06; a Sorkin-esque banter rhythm is not D01; a court chronicle's
distorted history is not V02 — it may be the world's memory system).

### Pass B0 — Project-contract scan (runs FIRST; `../taxonomy/19-project-tells.md`)
Check the draft against the ten project tells, cheapest first:
1. **PST-09 name-register check** (mechanical: resolve every name against
   DYN-02 §1 / CUL-01 §6 / CUL-02 §3).
2. **PST-03 wind-law check** (every scene's season, river stage, campaign
   logic, and mood-weather against GEO-03).
3. **PST-04 epistemology check** (every deep-time date, pre-horizon
   assertion, and analytic-history claim against the in-world record's
   limits + the narration contract).
4. **PST-10 mystery check** (every touch of Q-076/077/078 and the NOT READY
   list: approach vs. resolution).
5. **PST-05 faction check** (every collective attribution against the
   canon's documented internal fault lines — houses, wings, clans,
   factions).
6. **PST-01/PST-02 transplant & exotica checks** (institutional detail and
   sensory registers against the transformation logs and the canon surface).
7. **PST-07/PST-08 anachronism & language-map checks** (dialogue and
   interiority against the world's values and the functional language map).
8. **PST-06 framing check** (decline/empire framing against the root-cause/
   trigger model).

Each PST finding carries `authority: project_canonical` and cites the canon
IDs that establish the violated rule. PST findings enter the queue ahead of
empirical findings in the same spans (`../spec/06-scoring.md` §7).

### Pass B — Surface scan of the generic clusters (cheap, high-recall)
Run the generic tell-detection heuristics from the taxonomy, in this order
(cheapest first), **after** Pass B0 and informed by it:

1. **Repetition & variation audit** (most objective): near-duplicate passages,
   repeated scene skeletons, repeated emotional beats, unintended motif
   recurrence → L02, L03, L10, N05, SC05 — plus the two *disguised* repetition
   forms that plain duplicate-detection misses:
   - **Cosmetic variation** — different words, identical construction: three
     scene-endings built on the same "not X, but Y" frame with different
     nouns; three entrances announced with different emotion labels; three
     aphorisms with the same antithesis skeleton. Cluster on *construction*,
     not tokens → evidence for P02, P04, SC02, SC05. Varying the words did
     not vary the pattern.
   - **Referent cycling** — the same entity renamed per mention ("the
     Shreshtha … the minister … the older man") instead of repeating the
     established name or pronoun; a face of P01 (practitioner-cataloged,
     S54; fiction-specific frequency unmeasured — detect via this audit,
     never as a word list). Correction law: **the right word repeated is
     correct**; the cycling is the artifact, not the repetition. (In this
     project the *office* names — Shreshtha, Dhresh, Beshara — are the
     correct repeated terms.)
   Every repetition-family candidate is classified **verbatim** (L02-family),
   **cosmetic** (P02/P04/SC05-family), or **referent** (P01-family). The
   class selects the intervention family and blocks synonym-swapping "fixes"
   (F-2): a cosmetic finding fixed by re-wording is unresolved by definition.
2. **Explicitness & metadiscourse**: interpretation-statements,
   theme-statements, emotion labels + causes, significance-statements, symbol
   glosses → U01–U04, N02, C01, E01–E02, FS03, V02. Scan for the named
   metadiscourse faces (each is a construction, never a word list):
   - **Weight annotations** — narration grading its own beat ("It was
     nothing, and yet it was everything") → U02, V02;
   - **Trailing participial glosses** — enacted beat + `…ing` clause that
     interprets it ("He left without looking back, leaving everything
     unsaid") → U04, D07;
   - **Preview signposts** ("Little did she know…") → P06; **retrospective
     decodes** ("It wasn't anger, she realized — it was fear") → U04, E02;
   - **Symbol footnotes** ("the broken clock had always been a symbol of…")
     → FS03;
   - **Scene-purpose declarations** ("We need to talk about…") → SC03.

   *Project override:* an in-world chronicle voice asserting the empire's
   distorted memory (the founding myth, the golden age) is not a V02 finding
   unless the narration contract is historian-omniscient (`spec/01` §3.4).
3. **Continuity**: fact/timeline/rule/world-state violations → L04, L05, L09,
   A02 (via the story model, interventions/03). Continuity violations
   *against canon facts* are reported to the Canon Guard workflow (the PST
   report-only rule); prose-internal continuity is repaired here.
4. **Uniformity**: sentence-length variance, register monotony, scene-opening
   type distribution, scene-end button density, metaphor density, valence arc
   shape → P01–P07, S01–S06, SC01–SC04, T01–T04, E05, V01–V06 — all measured
   against the Pass A voice baseline **and the language map's legitimate
   register differences**, not an external norm.
5. **Template**: stage-ladder structures, milestone checklists, setup/payoff
   ledgers, stock humor → N01–N08, R02, FS02, H01, F01. *Project override:*
   the documented multi-pressure decline is not a T05/F04 "premature
   resolution" miss — check PST-06 before flagging structure.

### Pass C — Evidence attachment (quality gate)
Each candidate finding is documented with:
- Tell ID(s) + the quoted passage(s); PST findings additionally cite the
  canon IDs that establish the violated rule;
- the pattern evidence (recurrence count, distribution shape, ledger
  violation; for PST: the canon-vs-span mismatch);
- source IDs + confidence (empirical class) or authority class (project
  classes), per `../research/02-evidence-hierarchy.md`;
- the causal hypothesis (K-code — PST tells have K-causes too: the generator
  fails in these ways for these reasons);
- a **function test**: what does the passage do for the story (see
  taxonomy/20 §20.2)? Passages that do deliberate work are marked *intentional*
  and dropped from the intervention queue (not from the report);
- for **genericity findings** (P01, S03, W05, D04, C03, H01, U01, PST-02), a
  **transplant test** — the fiction form of the portability test (S54):
  demonstrate (a) the span transplants unchanged (the line of dialogue would
  serve any speaker in any story; the description could open any scene
  anywhere; the beat could belong to any character), and (b) the specificity
  that was *available and unused* — in this project, the **scene canon
  surface** (the established Oren stage, the institution's documented
  procedure, the region's named texture, the wind season). The transplant
  demonstration plus the ignored canon surface are the objective evidence;
  "it feels generic" is an adjective and is invalid. A span is genericity
  evidence only if it survives transplantation *and* ignores available
  project-specific material; a plain but canon-bound span passes.

### Pass D — Prioritization
Score findings (see `../spec/06-scoring.md`) and emit the intervention queue.
Priority = (severity × confidence × function-loss) − (false-positive risk ×
intent), with project-canonical findings holding queue priority over
empirical findings in the same span (`../spec/06-scoring.md` §7). Only
findings above threshold enter the queue.

## 3. Fiction-specific caveats (the false-positive guardrails)

1. **Genre contracts first.** Mystery's setup/payoff, romance's HEA ladder,
   thriller's scene buttons, hard SF's system specs are *features*. The genre
   gate (frameworks/07) runs before any flag becomes an intervention.
2. **Voice is not uniformity.** A deliberately flat or polished voice (V03
   false-positive) is identified via the work's own baseline and author
   anchors — never by comparing to an imagined "human" distribution.
3. **Literary devices are not tells.** One antithesis is rhetoric; the tell
   is the *reflex* (P02). Frequency thresholds are per-work, not universal.
4. **Long-form tells are state problems.** In texts > ~10k words, prioritize
   the L-cluster over style clusters: a draft with perfect style and broken
   continuity is more "AI-broken" than one with clean continuity and bland
   style.
5. **Reader-judgment data cuts both ways.** Readers rate AI stories highly and
   can't identify them (S28) — "would a reader notice?" is not a detection
   criterion; "does this cost the story something?" is.
6. **The transplant test has two pass conditions.** A span is genericity
   evidence only if it survives transplantation unchanged *and* ignores
   available story-specific material (here: the canon surface). Plain-but-
   canon-bound prose passes: plainness is not genericity, and plain styles
   are protected (PV-14, P01's FPR note).
7. **Repetition is not the enemy; unintended repetition is.** Established
   names, correct repeated words (the office names above all), and intended
   refrains (motif register) are craft. The artifacts are verbatim
   re-derivation (L02), the unchanged *construction* under changed words
   (cosmetic variation), and referent cycling. Never "fix" a finding by
   adding variation.
8. **In-world belief is not a tell.** Characters and chronicle voices may
   hold single-cause decline theories, distorted memories, and factional
   histories (PST-06/PST-04's FPR notes) — that is the world's memory
   system. The detector asks *whose knowledge is this?* before flagging.

## 4. Output contract

Detection produces the **AnalysisReport** (schema: `../schemas/analysis-report.schema.json`):
one `finding` per candidate tell with: passage span, tell ID, authority class,
confidence, severity, cause, function-test result, intentionality verdict,
proposed intervention level (or `none`), and preservation-risk notes. Nothing
in the report mutates text; mutation happens only through the intervention
pipeline (`../spec/05-pipeline.md`). Findings that allege canon contradiction
carry `report_only: canon workflow` routing (the PST monitored rule) and never
produce a canon-editing intervention.

## 5. What detection never does

- Never reports a probability of AI authorship (unreliable + harms authors,
  S14; non-native writers disproportionately flagged — Liang et al. 2023;
  Clarkesworld's concern, S44).
- Never flags based on a single sentence or word.
- Never treats Low/Folklore *empirical* patterns as actionable (author-declared
  project style rules are a different authority class, `spec/01` §2).
- Never emits "make it more human" as an instruction (vague, detector-flavored,
  quality-neutral).
- Never treats word-level repetition as automatically bad: repeating the
  established term is correct craft; cycling referents or rotating synonyms
  is the artifact (§2 Pass B, variation audit).
- Never imports a word list from any source (S54's catalog is adapted as
  *constructions and tests*, not as banned vocabulary; fiction word lists
  are Tier 4).
- Never edits, repairs, or "corrects" canon, and never resolves a deliberate
  mystery or a NOT READY matter (PST-10; `spec/01` §3.5) — canon work goes
  to the Canon Guard workflow.
- Never runs without the project context: a draft without a valid Samur
  binding is refused at intake, not analyzed generically (`spec/01` §1).
