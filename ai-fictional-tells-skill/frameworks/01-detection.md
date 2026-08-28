# Framework 01 — Fiction-Specific Detection Framework

**What this is.** A process for *finding candidate tells* in a fiction draft and
attaching evidence to each finding. It is explicitly **not** an AI detector: it
produces no "AI score," it is not adversarial, and it never substitutes for the
preservation gate.

**What this is not.** No statistical detector (S12–S14: unreliable, gameable,
biased); no single-sentence classifier (S02: the signal is distributional); no
"vibe check" (S26: label bias contaminates judgment).

## 1. Detection principles

1. **Detect patterns, not words.** A lexical item is flagged only as part of a
   documented behavioral pattern (taxonomy), never from a list.
2. **Detect causes, not symptoms.** Multiple flags sharing one cause (K1–K9)
   are one finding; the finding names the cause.
3. **Detect against baselines.** Uniformity/explicitness are defined relative
   to (a) the work's own internal baseline and (b) the genre contract — not
   against an external "human norm."
4. **Evidence before severity.** Every finding carries source IDs and a
   confidence level (see `../research/02-evidence-hierarchy.md`). Low-confidence
   tells are reported but cannot drive edits above Level 2.
5. **Explicitness about limits.** Where evidence is practitioner-only or
   adjacent-domain, the finding says so.

## 2. The detection pass structure

### Pass A — Establish the contract (prerequisite)
Before scanning for tells, extract:
- Genre + subgenre (and which conventions are **contractual** — frameworks/07).
- Perspective and narration contract (omniscient? close third? unreliable?).
- Authorial intent statements (style anchors, content boundaries, deliberate
  devices).
- Length/segment plan.

Without Pass A, every subsequent flag risks false positives (a romance HEA is
not N06; a Sorkin-esque banter rhythm is not D01).

### Pass B — Surface scan (cheap, high-recall)
Run the tell-detection heuristics from the taxonomy, in this order (cheapest
first):

1. **Repetition** (most objective): near-duplicate passages, repeated scene
   skeletons, repeated emotional beats, unintended motif recurrence → L02, L03,
   L10, N05, SC05.
2. **Explicitness**: interpretation-statements, theme-statements, emotion
   labels + causes, significance-statements, symbol glosses → U01–U04, N02,
   C01, E01–E02, FS03, V02.
3. **Continuity**: fact/timeline/rule/world-state violations → L04, L05, L09,
   A02 (via the story model, interventions/03).
4. **Uniformity**: sentence-length variance, register monotony, scene-opening
   type distribution, scene-end button density, metaphor density, valence arc
   shape → P01–P07, S01–S06, SC01–SC04, T01–T04, E05, V01–V06.
5. **Template**: stage-ladder structures, milestone checklists, setup/payoff
   ledgers, stock humor → N01–N08, R02, FS02, H01, F01.

### Pass C — Evidence attachment (quality gate)
Each candidate finding is documented with:
- Tell ID(s) + the quoted passage(s);
- the pattern evidence (recurrence count, distribution shape, ledger
  violation);
- source IDs + confidence;
- the causal hypothesis (K-code);
- a **function test**: what does the passage do for the story (see
  taxonomy/20 §20.2)? Passages that do deliberate work are marked *intentional*
  and dropped from the intervention queue (not from the report).

### Pass D — Prioritization
Score findings (see `../spec/06-scoring.md`) and emit the intervention queue.
Priority = (severity × confidence × function-loss) − (false-positive risk ×
intent). Only findings above threshold enter the queue.

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

## 4. Output contract

Detection produces the **AnalysisReport** (schema: `../schemas/analysis-report.schema.json`):
one `finding` per candidate tell with: passage span, tell ID, confidence,
severity, cause, function-test result, intentionality verdict, proposed
intervention level (or `none`), and preservation-risk notes. Nothing in the
report mutates text; mutation happens only through the intervention pipeline
(`../spec/05-pipeline.md`).

## 5. What detection never does

- Never reports a probability of AI authorship (unreliable + harms authors,
  S14; non-native writers disproportionately flagged — Liang et al. 2023;
  Clarkesworld's concern, S44).
- Never flags based on a single sentence or word.
- Never treats Low/Folklore patterns as actionable.
- Never emits "make it more human" as an instruction (vague, detector-flavored,
  quality-neutral).
