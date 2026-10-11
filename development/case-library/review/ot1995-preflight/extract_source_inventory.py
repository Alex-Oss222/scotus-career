#!/usr/bin/env python3
"""Prepare a read-only OT1995 source inventory, not a case-library import.

Writes only beside this script. The original catalogue/schema must be recovered
before stable library identities or an import can be reconstructed.
"""

from __future__ import annotations

import hashlib
import json
import re
import subprocess
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path


REPOSITORY = Path('/workspace/scotus-career')
DESTINATION = Path(__file__).resolve().parent
OUTPUT = DESTINATION / 'source-inventory.json'
LABELS = ('Case and dockets', 'Event and date', 'Result', 'Version / lineage')
READ_BYTES: dict[str, bytes] = {}


def read_source(relative: str) -> str:
    data = (REPOSITORY / relative).read_bytes()
    READ_BYTES[relative] = data
    return data.decode('utf-8')


def fingerprint(relative: str) -> dict:
    data = READ_BYTES[relative]
    return {
        'path': relative,
        'bytes': len(data),
        'sha256': hashlib.sha256(data).hexdigest(),
    }


def cells(line: str, expected: int) -> list[str]:
    result = [value.strip() for value in line.strip().strip('|').split('|')]
    if len(result) != expected:
        raise ValueError(f'Expected {expected} table columns, got {len(result)}: {line}')
    return result


def section_lines(text: str, heading: str):
    active = False
    for line_number, line in enumerate(text.splitlines(), 1):
        if line == heading:
            active = True
            continue
        if active and line.startswith('## '):
            break
        if active:
            yield line_number, line


def main() -> None:
    head = subprocess.check_output(
        ['git', 'rev-parse', 'HEAD'], cwd=REPOSITORY, text=True
    ).strip()
    source_paths = {
        'manifest': 'terms/OT1995/workspace/manifest.md',
        'ledger': 'terms/OT1995/workspace/ledger.md',
        'case_list': 'terms/OT1995/case-list.md',
        'close_dossier': 'terms/OT1995/close/TERM_CLOSE_DOSSIER.md',
        'close_audit': 'terms/OT1995/close/AUDIT.md',
        'holdings_tracker': 'state/HOLDINGS.md',
        'standards_and_tests_tracker': 'state/STANDARDS_AND_TESTS.md',
        'standing_state_tracker': 'state/STANDING_STATE.md',
        'case_index_template': 'foundation/templates/CASE_INDEX_TEMPLATE.md',
    }
    source_text = {role: read_source(path) for role, path in source_paths.items()}

    manifest_columns = [
        'Event date', 'Chunk', 'Case or matter', 'Citation or docket',
        'Matter type', 'Date status or event type', 'Status', 'Current stage',
    ]
    scheduled = []
    memberships: dict[str, list[dict]] = {}
    for line_number, line in section_lines(
        source_text['manifest'], '## Scheduled inventory and chronology'
    ):
        if line.startswith('| Event date |'):
            assert cells(line, 8) == manifest_columns
        if not re.match(r'^\| \d{4}-\d{2}-\d{2} \|', line):
            continue
        row_cells = cells(line, 8)
        status = row_cells[6]
        assert status.startswith('Completed: '), status
        filenames = re.findall(r'[^\s;,]+\.md', status)
        assert filenames and len(filenames) == len(set(filenames))
        record_paths = [f'terms/OT1995/records/{name}' for name in filenames]
        row_number = len(scheduled) + 1
        scheduled.append({
            'scheduled_row_number': row_number,
            'source_path': source_paths['manifest'],
            'source_line': line_number,
            'row_verbatim': line,
            'columns': dict(zip(manifest_columns, row_cells)),
            'record_paths_in_manifest_order': record_paths,
        })
        for record_path in record_paths:
            memberships.setdefault(record_path, []).append({
                'scheduled_row_number': row_number,
                'manifest_line': line_number,
                'chunk_verbatim': row_cells[1],
                'scheduled_date_verbatim': row_cells[0],
            })

    record_paths = sorted(
        path.relative_to(REPOSITORY).as_posix()
        for path in (REPOSITORY / 'terms/OT1995/records').glob('*.md')
    )
    assert len(record_paths) == 126
    assert set(memberships) <= set(record_paths), 'Manifest references a missing Record'
    assert all(len(rows) == 1 for rows in memberships.values())
    records = []
    for path in record_paths:
        text = read_source(path)
        header_lines = [
            (number, line) for number, line in enumerate(text.splitlines(), 1)
            if line.startswith('**')
        ][:4]
        assert len(header_lines) == 4
        labels = {}
        for expected, (line_number, line) in zip(LABELS, header_lines):
            assert line.startswith(f'**{expected}:**'), (path, line)
            labels[expected] = {'source_line': line_number, 'line_verbatim': line}
        is_court_event = path in memberships
        records.append({
            **fingerprint(path),
            'classification': 'court_event' if is_court_event else 'admitted_noncase_source',
            'classification_provenance': {
                'source_path': source_paths['manifest'],
                'rule': (
                    'Referenced explicitly by a Completed status in the scheduled inventory table.'
                    if is_court_event else
                    'Canonical Record not referenced in the scheduled inventory table; '
                    'the manifest current-status statement identifies ten admitted noncase-law sources.'
                ),
                'scheduled_memberships': memberships.get(path, []),
                'manifest_current_status_line': 7,
            },
            'four_opening_labels_verbatim': labels,
        })

    carryovers = []
    carryover_columns = [
        'Case or matter', 'Court below and judgment', 'Why on the docket',
        'Stage at opening', 'Source',
    ]
    for line_number, line in section_lines(
        source_text['standing_state_tracker'], '## 4. Docket of Cases Brought Up'
    ):
        if line.startswith('| Case or matter |'):
            assert cells(line, 5) == carryover_columns
        if not line.startswith('| *'):
            continue
        row_cells = cells(line, 5)
        carryovers.append({
            'source_path': source_paths['standing_state_tracker'],
            'source_line': line_number,
            'row_verbatim': line,
            'columns': dict(zip(carryover_columns, row_cells)),
        })

    chunks = Counter(row['columns']['Chunk'] for row in scheduled)
    classifications = Counter(record['classification'] for record in records)
    assert len(scheduled) == 115
    assert len(memberships) == 116
    assert classifications == {'court_event': 116, 'admitted_noncase_source': 10}
    assert chunks == {
        f'OT_1995CHUNK{chunk}': (12 if chunk < 10 else 7)
        for chunk in range(1, 11)
    }
    assert len(carryovers) == 12
    assert 'ten admitted noncase-law sources' in source_text['manifest']

    # Confirm a consistent read without writing to the repository. This checks
    # every inventoried source's current raw bytes, including all 126 Records.
    for path, captured in READ_BYTES.items():
        current = (REPOSITORY / path).read_bytes()
        assert hashlib.sha256(current).digest() == hashlib.sha256(captured).digest(), path
    assert head == subprocess.check_output(
        ['git', 'rev-parse', 'HEAD'], cwd=REPOSITORY, text=True
    ).strip(), 'Repository HEAD changed during inventory extraction'

    inventory = {
        'artifact_kind': 'ot1995_catch_up_source_preparation',
        'status': 'Preparation only; not a recovered library, schema replacement, or completed import.',
        'generated_at_utc': datetime.now(timezone.utc).isoformat(),
        'repository_path': str(REPOSITORY),
        'repository_head': head,
        'verbatim_convention': 'Line content is preserved exactly; line terminators are omitted. SHA256 covers raw file bytes.',
        'classification_scope': 'Operational source membership only; no legal classification or historical URL indexing.',
        'limitations': [
            'The original library and original schema are absent from this repository checkout.',
            'Stable library IDs cannot be restored or safely reassigned until the original library copy is available.',
            'Earlier imported chunks require refresh for in-place corrections and newly completed events; appending later chunks is insufficient.',
            'Manifest row order and record-reference order are not event chronology; Bowersox lists its final Record before its interim Record.',
            'A completed scheduled Court event does not mean the underlying matter is closed.',
            'Current state trackers contain the published OT1995 closing baseline, not OT1995 opening law.',
        ],
        'counts': {
            'scheduled_rows': len(scheduled),
            'scheduled_court_record_references': len(memberships),
            'court_event_records': classifications['court_event'],
            'admitted_noncase_source_records': classifications['admitted_noncase_source'],
            'canonical_records': len(records),
            'final_carried_matters': len(carryovers),
            'scheduled_rows_by_chunk': dict(chunks),
        },
        'source_fingerprints': [
            {'role': role, **fingerprint(path)} for role, path in source_paths.items()
        ],
        'manifest_scheduled_rows': scheduled,
        'records': records,
        'final_carryover_rows': carryovers,
        'validation': {
            'counts_and_references': 'passed',
            'four_opening_labels_per_record': 'passed',
            'all_captured_source_hashes_rechecked': 'passed',
            'repository_head_unchanged_during_extraction': 'passed',
            'source_files_verified': len(READ_BYTES),
            'repository_writes': 0,
        },
    }
    OUTPUT.write_text(json.dumps(inventory, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')
    print(json.dumps({
        'output': str(OUTPUT),
        'sha256': hashlib.sha256(OUTPUT.read_bytes()).hexdigest(),
        'repository_head': head,
        'counts': inventory['counts'],
        'validation': inventory['validation'],
    }, indent=2))


if __name__ == '__main__':
    main()
