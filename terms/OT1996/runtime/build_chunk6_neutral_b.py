"""Reproducible narrow source copies for neutral preflight; no adjudication."""
from pathlib import Path
import hashlib
import importlib.util
import re
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[3]
spec = importlib.util.spec_from_file_location('entering_copy', ROOT / 'tools/build_entering_law.py')
copy = importlib.util.module_from_spec(spec)
spec.loader.exec_module(copy)
CASES = {
66: ('Young v. Fordice','1997-03-31', [
 ('election-law', 'Voting Rights Coalition v. Wilson, judgment below 60 F.3d 1411'),
 ('election-law', 'Morse v. Republican Party of Virginia, 517 U.S. 186'),
 ('civil-rights', 'Presley v. Etowah County Commission; Mack v. Russell County Commission, 502 U.S. 491 (1992)')],
 ['Voting Rights Act §5 coverage of reallocations of governing authority', 'Voting Rights Act preclearance of primary-like party participation fees', 'The designated channel for preclearance review', 'Federal election registration duties through state agencies'], ['Lopez v. Monterey County']),
67: ('Opuku-Boateng v. California','1997-04-07', [
 ('labor-and-employment','Beadle v. City of Tampa, judgment below 42 F.3d 633')],
 ['Religious accommodation and demonstrated operational hardship'], ['Brown v. Polk County']),
68: ('In re Vey','1997-04-14', [
 ('federal-courts','Zatko v. California, 502 U.S. 16 (1991)'),
 ('federal-courts','Denton v. Hernandez, 504 U.S. 25 (1992)'),
 ('federal-courts','Martin v. District of Columbia Court of Appeals and Martin v. McDermott, 506 U.S. 1 (1992)'),
 ('federal-courts','Day v. Day, 510 U.S. 1'),
 ('federal-courts','In re Sassower, 510 U.S. 4'),
 ('federal-courts','In re Anderson, 511 U.S. 364'),
 ('federal-courts','Jones v. ABC-TV, 516 U.S. 363'),
 ('federal-courts','Shieh v. Kakita; Shieh v. United States Court of Appeals for the Ninth Circuit; Shieh v. Krieger, 517 U.S. 343'),
 ('federal-courts','Felker v. Turpin, 518 U.S. 651 (1996)')],
 ['Factual frivolousness and review of fee-screening dismissals','Supreme Court original habeas after an authorization-review bar'], ['In re Maria Luisa Costell Gaydos']),
69: ('Chandler v. Miller','1997-04-15', [
 ('criminal-procedure','Vernonia School District 47J v. Acton')],
 ['Limited drug testing of interscholastic athletes'], []),
70: ('Blessing v. Freestone','1997-04-21', [
 ('civil-rights','Suter v. Artist M., 503 U.S. 347 (1992)'),
 ('civil-rights','Livadas v. Bradshaw, 512 U.S. 107')],
 ['Private enforcement of Adoption Assistance Act reasonable-efforts and reporting clauses','Equal state enforcement for employees who collectively bargain'], []),
71: ('New Mexico Department of Human Services v. Joseph A. and Josephine A.','1997-04-21', [
 ('federal-courts','Rufo v. Inmates of Suffolk County Jail; Rapone v. Inmates of Suffolk County Jail, 502 U.S. 367 (1992)'),
 ('civil-rights','Freeman v. Pitts, 503 U.S. 467 (1992)'),
 ('civil-rights','Missouri v. Jenkins')],
 ['Modification of institutional consent decrees','Partial withdrawal of school-desegregation supervision'], [])
}

projection_path = ROOT / 'terms/OT1996/workspace/neutral-projection.md'
projection = projection_path.read_text(encoding='utf-8')
projection_parts = {}
for title in ['Current Court law in effective order','Material published noncontrolling positions','Public procedure after completed actions']:
    projection_parts[title] = copy.take_heading(projection, title)
source_rows = []
prior_public = {
 69: [('terms/OT1994/output/OT_1994CHUNK8.md','Vernonia School District 47J v. Acton, No. 94-590')],
 70: [('terms/OT1991/output/OT_1991CHUNK9.md','Suter v. Artist M., No. 90-1488')],
 71: [('terms/OT1991/output/OT_1991CHUNK4.md','Rufo v. Inmates of Suffolk County Jail; Rapone v. Inmates of Suffolk County Jail, Nos. 90-954 and 90-1004'),('terms/OT1994/output/OT_1994CHUNK7.md','Missouri v. Jenkins, No. 93-1823')]
}
for n, (name, date, holdings, standards, current) in CASES.items():
    out = ROOT / f'terms/OT1996/entering-law/OT_1996CHUNK6_{n}_ENTERING_LAW.md'
    cmd = [sys.executable,'-B',str(ROOT/'tools/build_entering_law.py'),str(out),'--standing-heading','1. Current Court']
    for heading in standards:
        cmd += ['--standard-heading',heading]
    subprocess.run(cmd, check=True)
    contents = out.read_text(encoding='utf-8')
    contents = contents.replace('# Entering-Law Reading Slice', f'# {n}. {name} — Entering-Law Reading Slice', 1)
    contents += f'\n## Cutoff and use\n\nEvent date: {date}. These selections copy the term-opening authority and relevant completed current-term public law. Later chunk-6 events are not authority. Refresh any materially affected selection after earlier-effective chunk-6 adjudications; uncoordinated same-day events share their entering baseline.\n'
    for slug, heading in holdings:
        src = ROOT / f'state/holdings/{slug}.md'
        section = copy.take_heading(src.read_text(encoding='utf-8'),heading)
        contents += f'\n## Verbatim Holdings selection\n\nSource: `state/holdings/{slug}.md`, exact heading `{heading}`.\n\n{section}\n'
        source_rows.append((n,src.relative_to(ROOT).as_posix(),heading,hashlib.sha256(section.encode()).hexdigest()))
    for query in current:
        for title, part in projection_parts.items():
            matches = re.findall(r'^### (.+)$', part, re.M)
            matches = [h for h in matches if query in h]
            if not matches:
                continue
            if len(matches) != 1:
                raise ValueError((query,title,matches))
            section = copy.take_heading(part,matches[0])
            if matches[0][:10] >= date:
                raise ValueError('Non-earlier authority selected')
            contents += f'\n## Verbatim current-term selection — {title}\n\nSource: `terms/OT1996/workspace/neutral-projection.md`, section `{title}`, exact heading `{matches[0]}`. The embedded Record link is provenance only; neutral/model contexts do not open it.\n\n{section}\n'
            source_rows.append((n,projection_path.relative_to(ROOT).as_posix(),title+' / '+matches[0],hashlib.sha256(section.encode()).hexdigest()))
    for path, heading in prior_public.get(n, []):
        event = copy.take_heading((ROOT/path).read_text(encoding='utf-8'),heading)
        if heading.startswith('Rufo '):
            section = next(p for p in event.split('\n\n') if p.startswith("O'Connor concurs only in the judgment."))
        else:
            section = copy.take_heading(event, 'Separate Positions Relevant to the Decision')
        contents += f'\n## Verbatim earlier public positions\n\nSource: `{path}`, case `{heading}`; published separate positions only, not controlling Court law.\n\n{section}\n'
        source_rows.append((n,path,heading+' / Separate Positions Relevant to the Decision',hashlib.sha256(section.encode()).hexdigest()))
    if n == 70:
        for name in ['1320a2_1996','1320a10_1996']:
            src = ROOT/f'terms/OT1996/sources/chunk6-neutral-b/{name}.txt'
            section = src.read_text(encoding='utf-8')
            contents += f'\n## Official pre-event statutory text\n\nSource: `{src.relative_to(ROOT).as_posix()}`; exact retrieval URL in `sources/chunk6-neutral-b/RETRIEVAL.md`. The GovInfo historical taxonomy is a navigation artifact.\n\n{section}\n'
            source_rows.append((n,src.relative_to(ROOT).as_posix(),'complete text',hashlib.sha256(section.encode()).hexdigest()))
        src = ROOT/'terms/OT1996/sources/chunk6-neutral-b/654_1996.txt'
        original = src.read_text(encoding='utf-8')
        section = original.split('Effective Date of 1996 Amendment',1)[1].split('Effective Date of 1988 Amendment',1)[0]
        contents += '\n## Exact 1996 statutory effective-date selection\n\nSource: `terms/OT1996/sources/chunk6-neutral-b/654_1996.txt`, Effective Date of 1996 Amendment. The selection does not establish any unproved Arizona implementation event.\n\n'+section+'\n'
        source_rows.append((n,src.relative_to(ROOT).as_posix(),'Effective Date of 1996 Amendment',hashlib.sha256(section.encode()).hexdigest()))
    out.write_text(contents,encoding='utf-8')
    print(n, len(contents), 'characters')
map_path = ROOT/'terms/OT1996/freeze/OT_1996CHUNK6_NEUTRAL_B_SOURCE_MAP.md'
lines = ['# OT1996 chunk 6 — Neutral B source-copy map','', 'Prepared without private positions, commitments, reconciliation, raw Records, or a version-control command. The six slices were seeded by `tools/build_entering_law.py`; Holdings and current-term excerpts are exact scripted section copies, not paraphrases. SHA-256 below covers normalized copied section text.','', '| Matter | Source | Exact section | Copied-section SHA-256 |','|---|---|---|---|']
for n,path,heading,digest in source_rows:
    lines.append(f'| {n} | `{path}` | {heading} | `{digest}` |')
lines += ['','Standards and Tests and Standing State selections appear verbatim in each generated slice. Their exact source headings are in the slice. Current projection cutoff was March 19, 1997; each selected decision predates the destination event.','']
map_path.write_text('\n'.join(lines),encoding='utf-8')
