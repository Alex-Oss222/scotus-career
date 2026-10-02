# OT1995 chunk1 — bounded local link and anchor check

Status: PASS for the inputs present.

Inputs checked: 16. Links catalogued: 209. External URLs/network targets not fetched: 44.
Current Render Input present: True; absence before generation is pending scope, not a missing link.

No Git, network, source edits, recursive directory walk or locked-target content inspection.

## Counts

| Category | Status | Count |
|---|---|---|
| current-term-local | anchor-exists | 28 |
| current-term-local | target-exists | 103 |
| external-url-not-fetched | not-fetched | 44 |
| legacy-baseline-local | anchor-exists | 21 |
| legacy-baseline-local | target-exists | 13 |

## Current-term local issues

No issues in this category.

## Legacy baseline local issues

No issues in this category.

## Other rejected or repository issues

No issues in this category.

## Scope and limits

- External URLs and network paths are catalogued without fetching.
- Fragments of non-Markdown targets are reported as not checked, not missing headings.
- Outside-workspace targets are not inspected.
- Generated-heading slugs are a local consistency approximation; unusual inline HTML or Markdown extensions may require manual anchor review.

Missing required workspace inputs: none.
Parser warnings: 0; see JSON for exact locations.

The JSON keeps target failures, heading failures, legacy baseline links and unfetched external URLs separate. Re-run after final workspace and Render Input generation. This report tests consistency only and supplies no legal conclusion.
