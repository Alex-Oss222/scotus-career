# Stone-Zsela Supreme Court

One repository for the alternate Supreme Court career of Chief Justice Alex-Lamar Stone-Zsela, October Term 1991 onward. `AGENTS.md` and the files in `foundation/` define the operating rules. Court-facing output is written as ordinary in-world legal history.

## Repository layout

```
foundation/      Engine, Render Contract, Court Composition, templates
state/           living Holdings, Standards and Tests, and Standing State
stone/           Stone research and planning aids; never entering law by themselves
tools/           deterministic consistency and projection tools
terms/OT<year>/  one directory per October Term
   case-list.md
   briefs/
   runtime/         generated NEUTRAL / STONE / COMPARATOR splits
   entering-law/    event-date current-law reading slices
   freeze/          immutable Model and Reconcile handoffs
   validation/      deterministic validation artifacts
   workspace/       OT1993+: manifest, ledger, continuity, neutral projection
   records/         canonical Decision Records and Admitted Source Records
   render-inputs/   generated public handoff from Records
   output/          Court-facing decisions and dispositions
   close/           staged term-close audit and publication work
```

OT1991 and OT1992 retain their legacy single-file `workspace.md` artifacts. OT1993 forward uses the split `workspace/` structure.

## Operating sequence

1. `Open October Term <year>.` validates the opening trackers and creates the term workspace projections.
2. `Prepare October Term <year>, chunk <n>.` regenerates the runtime split, builds the entering-law slice, and prepares neutral materials.
3. `Model October Term <year>, chunk <n>.` models the non-Stone Justices from neutral materials only and freezes provisional commitments.
4. `Reconcile October Term <year>, chunk <n>.` introduces the historical comparator, still without Stone, and freezes reconciled commitments.
5. `Run October Term <year>, chunk <n>.` is assembly only. Stone enters last; Records are written; workspace projections update; Render Inputs are generated from each Record's bounded Public projection.
6. `Render October Term <year>, chunk <n>.` reads only the generated Render Input and writes Court-facing output.
7. `Close October Term <year>.` runs deterministic checks first, then the staged substantive audit and coordinated tracker replacement.

Prepare, Model, Reconcile, Run, and Render are separate contexts. The freeze files are durable handoffs and are not rewritten during assembly.

## Mechanical versus adjudicative work

Scripts may check chronology, file correspondence, vote arithmetic, stale generated files, public-voice leakage, and other deterministic consistency matters. They may copy already-approved text between bounded interfaces.

Scripts may not predict a Justice's vote, form a coalition, decide what precedent means, determine whether a historical departure is justified, apply a fractured-decision rule, choose a remedy, or generate a holding. Those remain legal-modeling tasks under `foundation/ENGINE.md`.

## Public-output rule

Files in `output/` state the Court's action as ordinary Court history. They do not narrate model behavior, approvals, versions, commits, research-retrieval dates, correction provenance, or workflow blockers. Internal Records and Git history preserve provenance.

## Current status

- October Term 1991 is closed.
- October Term 1992 is closed and the audited tracker set has been published to `state/`.
- *Planned Parenthood of Southeastern Pennsylvania v. Casey* is governed by its current Canonical Decision Record. Superseded drafts are historical repository material and supply no current law.
- The stale paid/form-compliance conditions in *Zatko* and *Martin v. McDermott* were administratively closed effective October 1, 1993, before OT1993 opening. *Demos v. Storrie* was already terminal.
- October Term 1993 has a case list and empty staged-workflow directories, but the term has not yet been opened.
