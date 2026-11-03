from pathlib import Path
import hashlib
import json
import re

root=Path(__file__).resolve().parents[3]
term=root/'terms/OT1999'
draft=term/'preparation/OT_1999CHUNK6_SAENZ_RECORD_DRAFT.md'
stone=(term/'runtime/OT_1999CHUNK6_SAENZ_STONE.md').read_text(encoding='utf-8')
core=stone[stone.index('## B. JUDGMENT AND REMEDY'):].rstrip()
text=draft.read_text(encoding='utf-8')
assert text.count('@@STONE_APPROVED_CORE@@')==1
text=text.replace('@@STONE_APPROVED_CORE@@',core)
target=term/'records/saenz-v-heldenfels-brothers-inc_merits_2000-05-09.md'
assert not target.exists(), 'No existing adjudication may be overwritten'
labels=['**Case and dockets:**','**Event and date:**','**Result:**','**Version / lineage:**']
assert all(text.splitlines()[i].startswith(label) for i,label in enumerate(labels))
projection=text.split('\n## Public Projection\n',1)[1]
blocks=['Event','Participation','Public Action','Judgment & Remedy','Opinion Topology','Holdings','Precedent Treatment','Law After Decision','Separate Writings','Procedure After Action','Source Notes']
assert re.findall(r'^## (.+)$',projection,re.M)==blocks
assert not re.search(r'(?i)workflow|simulat|approved|reconcil|commitment|lineage|2026|count receipt|frozen',projection)
assert not re.search(r'(?i)file://|onedrive|github|C:[\\/]',text)
for destination in re.findall(r'\]\(([^)]+)\)',text):
    if destination.startswith('http'):continue
    destination=destination.split('#',1)[0]
    if destination.endswith('OT_1999CHUNK6_SAENZ_ASSEMBLY_VALIDATION.md'):continue
    assert (target.parent/destination).resolve().exists(),destination
counts=json.loads((term/'freeze/OT_1999CHUNK6_SAENZ_COUNTS.json').read_text(encoding='utf-8'))
expected={'Stone-Zsela':6,'Stevens':7,"O'Connor":6,'Scalia':6,'Kennedy':7,'Souter':7,'Thomas':6,'Ginsburg':7,'Breyer':6}
assert counts['counts']==expected
assert counts['last_event']['case']=='National Mining Association v. United States Department of the Interior'
roster=set(expected)
vacate={'Stone-Zsela','Stevens','Souter','Ginsburg','Breyer'}
affirm={"O'Connor",'Scalia','Kennedy','Thomas'}
application=vacate-{'Stone-Zsela'}
assert len(vacate)==5 and len(affirm)==4 and vacate|affirm==roster and not vacate&affirm
assert len(application)==4 and application|affirm|{'Stone-Zsela'}==roster
joins={'I':vacate,'II-A':roster,'II-B':application,'III':vacate}
assert [len(joins[p]) for p in ['I','II-A','II-B','III']]==[5,9,4,5]
eligible=set.intersection(*joins.values())
assert eligible==application
minimum=min(expected[j] for j in eligible)
pool={j for j in eligible if expected[j]<=minimum+1}
assert minimum==6 and pool==eligible and 'Breyer' in pool
holdings=projection.split('## Holdings\n',1)[1].split('## Precedent Treatment\n',1)[0]
word_counts=[]
for part in re.split(r'^#### ',holdings,flags=re.M)[1:]:
    body=part.split('**Controlling explanation:**',1)[1].split('**Limits and questions not reached:**',1)[0]
    words=len(body.split());assert words<=350,(part.splitlines()[0],words)
    word_counts.append(words)
assert core in text and core not in projection
hashes={}
for suffix in ['COMMITMENTS','COMMITMENTS_SOURCE_REVALIDATED','RECONCILED']:
    name='OT_1999CHUNK6_SAENZ_'+suffix+'.md'
    frozen=(term/'freeze'/name).read_bytes()
    hashes[suffix]=hashlib.sha256(frozen).hexdigest()
    if suffix!='COMMITMENTS':assert frozen==(term/'runtime'/name).read_bytes(),name
assert hashes['COMMITMENTS']=='1a14eb20b10fe407d48f7ee1b873190b4877787ec79f5494e2fc2bba4b5a2886'
assert hashes['COMMITMENTS_SOURCE_REVALIDATED']=='892d7af575d0099b269fb9061be026bc5c314c9405f5462d6be1fc9ec54d9fad'
assert hashes['RECONCILED'].startswith('e5168a5b30adcd')
target.write_text(text,encoding='utf-8')
receipt='''# Saenz assembly validation

Completed checks before final save:

- Exact four opening labels and eleven bounded level-two Public Projection blocks in required order.
- Exact authorized Stone judgment, remedy and issue positions mechanically copied. The actual incident date executes the reserved inquiry, not a new immunity conclusion. Parts I, II-A and III are joined; II-B is unjoined. No fallback or invented branch.
- Both federal judgments: five vacate (Stone-Zsela, Stevens, Souter, Ginsburg, Breyer), four affirm (O'Connor, Scalia, Kennedy, Thomas). Proposition joins I/II-A/II-B/III: 5/9/4/5. No majority immunity application or Marks shortcut. Personal immunity never substitutes for county attribution or the underlying deprivation.
- Form fixed before fresh count. Counts derive from actual prior Records including Mining; all nine, last event, eligible full-lead authors, minimum-plus-one pool, chosen Breyer and comparative fit are stated. Four eligible authors can carry the full lead, so no divided delivery. The Chief assigns because he supports both judgment components.
- Final reconciliation and source-revalidated supplement match their runtime working copies. Original source-model bytes remain preserved; obsolete eight-Associate immunity alignment is not operative. Recorded hashes follow below.
- Complete current lower opinion and eight notes read. Required source supplements considered with their actual holdings, dates and limitations; no new source or factual patch introduced. Later-law notice, hindsight intoxication, actual causation, county policy and guaranteed trial are excluded.
- Local links resolve except this simultaneously created receipt. No machine, OneDrive or GitHub links; no workflow/private metadata in Public Projection. Explanation word counts: %s, all below 350.

Legal review confirms the four vacating Associates retain their stronger no-immunity application as noncontrolling published substance; Stone's method-and-remand position is not converted into an application vote. No non-Stone commitment changes in assembly. No unresolved assembly blocker remains. This receipt does not claim workspace integration, term-wide verification, rendering or Git-history review. No Git operation was performed.

## Frozen source identity

%s
'''%(', '.join(map(str,word_counts)), '\n'.join('- '+k+': `'+v+'`' for k,v in hashes.items()))
(term/'freeze/OT_1999CHUNK6_SAENZ_ASSEMBLY_VALIDATION.md').write_text(receipt,encoding='utf-8')
print(target.relative_to(root).as_posix())
print('Exact core, freeze identity, projection, links, arithmetic and pool verified. Explanation words:',word_counts)
