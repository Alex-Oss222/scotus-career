#!/usr/bin/env python3
"""Read-only chunk 7 clerical validation, writing only its named audit receipt.

No subprocesses, Git access, adjudicative edits, or workspace integration.
Default final mode expects twelve events and a generated Render Input.
Use --partial while assembly is incomplete. A flagged vote/wording relationship
requires review; this script never decides a coalition or changes an outcome.
"""
from __future__ import annotations
import argparse
from collections import Counter
import difflib
import hashlib
import json
import os
from pathlib import Path
import re
import sys
import types
from urllib.parse import unquote, urlsplit

sys.dont_write_bytecode = True
ROOT = Path(__file__).absolute().parents[3]
TERM = ROOT / 'terms' / 'OT1998'
AUDIT = TERM / 'audit'
START, END = '1999-04-13', '1999-05-17'
BLOCKS = ('Event', 'Participation', 'Public Action', 'Judgment & Remedy', 'Opinion Topology',
          'Holdings', 'Precedent Treatment', 'Law After Decision', 'Separate Writings',
          'Procedure After Action', 'Source Notes')
JUSTICES = ('Stone-Zsela', 'Stevens', "O'Connor", 'Scalia', 'Kennedy', 'Souter', 'Thomas', 'Ginsburg', 'Breyer')
LABELS = ('Case and dockets', 'Event and date', 'Result', 'Version / lineage')
NAMED = re.compile(r"\b(?:Stone-Zsela|Stone|Stevens|O['’]Connor|Scalia|Kennedy|Souter|Thomas|Ginsburg|Breyer)\b")
VOTE = re.compile(r'(?<!\d)([0-9]+)\s*[–-]\s*([0-9]+)(?:\s*[–-]\s*([0-9]+))?(?!\d)')
LINK = re.compile(r'(?<!!)\[[^\]\n]*\]\((<[^>]+>|[^\s)]+)(?:\s+"[^"]*")?\)')
DEFINITION = re.compile(r'^\s*\[[^\]]+\]:\s*(<[^>]+>|\S+)', re.M)


def norm(path):
    return os.path.normcase(os.path.abspath(os.fsdecode(path)))


def guard(receipt):
    forbidden = [norm(ROOT / name) for name in ('stone', '.git')]
    allowed = norm(receipt)

    def audit(event, args):
        if event in {'subprocess.Popen', 'os.system', 'os.posix_spawn'} or event.startswith(('os.exec', 'os.spawn')):
            raise PermissionError('Every subprocess and shell invocation is prohibited')
        if event in {'open', 'os.listdir', 'os.scandir'} and args and isinstance(args[0], (str, bytes, os.PathLike)):
            value = norm(args[0])
            if any(value == item or value.startswith(item + os.sep) for item in forbidden):
                raise PermissionError('Prohibited directory access blocked')
        if event == 'open':
            path, mode, flags = args
            writing = (isinstance(mode, str) and any(char in mode for char in 'wax+')) or (
                isinstance(flags, int) and flags & (os.O_WRONLY | os.O_RDWR | os.O_CREAT | os.O_TRUNC | os.O_APPEND))
            if writing and (not isinstance(path, (str, bytes, os.PathLike)) or norm(path) != allowed):
                raise PermissionError('Only the named audit receipt may be written')
        if event in {'os.remove', 'os.unlink', 'os.rmdir', 'os.mkdir', 'os.rename', 'os.replace',
                     'os.link', 'os.symlink', 'os.truncate', 'os.chmod'}:
            raise PermissionError('Filesystem mutation is prohibited')

    sys.addaudithook(audit)


def names(text):
    values = [match[0].replace('’', "'") for match in NAMED.finditer(text)]
    return ['Stone-Zsela' if value == 'Stone' else value for value in values]


def cells(line):
    return [item.strip() for item in line.strip().strip('|').split('|')]


def public_blocks(text):
    matches = list(re.finditer(r'^##\s+([^\n]+)\s*$', text, re.M))
    return {match[1]: text[match.end():(matches[i + 1].start() if i + 1 < len(matches) else len(text))].strip()
            for i, match in enumerate(matches)}


def record_identity(path, text):
    case = re.search(r'^\*\*Case and dockets:\*\*\s*(.+)$', text, re.M)
    event = re.search(r'^\*\*Event and date:\*\*\s*(.+)$', text, re.M)
    if not case or not event:
        raise ValueError('Missing identity: ' + path.name)
    date = re.search(r'\b\d{4}-\d{2}-\d{2}\b', event[1])
    if not date:
        raise ValueError('Missing event date: ' + path.name)
    return {'file': path.name, 'date': date[0], 'case': case[1], 'event': event[1], 'text': text}


def anchor_set(text):
    found, counts = set(), Counter()
    for heading in re.findall(r'^#{1,6}\s+(.+?)\s*#*\s*$', text, re.M):
        heading = re.sub(r'\[([^\]]+)\]\([^)]*\)', r'\1', heading)
        heading = re.sub(r'<[^>]+>', '', heading)
        value = re.sub(r'[^\w\- ]', '', heading.casefold()).replace(' ', '-')
        suffix = counts[value]
        found.add(value + ('-' + str(suffix) if suffix else ''))
        counts[value] += 1
    found.update(re.findall(r'<(?:a\b[^>]*?\bname|[^>]*?\bid)=["\']([^"\']+)["\']', text, re.I))
    return found


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--partial', action='store_true')
    parser.add_argument('--expected-events', type=int, default=12)
    parser.add_argument('--receipt', default='OT_1998CHUNK7_FINAL_DETERMINISTIC.json')
    args = parser.parse_args()
    if Path(args.receipt).name != args.receipt or not args.receipt.endswith('.json'):
        raise SystemExit('--receipt must be a JSON basename in terms/OT1998/audit')
    receipt = AUDIT / args.receipt
    if receipt.exists():
        raise SystemExit('Preserve existing receipt; choose a new --receipt basename')
    guard(receipt)
    errors, coverage, votes, topology, links, lengths = [], [], [], [], [], {}
    all_records = []
    for path in (TERM / 'records').glob('*.md'):
        if path.name.startswith('.'):
            continue
        all_records.append(record_identity(path, path.read_text(encoding='utf-8')))
    all_records.sort(key=lambda row: (row['date'], row['case'].casefold(), row['file']))
    rows = [row for row in all_records if START <= row['date'] <= END]
    if len(rows) != args.expected_events:
        message = f'Found {len(rows)} of {args.expected_events} expected chunk 7 events'
        (coverage if args.partial and len(rows) < args.expected_events else errors).append(message)
    if not rows:
        errors.append('No chunk 7 Records to validate')

    helper_path = AUDIT / 'ot1998_chunk7_assignment_baseline.py'
    helper = types.ModuleType('assignment_helpers')
    helper.__file__ = str(helper_path)
    exec(compile(helper_path.read_text(encoding='utf-8'), str(helper_path), 'exec'), helper.__dict__)
    previous_exclusions = helper.EXCLUDED

    def check_link_targets(path, text, scope):
        targets = [match[1].strip('<>') for match in LINK.finditer(text)]
        targets += [match[1].strip('<>') for match in DEFINITION.finditer(text)]
        raw_urls = re.findall(r'(?:https?://|file://)[^\s<>\])]+', text, re.I)
        for target in list(dict.fromkeys(targets + raw_urls)):
            parsed = urlsplit(target)
            hostname = (parsed.hostname or '').casefold()
            forbidden_url = (parsed.scheme.casefold() == 'file' or re.match(r'^/?[A-Za-z]:[\\/]', target)
                             or target.startswith(('\\\\', '//')) or 'onedrive' in hostname
                             or hostname in {'1drv.ms', 'localhost', '127.0.0.1', '::1', 'github.com', 'github.io', 'githubusercontent.com'}
                             or hostname.endswith(('.github.com', '.github.io', '.githubusercontent.com')))
            if forbidden_url:
                errors.append(f'{scope}: prohibited local-machine/OneDrive/GitHub URL: {target}')
                continue
            if parsed.scheme or parsed.netloc:
                continue
            local_name, _, fragment = unquote(target).partition('#')
            if not local_name and not fragment:
                continue
            local = Path(os.path.abspath(path.parent / local_name)) if local_name else path
            locked = norm(ROOT / 'stone')
            if norm(local) == locked or norm(local).startswith(locked + os.sep):
                errors.append(scope + ': prohibited directory link target; not accessed')
                continue
            if not local.exists():
                errors.append(f'{scope}: missing local link: {target}')
                continue
            item = {'source': scope, 'target': target, 'exists': True}
            if fragment:
                if '_STONE' in local.name.upper() or local.parent == TERM / 'briefs':
                    coverage.append(scope + ': private-input anchor not opened: ' + target)
                    item['anchor'] = 'not opened'
                elif local.suffix.casefold() == '.md':
                    present = fragment in anchor_set(local.read_text(encoding='utf-8'))
                    item['anchor'] = present
                    if not present:
                        errors.append(f'{scope}: unresolved Markdown anchor: {target}')
                else:
                    coverage.append(scope + ': non-Markdown fragment not verified: ' + target)
            links.append(item)

    def group(cell, participants, history):
        value = names(cell)
        if value:
            return value
        if re.fullmatch(r'(?:None|No one)[.]?', cell.strip(), re.I):
            return []
        number_words = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}
        same = re.match(r'Same\s+(\d+|one|two|three|four|five|six|seven|eight|nine)\b', cell, re.I)
        if same:
            size = int(same[1]) if same[1].isdigit() else number_words[same[1].casefold()]
            return history.get(size)
        if re.search(r'\ball (?:nine|participating Justices)\b', cell, re.I):
            return participants[:]
        return None

    def validate_groups(filename, label, count, groups, participants):
        item = {'record': filename, 'component': label, 'count': count, 'groups': groups}
        if any(value is None for value in groups):
            item['status'] = 'unparsed'
            coverage.append(filename + ': named vote not fully parsed: ' + label)
        else:
            discrepancies = []
            if [len(value) for value in groups] != count:
                discrepancies.append('named group sizes differ from printed count')
            flat = [name for value in groups for name in value]
            if len(flat) != len(set(flat)):
                discrepancies.append('Justice duplicated within/across disposition groups')
            if set(flat) != set(participants):
                discrepancies.append('named disposition groups do not cover the participating roster')
            item['status'] = 'FLAG' if discrepancies else 'PASS'
            item['discrepancies'] = discrepancies
            errors.extend(filename + ': vote arithmetic flag (' + label + '): ' + problem for problem in discrepancies)
        votes.append(item)

    for row in rows:
        path, text = TERM / 'records' / row['file'], row['text']
        for line, label in zip(text.splitlines()[:4], LABELS):
            if not line.startswith('**' + label + ':**'):
                errors.append(row['file'] + ': opening label not in fixed line order: ' + label)
        if text.count('## Public Projection') != 1:
            errors.append(row['file'] + ': expected exactly one Public Projection boundary')
            continue
        projection = text.split('## Public Projection', 1)[1].strip()
        row['projection'] = projection
        headings = re.findall(r'^##\s+([^\n]+)\s*$', projection, re.M)
        if headings != list(BLOCKS):
            errors.append(row['file'] + ': public blocks differ from exact eleven-block interface')
            continue
        blocks = public_blocks(projection)
        if not re.search(r'research cutoff', text, re.I):
            errors.append(row['file'] + ': research cutoff absent')
        if re.search(r'\b(?:AUTHOR|DISSENT_AUTHOR|CONCURRENCE_AUTHOR|ASSIGNMENT_PENDING|OTHER_MAJORITY|OTHER_DISSENTERS)\b', text):
            errors.append(row['file'] + ': unresolved author/assignment placeholder')
        if re.search(r'(?i)\b(?:simulated|user-directed|workflow|version / lineage|git-committed|research cutoff)\b|\b(?:runtime|freeze)/', projection):
            errors.append(row['file'] + ': public workflow/provenance leak')
        wordcounts = []
        for match in re.finditer(r'\*\*Controlling explanation[.:]?\*\*\s*', blocks['Holdings']):
            tail = blocks['Holdings'][match.end():]
            stop = re.search(r'\n(?:\*\*|#{2,6}\s)', tail)
            explanation = tail[:stop.start()] if stop else tail
            size = len(explanation.split())
            wordcounts.append(size)
            if size == 0 or size > 350:
                errors.append(row['file'] + ': controlling explanation has ' + str(size) + ' words (ceiling 350)')
        if not wordcounts:
            coverage.append(row['file'] + ': no labelled controlling explanation parsed; manual completeness review required')
        lengths[row['file']] = wordcounts
        check_link_targets(path, text, row['file'])

        participants = list(dict.fromkeys(names(blocks['Participation'])))
        if not participants:
            coverage.append(row['file'] + ': participation roster not parsed')
            continue
        judgment = blocks['Judgment & Remedy']
        support_match = re.search(r'\*\*Supporting[^*]*:\*\*\s*([^\n]+)', judgment)
        oppose_match = re.search(r'\*\*Opposing[^*]*:\*\*\s*([^\n]+)', judgment)
        shared_support = names(support_match[1]) if support_match else None
        shared_oppose = names(oppose_match[1]) if oppose_match else None
        table_lines = [line for line in judgment.splitlines() if line.startswith('|')]
        support_history, oppose_history = {}, {}
        tested = 0
        if table_lines:
            headers = cells(table_lines[0])
            for line in table_lines[2:]:
                values = cells(line)
                if len(values) != len(headers):
                    errors.append(row['file'] + ': judgment table column mismatch')
                    continue
                printed = VOTE.search(' | '.join(values))
                if not printed:
                    coverage.append(row['file'] + ': table disposition count not parsed: ' + values[0])
                    continue
                count = [int(item) for item in printed.groups() if item is not None]
                si = next((i for i, heading in enumerate(headers) if heading == 'Supporting'), None)
                oi = next((i for i, heading in enumerate(headers) if heading in {'Opposing', 'Other positions'}), None)
                supporting = group(values[si], participants, support_history) if si is not None else shared_support
                if supporting is not None:
                    support_history[len(supporting)] = supporting
                if len(count) == 3:
                    other_cells = values[oi].split(';') if oi is not None else []
                    others = [group(value.strip(), participants, oppose_history) for value in other_cells]
                    if len(others) != 2:
                        others = [None, None]
                else:
                    opposing = group(values[oi], participants, oppose_history) if oi is not None else shared_oppose
                    if opposing is None and count[1] == 0 and supporting is not None and len(supporting) == len(participants):
                        opposing = []
                    if opposing is not None:
                        oppose_history[len(opposing)] = opposing
                    others = [opposing]
                validate_groups(row['file'], values[0], count, [supporting, *others], participants)
                tested += 1
        else:
            printed = VOTE.search(judgment)
            if printed:
                count = [int(item) for item in printed.groups() if item is not None]
                opposing = shared_oppose
                if len(count) == 2 and count[1] == 0 and shared_support is not None:
                    opposing = []
                validate_groups(row['file'], 'Published judgment', count, [shared_support, opposing], participants)
                tested += 1
        if not tested:
            coverage.append(row['file'] + ': no published named judgment arithmetic parsed')

        topo_lines = [line for line in blocks['Opinion Topology'].splitlines() if line.startswith('|')]
        if topo_lines:
            for line in topo_lines[2:]:
                values = cells(line)
                if len(values) < 3:
                    continue
                authors = names(values[1])
                joins = names(values[2])
                if re.search(r'All (?:eight Associate|other) Justices', values[2], re.I):
                    joins = [name for name in participants if name not in authors]
                if len(authors + joins) != len(set(authors + joins)):
                    errors.append(row['file'] + ': duplicate author/joins in public topology row: ' + values[0])
                topology.append({'record': row['file'], 'writing': values[0], 'authors': authors, 'joins': joins,
                                 'total_named': len(set(authors + joins)), 'scope': values[3:]})
        elif 'unanimous Opinion of the Court' in blocks['Opinion Topology']:
            statement = blocks['Opinion Topology'].split('. ', 1)[0]
            named = names(statement)
            if len(named) != len(set(named)) or set(named) != set(participants):
                errors.append(row['file'] + ': unanimous topology sentence does not name every participant exactly once')
            topology.append({'record': row['file'], 'writing': 'Unanimous Opinion of the Court', 'named': named})
        else:
            coverage.append(row['file'] + ': nonunanimous topology prose remains for human component reconciliation')

    # Every saved assignment receipt is tested against actual preceding authors.
    assignments = []
    matched_records = set()
    for path in sorted((TERM / 'freeze').glob('OT_1998CHUNK7_*RECOUNT.json')):
        saved = json.loads(path.read_text(encoding='utf-8'))
        date, case = saved['before_date'], saved['before_case']
        preceding = [row for row in all_records if (row['date'], row['case'].casefold()) < (date, case.casefold())]
        totals = Counter({name: 0 for name in JUSTICES})
        counted = []
        for row in preceding:
            if row['file'] in previous_exclusions or re.search(r'\*\*Counted lead opinion:\*\*\s*No\b', row['text'], re.I):
                continue
            authors = sorted({author for author, _ in helper.lead_rows(row['text'])}, key=JUSTICES.index)
            if not authors:
                errors.append(path.name + ': no explicit exclusion or lead table for preceding ' + row['file'])
                continue
            totals.update(authors)
            counted.append({'record': row['file'], 'authors': authors})
        saved_authors = [{'record': item['record'], 'authors': item['authors']} for item in saved.get('counted', [])]
        last = counted[-1]['record'] if counted else None
        passed = dict(totals) == saved['counts'] and last == (saved.get('last_counted') or {}).get('record')
        if saved_authors != counted:
            passed = False
        if not passed:
            errors.append(path.name + ': saved counts, ordered authors, or last event differ from fresh actual tables')
        matches = [row for row in rows if row['date'] == date and (row['case'].casefold().startswith(case.casefold()))]
        matched_records.update(row['file'] for row in matches)
        if len(matches) != 1:
            errors.append(path.name + ': receipt does not identify exactly one existing new Record')
        assignments.append({'receipt': path.name, 'status': 'PASS' if passed else 'FLAG', 'before_date': date,
                            'before_case': case, 'counts': dict(totals), 'last_counted': last, 'counted_opinions': len(counted)})
    for row in rows:
        if re.search(r'\*\*Counted lead opinion:\*\*\s*Yes\b', row['text'], re.I) and row['file'] not in matched_records:
            errors.append(row['file'] + ': no matching sequential assignment receipt')

    baseline = json.loads((TERM / 'freeze' / 'OT_1998CHUNK7_BASELINE.json').read_text(encoding='utf-8'))
    preserved, skipped_workspace = [], []
    for name, digest in baseline.items():
        path = ROOT / name
        if '/workspace/' in name:
            skipped_workspace.append(name)
            continue
        if not any('/' + folder + '/' in name for folder in ('records', 'briefs', 'output')):
            coverage.append('Baseline item outside requested protected classes: ' + name)
            continue
        if not path.exists() or hashlib.sha256(path.read_bytes()).hexdigest() != digest:
            errors.append('Protected prior bytes changed: ' + name)
        else:
            preserved.append(name)

    # Render is a separate task; validate generated input only if already built.
    rin = TERM / 'render-inputs' / 'OT_1998CHUNK7.md'
    render_status = 'not yet present'
    if rin.exists():
        text = rin.read_text(encoding='utf-8')
        parts = list(re.finditer(r'<!-- source-record: ([^>]+) -->\n(.*?)(?=\n---\n|\Z)', text, re.S))
        actual = [part[1].strip() for part in parts]
        expected = [row['file'] for row in sorted(rows, key=lambda row: (row['date'], row['case']))]
        if actual != expected:
            errors.append('Render Input membership/order differs from completed new Records')
        sources = {row['file']: row.get('projection') for row in rows}
        for part in parts:
            if part[2].strip() != sources.get(part[1].strip()):
                errors.append('Render Input projection mismatch: ' + part[1].strip())
        check_link_targets(rin, text, rin.name)
        # Public block links were written relative to Records; the sibling
        # render-inputs directory has the same term-relative depth.
        render_status = 'present and checked'
    elif args.partial:
        coverage.append('Generated chunk 7 Render Input not yet present; projection identity awaits integration')
    else:
        errors.append('Final validation requires generated chunk 7 Render Input')

    additions = {}
    for kind in ('manifest', 'continuity', 'neutral-projection', 'ledger'):
        path = TERM / 'workspace' / (kind + '.md')
        current = path.read_text(encoding='utf-8')
        baseline_key = path.relative_to(ROOT).as_posix()
        if hashlib.sha256(path.read_bytes()).hexdigest() == baseline.get(baseline_key):
            additions[kind] = {'unchanged': True, 'added_lines_checked': 0}
            continue
        opening = TERM / 'freeze' / ('OT_1998CHUNK7_OPENING_' + kind.upper().replace('-', '_') + '.md')
        if opening.exists():
            old_lines, new_lines = opening.read_text(encoding='utf-8').splitlines(), current.splitlines()
            added = []
            for operation, _a, _b, start, end in difflib.SequenceMatcher(a=old_lines, b=new_lines, autojunk=False).get_opcodes():
                if operation in {'insert', 'replace'}:
                    added.extend(new_lines[start:end])
        elif kind == 'ledger':
            # The baseline preserves only its digest. Inspect all current ledger
            # URL text and links, and flag that exact line-diff attribution is absent.
            added = current.splitlines()
            coverage.append('Ledger changed and has no opening text copy: all current ledger links/URLs checked; exact added-line attribution unavailable')
        else:
            errors.append('Missing opening workspace text for addition checks: ' + kind)
            added = current.splitlines()
        check_link_targets(path, '\n'.join(added), 'workspace/' + kind + '.md additions')
        additions[kind] = {'unchanged': False, 'added_lines_checked': len(added)}

    status = 'FAIL' if errors else ('PARTIAL PASS' if args.partial else 'PASS')
    result = {'status': status, 'errors': errors, 'coverage_limits': list(dict.fromkeys(coverage)),
              'checker_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              'event_count': len(rows), 'expected_events': args.expected_events,
              'events': [{key: row[key] for key in ('file', 'date', 'case')} for row in rows],
              'controlling_explanation_word_counts': lengths, 'named_vote_checks': votes,
              'topology_named_rosters': topology, 'assignment_receipt_checks': assignments,
              'protected_baseline_files_verified': len(preserved), 'baseline_files_total': len(baseline),
              'mutable_workspace_hashes_skipped': skipped_workspace, 'local_links_checked': len(links),
              'local_link_results': links, 'workspace_additions': additions, 'render_input': render_status,
              'limitations': ['No substantive coalition, qualification, source-support, or remedy decision is made.',
                             'Topology-to-judgment legal scope reconciliation remains a human task.',
                             'External URL availability is not tested.',
                             'Git existence, history, commitment status and commitment order are unverified.',
                             'The general term checker is reserved to root and was not called.'],
              'mutation': 'Only this new audit receipt; no Record, workspace, brief, source, or infrastructure edit.'}
    receipt.write_text(json.dumps(result, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')
    print(json.dumps({key: result[key] for key in ('status', 'errors', 'coverage_limits', 'event_count',
                     'protected_baseline_files_verified', 'local_links_checked')}, indent=2, ensure_ascii=False))
    print('Receipt: ' + str(receipt))
    raise SystemExit(bool(errors))


if __name__ == '__main__':
    main()
