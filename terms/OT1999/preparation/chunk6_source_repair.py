from pathlib import Path
import json
folder=Path('terms/OT1999/sources/chunk6-neutral')
for p in folder.glob('grazing-*.pdf'):
 data=p.read_bytes()
 if data.startswith(b'%PDF-'):continue
 assert data.lstrip().startswith(b'<!DOCTYPE html>')
 # Retain the failed server response with its truthful type; remove only this Run's mistaken derivative.
 failed=p.with_name(p.stem+'-failed-response.html');failed.write_bytes(data)
 p.unlink()
 derivative=p.with_suffix('.txt')
 if derivative.exists():derivative.unlink()
 metadata=p.with_name(p.stem+'-source.json')
 obj=json.loads(metadata.read_text(encoding='utf-8'))
 obj['status']='Failed retrieval: server returned HTML Page Not Found, not a PDF or regulation. Not substantive authority.'
 obj.pop('pages',None)
 obj['replacement']='grazing-final-rule.txt (official February 22, 1995 final rule, FR Doc 95-3866)'
 metadata.write_text(json.dumps(obj,indent=2)+'\n',encoding='utf-8')
lines=Path('terms/OT1999/sources/chunk6-comparator/johnson-529us694.txt').read_text(encoding='utf-8').splitlines()
header=next(l for l in lines[:20] if l.startswith('Argued'))
Path('terms/OT1999/entering-law/OT_1999CHUNK6_JOHNSON_DATE.md').write_text('# Johnson scheduling fact\n\nThe following header is mechanically copied from the official report, page 694. No disposition or reasoning is included.\n\n'+header+'\n\nSource: https://www.govinfo.gov/content/pkg/USREPORTS-529/pdf/USREPORTS-529-694.pdf\n',encoding='utf-8')
print('Reclassified five failed grazing responses; official final rule replaces them. Johnson header copied.')
