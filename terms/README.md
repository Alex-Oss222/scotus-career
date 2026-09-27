# Terms

One folder per October Term. Before a term, supply:

- `case-list.md` — the term-wide inventory of cases and Court actions.
- `briefs/OT_<year>CHUNK<n>.md` — approved three-section case briefs under `foundation/CASE_BRIEF_TEMPLATE.md`.

From OT1993 forward the operator and deterministic tools maintain the rest:

- `runtime/` — derived `_NEUTRAL`, `_STONE`, and `_COMPARATOR` splits plus frozen modeling/reconciliation handoffs as directed by `AGENTS.md`.
- `entering-law/` — derived reading slices from selected authoritative tracker sections.
- `freeze/` — committed non-Stone commitment, reconciliation, and validation handoffs.
- `workspace/` — `manifest.md`, `ledger.md`, `continuity.md`, and `neutral-projection.md`.
- `records/` — canonical Decision Records and Admitted Source Records.
- `render-inputs/` — generated from Record Public Projection sections.
- `output/` — Court-facing renders.
- `close/` — current audit, dossier, generated close indexes, and temporary candidates during term close.

The empty infrastructure directories may exist before a term opens. From OT1993 forward, a term is considered opened when `workspace/manifest.md` and the other three validated workspace files exist.

Do not hand-edit derived runtime splits, Render Inputs, ledger indexes, or generated close indexes. Regenerate them with the tools documented in the repository README.
