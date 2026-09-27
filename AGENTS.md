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

`state/` holds the three trackers the Engine calls Holdings, Standards and Tests, and Standing State. They are the term-opening baseline for the term in progress. Between chunks, current-term law and procedure live in the term's OT1993+ `workspace/` projections, or the legacy `workspace.md` for OT1991–OT1992, not in `state/`. The trackers are replaced only at term close, as one coordinated set. Standing State holds only the Court's setting: roster and seniority, circuit allotments, standing practices, and the docket of cases brought up; it never carries positions, dependencies, or history.

## Term folders

`terms/OT<year>/`

- `case-list.md` — the user's term-wide inventory of cases and Court actions (the Engine's "lightweight term-wide inventory").
- `briefs/` — the user's case briefs, one file per chunk of about ten cases (`OT_<year>CHUNK<n>.md`). Inputs. Never edit them; Stone's words are never altered.
- `runtime/` — when present, the user's split of each chunk into `_NEUTRAL`, `_STONE`, and `_COMPARATOR` files.
- `workspace/` — for OT1993 forward, four replaceable projections: `manifest.md`, `ledger.md`, `continuity.md`, and `neutral.md`. OT1991–OT1992 retain their legacy `workspace.md` files unchanged as historical artifacts.
- `entering-law/` — one generated reading slice per chunk, copied from the authoritative opening trackers and effective current-term Records immediately before modeling. It is derived context, never authority.
- `freeze/` — durable stage handoffs: provisional non-Stone commitments and reconciled commitments. These files are written before Stone enters assembly and may not be edited by the assembly task.
- `validation/` — durable deterministic check results and source-retrieval status used by the Record's validation statement.
- `records/` — one Canonical Decision Record or Admitted Source Record per completed event, named by natural case/docket identity, event type, and date. An authorized correction replaces the file in place; concise lineage belongs in internal provenance, not public Court prose.
- `render-inputs/` — generated from each Record's bounded `Public projection` section. The generated file is the renderer's physically separate handoff and is never independently redrafted.
- `output/` — written by Render: Court-facing public output only. It contains no workflow status, version history, approval history, model language, or operator provenance.
- `close/` — staged close work, one canonical `AUDIT.md`, generated indexes, and the Term-Close Dossier. Candidate tracker files and temporary pass notes are removed after a successful Commit pass; Git history preserves superseded working material.

## The four tasks the user gives

**"Open October Term <year>."** Validate `state/` against the Engine's term-opening baseline, read `case-list.md`, and for OT1993 forward write `workspace/manifest.md`, `workspace/ledger.md`, `workspace/continuity.md`, and `workspace/neutral.md`. Report any conflict or missing inventory item; do not invent one.

**"Prepare October Term <year>, chunk <n>."** Regenerate the `runtime/` split from the approved chunk brief, rebuild the event-date entering-law slice in `entering-law/`, and prepare the Neutral Modeling Packet. This task may read neutral materials and authoritative current law. It does not read the current chunk's Stone section or historical comparator after the mechanical split.

**"Model October Term <year>, chunk <n>."** A physically separate task. Read only the Neutral Modeling Packet, the event-date entering-law slice, and the Engine provisions required for non-Stone modeling. Write `freeze/OT_<year>CHUNK<n>_COMMITMENTS.md`. Do not read Stone, the historical comparator, prior reconciliation, or private audit material.

**"Reconcile October Term <year>, chunk <n>."** A physically separate task. Read the frozen Neutral Modeling Packet, provisional commitments, and historical comparator, but not Stone. Write `freeze/OT_<year>CHUNK<n>_RECONCILED.md`. Every historical departure must identify the concrete changed premise and why it can matter to that Justice. Do not turn this inquiry into a score or automatic historical-vote rule.

**"Run October Term <year>, chunk <n>."** Assembly only. Read the Neutral Modeling Packet, the frozen reconciled commitments, Stone's approved position last, and the date-eligible sources needed for final compatibility. Adjudicate in effective-date order, write each Canonical Decision Record, update the four workspace projections, and put the eleven public blocks once in the Record's bounded `Public projection` section. Generate `render-inputs/OT_<year>CHUNK<n>.md` mechanically from those sections. Run deterministic checks before commitment. Do not rewrite frozen Model or Reconcile files.

**"Render October Term <year>, chunk <n>."** A separate task. Read only `render-inputs/OT_<year>CHUNK<n>.md`, `foundation/RENDER_CONTRACT.md`, and the public-render instructions. Write `output/OT_<year>CHUNK<n>.md`. Do not open briefs, Records, freeze files, audit material, or sources; do not research, revisit votes, change coalitions, or add holdings. A blocker is reported to the operator and never printed inside the Court-facing output.

**Closing a term** is staged, one task per pass; see "Close protocol" below. Nothing in `state/` changes until the Commit pass.

The user may also say, in plain words, that the Court issues an order or takes up a lower-court case. Record it the way the Engine requires — an Admitted Source Record, a manifest change, or a Standing State entry — then continue.

## Mode

For OT1993 forward, Model, Reconcile, and Run are separate contexts with durable handoffs. Model never receives the comparator or Stone. Reconcile receives the comparator but never Stone. Run receives Stone only after the reconciled freeze exists. Single-conversation mode remains a documented emergency fallback, not the normal path. General model knowledge cannot be erased, but withheld current-matter files must be physically absent from each restricted task.

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
- **No workflow metadata in a render.** The public render carries no version numbers, commit hashes, lineage, approval history, correction labels, research-retrieval dates, or references to a model, simulation, user, operator, freeze, or workflow. A corrected entry reads as the Court's decision of its effective date. Provenance stays internal. Source Notes contain only historically ordinary source or quotation information when needed. Blockers never appear in the Court-facing file.

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

Canonical enhanced-case adjudication: *Planned Parenthood of Southeastern Pennsylvania v. Casey*, OT1991. The current Canonical Decision Record controls and is not reopened absent an authorized correction. Its controlling coalition on Stone's six-step framework is Stone, Blackmun, Stevens, O'Connor, and Souter. Extended holdings: the framework retaining protected choice; the standard governing previability regulation after the decision; stare decisis; spousal notice. Public output states the decision normally and never narrates the provenance of the canonical version.

## Close protocol

Term close runs only after every manifest item is completed, corrected, or expressly carried forward. Run `python tools/check_term.py <year>` first and resolve deterministic failures before asking an AI to audit law. The substantive close is staged so that no single context must hold the whole term; each pass is its own task, committed before the next. Records control; renders are cross-checks only. Do not change any adjudication during close — a defect goes back to a correction record.

1. **"Close October Term <year>, Holdings pass <k>."** Passes cover chunks in order (1–5, 6–10, 11–14). Each reads the records for its chunks and appends their controlling propositions to `terms/OT<year>/close/HOLDINGS.candidate.md` under the Holdings instructions: area-first organization, natural authority anchors, the entry form, current force, limits, operative remedy. A correction record is placed by its effective date. Nothing noncontrolling enters.
2. **"Close October Term <year>, Standards and Tests pass."** Derive `close/STANDARDS_AND_TESTS.candidate.md` independently from the term-opening register and the records — never from the Holdings candidate — under the Standards and Tests instructions. Reconcile navigation references to the Holdings candidate only after the substance is complete.
3. **"Close October Term <year>, Standing State pass."** Standing State is the Court's setting, not a running record. The next-term Standing State contains only: the header; the Current Court (roster and seniority at the next term's opening, from the Composition); the circuit allotments; the Court's standing practices already recorded (the referral practice); and a docket list of cases brought up — the user's lower-court additions and any matter the Court itself left open at term's end, one line each. No noncontrolling-positions register, no dependency, filing-condition, or history sections, whatever the template's later sections describe. A Justice's simulated prior-term positions are consulted from that term's public renders in `output/`, not from Standing State.
4. **"Audit October Term <year>."** A fresh task after deterministic checks pass. Compare the opening trackers, every Record, the final manifest and Continuity Note, the three candidates, and the renders. Spend the audit on votes, coalitions, holdings, remedies, historical-departure causation, and carry-forward. Provenance review is limited to whether concise internal claims point to real repository history; do not turn wording lineage into a substitute merits audit. Write or replace `close/AUDIT.md`; do not create `AUDIT.reaudit*.md` files.
5. **"Commit October Term <year> close."** Only when the audit lists no unresolved discrepancy. Generate `close/INDEX.md` (date, case, disposition, vote, author), `close/SEPARATE_WRITINGS.md` (author, case, date, joiners, one-line proposition), `close/DEPARTURES.md` (one line for each judgment, coalition, or controlling-rule departure from history with its Justice-specific causal basis), and `close/CONSEQUENCES.md` (advisory list of later historical predicates potentially displaced; never authority by itself). Generate `close/TERM_CLOSE_DOSSIER.md` from the relied-on files and repository hashes; copy the audited candidates over `state/` with synchronized headers; verify byte identity; then delete candidate files and temporary pass notes.

## Rules that never bend

1. Stone's approved position controls Stone. The Engine may not fill a missing Stone choice; stop the matter and say exactly what is missing.
2. A completed adjudicative entry is never silently rewritten. An authorized correction replaces the superseded Record in place and states concise internal supersession. Regenerate the affected Render Input from the Record's Public projection, then re-render only the affected public entry. Public text carries no version, commit, approval, or correction history. Earlier versions remain in Git history. After Commit, candidates and temporary pass notes are deleted; one final `AUDIT.md`, the generated close indexes, and the Term-Close Dossier remain.
3. Do not invent quotations, votes, dockets, dates, findings, concessions, or sources.
4. Only controlling law changes current doctrine. A render never changes substance.
5. No scores, dashboards, ideology labels, win-loss framing, or predictions. No fictional conference dialogue.
6. Use the shell to read files, fetch sources, and check arithmetic, chronology, and cross-references. Tools check consistency; they never decide legal meaning.
7. If anything needed to continue is missing or in conflict, stop the affected matter, name the exact blocker, and finish everything else.
