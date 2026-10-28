from pathlib import Path
import fitz,json,hashlib
ROOT=Path(__file__).resolve().parent
d=fitz.open(ROOT/'official-526.pdf')
cases=[('unum',358,379),('haggar',380,397),('sun-diamond',398,414),('aguirre',415,433),('lasalle',434,472),('el-paso',473,488),('saenz',489,528)]
for name,start,end in cases:
    out=[]
    for p in range(start+111,end+112): out.append(d[p-1].get_text())
    (ROOT/(name+'-official.txt')).write_text('\n'.join(out),encoding='utf-8')
checks=[]
for p in sorted(ROOT.iterdir()):
    if p.suffix in ('.pdf','.html','.txt','.json') and p.name != 'checksums.json':
        checks.append({'file':p.name,'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()})
(ROOT/'checksums.json').write_text(json.dumps(checks,indent=2),encoding='utf-8')
print('Extracted official case text slices; checksums for',len(checks),'source files')
