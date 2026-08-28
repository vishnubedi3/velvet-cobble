# Taxonomy 17 — Genre Variation & Model-Specific Behavior

## 17.1 Principles

1. **No tell is assumed universal across genres.** Genre conditions both the
   generator's output (templates) and the *norms* used to judge it. A behavior
   that is a tell in literary fiction may be a contract requirement in romance.
   CAspER directly demonstrates genre-conditioned character generation (S29).
2. **The tell is a *deviation from the work's own contract*.** The skill defines
   "excessive" relative to (a) the genre's conventions, (b) the author's stated
   intent, and (c) the work's internal baseline — never relative to a
   genre-neutral style ideal.
3. **Evidence status matters.** The matrix below marks each cell: ● = directly
   measured; ◐ = indirectly supported (adjacent measurement or mechanism);
   ○ = practitioner-only; — = no evidence.

## 17.2 Genre × tell-cluster matrix

Rows: tell clusters. Columns: Fantasy, SF, Mystery, Thriller, Horror, Romance,
Literary, Historical, Comedy, Drama, YA, Short story, Long-form novel.
Cell = relative strength of the AI-tell signal for that genre (●●● strong,
●● moderate, ● weak), with evidence marker.

| Cluster | Fantasy | SF | Mystery | Thriller | Horror | Romance | Literary | Historical | Comedy | Drama | YA | Short | Novel |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Prose (P01–P07) | ●●● ◐ | ●● ◐ | ●● ◐ | ●● ◐ | ●● ◐ | ●●● ◐ | ●●● ◐ | ●● ◐ | ●● ○ | ●● ◐ | ●●● ◐ | ●● ◐ | ●● ◐ |
| Narrative (N01–N08) | ●● ● | ●● ● | ●● ◐ | ●● ◐ | ●● ◐ | ●●● ● | ●●● ● | ●● ○ | ●● ○ | ●●● ● | ●●● ◐ | ●● ● | ●●● ● |
| Character (C01–C08) | ●● ● | ●● ● | ●● ◐ | ●● ◐ | ●● ◐ | ●●● ● | ●●● ● | ●● ○ | ●● ○ | ●●● ● | ●●● ◐ | ●● ● | ●● ● |
| Dialogue (D01–D07) | ●● ○ | ●● ○ | ●● ○ | ●● ○ | ●● ○ | ●●● ◐ | ●●● ◐ | ●● ○ | ●● ○ | ●●● ◐ | ●●● ○ | ●● ○ | ●● ○ |
| Description (S01–S06) | ●●● ◐ | ●●● ◐ | ●● ○ | ●● ○ | ●●● ○ | ●●● ◐ | ●●● ◐ | ●●● ○ | ●● ○ | ●● ○ | ●● ○ | ●● ○ | ●● ○ |
| Emotion (E01–E05) | ●● ● | ●● ● | ●● ◐ | ●● ◐ | ●●● ● | ●●● ● | ●●● ● | ●● ○ | ●● ◐ | ●●● ● | ●●● ◐ | ●● ● | ●● ● |
| Pacing (T01–T06) | ●● ◐ | ●● ◐ | ●●● ◐ | ●●● ◐ | ●● ◐ | ●●● ◐ | ●●● ◐ | ●● ○ | ●● ○ | ●●● ◐ | ●●● ◐ | ●● ◐ | ●●● ● |
| Scene (SC01–SC06) | ●● ○ | ●● ○ | ●● ○ | ●● ○ | ●● ○ | ●●● ◐ | ●●● ◐ | ●● ○ | ●● ○ | ●●● ◐ | ●●● ○ | ●● ○ | ●●● ● |
| Voice (V01–V06) | ●● ● | ●● ● | ●● ◐ | ●● ◐ | ●● ◐ | ●●● ● | ●●● ● | ●● ○ | ●● ○ | ●●● ● | ●● ◐ | ●● ● | ●● ● |
| Subtext (U01–U05) | ●● ◐ | ●● ◐ | ●●● ◐ | ●● ◐ | ●● ◐ | ●●● ● | ●●● ● | ●● ○ | ●● ○ | ●●● ● | ●● ◐ | ●● ● | ●● ● |
| Worldbuilding (W01–W05) | ●●● ● | ●●● ● | ● ○ | ● ○ | ●○ ○ | ● ○ | ● ○ | ●● ○ | ● ○ | ● ○ | ●● ○ | ● ○ | ●● ● |
| Conflict (F01–F05) | ●● ● | ●● ● | ●● ○ | ●●● ○ | ●●● ● | ●●● ● | ●●● ● | ●● ○ | ●○ ○ | ●●● ● | ●● ◐ | ●● ○ | ●● ● |
| Foreshadowing (FS01–FS03) | ●● ○ | ●● ○ | ●●● ○ | ●●● ○ | ●● ○ | ●● ○ | ●● ○ | ●● ○ | ● ○ | ●● ○ | ●● ○ | ●● ○ | ●● ○ |
| Humor (H01–H04) | ●● ○ | ●● ○ | ● ○ | ● ○ | ● ○ | ●● ○ | ●○ ○ | ● ○ | ●●● ● | ●○ ○ | ●● ○ | ●● ○ | ●● ○ |
| Action (A01–A04) | ●●● ○ | ●●● ○ | ●○ ○ | ●●● ○ | ●● ○ | ● ○ | ● ○ | ●○ ○ | ●○ ○ | ● ○ | ●● ○ | ●○ ○ | ●● ○ |
| Romance (R01–R04) | ●● ○ | ●○ ○ | ●○ ○ | ●○ ○ | ●○ ○ | ●●● ● | ●●● ◐ | ●○ ○ | ●○ ○ | ●●● ◐ | ●●● ◐ | ●● ○ | ●●● ○ |
| Long-form (L01–L10) | ●●● ● | ●●● ● | ●● ◐ | ●● ◐ | ●● ◐ | ●●● ◐ | ●●● ◐ | ●● ○ | ●● ○ | ●●● ◐ | ●●● ◐ | — | ●●● ● |

### Reading notes

- **Mystery/thriller:** foreshadowing and setup/payoff signals are *contractual*
  — FS/SC flags there must clear a genre-contract gate before any action.
- **Horror:** E05 (positivity smoothing) and F05 (sanitization) fight the genre
  most directly; they are the highest-value fix targets in horror.
- **Romance:** the highest signal density overall (S29), but most of it overlaps
  the genre's own conventions — the *over-execution* (R01's articulated
  attraction, R02's empty ladder) is the tell, not the convention.
- **Literary:** V03/V05/U02 are the defining tells (absence of idiosyncrasy,
  absence of ambiguity, explanatory narrator) — and the highest false-positive
  risk, because human literary fiction also varies enormously (S02).
- **Short stories:** long-form tells (L*) don't apply; N06/N08 (neat closure,
  valence smoothing) dominate.
- **YA:** SC/T signals are strong and partly contractual (scene buttons are a YA
  norm) — contract-gate required.
- Evidence markers: ● = S03/S04/S28/S29/S42 (Tier 0 fiction); ◐ = S37/S41/S05
  (Tier 1 adjacent or mechanism); ○ = practitioner only (S44/S53). "—" = no
  evidence; treat as hypothesis only.

## 17.3 Model-family variation (evidence status)

| Dimension | Finding | Source |
|---|---|---|
| Stylometric tightness | GPT-4 clusters tighter than GPT-3.5 (more internal consistency); Llama 70B also tight; all separate from humans | S02 |
| Character diversity | Phi > (others) > Llama (least diverse character portrayals) | S29 |
| Register variation | ChatGPT shows very limited register variation vs. humans | S41 |
| Affect | Llama "more emotionally expressive"; GPT-4o "neutral and polished"; Mistral balanced | S37 |
| Stereotype rates | GPT-3.5 and GPT-4 personas more stereotypical than human-written; newer/aligned models shift values (more progressive on gender/sexuality than humans) | S07, S03 |
| Lexical overrepresentation | "Delve"-class overuse traced to RLHF preference data (not pretraining/architecture); persists in current iterations | S19 |
| Decoding | Decoding strategy alone changes detectability (RAID's 4 strategies); temperature/repetition penalties shift uniformity | S23 |
| Long-context degradation | Varies by model family (1.2–47.1% degradation; Gemini least, GPT-3.5/Claude-3-Haiku most in LongGenBench) | S31 |

### Consequences for the skill

1. **No cross-model word lists.** Lexical tells must be *estimated per
   generator* (frequency baselines per model family, per decoding settings).
2. **Thresholds are model-relative.** "Repetition," "uniformity," and
   "explicitness" thresholds must be recalibrated per model+decoding because
   their baselines differ (S23, S37).
3. **Prompt-specificity is a first-class axis.** Prompt templates change which
   tells appear (genre prompts invoke templates — S29); the skill always records
   the prompt class in its analysis metadata and re-weights accordingly.
4. **Re-verify after switching generators.** A calibration from model A does not
   transfer to model B without re-baselining (S23's cross-model generalization
   failures are the same phenomenon in reverse).
