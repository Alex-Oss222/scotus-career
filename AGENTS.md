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
- `render-inputs/` — written by Run: the eleven-block Render Input for every event in the chunk, plus chunk metadata. Append-only.
- `output/` — written by Render: the public render of each chunk under the Contract. Append-only.
- `close/` — the three replacement trackers and the Term-Close Dossier, frozen at term close.

## The four tasks the user gives

**"Open October Term <year>."** Validate `state/` as the opening trackers against the Engine's term-opening baseline rules, read `case-list.md`, build the Full-Term Event Manifest, and write `terms/OT<year>/workspace.md`. Report any conflict or missing inventory item; do not invent one.

**"Run October Term <year>, chunk <n>."** Take `terms/OT<year>/briefs/OT_<year>CHUNK<n>.md` (and the matching `runtime/` files if present). Reconstruct the Current Term State from `state/` and `workspace.md`. Adjudicate every event in the chunk under the Engine, in effective-date order. For each completed event write its Decision Record to `records/`, and write the chunk's Render Inputs — the Engine's eleven blocks per event, in order, plus the chunk metadata — to `render-inputs/OT_<year>CHUNK<n>.md`; replace `workspace.md`. Do not write the public render. A stopped matter is listed in the chunk metadata with its exact blocker and left open — never resolved by guessing.

**"Render October Term <year>, chunk <n>."** A separate task. Read only `render-inputs/OT_<year>CHUNK<n>.md`, `foundation/RENDER_CONTRACT.md`, and the Render form, Holdings writing standard, and Voice sections below. Write `output/OT_<year>CHUNK<n>.md`. Do not open briefs, records, or sources; do not research, revisit votes, change coalitions, or add holdings. If a Render Input lacks something the Contract needs, render the entry as far as it goes and name the exact gap in the Simulation Workflow Blockers section.

**"Close October Term <year>."** Only after every manifest item is completed, corrected, or expressly carried forward. Build the Term-Close Dossier, derive the three replacement trackers as one coordinated set, write them to `terms/OT<year>/close/`, and replace `state/`. Do not change any adjudication during close.

The user may also say, in plain words, that the Court issues an order or takes up a lower-court case. Record it the way the Engine requires — an Admitted Source Record, a manifest change, or a Standing State entry — then continue.

## Mode

Each task is one context that sees the neutral packet, the comparator, and Stone's position together. That is the Engine's single-conversation mode: keep its stage order and frozen handoffs, and state in each Decision Record that true blindness was unavailable. Do not describe the process as blind. When `runtime/` split files exist, read the `_NEUTRAL` file first and freeze the provisional non-Stone commitments before opening `_COMPARATOR`; open `_STONE` last.

## Research

Follow Engine §14. Sources in order of preference:

1. The Internet Archive's Records and Briefs collection (`us-supreme-court`; one item per docket, holding the petition, briefs, joint appendix, and opinion as text PDFs). The most complete source for cases through 2006.
2. CourtListener and the Caselaw Access Project (courtlistener.com search and API; static.case.law) — the judgment below in every case, and any earlier opinion in full text, including each Justice's date-eligible opinions and joins.
3. loc.gov — the United States Reports; and the 1988 edition of the United States Code for statutory text as it stood in 1991.
4. supremecourt.gov — opinions, orders, Journals, transcripts. Strongest from 2007 onward.
5. govinfo.gov — the 1994 edition of the United States Code (the closest full edition after 1991), the Statutes at Large, and the Federal Register from 1994; congress.gov for legislative history.
6. Cornell LII and Oyez for opinions and argument audio.
7. HathiTrust (babel.hathitrust.org) only as a last resort, for a state code or session law whose exact 1991 text matters and is not quoted in the opinion or briefs.

Do not rely on Justia (it blocks automated requests) or on any aggregator alone. Send a browser User-Agent when a site refuses the default one. Download a PDF and read its text in full; do not skim the first pages and infer the rest. Scholarship and commentary are context only, never authority, and anything written after the event's date is not in-world. Record the research cutoff in every Decision Record.

## Render form

Decide the render form for each event when projecting its Render Input, and state it there ("Render form: compact" or "Render form: full", with the basis). The renderer follows that choice.

- **Compact form** is allowed only when both hold: the judgment margin is two votes or more (9-0, 8-1, 7-2, 6-3, or the reduced-Court equivalents such as 8-0, 7-1, 6-2, 5-3), and nothing material changed from the historical comparator. It is the Contract's routine narrative, but it still carries every supplied element in prose: argued and decided dates, route to the Court, questions, vote by component with names, every writing with author and joins, separate positions, limits and questions not reached, precedent treatment and current-law effect, and mandate, remedy, and stage.
- **Full form** is required otherwise: the Contract's standard form (complex where Contract section 4 calls for it), with the Judgment table and the Opinion Topology table.
- **Material change** means any of: a different judgment or disposition on any component; a different controlling proposition, or a different coalition supporting it; a Justice other than Stone voting differently from history; a different remedy, mandate, or remand; a matter history decided that this Court leaves undecided, or the reverse; a new or changed reusable doctrine; a different treatment of precedent. A change that follows solely from Stone casting the vote Rehnquist cast (a different author for the Court, a margin one vote different) is not material by itself.
- A 5-4 judgment, an equal division, or a fracture with no Opinion of the Court always takes the full form.
- Renders publish only what the Court publishes: dispositions, opinions, and noted statements. Never the conference or certiorari poll.

## Records

Every Canonical Decision Record carries its adaptive audit annex: each non-Stone Justice's provisional commitment and ground, the historical-comparator reconciliation, and any departure with its Justice-specific basis. A compact table is enough for routine cases. The annex, not the render, is where a departure from history is explained.

## Holdings writing standard

The render can only project what the record holds, so write the law of the decision at full depth in the record's controlling-holding section and carry it into the Render Input's Holdings block unchanged. For every controlling proposition and every independently sufficient alternative holding:

- **Holding and operative rule.** The complete rule — trigger, what is required or forbidden, the legal consequence, any operative qualification — in one or two sentences a later court could apply without reading anything else.
- **Authority.** The writing, the Justices who join it at that level of generality, and why it controls.
- **Controlling explanation.** 120–200 words in the Court's voice, containing only reasoning the controlling coalition adopted: the precedents relied on and what each supplies; the application to this record; why the principal contrary argument fails; what the Court expressly leaves open. No dicta, no Stone-only reasoning, no later law.
- **Precedent treatment.** One line per earlier decision the holding materially relies on, distinguishes, limits, extends, or overrules: the treatment in ordinary words and its consequence for that precedent's present force.

Use the Contract's labeled block in the full form; in the compact form keep the same four elements in prose at the same depth. A routine unanimous application still gets the explanation; it will simply be shorter than a rule change. Do not pad.

## Voice

Write the render the way the Court writes for the public, not the way a treatise writes for specialists: plain declarative sentences; the rule first in ordinary words, then its precise legal formulation; every cited precedent followed by a clause saying what it supplies here; terms of art only when needed, explained on first use; no Latin where English will do; the Court's voice ("The Court holds ..."), never "the model" or "the simulation." A careful non-lawyer should be able to follow every step; a lawyer should find nothing imprecise.

## Rules that never bend

1. Stone's approved position controls Stone. The Engine may not fill a missing Stone choice; stop the matter and say exactly what is missing.
2. Nothing in `records/`, `render-inputs/`, `output/`, or `close/` is modified once written. A correction is a new file that names what it corrects.
3. Do not invent quotations, votes, dockets, dates, findings, concessions, or sources.
4. Only controlling law changes current doctrine. A render never changes substance.
5. No scores, dashboards, ideology labels, win-loss framing, or predictions. No fictional conference dialogue.
6. Use the shell to read files, fetch sources, and check arithmetic, chronology, and cross-references. Tools check consistency; they never decide legal meaning.
7. If anything needed to continue is missing or in conflict, stop the affected matter, name the exact blocker, and finish everything else.
