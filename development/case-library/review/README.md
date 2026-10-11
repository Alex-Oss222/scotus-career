# Rebuild verification evidence

`rebuild-validation.json` summarizes the final rebuild; `tests.log` records the 99 new tests, including seven Chromium tests. `browser-report.json` and screenshots cover the published 575-Record browser, not only synthetic fixtures. `stress-report.json` and `stress.log` record twelve additional targeted contention, killed-process and publication-race runs against disposable fixture repositories. `live-check.log` and `repeat-build.log` show current-source validation and deterministic snapshot reuse.

All tests and browser checks are new. Archived recovery files are not imported as passing tests. Local file-link and same-page-anchor checks do not certify cross-file Markdown section locators or historical authenticity. External URLs were syntax-checked only and not retrieved.

To repeat the full-data browser audit in the current cloud environment, start `python -m http.server 8765 --bind 127.0.0.1` from the repository root in a separate terminal, then run `python -B development/case-library/review/browser-audit.py <absolute-path-to-current-snapshot/index.html>`. The optional audit uses the installed Playwright package and `/usr/bin/chromium`, and writes its report/screenshots under `/tmp`. Stop the temporary server afterwards. This is a verification command, not a production hook.

`ot1995-preflight/` is the earlier recovery preparation. It remains labelled as preparation only; its original extraction predated this rebuilt catalogue. The final caught-up coverage is established by the active snapshot and rebuild-validation report.
