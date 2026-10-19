"""Project the completed June 2 Boggs event; no adjudication and no Git."""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[3]
TERM = ROOT / 'terms/OT1996'
RECORD = TERM / 'records/Boggs_v_Boggs_merits_1997-06-02.md'


def main():
    text = RECORD.read_text(encoding='utf-8')
    public = text.split('## Public Projection', 1)[1].strip()
    case = re.search(r'^\*\*Case and dockets:\*\*\s*(.+)', text, re.M)[1].strip()
    result = re.search(r'^\*\*Result:\*\*\s*(.+)', text, re.M)[1].strip()
    assert '1997-06-02' in re.search(r'^\*\*Event and date:\*\*\s*(.+)', text, re.M)[1]

    def block(name):
        m = re.search(r'^## (?:\d+\. )?' + re.escape(name) + r'\s*\n(.*?)(?=^## |\Z)', public, re.M | re.S)
        assert m, name
        return m[1].strip()

    heading = '### 1997-06-02 — ' + case.rstrip('.')
    authority = 'Authority: [Record](../records/' + RECORD.name + ').'
    law_parts = [heading, authority]
    for name in ['Opinion Topology', 'Holdings', 'Precedent Treatment', 'Law After Decision']:
        law_parts.extend(['#### ' + name, block(name)])
    law = '\n\n'.join(law_parts)
    separate = '\n\n'.join([heading, authority, block('Separate Writings')])
    procedure = '\n\n'.join([heading, authority, block('Procedure After Action')])

    manifest_path = TERM / 'workspace/manifest.md'
    manifest = manifest_path.read_text(encoding='utf-8')
    rows = [line for line in manifest.splitlines() if re.match(r'^\| \d{4}-\d{2}-\d{2} \| OT_1996CHUNK', line)]
    assert len(rows) == 153
    chunk = [line for line in rows if '| OT_1996CHUNK9 |' in line]
    assert len(chunk) == 11 and all('| Completed:' in line for line in chunk)
    next_row = next(line for line in rows if '| Open |' in line or '| Stopped:' in line)
    assert '| OT_1996CHUNK10 |' in next_row

    def insert(doc, start, end, material):
        a = doc.index(start)
        b = doc.index(end, a + len(start))
        section = doc[a:b]
        assert heading not in section, start
        at = section.index('### 1997-06-02 — De Buono')
        return doc[:a] + section[:at] + material + '\n\n\n' + section[at:] + doc[b:]

    for name in ['continuity.md', 'neutral-projection.md']:
        path = TERM / 'workspace' / name
        doc = path.read_text(encoding='utf-8')
        assert doc.count('105 Court events and 3 admitted sources') == 1
        doc = doc.replace('105 Court events and 3 admitted sources', '106 Court events and 3 admitted sources')
        old_row = [line for line in doc.splitlines() if '| Boggs v. Boggs |' in line]
        assert len(old_row) == 1
        doc = doc.replace(old_row[0], next_row)
        if name == 'continuity.md':
            at = doc.index('| 1997-06-02 | De Buono')
            row = '| 1997-06-02 | ' + case + ' | ' + result + ' | [Record](../records/' + RECORD.name + ') |\n'
            doc = doc[:at] + row + doc[at:]
            doc = insert(doc, '## 3. Current Law', '## 4. Material Published Noncontrolling Positions', law)
            doc = insert(doc, '## 4. Material Published Noncontrolling Positions', '## 5. Current Procedure and Institution', separate)
            doc = insert(doc, '## 5. Current Procedure and Institution', '## 6. Blockers and Revalidation Needs', procedure)
            a = doc.index('## 6. Blockers and Revalidation Needs')
            b = doc.index('## 7. Source and Research Cutoff', a)
            doc = doc[:a] + ('## 6. Blockers and Revalidation Needs\n\n'
                'All eleven chunk 9 Court events are complete in their original chronological slots. No chunk 9 matter remains stopped. '
                'The earlier Boggs assembly stop is resolved by the completed June 2 Record. '
                'The five other completed June 2 Records retain their common earlier-law baseline, judgments, reasoning and assignments. '
                'See the [dependency review](../freeze/OT_1996CHUNK9_102_DEPENDENCY_REVIEW.md) and '
                '[resumption validation](../freeze/OT_1996CHUNK9_102_RESUMPTION_VALIDATION.md).\n\n'
                'Gaydos, Vey and Brown retain the separate open procedural matters recorded in the manifest; no new event, deadline or disposition is inferred.\n\n') + doc[b:]
        else:
            doc = insert(doc, '## Current Court law in effective order', '## Material published noncontrolling positions', law)
            doc = insert(doc, '## Material published noncontrolling positions', '## Public procedure after completed actions', separate)
            doc = insert(doc, '## Public procedure after completed actions', '## Scope and cutoff', procedure)
            assert doc.count('105 Court events and three admitted sources') == 1
            doc = doc.replace('105 Court events and three admitted sources', '106 Court events and three admitted sources')
        path.write_text(doc, encoding='utf-8')

    old = re.search(r'^There are 48 distinct scheduled dates,.*$', manifest, re.M)
    assert old
    manifest = manifest.replace(old[0],
        'There are 48 distinct scheduled dates, including 28 multi-matter groups; eleven groups cross chunk boundaries. '
        'One hundred six current-term Court events through chunk 9 are completed, with the current cursor at June 2, 1997; '
        'three admitted sources are separately recorded. All eleven chunk 9 events are complete in their original chronological slots. '
        "Brown's April 28 reargument order leaves that matter open and carried forward, with no reargument date or added event. "
        'Uncoordinated June 2 peers across chunks 9 and 10 share their common pre-June-2 entering-law baseline; '
        'the completed same-day decisions are combined only prospectively.')
    manifest_path.write_text(manifest, encoding='utf-8')
    print('Projected Boggs from its Public Projection into both cumulative workspace projections; manifest scope updated.')


if __name__ == '__main__':
    main()
