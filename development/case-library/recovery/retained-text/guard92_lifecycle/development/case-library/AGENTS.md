# Case-library development boundary

This directory is an isolated development area authorized on October 3, 2026. It is not part of the active Court workflow and contains no governing law. The source catalogue and citation index are being designed and built here while the user continues OT1995 and OT1996.

- Work here only in a separate development/maintenance task or fresh, explicitly scoped development context. Do not load this directory in Open, Run, Render, or Close contexts, or use its contents as entering law, research inputs, or authority.
- Write only inside `development/case-library/` for library development. Read existing repository files only as the development task requires. Do not change or move `foundation/`, `state/`, term records, briefs, freezes, sources, renders, or existing production tools. A separately authorized boundary notice in the root documentation is the sole current exception.
- No hooks, scheduled refreshes, automatic imports into court tasks, production tool dependencies, or changes to normal adjudication commands. Catch-up and implementation work happens separately. Index failures never change an adjudication or its completion status.
- Keep `production_integration` false. Catching up does not authorize activation. Integration needs a completed readiness review and explicit user authorization in a later task.
- Preserve original source files. Prefer pointers to existing repository files and source URLs. Do not download a new corpus, relocate PDFs, or rewrite authoritative documents as part of scaffolding.
- Keep historical sources, simulated public material, and internal audit material distinguishable. This development area is not stage-safe input. A future stage-specific retrieval layer must supply only authorized documents or bounded sections, not expose a full Record to a restricted stage.
- Dates do not determine authority by themselves. Preserve event identity, source chronology, same-day baseline rules, and correction lineage. Do not infer controlling force, holdings, votes, overrides, or legal treatment from filenames, dates, citations, or keyword matches.
- Keep human-verified mappings separate from generated data. Preserve uncertain and missing metadata explicitly. A URL being present is not source verification, and a valid schema is not legal validation.
- Use the existing checkout; do not create another Git worktree. Use the installed Python tools and avoid adding runtime dependencies without a concrete need.
- Update `STATUS.md` and the development progress metadata truthfully when development work advances. Observed source counts are not indexed or reviewed counts. Record the repository revision and scope behind any claimed catch-up milestone.

Read `README.md`, `DESIGN.md`, and `STATUS.md` in this directory before continuing library development. Draft examples are synthetic and must never be counted as indexed cases.
