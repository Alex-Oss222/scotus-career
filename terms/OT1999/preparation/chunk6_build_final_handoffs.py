"""Mechanically compile completed stage handoffs and invoke the stock Render Input builder."""
from pathlib import Path
import argparse
import hashlib
import json
import re
import runpy
import sys

sys.dont_write_bytecode = True
root = Path(__file__).resolve().parents[3]
term = root / 'terms/OT1999'
parser = argparse.ArgumentParser()
parser.add_argument('--expected', type=int, default=12)
parser.add_argument('--stopped', type=Path, help='JSON object mapping case captions to exact blockers')
args = parser.parse_args()
stopped = json.loads(args.stopped.read_text(encoding='utf-8')) if args.stopped else {}
baseline = json.loads((term / 'freeze/OT_1999CHUNK6_BASELINE_HASHES.json').read_text(encoding='utf-8'))
events = []
for path in (term / 'records').glob('*.md'):
    if path.relative_to(root).as_posix() in baseline or path.name.startswith('.'):
        continue
    body = path.read_text(encoding='utf-8')
    case = re.search(r'^\*\*Case and dockets:\*\* (.+)$', body, re.M).group(1).split(';', 1)[0]
    event = re.search(r'^\*\*Event and date:\*\* (.+)$', body, re.M).group(1)
    date = re.search(r'\d{4}-\d{2}-\d{2}', event).group()
    events.append({'path': path, 'case': case, 'date': date})
events.sort(key=lambda item: (item['date'], item['case'].casefold()))
assert len(events) == args.expected, 'Unexpected completed-event count'
assert len(events) + len(stopped) == 12, 'All twelve matters must be completed or expressly stopped'
receipts = {}
for path in (term / 'freeze').glob('OT_1999CHUNK6_*_COUNTS.json'):
    receipt = json.loads(path.read_text(encoding='utf-8'))
    if 'before_date' in receipt:
        receipts[(receipt['before_date'], receipt['before_case'])] = path.name.removeprefix('OT_1999CHUNK6_').removesuffix('_COUNTS.json')
hashes = []
compilations = {}
for stage in ['COMMITMENTS', 'RECONCILED']:
    sections = [f'# OT1999 chunk 6 {stage.lower()} handoffs', '', 'Mechanical compilation of the individual frozen handoffs, which control. Filesystem handoffs are not represented as repository commits; no Git command was invoked.']
    for event in events:
        key = receipts[(event['date'], event['case'])]
        name = f'OT_1999CHUNK6_{key}_{stage}.md'
        frozen = term / 'freeze' / name
        runtime = term / 'runtime' / name
        assert frozen.read_bytes() == runtime.read_bytes(), name + ': runtime differs from authoritative freeze'
        body = frozen.read_text(encoding='utf-8').rstrip()
        sections.extend(['', '---', '', f'<!-- source-freeze: {name} -->', '', body])
        hashes.append({'case': event['case'], 'stage': stage, 'file': name, 'sha256': hashlib.sha256(frozen.read_bytes()).hexdigest()})
        if stage == 'COMMITMENTS':
            supplement_name = f'OT_1999CHUNK6_{key}_COMMITMENTS_SOURCE_REVALIDATED.md'
            supplement = term / 'freeze' / supplement_name
            if supplement.exists():
                assert supplement.read_bytes() == (term / 'runtime' / supplement_name).read_bytes(), supplement_name + ': runtime differs from authoritative freeze'
                sections.extend(['', f'<!-- source-freeze: {supplement_name}; operative source revalidation at the scope it states -->', '', supplement.read_text(encoding='utf-8').rstrip()])
                hashes.append({'case': event['case'], 'stage': 'COMMITMENTS_SOURCE_REVALIDATED', 'file': supplement_name, 'sha256': hashlib.sha256(supplement.read_bytes()).hexdigest()})
    if stopped:
        sections.extend(['', '## Matters without completed adjudications', ''])
        stopped_keys = {'United States v. McIver': 'MCIVER'}
        for case in stopped:
            key = stopped_keys[case]
            name = f'OT_1999CHUNK6_{key}_{stage}.md'
            frozen = term / 'freeze' / name
            assert frozen.read_bytes() == (term / 'runtime' / name).read_bytes(), name + ': stopped-matter runtime differs'
            # Keep the stage files safe for their original contexts. Exact
            # control/approval blockers belong only in operator-facing metadata.
            sections.extend([f'### {case}', '', 'Frozen stage handoff only; no completed judicial event, assignment or effective holding is supplied.', '', f'<!-- source-freeze: {name} -->', '', frozen.read_text(encoding='utf-8').rstrip(), ''])
            hashes.append({'case': case, 'stage': stage, 'file': name, 'sha256': hashlib.sha256(frozen.read_bytes()).hexdigest(), 'status': 'No completed judicial event'})
    compilations[stage] = '\n'.join(sections).rstrip() + '\n'
for stage, body in compilations.items():
    for folder in ['freeze', 'runtime']:
        (term / folder / f'OT_1999CHUNK6_{stage}.md').write_text(body, encoding='utf-8')
output = term / 'render-inputs/OT_1999CHUNK6.md'
sys.argv = ['build_render_input.py', str(output), *[str(event['path']) for event in events]]
for case, blocker in stopped.items():
    sys.argv.extend(['--stopped', case + ': ' + blocker])
runpy.run_path(str(root / 'tools/build_render_input.py'), run_name='__main__')
receipt = {'completed_events': len(events), 'stopped_matters': stopped, 'individual_stage_hashes': hashes, 'render_input_sha256': hashlib.sha256(output.read_bytes()).hexdigest(), 'method': 'Frozen stage files copied without substantive alteration; stock build_render_input.py copies Record Public Projections. No public Render or repository-history operation.'}
(term / 'freeze/OT_1999CHUNK6_FINAL_HANDOFF_RECEIPT.json').write_text(json.dumps(receipt, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')
print(f'Compiled {len(events)} completed events; {len(stopped)} stopped matters; generated Render Input.')
