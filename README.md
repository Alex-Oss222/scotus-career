# Stone-Zsela Supreme Court — term simulation

One repository for the whole career of Chief Justice Alex-Lamar Stone-Zsela, October Term 1991 onward. Both the Codex CLI and this assistant read `AGENTS.md` first. The user-facing workflow remains four commands; from OT1993 forward, Run internally uses physically separated modeling, reconciliation, and assembly contexts.

## Layout

```
foundation/      Engine, Render Contract, Court Composition, case-brief template,
                 tracker instructions. Changes only by explicit architecture revision outside an active term.
state/           The three living trackers: Holdings, Standards and Tests,
                 Standing State. `state/holdings/` contains the canonical doctrinal
                 Holdings reading volumes; `state/HOLDINGS.md` is the generated
                 continuous compatibility view. Replaced only at term close.
terms/OT<year>/  One folder per term:
   case-list.md     your inventory of the term's cases and actions
   briefs/          your case briefs, one file per chunk (OT_<year>CHUNK<n>.md)
   runtime/         derived current-chunk handoffs (_NEUTRAL / _COMMITMENTS /
                     _COMPARATOR / _RECONCILED / _STONE)
   entering-law/    derived case-specific reading slices from authoritative state
   freeze/           committed non-Stone commitment/reconciliation handoffs and validation summaries
   workspace/        OT1993+: manifest, ledger, continuity, neutral projection as separate files
   records/          written by Run: one canonical Record per event, with concise lineage
                     and a bounded Public Projection section
   render-inputs/    generated from Record Public Projection sections; never independently authored
   output/          written by Render: the public render of each chunk; a correction
                     replaces only the affected entry, in place, with no version
                     numbers, commit hashes, or correction labels in the public text
   close/           staged close notes, one canonical AUDIT.md, and the Term-Close Dossier; candidates are removed after publication
```

## The four tasks

1. `Open October Term <year>.` — validates `state/`, builds the manifest from `case-list.md`, and from OT1993 forward writes the four files under `workspace/`.
2. `Run October Term <year>, chunk <n>.` — regenerates the runtime split and entering-law slice, freezes non-Stone commitments in an isolated modeling context, reconciles them against history in a second Stone-blind context, introduces Stone only in assembly, writes Records/workspace projections, then generates `render-inputs/` from the Records.
3. `Render October Term <year>, chunk <n>.` — a separate task; writes the public render to `output/` from the Render Inputs alone.
4. `Close October Term <year>.` — staged in five passes (Holdings, Standards and Tests, Standing State, Audit, Commit); Commit regenerates Holdings volumes and the term indexes. See `AGENTS.md`.

Steps 2 and 3 repeat per chunk, each as its own task, each merged before the next.

The user may designate a matter for **special consideration** (extended holdings, a full coalition and vote audit, statute quoted in terms) — see `AGENTS.md`'s "Special consideration matters." A correction to an already-adjudicated matter is authorized by the user and replaces the superseded entry in place, in the record, the chunk's Render Input, and the chunk's render; it is not a new event. When only Stone's own vote and authorship move — no other Justice's modeled position changes — the operator may prepare the correction directly, without a further Codex CLI run.

Anything else, in plain words, in the same task: "Also: stay the execution in …", "Add this lower-court case to the term: …".

## Where things stand

This section is a pointer to current sources, not a restatement of the law. If it and a linked source ever disagree, the source controls.

- **October Term 1991 is closed.** All 14 chunks are run and rendered (`terms/OT1991/output/`); the [Term-Close Dossier](terms/OT1991/close/TERM_CLOSE_DOSSIER.md) records the coordinated replacement of `state/`'s three trackers.
- ***Planned Parenthood of Southeastern Pennsylvania v. Casey*** was the term's special-consideration matter. Its controlling law is stated in the canonical Record and public render. Internal approval and correction provenance remains internal and is not part of the Court-facing account.
- **October Term 1992 is closed.** All 11 chunks are run and rendered (`terms/OT1992/output/`), the final audit reports no unresolved discrepancy, and the audited tracker set has been published to `state/`. See `terms/OT1992/close/AUDIT.md` and `terms/OT1992/close/TERM_CLOSE_DOSSIER.md`.
- **The repository is positioned to open October Term 1993.** `state/` contains the OT1993 opening setting. `terms/OT1993/case-list.md` is present, and the empty OT1993 infrastructure directories are prepared. The term has not been opened because `terms/OT1993/workspace/manifest.md` does not yet exist. Demos is terminal in OT1992, and Martin No. 92-5618 is closed for continuity and is not carried into OT1993. Coleman remains confined to OT1991.
- Corrections to Holmes, Suter, Montana, Alaska, and the two Harris applications (OT1991 chunks 6–8) predate the in-place correction convention and remain as separate files, named in their chunks' Render Inputs.

## Running it

- **Codex cloud** (chatgpt.com/codex): connect this GitHub repository, environment image `universal`, no setup script (add `pip install pypdf` only if PDF reads fail). Internet **Limited**, allowlist `archive.org`, `us.archive.org`, `supremecourt.gov`, `loc.gov`, `govinfo.gov`, `law.cornell.edu`, `oyez.org`. Model GPT‑6 Astra, or GPT‑5.6 Sol at high effort.
- **Codex CLI, local**: `codex.exe exec -C <repo> --approve-for-me -c 'sandbox_workspace_write.network_access=true' "<task sentence>"`. Used for every Run and Render in this term; faster iteration, same rules from `AGENTS.md`.
- **Direct operator edit**: for a correction that changes only Stone's own vote and authorship, the record, Render Input block, and render entry may be edited directly, at the user's express direction, in place of a further Codex run. Every such edit still follows the Engine's rules — no other Justice's position moves without a textual basis in that Justice's own recorded commitments.


## OT1993 architecture boundary

From OT1993 forward, scripts may check and generate bookkeeping, but they do not decide legal meaning. Deterministic tools may verify chronology, arithmetic, identity, file freshness, links, projection fidelity, and manifest completeness. They may not predict a Justice, decide whether precedent controls, choose a holding, form a coalition, apply a fractured-decision rule, or determine whether a historical departure is substantively justified.

## Deterministic support tools

- `tools/open_term.py` seeds the four-file OT1993-forward workspace from the term inventory.
- `tools/split_chunk.py` regenerates the neutral, Stone, and comparator runtime split and refuses multiple live section revisions.
- `tools/build_entering_law.py` copies operator-selected Holdings volumes and tracker sections into a derived reading slice.
- `tools/rebuild_ledger.py` regenerates the Term Working Ledger index from canonical Records and Git commitment history.
- `tools/rebuild_manifest.py` regenerates inventory status from the case list and canonical Records, with explicit stopped/carry-forward inputs.
- `tools/build_render_input.py` copies validated Record Public Projection sections into the renderer handoff.
- `tools/check_term.py` performs deterministic integrity checks only.
- `tools/holdings_volumes.py` keeps doctrinal Holdings volumes and the continuous compatibility view synchronized.
- `tools/build_close_indexes.py` generates the term index, separate-writings index, departures page, and consequences page from explicit Record text.

These tools never decide a vote, holding, precedent meaning, coalition, remedy, or whether a historical departure is legally justified.
