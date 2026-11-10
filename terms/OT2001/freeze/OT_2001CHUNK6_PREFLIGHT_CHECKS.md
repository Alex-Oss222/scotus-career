# OT2001 chunk 6 tooling preflight

Checked November 10, 2026, before chunk 6 assembly. This is a filesystem validation summary, not a Git commitment or a completed-Run certificate. No Git command was invoked. Infrastructure was not changed, and the top-level `stone/` directory was not accessed.

## Baseline results

- `python -B tmp/ot2001_no_git_tools.py check_term OT2001 --report-json tmp/OT_2001CHUNK6_baseline_check.json`: exit 0; all executed deterministic checks passed. One explicit warning records that two commit-existence reference checks were deliberately bypassed under the user's no-Git instruction. Those references remain unverified. This baseline does not validate chunk 6 work created afterward.
- `python -B tools/holdings_volumes.py check`: exit 0; doctrinal volumes and continuous compatibility view are synchronized.
- No ledger rebuild was performed in this preflight. The prepared wrapper preserves every existing ledger order/reference and gives new entries explicit unqueried status; it does not invent a hash or claim verified commitment order.

## No-Git tooling

`tmp/ot2001_no_git_tools.py` loads the existing required tool in memory, leaves infrastructure untouched, bypasses its Git lookup function, and explicitly reports the unperformed operation. Its subprocess guard permits only the reviewed, read-only Holdings and split-validation Python subprocesses; any other executable is rejected. Bytecode writes are disabled, including in child Python processes.

For final assembly validation use `python -B tmp/ot2001_no_git_tools.py check_term OT2001`. For the authorized ledger rebuild use `python -B tmp/ot2001_no_git_tools.py rebuild_ledger OT2001`. Optional `--report-json` destinations must remain under `terms/OT2001/` or `tmp/`. Direct invocation of either original tool would invoke Git and is prohibited for this task.

The remaining inspected tools have no Git calls. Their destinations must be kept within the authorized term or temporary directories. There is no freeze script in `tools/`. The only recursive scan in `check_term.py` is bounded to the selected term. `build_entering_law.py` copies opening-state selections only; effective current-term authority must be added faithfully to the term-local reading slice separately.

## Assembly source extraction

`python -B tmp/ot2001_assignment_sources.py` generated `terms/OT2001/entering-law/OT_2001CHUNK6_ASSIGNMENT_SOURCE.md`: 79 Records, 79 public opinion tables, and 140 assignment-containing prose paragraphs from recognized assignment sections. The extraction excludes judgment blocks, holdings, Stone sections, comparator material, and unrelated audit text. It supplies no new counts or assignment decisions. Do not expose it to neutral modeling or reconciliation.

Four Records have no extracted assignment paragraph: `zahrey-v-coffey_merits_2002-03-19.md`, `steele_v_hamilton_county_dig_2002-03-27.md`, `adams_v_florida_power_corp_dig_2002-04-01.md`, and `mathias_v_worldcom_technologies_dig_2002-05-20.md`. Their public opinion tables are present; no assignment was inferred.

For each new decision, count eligible writings from the tables by effective date and same-date alphabetical order. In particular, Compaq's May 28 assignment cannot count later-alphabetical May 28 Records merely because their filesystem artifacts already exist. The extractor can create a bounded source with `--as-of 2002-05-28 --same-day-before "Compaq" --output <authorized-path>`. Later June decisions may count all eligible May 28 Records. Existing durably preserved Records count under Engine section 8 even though the user will perform Git verification and commitment later.
