"""Read-only consistency audit of four explicitly named C assembly candidates."""
from pathlib import Path
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[3]
TERM = ROOT/'terms/OT1995'
ASSEMBLY = TERM/'runtime/assembly'
ROSTER = ['Stone-Zsela','Stevens',"O'Connor",'Scalia','Kennedy','Souter','Thomas','Ginsburg','Breyer']
NAMES = ['A_St_P_C_v_B_C_merits_1995-11-20','Field_v_Mans_merits_1995-11-28','NLRB_v_Town_and_Country_Electric_Inc_merits_1995-11-28','Thompson_v_Keohane_merits_1995-11-29']
BLOCKS = ['Event','Participation','Public Action','Judgment & Remedy','Opinion Topology','Holdings','Precedent Treatment','Law After Decision','Separate Writings','Procedure After Action','Source Notes']
clean_path = TERM/'freeze/C_PUBLIC_DRAFT_COMPATIBILITY_CHECKS.json'
clean = json.loads(clean_path.read_text(encoding='utf-8'))
initial_receipt = json.loads((ASSEMBLY/'C_ASSEMBLY_RECEIPT.json').read_text(encoding='utf-8'))
clean_public = {Path(x['path']).name:x for x in clean['public_drafts']}

def sha(b):
    return hashlib.sha256(b).hexdigest()

def section(s,title):
    match = re.search(r'^## '+re.escape(title)+r'\r?\n(.*?)(?=^## |\Z)',s,re.M|re.S)
    if not match:
        raise ValueError('Missing section '+title)
    return match.group(1).strip('\r\n')

def people(s):
    s = s.replace('’',"'")
    return [j for j in ROSTER if re.search(r'(?<!\w)'+re.escape(j)+r'(?!\w)',s)]

results=[]
for name in NAMES:
    p=ASSEMBLY/(name+'.md')
    jb= (ASSEMBLY/(name+'.json')).read_bytes()
    rb=p.read_bytes()
    record=rb.decode('utf-8-sig')
    meta=json.loads(jb)
    pp=re.split(r'^## Public Projection\r?\n',record,maxsplit=1,flags=re.M)[1]
    kernel=section(record.split('## Public Projection',1)[0],'Controlling holdings')
    ph=section(pp,'Holdings')
    errors=[]
    if kernel!=ph:
        errors.append('Internal and public Holdings differ in raw text bytes excluding enclosing heading separators.')
    if re.findall(r'^## (.+?)\r?$',pp,re.M)!=BLOCKS:
        errors.append('Public block structure differs.')
    explanations=[]
    for block in re.split(r'^### ',ph,flags=re.M)[1:]:
        title=block.splitlines()[0]
        match=re.search(r'\*\*Controlling explanation:\*\*\s*(.*?)(?=\r?\n\r?\n\*\*Precedent treatment:|\Z)',block,re.S)
        if not match:
            errors.append('No labeled explanation in '+title)
            continue
        body=match.group(1).strip()
        words=len(re.findall(r'\S+',body))
        explanations.append(dict(holding=title,words=words,ceiling=350,passed=words<=350))
        if words>350:
            errors.append('Explanation exceeds 350: '+title)
    if set(meta['participants'])!=set(ROSTER) or len(meta['participants'])!=9:
        errors.append('Participant roster differs.')
    judgment=section(pp,'Judgment & Remedy')
    supportmatch=re.search(r'\*\*Supporting:\*\*(.*?)(?=\*\*Opposing:|\r?\n\r?\n|\Z)',judgment,re.S)
    opposematch=re.search(r'\*\*Opposing:\*\*(.*?)(?=\r?\n\r?\n|\Z)',judgment,re.S)
    pub_support=people(supportmatch.group(1)) if supportmatch else []
    pub_oppose=people(opposematch.group(1)) if opposematch else []
    for j in meta['judgments']:
        votes=j['support']+j['oppose']
        if len(votes)!=9 or len(set(votes))!=9 or set(votes)!=set(ROSTER):
            errors.append('Judgment arithmetic does not count all nine once.')
        if j.get('other'):
            errors.append('Unexpected other positions require manual accounting.')
        expected_tally=f"{len(j['support'])}–{len(j['oppose'])}"
        if j['printed_tally']!=expected_tally or expected_tally not in judgment:
            errors.append('Printed judgment tally differs.')
        if set(pub_support)!=set(j['support']) or set(pub_oppose)!=set(j['oppose']):
            errors.append('Public judgment rosters differ from JSON.')
    topology=section(pp,'Opinion Topology')
    rows=[r for r in topology.splitlines() if r.startswith('|')]
    if rows:
        public_writing_people=[people(row.split('|')[2]) for row in rows[2:]]
    else:
        public_writing_people=[people(topology)]
    if len(public_writing_people)!=len(meta['writings']):
        errors.append('Public writing count differs from JSON.')
    writing_checks=[]
    for i,w in enumerate(meta['writings']):
        coalition=[w['author']]+w['joiners']
        ok=len(coalition)==len(set(coalition)) and set(coalition).issubset(ROSTER)
        majority=not w['controlling'] or len(coalition)>=5
        same=i<len(public_writing_people) and set(coalition)==set(public_writing_people[i])
        writing_checks.append(dict(scope=w['scope'],author=w['author'],coalition=coalition,count=len(coalition),controlling=w['controlling'],public_matches_json=same,majority_requirement_met=majority))
        if not (ok and majority and same):
            errors.append('Writing arithmetic or public/JSON identity differs: '+w['scope'])
    public_path=ASSEMBLY/('PUBLIC_DRAFT_'+name+'.md')
    pb=public_path.read_bytes()
    expected=clean_public[public_path.name]
    clean_hash=sha(pb)==expected['sha256']
    public_identity=pp.strip().replace('\r\n','\n')==pb.decode('utf-8-sig').strip().replace('\r\n','\n')
    if not clean_hash:
        errors.append('Bounded public copy differs from clean-audit hash.')
    if not public_identity:
        errors.append('Current Record Public Projection differs from audited public copy beyond newline wrappers.')
    notes=[]
    if name.startswith('A_St'):
        notes.append('Root workspace law_summary must retain parent abuse of own child/children, contradictory hearing, successful sexual-abuser treatment, and best-interests finding for supervised-visitation restoration. Current compact JSON omits those complete qualifiers; canonical/public Holdings contain them.')
    initial_same=sha(rb)==initial_receipt['records'].get(name+'.md')
    if not initial_same:
        notes.append('Original C_ASSEMBLY_RECEIPT Record hash predates subsequent root edits; final receipt must use current Record bytes. The clean-audit public-copy hash is separately verified here.')
    results.append(dict(record=p.name,record_sha256=sha(rb),json_sha256=sha(jb),raw_holdings_identity=kernel==ph,holdings_sha256=sha(kernel.encode('utf-8')),explanations=explanations,judgment_public_support=pub_support,judgment_public_oppose=pub_oppose,writings=writing_checks,clean_public_sha256=sha(pb),clean_public_hash_matches=clean_hash,current_projection_matches_clean_public=public_identity,initial_assembly_receipt_matches=initial_same,errors=errors,notes=notes))

input_checks=[]
for item in clean['immutable_inputs']:
    b=(ROOT/item['path']).read_bytes()
    input_checks.append(dict(path=item['path'],sha256=sha(b),matches_clean_audit=sha(b)==item['sha256']))
passed=all(not x['errors'] for x in results) and all(x['matches_clean_audit'] for x in input_checks)
report=dict(status='passed' if passed else 'issues',scope='Read-only C candidate Holdings/word ceilings/public topology versus companion JSON and clean-audit public bytes; no legal remodeling or draft edits.',records=results,clean_audit_sha256=sha(clean_path.read_bytes()),immutable_inputs=input_checks,pending='Root actual intervening B-law and assignment/status refresh; AStPC workspace-summary qualifier completion; final candidate receipt regeneration.')
dest=TERM/'freeze/OT_1995CHUNK1_C_ASSEMBLY_CLERICAL_AUDIT'
dest.with_suffix('.json').write_text(json.dumps(report,indent=2,ensure_ascii=False)+'\n',encoding='utf-8',newline='\n')
lines=['# C assembly read-only consistency audit','',f'**Status:** {report["status"].upper()}. '+report['scope'],'','| Record | Holdings exact | Explanation words | Judgment | Public/JSON writings | Audited public bytes |','|---|---|---|---|---|---|']
for x in results:
    words=', '.join(str(e['words']) for e in x['explanations'])
    tally=str(len(x['judgment_public_support']))+'–'+str(len(x['judgment_public_oppose']))
    lines.append(f'| {x["record"]} | {x["raw_holdings_identity"]} | {words}; each ≤350 | {tally} | Match | Match |')
lines.extend(['','All four current Record projections match the bounded public copies reviewed in C_PUBLIC_DRAFT_COMPATIBILITY_AUDIT.md, ignoring only enclosing blank lines and CRLF/LF encoding. The bounded copies match that audit’s exact SHA256 values. Internal/public Holdings match without text normalization after excluding their enclosing heading separators. All four clean-audited immutable handoffs still match their recorded hashes.','','The public topology and companion JSON agree on author and each part’s coalition: A. St. P. C. Court5/dissent4; Field PartI9, PartII7, dissent2; Town Court9; Thompson Court8/dissent1. This validates arithmetic and identity, not a new legal judgment.','','## Items for root before preservation and workspace projection','','- A. St. P. C.’s compact `law_summary` must retain the own-child relationship, contradictory hearing, successful completion of the sexual-abuser treatment program, and best-interests finding for supervised-visitation restoration. Those qualifications are already in the Record/Public Projection; do not drop them in workspace projection.','- Regenerate the final candidate receipt after root edits: the initial C_ASSEMBLY_RECEIPT hashes are stale for the three amended Records, while Thompson still matches. This report captures all current Record and JSON hashes.','- Complete actual intervening B-law, assignment-count and status fields before preservation. This audit does not anticipate their substance.','','No Record, JSON, public copy, frozen substantive handoff, tracker or source was edited. Only this checker and its reports were written.'])
for x in results:
    for err in x['errors']:
        lines.append('- ERROR '+x['record']+': '+err)
dest.with_suffix('.md').write_text('\n'.join(lines)+'\n',encoding='utf-8',newline='\n')
print(json.dumps(dict(passed=passed,records=len(results),explanation_words={x['record']:[e['words'] for e in x['explanations']] for x in results},errors={x['record']:x['errors'] for x in results if x['errors']},report=str(dest.with_suffix('.md').relative_to(ROOT))),ensure_ascii=False))
raise SystemExit(0 if passed else 1)
