"""Build bounded, verbatim public entering-law readings for McConnell."""
from pathlib import Path
import importlib.util
import subprocess
import sys
import re

ROOT = Path(__file__).resolve().parents[3]
spec = importlib.util.spec_from_file_location('entering_builder', ROOT / 'tools/build_entering_law.py')
builder = importlib.util.module_from_spec(spec)
spec.loader.exec_module(builder)

standards = [
 'Concrete personal interests and procedural citizen-suit standing',
 'Individual legislator standing for institutional dilution',
 'Present civil obligations and pre-enforcement ripeness',
 'Permissive FEC advisory opinions before pre-enforcement review',
 'Anonymous individual political leaflets',
 'Intermediary contribution limits and meaningful association',
 'Nonprofit political spending outside a literal safe harbor',
 'Independent political-party campaign expression and candidate connections',
 'Candidate financing, political-committee thresholds and membership exclusions',
 'Candidate inquiries and independently edited voter guides',
 'Express advocacy through limited context under §100.22(b)',
 'Candidate contribution limits and anticorruption fit',
 'Issue advocacy and definite campaign-finance coverage',
 'Bounded responsive grants within a voluntary public-financing option',
 'Truthful source attribution in candidate contributions',
]
holdings = [
 ('federal-courts-justiciability','Lujan v. Defenders of Wildlife, 504 U.S. 555 (1992)'),
 ('federal-courts-justiciability','Raines v. Byrd'),
 ('federal-courts-justiciability','National Park Hospitality Association v. Department of the Interior, 538 U.S. 803'),
 ('first-amendment','Day v. Holahan'),
 ('first-amendment','Colorado Republican Federal Campaign Committee v. Federal Election Commission, 518 U.S. 604 (1996)'),
 ('election-law','Akins v. FEC'),
 ('election-law','Federal Election Commission v. Maine Right to Life Committee, Inc.'),
 ('election-law','Kentucky Right to Life, Inc. v. Stengel'),
 ('election-law','Clifton v. Federal Election Commission'),
 ('election-law','Russell v. Burris'),
 ('election-law','Nixon v. Shrink Missouri Government PAC, 528 U.S. 377 (2000)'),
 ('election-law','North Carolina Right to Life, Inc. v. Bartlett'),
 ('federal-courts-justiciability','North Carolina Right to Life, Inc. v. Bartlett'),
 ('election-law','Daggett v. Commission on Governmental Ethics & Election Practices'),
 ('election-law','Mariani v. United States'),
 ('election-law','FEC v. Colorado Republican Federal Campaign Committee'),
 ('election-law','Missouri Republican Party v. Lamb'),
 ('election-law','Federal Election Commission v. Beaumont, 539 U.S. 146'),
]
public_names = ['Day v. Holahan','Colorado Republican','Shrink Missouri','Mariani v.','Clifton v.',
 'Daggett v.','Beaumont','Stengel','Missouri Republican Party v. Lamb','North Carolina Right to Life, Inc. v. Bartlett',
 'Russell v. Burris','Maine Right to Life Committee']
output = ROOT / 'terms/OT2003/entering-law/OT_2003CHUNK2_C.md'
args = [sys.executable,'-B',str(ROOT/'tools/build_entering_law.py'),str(output)]
for title in standards: args.extend(['--standard-heading', title])
args.extend(['--standing-heading','1. Current Court'])
subprocess.run(args,cwd=ROOT,check=True,capture_output=True,text=True)
parts=[output.read_text(encoding='utf-8')]
for volume,title in holdings:
 source='state/holdings/'+volume+'.md'
 parts.extend(['\n## Verbatim Holdings selection\n\nSource: `'+source+'`; heading: '+title+'\n',builder.take_heading((ROOT/source).read_text(encoding='utf-8'),title)])
for year in range(1991,2003):
 for path in sorted((ROOT/('terms/OT'+str(year)+'/output')).glob('*.md')):
  text=path.read_text(encoding='utf-8')
  titles=[re.sub(r'^#{2,3}\s+','',line) for line in text.splitlines() if re.match(r'^#{2,3} ',line) and any(n in line for n in public_names)]
  for title in titles:
   case=builder.take_heading(text,title)
   parts.append('\n## Prior public Justice positions\n\nSource: `'+path.relative_to(ROOT).as_posix()+'`; case: '+title+'\n')
   for section in ['Judgment & Remedy','Opinion Topology','Separate Writings','Selected Separate Positions','Selected Separate Writings','Separate Positions Relevant to the Decision']:
    try:copied=builder.take_heading(case,section)
    except ValueError:continue
    parts.append(copied)
output.write_text('\n\n'.join(parts).rstrip()+'\n',encoding='utf-8')
print(output.relative_to(ROOT).as_posix(),len(output.read_text(encoding='utf-8').split()),'words')
