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
   close/           the three replacement trackers and the Term-Close Dossier
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

- **October Term 1991 is complete.** All 14 chunks are run and rendered (`terms/OT1991/output/`). The chronology cursor is July 17, 1992, after *Benten v. Kessler*.
- ***Planned Parenthood of Southeastern Pennsylvania v. Casey*** is the term's special-consideration matter. Stone's position went through four revisions (`terms/OT1991/briefs/OT_1991CHUNK14_CASEY_V1_1.md` through `_V1_4.md`); version 1.4 is current. The Court retains Roe's core 6–3, adopts a five-Justice severe-interference floor (Stone, Blackmun, Stevens, O'Connor, Souter), and displaces the trimester timetable 6–3 (Stone joins on his own resolved condition). Stone's complete six-step framework does not replace that timetable as the Court's controlling standard — it has two votes, Stone and Stevens — and no majority adopts any single general test for previability regulation. Spousal notice is invalid 6–3; the other challenged provisions are sustained at the scopes stated in the record.
- **Term close has not been performed.** It needs the user present; see the five-pass protocol in `AGENTS.md`.
- `terms/OT1992/` already holds a case index, chunk briefs, runtime split files, and Stone's Option C build, written before OT1991 was run. They need to be regenerated against the closed OT1991 registers before `Open October Term 1992.`
- Corrections to Holmes, Suter, Montana, Alaska, and the two Harris applications (chunk 6–8) predate the in-place correction convention and remain as separate files, named in their chunks' Render Inputs.

## Running it

- **Codex cloud** (chatgpt.com/codex): connect this GitHub repository, environment image `universal`, no setup script (add `pip install pypdf` only if PDF reads fail). Internet **Limited**, allowlist `archive.org`, `us.archive.org`, `supremecourt.gov`, `loc.gov`, `govinfo.gov`, `law.cornell.edu`, `oyez.org`. Model GPT‑6 Astra, or GPT‑5.6 Sol at high effort.
- **Codex CLI, local**: `codex.exe exec -C <repo> --approve-for-me -c 'sandbox_workspace_write.network_access=true' "<task sentence>"`. Used for every Run and Render in this term; faster iteration, same rules from `AGENTS.md`.
- **Direct operator edit**: for a correction that changes only Stone's own vote and authorship, the record, Render Input block, and render entry may be edited directly, at the user's express direction, in place of a further Codex run. Every such edit still follows the Engine's rules — no other Justice's position moves without a textual basis in that Justice's own recorded commitments.
