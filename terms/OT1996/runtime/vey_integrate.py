"""Project the completed Vey Record into the current workspace and chunk input."""
from pathlib import Path
import re
import subprocess
import sys

root = Path(__file__).resolve().parents[3]
term = root / 'terms/OT1996'
record = term / 'records/In_re_Vey_financial_leave_1997-04-14.md'
text = record.read_text(encoding='utf-8')
public = text.split('## Public Projection\n', 1)[1]
case = re.search(r'^\*\*Case and dockets:\*\*\s*(.+)', text, re.M)[1].strip()
result = re.search(r'^\*\*Result:\*\*\s*(.+)', text, re.M)[1].strip()
assert '1997-04-14' in re.search(r'^\*\*Event and date:\*\*\s*(.+)', text, re.M)[1]

def block(name):
    m = re.search(r'^## (?:\d+\. )?' + re.escape(name) + r'\s*\n(.*?)(?=^## |\Z)', public, re.M | re.S)
    if not m:
        raise ValueError('Missing public block: ' + name)
    return m[1].strip()

heading = '### 1997-04-14 — ' + case.rstrip('.')
authority = 'Authority: [Record](../records/' + record.name + ').'
law = '\n\n'.join([heading, authority, '#### Opinion Topology', block('Opinion Topology'),
                    '#### Holdings', block('Holdings'),
                    '#### Precedent Treatment', block('Precedent Treatment'),
                    '#### Law After Decision', block('Law After Decision')])
procedure = '\n\n'.join([heading, authority, block('Procedure After Action')])

def insert_in_section(doc, start, end, material):
    a = doc.index(start)
    b = doc.index(end, a + len(start))
    selected = doc[a:b]
    if heading in selected:
        raise ValueError('Vey already projected in ' + start)
    at = selected.index('### 1997-04-15')
    return doc[:a] + selected[:at] + material + '\n\n' + selected[at:] + doc[b:]

for name in ['continuity.md', 'neutral-projection.md']:
    path = term / 'workspace' / name
    doc = path.read_text(encoding='utf-8')
    assert doc.count('70 Court events and 2 admitted sources') == 1
    doc = doc.replace('70 Court events and 2 admitted sources', '71 Court events and 2 admitted sources')
    if name == 'continuity.md':
        row = '| 1997-04-14 | ' + case + ' | ' + result + ' | [Record](../records/' + record.name + ') |\n'
        at = doc.index('| 1997-04-15 |')
        doc = doc[:at] + row + doc[at:]
        doc = insert_in_section(doc, '## 3. Current Law', '## 4. Material Published Noncontrolling Positions', law)
        doc = insert_in_section(doc, '## 5. Current Procedure and Institution', '## 6. Blockers and Revalidation Needs', procedure)
        lines = doc.splitlines()
        stopped = [line for line in lines if '| In re Vey |' in line and '| Stopped:' in line]
        assert len(stopped) == 1
        doc = doc.replace(stopped[0], 'No stopped matter remains from chunk 6. The April 14 financial event is completed; the distinct original petition remains reserved as stated in its Record. The adopted financial premise and physically separated resumption stages are documented in [the resumption validation](../freeze/OT_1996CHUNK6_68_RESUMPTION_VALIDATION.md).')
    else:
        doc = insert_in_section(doc, '## Current Court law in effective order', '## Material published noncontrolling positions', law)
        doc = insert_in_section(doc, '## Public procedure after completed actions', '## Scope and cutoff', procedure)
    path.write_text(doc, encoding='utf-8')

manifest_path = term / 'workspace/manifest.md'
manifest = manifest_path.read_text(encoding='utf-8')
old = re.search(r'^There are 48 distinct scheduled dates,.*$', manifest, re.M)
assert old
manifest = manifest.replace(old[0],
    'There are 48 distinct scheduled dates, including 28 multi-matter groups; eleven groups cross chunk boundaries. Seventy-one current-term Court events through chunk 6 are completed, with the current cursor at April 21, 1997; two admitted sources are separately recorded. All twelve chunk 6 financial, procedural and merits events are complete in their original slots. The remaining April 21 peers in chunk 7 use the common pre-April-21 entering-law baseline; Blessing and Joseph A. do not become their precedent by processing order.')
assert '| In re Vey — original petition, No. 96-8005 |' not in manifest
manifest = manifest.rstrip() + '\n| In re Vey — original petition, No. 96-8005 | Open: the April 14 financial motion is completed, but original jurisdiction, exceptional circumstances and the petition itself remain reserved. No new event or deadline is scheduled by this entry. | [April 14 Record](../records/' + record.name + ') |\n'
manifest_path.write_text(manifest, encoding='utf-8')

subprocess.run([sys.executable, '-B', str(root / 'tools/rebuild_manifest.py'), 'OT1996'], check=True)
subprocess.run([sys.executable, '-B', str(term / 'runtime/vey_resume_checks.py'), 'ledger'], check=True)
target = term / 'render-inputs/OT_1996CHUNK6.md'
old_input = target.read_text(encoding='utf-8')
names = re.findall(r'<!-- source-record: ([^>]+) -->', old_input)
assert len(names) == 11 and record.name not in names
names.append(record.name)
subprocess.run([sys.executable, '-B', str(root / 'tools/build_render_input.py'), str(target)] +
               [str(term / 'records' / name) for name in names], check=True)
print('Projected Vey from its Public Projection; rebuilt 12-event input without stopped metadata.')
