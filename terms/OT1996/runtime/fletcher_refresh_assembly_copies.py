"""Refresh bounded assembly source copies from canonical OT1996 Records."""
from pathlib import Path
import hashlib
import importlib.util
import json
import re
import sys

sys.dontwritebytecode = True
TERM = Path(__file__).resolve().parents[1]
FREEZE = TERM / 'freeze'
TARGET = 'Fletcher_v_Kalina_merits_1997-06-16.md'


def dump(path, value):
    data = json.dumps(value, ensure_ascii=False, indent=2) + '\n'
    if path.read_text(encoding='utf-8-sig') != data:
        path.write_text(data, encoding='utf-8', newline='\n')


def main():
    spec = importlib.util.spec_from_file_location('fletcher_census', TERM / 'runtime/fletcher_downstream_audit.py')
    audit = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(audit)
    rows, _ = audit.census()
    by_name = {r['file']: r for r in rows}
    assert by_name[TARGET]['authors'] == ['Stevens']
    texts = {r['file']: (TERM / 'records' / r['file']).read_text(encoding='utf-8-sig') for r in rows}

    def topology(name):
        public = texts[name].split('## Public Projection', 1)[1]
        return re.search(r'^## Opinion Topology\s*\n(.*?)(?=^## |\Z)', public, re.M | re.S)[1].strip()

    def evidence(row):
        top = topology(row['file'])
        lines = []
        for line in top.splitlines():
            cells = [v.strip() for v in line.strip('|').split('|')]
            if line.startswith('|') and len(cells) > 1 and audit.normalized(cells[1]) in row['authors']:
                if re.match(r'Opinion of the Court|Court opinion|Same opinion|Lead opinion|Opinion announcing', cells[0], re.I):
                    lines.append(line)
        if not lines:
            lines = [line for line in top.splitlines() if re.search(r'\b(?:delivers|writes)\b', line)]
        assert lines, row['file']
        return {'record': row['file'], 'case': row['case'], 'date': row['date'],
                'authors': row['authors'], 'author_evidence': lines,
                'topology_sha256': hashlib.sha256(top.encode()).hexdigest()}

    for path in sorted(FREEZE.glob('OT_1996CHUNK11_ASSIGNMENT*.json')):
        if path.name in ('OT_1996CHUNK11_ASSIGNMENT_FLETCHER.json', 'OT_1996CHUNK11_ASSIGNMENT_SOURCES_FLETCHER.json'):
            continue
        data = json.loads(path.read_text(encoding='utf-8-sig'))
        if isinstance(data, list):
            for item in data:
                name = item.get('record') if isinstance(item, dict) else None
                if name not in by_name or by_name[name]['date'] < '1997-06-16':
                    continue
                if 'opinion_topology' not in item:
                    continue
                item['headers'] = texts[name].splitlines()[:4]
                item['opinion_topology'] = topology(name)
                if 'assignment_sections' in item:
                    try:
                        _, _, section = audit.assignment_segment(texts[name].split('## Public Projection', 1)[0])
                        item['assignment_sections'] = [section.strip()]
                    except RuntimeError:
                        section = re.search(r'^## Opinion form and assignment\s*\n.*?(?=^## |\Z)', texts[name].split('## Public Projection', 1)[0], re.M | re.S)
                        if section:
                            item['assignment_sections'] = [section[0].strip()]
            dump(path, data)
        elif isinstance(data, dict) and 'target_event_date' in data and 'target_case_name' in data:
            matches = [r for r in rows if r['date'] == data['target_event_date'] and
                       audit.normalized(r['case']).casefold() == audit.normalized(data['target_case_name']).casefold()]
            assert len(matches) == 1, (path.name, data['target_case_name'])
            target = matches[0]
            selected = rows[:rows.index(target)]
            counted = [evidence(r) for r in selected if r['counted']]
            data['counts'] = target['counts_before']
            data['qualifying_opinions'] = target['opinions_before']
            data['last_counted'] = counted[-1] if counted else None
            data['counted'] = counted
            dump(path, data)

    # The entering-law copies contain only the current Public Projection.
    text = texts[TARGET]
    case = re.search(r'^\*\*Case and dockets:\*\*\s*(.+)', text, re.M)[1].strip()
    public = text.split('## Public Projection', 1)[1].strip()
    replacement = '# 1997-06-16 — ' + case + '\n\nAuthority: [Record](../records/' + TARGET + ').\n\n' + public + '\n\n---\n\n'
    for path in (TERM / 'entering-law').glob('OT_1996CHUNK11_BEFORE_*.md'):
        data = path.read_text(encoding='utf-8-sig')
        pattern = r'^# 1997-06-16 — Fletcher v\. Kalina[^\n]*\n.*?(?=^# \d{4}-\d\d-\d\d — |\Z)'
        data, n = re.subn(pattern, lambda _: replacement, data, flags=re.M | re.S)
        assert n == 1, path.name
        path.write_text(data, encoding='utf-8', newline='\n')

    # Refresh the exact canonical-file fingerprints in assembly/law receipts.
    for path in FREEZE.glob('OT_1996CHUNK11_LAW_REFRESH_*.json'):
        data = json.loads(path.read_text(encoding='utf-8-sig'))
        for name in data:
            source = TERM / 'records' / name
            if source.exists():
                data[name] = hashlib.sha256(source.read_bytes()).hexdigest()
        dump(path, data)

    path = FREEZE / 'OT_1996CHUNK11_FINAL_ASSIGNMENT_RECONCILIATION.json'
    data = json.loads(path.read_text(encoding='utf-8-sig'))
    for item in data['results']:
        row = by_name[item['record']]
        item['author'] = row['authors']
        item['counts_before'] = row['counts_before']
    dump(path, data)
    print('Refreshed assembly assignment copies, count receipts and Fletcher entering-law projections.')


if __name__ == '__main__':
    main()
