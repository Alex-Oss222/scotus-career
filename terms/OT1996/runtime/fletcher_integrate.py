"""Project Fletcher's canonical public law and published positions in place."""
from pathlib import Path
import re

TERM = Path(__file__).resolve().parents[1]
RECORD = TERM / 'records/Fletcher_v_Kalina_merits_1997-06-16.md'


def main():
    text = RECORD.read_text(encoding='utf-8-sig')
    kernel, public = text.split('## Public Projection', 1)
    case = re.search(r'^\*\*Case and dockets:\*\*\s*(.+)', text, re.M)[1].strip()
    result = re.search(r'^\*\*Result:\*\*\s*(.+)', text, re.M)[1].strip()
    event = re.search(r'^\*\*Event and date:\*\*\s*(.+)', text, re.M)[1]
    assert '1997-06-16' in event
    assert '**Version / lineage:** Original decision.' in kernel

    def block(name):
        match = re.search(r'^## (?:\d+\. )?' + re.escape(name) + r'\s*\n(.*?)(?=^## |\Z)', public, re.M | re.S)
        if not match:
            raise ValueError('Missing public block: ' + name)
        return re.sub(r'^(#{3,4}) ', r'\1## ', match[1].strip(), flags=re.M)

    heading = '### 1997-06-16 — ' + case.rstrip('.')
    authority = 'Authority: [Record](../records/' + RECORD.name + ').'
    law = '\n\n'.join([heading, authority, '#### Opinion Topology', block('Opinion Topology'),
                        '#### Holdings', block('Holdings'), '#### Precedent Treatment', block('Precedent Treatment'),
                        '#### Law After Decision', block('Law After Decision')])
    # All published separate positions are supplied in this Record's public block.
    positions = '\n\n'.join([heading, authority, block('Separate Writings')])
    procedure = '\n\n'.join([heading, authority, block('Procedure After Action')])

    def replace_entry(doc, start, end, material):
        a = doc.index(start)
        b = doc.index(end, a + len(start))
        section = doc[a:b]
        pattern = r'^### 1997-06-16 — Fletcher v\. Kalina[^\n]*\n.*?(?=^### |\Z)'
        matches = list(re.finditer(pattern, section, re.M | re.S))
        assert len(matches) == 1, (start, len(matches))
        m = matches[0]
        return doc[:a] + section[:m.start()] + material + '\n\n' + section[m.end():] + doc[b:]

    updates = {}
    for name in ('continuity.md', 'neutral-projection.md'):
        path = TERM / 'workspace' / name
        doc = path.read_text(encoding='utf-8-sig')
        if name == 'continuity.md':
            pattern = r'^\| 1997-06-16 \| Fletcher v\. Kalina[^\n]*$'
            row = '| 1997-06-16 | ' + case + ' | ' + result + ' | [Record](../records/' + RECORD.name + ') |'
            doc, n = re.subn(pattern, lambda _: row, doc, flags=re.M)
            assert n == 1
            doc = replace_entry(doc, '## 3. Current Law', '## 4. Material Published Noncontrolling Positions', law)
            doc = replace_entry(doc, '## 4. Material Published Noncontrolling Positions', '## 5. Current Procedure and Institution', positions)
            doc = replace_entry(doc, '## 5. Current Procedure and Institution', '## 6. Blockers and Revalidation Needs', procedure)
        else:
            doc = replace_entry(doc, '## Current Court law in effective order', '## Material published noncontrolling positions', law)
            doc = replace_entry(doc, '## Material published noncontrolling positions', '## Public procedure after completed actions', positions)
            doc = replace_entry(doc, '## Public procedure after completed actions', '## Scope and cutoff', procedure)
        updates[path] = doc

    # Validate all replacements before publishing coordinated projections.
    for path, doc in updates.items():
        path.write_text(doc, encoding='utf-8', newline='\n')
    print('Projected Fletcher law, published positions and procedure in both workspace projections.')


if __name__ == '__main__':
    main()
