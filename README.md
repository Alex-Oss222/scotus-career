# Stone-Zsela Supreme Court — term simulation

One repository for the whole career of Chief Justice Alex-Lamar Stone-Zsela, October Term 1992 onward. Codex reads `AGENTS.md` first. You put files where they belong and type one of three sentences.

## Layout

```
foundation/      Engine, Render Contract, Court Composition, case-brief template,
                 tracker instructions. Never changes.
state/           The three living trackers: Holdings, Standards and Tests,
                 Standing State. Replaced only at term close.
terms/OT<year>/  One folder per term, OT1992–OT2015:
   case-list.md     your inventory of the term's cases and actions
   briefs/          your case briefs, one file per chunk (OT_<year>CHUNK<n>.md)
   runtime/         optional split files (_NEUTRAL / _STONE / _COMPARATOR)
   workspace.md     written by Codex: manifest, ledger index, continuity note
   records/         written by Codex: one Decision Record per event
   output/          written by Codex: the render of each chunk
   close/           written by Codex at term close
archive/         The earlier career line (Stone from October 1993, OT1993–OT2002):
                 briefs, chat exports, per-term trackers, simulated opinions, and
                 the OT2002 opening trackers. Reference only — nothing in it is
                 current law for the OT1992 line.
docs/            The project handoff and the doctrine taxonomy.
```

## The three sentences

1. `Open October Term 1992.` — validates `state/`, builds the manifest from `case-list.md`, writes `workspace.md`.
2. `Run October Term 1992, chunk 1.` — adjudicates the chunk; writes `records/`, `output/`, `workspace.md`. Repeat per chunk.
3. `Close October Term 1992.` — rebuilds the three trackers as one set into `state/` and `close/`.

Anything else, in plain words, in the same task: "Also: stay the execution in …", "Add this lower-court case to the term: …".

Each task comes back as a diff. Read the render in `output/`, check that nothing already in `records/` or `output/` shows as changed, merge.

## Where the OT1992 line stands

- `state/STANDING_STATE.md` is the OT1992 opening state (edition September 6, 2026).
- `state/HOLDINGS.md` and `state/STANDARDS_AND_TESTS.md` start empty. Pre-divergence law enters each case through the Engine's source rules and the brief's Law Entering the Case section, not through the registers.
- `terms/OT1992/` already holds the case index (`case-list.md`), nine chunk briefs, the runtime split files, and Stone's Option C build.
- Next step: `Open October Term 1992.`

## Codex cloud environment

- Repository: this one. Image: `universal`. Setup script: none to start; if Codex reports it cannot read a PDF, add `pip install pypdf`.
- Internet: **Limited**, allowlist `archive.org`, `us.archive.org`, `supremecourt.gov`, `loc.gov`, `govinfo.gov`, `law.cornell.edu`, `oyez.org`. If a download fails, add the host Codex names.
- Model: GPT‑6 Astra, or GPT‑5.6 Sol at high effort, for Open / Run / Close.
