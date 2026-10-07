"""Repair renamed navigation without rewriting historical adjudicative substance."""
from pathlib import Path
import hashlib
import json
import re

TERM = Path(__file__).resolve().parents[1]
renames = {
    'Vera_and_consolidated_standing_1996-06-13.md': 'Vera_and_consolidated_merits_1996-06-13.md',
    'Leavitt_v_Jane_L_certiorari_1996-06-17.md': 'Leavitt_v_Jane_L_summary_merits_1996-06-17.md',
}
assert all((TERM / 'records' / name).exists() for name in renames.values())
repairs = []
for folder in ('freeze', 'runtime', 'entering-law', 'workspace', 'render-inputs', 'sources'):
    for path in (TERM / folder).rglob('*.md'):
        raw = path.read_bytes()
        text = raw.decode('utf-8')
        updated = text
        for old, new in renames.items():
            # Fix actual Markdown navigation only. Quoted old identifiers in
            # immutable preimage receipts/lineage remain truthful history.
            updated = re.sub(r'(\]\([^\)\n]*?)' + re.escape(old) + r'(?=[#\)])',
                             lambda m: m.group(1) + new, updated)
        if updated == text:
            continue
        if folder == 'freeze' and '_REVISION_' not in path.name:
            newline = '\r\n' if '\r\n' in text else '\n'
            note = ('> Historical handoff: its substantive statements describe the original Run. '
                    'The authorized October 7 revision repairs renamed navigation only; linked canonical '
                    'Records and public copies now show the replacement decisions. The current stage '
                    'routing and the navigation preimage hashes are in '
                    '[the revision handoff index](OT_1995CHUNK8_REVISION_HANDOFFS.md) and '
                    '[navigation receipt](OT_1995CHUNK8_REVISION_NAVIGATION.json).')
            first, rest = updated.split(newline, 1)
            updated = first + newline + newline + note + newline + rest
        path.write_bytes(updated.encode('utf-8'))
        repairs.append({'path': path.relative_to(TERM).as_posix(),
                        'before_sha256': hashlib.sha256(raw).hexdigest(),
                        'after_sha256': hashlib.sha256(path.read_bytes()).hexdigest(),
                        'scope': 'renamed Markdown link targets; historical-handoff annotation where needed'})

# Remove obsolete derived live copies only after their replacements exist.
removed = []
for old, new in renames.items():
    old_path = TERM / 'entering-law' / ('PUBLIC_' + old)
    new_path = TERM / 'entering-law' / ('PUBLIC_' + new)
    assert new_path.is_file()
    if old_path.exists():
        assert old_path.resolve().parent == (TERM / 'entering-law').resolve()
        removed.append({'path': old_path.relative_to(TERM).as_posix(),
                        'sha256': hashlib.sha256(old_path.read_bytes()).hexdigest()})
        old_path.unlink()

matters = ('IBM', 'SPINK', 'MYERS', 'VERA', 'JAFFEE', 'EGELHOFF',
           'KOON', 'RISE', 'MELENDEZ', 'LEAVITT', 'CALDERON', 'GRAY')
targets = {'VERA', 'EGELHOFF', 'LEAVITT'}
lines = ['# Chunk 8 current frozen handoff routing', '',
         'The three authorized replacements use their separate revision freezes. The other nine matters retain their original frozen commitments and reconciliations. Old aggregate freezes remain historical; their superseded three-matter assembly status is not current authority. No Git operation was performed.', '',
         'Navigation-only repairs to historical frozen files do not refreeze votes or grounds. Hashes recorded by earlier stages refer to their original input bytes; the [navigation receipt](OT_1995CHUNK8_REVISION_NAVIGATION.json) maps affected preimages to repaired navigation. Original excluded-peer identifiers and preservation hashes remain historical metadata.', '',
         '| Matter | Independent commitments | Reconciliation |', '|---|---|---|']
for matter in matters:
    infix = '_REVISION' if matter in targets else ''
    names = [f'OT_1995CHUNK8_{matter}{infix}_{stage}.md' for stage in ('COMMITMENTS', 'RECONCILED')]
    assert all((TERM / 'freeze' / name).is_file() for name in names), names
    lines.append('| ' + matter + ' | ' + ' | '.join(f'[{stage.lower()}]({name})' for stage, name in zip(('COMMITMENTS', 'RECONCILED'), names)) + ' |')
lines += ['', '## Assignment continuity', '',
          'See [the revised assignment reference](OT_1995CHUNK8_REVISION_ASSIGNMENT_REFERENCE.md). The original named assignments of all other Records remain unchanged. The later-note dependency review adds no decisional ground or new judicial event.', '']
(TERM / 'freeze/OT_1995CHUNK8_REVISION_HANDOFFS.md').write_text('\n'.join(lines), encoding='utf-8')
for stage in ('COMMITMENTS', 'RECONCILED'):
    (TERM / 'runtime' / f'OT_1995CHUNK8_{stage}.md').write_text(
        f'# Chunk 8 current {stage.lower()} routing\n\n'
        'The current frozen matter-specific sources are listed in '
        '[the authoritative revision handoff index](../freeze/OT_1995CHUNK8_REVISION_HANDOFFS.md). '
        'This runtime index is derived navigation, not an independent commitment or reconciliation. '
        'Vera, Egelhoff and Leavitt use their revision freezes; all other matters retain their original freezes.\n',
        encoding='utf-8')

# The current workspace links to refreshed public common baselines, while the
# old snapshots remain historical evidence of what the earlier Run received.
for name in ('manifest.md', 'continuity.md', 'neutral-projection.md'):
    path = TERM / 'workspace' / name
    raw = path.read_bytes()
    updated = raw
    for group in ('JUNE14', 'JUNE17', 'JUNE20'):
        updated = updated.replace(f'OT_1995CHUNK8_PRE_{group}_NEUTRAL_PROJECTION.md'.encode(),
                                  f'OT_1995CHUNK8_REVISION_PRE_{group}_NEUTRAL_PROJECTION.md'.encode())
    if updated != raw:
        path.write_bytes(updated)
        repairs.append({'path': path.relative_to(TERM).as_posix(), 'scope': 'current baseline link targets',
                        'before_sha256': hashlib.sha256(raw).hexdigest(),
                        'after_sha256': hashlib.sha256(updated).hexdigest()})

receipt = {'repairs': repairs, 'obsolete_derived_copies_removed': removed,
           'historical_identifiers': 'Retained in lineage, preimage hashes, excluded-peer snapshot tables, and old snapshot markers; none is a live file link.',
           'adjudication': 'No Record or Public Projection changed by this operation.', 'git_operations': 0}
(TERM / 'freeze/OT_1995CHUNK8_REVISION_NAVIGATION.json').write_text(json.dumps(receipt, indent=2) + '\n', encoding='utf-8')
print(f'Repaired {len(repairs)} navigation files; removed {len(removed)} obsolete derived copies.')
