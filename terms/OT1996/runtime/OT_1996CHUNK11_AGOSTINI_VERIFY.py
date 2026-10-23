from pathlib import Path
import re,json,hashlib
ROOT=Path.cwd(); BASE=ROOT/'terms/OT1996'
baseline=json.loads((ROOT/'tmp/agostini_baseline_sha256.json').read_text())
files=baseline['files']; sha=lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
protected=[n for n in files if '/briefs/' in n or '/output/' in n or n.endswith('/case-list.md')]
earlier=[n for n in files if '/records/' in n and (m:=re.search(r'(\d{4}-\d{2}-\d{2})\.md$',n)) and m.group(1)<'1997-06-23']
frozen=[n for n in files if re.search(r'/freeze/OT_1996CHUNK11_(?:NEUTRAL|COMMITMENTS|RECONCILED)(?:_JUNE23)?\.md$',n)]
errors=[]
for n in protected+earlier+frozen:
    if sha(ROOT/n)!=files[n]: errors.append('protected hash mismatch: '+n)
current={p.relative_to(ROOT).as_posix() for p in (BASE/'records').glob('*.md') if p.is_file()}
previous={n for n in files if '/records/' in n and n.endswith('.md')}
if current!=previous: errors.append('Record file set changed')
pre=json.loads((ROOT/'tmp/agostini_prebuild_entry_hashes.json').read_text())
changed_entries=[]; total=0
for filename,rows in pre.items():
    p=BASE/'render-inputs'/filename; s=p.read_bytes(); ms=list(re.finditer(rb'<!-- source-record: ([^>]+) -->',s))
    names=[m.group(1).decode() for m in ms]
    if names != [r['record'] for r in rows]: errors.append('entry order differs: '+filename)
    for i,m in enumerate(ms):
        total+=1; block=s[m.start():ms[i+1].start() if i+1<len(ms) else len(s)]
        if hashlib.sha256(block).hexdigest()!=rows[i]['sha256']: changed_entries.append(names[i])
allowed={'Agostini_v_Felton_merits_1997-06-23.md','City_of_Boerne_v_Flores_merits_1997-06-25.md'}
if set(changed_entries)!=allowed: errors.append('Unexpected changed public entry set: '+str(changed_entries))
for n,order in baseline['render_input_entry_order'].items():
    actual=re.findall(r'<!-- source-record: ([^>]+) -->',(ROOT/n).read_text(encoding='utf-8'))
    if actual!=order: errors.append('term-wide entry order differs: '+n)
record=BASE/'records/Agostini_v_Felton_merits_1997-06-23.md'; s=record.read_text(encoding='utf-8')
assert '**Version / lineage:** Original decision.' in s
pub=s.split('\n## Public Projection\n')[1]
annex=s[:s.index('## Public Projection')]
canonical=annex.split('## Controlling law of the decision\n',1)[1].split('## Precedent treatment and resulting law',1)[0].strip()
public=pub.split('## Holdings\n',1)[1].split('## Precedent Treatment',1)[0].strip()
if canonical!=public: errors.append('Canonical/public Holdings differ')
report={'record':record.relative_to(ROOT).as_posix(),'record_sha256':sha(record),'protected_files_checked':len(protected),'earlier_records_checked':len(earlier),'frozen_handoffs_checked':len(frozen),'record_count':len(current),'public_entries_compared':total,'public_entries_with_authorized_changes':changed_entries,'all_other_entry_bytes_and_all_entry_order_preserved':not errors,'errors':errors}
(BASE/'freeze/OT_1996CHUNK11_AGOSTINI_PACKAGE_CHECKS.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
print(json.dumps(report,indent=2))
raise SystemExit(bool(errors))
