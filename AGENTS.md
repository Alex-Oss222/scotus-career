# AGENTS.md — Stone-Zsela Supreme Court term simulation

This repository is a simulated Supreme Court of the United States, run one October Term at a time. The user controls one Justice, Chief Justice Alex-Lamar Stone-Zsela, who replaces Rehnquist at the opening of October Term 1991 (October 7, 1991). Everything else — the other Justices, the Court's actions, and the law that results — is produced under the Engine.

You are the Engine's operator for one task at a time. Read this file, then the three foundation files, before doing anything else.

## Files that govern every task

| File | Role |
|---|---|
| `foundation/ENGINE.md` | The Supreme Court Term Simulator Engine. Controls adjudication, chronology, participation, coalitions, records, and term close. |
| `foundation/RENDER_CONTRACT.md` | The Judicial Turn Output Render Contract. Controls how a completed event is presented. Presentation only. |
| `foundation/COURT_COMPOSITION.md` | Who sits on the Court, seniority, seat lines, and circuit allotments, OT1991–OT2026. |
| `foundation/CASE_BRIEF_TEMPLATE.md` | The structure of a case brief: Section I neutral packet, Section II Stone position, Section III historical comparator. |
| `foundation/templates/` | The instructions for the three trackers. |

Never edit anything under `foundation/`.

## Current state

`state/` holds the three trackers the Engine calls Holdings, Standards and Tests, and Standing State. They are the term-opening baseline for the term in progress. Between chunks, current-term law and procedure live in the term's `workspace.md`, not in `state/`. The trackers are replaced only by a Close task, all three together, under the Engine's Centralized Term-Close Protocol.

## Term folders

`terms/OT<year>/`

- `case-list.md` — the user's term-wide inventory of cases and Court actions (the Engine's "lightweight term-wide inventory").
- `briefs/` — the user's case briefs, one file per chunk of about ten cases (`OT_<year>CHUNK<n>.md`). Inputs. Never edit them; Stone's words are never altered.
- `runtime/` — when present, the user's split of each chunk into `_NEUTRAL`, `_STONE`, and `_COMPARATOR` files.
- `workspace.md` — the Term Workspace: Full-Term Event Manifest, Term Working Ledger index, latest Term Continuity Note, Current-Term Neutral Projection. Written by Open, replaced by every Run.
- `records/` — one Canonical Decision Record or Admitted Source Record per completed event, named by case, event type, and date. Append-only.
- `output/` — the public render of each chunk, produced under the Contract. Append-only.
- `close/` — the three replacement trackers and the Term-Close Dossier, frozen at term close.

## The three tasks the user gives

**"Open October Term <year>."** Validate `state/` as the opening trackers against the Engine's term-opening baseline rules, read `case-list.md`, build the Full-Term Event Manifest, and write `terms/OT<year>/workspace.md`. Report any conflict or missing inventory item; do not invent one.

**"Run October Term <year>, chunk <n>."** Take `terms/OT<year>/briefs/OT_<year>CHUNK<n>.md` (and the matching `runtime/` files if present). Reconstruct the Current Term State from `state/` and `workspace.md`. Adjudicate every event in the chunk under the Engine, in effective-date order. For each completed event write its Decision Record to `records/` and project its Render Input; render the chunk under the Contract to `output/OT_<year>CHUNK<n>.md`; replace `workspace.md`. A stopped matter is reported in the render's Simulation Workflow Blockers section and left open — never resolved by guessing.

**"Close October Term <year>."** Only after every manifest item is completed, corrected, or expressly carried forward. Build the Term-Close Dossier, derive the three replacement trackers as one coordinated set, write them to `terms/OT<year>/close/`, and replace `state/`. Do not change any adjudication during close.

The user may also say, in plain words, that the Court issues an order or takes up a lower-court case. Record it the way the Engine requires — an Admitted Source Record, a manifest change, or a Standing State entry — then continue.

## Mode

Each task is one context that sees the neutral packet, the comparator, and Stone's position together. That is the Engine's single-conversation mode: keep its stage order and frozen handoffs, and state in each Decision Record that true blindness was unavailable. Do not describe the process as blind. When `runtime/` split files exist, read the `_NEUTRAL` file first and freeze the provisional non-Stone commitments before opening `_COMPARATOR`; open `_STONE` last.

## Research

Follow Engine §14. Sources in order of preference:

1. The Internet Archive's Records and Briefs collection (`us-supreme-court`; one item per docket, holding the petition, briefs, joint appendix, and opinion as text PDFs). The most complete source for cases through 2006.
2. supremecourt.gov — opinions, orders, Journals, transcripts. Strongest from 2007 onward.
3. loc.gov — the United States Reports.
4. govinfo.gov.
5. Cornell LII and Oyez for opinions and argument audio.

Do not rely on Justia (it blocks automated requests) or on any aggregator alone. Download a PDF and read its text in full; do not skim the first pages and infer the rest. Record the research cutoff in every Decision Record.

## Render form

Decide the render form for each event when projecting its Render Input, and state it there ("Render form: compact" or "Render form: full", with the basis). The renderer follows that choice.

- **Compact form** is allowed only when both hold: the judgment margin is two votes or more (9-0, 8-1, 7-2, 6-3, or the reduced-Court equivalents such as 8-0, 7-1, 6-2, 5-3), and nothing material changed from the historical comparator. It is the Contract's routine narrative, but it still carries every supplied element in prose: argued and decided dates, route to the Court, questions, vote by component with names, every writing with author and joins, separate positions, limits and questions not reached, precedent treatment and current-law effect, and mandate, remedy, and stage.
- **Full form** is required otherwise: the Contract's standard form (complex where Contract section 4 calls for it), with the Judgment table and the Opinion Topology table.
- **Material change** means any of: a different judgment or disposition on any component; a different controlling proposition, or a different coalition supporting it; a Justice other than Stone voting differently from history; a different remedy, mandate, or remand; a matter history decided that this Court leaves undecided, or the reverse; a new or changed reusable doctrine; a different treatment of precedent. A change that follows solely from Stone casting the vote Rehnquist cast (a different author for the Court, a margin one vote different) is not material by itself.
- A 5-4 judgment, an equal division, or a fracture with no Opinion of the Court always takes the full form.
- Renders publish only what the Court publishes: dispositions, opinions, and noted statements. Never the conference or certiorari poll.

## Records

Every Canonical Decision Record carries its adaptive audit annex: each non-Stone Justice's provisional commitment and ground, the historical-comparator reconciliation, and any departure with its Justice-specific basis. A compact table is enough for routine cases. The annex, not the render, is where a departure from history is explained.

## Rules that never bend

1. Stone's approved position controls Stone. The Engine may not fill a missing Stone choice; stop the matter and say exactly what is missing.
2. Nothing in `records/`, `output/`, or `close/` is modified once written. A correction is a new file that names what it corrects.
3. Do not invent quotations, votes, dockets, dates, findings, concessions, or sources.
4. Only controlling law changes current doctrine. A render never changes substance.
5. No scores, dashboards, ideology labels, win-loss framing, or predictions. No fictional conference dialogue.
6. Use the shell to read files, fetch sources, and check arithmetic, chronology, and cross-references. Tools check consistency; they never decide legal meaning.
7. If anything needed to continue is missing or in conflict, stop the affected matter, name the exact blocker, and finish everything else.
