from pathlib import Path
import re

root = Path(__file__).resolve().parents[4]
base = Path(__file__).parent
law = root / 'terms/OT2001/entering-law/OT_2001CHUNK7_EMERSON_LAW_CLEAN.md'
text = law.read_text(encoding='utf-8')
lines = text.splitlines()
def section(s, heading):
    rows = s.splitlines()
    start = next(i for i, row in enumerate(rows) if row == heading)
    level = len(heading) - len(heading.lstrip('#'))
    end = len(rows)
    for i in range(start+1,len(rows)):
        match = re.match(r'^(#{1,6})\s', rows[i])
        if match and len(match[1]) <= level:
            end = i
            break
    return '\n'.join(rows[start:end]).strip()

selected = ['# Selected arms authorities', '', 'Mechanical reading extracts from the generated entering-law slice.', '']
for heading in ['#### Love v. Pepersack', '#### United States v. Hale', '#### Fraternal Order of Police v. United States', '#### United States v. Wright', '#### United States v. Napier']:
    matches = [row for row in lines if row.startswith(heading)]
    assert len(matches)==1, (heading,matches)
    selected += [section(text,matches[0]),'']
(base / 'selected_law.md').write_text('\n'.join(selected),encoding='utf-8')

prior = (root / 'terms/OT2000/output/OT_2000CHUNK6.md').read_text(encoding='utf-8')
heading = next(row for row in prior.splitlines() if row.startswith('### United States v. Napier,'))
napier = section(prior,heading)
(base / 'napier_public_copy.md').write_text(napier+'\n',encoding='utf-8')
print('Selected law and complete public Napier entry copied mechanically.')
