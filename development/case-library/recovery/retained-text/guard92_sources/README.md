# Case-library development area

**Development only. Production integration is disabled.**

This area preserves the source-library and citation-index work while the Court continues its existing OT1995 and OT1996 workflow. The user authorized this separate area on October 3, 2026. It is an organizational boundary within the same Git repository, not a private branch, separate repository, or filesystem access control.

```text
Existing Court workflow                       Separate development work
Open -> Run -> Render -> Close                 schema -> pilot -> catch up -> review
            |                                                    |
            +-- completed repository artifacts --read only------+

                 No development output feeds back into the Court.
```

## What is here

| File | Purpose |
|---|---|
| [AGENTS.md](AGENTS.md) | The development boundary and instructions for future agents. |
| [DESIGN.md](DESIGN.md) | Data design, safeguards, and proposed future update lifecycle. |
| [SAFEGUARDS.md](SAFEGUARDS.md) | Tested failure behavior, safe refresh, and recovery instructions. |
| [schemas/case.schema.json](schemas/case.schema.json) | Draft machine-readable case-entry structure. |
| [schemas/selection.schema.json](schemas/selection.schema.json) and [schemas/historical-sources.schema.json](schemas/historical-sources.schema.json) | Strict structures for reviewed pilot inputs. |
| [examples/example.case.json](examples/example.case.json) | A synthetic example, not a real case or indexed source. |
| [STATUS.md](STATUS.md) | Human-readable progress, next work, and activation conditions. |
| [progress.json](progress.json) | Observed repository baseline and explicitly uncompleted coverage. |
| [catalogues/OT1992/README.md](catalogues/OT1992/README.md) | Full-term catalogue: 123 matter entries, 123 Court events, all 11 chunks. |
| [catalogues/OT1991/README.md](catalogues/OT1991/README.md) | Full-term catalogue: 124 matter entries, 125 Court events, all 14 chunks. |
| [pilot/OT1991-chunks-1-3/README.md](pilot/OT1991-chunks-1-3/README.md) | Retained 24-matter pilot and earlier snapshots. |
| [tools/pilot.py](tools/pilot.py) | Offline pilot build, validation, lookup, and case-card commands. |
| [tests/](tests/) | Isolated behavior, input, rendering, and failure/recovery tests. |

The working offline catalogue now covers all of OT1991: 124 case/matter entries, 125 Court events across 14 chunks, and 375 recorded historical-source pointers. All 126 term Record files are accounted for, including the separate institutional exception. The original 24-matter pilot is retained independently. OT1992 is also complete against its repository inventory: 123 entries/events, 401 historical-source records, and three separately accounted non-case sources. OT1993 onward remain unindexed. Production integration and stage-specific retrieval remain disabled.

## Run a full-term catalogue

From the repository root, in the Linux cloud environment with Python 3.12 and the installed `jsonschema` package:

```bash
python3 -B development/case-library/tools/pilot.py --catalogue OT1992 build
python3 -B development/case-library/tools/pilot.py --catalogue OT1992 validate
python3 -B development/case-library/tools/pilot.py --catalogue OT1992 lookup 'Smith v. United States'
python3 -B development/case-library/tools/pilot.py --catalogue OT1992 lookup '91-1538'
python3 -B development/case-library/tools/pilot.py --catalogue OT1992 show scotus-91-1538
python3 -B -m unittest discover -s development/case-library/tests -v
```

The build command prints the Markdown catalogue location; `index.html` beside it provides local search and chunk filtering. No server or network request is needed. Historical links open their original sites only when followed; this pilot has not verified those remote documents. Local links require the repository directory layout.

`validate`, `lookup`, and `show` reject stale inputs or altered generated files. A build checks the selected mappings against their exact supporting text, canonical identity lines and docket sets, the term inventory, and explicit ledger effective dates. Identical inputs reuse the existing snapshot. A changed Record requires review and a new build. Builds stage and validate output before switching the pointer, serialize writers, and restore the previous pointer if publication fails while the pointer is still owned by that build. No process writes outside this development area.

Direct HTML and Markdown views are saved snapshots and cannot perform those freshness checks. Validate before use, then open the build named in `CURRENT.json`. For a damaged pointer or generated file, `python3 -B development/case-library/tools/pilot.py --catalogue OT1992 recover` rebuilds from valid mappings while preserving prior pointer bytes and snapshots. See [the recovery guide](SAFEGUARDS.md) for tested behavior and limits.

Select `--catalogue OT1991` or `--catalogue OT1992` for the respective full term. Omit `--catalogue` to address the retained three-chunk pilot. Edit the selected term's `selection.json` and `historical-sources.json` under `catalogues/`, not generated snapshot entries. Snapshots project those operator-owned inputs into the schema's `curated` fields without modifying the input files. The full-term adapter accepts explicit mappings for each supported term's legacy formats. OT1992 uses [version 4](schemas/term-selection-v4.schema.json), which binds repeated Render Input headings to an occurrence and an exact case-identity quote. Its date-first effective ledger is handled explicitly. OT1991 retains its [version-3 selection schema](schemas/term-selection-v3.schema.json), with event-level identity, docket, inventory and presentation mappings, owned-docket evidence and explicit supplemental date roles. Version 2 remains readable for retained snapshots; the original pilot keeps version 1. This is not automatic research or an importer for every term.

## Continue work without changing adjudication

Use a separate development task or a fresh context scoped to this directory. For example: “Continue the case-library pilot using completed OT1995 material; keep integration disabled.” After another chunk finishes, a separate maintenance task can update the development baseline and catch up to those completed artifacts. There is no background process or automatic refresh at this stage, and ordinary Court commands do not acquire extra maintenance duties.

Development tasks may read the repository artifacts needed for the stated development scope. Write all experimental tools, generated entries, reports, and test fixtures here. Do not move or duplicate the PDF collection, rewrite Records, modify governing trackers, or put new dependencies into existing term tools. Keep source retrieval and legal review gaps visible.

Suggested development sequence:

1. Review and refine the draft schema using a completed modern chunk, a lower-court addition, a consolidated matter, and a case with several events.
2. Build a read-only importer and readable case cards inside this directory. Separate manually confirmed source mappings from reproducible generated information.
3. Add validation, stale-source detection, safe regeneration, and meaningful failure/recovery checks. Keep all generated output inside this directory.
4. Backfill completed OT1991–OT1994 records, handling their actual formats, then catch up to completed OT1995 work. Include OT1996 as its completed events become available.
5. Reconcile the development entries against the current authoritative repository revision and review unresolved mappings. Review historical-source availability separately from simulation-record coverage.
6. Present the readiness evidence and an integration proposal. Keep integration disabled until the user explicitly authorizes it.

## What “caught up” means

Catch-up is measured against a named repository revision and the completed events available at that revision, not a promise that an entire future term is done. Every in-scope completed Record must be accounted for as indexed and checked or as an explicit unresolved exception. Corrections must refresh the same event rather than create a second adjudication. Do not equate file counts with unique cases.

Before proposing activation, reconcile that coverage to the existing manifests and authoritative records; confirm local pointers, identifiers, correction handling, chronology qualifications, and stage-specific retrieval behavior. Missing historical documents may remain documented research gaps. Unresolved ambiguity about case/event identity, simulation pointers, or exposure of restricted material must be resolved before the affected entries can be used. A schema-valid JSON file alone is not readiness evidence.

## Two different kinds of update

**During this development period:** update this area's data and progress only in a separate scoped task. Normal Run, Render, and Close stay independent.

**If integration is later approved:** the proposed lifecycle is an incremental refresh after a validated chunk or authorized correction, optional presentation-link refresh after Render, and full reconciliation after term close publishes its trackers. That lifecycle is a design proposal, not an enabled hook.

The schema version changes only when the file structure changes. Ordinary additions, source-link fixes, and catch-up refreshes do not themselves require a schema revision. Structural changes need a documented migration and validation before existing entries are replaced.
