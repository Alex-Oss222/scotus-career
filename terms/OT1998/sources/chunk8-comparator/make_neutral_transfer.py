from pathlib import Path
import shutil,hashlib,json,re
base=Path('terms/OT1998/sources/chunk8-comparator');out=Path('terms/OT1998/sources/chunk8-neutral-control');out.mkdir(exist_ok=True)
def clean(n):
 p=(base/(n+'-official.txt')).read_text(encoding='utf-8').split('\f')
 return '\n'.join('\n'.join(x.strip().splitlines()[3:]) for x in p)
def cut(t,a,b):
 return t[t.index(a):t.index(b,t.index(a))]
f=[]
t=clean('goldsmith');f.append(('Goldsmith: actual court-martial sentence, finality, and administrative proposal; 526 U.S. 531–533',cut(t,'Respondent James Goldsmith','We granted certiorari')))
t=clean('wilson');f.append(('Wilson: underlying events and judgment below; 526 U.S. 606–608',cut(t,'In early 1992','Recognizing a split among the Circuits')))
t=clean('hanlon');f.append(('Hanlon: warrant and execution facts as recited from complaint and parties; 526 U.S. 809',cut(t,'Respondents live on a 75,000-acre ranch','Review of the complaint')))
t=clean('cromartie');f.append(('Hunt: judgment below, 526 U.S. 545 (footnote starts but is excluded)',cut(t,'They ﬁled suit in the United States District Court','1 In response to the District Court')))
f.append(('Hunt: route to Court, 526 U.S. 546',cut(t,'The state ofﬁcials ﬁled a notice of appeal.','II\nOur decisions')))
# Remove Supreme Court outcome phrase from the limited appeal-route extraction, preserving all other bytes.
f[-1]=(f[-1][0],f[-1][1].split('and now reverse.')[0])
text='# Objective source extracts for neutral validation\n\nThese are mechanically copied source passages. Reporter running headers are removed. They are evidentiary source material; later reasoning, vote, and outcome passages are excluded. The control receipt distinguishes recitations and allegations.\n\n'
for title,body in f:text+='## '+title+'\n\n'+body.strip()+'\n\n'
(out/'OBJECTIVE_EXTRACTS.md').write_text(text,encoding='utf-8')
t=clean('new-jersey-decree');start=t.index('\nI\n')+1;end=t.index('[Ellis Island Boundary map follows this page.]');instrument=t[start:end].strip()
(out/'NJ_PROPOSED_INSTRUMENT.txt').write_text(instrument+'\n',encoding='utf-8')
shutil.copyfile(base/'new-jersey-decree-map.png',out/'NJ_BOUNDARY_MAP.png')
receipt={'mechanism':'exact substring copies from saved official source text, with reporter running headers removed; six numbered decree parts copied as proposed instrument; map copied byte-for-byte','source':'https://www.supremecourt.gov/opinions/boundvolumes/526bv.pdf','source_sha256':hashlib.sha256(Path('terms/OT1998/sources/chunk7-control/official-526.pdf').read_bytes()).hexdigest(),'artifacts':{p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in out.iterdir() if p.is_file()}}
(out/'COPY_RECEIPT.json').write_text(json.dumps(receipt,indent=2),encoding='utf-8')
print('Copied',len(f),'objective blocks; NJ numbered courses',len(re.findall(r'\(\d+\)',instrument)))
