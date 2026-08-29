# AGENTS.md — Central Operational Directive

**Project:** The Wind's Record
**Codename:** WINDLAW
**Status:** ACTIVE — governs all agent operations in this repository
**Last revised:** 2026-08-28
**Supersedes:** ambiguity in prior instructions; does not supersede `PROJECT.md` (the charter) or the canon files (the source of truth for world facts)

> **Project identity.** "The Wind's Record" is the name of the complete project — the world, its deep history, its lore, its research, its narrative, its characters, its civilizations, and their interconnected development. "WINDLAW" is the project's codename — a functional identifier for operational use. The **Samur Empire** is a fictional empire within the project's world; it is not the name of the project itself. The project encompasses far more than any single empire: the planet's billions of years, the sea's antiquity, the wind's foundational law, the deep civilizations, the pre-imperial history, and the novel that emerges from all of this.

> This file is the compulsory operational directive for any agent operating in this repository. It consolidates the user's established directives and adds the additional directives required by the project's current state, research methodology, worldbuilding process, narrative structure, continuity requirements, and autonomous authoring system. Every agent action must comply with this file.

---

## 1. The Two-Space Model (Permanent Operating State)

The project operates in two concurrent, permanent spaces:

### 1.1 Expansion Space — World Development (ALWAYS ACTIVE)

Expansion Space is the permanent environment for developing the underlying fictional world. It is **always active**. It does not pause, deactivate, or suspend when drafting begins. It is not a phase — it is a persistent authorial function.

**Active-duty requirements:**
- Every official chapter (beginning with Chapter One) requires active re-evaluation of the underlying world in relation to the chapter being developed.
- The agent must examine current lore, determine whether meaningful new development is warranted, and develop it autonomously where justified.
- Expansion is not optional because drafting is the immediate visible task.
- New lore must arise from the world's established conditions, internal logic, existing canon, developing narrative, or legitimate consequences.
- Do not expand for numerical volume. Do not manufacture filler lore, arbitrary facts, decorative history, unnecessary characters, artificial conflicts, or disconnected worldbuilding.
- The world should become more interconnected as it expands.

**Research and hypothesis development do not end when drafting begins.** The comparative research (`samur/01-research/`) and working hypotheses (`samur/03-hypotheses/`) remain active inputs to worldbuilding throughout the novel's development. New research may be commissioned when the narrative exposes a need for deeper understanding of a historical mechanism. New hypotheses may be formulated when the world's internal logic requires testing.

### 1.2 Drafting Space — Novel Production (ACTIVE)

Drafting Space is the permanent environment for producing the novel. It contains the actual narrative: chapters, scenes, dialogue, character interactions, descriptions, narrative sequences, perspective, pacing, structure, working prose, and final prose.

**Current state:** The pilot chapter is complete and awaiting user review. Chapter One requires explicit user authorization before it can begin.

**Drafting requirements:**
- Drafting Space must use the current canonical world state (`samur/02-canon/`).
- It must not freeze that state — the world continues developing.
- The novel is an interconnected lattice of people, houses, rulers, civilizations, histories, institutions, cultures, locations, conflicts, mysteries, political developments, personal narratives, and long-term consequences.
- Do not force the work into a single central premise. Do not reduce the novel to the Samur Empire alone. Do not impose a title prematurely.
- Reveal information through the narrative when appropriate. Do not convert the novel into a lore encyclopedia. Do not explain information solely because it exists in the database.

### 1.3 The Bidirectional Relationship

World development influences drafting. Drafting influences world development. A chapter may expose a need for new lore. New lore may expose consequences for future chapters. When drafting reveals a legitimate requirement for additional worldbuilding, develop it in Expansion Space, integrate it with the authoritative project state, verify its consequences, and return to the narrative naturally.

---

## 2. Authoritative State and Repository Protocol

### 2.1 The Repository Is the Primary Environment

This private GitHub repository is the authoritative source of truth and storage system. Chat is command intake and reporting only. Durable memory is committed to the session branch at the end of each working turn.

### 2.2 Pre-Action Protocol (Mandatory)

Before any consequential action:

1. **Inspect the repository.** Read the current state of relevant files.
2. **Consult the authoritative representation.** Check `samur/WORLD-MODEL.md` and the relevant canon files.
3. **Locate the relevant existing material.** Search before creating. Never assume something is absent because it was not found in the first location inspected.
4. **Establish the current canonical state.** Understand what is established, what is hypothesized, what is open, and what is deliberately mysterious.
5. **Identify dependencies, constraints, unresolved matters, and recent changes.** Check `Depends on` / `Dependents` links in canon files. Check `samur/CHANGELOG.md` for recent changes.
6. **Only then execute the action.**

### 2.3 Recovery Point Discipline

Before every consequential change:

1. **Create a recovery point** (an annotated git tag: `recovery/<operation-name>`).
2. **Perform the change.**
3. **Verify the resulting state** (cross-check against canon, dependency sweep, contradiction check).
4. **Persist the valid result** (commit to the session branch).
5. **Record the action** in `samur/CHANGELOG.md` and `ops/logs/`.

If a modification causes corruption, contradiction, loss, or unintended structural damage: stop further modification, inspect the affected state, restore the appropriate recovery point, verify the restored state, and record the failure and recovery. Never conceal failed operations. Never destroy the recovery history.

---

## 3. Canon Status Taxonomy

Every recorded item carries exactly one status. The status determines where it lives and how it may be cited.

| Status | Location | Definition | Citable as fact? |
|---|---|---|---|
| **CANON** | `samur/02-canon/` | Active, internally consistent fact of the Samur world. Requires provenance, dependency links, and a changelog entry. | Yes |
| **HYPOTHESIS** | `samur/03-hypotheses/` | Working hypothesis. Labeled with confirm/falsify conditions. | No — never citable as canon |
| **QUESTION** | `samur/04-questions/` | Open question with stakes. Two legitimate states: RESOLVED or NOT READY. No partial resolution. | Only when resolved |
| **RESEARCH** | `samur/01-research/` | Real-world comparative material. Never canon by location change; enters the world only via a transformation log. | No — analytical reference only |
| **PILOT / DRAFT** | `samur/narrative/` | Narrative prose. Not canon. New lore discovered during drafting enters `02-canon/` through the standard process. | No |
| **ANALYSIS** | `samur/05-quality/` | Quality analysis reports, intervention logs, preservation checks. | No — craft substrate only |
| **INFLUENCE** | register inside `01-research/` + `CHANGELOG` | Real-world counterpart recorded for each major CANON element, for drift control. | No |

### 3.1 Canonical Integrity

Established canon is binding unless deliberately revised through the authorized process. Do not casually alter foundational laws, cosmology, fixed chronology, established historical events, institutions, houses, rulers, established causal relationships, or deliberate mysteries. When new expansion conflicts with existing canon, identify the conflict. Do not silently overwrite either side. Do not conceal contradictions inside prose.

### 3.2 Deliberate Mysteries

Distinguish between deliberate mysteries, genuine contradictions, unanswered questions, and missing information. A deliberate mystery must remain a mystery until the project itself establishes otherwise. The current deliberate mysteries are:
- **Q-076:** the distant western maritime partner
- **Q-077:** the hidden history (the gap between source traditions)
- **Q-078:** the Kesra Charter's full text

### 3.3 Contradiction System

Maintain an active contradictions record in `samur/CONTRADICTIONS.md`. For every genuine contradiction: record it, identify affected canon, identify dependent material, determine scope, determine whether sufficient information exists for complete resolution, resolve completely when justified, update every affected dependency, verify the result, and remove from the active record only after verification. If sufficient information does not exist, leave it unresolved. Do not partially resolve canonical contradictions.

---

## 4. Per-Chapter Authoring Cycle

Beginning with Chapter One, apply this cycle continuously:

```
CONSULT AUTHORITATIVE PROJECT STATE
↓
UNDERSTAND CURRENT CANON
↓
RE-EVALUATE THE WORLD FOR THE CHAPTER (Expansion Space)
↓
IDENTIFY MEANINGFUL EXPANSION
↓
DEVELOP NEW LORE WHERE JUSTIFIED
↓
CHECK NEW LORE AGAINST CANON
↓
INTEGRATE CONSEQUENCES
↓
PERSIST SIGNIFICANT CHANGES
↓
RUN PRE-FLIGHT CANON GUARD (skills/fiction-writing/)
↓
DRAFT THE CHAPTER (Drafting Space)
↓
RUN POST-GENERATION ARTIFACT REDUCTION (skills/ai-fictional-tells-skill/)
↓
PERSIST SKILL REPORT IN samur/05-quality/
↓
OBSERVE NEW NARRATIVE CONSEQUENCES
↓
RE-EVALUATE THE WORLD AGAIN (Expansion Space)
↓
EXPAND AGAIN WHERE JUSTIFIED
↓
VERIFY CONTINUITY
↓
PERSIST
↓
LOG IN ops/logs/ AND samur/CHANGELOG.md
↓
CONTINUE
```

The evaluation is mandatory. The quantity of expansion is not. If expansion is not justified, preserve the existing world.

---

## 5. Originality and Research Protocol

### 5.1 The No-Transplant Rule

The Sumur world must be independently constructed. Real-world history may be researched for analytical understanding. Research must not become fictional source material. Study historical societies to understand mechanisms, not to reproduce their content.

Do not reproduce recognizable real-world civilizations, empires, kingdoms, rulers, wars, borders, institutions, political systems, cultures, historical sequences, or administrative structures under fictional names. Broad similarities in how complex societies develop are acceptable. Direct adaptation is not.

### 5.2 Transformation Method

No institution or event enters canon without either a 5-step transformation log (see `samur/01-research/comparative/README.md`) or explicit material/geographic reasoning. Every major CANON element records its historical counterpart(s) in the influence register. A Samur institution that is merely a renamed historical counterpart is a redesign candidate.

### 5.3 Active Research

The comparative research in `samur/01-research/` (six historical models + four religious systems) and the transformation logs remain active inputs. New research may be commissioned when:
- The narrative exposes a need for deeper understanding of a historical mechanism.
- A new worldbuilding domain requires comparative grounding.
- An existing hypothesis requires additional real-world evidence to confirm or falsify.

Research entries follow the status taxonomy: they are RESEARCH, never canon by location change.

---

## 6. Repository Architecture

### 6.1 Top-Level Structure

```
velvet-cobble/
├── AGENTS.md                          # THIS FILE — central operational directive
├── PROJECT.md                         # Project charter (mission, phases, taxonomy)
├── README.md                          # Top-level overview
├── samur/                             # The world + the novel
│   ├── 00-audit/                      # Repository and workspace audits
│   ├── 01-research/                   # Real-world comparative research (active)
│   ├── 02-canon/                      # Active canon (the authoritative world state)
│   ├── 03-hypotheses/                 # Working hypotheses (active)
│   ├── 04-questions/                  # Open questions register
│   ├── 05-quality/                    # Narrative quality analysis reports
│   ├── narrative/                     # The novel (clean prose only)
│   ├── CHANGELOG.md                   # Canon change log
│   ├── CONTRADICTIONS.md              # Active contradictions register
│   ├── WORLD-MODEL.md                 # Authoritative one-page summary
│   └── README.md                      # Material map and naming conventions
├── skills/                            # All agent skills
│   ├── fiction-writing/               # Pre-generation canon guard
│   ├── ai-fictional-tells-skill/      # Post-generation artifact reduction
│   ├── INTEGRATION.md                 # Skill integration record
│   └── README.md                      # Skills overview
├── ops/                               # Operational records
│   ├── logs/                          # Agent operation logs
│   ├── recovery/                      # Recovery point documentation
│   └── README.md                      # Ops overview
└── site/                              # Reader-facing website (SEPARATE ENVIRONMENT)
    └── README.md                      # Scope, ownership, boundary rules
```

### 6.2 Separation Rules

- **`samur/narrative/`** contains only clean, reader-facing prose. No reports, no analysis outputs, no lore documents, no canon files.
- **`samur/05-quality/`** contains only quality analysis reports. No narrative prose, no canon files.
- **`samur/02-canon/`** contains only established canon. No narrative prose, no reports.
- **`samur/01-research/`** contains only real-world comparative research. Never canon by location change.
- **`ops/`** contains operational records. Never canon, never narrative prose.
- **`skills/`** contains agent skills. Never canon, never narrative prose.
- **`site/`** is the reader-facing website environment. It is a **separate working environment** — owned by the website agent, not the authoring agent. It may consume approved narrative material from `samur/narrative/` for publication, but it must not contain canon, lore, research, narrative development, quality analysis, or any authoring-system artefact. The authoring agent must not operate in `site/`.
### 6.3 Naming Conventions

- **Canon files:** `<DOMAIN>-<NN>_<slug>.md` (e.g., `GEO-01_material_geographic_foundation.md`)
- **Question files:** `Q-<NNN>_<slug>.md` (e.g., `Q-076_distant_western_partner.md`)
- **Audit files:** `<YYYY-MM-DD>-<operation>.md` (e.g., `2026-08-28-initial-cross-check.md`)
- **Quality reports:** `<tool>-report-<target>.md` (e.g., `skill-report-pilot.md`)
- **Narrative files:** `pilot-chapter.md` (pilot); `ch<NN>-<slug>.md` (chapters)
- **Recovery tags:** `recovery/<operation-name>` (annotated git tags)
- **Log files:** `<YYYY-MM-DD>-<operation>.md` in `ops/logs/`

### 6.4 README Requirement

Every major folder has a `README.md` explaining its purpose, contents, relationships, and operating rules. The READMEs are:
- `samur/README.md` — material map, file naming, templates, promotion rules
- `samur/02-canon/README.md` — canon file template, dependency rules
- `samur/01-research/comparative/README.md` — transformation method, influence register
- `samur/01-research/religious-systems/README.md` — religious systems as institutions
- `samur/03-hypotheses/README.md` — hypothesis template, confirm/falsify conditions
- `samur/04-questions/README.md` — question template, status rules
- `samur/05-quality/README.md` — quality analysis purpose, naming, governance
- `samur/narrative/README.md` — narrative purpose, naming, governance, relationship to canon
- `skills/README.md` — skills overview, invocation rules
- `ops/README.md` — operational records purpose, logging rules
- `site/README.md` — website project overview (independent)

### 6.5 Website Directory Isolation (Permanent Boundary)

`site/` is a **completely separate project** that exists within the repository but is **outside the authoring project**. The root `AGENTS.md`, `PROJECT.md`, and all authoring directives have **no authority** over `site/`. The website agent independently defines its own governance, architecture, workflow, and documentation.

**The authoring agent must:**
- Not develop, modify, manage, govern, review, or otherwise interfere with `site/`.
- Not consult, reference, inspect, acknowledge, or incorporate `site/` contents into any decision about the world, lore, research, canon, narrative, or authoring workflow.
- Treat `site/` as outside its operational awareness during all normal authoring work.
- Not assume anything about how the website agent will develop the website.

**The only permitted interaction** is practical interoperability when explicitly required — such as allowing the website agent to receive approved narrative material from `samur/narrative/` for publication. Even then, the authoring agent does not operate inside `site/`; it makes the material available in its own canonical location.

This boundary is permanent and applies to every agent operating under this directive.

---

## 7. Narrative Quality Standards

### 7.1 Pre-Generation Canon Guard

Before every chapter, run the pre-flight canon check (`skills/fiction-writing/anti-patterns.md`):
1. Canon check: every named institution, place, and custom exists in `02-canon/`.
2. Name-pool check: character names come from the established Samur register.
3. Coincidence audit: at most one per major arc, flagged.
4. Tic scan: weather-opening, tricolons, "as if" count, motif reuse.
5. Anachronism scan against the era vocabulary list.
6. Consequence ledger: does the scene end with a cost or constraint the next scene must inherit?

### 7.2 Post-Generation Artifact Reduction

After every chapter, run the `ai-fictional-tells-skill` post-generation pipeline:
1. Contract extraction (genre, perspective, style anchors, content boundaries).
2. Analysis (build story model, run framework detectors, attach evidence).
3. Prioritization (score findings).
4. Intervention (apply minimal edits, level by level, with preservation checks).
5. Re-evaluation (verify preservation dimensions, re-check tells on changed spans).
6. Report (persist in `samur/05-quality/`).

### 7.3 Prose Anti-Patterns

The following are banned or restricted in narrative prose:
- Weather/light as mood shorthand at scene openings (banned unless functionally loaded)
- Tricolon overuse ("not X, not Y, but Z")
- "As if" similes more than once per page
- Default adverb-verb crutches (slowly, gently, quietly as unexamined modifiers)
- Double-explained metaphor (the image plus a second sentence restating it)
- Recycled motifs (the same image reused across scenes without earning it)
- Exposition dumps (characters explaining shared knowledge; world information must arrive through friction)
- Uniform register (all characters sharing one rhythm and vocabulary class)
- Unearned resolution (tension released without cost, consequence, or lingering damage)
- Narrator-explains-significance (the narrator tells the reader why something matters when the scene already carries it)

---

## 8. Autonomous Authorial Judgment

Within established constraints, exercise autonomous creative judgment. Determine:
- What requires expansion and what does not
- What should be revealed and what should remain unknown
- What should become canon and what should remain temporary
- What consequences should follow
- What belongs in the novel and what belongs only in the world

Do not repeatedly ask the user to make routine creative decisions. Do not invent user requirements. Respect explicit user-controlled gates (the pilot review gate, the Chapter One authorization gate).

---

## 9. No Artificial Productivity

Do not manufacture activity merely to appear productive. Do not create lore without purpose. Do not create contradictions. Do not create mysteries. Do not create historical events. Do not expand a subject merely because it is currently underdeveloped. Do not confuse greater volume with greater depth. Every consequential addition must have a legitimate reason to exist within the world or narrative.

---

## 10. Agent Logging

Maintain concise operational logs in `ops/logs/` for meaningful actions. Record:
- Action performed
- Project area affected
- Significant result
- Material created or changed
- Verification performed
- Recovery point created
- Dependencies affected
- Contradictions discovered or resolved
- Matters left unresolved

Do not record hidden chain-of-thought. Do not reproduce this directive file in the logs.

---

## 11. Current Execution State

```
INITIAL EXPANSION GATEWAY = COMPLETE
EXPANSION SPACE = ALWAYS ACTIVE
DRAFTING SPACE = ACTIVE
CURRENT DRAFTING OBJECTIVE = PILOT REVIEW (awaiting user approval)
CHAPTER ONE = NOT YET AUTHORIZED
CANON FILES = 34
QUESTIONS = 87 (77 resolved + 1 partially resolved + 3 intentionally unresolved + 4 open + 1 NOT READY + 1 open deep unknown)
CONTRADICTIONS = 1 carried (CC-08, the long-reign cluster)
DELIBERATE MYSTERIES = 3 (Q-076, Q-077, Q-078 — preserved)
```

---

## 12. Permanent Operating State After Chapter One Authorization

After the user authorizes Chapter One, the following becomes permanent:

```
EXPANSION SPACE = ALWAYS ACTIVE
DRAFTING SPACE = ALWAYS ACTIVE
RESEARCH = ACTIVE (new research commissioned as needed)
HYPOTHESES = ACTIVE (new hypotheses formulated as needed)
```

For every chapter: re-evaluate the world, develop new lore when justified, integrate it with canon, verify its consequences, run the pre-flight canon guard, draft the chapter, run the post-generation artifact reduction, persist the skill report, observe what the chapter reveals, expand again when justified, maintain continuity, persist the result, log the operation.

The world and the novel develop together throughout the series. The agent must never interpret the beginning of drafting as the end of worldbuilding. Expansion Space is an active, autonomous, continuously operating component of the authoring system.
