"""Project the single completed Doe Record into the existing OT1995 workspace.

Run only after assembly and dependency review. No adjudicative choices are made
here. Existing public entries and fixed same-day reading snapshots are retained.
"""
from pathlib import Path
import argparse
import re

BASE = Path(__file__).resolve().parents[1]
BLOCKS = ['Event', 'Participation', 'Public Action', 'Judgment & Remedy',
          'Opinion Topology', 'Holdings', 'Precedent Treatment', 'Law After Decision',
          'Separate Writings', 'Procedure After Action', 'Source Notes']


def once(text, old, new):
    if text.count(old) != 1:
        raise ValueError(f'Expected one occurrence: {old[:100]!r}; got {text.count(old)}')
    return text.replace(old, new, 1)


def shift(text, levels):
    return re.sub(r'^(#{1,6}) ', lambda m: '#' * (len(m[1]) + levels) + ' ', text, flags=re.M)


def insert_in_section(text, section, needle, addition):
    start = text.index(section)
    at = text.index(needle, start)
    return text[:at] + addition + '\n\n' + text[at:]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('record')
    args = ap.parse_args()
    if Path(args.record).name != args.record:
        raise ValueError('Pass the natural-key filename only')
    record = BASE / 'records' / args.record
    raw = record.read_text(encoding='utf-8')
    case = re.search(r'^\*\*Case and dockets:\*\* (.+)$', raw, re.M)[1]
    result = re.search(r'^\*\*Result:\*\* (.+)$', raw, re.M)[1]
    event = re.search(r'^\*\*Event and date:\*\* (.+)$', raw, re.M)[1]
    assert '1996-06-21' in event and '76063' in case
    public = raw.split('## Public Projection\n', 1)[1].strip() + '\n'
    headings = list(re.finditer(r'^## ([^\n]+)\n', public, re.M))
    assert [m[1] for m in headings] == BLOCKS
    parts = {m[1]: public[m.end():headings[i+1].start() if i+1 < len(headings) else len(public)].strip()
             for i, m in enumerate(headings)}
    link = f'../records/{args.record}'
    reading_name = 'PUBLIC_' + args.record
    reading = '# Public reading copy\n\nDerived verbatim from the Canonical Decision Record Public Projection. The Record remains authoritative.\n\n' + public
    supplement_name = 'OT_1995CHUNK9_DOE_COMPLETION_LAW_ADDENDUM.md'
    supplement = ('# Doe completion — prospective entering-law addendum\n\n'
                  'The June 21 Doe Record is now effective for later date groups. The original pre-June24, '
                  'pre-June25 and pre-June26 reading snapshots remain unchanged records of their original inputs; '
                  'this addendum supplies the subsequently completed event without claiming it was in those files. '
                  'It does not enter either June 21 peer: Doe and Baby Richard retain the identical common '
                  'pre-June21 baseline. No earlier result or reasoning changes.\n\n'
                  f'Authority: [Doe Record]({link}). The following is its verbatim Public Projection, not independent authority.\n\n' + public)
    status = ('109 completed Court events and nine admitted noncase-law sources (118 canonical Records). '
              'Current Court-event cutoff: 1996-06-26. Chunk 9 has 12 completed Court events and no stopped matters. '
              'Its June20 peers used the preserved common pre-June20 baseline, excluding Gray and one another. '
              'The coordinated June21 matters retain their common pre-June21 baseline and distinct judgments; '
              'Doe is complete without an adult-right merits ruling. The later completed Records have been checked '
              'for material dependence and retain their results and reasoning. The preserved '
              '[common pre-June26 baseline](../entering-law/OT_1995CHUNK9_PRE_19960626_NEUTRAL_PROJECTION.md), '
              f'together with the [Doe completion addendum](../entering-law/{supplement_name}), governs the '
              'June26 peer in chunk 10, excluding the June26 chunk9 decisions. Jones\'s financial-leave motion '
              'and petition, Wood\'s plenary grant, Maine No.35 and Louisiana No.121 implementation, the five '
              'inherited open matters, and Shieh\'s three separate certiorari petitions remain open. '
              'No transmission, service, expiration, execution or other unentered external event is presumed. '
              'Records control over these projections.')
    internal_status = status + ' Operator verification and commit remain pending; public rendering is a separate task.'
    targets = {}
    for name, prefix in [('manifest.md', '**Current status:** '),
                         ('continuity.md', '**Posture:** '),
                         ('neutral-projection.md', 'Current Court actions comprise ')]:
        p = BASE / 'workspace' / name
        text = p.read_text(encoding='utf-8')
        matches = [line for line in text.splitlines() if line.startswith(prefix)]
        assert len(matches) == 1
        replacement = prefix + (status if name == 'neutral-projection.md' else internal_status)
        text = once(text, matches[0], replacement)
        targets[p] = text

    p = BASE / 'workspace' / 'manifest.md'
    text = targets[p]
    rows = [line for line in text.splitlines() if line.startswith('| 1996-06-21 | OT_1995CHUNK9 | + Doe v. Kirchner')]
    assert len(rows) == 1
    cells = [c.strip() for c in rows[0].strip('|').split('|')]
    assert len(cells) == 8
    cells[7] = ' '.join(parts['Procedure After Action'].split()).replace('|', '\\|')
    text = once(text, rows[0], '| ' + ' | '.join(cells) + ' |')
    targets[p] = text

    p = BASE / 'workspace' / 'continuity.md'
    text = targets[p]
    table_row = f'| 1996-06-21 | [{case}]({link}) | {result} |\n'
    text = insert_in_section(text, '### Chunk 9 completed events', '| 1996-06-24 |', table_row.rstrip())
    title = f'#### {case} — 1996-06-21\n\nAuthority: [{case}]({link}).\n\n'
    for section, chosen in [
        ('### Chunk 9 controlling public law', ['Holdings', 'Precedent Treatment', 'Law After Decision']),
        ('### Chunk 9 published separate positions', ['Opinion Topology', 'Separate Writings']),
        ('### Chunk 9 post-decision procedure', ['Procedure After Action']),
    ]:
        entry = title + '\n\n'.join('##### ' + key + '\n\n' + shift(parts[key], 3) for key in chosen)
        text = insert_in_section(text, section, '#### Gasperini', entry)
    block_start = text.index('### Chunk 9 blockers')
    block_end = text.index('## 7. Source and Research Cutoff', block_start)
    text = text[:block_start] + ('### Chunk 9 blockers\n\nNo stopped matter remains in chunk 9. '
           f'Doe is completed in its original June 21 slot; [dependency review](../freeze/OT_1995CHUNK9_DOE_RESUMED_DEPENDENCE.md) '
           'preserves all later adjudications. Adult-claim presentation remains undecided by the Court and does not '
           'prevent its final vehicle disposition.\n\n') + text[block_end:]
    source_line = f'- [{case}]({link}); [verbatim public reading copy](../entering-law/{reading_name}).\n'
    text = insert_in_section(text, '### Chunk 9 sources and handoffs', '- [Gasperini', source_line.rstrip())
    text += ('\nResumed Doe preparation and final stage provenance: '
             '[control receipt](../freeze/OT_1995CHUNK9_DOE_RESUMED_CONTROL.md), '
             '[new independent commitments](../freeze/OT_1995CHUNK9_DOE_RESUMED_COMMITMENTS.md), '
             '[new reconciliation](../freeze/OT_1995CHUNK9_DOE_RESUMED_RECONCILED.md). '
             'The older stopped handoffs and withdrawn provisional dismissal remain preserved history, '
             'not operative votes or a current blocker. No Git provenance is newly verified.\n')
    targets[p] = text

    p = BASE / 'workspace' / 'neutral-projection.md'
    text = targets[p]
    entry = (f'### {case} — 1996-06-21\n\n[Public reading copy](../entering-law/{reading_name}).\n\n' + shift(public, 2).rstrip())
    text = insert_in_section(text, '## Chunk 9 completed public decisions', '### Gasperini', entry)
    start = text.index('## Unresolved chunk 9 matters')
    assert not re.search(r'^## ', text[start + len('## Unresolved chunk 9 matters'):], re.M)
    text = text[:start].rstrip() + '\n'
    targets[p] = text

    # All assertions run before any projection is written.
    (BASE / 'entering-law' / reading_name).write_text(reading, encoding='utf-8')
    (BASE / 'entering-law' / supplement_name).write_text(supplement, encoding='utf-8')
    for p, text in targets.items():
        p.write_text(text, encoding='utf-8')
    print('Projected Doe into manifest, continuity, neutral projection and two public entering-law copies. Ledger and manifest status builders remain to run.')


if __name__ == '__main__':
    main()
