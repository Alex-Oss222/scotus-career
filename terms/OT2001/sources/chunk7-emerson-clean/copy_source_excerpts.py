from pathlib import Path
import re
base = Path(__file__).parent
root = Path(__file__).resolve().parents[4]
source = (base / 'fifth_circuit.txt').read_text(encoding='utf-8')
pages = source.split('--- PDF page ')
parts = ['# Mechanical primary-source extracts', '', 'Each page below is copied from the saved text extraction of the official Fifth Circuit opinion; page numbers identify PDF pages.', '']
for i in [2,3,4,6,14,15,105,106,107,108,109,110,123,124]:
    parts += ['--- PDF page '+pages[i], '']
(base / 'record_extracts.md').write_text('\n'.join(parts), encoding='utf-8')

projection = (root / 'terms/OT2001/workspace/neutral-projection.md').read_text(encoding='utf-8')
selected = ['# Effective current-term public-law supplements', '', 'Mechanical copy from the sanitized current-term neutral projection. No uncoordinated June 17 event enters the June 17 baseline.', '']
for name in ['United States v. Faasse', 'United States v. Farmer']:
    match = re.search(r'^### '+re.escape(name)+r'[^\n]*\n', projection, re.M)
    assert match
    end = re.search(r'^### ',projection[match.end():],re.M)
    bound=match.end()+end.start() if end else len(projection)
    selected += [projection[match.start():bound].strip(),'']
(base / 'current_public_law_copy.md').write_text('\n'.join(selected),encoding='utf-8')
print('Source passages and current public law copied mechanically.')
