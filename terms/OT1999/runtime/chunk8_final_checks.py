from pathlib import Path
import hashlib
import importlib.util
import json
import re
import sys
from urllib.parse import unquote

sys.dont_write_bytecode = True
ROOT = Path(__file__).resolve().parents[3]
TERM = ROOT / 'terms/OT1999'
spec = importlib.util.spec_from_file_location('local_tools', TERM / 'runtime/chunk8_tools.py')
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)
headings = ['Event','Participation','Public Action','Judgment & Remedy','Opinion Topology','Holdings','Precedent Treatment','Law After Decision','Separate Writings','Procedure After Action','Source Notes']
errors = []
records = []
for p in (TERM / 'records').glob('*.md'):
    t = p.read_text(encoding='utf-8')
    em = re.search(r'^\*\*Event and date:\*\*.*$',t,re.M)
    if not em or not re.search(r'chunk 8\b',em[0],re.I):
        continue
    date = re.search(r'\d{4}-\d{2}-\d{2}',em[0])[0]
    case = re.search(r'^\*\*Case and dockets:\*\*\s*(.*)',t,re.M)[1].split(';')[0].rstrip('.')
    records.append((date,case,p,t))
    pub = t.split('## Public Projection',1)[-1]
    hs = re.findall(r'^## ([^\n]+)',pub,re.M)
    if hs != headings:
        errors.append(p.name+': incorrect public headings '+str(hs))
    internal = re.search(r'^## Controlling holdings\s*\n(.*?)(?=^## |\Z)',t,re.M|re.S|re.I)
    public = re.search(r'^## Holdings\s*\n(.*?)(?=^## |\Z)',pub,re.M|re.S)
    if internal and public and internal[1].strip()!=public[1].strip():
        errors.append(p.name+': internal/public holdings differ')
    if re.search(r'\b(?:simulated|user-directed|approval history|approved by (?:the )?user|freeze/|runtime/|workflow|research cutoff|commit hash)\b',pub,re.I):
        errors.append(p.name+': public workflow term requires review')
    for target in re.findall(r'\]\(([^)]+)\)',t):
        if target.startswith(('https://','http://','#')):
            continue
        path = target.split('#',1)[0].strip('<>')
        if path and not (p.parent / unquote(path)).exists():
            errors.append(p.name+': unresolved link '+target)
stops = json.loads((TERM/'runtime/OT_1999CHUNK8_STOPS.json').read_text(encoding='utf-8'))
if len(records)+len(stops)!=12:
    errors.append(f'Expected twelve matters, got {len(records)} complete and {len(stops)} stopped')
# Recompute every saved count independently of any preceding tally.
count_checks = []
for p in sorted((TERM/'freeze').glob('OT_1999CHUNK8_*_COUNTS.json')):
    data=json.loads(p.read_text(encoding='utf-8'))
    fresh=mod.counts(data['before_date'],data['before_case'])
    same=all(data.get(k)==fresh[k] for k in ['counts','total','last_event','counted_events'])
    count_checks.append({'receipt':p.name,'matches_actual_records':same})
    if not same:errors.append(p.name+': count receipt does not match actual preceding Records')
# Scan new task-controlled text only; do not inspect the locked directory or historical source trees.
controlled=[]
for sub in ['runtime','freeze','entering-law','sources/chunk8','workspace']:
    for p in (TERM/sub).rglob('*'):
        if p.is_file() and p.suffix.lower() in ['.md','.txt','.json','.html','.csv']:
            if sub in ['runtime','freeze','entering-law'] and 'CHUNK8' not in p.name:continue
            controlled.append(p)
controlled += [r[2] for r in records]+[TERM/'render-inputs/OT_1999CHUNK8.md']
for p in controlled:
    if not p.exists():continue
    t=p.read_text(encoding='utf-8',errors='replace')
    if re.search(r'(?:https?://(?:[^/\s]+\.)?(?:github\.com|githubusercontent\.com|onedrive\.(?:live\.com|com))|https?://(?:localhost|127\.0\.0\.1)|file://|\]\(<?[A-Za-z]:[/\\])',t,re.I):
        errors.append(str(p.relative_to(TERM))+': forbidden external or local-machine link')
report={'completed':len(records),'stopped':stops,'count_checks':count_checks,'errors':errors,'git_commands':'Not run; prohibited by the operator','records':[{'date':d,'case':c,'file':p.name,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()} for d,c,p,t in sorted(records)]}
out=TERM/'freeze/OT_1999CHUNK8_FINAL_CHECKS.json'
out.write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
print(json.dumps(report,indent=2))
if errors:raise SystemExit(1)
