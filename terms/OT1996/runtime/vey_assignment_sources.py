"""Mechanical pre-event opinion/assignment excerpts; no adjudication or Git."""
from pathlib import Path
import re

term = Path(__file__).resolve().parents[1]
rows = []
for path in (term / 'records').glob('*.md'):
    text = path.read_text(encoding='utf-8')
    m = re.search(r'^\*\*Event and date:\*\*.*?(\d{4}-\d{2}-\d{2})', text, re.M)
    if not m or m[1] >= '1997-04-14':
        continue
    if '## Public Projection' not in text:
        continue
    kernel, public = text.split('## Public Projection', 1)
    lines = kernel.splitlines()
    sections = []
    i = 0
    while i < len(lines):
        if lines[i].startswith('|'):
            end = i + 1
            while end < len(lines) and lines[end].startswith('|'):
                end += 1
            table = '\n'.join(lines[i:end])
            if re.search('author', lines[i], re.I) and re.search('writ|opinion|part', lines[i], re.I):
                sections.append(table)
            i = end
        else:
            i += 1
    for para in kernel.split('\n\n'):
        if re.search(r'assign(?:ment|s|ed|ing)|balance.pool', para, re.I) and not para.lstrip().startswith('|'):
            sections.append(para)
    topology = re.search(r'^## (?:\d+\. )?Opinion Topology\s*\n(.*?)(?=^## |\Z)', public, re.M | re.S)
    if topology:
        sections.append('Public opinion topology (verbatim):\n\n' + topology[1].strip())
    if sections:
        rows.append((m[1], path.name, sections))
out = ['# Vey pre-event assignment sources', '',
       'Mechanical excerpts only. The cited Records control. No tally or legal conclusion is generated. Only Records effective before 1997-04-14 appear; no opinion form is prescribed.', '']
for date, name, sections in sorted(rows):
    out += [f'## {date} — {name}', '', f'Source: ../../records/{name}', '']
    out += ['\n\n'.join(sections), '']
target = term / 'runtime/assembly/OT_1996CHUNK6_68_ASSIGNMENT_SOURCES.md'
target.write_text('\n'.join(out), encoding='utf-8')
print(f'{target}: {len(rows)} Record extracts')
