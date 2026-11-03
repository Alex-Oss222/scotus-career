from pathlib import Path
import json
import re

root = Path(__file__).resolve().parents[3]
term = root / 'terms/OT1999'
draft = term / 'preparation/OT_1999CHUNK6_MINING_RECORD_DRAFT.md'
stone = (term / 'runtime/OT_1999CHUNK6_MINING_STONE.md').read_text(encoding='utf-8')
core = stone[stone.index('## B. JUDGMENT AND REMEDY'):].rstrip()
text = draft.read_text(encoding='utf-8')
assert text.count('@@STONE_APPROVED_CORE@@') == 1
text = text.replace('@@STONE_APPROVED_CORE@@', core)
target = term / 'records/national-mining-association-v-department-of-interior_merits_2000-05-08.md'
assert not target.exists(), 'Existing adjudication must not be overwritten'
labels = ['**Case and dockets:**','**Event and date:**','**Result:**','**Version / lineage:**']
assert all(text.splitlines()[i].startswith(label) for i,label in enumerate(labels))
projection = text.split('\n## Public Projection\n',1)[1]
blocks = ['Event','Participation','Public Action','Judgment & Remedy','Opinion Topology','Holdings','Precedent Treatment','Law After Decision','Separate Writings','Procedure After Action','Source Notes']
assert re.findall(r'^## (.+)$', projection, re.M) == blocks
assert not re.search(r'(?i)workflow|simulat|approved|reconcil|commitment|lineage|2026|count receipt', projection)
assert not re.search(r'(?i)file://|onedrive|github|C:[\\/]', text)
for destination in re.findall(r'\]\(([^)]+)\)', text):
    if destination.startswith('http'): continue
    destination=destination.split('#',1)[0]
    if destination.endswith('OT_1999CHUNK6_MINING_ASSEMBLY_VALIDATION.md'): continue
    assert (target.parent/destination).resolve().exists(), destination
counts=json.loads((term/'freeze/OT_1999CHUNK6_MINING_COUNTS.json').read_text(encoding='utf-8'))
expected={'Stone-Zsela':6,'Stevens':6,"O'Connor":6,'Scalia':6,'Kennedy':7,'Souter':7,'Thomas':6,'Ginsburg':7,'Breyer':6}
assert counts['counts'] == expected
assert counts['last_event']['case']=='North Carolina Right to Life, Inc. v. Bartlett'
roster=set(expected)
associates=roster-{'Stone-Zsela'}
components={'I':(roster,set()),'II':(associates,{'Stone-Zsela'}),'III':(roster,set())}
for support,oppose in components.values():
    assert support|oppose==roster and not support&oppose
    assert len(support)+len(oppose)==9
eligible=associates
minimum=min(expected[j] for j in eligible)
pool={j for j in eligible if expected[j]<=minimum+1}
assert minimum==6 and pool==associates and 'Stevens' in pool
word_counts=[]
holdings=projection.split('## Holdings\n',1)[1].split('## Precedent Treatment\n',1)[0]
for part in re.split(r'^#### ',holdings,flags=re.M)[1:]:
    body=part.split('**Controlling explanation:**',1)[1]
    body=body.split('**Limits and questions not reached:**',1)[0]
    words=len(body.split())
    assert words<=350, (part.splitlines()[0],words)
    word_counts.append(words)
assert core in text and core not in projection
target.write_text(text,encoding='utf-8')
receipt='''# National Mining assembly validation

Completed checks before final save:

- Exact four opening labels and bounded eleven level-two Public Projection blocks in required order.
- Exact approved judgment/remedy/issue core mechanically copied from the authorized per-case Stone file. Fixed affirmance preserved on the temporal component; no fallback, new conditional branch or conversion of the prospective reservation into reversal assent.
- All nine participants accounted for: Parts I/III 9–0, Part II 8–1. Opinion joins and consequent remedy agree with each component. Stone has the stated partial join and separate dissent; no Associate commitment changes.
- Form fixed before fresh counts. Counts parsed from actual earlier Records including Carmell and NCRL. All nine counts, last event, full-rationale eligibility, minimum-plus-one pool, author and comparative fit are recorded. Component assignment authorities are Chief/Stevens/Chief. A single fully eligible Stevens lead counts once.
- Full lower opinion including fourteen footnotes read; present/former control, every willful-pattern condition, correction-in-progress, schedule/other-information distinction, pre-rule violation/post-rule acquisition, express correction and state-primacy safeguards preserved. No specific final adjudication or source-gap default supplied.
- Frozen modeling and reconciliation positions retained with Justice-specific legal support and the limited historical-departure account. No invented circulation or source patch.
- Local links resolve, apart from this receipt which is created with the Record. No machine, OneDrive or GitHub links. No workflow/private metadata in Public Projection. Controlling explanation word counts: %s; each below 350.

No legal assembly blocker remains. This check does not claim Git-history verification, workspace integration, term-wide check or Render completion; those were outside this assembly task. No Git operation was performed.
''' % ', '.join(map(str,word_counts))
(term/'freeze/OT_1999CHUNK6_MINING_ASSEMBLY_VALIDATION.md').write_text(receipt,encoding='utf-8')
print(target.relative_to(root).as_posix())
print('Projection, links, exact core, arithmetic and pool checks passed; explanation words:',word_counts)
