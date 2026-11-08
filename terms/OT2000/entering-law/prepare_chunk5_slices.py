from pathlib import Path
import re
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / 'tools'))
from build_entering_law import take_heading

BASE = ROOT / 'terms/OT2000'
OUT = BASE / 'entering-law'
NEUTRAL = (BASE / 'runtime/OT_2000CHUNK5_NEUTRAL.md').read_text(encoding='utf-8')
PROJECTION = (BASE / 'workspace/neutral-projection.md').read_text(encoding='utf-8')

def safe_write(path, text):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.rstrip() + '\n', encoding='utf-8')

def all_sections(text, query):
    lines = text.splitlines()
    found = []
    for i, line in enumerate(lines):
        if not re.match(r'^#{2,5} ', line) or query not in line:
            continue
        level = len(line) - len(line.lstrip('#'))
        end = len(lines)
        for j in range(i+1,len(lines)):
            m = re.match(r'^(#{1,5}) ', lines[j])
            if m and len(m[1]) <= level:
                end = j
                break
        found.append('\n'.join(lines[i:end]).strip())
    if not found:
        raise ValueError(query)
    return found

def build(slug, title, standards, holdings, outputs, current):
    dest = OUT / ('OT_2000CHUNK5_' + slug + '.md')
    cmd = [sys.executable, str(ROOT/'tools/build_entering_law.py'), str(dest)]
    for h in standards:
        cmd += ['--standard-heading',h]
    subprocess.run(cmd, cwd=ROOT, check=True, capture_output=True)
    text = dest.read_text(encoding='utf-8')
    text += '\n## Matter and effective-law boundary\n\n' + title + '\n\n'
    text += 'Opening law is processed through June 29, 2000. The copied current-term sections below supply later effective law and published positions. A same-date processing order alone creates no substantive precedent. No current-matter outcome is supplied.\n'
    for volume, query in holdings:
        src = 'state/holdings/' + volume + '.md'
        text += '\n## Opening authority: ' + query + '\n\nSource: `' + src + '`.\n\n'
        text += take_heading((ROOT/src).read_text(encoding='utf-8'),query) + '\n'
    for src,query in outputs:
        text += '\n## Earlier published decision: ' + query + '\n\nSource: `' + src + '`.\n\n'
        text += take_heading((ROOT/src).read_text(encoding='utf-8'),query) + '\n'
    for query in current:
        text += '\n## Current-term public authority: ' + query + '\n\nSource: `terms/OT2000/workspace/neutral-projection.md`. Each matching law and published-position section is copied below.\n\n'
        text += '\n\n'.join(all_sections(PROJECTION,query)) + '\n'
    safe_write(dest,text)
    print(dest.name, len(text.split()), 'words')

def freeze_group(slug,names):
    chunks = re.split(r'(?m)(?=^# (?!SECTION|OT_))',NEUTRAL)[1:]
    selected = [c for c in chunks if c.splitlines()[0][2:] in names]
    assert len(selected)==len(names)
    dest=BASE/'freeze'/('OT_2000CHUNK5_NEUTRAL_'+slug+'.md')
    safe_write(dest,'# OT_2000CHUNK5 — '+slug+' neutral selection\n\n'+'\n'.join(selected))
    print(dest.name)

if __name__=='__main__':
    build('SANDOVAL','Alexander v. Sandoval; decision April 24, 2001.',
      ['Private enforcement of Title VI disparate-impact regulations'],
      [('business-and-commercial-law','Central Bank of Denver, N.A. v. First Interstate Bank of Denver, N.A., 511 U.S. 164'),('civil-rights','Franklin v. Gwinnett County Public Schools, 503 U.S. 60 (1992)'),('civil-rights','Blessing v. Freestone')],
      [('terms/OT1999/output/OT_1999CHUNK4.md','Powell v. Ridge'),('terms/OT1998/output/OT_1998CHUNK3.md','McClellan v. Cablevision')],[])
    build('ATWATER','Atwater v. City of Lago Vista; decision April 24, 2001; conduct March 1997.',
      ['Additional station-house custody for a civil licensing offense','Traffic citations and the custodial-arrest search exception','Objective probable cause for an ordinary initial traffic stop'],
      [('criminal-procedure','Knowles v. Iowa, 525 U.S. 113'),('criminal-procedure','Whren v. United States, 517 U.S. 806'),('criminal-procedure','Wilson v. Arkansas'),('civil-rights','Wilson v. Layne')],
      [('terms/OT1997/output/OT_1997CHUNK7.md','Ricci v. Village')],['Illinois v. McArthur — 2001-02-20','Wallis v. Spencer — 2001-04-02'])
    build('STERLING','Sterling v. Borough of Minersville; decision April 24, 2001; conduct April 17, 1997.',
      ['Official dissemination of intimate marital and family information','Qualified-immunity legal appeals and factual sufficiency','Relevant precedent in appellate qualified-immunity review'],
      [('civil-rights','Doe v. Southeastern Pennsylvania Transportation Authority'),('civil-rights','Shahar v. Bowers'),('federal-courts','Johnson v. Jones'),('federal-courts','Behrens v. Pelletier, 516 U.S. 299'),('civil-rights','Hunter v. Bryant, 502 U.S. 224 (1991)'),('civil-rights','Elder v. Holloway, 510 U.S. 510'),('civil-rights','Wilson v. Layne')],
      [('terms/OT1995/output/OT_1995CHUNK6.md','Sheets v. Salt Lake')],['Denius v. Dunlap — 2001-01-17'])
    for slug,title in [('DANIELS','Daniels v. United States'),('COSS','Lackawanna County District Attorney v. Coss')]:
      build(slug,title+'; decision April 25, 2001. Coordinate with the companion on the common pre-date baseline unless an express effective sequence is established. Coss filed federal habeas in September 1994; its former chapter 153 rules remain distinct from Daniels section 2255 procedure.',
        ['Collateral attacks on ACCA predicates at federal sentencing','Habeas custody in a continuous consecutive sentence series','Collateral regularity of prior counseled pleas used for enhancement'],
        [('federal-courts','Garlotte v. Fordice'),('criminal-procedure','Parke v. Raley, 506 U.S. 20 (1992)'),('criminal-procedure','Nichols v. United States, 511 U.S. 738'),('criminal-procedure','Almendarez-Torres v. United States')],
        [('terms/OT1993/output/OT_1993CHUNK5.md','Custis v. United States')],['Fiore v. White — 2001-01-09','Glover v. United States — 2001-01-09'])
    build('RANDELL','Randell v. Johnson; decision April 25, 2001. Daniels and Coss are same-date matters, not entering precedent absent an express substantive sequence.',
      ['Conviction-negating damages claims and favorable invalidation','Expired parole-revocation sentences and continuing habeas injury','Dismissal and counsel requests under amended §1915'],[],
      [('terms/OT1993/output/OT_1993CHUNK7.md','Heck v. Humphrey'),('terms/OT1997/output/OT_1997CHUNK4.md','Spencer v. Kemna')],[])
    freeze_group('APR24_25',['Alexander v. Sandoval','Atwater v. City of Lago Vista','Sterling v. Borough of Minersville','Daniels v. United States','Lackawanna County District Attorney v. Coss','Randell v. Johnson'])
