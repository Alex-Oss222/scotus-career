"""Mechanical, scoped copies for the June 28 control handoff. Run with python -B."""
from pathlib import Path
import re
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / 'terms/OT1999/entering-law/OT_1999CHUNK9_LATE.md'

def section(text, title, level=None):
    lines = text.splitlines()
    hits = [i for i, line in enumerate(lines) if re.match(r'^#{1,5} ', line)
            and title.casefold() in line.casefold()
            and (level is None or len(line)-len(line.lstrip('#')) == level)]
    if len(hits) != 1:
        raise ValueError((title, hits))
    start = hits[0]
    depth = len(lines[start])-len(lines[start].lstrip('#'))
    end = next((i for i in range(start+1, len(lines))
                if re.match(r'^#{1,'+str(depth)+r'} ', lines[i])), len(lines))
    return '\n'.join(lines[start:end]).strip()

def read(p):
    return (ROOT/p).read_text(encoding='utf-8')

standards = ['Speech burdens in a content-neutral injunction', 'Lemon test',
             'Private religious viewpoints in public forums and printing benefits',
             'Protected choice and the six-step standard for previability regulation',
             'Medical emergency and the separate disclosure-health defense',
             'North Dakota definitions and separate enforcement conditions']
cmd=[sys.executable,'-B',str(ROOT/'tools/build_entering_law.py'),str(OUT)]
for title in standards: cmd += ['--standard-heading',title]
subprocess.run(cmd,check=True,cwd=ROOT)
base = OUT.read_text(encoding='utf-8')
parts=[base, '\n## Chronology and reading scope\n\nCutoff: immediately before June 28, 2000. All four June 28 matters use the same entering-law baseline. The June 26 Jones decision must be added after its completed public projection is available; no pending position or historical result supplies it. This copy contains no target-case outcome or private position. Authority remains in the cited trackers and completed events.\n']

fa='state/holdings/first-amendment.md'
cr='state/holdings/civil-rights.md'
for label,file,titles in [
 ('Dale',fa,['Hurley v.']),
 ('Hill',fa,['Madsen v.','Schenck v.']),
 ('Mitchell',fa,['Rosenberger v.','Agostini v.','Jackson v. Benson']),
 ('Stenberg',cr,['Reproductive liberty and constitutional precedent','Abortion emergency care','Fargo Women','Women\u2019s Medical Professional Corp. v. Voinovich'])]:
    parts += ['\n## '+label+' - controlling prior holdings\n', 'Source: `'+file+'`. Copied sections.\n']
    text=read(file)
    for title in titles: parts += [section(text,title), '\n']

projection=read('terms/OT1999/workspace/neutral-projection.md')
lines=projection.splitlines()
parts += ['\n## Effective current-term public law and positions\n\nSource: `terms/OT1999/workspace/neutral-projection.md`. Every matching public section is copied; no raw Record or audit annex was read.\n']
names=['Strout v. Albanese','Board of Regents of the University of Wisconsin System v. Southworth','Santa Fe Independent School District v. Doe']
for name in names:
    starts=[i for i,l in enumerate(lines) if l.startswith('### ') and name in l]
    for start in starts:
        end=next((i for i in range(start+1,len(lines)) if re.match(r'^#{1,3} ',lines[i])),len(lines))
        parts+=['\n'.join(lines[start:end]).strip(),'\n']

priors=[('terms/OT1994/output/OT_1994CHUNK8.md','Hurley'),
        ('terms/OT1993/output/OT_1993CHUNK8.md','Madsen'),
        ('terms/OT1996/output/OT_1996CHUNK4.md','Schenck'),
        ('terms/OT1996/output/OT_1996CHUNK11.md','Agostini'),
        ('terms/OT1998/output/OT_1998CHUNK5.md','Jackson v. Benson'),
        ('terms/OT1997/output/OT_1997CHUNK7.md','Voinovich')]
parts+=['\n## Prior public Justice positions - scoped source copies\n']
for file,name in priors:
    sec=section(read(file),name,3)
    parts+=['\n### '+name+' - published source\n\nSource: `'+file+'`.\n']
    if name=='Hurley':
        parts+=[sec]
        continue
    sl=sec.splitlines()
    for heading in ['Opinion Topology','Separate Writings','Separate Positions']:
        matches=[l for l in sl if l.startswith('#### ') and heading in l]
        for title in matches:
            parts+=[section(sec,title.removeprefix('#### '),4)]

OUT.write_text('\n\n'.join(parts).rstrip()+'\n',encoding='utf-8')
print('Focused law handoff bytes:',OUT.stat().st_size)
