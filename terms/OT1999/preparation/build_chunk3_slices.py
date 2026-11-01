from pathlib import Path
import importlib.util
import subprocess
import sys

sys.dont_write_bytecode = True
root = Path(__file__).resolve().parents[3]
spec = importlib.util.spec_from_file_location('slice_tool', root/'tools/build_entering_law.py')
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)
outdir = root/'terms/OT1999/entering-law'
groups = {
 'EARLY': {
  'standards': ['Scientific expert evidence under original Rules 104(a) and 702', 'Operational assets and the unitary-business limitation on apportioned income', 'Notice-date selection of the Tax Court refund lookback', 'Tax-refund filing and payment limits do not permit incapacity tolling', 'Civil RICO limitation, new injury and concealed discovery', 'Territorial racial design and independently cognizable injury', 'Common substantial-justification standard for governmental racial classifications', 'Appeal-warning omissions and causal loss on §2255 review'],
  'holdings': {'federal-courts':['Daubert v.', 'General Electric Co. v. Joiner', 'Kumho Tire Co. v. Carmichael'], 'constitutional-structure':['Allied-Signal, Inc.'], 'federal-taxation':['Commissioner v. Lundy','United States v. Brockamp'], 'business-and-commercial-law':['Klehr v.'], 'civil-rights':['Adarand Constructors, Inc. v. Peña','Hopwood v. Texas'], 'election-law':['Shaw v. Reno'], 'criminal-procedure':['Peguero v. United States']}
 },
 'LATER': {
  'standards':['Rational-basis review of ordinary economic classifications','Equal protection of commitment proof and family participation','Private religious viewpoints in public forums and printing benefits','Religious targeting, comparable secular conduct and strict scrutiny','Parental educational choice and genuine public-school instruction','Mine Act channeling and meaningful judicial review','Review of Medicare reimbursement reopening refusals','Occupational-safety supplementation without an approved state plan','Supported categorical exclusion of polygraph credibility evidence','Preserved protected-silence and personal-intent errors on federal habeas review','Temporal reach of ordinary AEDPA habeas amendments'],
  'holdings':{'civil-rights':['FCC v. Beach Communications','Heller v. Doe','Romer v. Evans'], 'first-amendment':['Rosenberger v.','Agostini v.'], 'federal-courts':['Zobrest v.','Your Home Visiting Nurse Services','Lindh v. Murphy'], 'administrative-law':['Thunder Basin Coal Co.'], 'constitutional-structure':['Gade v.','Freightliner Corp. v. Myrick'], 'criminal-procedure':['Brecht v. Abrahamson','United States v. Scheffer']}
 }
}
for group, selection in groups.items():
 output = outdir/f'OT_1999CHUNK3_{group}.md'
 cmd=[sys.executable,'-B',str(root/'tools/build_entering_law.py'),str(output),'--root',str(root)]
 for h in selection['standards']: cmd += ['--standard-heading',h]
 for h in ['1. Current Court','2. Current Circuit Allotments']: cmd += ['--standing-heading',h]
 subprocess.run(cmd,check=True)
 with output.open('a',encoding='utf-8') as f:
  for slug,queries in selection['holdings'].items():
   text=(root/f'state/holdings/{slug}.md').read_text(encoding='utf-8')
   for query in queries:
    f.write(f'\n## Authority copied from state/holdings/{slug}.md\n\n')
    f.write(mod.take_heading(text,query)+'\n')
  f.write('\n## Effective current-term supplement\n\nRead the frozen chunk-entry neutral projection alongside this slice. Its current-law and published-position fields incorporate all effective current-term Records through February 14, 2000. Same-day events retain a common legal baseline; alphabetical order controls assignment counts only. The source Records remain authoritative.\n')
 print(group,output.stat().st_size)
