"""Clerical validation of chunk-one Record interfaces and arithmetic; no legal decisions."""
from pathlib import Path
import json
import re
import sys
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[3]
TERM = ROOT / 'terms/OT1995'
ROSTER = {'Stone-Zsela', 'Stevens', "O'Connor", 'Scalia', 'Kennedy', 'Souter', 'Thomas', 'Ginsburg', 'Breyer'}
HEADINGS = ['Event', 'Participation', 'Public Action', 'Judgment & Remedy', 'Opinion Topology', 'Holdings', 'Precedent Treatment', 'Law After Decision', 'Separate Writings', 'Procedure After Action', 'Source Notes']
LABELS = ['**Case and dockets:**', '**Event and date:**', '**Result:**', '**Version / lineage:**']
errors = []
checked = []
draft_mode = '--draft' in sys.argv
for meta in sorted((TERM / 'runtime/assembly').glob('*.json')):
    data = json.loads(meta.read_text(encoding='utf-8'))
    if not isinstance(data, dict) or 'record' not in data:
        continue
    if meta.stem + '.md' != data['record']:
        continue  # A review receipt can name a Record without being its companion.
    name = data['record']
    record = TERM / ('runtime/assembly' if draft_mode else 'records') / name
    if not record.exists():
        continue  # Drafts and blocked matters are not canonical events.
    text = record.read_text(encoding='utf-8')
    lines = text.splitlines()
    if any(not lines[i].startswith(label) for i, label in enumerate(LABELS)):
        errors.append(f'{name}: four opening labels not exact first four lines')
    if data['date'] not in lines[1]:
        errors.append(f'{name}: metadata date differs from event label')
    if set(data['participants']) != ROSTER or len(data['participants']) != 9:
        errors.append(f'{name}: roster mismatch')
    for component in data['judgments']:
        support = component['support']
        oppose = component['oppose']
        other = component.get('other', [])
        other_names = [x['justice'] if isinstance(x, dict) else x for x in other]
        votes = support + oppose + other_names
        if set(votes) != ROSTER or len(votes) != 9:
            errors.append(f'{name}: judgment {component["component"]} omits or duplicates a participant')
        tally = component.get('printed_tally', component.get('tally', ''))
        expected = f'{len(support)}-{len(oppose)}'
        if not other and tally.replace('–', '-').replace('—', '-') != expected:
            errors.append(f'{name}: tally {tally!r} != {expected}')
    for writing in data['writings']:
        author = writing['author']
        joined = writing.get('joiners', [])
        if author not in ROSTER and author not in ['Per curiam', 'per curiam']:
            errors.append(f'{name}: unknown author {author}')
        if len(joined) != len(set(joined)) or not set(joined) <= ROSTER:
            errors.append(f'{name}: invalid joins')
        if author in joined:
            errors.append(f'{name}: author repeated as joiner')
        count = len(joined) + (author in ROSTER)
        if writing.get('controlling') and count < 5:
            errors.append(f'{name}: purported direct controlling writing has only {count} joins')
    if '## Public Projection' not in text:
        errors.append(f'{name}: no Public Projection')
        continue
    private, public = text.split('## Public Projection', 1)
    actual = re.findall(r'^## (.+?)\s*$', public, re.M)
    if actual != HEADINGS:
        errors.append(f'{name}: public headings differ: {actual}')
    for forbidden in ['user-directed', 'research cutoff', 'approval status', 'Version / lineage', 'modeling context', 'single-conversation', 'simulated', 'historical comparator', 'operator commit', 'frozen commitment']:
        if forbidden.casefold() in public.casefold():
            errors.append(f'{name}: public workflow phrase {forbidden}')
    if not re.search(r'research cutoff', private, re.I):
        errors.append(f'{name}: internal research cutoff missing')
    holdings = re.search(r'^## Holdings\s*\n(.*?)(?=^## Precedent Treatment\s*$)', public, re.M | re.S)
    if holdings and holdings.group(1).strip() not in private:
        errors.append(f'{name}: public Holdings are not an unchanged copy of the internal controlling holdings')
    for dest in re.findall(r'\]\(([^)]+)\)', text):
        if dest.startswith(('http:', 'https:', '#')):
            continue
        dest = unquote(dest.strip('<>').split('#', 1)[0])
        if not dest:
            continue
        # Drafts already use their eventual canonical-record relative links.
        target = (TERM / 'records' / dest).resolve()
        try:
            relative = target.relative_to(ROOT)
        except ValueError:
            errors.append(f'{name}: local link outside repository {dest}')
            continue
        if relative.parts[0].casefold() == 'stone':
            errors.append(f'{name}: forbidden locked-directory link (not followed)')
            continue
        if not target.exists():
            errors.append(f'{name}: unresolved local file link {dest}')
    checked.append(name)

canonical = set(checked) if draft_mode else {p.name for p in (TERM / 'records').glob('*.md') if not p.name.startswith('.')}
if canonical != set(checked):
    errors.append('Canonical Records lacking checked arithmetic metadata: ' + ', '.join(sorted(canonical - set(checked))))
result = {'checked_records': checked, 'errors': errors, 'git': 'not invoked; operator verification pending'}
out_name = 'OT_1995CHUNK1_DRAFT_CLERICAL_CHECK.json' if draft_mode else 'OT_1995CHUNK1_CLERICAL_CHECK.json'
(TERM / 'freeze' / out_name).write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
print(json.dumps({'checked': len(checked), 'errors': errors}, ensure_ascii=False))
raise SystemExit(1 if errors else 0)
