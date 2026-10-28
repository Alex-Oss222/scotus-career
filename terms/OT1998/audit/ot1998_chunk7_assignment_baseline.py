#!/usr/bin/env python3
"""Generate a bounded assignment baseline from actual current-term Record tables."""
from __future__ import annotations
from collections import Counter
import hashlib
import json
from pathlib import Path
import re
import sys

sys.dont_write_bytecode = True
ROOT = Path(__file__).absolute().parents[3]
TERM = ROOT / 'terms' / 'OT1998'
OUT = TERM / 'audit' / 'OT_1998CHUNK7_ASSIGNMENT_BASELINE.md'
EXCERPTS = TERM / 'audit' / 'OT_1998CHUNK7_ASSIGNMENT_EXCERPTS.md'
RECEIPT = TERM / 'audit' / 'OT_1998CHUNK7_ASSIGNMENT_BASELINE.json'
JUSTICES = ('Stone-Zsela', 'Stevens', "O'Connor", 'Scalia', 'Kennedy', 'Souter', 'Thomas', 'Ginsburg', 'Breyer')
CUTOFF = '1999-04-13'
EXCLUDED = {
    'united_states_v_louisiana_supplemental_decree_1998-10-13.md': 'Unsigned implementing decree.',
    'mosley_v_united_states_death_disposition_1998-12-08.md': 'Per curiam procedural disposition after death.',
    'calderon_v_coleman_summary_merits_1998-12-14.md': 'Per curiam summary merits disposition.',
    'maine_initiative_qualification_admitted_source_1998-12-23.md': 'Admitted source; no judicial opinion.',
    'roberts_v_galen_of_virginia_merits_1999-01-13.md': 'Per curiam merits opinion.',
    'federal_republic_of_germany_original_leave_and_interim_order_1999-03-03.md': 'Original-leave/interim action and Section 10 explanations.',
    'stewart_v_lagrand_application_and_summary_merits_1999-03-03.md': 'Summary merits disposition and application explanations.',
    'stewart_v_lagrand_certiorari_1999-03-03.md': 'Certiorari grant.',
    'central_state_university_v_aaup_certiorari_1999-03-22.md': 'Certiorari grant.',
    'central_state_university_v_aaup_summary_merits_1999-03-22.md': 'Per curiam summary merits disposition.',
}


def headings(text):
    return list(re.finditer(r'^(#{2,6})\s+(.+?)\s*$', text, re.M))


def selected_sections(text):
    hs = headings(text)
    pieces = []
    for index, match in enumerate(hs):
        title, level = match[2], len(match[1])
        if title != 'Opinion Topology' and not re.search(r'\bassignment\b', title, re.I):
            continue
        end = next((later.start() for later in hs[index + 1:] if len(later[1]) <= level), len(text))
        pieces.append((title, text[match.start():end].rstrip()))
    return pieces


def lead_rows(text):
    result = []
    for line in text.splitlines():
        if not line.startswith('|'):
            continue
        cells = [cell.strip() for cell in line.strip().strip('|').split('|')]
        if len(cells) < 2 or not re.match(r'(?:Opinion of the Court|Lead opinion|Opinion announcing the judgment)\b', cells[0], re.I):
            continue
        if cells[1] not in JUSTICES:
            raise ValueError('Unknown lead author: ' + line)
        if (cells[1], line) not in result:
            result.append((cells[1], line))
    return result


def slug(title):
    return re.sub(r'[^\w\- ]', '', title.casefold()).replace(' ', '-')


def main():
    if any(path.exists() for path in (OUT, EXCERPTS, RECEIPT)):
        raise SystemExit('Baseline artifacts already exist; preserve their snapshot and create a new explicitly named recount.')
    items = []
    for path in (TERM / 'records').glob('*.md'):
        text = path.read_text(encoding='utf-8')
        case = re.search(r'^\*\*Case and dockets:\*\*\s*(.+)$', text, re.M)
        event = re.search(r'^\*\*Event and date:\*\*\s*(.+)$', text, re.M)
        if not case or not event:
            raise ValueError('Missing Record identity: ' + path.name)
        date = re.search(r'\b\d{4}-\d{2}-\d{2}\b', event[1])[0]
        if date < CUTOFF:
            items.append((date, case[1].casefold(), path, text, case[1], event[1]))
    items.sort(key=lambda item: (item[0], item[1], item[2].name))
    counts = Counter({justice: 0 for justice in JUSTICES})
    counted, exclusions = [], []
    excerpts = ['# OT1998 chunk 7 bounded assignment source excerpts', '',
                'Exact opinion-table rows and assignment/Opinion Topology sections from existing Records dated before April 13, 1999. These are assignment-only inputs; no new-case position is supplied. Historical tally statements are reproduced as source text but do not supply the fresh counts. Records remain authoritative. No Git verification was performed.', '']
    table = []
    for date, _, path, text, case, event in items:
        rows = lead_rows(text)
        selected = selected_sections(text)
        identity = {'record': path.name, 'date': date, 'case': case, 'event': event,
                    'source_sha256': hashlib.sha256(path.read_bytes()).hexdigest()}
        authors = sorted({author for author, _ in rows}, key=JUSTICES.index)
        if path.name in EXCLUDED:
            exclusions.append({**identity, 'reason': EXCLUDED[path.name]})
        else:
            if not authors:
                raise ValueError('Nonexcluded Record has no signed lead table: ' + path.name)
            for author in authors:
                counts[author] += 1
            counted.append({**identity, 'authors': authors, 'exact_lead_rows': [row for _, row in rows]})
            statement_links = [f'[{title}](../records/{path.name}#{slug(title)})' for title, _ in selected if title != 'Opinion Topology']
            if not statement_links:
                raise ValueError('No assignment statement for counted Record: ' + path.name)
            table.append('| ' + date + ' | [' + case.replace('|', '/') + '](../records/' + path.name + ') | ' + ', '.join(authors) + ' | ' + '; '.join(statement_links) + ' |')
        excerpts += ['---', '', '<!-- source-record: ' + path.name + ' -->', '',
                     '**Case and dockets:** ' + case, '**Event and date:** ' + event, '']
        copied = '\n\n'.join(piece for _, piece in selected)
        excerpts += [copied, '']
        missing_rows = [row for _, row in rows if row not in copied]
        if missing_rows:
            excerpts += ['### Exact additional lead-opinion table rows', '',
                         '| Writing | Author | Joined by | Relationship to judgment | Scope joined |',
                         '|---|---|---|---|---|', *missing_rows, '']
    last = counted[-1] if counted else None
    lines = ['# OT1998 chunk 7 assignment baseline', '',
             'Recounted from current Record opinion tables before April 13, 1999, with same-date cases in alphabetical order. Prior assignment tallies were not used. This baseline is a snapshot; Engine section 8 requires a new recount before each assignment, including Records already written in this Run.', '',
             '| Justice | Counted signed lead opinions |', '|---|---:|',
             *[f'| {justice} | {counts[justice]} |' for justice in JUSTICES], '',
             f'{len(items)} existing Records yield {len(counted)} counted lead opinions and {sum(counts.values())} author increments. {len(exclusions)} events are excluded. The last counted event is [{last["case"]}](../records/{last["record"]}) ({last["date"]}).', '',
             'A signed lead after full merits submission counts once per author even when the Court resolves a threshold issue; NAACP, Hart and Gable retain their existing plenary-submission classifications. Per curiam opinions, summary dispositions, procedural orders, Section 10 explanations, separate writings and the admitted source do not count. Suster and Gable identify their lead authors in internal opinion tables; multiple parts delivered by one author count once.', '',
             'Counts alone establish no eligibility or assignment. First fix opinion form and propositions, then identify the members of the tentative judgment coalition whose commitments fully support every proposition. For a Chief-assigned opinion, the pool comprises eligible authors no more than one above the lowest eligible count. An Associate-assigned lead still counts. No assignment is reopened by this extraction.', '',
             'The [bounded source excerpts](OT_1998CHUNK7_ASSIGNMENT_EXCERPTS.md) reproduce the opinion topologies and assignment statements. The [machine-readable receipt](OT_1998CHUNK7_ASSIGNMENT_BASELINE.json) records exact lead rows and source digests. Git commitment status and provenance were not verified.', '',
             '## Counted sources and assignment references', '',
             '| Date | Case and Record | Lead author | Assignment statement |', '|---|---|---|---|', *table, '',
             '## Excluded events', '', '| Date | Record | Reason |', '|---|---|---|',
             *[f'| {item["date"]} | [{item["case"]}](../records/{item["record"]}) | {item["reason"]} |' for item in exclusions], '']
    data = {'scope': 'Existing OT1998 Records dated before 1999-04-13; actual opinion-table authors, not previous assignment tallies.',
            'record_count': len(items), 'counted_opinions': len(counted), 'author_increments': sum(counts.values()),
            'counts': dict(counts), 'last_counted': last, 'counted': counted, 'excluded': exclusions,
            'git_verification': 'Deferred; every Git command is prohibited.',
            'future_assignments': 'Recount current actual preceding Records afresh before every assignment.'}
    OUT.write_text('\n'.join(lines), encoding='utf-8')
    EXCERPTS.write_text('\n'.join(excerpts).rstrip() + '\n', encoding='utf-8')
    RECEIPT.write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(json.dumps({'records': len(items), 'counted': len(counted), 'counts': dict(counts), 'excluded': len(exclusions),
                      'last': last['record'], 'baseline': str(OUT), 'excerpts': str(EXCERPTS)}, indent=2))


if __name__ == '__main__':
    main()
