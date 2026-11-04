from pathlib import Path
import re, subprocess, sys

root = Path(__file__).resolve().parents[3]
out = root / 'terms/OT1999/entering-law'
out.mkdir(parents=True, exist_ok=True)

def section(path, title):
    text = (root/path).read_text(encoding='utf-8')
    lines = text.splitlines()
    starts = [(i,l) for i,l in enumerate(lines) if re.match(r'^#{2,5} ',l)]
    found = [(i,l) for i,l in starts if re.sub(r'^#+ ', '', l) == title]
    assert len(found) == 1, (path,title,found)
    start,line = found[0]; level=len(line)-len(line.lstrip('#'))
    end=next((i for i,l in starts if i>start and len(l)-len(l.lstrip('#')) <= level),len(lines))
    return '\n'.join(lines[start:end]).strip()

def write(name, selections, extra=''):
    parts=['# Focused entering-law copy — '+name,'','Derived reading copy; cited authorities remain controlling. Event dates: June 26, 2000 for Jones, Mobil/Marathon and Henerey; June 29, 2000 for Alaska. No current-case historical outcome is included.','']
    for path,title in selections:
        parts += ['Source: `'+path+'`; exact heading: '+title,'',section(path,title),'']
    if extra: parts += [extra]
    (out/('OT_1999CHUNK9_'+name+'.md')).write_text('\n'.join(parts)+'\n',encoding='utf-8')

cmd=[sys.executable,'-B',str(root/'tools/build_entering_law.py'),str(out/'OT_1999CHUNK9_EARLY_TOOL.md')]
for title in ['Write-in voting within the complete ballot-access system','Actual federal contractual undertakings and allocated regulatory risk','Assigned school productions and teachers’ personal speech','Ordinary high-water emergence for natural island status','Coordinate fixation of state-federal submerged-land boundaries']:
    cmd += ['--standard-heading',title]
subprocess.run(cmd,check=True,cwd=root)
jones=[('state/holdings/election-law.md','Burdick v. Takushi, 504 U.S. 428 (1992)'),('state/holdings/election-law.md','Timmons v. Twin Cities Area New Party'),('state/holdings/first-amendment.md','Hurley v. Irish-American Gay, Lesbian and Bisexual Group of Boston'),('state/STANDARDS_AND_TESTS.md','Write-in voting within the complete ballot-access system'),('state/STANDARDS_AND_TESTS.md','Private parade composition and compelled messages')]
public=section('terms/OT1996/output/OT_1996CHUNK7.md','Timmons v. Twin Cities Area New Party, No. 95-1608') if False else ''
text=(root/'terms/OT1996/output/OT_1996CHUNK7.md').read_text(encoding='utf-8')
start=text.index('### Timmons'); end=text.find('\n### ',start+5)
case=text[start:end if end!=-1 else len(text)]
start=case.index('#### Separate Positions Relevant to the Decision')
end=case.index('Stone-Zsela dissents.',start)
public='## Prior public noncontrolling positions: Timmons\n\nSource: `terms/OT1996/output/OT_1996CHUNK7.md`; exact public separate-position paragraphs for Stevens/Ginsburg/Souter, copied without private material.\n\n'+case[start:end].strip()
write('JONES',jones,public)
write('MOBIL',[('state/holdings/business-and-commercial-law.md','United States v. Winstar Corp., 518 U.S. 839 (1996)'),('state/STANDARDS_AND_TESTS.md','Actual federal contractual undertakings and allocated regulatory risk')])
write('HENEREY',[('state/holdings/first-amendment.md','Settle v. Dickson County School Board'),('state/holdings/first-amendment.md','Boring v. Buncombe County Board of Education'),('state/STANDARDS_AND_TESTS.md','Assigned school productions and teachers’ personal speech')])
write('ALASKA',[('state/holdings/property-and-economic-rights.md','United States v. Alaska'),('state/STANDARDS_AND_TESTS.md','Ordinary high-water emergence for natural island status'),('state/STANDARDS_AND_TESTS.md','Coordinate fixation of state-federal submerged-land boundaries')])
# Current-term Santa Fe is a scoped neutral-projection authority, effective June 19.
text=(root/'terms/OT1999/workspace/neutral-projection.md').read_text(encoding='utf-8')
needle='### Santa Fe Independent School District v. Doe — 2000-06-19'
start=text.index(needle); end=text.find('\n### ',start+len(needle))
with (out/'OT_1999CHUNK9_HENEREY.md').open('a',encoding='utf-8') as f:
    f.write('\n## Current-term addition\n\nSource: `terms/OT1999/workspace/neutral-projection.md`; Santa Fe controlling-law block only.\n\n'+text[start:end].strip()+'\n')
print('Focused slices created.')
