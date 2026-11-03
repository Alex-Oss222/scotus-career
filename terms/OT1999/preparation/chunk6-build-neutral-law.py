"""Operator-selected verbatim law copies; selections are legal judgments, copying is mechanical."""
import importlib.util
import subprocess
import sys
from pathlib import Path

root=Path('.')
spec=importlib.util.spec_from_file_location('slicer',root/'tools/build_entering_law.py')
module=importlib.util.module_from_spec(spec); spec.loader.exec_module(module)
configs={
 'ncrl': {
  'date':'2000-05-01',
  'standards':['Candidate financing, political-committee thresholds and membership exclusions','Express advocacy through limited context under §100.22(b)','Nonprofit political spending outside a literal safe harbor','Anonymous individual political leaflets','Intermediary contribution limits and meaningful association','Candidate contribution limits and anticorruption fit'],
  'holdings':{'election-law':['Political-committee coverage and membership communications','Contextual express advocacy and statutory limits','Independent voter guides and candidate inquiries'],'first-amendment':['Campaign financing, intermediary contributions and nonprofit advocacy','Anonymous individual political leaflets']},
  'paragraphs':['**Nixon v. Shrink Missouri Government PAC — January 24, 2000','**Kennedy, Shrink dissent']
 },
 'mining': {
  'date':'2000-05-08',
  'standards':['Statutory temporal reach and new consequences for completed conduct','APA persuasion burdens and statutory departures','Controlling weight for a responsible agency\'s fair regulatory interpretation','Whole-record agency review under the announced substantive standard'],
  'holdings':{'civil-rights':['Civil statutory temporal reach'],'administrative-law':['Agency interpretation, policy change and antecedent transactions','Interpretation of agency regulations','Administrative burdens of persuasion']},
  'sections':['FDA v. Brown & Williamson Tobacco Corp. — 2000-03-21','Christensen v. Harris County — 2000-05-01']
 },
 'saenz': {
  'date':'2000-05-09',
  'standards':['Voluntary public employment and substantive workplace safety duties','Police restraint and involuntary transfer into known danger','Relevant precedent in appellate qualified-immunity review'],
  'holdings':{'civil-rights':['Affirmative danger and conduct-time qualified immunity','Knowing dangerous restraint and arbitrary selective enforcement','Substantive due process in rapid police pursuits','Municipal liability and public employment','Qualified immunity']},
  'sections':['Doe v. Rosenberg — 2000-04-24']
 },
 'mciver': {
  'date':'2000-05-15',
  'standards':['Possessory seizures and the claimant\'s own Fourth Amendment interest','Targeted thermal examination of concealed home activity','Privacy in a rented vehicle and personal luggage','Nonassisting media observers during a home search'],
  'holdings':{'criminal-procedure':['Automobile searches']},
  'sections':['Bond v. United States — 2000-04-17']
 },
 'carmell': {
  'date':'2000-05-01',
  'standards':['Retrospective withdrawal of mandatory parole reconsideration'],
  'holdings':{'criminal-procedure':['Retrospective loss of parole consideration']},
  'sections':['Garner v. Jones — 2000-03-28']
 },
 'fischer': {
  'date':'2000-05-15',
  'standards':['Federal-program bribery without traced federal-funds effect','Medicare corrective adjustments and permissible interpretive change','Lawful historical Medicare costs in later reimbursement formulas'],
  'holdings':{'criminal-procedure':['Federal bribery and RICO conspiracy elements']}
 },
 'morrison': {
  'date':'2000-05-15',
  'standards':['Commerce connection, mechanism, and class-wide effects','Congruent and proportional Fourteenth Amendment enforcement'],
  'holdings':{'constitutional-structure':['Commerce power and school-zone firearm possession','Commerce power and clinic access','Commerce power and business robbery','Commerce authority over service-directed force','Commerce authority over intrastate endangered-species takings','Fourteenth Amendment enforcement power']},
  'paragraphs':['**Reno v. Condon — January 12, 2000','- **Kimel / United States v. Florida Board of Regents — January 11, 2000'],
  'sections':['Gillespie v. City of Indianapolis — 2000-04-17']
 },
 'johnson': {
  'date':'2000-05-15',
  'standards':['Former drug-possession probation revocation and the imprisonment range','Retrospective withdrawal of mandatory parole reconsideration','Statutory temporal reach and new consequences for completed conduct'],
  'holdings':{'criminal-procedure':['Probation revocation and lenity','Conditional community release and revocation']},
  'sections':['Garner v. Jones — 2000-03-28']
 },
 'public_lands': {
  'date':'2000-05-15',
  'standards':['Statutory temporal reach and new consequences for completed conduct','An agency interpretation necessarily embodied in its decision','Whole-record agency review under the announced substantive standard'],
  'holdings':{'administrative-law':['Agency interpretation, policy change and antecedent transactions']},
  'sections':['FDA v. Brown & Williamson Tobacco Corp. — 2000-03-21','Christensen v. Harris County — 2000-05-01']
 },
 'geier': {
  'date':'2000-05-22',
  'standards':['Motor-vehicle standards and independent actual conflict','Cigarette-labeling preemption by statutory period and predicate duty'],
  'holdings':{'constitutional-structure':['Motor-vehicle safety and common-law preemption']},
  'sections':['Norfolk Southern Railway Co. v. Shanklin — 2000-04-17','United States v. Locke / Intertanko v. Locke — 2000-03-06']
 },
 'jones': {
  'date':'2000-05-22',
  'standards':['Property-function connection under the federal arson statute','Commerce connection, mechanism, and class-wide effects'],
  'holdings':{'criminal-procedure':['Federal arson and the property-use element'],'constitutional-structure':['Commerce power and school-zone firearm possession','Commerce power and business robbery']},
  'paragraphs':['**Reno v. Condon — January 12, 2000'],
  'sections':['Gillespie v. City of Indianapolis — 2000-04-17']
 },
 'playboy': {
  'date':'2000-05-22',
  'standards':['Content-selected restrictions on protected broadcast indecency','Cable access permissions and the invalid compulsory segregation system','Cable-channel blocking duties under the 1996 Act','Adult access and content-based criminal network-speech restrictions','Cable-carriage rules and review of legislative predictions'],
  'holdings':{'first-amendment':['Indecent broadcasting and adult access','Cable access and protected indecency','Internet content restrictions']},
  'sections':["City of Erie v. Pap's A.M. — 2000-03-29"]
 }
}
neutral=(root/'terms/OT1999/workspace/neutral-projection.md').read_text(encoding='utf-8')
for case in sys.argv[1:] or configs:
    c=configs[case]
    output=root/f'terms/OT1999/entering-law/OT_1999CHUNK6_{case.upper()}.md'
    args=[sys.executable,'-B','tools/build_entering_law.py',str(output)]
    for heading in c.get('standards',[]): args += ['--standard-heading',heading]
    subprocess.run(args,check=True)
    parts=[output.read_text(encoding='utf-8'),f'## Selection receipt\n\nEvent cutoff: {c["date"]}. Holdings excerpts below are copied verbatim from canonical doctrinal volumes. Current-term extracts are copied from the sanitized neutral projection. Same-day uncoordinated decisions are excluded; later chunk-6 law must be refreshed after its authoritative completion. The slice does not establish new law.\n']
    for slug,headings in c.get('holdings',{}).items():
        path=root/f'state/holdings/{slug}.md'; source=path.read_text(encoding='utf-8')
        for heading in headings:
            parts += [f'## Verbatim Holdings selection: {slug} — {heading}\n\nSource: `state/holdings/{slug}.md`.\n',module.take_heading(source,heading)]
    for prefix in c.get('paragraphs',[]):
        paragraphs=[p for p in neutral.split('\n\n') if p.startswith(prefix)]
        if len(paragraphs)!=1: raise ValueError((case,prefix,len(paragraphs)))
        parts += ['## Current-term verbatim published law or position\n\nSource: `terms/OT1999/workspace/neutral-projection.md`.\n',paragraphs[0]]
    for heading in c.get('sections',[]):
        # Same case may recur in law and published-position sections: preserve both.
        lines=neutral.splitlines(); starts=[i for i,line in enumerate(lines) if line==f'### {heading}']
        if not starts: raise ValueError((case,heading))
        for start in starts:
            end=next((i for i in range(start+1,len(lines)) if lines[i].startswith(('## ','### '))),len(lines))
            parts += ['## Current-term verbatim published law or position\n\nSource: `terms/OT1999/workspace/neutral-projection.md`.\n','\n'.join(lines[start:end])]
    output.write_text('\n\n'.join(parts).rstrip()+'\n',encoding='utf-8')
    print(case,len(output.read_text(encoding='utf-8')))
