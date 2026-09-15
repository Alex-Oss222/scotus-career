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

`state/` holds the three trackers the Engine calls Holdings, Standards and Tests, and Standing State. They are the term-opening baseline for the term in progress. Between chunks, current-term law and procedure live in the term's `workspace.md`, not in `state/`. The trackers are replaced only at term close, as one coordinated set, under the Close protocol below. Standing State holds only the Court's setting: roster and seniority, circuit allotments, standing practices, and the docket of cases brought up; it never carries positions, dependencies, or history.

## Term folders

`terms/OT<year>/`

- `case-list.md` — the user's term-wide inventory of cases and Court actions (the Engine's "lightweight term-wide inventory").
- `briefs/` — the user's case briefs, one file per chunk of about ten cases (`OT_<year>CHUNK<n>.md`). Inputs. Never edit them; Stone's words are never altered.
- `runtime/` — when present, the user's split of each chunk into `_NEUTRAL`, `_STONE`, and `_COMPARATOR` files.
- `workspace.md` — the Term Workspace: Full-Term Event Manifest, Term Working Ledger index, latest Term Continuity Note, Current-Term Neutral Projection. Written by Open, replaced by every Run.
- `records/` — one Canonical Decision Record or Admitted Source Record per completed event, named by case, event type, and date. One file per event: a user-authorized correction replaces the file in place and states its lineage (versions and commit hashes).
- `render-inputs/` — written by Run: the eleven-block Render Input for every event in the chunk, plus chunk metadata. One file per chunk: a correction replaces the event’s block in place and updates the chunk metadata; the other blocks stay byte-identical.
- `output/` — written by Render: the public render of each chunk under the Contract. One file per chunk: a correction replaces the event’s entry in place; the other entries stay byte-identical.
- `close/` — the three replacement trackers and the Term-Close Dossier, frozen at term close.

## The four tasks the user gives

**"Open October Term <year>."** Validate `state/` as the opening trackers against the Engine's term-opening baseline rules, read `case-list.md`, build the Full-Term Event Manifest, and write `terms/OT<year>/workspace.md`. Report any conflict or missing inventory item; do not invent one.

**"Run October Term <year>, chunk <n>."** Take `terms/OT<year>/briefs/OT_<year>CHUNK<n>.md` (and the matching `runtime/` files if present). Reconstruct the Current Term State from `state/` and `workspace.md`. Adjudicate every event in the chunk under the Engine, in effective-date order. For each completed event write its Decision Record to `records/`, and write the chunk's Render Inputs — the Engine's eleven blocks per event, in order, plus the chunk metadata — to `render-inputs/OT_<year>CHUNK<n>.md`; replace `workspace.md`. Do not write the public render. A stopped matter is listed in the chunk metadata with its exact blocker and left open — never resolved by guessing.

**"Render October Term <year>, chunk <n>."** A separate task. Read only `render-inputs/OT_<year>CHUNK<n>.md`, `foundation/RENDER_CONTRACT.md`, and the Render form, Holdings writing standard, and Voice sections below. Write `output/OT_<year>CHUNK<n>.md`. Do not open briefs, records, or sources; do not research, revisit votes, change coalitions, or add holdings. If a Render Input lacks something the Contract needs, render the entry as far as it goes and name the exact gap in the Simulation Workflow Blockers section.

**Closing a term** is staged, one task per pass; see "Close protocol" below. Nothing in `state/` changes until the Commit pass.

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

**Completeness checks** (added September 15, 2026, from the user’s Casey version 1.1 handoff; they bind every record, Render Input, and render from now on, and later briefs): state every material exception, qualification, alternative, and triggering condition the analysis uses, in its own terms; never write “the specified exception” or “the stated qualification” unless the same entry supplies the terms; keep permission and obligation distinct (“may be omitted” never becomes “must be omitted”); distinguish a statutory command from a lower-court finding about how it operates; keep distinct provisions distinct (an exception in one section is not the exception in another); trace every disposition to its stated legal ground and its remedy; if a material qualification is genuinely unresolved, name the omission and the source needed rather than filling it by inference.

## Holdings writing standard

The render can only project what the record holds, so write the law of the decision at full depth in the record's controlling-holding section and carry it into the Render Input's Holdings block unchanged. For every controlling proposition and every independently sufficient alternative holding:

- **Holding and operative rule.** The complete rule — trigger, what is required or forbidden, the legal consequence, any operative qualification — in one or two sentences a later court could apply without reading anything else.
- **Authority.** The writing, the Justices who join it at that level of generality, and why it controls.
- **Controlling explanation.** 120–200 words in the Court's voice, containing only reasoning the controlling coalition adopted: the precedents relied on and what each supplies; the application to this record; why the principal contrary argument fails; what the Court expressly leaves open. No dicta, no Stone-only reasoning, no later law.
- **Precedent treatment.** One line per earlier decision the holding materially relies on, distinguishes, limits, extends, or overrules: the treatment in ordinary words and its consequence for that precedent's present force.

Use the Contract's labeled block in the full form; in the compact form keep the same four elements in prose at the same depth. A routine unanimous application still gets the explanation; it will simply be shorter than a rule change. Do not pad.

## Voice

Write the render the way the Court writes for the public, not the way a treatise writes for specialists: plain declarative sentences; the rule first in ordinary words, then its precise legal formulation; every cited precedent followed by a clause saying what it supplies here; terms of art only when needed, explained on first use; no Latin where English will do; the Court's voice ("The Court holds ..."), never "the model" or "the simulation." A careful non-lawyer should be able to follow every step; a lawyer should find nothing imprecise.

## Stone's standing fallback (approved)

Approved by the user on September 14, 2026, for October Term 1991 and until revoked: "For any claim, count, or docket component the record presents that Section II does not expressly address, Stone joins the disposition the Court's majority reaches on that component and adds no ground." Apply it only to a component on which Section II is silent — never to narrow, extend, or replace a position Section II states. Record each use in the Decision Record's Stone section and in the Render Input, naming the component. A matter is not stopped for that reason alone.

## Special consideration matters

The user may designate a matter for special consideration. Its Run and Render follow every rule above and these additional ones:

- **Statute in terms.** The neutral packet quotes each challenged provision from the statute’s own text, with every exception and qualification, from the source file the user supplies or the official text. A brief’s paraphrase is not enough.
- **Enhanced record for every Justice on every component.** The Engine’s enhanced issue-specific comparison (§7) is mandatory throughout: for each non-Stone Justice and each separable component, the two-path adversarial test, the strongest counterargument, the join barriers, and the narrower positions, each resting first on that Justice’s own date-eligible writings and simulated positions earlier in the term, with the historical comparator used only to confirm or to record a departure. Cite the writing each row rests on.
- **Explicit join test.** After Stone’s position enters, record for every part of every opinion each Justice’s join or refusal, the recorded objection, and the minimum revision that would resolve it (§8). Assignment follows §8 and is stated.
- **Separate writings at depth.** Each published separate writing is summarized at 300–500 words in the record’s continuity section and in the Render Input: framework, each component, authorities, join barriers.
- **Extended holdings.** The user names the holdings that carry the decision’s doctrine; their controlling explanations run 500–750 words. All other holdings keep the 120–200-word standard. One dedicated holding states the standard lower courts apply after the decision and the controlling status of each component.
- **Reconciliation checks.** Every vote count in the opinion topology reconciles to the per-component judgment table; every Marks claim shows both rationales and why one is a logical subset of the other; no historical authorship or joinder fact is imported.
- **Coalition and vote audit.** The record’s audit annex carries a vote audit: before-and-after vote tables naming the Justices for every controlling proposition and every provision; for each proposed new join, the Justice’s recorded objection, the revised reasoning that answers it, and the exact scope of agreement (complete-framework support, support for particular protections, or judgment-only agreement); an explanation for every changed vote; and the author and joins of every controlling portion. Where the user asks what would follow if a proposal obtained five votes, the annex adds a clearly labeled hypothetical successful-adoption scenario that names the additional judicial choices it assumes and is kept apart from the support the record establishes; nothing from that scenario enters the decision, the Render Input, the render, or current law.
- **Render form: full**, always; the Render carries the separate-writing summaries and the extended holdings at the depth the Render Input supplies.

Designated: *Planned Parenthood of Southeastern Pennsylvania v. Casey*, OT1991 (version 1.4 rerun, September 15, 2026; Stone’s definitive six-step framework with ordered protections, displacing the trimester timetable in the same decision). Extended holdings: the framework retaining protected choice; the standard governing previability regulation after the decision; stare decisis; spousal notice.

## Close protocol

Term close runs only after every manifest item is completed, corrected, or expressly carried forward. It is staged so that no single context must hold the whole term; each pass is its own task, committed before the next. Records control; renders are cross-checks only. Do not change any adjudication during close — a defect goes back to a correction record.

1. **"Close October Term <year>, Holdings pass <k>."** Passes cover chunks in order (1–5, 6–10, 11–14). Each reads the records for its chunks and appends their controlling propositions to `terms/OT<year>/close/HOLDINGS.candidate.md` under the Holdings instructions: area-first organization, natural authority anchors, the entry form, current force, limits, operative remedy. A correction record is placed by its effective date. Nothing noncontrolling enters.
2. **"Close October Term <year>, Standards and Tests pass."** Derive `close/STANDARDS_AND_TESTS.candidate.md` independently from the term-opening register and the records — never from the Holdings candidate — under the Standards and Tests instructions. Reconcile navigation references to the Holdings candidate only after the substance is complete.
3. **"Close October Term <year>, Standing State pass."** Standing State is the Court's setting, not a running record. The next-term Standing State contains only: the header; the Current Court (roster and seniority at the next term's opening, from the Composition); the circuit allotments; the Court's standing practices already recorded (the referral practice); and a docket list of cases brought up — the user's lower-court additions and any matter the Court itself left open at term's end, one line each. No noncontrolling-positions register, no dependency, filing-condition, or history sections, whatever the template's later sections describe. A Justice's simulated prior-term positions are consulted from that term's public renders in `output/`, not from Standing State.
4. **"Audit October Term <year>."** A fresh task. Compare the opening trackers, every record, the final manifest and Continuity Note, the three candidates, and the renders. Verify identical header values across the three candidates, natural anchors, every controlling holding present once and nothing noncontrolling promoted to law, every open matter carried onto the docket list, and the Standing State rule above. Write `close/AUDIT.md` listing every discrepancy. Report only; repair nothing.
5. **"Commit October Term <year> close."** Only when the audit lists no unresolved discrepancy (a discrepancy is resolved by a correction record and a candidate rewrite, never by editing a record). Write `close/TERM_CLOSE_DOSSIER.md` as an index of every file the close relied on, with commit hashes; copy the three candidates over `state/` using the templates' exact header labels (`Last completed October Term`, `Processed through`, `Edition`) with identical values in all three; keep the candidates frozen in `close/`.

## Rules that never bend

1. Stone's approved position controls Stone. The Engine may not fill a missing Stone choice; stop the matter and say exactly what is missing.
2. A completed entry is never silently rewritten. A correction the user authorizes replaces the superseded entry in place — in its record file, in its chunk’s Render Input, and in its chunk’s render — names what it corrects, and carries a lineage line (versions and commit hashes); every earlier version stays in the repository history. Nothing in `close/` is modified once written. (Convention changed September 15, 2026 at the user’s direction; the Holmes, Suter/Montana, Alaska and Harris corrections predate it and remain as separate files.)
3. Do not invent quotations, votes, dockets, dates, findings, concessions, or sources.
4. Only controlling law changes current doctrine. A render never changes substance.
5. No scores, dashboards, ideology labels, win-loss framing, or predictions. No fictional conference dialogue.
6. Use the shell to read files, fetch sources, and check arithmetic, chronology, and cross-references. Tools check consistency; they never decide legal meaning.
7. If anything needed to continue is missing or in conflict, stop the affected matter, name the exact blocker, and finish everything else.
