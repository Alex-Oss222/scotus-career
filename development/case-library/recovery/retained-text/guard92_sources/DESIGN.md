# Case-library draft design

This is a development specification, not a production schema or an input to any Court task. The catalogue points to historical sources and simulated Records. It neither supplies governing law nor changes Open, Run, Render, or Close. `production_integration` remains `false` even after catch-up; activation requires a later readiness review and explicit user authorization.

## Case entries

The draft uses one JSON file per case identity. A case can have aliases, several court-scoped dockets, multiple historical documents, and multiple simulated events. Consolidated matters require an explicit reviewed identity mapping; matching names or docket numbers alone does not establish identity. Admitted statutory sources will need a separate source model and must not be counted as cases.

`schemas/case.schema.json` uses JSON Schema 2020-12. It is deliberately small enough to revise during development. `examples/example.case.json` is entirely synthetic, uses null locations rather than invented evidence, and must never enter case counts or catch-up claims.

| Part | Purpose | Ownership |
|---|---|---|
| `curated` | Case identity, historical-document pointers, simulated-event pointers, and explicit later-treatment links | Operator-maintained; unreviewed entries remain marked unreviewed |
| `generated` | Observed file metadata and the revision/time of a scan | Replaceable tool output; never overwrites curated fields |
| `uncertainties` | Missing information or unresolved mappings | Operator-maintained; no silent defaults |
| `extensions` (optional) | Named experimental metadata without changing core fields | Preserved on regeneration; no core behavior or legal effect is inferred |

A pointer can identify an external URL, an existing repository file, and a section locator. `null` means unknown or not yet supplied; it does not mean a document does not exist. An empty later-treatment list means no links have been recorded, not that no later treatment exists. Review status concerns metadata accuracy only. A URL is not evidence that its content was checked. File hashes detect changes; they do not establish authenticity or legal force.

## Chronology, authority, and reading boundaries

An event date and a legal effective date are separate fields; neither is inferred from the other. Same-day baseline rules and expressly coordinated events must be resolved under the Engine, not file order or date sorting. Historical docket identifiers do not establish simulated grants or outcomes.

Later-treatment entries point to the Record and section containing an express relationship. The draft has no automated fields for controlling force, overruling, holdings, or vote predictions. A reviewed pointer still requires reading the authoritative statement in context.

References distinguish historical material, simulated public material, internal material, mixed material, and unknown material. A full Record may be mixed. These classifications do not certify stage safety. A future authorized retrieval layer must expose only stage-permitted documents or bounded sections; an unrestricted catalogue must never be passed to a neutral, reconciliation, assembly, or Render context as a substitute for its prescribed inputs.

## Separate development and eventual refresh

During development, scans, pilots, and catch-up occur only in separate scoped tasks inside this directory. There are no hooks, imports, scheduled jobs, or changes to existing commands. Index failures cannot affect adjudication completion. Catch-up milestones must identify the repository revision and scope examined and distinguish discovered files from indexed and reviewed cases.

If integration is later authorized, the proposed timing is an incremental refresh after the existing chunk validation succeeds and a full reconciliation after term-close publication. Corrections in place require refreshing their pointers and observed hashes while preserving stable event identity. Git retains earlier Record versions; the catalogue must not invent new legal events for clerical corrections. Term close is a useful checkpoint, but waiting until close would omit current-term research links.

## Recovery and evolution requirements

Writers stage generated output, validate it, and publish through an atomic pointer replacement. Generated observations must be reproducible; curated mappings must survive regeneration and be retained in version control. No process may edit a Record or source to make index validation pass. The pilot implements these safeguards as described below; the current development work has not yet been committed.

`schema_version` changes only when the entry structure changes. A data refresh instead updates scan provenance and observed hashes. Structural changes need an explicit migration and validation, never an in-place guess. Ordinary development revisions do not grant production integration.

Schema validation checks structure and formatted dates, not file existence, URL availability, duplicate identities, source completeness, chronology, stage authorization, or legal meaning. Those require separate checks and, where appropriate, operator review. The OT1991 chunks 1–3 pilot now implements clerical import and search; stage-specific retrieval and production integration remain unimplemented.

Core objects reject unrecognized fields so misspellings are detected. Optional `extensions` hold named objects for experiments; they cannot replace core fields, change integration flags, or bypass a later schema migration. Pilot paths resolve inside the checkout and reject escapes, symlinks, and noncanonical spellings. Identifiers are checked before output. Reviewed manifests have their own strict schemas; adding fields requires explicit importer support rather than silently discarding unknown data.

## Implemented pilot boundaries

The pilot has two operator-owned mapping files: `selection.json` binds the 24 selected events to their canonical identities and exact evidence, while `historical-sources.json` attributes each historical pointer to recorded local evidence. The importer projects those inputs into case entries; it does not invent case matching, URLs, historical dates, or legal treatment. Each historical document has its own citation. In particular, lower-court opinions do not inherit a Supreme Court citation, and Archive packet landing pages have no invented document citation.

Every consumed source and tool/schema input is fingerprinted. Case names, scoped docket sets, evidence quotations, inventory coverage, and explicit ledger effective dates are checked before output. The current pilot rejects unsupported legacy identity shapes instead of guessing. This is a bounded adapter for the selected records, not a universal historical-record parser.

Generated JSON, Markdown cards, HTML, and coverage reports live in retained `builds/<snapshot-id>/` directories that the tool never edits after publication. Normal IDs derive from input fingerprints; recovery can allocate a fresh ID to preserve a damaged directory. `CURRENT.json` identifies the active snapshot and fingerprints its artifact manifest. A new build is staged and fully validated before the pointer changes. Writer locking, source rechecks, and rollback protect publication; a complete snapshot left by an interrupted update can be reused after validation. Explicit recovery backs up damaged pointer bytes and retains existing snapshots without rewriting reviewed inputs.

Identical inputs reuse the validated active snapshot. Command-line reads check source freshness, output fingerprints, expected file layout, and coverage counts, so generated files must not be edited by hand. Direct HTML/Markdown views cannot check freshness and disclose that limit. These checks detect accidental changes and are not a cryptographic signature or a claim of source authenticity. See [SAFEGUARDS.md](SAFEGUARDS.md) for recovery commands, failure tests, and filesystem limits.

Case entries currently contain no later-treatment links because that review was outside the pilot scope. Full Records are classified as mixed material, and presentation files are navigation links only. No case card or catalogue is approved as input to any substantive Court stage.

## Full-term OT1991 expansion

`catalogues/OT1991/` has a separate version-3 selection manifest (with version 2 retained for older snapshots) and snapshot lifecycle. The case-entry schema remains version 1; new event metadata is explicit under the named pilot extension. The original three-chunk input manifests and saved snapshots remain available, with no in-place migration.

Each event supplies its own identity evidence, owned docket numbers, exact inventory match or documented supplemental status, and actual publication locations. Case-level dockets and presentation links are checked against their event-level union. The post-close Coleman petition is separately dated under the same case; the two distinct Harris applications retain separate matter identities. Whole-term reconciliation accounts for every Record and detects new directory members as well as changed file contents.

Full-term coverage means 124 inventory events plus the documented supplemental event, with the institutional source kept outside case counts. It does not establish historical packet completeness, later treatment, current legal force or readiness for a restricted adjudication stage. No update hook or production dependency is introduced.

## OT1992 profile and term isolation

`catalogues/OT1992/` uses a version-4 selection schema with the same core entry schema, an explicit eleven-chunk scope and its own snapshots, writer lock and recovery history. The shared importer checks the selected term at each manifest, inventory, Record, presentation and saved-report boundary. It reads OT1992's date-first working ledger explicitly rather than treating publication dates as event dates.

Repeated `## Event` Render Input headings use a paired `heading_occurrence` and `identity_quote`. The importer validates the selected bounded section, its exact unique quote, case caption, docket identity and event date. The renderer preserves the occurrence and links its numbered Markdown anchor. Ordinary unique-heading pointers remain unchanged; prior selection schemas and snapshots stay available.

All 123 inventory events and three non-case sources are accounted for. Corrections and the Martin continuity reconciliation do not create new events; Coleman remains in OT1991. Historical locations are locally attributed, and four recorded documents have explicit location gaps. This expansion adds neither automatic research nor production integration.
