# Stone-Zsela Supreme Court — term simulation

One repository for the whole career of Chief Justice Alex-Lamar Stone-Zsela, October Term 1991 onward. Both the Codex CLI and this assistant read `AGENTS.md` first. You put files where they belong and type one of four sentences.

## Layout

```
foundation/      Engine, Render Contract, Court Composition, case-brief template,
                 tracker instructions. Never changes.
state/           The three living trackers: Holdings, Standards and Tests,
                 Standing State. Replaced only at term close.
terms/OT<year>/  One folder per term:
   case-list.md     your inventory of the term's cases and actions
   briefs/          your case briefs, one file per chunk (OT_<year>CHUNK<n>.md)
   runtime/         optional split files (_NEUTRAL / _STONE / _COMPARATOR)
   workspace.md     written by Run: manifest, ledger index, continuity note
   records/         written by Run: one Decision Record per event; a user-authorized
                     correction replaces the superseded record in place, with a
                     lineage line naming every earlier version
   render-inputs/   written by Run: the Render Input for each chunk; a correction
                     replaces only the affected event's block, in place
   output/          written by Render: the public render of each chunk; a correction
                     replaces only the affected entry, in place, with no version
                     numbers, commit hashes, or correction labels in the public text
   close/           staged close notes, one canonical AUDIT.md, and the Term-Close Dossier; candidates are removed after publication
```

## The four tasks

1. `Open October Term <year>.` — validates `state/`, builds the manifest from `case-list.md`, writes `workspace.md`.
2. `Run October Term <year>, chunk <n>.` — adjudicates the chunk under the Engine; writes `records/`, `render-inputs/`, `workspace.md`.
3. `Render October Term <year>, chunk <n>.` — a separate task; writes the public render to `output/` from the Render Inputs alone.
4. `Close October Term <year>.` — staged in five passes (Holdings, Standards and Tests, Standing State, Audit, Commit); see `AGENTS.md`.

Steps 2 and 3 repeat per chunk, each as its own task, each merged before the next.

The user may designate a matter for **special consideration** (extended holdings, a full coalition and vote audit, statute quoted in terms) — see `AGENTS.md`'s "Special consideration matters." A correction to an already-adjudicated matter is authorized by the user and replaces the superseded entry in place, in the record, the chunk's Render Input, and the chunk's render; it is not a new event. When only Stone's own vote and authorship move — no other Justice's modeled position changes — the operator may prepare the correction directly, without a further Codex CLI run.

Anything else, in plain words, in the same task: "Also: stay the execution in …", "Add this lower-court case to the term: …".

## Where things stand

This section is a pointer to current sources, not a restatement of the law. If it and a linked source ever disagree, the source controls.

- **October Term 1991 is closed.** All 14 chunks are run and rendered (`terms/OT1991/output/`); the [Term-Close Dossier](terms/OT1991/close/TERM_CLOSE_DOSSIER.md) records the coordinated replacement of `state/`'s three trackers.
- ***Planned Parenthood of Southeastern Pennsylvania v. Casey*** was the term's special-consideration matter. Its current, controlling version is stated in the record's ["Version 1.5 assembly" section](terms/OT1991/records/Planned_Parenthood_of_Southeastern_Pennsylvania_v_Casey_merits_1992-06-29.md); earlier versions (v1.1–v1.4) remain in `terms/OT1991/briefs/` as superseded history, not current law.
- **October Term 1992 is closed.** All 11 chunks are run and rendered (`terms/OT1992/output/`), the final audit reports no unresolved discrepancy, and the audited tracker set has been published to `state/`. See `terms/OT1992/close/AUDIT.md` and `terms/OT1992/close/TERM_CLOSE_DOSSIER.md`.
- **The repository is positioned to open October Term 1993.** `state/` contains the OT1993 opening setting. `terms/OT1993/case-list.md` is present, but no OT1993 `workspace.md` exists yet, so the term has not been opened. The final OT1992 audit records the corrected Martin, Moreau, Demos, and Blair dispositions; Coleman is correctly confined to OT1991 by its June 15, 1992 post-close correction record.
- Corrections to Holmes, Suter, Montana, Alaska, and the two Harris applications (OT1991 chunks 6–8) predate the in-place correction convention and remain as separate files, named in their chunks' Render Inputs.

## Running it

- **Codex cloud** (chatgpt.com/codex): connect this GitHub repository, environment image `universal`, no setup script (add `pip install pypdf` only if PDF reads fail). Internet **Limited**, allowlist `archive.org`, `us.archive.org`, `supremecourt.gov`, `loc.gov`, `govinfo.gov`, `law.cornell.edu`, `oyez.org`. Model GPT‑6 Astra, or GPT‑5.6 Sol at high effort.
- **Codex CLI, local**: `codex.exe exec -C <repo> --approve-for-me -c 'sandbox_workspace_write.network_access=true' "<task sentence>"`. Used for every Run and Render in this term; faster iteration, same rules from `AGENTS.md`.
- **Direct operator edit**: for a correction that changes only Stone's own vote and authorship, the record, Render Input block, and render entry may be edited directly, at the user's express direction, in place of a further Codex run. Every such edit still follows the Engine's rules — no other Justice's position moves without a textual basis in that Justice's own recorded commitments.
