"""Check file targets of new Record/receipt links without probing locked paths."""
from pathlib import Path
from urllib.parse import unquote
import json
import re

TERM = Path(__file__).resolve().parents[1]
names = ['Vera_and_consolidated_merits_1996-06-13.md', 'Montana_v_Egelhoff_merits_1996-06-13.md', 'Leavitt_v_Jane_L_summary_merits_1996-06-17.md']
files = [TERM / 'records' / name for name in names]
files += sorted((TERM / 'freeze').glob('OT_1995CHUNK8_*REVISION_ASSEMBLY.md'))
missing, checked, excluded = [], 0, 0
for path in files:
    if not path.exists():
        missing.append({'file': str(path.relative_to(TERM)), 'target': 'FILE ITSELF MISSING'})
        continue
    for target in re.findall(r'\]\(([^)]+)\)', path.read_text(encoding='utf-8')):
        if target.startswith(('http:', 'https:', '#', 'mailto:')): continue
        literal = unquote(target.split('#', 1)[0].strip('<>'))
        # Do not resolve, test existence or otherwise inspect a locked-directory link.
        if 'stone' in [piece.casefold() for piece in literal.replace('\\', '/').split('/')]:
            excluded += 1
            continue
        if not literal: continue
        checked += 1
        candidate = path.parent / literal
        if not candidate.exists(): missing.append({'file': str(path.relative_to(TERM)), 'target': target})
receipt = {'checked_file_targets': checked, 'locked_path_targets_not_inspected': excluded, 'missing': missing,
           'scope': 'File targets in three new Records and revision assembly receipts; external URLs and anchors not fetched.'}
(TERM / 'freeze/OT_1995CHUNK8_REVISION_LINK_CHECK.json').write_text(json.dumps(receipt, indent=2)+'\n', encoding='utf-8')
print(json.dumps(receipt, indent=2))
if missing: raise SystemExit(1)
