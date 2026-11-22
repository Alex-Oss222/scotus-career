from pathlib import Path
import hashlib
import re
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[3]
TERM = ROOT / 'terms/OT2003'
BASE = TERM / 'entering-law'
FREEZE = TERM / 'freeze'
BASE.mkdir(exist_ok=True)
FREEZE.mkdir(exist_ok=True)

def section(path, query, level=None):
    lines = path.read_text(encoding='utf-8-sig').splitlines()
    hits = []
    for i, line in enumerate(lines):
        m = re.match(r'^(#{1,5}) (.*)$', line)
        if m and (level is None or len(m[1]) == level) and query in m[2]:
            hits.append((i, len(m[1])))
    if len(hits) != 1:
        raise ValueError((str(path), query, hits))
    start, depth = hits[0]
    end = next((i for i in range(start + 1, len(lines))
                if re.match(r'^#{1,' + str(depth) + r'} ', lines[i])), len(lines))
    return '\n'.join(lines[start:end]).rstrip()

cases = {
72: dict(name='Jones', standards=['Statutory temporal reach and new consequences for completed conduct', 'The 1991 Civil Rights Act'], holdings=[('civil-rights','Rivers v.'), ('civil-rights','Landgraf v.'), ('federal-courts','Landgraf v.')], current=[], statutes=['28_1658_2000.txt','42_1981_2000.txt']),
73: dict(name='Dretke', standards=['Capital eligibility innocence as a gateway','Crime innocence as a gateway','Defaulted ineffective assistance offered as cause','State-court merits decisions and factual development','Sequencing nonretroactivity and procedural default','Renewed proof of noncapital recidivist status'], holdings=[('federal-courts-habeas','Sawyer v.'),('federal-courts-habeas','Schlup v.'),('federal-courts-habeas','Edwards v.'),('federal-courts-habeas','Williams v. Taylor (Terry'),('federal-courts-habeas','Bell v. Cone'),('criminal-procedure','Trest v.'),('criminal-procedure-sentencing-and-capital','Lambrix v.'),('criminal-procedure','Monge v.')], current=['Banks v. Dretke','Baldwin v. Reese'], statutes=[]),
74: dict(name='Scarborough', standards=['Verification cure for timely administrative discrimination charges','An appellate brief functioning as a notice of appeal','Social Security remand judgments and EAJA fees','Administrative EAJA coverage of deportation hearings'], holdings=[('federal-courts','Becker v.'),('labor-and-employment','Edelman v.'),('administrative-law','Ardestani v.'),('federal-courts-immunities-and-remedies','Shalala v. Schaefer')], current=['Kontrick v. Ryan'], statutes=['28_2412_2000.txt']),
75: dict(name='Johnson', standards=['State final-judgment rules and federal qualified immunity','Presented questions, subsidiary arguments and exceptional Supreme Court review'], holdings=[('federal-courts','Florida v. Thomas'),('federal-courts','Jefferson v. City of Tarrant')], current=[], statutes=[]),
76: dict(name='Middleton', standards=['State-court merits decisions and factual development'], holdings=[('criminal-procedure','Estelle v.'),('federal-courts-habeas','Williams v. Taylor (Terry'),('federal-courts-habeas','Woodford v. Visciotti'),('federal-courts-habeas','Lockyer v. Andrade'),('federal-courts-habeas','Early v. Packer'),('federal-courts-habeas','Bell v. Cone'),('criminal-procedure','Brecht v.')], current=['Yarborough v. Gentry','Mitchell v. Esparza'], statutes=[]),
77: dict(name='Nippon_Steel', standards=['Delegated Customs interpretation and independent tariff review','Whole-record agency review under the announced substantive standard','Remand for an initial determination assigned to an agency','Persuasive weight of a nonbinding agency advisory interpretation'], holdings=[('administrative-law','United States v. Haggar'),('administrative-law','United States v. Mead'),('administrative-law','INS v. Ventura'),('labor-and-employment','Allentown Mack'),('administrative-law','Christensen v.')], current=['Alaska Department of Environmental Conservation v. EPA','California ex rel. Lockyer v. FERC','Household Credit Services, Inc. v. Pfennig'], statutes=['19_1677e_2000.txt','19_1677m_2000.txt']),
}

projection = TERM / 'workspace/neutral-projection.md'
for number, cfg in cases.items():
    target = BASE / f'OT_2003CHUNK6_CASE{number}_{cfg["name"]}.md'
    command = [sys.executable, '-B', str(ROOT / 'tools/build_entering_law.py'), str(target), '--standing-heading', '1. Current Court']
    for heading in cfg['standards']:
        command.extend(['--standard-heading', heading])
    subprocess.run(command, cwd=ROOT, check=True)
    additions = ['\n## Scoped preparation and date limit\n',
        f'Inventory case {number}. Effective event date: ' + ('2004-05-10' if number == 77 else '2004-05-03') + '. Only completed authority effective before this date enters. Uncoordinated May 3 matters share the same pre-date baseline. A later-completed authority requires an affected-law refresh before dependent assembly. These selections do not model a vote.\n']
    for volume, query in cfg['holdings']:
        path = ROOT / 'state/holdings' / (volume + '.md')
        additions.extend([f'## Canonical Holdings selection from {path.relative_to(ROOT).as_posix()}\n',section(path, query, 4)+'\n'])
    for query in cfg['current']:
        public = section(projection, query, 3)
        additions.extend(['## Effective current-term public projection\n', public+'\n'])
        links = re.findall(r'\]\((\.\./runtime/[^)]+)\)', public)
        for link in links:
            path = (projection.parent / link).resolve()
            payload = path.read_text(encoding='utf-8-sig')
            additions.extend([f'## Complete linked public-only handoff: {path.relative_to(ROOT).as_posix()}\n', payload.rstrip()+'\n'])
    for name in cfg['statutes']:
        path = TERM / 'runtime/chunk6-neutral-sources' / name
        payload = path.read_text(encoding='utf-8')
        additions.extend([f'## Official statutory reading copy: {name}\n',payload.rstrip()+'\n'])
    target.write_text(target.read_text(encoding='utf-8')+'\n'.join(additions),encoding='utf-8')
    print(number, len(target.read_bytes()), hashlib.sha256(target.read_bytes()).hexdigest())

source = TERM / 'runtime/OT_2003CHUNK6_NEUTRAL.md'
text = source.read_text(encoding='utf-8-sig')
selected = text[:text.index('## 78. ')].rstrip()+'\n'
(FREEZE / 'OT_2003CHUNK6_A_NEUTRAL.md').write_text(selected,encoding='utf-8')
