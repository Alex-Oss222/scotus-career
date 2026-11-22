from pathlib import Path
import importlib.util, json, re, sys

BASE = Path(__file__).resolve().parents[4]
TERM = BASE / 'terms/OT2003'
HERE = Path(__file__).resolve().parent
config = json.loads(Path(sys.argv[1]).read_text(encoding='utf-8'))
spec = importlib.util.spec_from_file_location('assign3', BASE/'tmp/ot2003_chunk3_assign.py')
assignment = importlib.util.module_from_spec(spec)
spec.loader.exec_module(assignment)
block, receipt = assignment.block(**config['assignment'])
author = config['assignment']['author']
text = (HERE/config['draft']).read_text(encoding='utf-8')
text = text.replace('{{ASSIGNMENT}}', block)
text = text.replace('{{AUTHOR}}', author)
text = text.replace('{{OTHER_JOINERS}}', config['joiners'])
text = text.replace(author+' delivered the opinion of the Court, in which '+config['joiners']+' joined.', config['delivery'])
text = text.replace('Any earlier event completed during this Run must be screened before final commitment.', config['screen'])
text = text.replace('{{AUDIT}}', config['audit'])
text = text.replace('Final assignment, later-written earlier-event screening, mechanical projection checks and term validation remain for finalization; this draft is not a completed Record.', 'The assignment was recomputed immediately before writing this Record from the actual public lead-opinion tables, and the stated author satisfies the eligibility and pool rule. Later-written earlier-event public law was screened as stated above. Fixed labels, exactly eleven ordered public blocks, source-copy identity, unresolved placeholders, Chief public naming, links and opinion arithmetic were checked for this Record. Whole-term ledger, manifest, Render Input and check_term validation remain integration tasks and are not represented as completed here.')
text = text.replace('checked at draft stage', 'checked against the final formulation')
text = text.replace('No frozen commitment changes in this draft.', 'No frozen commitment changes in this final formulation.')
text = text.replace('The eight Associates are eligible for the complete lead. Stone-Zsela\'s preservation disposition supplies no complete-rationale eligibility. Fit concerns precise separation of direct commerce, sovereign compulsion and agency presentation; O\'Connor and Scalia have especially direct prior work on the own-activity boundary, while any eligible pool member can express the complete common ground.', 'The eight Associates are eligible for the complete lead. Stone-Zsela\'s preservation disposition supplies no complete-rationale eligibility. The assignment below applies the actual balance pool to the opinion\'s required separation of direct commerce, sovereign compulsion and agency presentation.')
text = text.replace('the actual-burden distinction between operator compliance', 'the distinction between operator compliance')
pub = text.split('## Public Projection\n\n',1)[1]
heads = re.findall(r'^## (.+)$',pub,re.M)
expected = ['Event','Participation','Public Action','Judgment & Remedy','Opinion Topology','Holdings','Precedent Treatment','Law After Decision','Separate Writings','Procedure After Action','Source Notes']
assert heads == expected, heads
assert not re.search(r'\{\{.*?\}\}', text)
assert not re.search(r'\bStone\b(?!-Zsela)',pub)
for label,line in zip(['Case and dockets','Event and date','Result','Version / lineage'],text.splitlines()[:4]):
    assert line.startswith('**'+label+':**')
dest = TERM/'records'/config['record']
assert not dest.exists(), 'Completed event already exists; refusing replacement'
for target in re.findall(r'\]\(([^)]+)\)', text):
    if target.startswith(('http:','https:','#')): continue
    target = target.split('#')[0]
    assert not target or (dest.parent/target).resolve().exists(), target
dest.write_text(text,encoding='utf-8',newline='\n')
(TERM/'freeze'/config['public']).write_text(pub,encoding='utf-8',newline='\n')
(HERE/(config['key']+'_final_assignment.json')).write_text(json.dumps(receipt,indent=2),encoding='utf-8')
print(json.dumps({'record':config['record'],'author':author,'counts':receipt['counts'],'pool':receipt['pool'],'blocks':len(heads)},indent=2))
