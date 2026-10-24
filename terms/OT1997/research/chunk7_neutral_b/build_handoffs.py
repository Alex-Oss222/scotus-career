from pathlib import Path
import os, re, subprocess, sys

ROOT=Path(__file__).resolve().parents[4]
os.environ['PYTHONDONTWRITEBYTECODE']='1'
TERM=ROOT/'terms/OT1997'
RUNTIME=(TERM/'runtime/OT_1997CHUNK7_NEUTRAL.md').read_text(encoding='utf-8')
PROJ=(TERM/'workspace/neutral-projection.md').read_text(encoding='utf-8')

CASES={
 'chaudhuri':('Chaudhuri v. Tennessee', ['Lemon test','Official graduation worship and independent religious pressure','Continuing individual controversy and legally unavailable damages','Private religious viewpoints in public forums and printing benefits'], {'first-amendment':['Lee v. Weisman','Agostini','Sherman','Ingebretsen','Pinette','Rosenberger'],'federal-courts':['Arizonans for Official English']}, ['Tanford v. Brand']),
 'edwards':('Edwards v. United States', ['Relevant-conduct sentencing and a later distinct prosecution','Jury determination of criminal materiality','Forfeited error and discretionary correction under Rule 52(b)','Authoritative interpretive Guidelines commentary'], {'criminal-procedure':['Witte v.','Watts /','United States v. Gaudin','Johnson v. United States','Griffin v. United States','United States v. R.L.C.','United States v. LaBonte']}, ['Almendarez-Torres','Rogers v. United States']),
 'calderon':('Calderon v. Thompson', ['Crime innocence as a gateway to otherwise barred habeas claims','Capital eligibility innocence as a gateway to barred habeas claims','Temporal reach of ordinary AEDPA habeas amendments','Second or successive state-custody habeas applications'], {'federal-courts':['Schlup','Sawyer v. Whitley','Lindh','Felker','Bell v. Thompson'],'criminal-procedure':['Schlup','Sawyer v. Whitley']}, ['Carriger v. Stewart','Trest v. Cain']),
 'romani':('United States v. Estate of Romani', ['Federal lien notice and after-acquired property priority','Federal income-tax duties of corporate assignees and separate liquidating trusts'], {'federal-taxation':['Holywell','United States v. Hill','United States v. McDermott']}, []),
 'ricci':('Ricci v. Village of Arlington Heights', ['Objective probable cause for an ordinary initial traffic stop','Possessory seizures and the claimant\'s own Fourth Amendment interest','Criminal fair warning under §242'], {'criminal-procedure':['Whren','Wilson v. Arkansas','Soldal','Lanier'],'civil-rights':['Hafer','Leatherman','Lanier','Ayeni']}, ['Smith v. Barber']),
 'perry':('Perry v. Los Angeles Police Department', ['Commercial-speech advancement and fit in selective restrictions','Speech burdens in a content-neutral injunction','Private religious viewpoints in public forums and printing benefits','Residential signs and preservation of a distinctive speech medium','Anonymous individual political leaflets'], {'first-amendment':['Cincinnati v. Discovery','Rosenberger','Madsen','City of Ladue','McIntyre','International Society for Krishna Consciousness']}, []),
}

def sections(text, level):
 pat=r'^'+('#'*level)+r' ([^\n]*)\n(.*?)(?=^#{1,'+str(level)+r'} |\Z)'
 return [(m.group(1),m.group(0).strip()) for m in re.finditer(pat,text,re.S|re.M)]

freeze=[]
for slug,(name,standards,areas,current) in CASES.items():
 out=TERM/'entering-law'/('OT_1997CHUNK7_'+slug+'.md')
 cmd=[sys.executable,str(ROOT/'tools/build_entering_law.py'),str(out),'--root',str(ROOT)]
 for title in standards:cmd+=['--standard-heading',title]
 subprocess.run(cmd,check=True,env=os.environ)
 with out.open('a',encoding='utf-8') as f:
  for area,names in areas.items():
   source=ROOT/'state/holdings'/f'{area}.md'
   for title,body in sections(source.read_text(encoding='utf-8'),4):
    if any(n in title for n in names):f.write('\n\n## Verbatim authority from state/holdings/'+area+'.md\n\n'+body+'\n')
  for title,body in sections(PROJ,3):
   if any(n in title for n in current):f.write('\n\n## Current-term public law copied from workspace/neutral-projection.md\n\n'+body+'\n')
  f.write('\n\n## Chronology and participation\n\nThe current neutral projection is effective through April 16, 1998. Earlier completed chunk-7 events must be refreshed before a dependent event; uncoordinated same-day matters use the common preceding baseline. The established roster is Chief Justice Stone-Zsela and Justices Stevens, O\'Connor, Scalia, Kennedy, Souter, Thomas, Ginsburg and Breyer. No case-specific nonparticipation is established in this neutral packet. A missing argument date is not invented.\n')
 # This export edits derived material only, preserving supplied record facts mechanically.
 raw=next(body for title,body in sections(RUNTIME,1) if title==name) if False else re.search(r'^# '+re.escape(name)+r'\n(.*?)(?=^# (?!SECTION I)|\Z)',RUNTIME,re.S|re.M).group(0)
 raw=raw.split('## B. LAW ENTERING THE CASE')[0]
 raw='\n'.join(l for l in raw.splitlines() if not any(x in l for x in ['**Participation Matter:**','**Evidence Status:**','**Threshold, Preservation, and Vehicle Matters:**']))
 raw=re.sub(r'^\* \*\*Entry Stage and Event:\*\*.*$', '* **Entry Stage and Event:** Scheduled Supreme Court review event; the supplied question and lower judgment identify the matter. No present Supreme Court disposition is supplied.', raw,flags=re.M)
 raw=re.sub(r'^\* \*\*Citation or Docket:\*\* 523 U\.S\. \d+; ', '* **Citation or Docket:** ',raw,flags=re.M)
 raw=raw.replace('Opinion/order delivered ', 'Scheduled event ')
 raw=raw.replace('The procedural character of the historical matter is retained; no additional grant or completed new-run judgment is inferred.','')
 # Excluded framing is not carried through the safe draft.
 raw=raw.replace('Historical opinion delivery date.','').replace('Historical DIG order date.','')
 if slug=='calderon':
  raw=raw.replace(' after the Supreme Court had denied review of the earlier judgment','')
  raw=raw.replace("In June, Thompson's certiorari petition was denied, and the Ninth Circuit issued",'In June, the Ninth Circuit issued')
  raw+='\n\nSource-status limit: No historical Supreme Court procedural action is imported as an in-world order. The described lower-court mandate chronology remains a source account for fresh validation; it supplies no intervening Supreme Court disposition.\n'
 raw+='\n\n## B. Current entering law\n\nRead entering-law/OT_1997CHUNK7_'+slug+'.md and the current workspace/neutral-projection.md. Current dated holdings supersede older supplied law excerpts. No same-matter Supreme Court outcome or private position supplies an entering premise.\n'
 raw+='\n## C. Source limits and neutral supplement\n\nThe questions above are analytical formulations, not verified petition quotations. The current roster supplies participation subject to a supported case-specific order. No unseen filing, concession, waiver, deadline, later procedural act or docket number is inferred. See research/chunk7_neutral_b/SUPPLEMENT.md for the validated case-specific scope and analytical alternatives; cases without a supplement require fresh preflight validation before modeling.\n'
 if slug=='edwards':
  sup=(TERM/'research/chunk7_neutral_facts/edwards.md').read_text(encoding='utf-8')
  sup='\n'.join(l for l in sup.splitlines() if not l.startswith('Sources:'))
  raw+='\n## D. Objective record supplement\n\nSource: control-extracted published record recitations, with the source limits expressly retained below.\n\n'+sup+'\n'
 dest=TERM/'freeze'/('OT_1997CHUNK7_'+slug.upper()+'_NEUTRAL.md')
 dest.write_text(raw.strip()+'\n',encoding='utf-8')
 freeze.append(raw.strip())
(TERM/'freeze/OT_1997CHUNK7_B_NEUTRAL.md').write_text('# OT1997 chunk 7 — six neutral packets\n\nDerived case facts and current-law handoffs. Read the case-specific supplement and preparation receipt for validation scope; no commitments are made by these packets.\n\n'+'\n\n---\n\n'.join(freeze)+'\n',encoding='utf-8')
print('Six case packets and entering-law slices written.')
