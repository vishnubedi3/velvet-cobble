# Framework 07 — Genre-Aware Analysis Framework

**Purpose.** Turn genre from a source of false positives into a *filter*: every
tell flag must clear the genre contract before it can become an intervention.

**Sources:** S29 (genre conditions generation), S46/S47 (genre-sensitive
judging/identification), S03/S04/S28 (baseline findings), plus genre craft
literature for the contract definitions (Tier 3, labeled).

## 1. The genre contract table (abridged)

| Genre | Contractual conventions (never flagged as tells) | Where AI over-executes (flagged) |
|---|---|---|
| **Fantasy** | establishing shots; system specs; quest templates; archetype characters | the *default* quest (N04); encyclopedia lore (W01); generic invented detail (W03); naming uniformity |
| **Science fiction** | world exposition; spec-driven plots (hard SF) | exposition *blocks* vs. dramatized (W01); explicitness (U/N clusters); flat characters under ideas |
| **Mystery** | setup/payoff ledger; foreshadowing; closure at denouement; withheld information | the *perfect* ledger (N03/FS02 — exempt if the solution is fairly planted); stated-purpose scenes; premature resolution (F04) |
| **Thriller** | scene buttons/cliffhangers; escalation ladders; competence | button fatigue (T03/SC04); escalation without change of kind (F01); sanitized consequences (F05) |
| **Horror** | dread-building; the uncanny; (optionally) bleak endings | positivity smoothing (E05 — the genre's main AI tell); sanitized stakes (F05); explained fear (E01) |
| **Romance** | HEA; emotional transparency beats; milestone ladder; reconciliation | articulated attraction (R01); empty ladder (R02); residue-free reconciliation (R03); over-analysis (R04); transparent characters (C08/S29) |
| **Literary** | ambiguity; essayistic narrators; interiority; idiosyncrasy | explanatory narrator (V02); no ambiguity (V05); generic polish (V03); theme-vehicle structure (N01) |
| **Historical** | period texture; specific setting detail | generic period flavor (W05); modern-sensibility characters (C04/E05); info-dump history (W01) |
| **Comedy** | comic rhythm; callbacks; running gags | stock jokes (H01); explained jokes (H02); uniform wit (H03) |
| **Drama** | emotional arcs; conflict; interiority | emotional captioning (C01/E01); fast reconciliation (T05/R03); polite conflict (C05) |
| **YA** | scene buttons; clear arcs; voice | over-executed buttons (T03); didactic themes (N02/N07); instant backstory (C02) |
| **Short story** | compression; single effect; open or resonant endings | neat closure (N06); valence smoothing (N08); template structure (N04) |
| **Long-form novel** | subplots; digression; texture | all L-tells (taxonomy/18); ledger rigidity (N03) |

## 2. The genre gate (runs before every intervention)

For each flagged tell:
1. Look up the genre in the contract table.
2. If the flagged pattern is **contractual** → the flag is reclassified as
   "contract, verified" and produces no intervention (it may still appear in
   the report as context).
3. If the pattern is contractual but **over-executed** → intervention targets
   the over-execution only (e.g., romance ladder keeps the ladder, loses the
   empty rungs).
4. If non-contractual → normal handling.
5. **Subgenre overrides genre.** Cozy mystery ≠ noir; the contract is taken
   from the narrowest applicable category the author has declared.

## 3. Genre declaration (required input)

The input schema requires a genre/subgenre field (`../spec/03-input-schema.md`).
When the author declines to declare a genre, the skill:
- infers a *provisional* genre for analysis only;
- marks every genre-gated decision `provisional`;
- escalates contract-sensitive findings to the author instead of acting.

## 4. Genre-sensitive measurement

- **Baselines are genre-relative.** Metaphor density, hedge density, closure
  rate, and valence depth are compared to the *genre's* baseline distribution
  (from reference corpora where available; otherwise from the work's own
  internal baseline).
- **LLM-judge distrust.** LLM judges of literary quality are genre-biased
  (S46) and poorly correlated with experts (S04) — genre-aware evaluation
  must use the benchmark's rubric with human spot-checks
  (`../spec/09-evaluation-benchmark.md`).

## 5. Preservation checks (binding)

- PV-12 (genre): no intervention may remove a contractual element.
- PV-13 (intent): genre conventions the author has *chosen to subvert* are
  authorial intent, not tells — the author's declared subversions override
  the contract table.
