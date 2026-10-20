"""Mechanically project the one completed Thomasson event into the workspace."""
from pathlib import Path
import re

term = Path(__file__).resolve().parents[1]
record = term / 'records/Thomasson_v_Perry_merits_1997-06-09.md'
text = record.read_text(encoding='utf-8')
kernel, public = text.split('## Public Projection', 1)
case = re.search(r'^\*\*Case and dockets:\*\*\s*(.+)', text, re.M)[1].strip()
result = re.search(r'^\*\*Result:\*\*\s*(.+)', text, re.M)[1].strip()
assert '1997-06-09' in re.search(r'^\*\*Event and date:\*\*\s*(.+)', text, re.M)[1]

def block(name):
    match = re.search(r'^## (?:\d+\. )?' + re.escape(name) + r'\s*\n(.*?)(?=^## |\Z)', public, re.M | re.S)
    if not match:
        raise ValueError('Missing public block: ' + name)
    return match[1].strip()

heading = '### 1997-06-09 — ' + case.rstrip('.')
authority = 'Authority: [Record](../records/' + record.name + ').'
law = '\n\n'.join([heading, authority, '#### Opinion Topology', block('Opinion Topology'),
                    '#### Holdings', block('Holdings'), '#### Precedent Treatment', block('Precedent Treatment'),
                    '#### Law After Decision', block('Law After Decision')])
procedure = '\n\n'.join([heading, authority, block('Procedure After Action')])
positions_match = re.search(r'^### Material published noncontrolling positions\s*\n(.*?)(?=^###? |\Z)', kernel, re.M | re.S)
if not positions_match:
    raise ValueError('Missing complete published-position continuity subsection')
positions = '\n\n'.join([heading, authority, positions_match[1].strip()])

def insert(doc, start, end, material):
    a = doc.index(start)
    b = doc.index(end, a + len(start))
    section = doc[a:b]
    if heading in section:
        raise ValueError('Thomasson already projected in ' + start)
    at = section.index('### 1997-06-09 — Vey v. Clinton')
    return doc[:a] + section[:at] + material + '\n\n' + section[at:] + doc[b:]

updates = {}
for name in ['continuity.md', 'neutral-projection.md']:
    path = term / 'workspace' / name
    doc = path.read_text(encoding='utf-8')
    assert doc.count('117 Court events and 3 admitted sources') == 1
    assert doc.count('Thomasson remains unadjudicated.') == 1
    doc = doc.replace('117 Court events and 3 admitted sources', '118 Court events and 3 admitted sources')
    doc = doc.replace('Thomasson remains unadjudicated.', 'Thomasson is completed in its June 9 slot; all twelve chunk 10 events are complete.')
    if name == 'continuity.md':
        row = '| 1997-06-09 | ' + case + ' | ' + result + ' | [Record](../records/' + record.name + ') |\n'
        at = doc.index('| 1997-06-09 | Vey v. Clinton')
        doc = doc[:at] + row + doc[at:]
        doc = insert(doc, '## 3. Current Law', '## 4. Material Published Noncontrolling Positions', law)
        doc = insert(doc, '## 4. Material Published Noncontrolling Positions', '## 5. Current Procedure and Institution', positions)
        doc = insert(doc, '## 5. Current Procedure and Institution', '## 6. Blockers and Revalidation Needs', procedure)
        old = re.search(r'^Eleven chunk 10 Court events are complete\. Thomasson.*$', doc, re.M)
        assert old
        doc = doc.replace(old[0], 'All twelve chunk 10 Court events are complete. No stopped matter remains in the chunk. Thomasson\'s June 9 affirmance has been reviewed against every existing same-day and later Record; no material dependency or entering-law correction was found. The [resumption validation](../freeze/OT_1996CHUNK10_THOMASSON_FINAL_VALIDATION.md) records the completed checks and the Git verification reserved for the operator.')
    else:
        doc = insert(doc, '## Current Court law in effective order', '## Material published noncontrolling positions', law)
        doc = insert(doc, '## Material published noncontrolling positions', '## Public procedure after completed actions', positions)
        doc = insert(doc, '## Public procedure after completed actions', '## Scope and cutoff', procedure)
        assert doc.count('Coverage is 117 Court events') == 1
        doc = doc.replace('Coverage is 117 Court events', 'Coverage is 118 Court events')
    updates[path] = doc

manifest_path = term / 'workspace/manifest.md'
manifest = manifest_path.read_text(encoding='utf-8')
old = re.search(r'^There are 48 distinct scheduled dates,.*$', manifest, re.M)
assert old
replacement = old[0].replace('One hundred seventeen current-term Court events', 'One hundred eighteen current-term Court events')
assert 'Eleven chunk 10 events are complete; Thomasson remains stopped at its exact inventory blocker and supplies no adjudication.' in replacement
replacement = replacement.replace('Eleven chunk 10 events are complete; Thomasson remains stopped at its exact inventory blocker and supplies no adjudication.', 'All twelve chunk 10 events are complete in their existing slots; no chunk 10 matter remains stopped.')
manifest = manifest.replace(old[0], replacement)
updates[manifest_path] = manifest

# All assertions precede the coordinated workspace writes.
for path, data in updates.items():
    path.write_text(data, encoding='utf-8')
print('Projected Thomasson law, all published separate positions and procedure; cursor remains June 16.')
