from pathlib import Path
import json,re,hashlib,sys
ROOT=Path(__file__).resolve().parents[4]
W=Path(__file__).resolve().parent
def sha(b):return hashlib.sha256(b).hexdigest()
HEADER='# SUPREME COURT OF THE UNITED STATES: HOLDINGS REGISTER\r\n\r\n**Last completed October Term:** 1998\r\n**Processed through:** June 23, 1999, after all 130 completed OT1998 Court events and one admitted source event.\r\n**Edition:** October 29, 2026\r\n\r\n'

def add_backlink(text,case,question,note):
    # Existing holdings remain verbatim; only the particular later-treatment
    # field changes. Select by natural case and question anchors.
    casepos=text.index('#### '+case)
    qpos=text.index('##### '+question,casepos)
    end=re.search(r'\r\n#{2,5} ',text[qpos+1:])
    stop=qpos+1+end.start() if end else len(text)
    block=text[qpos:stop]
    key='**Later-authority backlinks:**'
    if key in block:
        i=block.index(key); stopfield=block.find('\r\n\r\n',i)
        if stopfield<0:stopfield=len(block.rstrip())
        block=block[:stopfield]+' '+note+block[stopfield:]
    else:block=block.rstrip()+'\r\n\r\n'+key+' '+note+'\r\n'
    return text[:qpos]+block+text[stop:]

def modify_force(text,case,question,note,backlink):
    casepos=text.index('#### '+case);qpos=text.index('##### '+question,casepos)
    m=re.search(r'\r\n#{2,5} ',text[qpos+1:]);stop=qpos+1+m.start() if m else len(text)
    block=text[qpos:stop]
    if '**Current-force modification:**' in block:
        block=re.sub(r'\*\*Current-force modification:\*\*.*?(?=\r\n\r\n|\Z)','**Current-force modification:** '+note,block,flags=re.S)
    else:
        authority=re.search(r'\*\*Proposition-level authority:\*\*.*?(?=\r\n\r\n|\Z)',block,re.S)
        at=authority.end();block=block[:at]+'\r\n\r\n**Current-force modification:** '+note+block[at:]
    text=text[:qpos]+block+text[stop:]
    return add_backlink(text,case,question,backlink)

def assemble(passno,files):
    opening=(ROOT/'state/HOLDINGS.md').read_bytes()
    baseline=opening.decode()
    text=HEADER+baseline[baseline.index('## Constitutional Structure'):]
    text=add_backlink(text,'United States v. Fields / Crawley','Each defendant has his own protected relationship to the room',"Minnesota v. Carter and Minnesota v. Johns, No. 97-1147, December 1, 1998: extends the shared-privacy holding to the actual host-authorized private occupancy without making recurring use indispensable; Fields's independent-control ground and exclusion of mere presence remain intact.")
    for case,q in [('Brecht v. Abrahamson','Chapman governs this preserved Doyle claim on habeas'),("O'Neal v. McAninch",'Chapman governs the preserved personal-intent instructional claim'),('California v. Roy','This personal-intent omission permits harmless-error review under Chapman')]:
        text=add_backlink(text,case,q,'Calderon v. Coleman, No. 98-437, December 14, 1998: extends State-borne Chapman review to the defined, properly available capital-selection commutation-instruction claim; the earlier holding remains unchanged and no universal constitutional-habeas extension is adopted.')
    if passno>=2:
        text=modify_force(text,'Growe v. Emison','Fragmentation claims require proof of the causal voting conditions',"Valdespino v. Alamo Heights Independent School District, June 17, 1999, modifies the exclusivity of the district-majority condition for one protected group. The group may instead prove a lawful, geographically compact district in which cohesive voting and dependable crossover support give it actual ability to elect its candidates of choice. The numerical-majority route survives; speculation, isolated electoral success, near-majority arithmetic and influence alone do not establish the alternative. Cohesion, the relevant majority-bloc showing with its special-circumstances qualification, causation, independent totality and constitutional limits remain necessary. The distinct-group coalition and influence-only reservations are not resolved.","Valdespino v. Alamo Heights Independent School District, lower docket 98-50227, June 17, 1999: first-condition functional ability-to-elect alternative for a single protected group.")
        text=add_backlink(text,'Bragdon v. Abbott',"Abbott's own reproductive activity is substantially limited on this record",'Sutton v. United Air Lines, Inc., No. 97-1943, June 22, 1999: resolves the reserved general mitigation question under the original ADA by considering actually used measures and their beneficial and adverse effects; Bragdon\'s reproduction holding and residual-risk application remain intact.')
        text=add_backlink(text,'California v. Roy','Necessary equivalence is sufficient, but not the exclusive permissible inquiry','Neder v. United States, No. 97-1985, June 10, 1999: extends the qualified actual-verdict method to the identified materiality omissions and withdrawals; the charge, actual findings and record conflicts must support reliable noncontribution beyond a reasonable doubt.')
        text=modify_force(text,'New Jersey v. New York','6. Implementation must locate the Compact boundary, not exchange territory',"The Court separately entered the implementing decree on May 17, 1999, 526 U.S. 589, completing this recommittal. Its six-part instrument, complete 182-course perimeter and incorporated December 1, 1998 map now fix the boundary and include the accepted historical filled-pier land once. Approximate acreage and an additional pier parcel do not replace that perimeter. The 1998 Compact construction and territorial entitlement remain unchanged; the decree's injunction and retained implementation jurisdiction govern enforcement.","New Jersey v. New York, No. 120, Original, implementing decree entered May 17, 1999, 526 U.S. 589: geographic implementation and enforcement of the May 26, 1998 judgment.")
    if passno>=3:
        text=add_backlink(text,'Bragdon v. Abbott',"Abbott's own reproductive activity is substantially limited on this record",'Murphy v. United Parcel Service, Inc., No. 97-1992, June 22, 1999, independently adopts the actually-used-measures rule and preserves residual restrictions and adverse effects. Albertson\'s, No. 98-591, supplies no additional disability-method holding.')
        text=add_backlink(text,'Hilton v. South Carolina Public Railways Commission','Whether FELA liability of a state-owned interstate railroad remains enforceable in state court','Alden v. Maine, No. 98-436, June 23, 1999: extends the state-court enforcement principle to the expressly authorized FLSA remedy through its own five-Justice constitutional holding; Hilton\'s retained FELA construction and specialized reliance grounds remain intact.')
        text=add_backlink(text,'Daubert v. Merrell Dow Pharmaceuticals','Reliable scientific foundation and fit require flexible preliminary screening','Kumho Tire Co. v. Carmichael, No. 97-1709, March 23, 1999: extends original-Rule-702 reliability and fit screening to technical and other specialized knowledge, with case-specific flexible criteria and discretion over the reasonable screening method.')
        text=add_backlink(text,'General Electric Co. v. Joiner','Admission and exclusion receive the same abuse-of-discretion review','Kumho Tire Co. v. Carmichael, No. 97-1709, March 23, 1999: applies abuse-of-discretion review to both the reasonable reliability-screening method and the final technical-expert evidentiary decision.')
        text=add_backlink(text,'Kinman v. Omaha Public School District','Recipient damages require actual corrective-official notice and culpable disregard','Davis v. Monroe County Board of Education, No. 97-843, May 24, 1999: extends the sufficient actual-corrective-notice and culpable-disregard route to substantially controlled peer harassment, retaining independent control, sex-based harm, causation and loss requirements. It does not restore exclusivity or transfer the complete teacher-authority route to peers.')
        text=add_backlink(text,'Citizens for a Better Environment v. Steel Co.','Constitutional jurisdiction before a disputed EPCRA merits question','Ruhrgas AG v. Marathon Oil Co., No. 98-470, May 17, 1999: resolves the bounded nonmerits sequencing question by permitting straightforward personal-jurisdiction dismissal before a difficult subject-matter inquiry, subject to the stated state-law and statutory limits; the contested-merits prohibition remains unchanged.')
    entries=[]
    for f in files:entries+=json.loads((W/f).read_text())
    for area in re.findall(r'^## ([^\r\n]+)',text,re.M):
        added=[e for e in entries if e.get('area')==area]
        if not added:continue
        added.sort(key=lambda e:(e['text'].splitlines()[0],e['file']))
        i=text.index('## '+area+'\r\n');nxt=re.search(r'\r\n## ',text[i+1:]);at=i+1+nxt.start() if nxt else len(text)
        blocks=[]
        for e in added:
            question=re.search(r'^##### (.+)$',e['text'],re.M)
            subject=question.group(1) if question else e['text'].splitlines()[0][5:]
            blocks.append('### '+subject+'\n\n'+e['text'].strip())
        insertion='\r\n\r\n'+'\r\n\r\n'.join(x.replace('\n','\r\n') for x in blocks)+'\r\n'
        text=text[:at]+insertion+text[at:]
    out=ROOT/'terms/OT1998/close/HOLDINGS.candidate.md';out.write_bytes(text.encode())
    snapshot=W/f'HOLDINGS.pass{passno}.md';snapshot.write_bytes(out.read_bytes())
    sources={}
    for f in ['state/HOLDINGS.md','foundation/templates/HOLDINGS_TEMPLATE.md','foundation/ENGINE.md','AGENTS.md']:
        sources[f]=sha((ROOT/f).read_bytes())
    for p in (ROOT/'state/holdings').glob('*.md'):sources[str(p.relative_to(ROOT))]=sha(p.read_bytes())
    for e in entries:
        p=ROOT/'terms/OT1998/records'/e['file'];sources[str(p.relative_to(ROOT))]=sha(p.read_bytes())
    renderchunks={1:range(1,6),2:range(1,11),3:range(1,12)}[passno]
    for c in renderchunks:
        p=ROOT/f'terms/OT1998/output/OT_1998CHUNK{c}.md';sources[str(p.relative_to(ROOT))]=sha(p.read_bytes())
    source=ROOT/'terms/OT1998/records/maine_initiative_qualification_admitted_source_1998-12-23.md';sources[str(source.relative_to(ROOT))]=sha(source.read_bytes())
    receipt={'pass':passno,'completed':True,'operation':'Candidate preparation only; no Audit or publication. Chronological pass saved before subsequent pass.','source_sha256':sources,'entry_files':files,'covered_court_records':len({e['file'] for e in entries}),'included_court_records':len({e['file'] for e in entries if e.get('text')}),'area_entries':sum(bool(e.get('text')) for e in entries),'source_event':'Maine administrative qualification; no judicial holding or change to earlier holding present force.','output':str(out.relative_to(ROOT)),'output_bytes':len(out.read_bytes()),'output_sha256':sha(out.read_bytes()),'snapshot':str(snapshot.relative_to(ROOT)),'snapshot_sha256':sha(snapshot.read_bytes()),'baseline_preservation':'Complete opening register retained. Header synchronized. Original Holding text unchanged. Later treatment recorded only in the named current-force fields and material backlinks.'}
    receipt['entry_file_sha256']={f:sha((W/f).read_bytes()) for f in files}
    if passno>1:receipt['preceding_saved_pass_sha256']=sha((W/f'HOLDINGS.pass{passno-1}.md').read_bytes())
    (W/f'PASS{passno}_RECEIPT.json').write_text(json.dumps(receipt,indent=2))
    print(json.dumps({k:v for k,v in receipt.items() if k!='source_sha256'},indent=2))

if __name__=='__main__':assemble(int(sys.argv[1]),sys.argv[2:])
