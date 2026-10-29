#!/usr/bin/env python3
"""Mechanical Chunk10 workspace integration; no adjudication or Git access.

Run with python -B. By default, capture all new Record paths at invocation.
Optional --records NAME [NAME ...] fixes the captured set explicitly. Repeat
--stopped CASE=BLOCKER for unresolved Chunk10 matters without a Record. The
freshness file supplies the baseline; immutable opening projections supply all
prior content. Only identity labels, the eleven Public Projection blocks, and
the bounded published-noncontrolling-position section are retained from Records.
"""
from __future__ import annotations
import argparse
from datetime import date
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import sys

sys.dont_write_bytecode = True
ROOT = Path(__file__).absolute().parents[3]
TERM = ROOT / 'terms/OT1998'
BLOCKS = ('Event', 'Participation', 'Public Action', 'Judgment & Remedy',
          'Opinion Topology', 'Holdings', 'Precedent Treatment',
          'Law After Decision', 'Separate Writings', 'Procedure After Action',
          'Source Notes')
LABELS = ('Case and dockets', 'Event and date', 'Result', 'Version / lineage')
FRESH = TERM / 'freeze/OT_1998CHUNK10_SOURCE_FRESHNESS.json'
ADAPTER = TERM / 'audit/ot1998_chunk10_rebuild_manifest.py'
RECEIPT = TERM / 'audit/OT_1998CHUNK10_WORKSPACE_INTEGRATION.json'
CHUNK = 'OT_1998CHUNK10'
DYSON_COMPONENTS = {
    'maryland_v_dyson_certiorari_1999-06-21.md': 'Certiorari grant',
    'maryland_v_dyson_summary_merits_1999-06-21.md': 'Summary merits decision',
}
DYSON_TERMINAL = 'maryland_v_dyson_summary_merits_1999-06-21.md'
ACKER_PUBLIC_BLOCKER = ('Required remedy revalidation concerning the separate '
                        'unreviewed Compensation Clause remains incomplete; '
                        'no completed Court event is supplied.')
DATE = re.compile(r'\b\d{4}-\d{2}-\d{2}\b')
BOUNDARY = ('Uncoordinated June 14, June 17, June 21 and June 22 matters each use '
            'the common law effective before that entire date group. June 14 crosses '
            'chunks 9 and 10; June 22 crosses chunks 10 and 11. Sutton supplies no '
            'entering law to its uncoordinated June 22 chunk 11 peers. Later dates '
            'receive every effective earlier holding; a scheduled date supplies no '
            'future Court action or law.')


def read(path):
    raw = path.read_bytes().decode('utf-8')
    newline = '\r\n' if '\r\n' in raw else '\n'
    return raw.replace('\r\n', '\n'), newline


def write(path, text, newline='\n'):
    allowed = {TERM/'workspace/continuity.md', TERM/'workspace/neutral-projection.md',
               TERM/'workspace/manifest.md', RECEIPT}
    assert path in allowed or (path.parent == TERM/'entering-law' and path.name in captured_names)
    path.write_bytes(text.replace('\n', newline).encode('utf-8'))


def cells(line):
    return [x.strip() for x in line.strip().strip('|').split('|')]


def inventory(text):
    return [cells(l) for l in text.splitlines()
            if l.startswith('| ') and len(cells(l)) == 12 and DATE.fullmatch(cells(l)[0])]


def rows_by_key(text):
    return {(r[0], r[1], r[2], r[3]): (r, l)
            for l in text.splitlines() if l.startswith('| ')
            for r in [cells(l)] if len(r) == 12 and DATE.fullmatch(r[0])}


def docket(text):
    return set(re.findall(r'\b\d{1,3}-\d{1,5}\b', text))


def case_key(text):
    return re.sub(r'\s+', ' ', text.casefold().replace('+', ' ').replace(' / ', '; ')).strip(' ;,.')


def group_records(records):
    grouped = {}
    for record in records:
        grouped.setdefault(record['key'], []).append(record)
    for group in grouped.values():
        names = {r['name'] for r in group}
        if names & DYSON_COMPONENTS.keys():
            assert names == set(DYSON_COMPONENTS), 'Dyson requires both finalized dated component Records before integration'
        elif len(group) > 1:
            raise AssertionError('Unspecified multi-component inventory row requires component review')
        for record in group:
            component = DYSON_COMPONENTS.get(record['name'])
            record['display_caption'] = record['caption'] + (' — ' + component if component else '')
    return grouped


def parse_stopped(values, old_rows, grouped):
    stopped = {}
    for value in values:
        assert '=' in value, '--stopped requires CASE=exact blocker'
        name, blocker = value.split('=', 1)
        assert name.strip() and blocker.strip() and not any(c in blocker for c in '\r\n|'), 'stopped blocker must be a nonempty single-line table-safe value'
        candidates = [(key, row) for key, (row, _) in old_rows.items()
                      if row[1] == CHUNK and case_key(row[2]) == case_key(name)]
        assert len(candidates) == 1, f'--stopped must identify one Chunk10 row: {name}'
        key, row = candidates[0]
        assert key not in stopped and key not in grouped, f'stopped and completed states conflict: {name}'
        assert not row[6].startswith(('Completed:', 'Reconciled:')), f'cannot stop a completed opening row: {name}'
        public = ACKER_PUBLIC_BLOCKER if case_key(row[2]) == case_key('Jefferson County v. Acker') else 'Required event-specific revalidation remains incomplete; no completed Court event is supplied.'
        stopped[key] = {'caption': row[2].removesuffix(' +'), 'date': row[0],
                        'blocker': blocker, 'public_blocker': public}
    return stopped


def schedule_cursor(unresolved):
    pending = [r for r in unresolved if r[1] in (CHUNK, 'OT_1998CHUNK11')]
    stopped = [r for r in pending if r[6].startswith('Stopped:')]
    runnable = [r for r in pending if not r[6].startswith(('Stopped:', 'Carry forward:'))]
    backlog = ('Stopped backlog: ' + '; '.join(r[2].removesuffix(' +') + ' (' + r[0] + ')' for r in stopped)
               + '. These matters remain unresolved and do not supply completed Court events. ') if stopped else ''
    if runnable:
        r = runnable[0]
        day = date.fromisoformat(r[0])
        next_event = (f"The next runnable scheduled inventory event is {r[2].removesuffix(' +')}, {r[3]}, "
                      f"on {day.strftime('%B')} {day.day}, {day.year}, in {r[1]}.")
    else:
        next_event = 'No runnable uncompleted scheduled inventory event remains in chunks 10 and 11; unresolved matters retain their recorded conditions.'
    return backlog + next_event


def read_record(path):
    identity, public, positions = {}, [], []
    mode = None
    marker_count = 0
    # Only permitted segments are retained or interpreted. Private sections are skipped.
    with path.open(encoding='utf-8', newline='') as stream:
        for raw in stream:
            line = raw.replace('\r\n', '\n')
            if mode != 'public':
                for label in LABELS:
                    prefix = f'**{label}:**'
                    if line.startswith(prefix):
                        assert label not in identity, f'duplicate identity: {path.name}: {label}'
                        identity[label] = line[len(prefix):].strip()
            if line.rstrip('\n') == '## Public Projection':
                marker_count += 1
                mode = 'public'
                continue
            if mode == 'public':
                public.append(line)
                continue
            if line.startswith('## '):
                mode = 'positions' if line.rstrip('\n') == '## Material Published Noncontrolling Positions' else None
                continue
            if mode == 'positions':
                positions.append(line)
    assert marker_count == 1 and set(identity) == set(LABELS), f'incomplete Record: {path.name}'
    public = ''.join(public).strip() + '\n'
    headings = re.findall(r'^## (.+)$', public, re.M)
    assert headings == list(BLOCKS), f'Public Projection blocks: {path.name}: {headings}'
    blocks = {}
    for match in re.finditer(r'^## ([^\n]+)\n(.*?)(?=^## |\Z)', public, re.M | re.S):
        blocks[match.group(1)] = match.group(2).strip()
    assert all(blocks.values()), f'empty Public Projection block: {path.name}'
    event_date = DATE.search(identity['Event and date'])
    assert event_date, f'missing effective date: {path.name}'
    return {'name': path.name, 'identity': identity, 'date': event_date.group(),
            'public': public, 'blocks': blocks, 'positions': ''.join(positions).strip()}


def append_section(text, heading, addition):
    marker = heading + '\n'
    assert text.count(marker) == 1, heading
    start = text.index(marker) + len(marker)
    end = text.find('\n## ', start)
    if end < 0:
        end = len(text)
    return text[:end].rstrip('\n') + '\n\n' + addition.rstrip('\n') + '\n\n' + text[end:].lstrip('\n')


def rebase(body):
    return re.sub(r'^(#{1,6})(?= )', lambda m: '#' * min(6, len(m[1])+2), body, flags=re.M)


def section_entry(record, parts, neutral=False):
    title = f"### {record['display_caption']} — {record['date']}\n\n"
    body = '\n\n'.join('#### ' + name + '\n\n' + rebase(value) for name, value in parts)
    directory = 'entering-law' if neutral else 'records'
    return title + body + f"\n\n[Authority and public scope](../{directory}/{record['name']}).\n"


def positions_entry(record, neutral=False):
    parts = []
    if record['positions']:
        parts.append(('Material Published Noncontrolling Positions', record['positions']))
    if record['blocks']['Separate Writings'] != record['positions']:
        parts.append(('Separate Writings', record['blocks']['Separate Writings']))
    result = section_entry(record, parts, neutral)
    if neutral and record['positions']:
        result += f"\n[Published positions retained for continuity](../records/{record['name']}#material-published-noncontrolling-positions).\n"
    return result


def insert_event_rows(text, records, neutral=False):
    lines = text.splitlines(keepends=True)
    heading = '## Completed current-term events' if neutral else '## Completed Events and Admitted Sources'
    start = next(i for i, l in enumerate(lines) if l.rstrip('\n') == heading)
    header = next(i for i in range(start, len(lines)) if lines[i].startswith('| Effective date |'))
    end = header + 2
    while end < len(lines) and lines[end].startswith('|'):
        end += 1
    directory, link = ('entering-law', 'public copy') if neutral else ('records', 'record')
    added = []
    for r in records:
        action = re.sub(r'\s+', ' ', r['blocks']['Public Action']).replace('|', '&#124;')
        added.append(f"| {r['date']} | {r['display_caption']} | {action} | [{link}](../{directory}/{r['name']}) |\n")
    lines[end:end] = added
    return ''.join(lines)


def replace_metadata(text, status, latest, next_event):
    text = re.sub(r'109 current-term Court events completed, with the latest dated 1999-06-14\. 21 scheduled items remain unresolved, plus 13 undated carryovers: 34 unresolved inventory items in total\. One nonjudicial source event is admitted separately\. Del Monte Dunes is reconciled without a new Court event\. Records control\.', status, text)
    text = text.replace('Current public law and procedure through 1999-06-14.', f'Current public law and procedure through {latest}.')
    text = text.replace('The latest completed-event date is **1999-06-14**', f'The latest completed-event date is **{latest}**')
    old_cursor = ('The next scheduled inventory event is West v. Gibson, No. 98-238, on June 14, 1999, in OT_1998CHUNK10. '
                  'It shares the pre-June-14 entering-law baseline with the uncoordinated June 14 matters in chunk 9.')
    text = text.replace(old_cursor, next_event + ' ' + BOUNDARY)
    text = text.replace('Current public law is complete through May 24, 1999.', f'Current public law includes the finalized events through {latest}; unresolved scheduled and carried matters remain open.')
    text = text.replace('Current public law extends through 1999-06-14,', f'Current public law extends through {latest},')
    return text


def preserved_sections(before, after):
    """Every original top-level section survives in order, modulo explicit cursor edits."""
    headings = re.findall(r'^## .+$', before, re.M)
    assert re.findall(r'^## .+$', after, re.M) == headings
    for heading in headings:
        def body(text):
            start = text.index(heading + '\n')
            end = text.find('\n## ', start + len(heading))
            return text[start:end if end >= 0 else len(text)].rstrip('\n')
        assert body(before) in body(after), f'prior section changed: {heading}'
    return headings


ap = argparse.ArgumentParser(description=__doc__)
ap.add_argument('--records', nargs='+', help='exact new finalized Record basenames for this invocation')
ap.add_argument('--stopped', action='append', default=[], metavar='CASE=BLOCKER', help='exact blocker for an unresolved Chunk10 row without a Record')
args = ap.parse_args()
freshness = json.loads(FRESH.read_text())
baseline = {x['path'] for x in freshness['files']}
new_at_start = sorted(p.name for p in (TERM/'records').glob('*.md')
                      if str(p.relative_to(ROOT)) not in baseline)
captured_names = sorted(args.records if args.records is not None else new_at_start)
assert captured_names and len(set(captured_names)) == len(captured_names)
assert all(Path(n).name == n and n in new_at_start for n in captured_names), 'capture includes a non-new Record'
opening = {}
newlines = {}
for key in ['CONTINUITY', 'NEUTRAL_PROJECTION', 'MANIFEST']:
    opening[key], newlines[key] = read(TERM/f'freeze/OT_1998CHUNK10_OPENING_{key}.md')
old_rows = rows_by_key(opening['MANIFEST'])
records = [read_record(TERM/'records'/n) for n in captured_names]
for r in records:
    candidates = [(key, row) for key, (row, _) in old_rows.items()
                  if row[0] == r['date'] and row[1] == CHUNK
                  and docket(row[3]) & docket(r['identity']['Case and dockets'])]
    assert len(candidates) == 1, f'nonunique Chunk10 identity: {r["name"]}'
    r['key'], r['row'] = candidates[0]
    r['caption'] = r['row'][2].removesuffix(' +')
by_key = group_records(records)
stopped = parse_stopped(args.stopped, old_rows, by_key)
touched_keys = set(by_key) | set(stopped)
order = {key: n for n, key in enumerate(old_rows)}
records.sort(key=lambda r: (order[r['key']], r['name'] == DYSON_TERMINAL, r['name']))

# Canonical status builder is always executed through the inspected adapter.
# Restore uncaptured rows below if another assembler finalizes a Record meanwhile.
write(TERM/'workspace/manifest.md', opening['MANIFEST'], newlines['MANIFEST'])
adapter_args = [argument for value in args.stopped for argument in ('--stopped', value)]
result = subprocess.run([sys.executable, '-B', str(ADAPTER), *adapter_args], cwd=ROOT,
                        env={**os.environ, 'PYTHONDONTWRITEBYTECODE': '1'},
                        check=True, text=True, capture_output=True)
canonical, _ = read(TERM/'workspace/manifest.md')
canonical_rows = rows_by_key(canonical)
manifest_lines = []
for line in opening['MANIFEST'].splitlines(keepends=True):
    row = cells(line) if line.startswith('| ') else []
    key = tuple(row[:4]) if len(row) == 12 else None
    if key in by_key:
        components = by_key[key]
        built = canonical_rows[key][0]
        canonical_names = built[6].removeprefix('Completed: ').split(', ')
        expected_names = {r['name'] for r in components}
        assert built[6].startswith('Completed: ') and len(canonical_names) == len(expected_names) and set(canonical_names) == expected_names, f'canonical component status mismatch: {row[2]}'
        terminal = next((r for r in components if r['name'] == DYSON_TERMINAL), components[0])
        row[6] = built[6]
        row[7] = f"Completed Court event{'s' if len(components) > 1 else ''}; [operative procedure](../records/{terminal['name']}#procedure-after-action)."
        row[10] = f"Completed inventory matter; [canonical procedure and continuing conditions](../records/{terminal['name']}#procedure-after-action) and [source limits](../records/{terminal['name']}#source-notes). No unresolved Chunk10 assembly blocker."
        row[11] = '; '.join(f"[{DYSON_COMPONENTS.get(r['name'], 'Record')}](../records/{r['name']})" for r in sorted(components, key=lambda r: (r['name'] == DYSON_TERMINAL, r['name'])))
        line = '| ' + ' | '.join(row) + ' |\n'
    elif key in stopped:
        blocker = stopped[key]['blocker']
        assert canonical_rows[key][0][6] == 'Stopped: ' + blocker, f'canonical stopped status mismatch: {row[2]}'
        row[6] = canonical_rows[key][0][6]
        row[7] = 'Stopped before a completed Court event; required revalidation remains pending.'
        row[10] = blocker
        row[11] = ''
        line = '| ' + ' | '.join(row) + ' |\n'
    manifest_lines.append(line)
manifest = ''.join(manifest_lines)
current_rows = inventory(manifest)
unresolved = [r for r in current_rows if not r[6].startswith(('Completed:', 'Reconciled:'))]
count = 109 + len(records)
latest = max(['1999-06-14'] + [r['date'] for r in records])
carry = sum(l.startswith('| Unscheduled; no date supplied |') for l in manifest.splitlines())
assert carry == 13
status = (f'{count} current-term Court events completed, with the latest dated {latest}. '
          f'{len(unresolved)} scheduled items remain unresolved, plus {carry} undated carryovers: '
          f'{len(unresolved)+carry} unresolved inventory items in total. One nonjudicial source event '
          'is admitted separately. Del Monte Dunes is reconciled without a new Court event. Records control.')
next_event = schedule_cursor(unresolved)
manifest = replace_metadata(manifest, status, latest, next_event)
completed_chunk = sum(r[1] == CHUNK and r[6].startswith('Completed:') for r in current_rows)
chunk_total = sum(r[1] == CHUNK for r in current_rows)
progress = f'{completed_chunk} of {chunk_total} Chunk10 scheduled inventory items are completed, comprising {len(records)} new dated Court events; {chunk_total-completed_chunk} inventory items remain unresolved. '

outputs = {}
retained = {}
for key, neutral in [('CONTINUITY', False), ('NEUTRAL_PROJECTION', True)]:
    base = replace_metadata(opening[key], status, latest, next_event)
    text = insert_event_rows(base, records, neutral)
    law_heading = '## Current-term law' if neutral else '## Current Law'
    positions_heading = '## Current-term published noncontrolling positions' if neutral else '## Material Published Noncontrolling Positions'
    procedure_heading = '## Term-opening carryovers and current pending procedure' if neutral else '## Current Procedure and Institution'
    source_heading = '## Source limits' if neutral else '## Source and Research Cutoff'
    law = '\n'.join(section_entry(r, [(b, r['blocks'][b]) for b in ['Holdings', 'Precedent Treatment', 'Law After Decision']], neutral) for r in records)
    positions = '\n'.join(positions_entry(r, neutral) for r in records)
    procedure = '\n'.join(section_entry(r, [('Procedure After Action', r['blocks']['Procedure After Action'])], neutral) for r in records)
    sources = '\n'.join(section_entry(r, [('Source Notes', r['blocks']['Source Notes'])], neutral) for r in records)
    text = append_section(text, law_heading, law)
    text = append_section(text, positions_heading, positions)
    text = append_section(text, procedure_heading, procedure)
    text = append_section(text, source_heading, f'Chunk10 authority comprises the {len(records)} newly finalized Canonical Decision Records included below, effective only on their stated dates through {latest}.\n\n' + sources)
    blockers = '\n\n'.join(f"**Stopped — {item['caption']} ({item['date']}):** " + item['public_blocker' if neutral else 'blocker'] for item in stopped.values())
    if neutral:
        text = append_section(text, '## Prospective events and material dependencies', progress + next_event + ' ' + BOUNDARY + ('\n\n' + blockers if blockers else ''))
    else:
        text = append_section(text, '## Blockers and Revalidation Needs', progress + 'Earlier open matters, including Germany\'s original leave request and the thirteen undated carryovers, retain their exact recorded conditions. No matter closes through silence or elapsed time.' + ('\n\n' + blockers if blockers else ''))
    # Event-table insertion is the only addition inside a retained section body;
    # remove those added rows before checking exact old section containment.
    without_event_rows = '\n'.join(l for l in text.split('\n') if not (
        l.startswith('| ') and any(f'/{r["name"]})' in l for r in records)))
    retained[key] = preserved_sections(base, without_event_rows)
    for r in records:
        heading = f"### {r['display_caption']} — {r['date']}"
        assert text.count(heading) == 4, f'duplicate or missing case sections: {key}: {r["name"]}'
        assert sum(l.startswith('| ') and f'/{r["name"]})' in l for l in text.splitlines()) == 1
    outputs[key] = text

# Check all untouched manifest rows, open carryovers, institutional/prior-position
# sections, and exact public copies. No unrelated tree traversal or broad audit.
final_rows = rows_by_key(manifest)
assert len(final_rows) == len(old_rows) == 128
for key, (row, line) in old_rows.items():
    if key not in touched_keys:
        assert final_rows[key][1] == line, f'unrelated manifest row changed: {row[2]}'
for r in records:
    assert read_record(TERM/'records'/r['name']) == {k:v for k,v in r.items() if k not in ('key','row','caption','display_caption')}, f'Record changed during integration: {r["name"]}'
    write(TERM/'entering-law'/r['name'], r['public'])
    assert (TERM/'entering-law'/r['name']).read_bytes() == r['public'].encode()
write(TERM/'workspace/manifest.md', manifest, newlines['MANIFEST'])
write(TERM/'workspace/continuity.md', outputs['CONTINUITY'], newlines['CONTINUITY'])
write(TERM/'workspace/neutral-projection.md', outputs['NEUTRAL_PROJECTION'], newlines['NEUTRAL_PROJECTION'])
receipt = {
    'method': 'Mechanical copy from immutable opening snapshots and permitted finalized Record sections; no Git access or adjudication.',
    'captured_new_records': [r['name'] for r in records],
    'capture_excludes_records_arriving_later': True,
    'completed_court_events': count, 'latest_effective_date': latest,
    'unresolved_scheduled_items': len(unresolved), 'undated_carryovers': carry,
    'unresolved_total': len(unresolved)+carry, 'completed_chunk10_rows': completed_chunk,
    'new_completed_court_events': len(records), 'stopped_chunk10_rows': list(stopped.values()),
    'completed_component_records_by_inventory_row': {group[0]['caption']: [r['name'] for r in group] for group in by_key.values()},
    'next_scheduled_event': next_event, 'same_day_boundary': BOUNDARY,
    'canonical_manifest_adapter_executed': str(ADAPTER.relative_to(ROOT)),
    'canonical_builder_output': result.stdout.strip(),
    'prior_sections_preserved': retained, 'unchanged_manifest_rows': len(old_rows)-len(touched_keys),
    'germany_status': next(r[6] for r in current_rows if 'Germany' in r[2]),
    'del_monte_status': next(r[6] for r in current_rows if 'Del Monte' in r[2]),
    'public_copy_sha256': {r['name']: hashlib.sha256(r['public'].encode()).hexdigest() for r in records},
    'duplicate_new_entries': False,
    'write_scope': ['workspace/manifest.md','workspace/continuity.md','workspace/neutral-projection.md',
                    'entering-law/<captured new Record basenames>', 'audit/OT_1998CHUNK10_WORKSPACE_INTEGRATION.json'],
    'limits': 'No ledger rebuild, check_term, Render Input build, substantive audit, or unrelated file audit performed.'
}
write(RECEIPT, json.dumps(receipt, indent=2, ensure_ascii=False) + '\n')
print(json.dumps({k:receipt[k] for k in ['captured_new_records','completed_court_events','latest_effective_date',
    'unresolved_scheduled_items','undated_carryovers','next_scheduled_event','unchanged_manifest_rows','germany_status','del_monte_status']}, indent=2))
