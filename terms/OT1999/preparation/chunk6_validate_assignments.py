"""Check frozen count receipts against actual prior Record opinion tables; no Git."""
from pathlib import Path
import importlib.util
import json
import re
import sys

sys.dont_write_bytecode = True
root = Path(__file__).resolve().parents[3]
term = root / 'terms/OT1999'
spec = importlib.util.spec_from_file_location('assignment_source', root / 'tmp/ot1999_chunk6_prior_assignments.py')
source = importlib.util.module_from_spec(spec)
spec.loader.exec_module(source)
baseline = json.loads((term / 'freeze/OT_1999CHUNK6_BASELINE_HASHES.json').read_text(encoding='utf-8'))
durable_order = {}
for line in (term / 'workspace/ledger.md').read_text(encoding='utf-8').splitlines():
    if not line.startswith('|'):
        continue
    cells = [cell.strip() for cell in line.strip('|').split('|')]
    match = re.search(r'\[record\]\(\.\./records/([^/]+\.md)\)', line)
    if match and cells[0].isdigit():
        durable_order[match.group(1)] = int(cells[0])
records = []
for path in (term / 'records').glob('*.md'):
    if path.name.startswith('.'):
        continue
    item = source.selected_record(path)
    item['caption'] = item['case'].split(';', 1)[0]
    item['path'] = path
    item['key'] = (item['date'], item['caption'].casefold())
    records.append(item)
records.sort(key=lambda item: item['key'])
new = [item for item in records if item['path'].relative_to(root).as_posix() not in baseline]
errors = []
report = []
pending = []
for path in sorted((term / 'freeze').glob('OT_1999CHUNK6_*_COUNTS.json')):
    if path.name == 'OT_1999CHUNK6_CURRENT_COUNTS.json':
        continue
    frozen = json.loads(path.read_text(encoding='utf-8'))
    if 'before_date' not in frozen:
        continue
    key = (frozen['before_date'], frozen['before_case'].casefold())
    current = next((item for item in new if item['key'] == key), None)
    if current is None:
        pending.append(path.name)
        continue
    counts = dict.fromkeys(source.JUSTICES, 0)
    counted = []
    current_order = durable_order.get(current['path'].name)
    if current_order is None:
        errors.append(current['path'].name + ': missing durable ledger order; integrate before final validation')
        continue
    for item in records:
        if item['key'] >= key:
            break
        # A later-written earlier-dated event never retroactively changes an
        # assignment already made. The ledger supplies order only, not authors.
        if durable_order.get(item['path'].name, float('inf')) >= current_order:
            continue
        for author in item['authors']:
            counts[author] += 1
        if item['authors']:
            counted.append({'date': item['date'], 'case': item['caption'], 'authors': sorted(item['authors']), 'record': item['path'].name})
    for name, actual in [('counts', counts), ('total', sum(counts.values())), ('last_event', counted[-1] if counted else None), ('counted_events', counted)]:
        if frozen.get(name) != actual:
            errors.append(path.name + ': ' + name + ' differs from actual prior Records')
    text = current['path'].read_text(encoding='utf-8')
    statement = re.search(r'^\*\*Fresh counts before assignment:\*\*(.*)$', text, re.M)
    if statement is None:
        errors.append(current['path'].name + ': exact fresh-count statement absent')
    else:
        for justice, count in counts.items():
            if re.search(re.escape(justice) + r'\s+' + str(count) + r'\b', statement.group(1)) is None:
                errors.append(current['path'].name + ': count statement differs for ' + justice)
    report.append({'case': current['caption'], 'date': current['date'], 'counts_before': counts, 'lead_authors': sorted(current['authors']), 'receipt': path.name})
covered = {(row['date'], row['case'].casefold()) for row in report}
for item in new:
    if item['authors'] and item['key'] not in covered:
        errors.append(item['path'].name + ': counted lead lacks audited receipt')
if len(new) == 12 and pending:
    errors.extend(name + ': unmatched receipt after all twelve Records are written' for name in pending)
result = {'checked_new_records': len(new), 'checked_assignments': len(report), 'pending_count_receipts_without_records': pending, 'errors': errors, 'assignments': sorted(report, key=lambda item: (item['date'], item['case'].casefold())), 'limits': 'Checks arithmetic, effective-date/alphabetical ordering, source membership and written count statements. Actual Record opinion tables supply authors; preserved durable ledger order excludes later-written earlier-dated events from retrospective counts. Counts prepared for unfinished assembly are reported separately and add no lead. Eligibility, opinion form and comparative fit remain the legal judgments recorded in each assembly receipt. No repository-history query or Git command.'}
(term / 'freeze/OT_1999CHUNK6_ASSIGNMENT_CHECK.json').write_text(json.dumps(result, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')
print(json.dumps({'checked_new_records': len(new), 'checked_assignments': len(report), 'errors': errors}, ensure_ascii=False))
raise SystemExit(bool(errors))
