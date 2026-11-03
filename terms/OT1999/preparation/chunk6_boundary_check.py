from pathlib import Path
import json,re,hashlib
root=Path(__file__).resolve().parents[3];term=root/'terms/OT1999'
baseline=json.loads((term/'freeze/OT_1999CHUNK6_BASELINE_HASHES.json').read_text(encoding='utf-8'))
changed=[name for name,digest in baseline.items() if not (root/name).exists() or hashlib.sha256((root/name).read_bytes()).hexdigest()!=digest]
files=[]
for sub in ['freeze','preparation','entering-law','runtime']:
 files += [p for p in (term/sub).glob('*') if p.is_file() and ('chunk6' in p.name.lower() or 'chunk_6' in p.name.lower())]
for directory in (term/'sources').glob('chunk6*'):
 if directory.is_dir():files += list(directory.rglob('*'))
files += [p for p in (term/'workspace').glob('*.md')]
files += [p for p in (term/'tmp').glob('*CHUNK6*') if p.is_file()]
files += [p for p in (term/'records').glob('*.md') if p.relative_to(root).as_posix() not in baseline]
files += [p for p in (term/'render-inputs').glob('*CHUNK6.md')]
bad=[]
for p in files:
 if not p.is_file() or p.suffix not in ['.txt','.md','.html','.json','.py']:continue
 t=p.read_text(encoding='utf-8',errors='replace')
 urls=re.findall(r'(?:https?://|www\.)[^\s<>"\x27]+',t,re.I)
 if any(any(host in u.lower() for host in ['github.com','onedrive','1drv.ms']) for u in urls):bad.append(p.relative_to(root).as_posix())
 if re.search(r'\]\((?:file://|[A-Za-z]:[/\\])',t):bad.append(p.relative_to(root).as_posix()+' (machine hyperlink)')
result={'protected_baseline_files':len(baseline),'protected_files_changed':changed,'new_text_artifacts_scanned':len(files),'forbidden_links':bad,'scope':'Explicit authorized roots only; no locked-directory or Git access.'}
(term/'freeze/OT_1999CHUNK6_BOUNDARY_CHECK.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,indent=2))
raise SystemExit(bool(changed or bad))
