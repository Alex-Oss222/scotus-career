"""Copy selected public same-term authority with strict case-specific chronology."""
from pathlib import Path
import hashlib
import json
import re

base = Path('terms/OT2002')
source = base / 'workspace/neutral-projection.md'
text = source.read_text(encoding='utf-8')
selections = json.loads((base / 'entering-law/OT_2002CHUNK7_SELECTIONS.json').read_text(encoding='utf-8'))
cases = selections['matters']
relevance = {
    'Newman v. Sathyavaglswaran': [79],
    'Tenafly Eruv Association': [80],
    'Adland v. Russ': [80],
    'Commack Self-Service Kosher Meats': [80],
    'Montiel v. Davis': [81],
    'Cartwright v. Barnes': [81],
    'Cano v. Davis': [81],
    'Konop v. Hawaiian Airlines': [82, 88],
    'United States v. Bach': [82],
    'FCC v. NextWave': [83],
    'Gibson v. County of Washoe': [84],
    'McClendon v. City of Columbia': [84],
    'Howsam v. Dean Witter': [85],
    'Planned Parenthood of the Columbia/Willamette': [87],
    'American Amusement Machine Association': [87],
    'Popovich v. Cuyahoga': [89],
    'Westside Mothers v. Haveman': [89],
    'Odom v. Antrican': [89],
    'Okpalobi v. Foster': [89],
}
out = ['# OT2002 chunk 7 same-term entering-law supplement', '',
       'Derived public reading copy. The source projection is sanitized; effective Records remain authority. No future holding or unrelated same-date holding enters a case. The case-specific table controls eligibility; cross-case relevance is a navigation aid, not an additional rule.', '',
       'Source: `terms/OT2002/workspace/neutral-projection.md`.', '',
       'Source SHA-256: `' + hashlib.sha256(source.read_bytes()).hexdigest() + '`.', '',
       '## Event cutoffs', '', '| Matter | Event date | Permitted same-term law |', '|---|---|---|']
for case in cases:
    out.append(f"| {case['number']}. {case['case']} | {case['date']} | Completed events strictly before {case['date']}; unrelated events on that date excluded. |")
out += ['', '## Source opening instructions (verbatim)', '']
opening = re.search(r'(?ms)^## Opening authority and cursor\n(.*?)(?=^## )', text).group(1).strip()
out.append(opening)
current_category = ''
selected_count = 0
for chunk in re.split(r'(?m)(?=^## )', text):
    category = chunk.splitlines()[0] if chunk else ''
    if category not in ('## Current law', '## Published noncontrolling positions'):
        continue
    for section in re.split(r'(?m)(?=^### )', chunk)[1:]:
        heading = section.splitlines()[0]
        match = re.match(r'^### (\d{4}-\d{2}-\d{2}) — (.*)', heading)
        if not match:
            continue
        date, title = match.groups()
        relevant = sorted({n for name, numbers in relevance.items() if name in title for n in numbers})
        eligible = [c['number'] for c in cases if date < c['date']]
        if not relevant or not eligible:
            continue
        assert all(n in eligible for n in relevant), (heading, relevant, eligible)
        if category != current_category:
            out += ['', category, '']
            current_category = category
        out += [f"Navigation: directly or contextually relevant to matter(s) {', '.join(map(str, relevant))}. Date-eligible for matter(s) {', '.join(map(str, eligible))}. The following source section is copied verbatim.", '', section.strip(), '']
        selected_count += 1
out += ['## Excluded later effective law', '',
        'The projection includes completed decisions as late as June 26, 2003. In particular, Georgia v. Ashcroft and Old Person v. Brown (June 26) do not enter Branch. Lawall (April 28) does not enter any March or April event; Benson (May 27), Roe v. Texas (June 2), and Center for Reproductive Law and Policy (June 16) do not enter any event in this chunk. No pending matter supplies law merely from its planned earlier date.', '']
target = base / 'entering-law/OT_2002CHUNK7_SAME_TERM.md'
target.write_text('\n'.join(out).rstrip()+'\n', encoding='utf-8')
print(f'{target.as_posix()}: {selected_count} source sections copied')
