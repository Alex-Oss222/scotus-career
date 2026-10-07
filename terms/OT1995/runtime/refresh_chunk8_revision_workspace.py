"""Refresh live chunk 8 projections from the twelve canonical Records.

Run only after assembly and the later-record dependency review are complete.
This tool does not run Git or any repository tool, edit a Record, alter a
brief/inventory/render, or change frozen handoffs. Root runs the required
ledger, manifest, Render Input and term-check tools separately afterward.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import re

TERM = Path(__file__).resolve().parents[1]
MARKER = "<!-- chunk8-projection: "
OLD_VERA = "Vera_and_consolidated_standing_1996-06-13.md"
OLD_LEAVITT = "Leavitt_v_Jane_L_certiorari_1996-06-17.md"
HEADINGS = (
    "Event", "Participation", "Public Action", "Judgment & Remedy",
    "Opinion Topology", "Holdings", "Precedent Treatment",
    "Law After Decision", "Separate Writings", "Procedure After Action",
    "Source Notes",
)


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def read_record(name: str) -> dict:
    assert Path(name).name == name and name.endswith('.md'), name
    text = (TERM / 'records' / name).read_text(encoding='utf-8')
    assert text.count('## Public Projection') == 1, name
    public = text.split('## Public Projection', 1)[1].strip() + '\n'
    fields = {}
    for label, key in [('Case and dockets', 'case'), ('Event and date', 'event'), ('Result', 'result')]:
        m = re.search(r'^\*\*' + re.escape(label) + r':\*\*\s*(.+)$', text, re.M)
        assert m, (name, label)
        fields[key] = m.group(1)
    fields['date'] = re.search(r'\b\d{4}-\d{2}-\d{2}\b', fields['event']).group()
    blocks = {}
    matches = list(re.finditer(r'^## (.+?)\s*$', public, re.M))
    assert [m.group(1) for m in matches] == list(HEADINGS), (name, [m.group(1) for m in matches])
    for i, match in enumerate(matches):
        end = matches[i + 1].start() if i + 1 < len(matches) else len(public)
        blocks[match.group(1)] = public[match.end():end].strip()
    return dict(fields, name=name, public=public, blocks=blocks)


def plain(value: str) -> str:
    return value.replace('|', '&#124;').replace('\n', ' ')


def live_names(text: str, names: dict[str, str]) -> str:
    for old, new in names.items():
        text = text.replace(old, new)
    return text


def chunk_rows(manifest: str, targets: dict[str, str]):
    result = []
    for line in manifest.splitlines():
        if '| OT_1995CHUNK8 |' not in line:
            continue
        cells = [c.strip() for c in line.strip().strip('|').split('|')]
        assert len(cells) == 8, line
        if 'Montana v. Egelhoff' == cells[2]:
            name = targets['egelhoff']
        elif 'Bush v. Vera;' in cells[2]:
            name = targets['vera']
        elif 'Leavitt v. Jane L.' == cells[2]:
            name = targets['leavitt']
        else:
            assert cells[6].startswith('Completed: '), line
            name = cells[6].removeprefix('Completed: ')
        item = read_record(name)
        assert item['date'] == cells[0], (name, item['date'], cells[0])
        result.append((cells, item))
    assert len(result) == 12 and len({r['name'] for _, r in result}) == 12
    assert [r['date'] for _, r in result] == sorted(r['date'] for _, r in result)
    return result


def summary_block(item: dict, caption: str) -> str:
    return (
        f"{MARKER}{item['name']} -->\n\n"
        f"## Chunk 8 completed event — {caption}\n\n"
        f"{item['result']}\n\n{item['blocks']['Procedure After Action']}\n\n"
        f"[Canonical Record](../records/{item['name']}); "
        f"[complete public law and writings](../entering-law/PUBLIC_{item['name']}).\n"
    )


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--vera', default='Vera_and_consolidated_merits_1996-06-13.md')
    ap.add_argument('--egelhoff', default='Montana_v_Egelhoff_merits_1996-06-13.md')
    ap.add_argument('--leavitt', default='Leavitt_v_Jane_L_summary_merits_1996-06-17.md')
    ap.add_argument('--write', action='store_true', help='Write the reviewed projections; without this flag show a read-only plan.')
    args = ap.parse_args()
    targets = {key: getattr(args, key) for key in ('vera', 'egelhoff', 'leavitt')}
    names = {OLD_VERA: args.vera, OLD_LEAVITT: args.leavitt}
    manifest_path = TERM / 'workspace' / 'manifest.md'
    manifest_original = manifest_path.read_text(encoding='utf-8')
    rows = chunk_rows(manifest_original, targets)
    all_records = list((TERM / 'records').glob('*.md'))
    assert len(all_records) == 106, ('Expected 106 canonical Records', len(all_records))
    assert not (TERM / 'records' / OLD_VERA).exists(), 'Old Vera Record still exists'
    assert not (TERM / 'records' / OLD_LEAVITT).exists(), 'Old Leavitt Record still exists'
    pending = {}
    receipt = {'operation': 'Canonical-record-derived chunk 8 live workspace projection refresh',
               'git_operations': 'None; history verification remains deferred to operator',
               'canonical_record_count': 106, 'court_event_count': 97,
               'chunk8_record_order': [item['name'] for _, item in rows], 'writes': []}

    # Read existing captions to leave unchanged peers' display labels intact.
    captions = {}
    for match in re.finditer(r'<!-- chunk8-projection: ([^>]+) -->\s*\n## Chunk 8 completed event — (.+)$', manifest_original, re.M):
        captions[live_names(match.group(1).strip(), names)] = match.group(2)
    for cells, item in rows:
        captions.setdefault(item['name'], cells[2].removeprefix('+ '))

    old_pending = (
        'Egelhoff remains pending; no new Court disposition or law has been entered in that matter. '
        'The three Vera direct appeals remain pending after the June13 standing-only decision; existing lower relief is unchanged. '
        'Leavitt remains pending for merits review and supplemental briefing under the June17 grant; existing lower relief is undisturbed.'
    )
    new_current = (
        'The June 13 Vera event now resolves standing and the merits of all three direct appeals; '
        'the June 13 Egelhoff event and June 17 Leavitt summary merits event are completed. '
        'Their precise rules, coalitions, writings, remedies and remaining lower-court proceedings appear in the canonical-record-derived chunk 8 entries below. '
        'No chunk 8 matter remains stopped. The June 13 and June 17 peers retain their common pre-group baselines; '
        'later entering-law notes reflect the effective decisions within their actual scope.'
    )

    def prefix_refresh(text: str, neutral: bool) -> str:
        assert MARKER in text
        prefix = text[:text.index(MARKER)]
        prefix = prefix.replace('96 completed Court events and nine admitted noncase-law sources (105 canonical Records)',
                                '97 completed Court events and nine admitted noncase-law sources (106 canonical Records)')
        prefix = prefix.replace('Chunk 8 has eleven completed Court events and one stopped matter.',
                                'Chunk 8 has twelve completed Court events and no stopped matter.')
        assert old_pending in prefix or new_current in prefix, 'Expected current-status paragraph not found'
        prefix = prefix.replace(old_pending, new_current)
        prefix = prefix.replace(
            "Whether the assignment itself supplies Article III injury is the question for decision; the merits ruling's correctness is outside it.",
            'The opening intake presented the assignment-based standing question. The completed June 13 event also resolves the merits of all three direct appeals; its canonical Record supplies the controlling scope and relief.')
        prefix = prefix.replace(
            'Preserve all three dockets and all supplied parties; do not substitute a Chen-only case or decide the historical racial-predominance merits question.',
            'Preserve all three dockets and all supplied parties; do not substitute a Chen-only case. The completed June 13 Record governs the merits and resulting relief.')
        prefix = prefix.replace(
            'The presented question is whether the assignment itself supplies Article III injury; the correctness of the merits ruling is outside it.',
            'The opening intake presented the assignment-based standing question. The completed June 13 event also resolves the merits of all three direct appeals; the current public projection below supplies the controlling scope and relief.')
        return live_names(prefix, names)

    for filename in ('manifest.md', 'continuity.md', 'neutral-projection.md'):
        path = TERM / 'workspace' / filename
        text = path.read_text(encoding='utf-8')
        prefix = prefix_refresh(text, filename == 'neutral-projection.md')
        if filename == 'manifest.md':
            replacements = {}
            for cells, item in rows:
                if item['name'] not in set(targets.values()):
                    continue
                current = cells.copy()
                current[6] = 'Completed: ' + item['name']
                current[7] = plain(item['blocks']['Procedure After Action'])
                if item['name'] == args.vera:
                    current[5] = 'Direct-appeal standing and merits decision'
                if item['name'] == args.leavitt:
                    current[5] = 'Summary merits decision on certiorari petition'
                replacements[(cells[0], cells[2])] = '| ' + ' | '.join(current) + ' |'
            lines = prefix.splitlines(keepends=True)
            for i, line in enumerate(lines):
                if '| OT_1995CHUNK8 |' in line:
                    cells = [c.strip() for c in line.strip().strip('|').split('|')]
                    key = (cells[0], cells[2])
                    if key in replacements:
                        lines[i] = replacements[key] + '\n'
            prefix = ''.join(lines)
        appendices = []
        for _, item in rows:
            if filename == 'neutral-projection.md':
                block = f"{MARKER}{item['name']} -->\n\n{item['public']}"
            else:
                block = summary_block(item, captions[item['name']])
                if filename == 'continuity.md':
                    for heading in ('Holdings', 'Precedent Treatment', 'Law After Decision', 'Separate Writings'):
                        block += f"\n### {heading}\n\n{item['blocks'][heading]}\n"
            appendices.append(block.rstrip())
        pending[path] = prefix.rstrip() + '\n\n' + '\n\n\n'.join(appendices) + '\n'

    # Preserve the displayed ledger order and first-record metadata across rename.
    ledger = TERM / 'workspace' / 'ledger.md'
    pending[ledger] = live_names(ledger.read_text(encoding='utf-8'), names)

    # Recreate each bounded public reading copy directly from its canonical source.
    for _, item in rows:
        path = TERM / 'entering-law' / ('PUBLIC_' + item['name'])
        existing = path.read_text(encoding='utf-8') if path.exists() else None
        if existing and item['public'].strip() in existing:
            # Preserve a valid existing wrapper and byte-equivalent public body.
            continue
        pending[path] = (
            '# Bounded current-term public reading copy\n\n'
            f"Authority: canonical event {item['case']}, {item['date']}; natural-key Record {item['name']}. "
            'The following Public Projection is copied unchanged; no audit or private material is included.\n\n'
            + item['public'])

    for path, text in pending.items():
        before = path.read_bytes() if path.exists() else b''
        after = text.encode('utf-8')
        receipt['writes'].append({'path': path.relative_to(TERM).as_posix(),
                                 'before_sha256': sha(before), 'after_sha256': sha(after),
                                 'changed': before != after})
    if args.write:
        for path, text in pending.items():
            path.write_bytes(text.encode('utf-8'))
        (TERM / 'freeze' / 'OT_1995CHUNK8_REVISION_WORKSPACE_RECEIPT.json').write_text(
            json.dumps(receipt, indent=2) + '\n', encoding='utf-8')
        print('Projected twelve chunk 8 Records; ledger and required repository tools remain to be run separately.')
    else:
        print('Read-only plan; no workspace, Record or public-copy write performed.')
    print(json.dumps(receipt, indent=2))


if __name__ == '__main__':
    main()
