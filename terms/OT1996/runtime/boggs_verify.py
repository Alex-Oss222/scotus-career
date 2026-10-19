"""Deterministic completion checks for the one-event Boggs resumption."""
from pathlib import Path
import hashlib
import json
import re
import unicodedata
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[3]
TERM = ROOT / 'terms/OT1996'
NAME = 'Boggs_v_Boggs_merits_1997-06-02.md'


def digest(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def main():
    errors = []
    baseline = json.loads((ROOT / 'tmp/boggs_resume_baseline.json').read_text(encoding='utf-8'))
    allowed = {'terms/OT1996/workspace/' + n for n in ['manifest.md', 'ledger.md', 'continuity.md', 'neutral-projection.md']}
    changed = []
    for name, expected in baseline.items():
        p = ROOT / name
        if not p.is_file() or digest(p) != expected:
            changed.append(name)
            if name not in allowed:
                errors.append('Protected file changed: ' + name)
    old_records = {Path(n).name for n in baseline if n.startswith('terms/OT1996/records/')}
    records = {p.name for p in (TERM / 'records').glob('*.md')}
    if records - old_records != {NAME} or old_records - records:
        errors.append('Expected exactly one added Record and no removed Record')
    text = (TERM / 'records' / NAME).read_text(encoding='utf-8')
    labels = ['**Case and dockets:**', '**Event and date:**', '**Result:**', '**Version / lineage:**']
    if not all(line.startswith(label) for line, label in zip(text.splitlines()[:4], labels)):
        errors.append('Fixed first-four-line interface failed')
    public = text.split('## Public Projection', 1)[1].strip()
    required = ['Event', 'Participation', 'Public Action', 'Judgment & Remedy', 'Opinion Topology', 'Holdings', 'Precedent Treatment', 'Law After Decision', 'Separate Writings', 'Procedure After Action', 'Source Notes']
    headings = re.findall(r'^## (?:\d+\. )?(.+)$', public, re.M)
    if headings != required:
        errors.append('Public Projection must have exactly eleven ordered blocks')
    if re.search(r'\b(?:user-directed|simulated|commit|Version 2|reconciliation|workflow)\b', public, re.I):
        errors.append('Public Projection may contain private workflow wording')

    def pubblock(name):
        return re.search(r'^## (?:\d+\. )?' + re.escape(name) + r'\s*\n(.*?)(?=^## |\Z)', public, re.M | re.S)[1].strip()

    target = TERM / 'render-inputs/OT_1996CHUNK9.md'
    rin = target.read_text(encoding='utf-8')
    entries = {m[1]: m[2].strip() for m in re.finditer(r'<!-- source-record: ([^>]+) -->\n(.*?)(?=\n---\n|\Z)', rin, re.S)}
    if len(entries) != 11 or rin.count('<!-- source-record:') != 11 or '**Stopped matters:**' in rin:
        errors.append('Chunk 9 must contain eleven unique completed events and no stopped metadata')
    old_input = (ROOT / 'tmp/boggs_chunk9_input_before.md').read_text(encoding='utf-8')
    old_entries = {m[1]: m[2].strip() for m in re.finditer(r'<!-- source-record: ([^>]+) -->\n(.*?)(?=\n---\n|\Z)', old_input, re.S)}
    for name, body in entries.items():
        actual = (TERM / 'records' / name).read_text(encoding='utf-8').split('## Public Projection', 1)[1].strip()
        if body != actual:
            errors.append('Projection drift: ' + name)
    if any(entries.get(name) != body for name, body in old_entries.items()):
        errors.append('Another chunk 9 entry changed')
    if entries.get(NAME) != public:
        errors.append('Boggs projection not identical to its source')

    old_manifest = (ROOT / 'tmp/boggs_manifest_before.md').read_text(encoding='utf-8')
    manifest = (TERM / 'workspace/manifest.md').read_text(encoding='utf-8')
    row_pattern = re.compile(r'^\| \d{4}-\d{2}-\d{2} \| OT_1996CHUNK.+$', re.M)
    old_rows, rows = row_pattern.findall(old_manifest), row_pattern.findall(manifest)
    if len(rows) != 153 or len(old_rows) != len(rows):
        errors.append('Inventory row count changed')
    altered = []
    for old, new in zip(old_rows, rows):
        if old == new:
            continue
        altered.append(new)
        a, b = old.split('|'), new.split('|')
        if '| Boggs v. Boggs |' not in old or a[:7] != b[:7] or a[8:] != b[8:] or 'Completed: ' + NAME not in b[7]:
            errors.append('Unexpected manifest inventory edit')
    if len(altered) != 1:
        errors.append('Expected exactly the Boggs manifest status change')
    for name in ['Gaydos', 'Vey', 'Bryan County']:
        if name not in manifest:
            errors.append('Missing existing open procedure: ' + name)
    for filename in ['continuity.md', 'neutral-projection.md']:
        doc = (TERM / 'workspace' / filename).read_text(encoding='utf-8')
        if '106 Court events and 3 admitted sources' not in doc:
            errors.append(filename + ': incorrect event count')
        for name in ['Opinion Topology', 'Holdings', 'Precedent Treatment', 'Law After Decision', 'Separate Writings', 'Procedure After Action']:
            if pubblock(name) not in doc:
                errors.append(filename + ': missing exact public block ' + name)
        if '| Boggs v. Boggs |' in doc or re.search(r'^.*Boggs.*Stopped:', doc, re.M):
            errors.append(filename + ': stale pending Boggs row')

    def anchors(s):
        result = set()
        for h in re.findall(r'^#{1,6} (.+)$', s, re.M):
            h = h.strip().lower()
            h = ''.join(c for c in h if not unicodedata.category(c).startswith('P') or c in '-_')
            result.add(h.replace(' ', '-'))
        return result | set(re.findall(r'<a\s+(?:name|id)=[\"\x27]([^\"\x27]+)', s))
    paths = [TERM / 'records' / NAME, TERM / 'freeze/OT_1996CHUNK9_102_DEPENDENCY_REVIEW.md', TERM / 'freeze/OT_1996CHUNK9_102_RESUMPTION_VALIDATION.md']
    checked_links = 0
    for p in paths:
        if not p.exists():
            errors.append('Missing validation artifact: ' + p.name)
            continue
        for raw in re.findall(r'\]\(([^)]+)\)', p.read_text(encoding='utf-8')):
            if re.match(r'\w+://', raw):
                continue
            address, _, anchor = unquote(raw.strip('<>')).partition('#')
            q = (p.parent / address).resolve() if address else p
            if ROOT / 'stone' in [q, *q.parents]:
                errors.append('Forbidden directory link: ' + raw)
                continue
            checked_links += 1
            if not q.exists():
                errors.append('Broken local link from ' + p.name + ': ' + raw)
            elif anchor and q.is_file() and q.suffix == '.md' and anchor not in anchors(q.read_text(encoding='utf-8')):
                errors.append('Missing anchor from ' + p.name + ': ' + raw)
    result = {'status': 'passed' if not errors else 'failed', 'protected_files_checked': len(baseline), 'changed_existing_baseline_files': changed, 'unchanged_prior_records': len(old_records), 'added_record': NAME, 'total_records': len(records), 'inventory_events': len(rows), 'chunk9_events': len(entries), 'unchanged_other_chunk9_projections': len(old_entries), 'local_links_checked': checked_links, 'errors': errors, 'git_commands_executed': 0, 'git_verification': 'Deferred to operator under explicit instruction; no existence claim.'}
    path = TERM / 'freeze/OT_1996CHUNK9_102_RESUMPTION_INTEGRITY.json'
    path.write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
    print(json.dumps(result, indent=2))
    if errors:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
