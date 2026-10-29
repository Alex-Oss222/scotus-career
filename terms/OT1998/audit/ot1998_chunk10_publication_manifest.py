#!/usr/bin/env python3
"""Mechanical OT1998 Chunk10 publication inventory. Run with python -B.

Default mode is a read-only dry run. Final emission requires both --emit-final
and --writers-finished, and fails on unauthorized baseline mutations, missing
linked term files, unsafe paths, or files changing during inspection. No Git,
network access, global listing, legal interpretation, or substantive writes.
Only explicit term directories are scanned; exact receipt entries are hashed.
"""
from __future__ import annotations

import argparse
from collections import Counter, deque
import hashlib
import html
import json
import os
from pathlib import Path, PurePosixPath
import posixpath
import re
import stat
import sys
from urllib.parse import unquote, urlsplit

sys.dont_write_bytecode = True
ROOT = Path(__file__).absolute().parents[3]
TERM = 'terms/OT1998'
ALLOWED_DIRS = frozenset({'audit', 'briefs', 'entering-law', 'freeze', 'output',
                          'records', 'render-inputs', 'research', 'runtime',
                          'sources', 'workspace'})
RECEIPT = TERM + '/freeze/OT_1998CHUNK10_SOURCE_FRESHNESS.json'
PRIOR = TERM + '/freeze/OT_1998CHUNK10_PRIOR_PUBLIC_SOURCES.json'
PRIOR_RECORDS = TERM + '/freeze/OT_1998CHUNK10_PRIOR_RECORD_LINK_TARGETS.json'
FINAL = TERM + '/audit/OT_1998CHUNK10_PUBLICATION_MANIFEST.json'
WORKSPACE = {TERM + '/workspace/' + name + '.md' for name in
             ('manifest', 'ledger', 'continuity', 'neutral-projection')}
SNAPSHOTS = {TERM + '/freeze/OT_1998CHUNK10_OPENING_' + label + '.md':
             TERM + '/workspace/' + name + '.md' for label, name in (
                 ('MANIFEST', 'manifest'), ('LEDGER', 'ledger'),
                 ('CONTINUITY', 'continuity'),
                 ('NEUTRAL_PROJECTION', 'neutral-projection'))}
CURRENT_RECORDS = frozenset({
    'west_v_gibson_merits_1999-06-14.md',
    'schleifer_v_city_of_charlottesville_merits_1999-06-15.md',
    'grupo_mexicano_de_desarrollo_sa_v_alliance_bond_fund_inc_merits_1999-06-17.md',
    'nasa_v_flra_merits_1999-06-17.md',
    'strickler_v_greene_merits_1999-06-17.md',
    'valdespino_v_alamo_heights_independent_school_district_merits_1999-06-17.md',
    'city_of_dallas_v_dallas_fire_fighters_association_merits_1999-06-18.md',
    'maryland_v_dyson_certiorari_1999-06-21.md',
    'maryland_v_dyson_summary_merits_1999-06-21.md',
    'jones_v_united_states_merits_1999-06-21.md',
    'martin_v_hadix_merits_1999-06-21.md',
    'sutton_v_united_air_lines_inc_merits_1999-06-22.md',
    'jefferson_county_v_acker_merits_1999-06-21.md',
})
BROAD = {TERM + '/research/chunk10_root/' + name for name in (
    'USCODE-1998-title28-mods.xml', 'USCODE-1998-title28.txt',
    'USCODE-1998-title28.pdf')}
CACHE_PARTS = frozenset({'__pycache__', '.pytest_cache', '.mypy_cache',
                         '.ruff_cache', '.git', '.cache', 'tmp', 'temp'})
CHUNK10 = re.compile(r'chunk10(?!\d)', re.I)
SCHEME = re.compile(r'^[A-Za-z][A-Za-z0-9+.-]*:')
MAX_FILES = 10000
MAX_MARKDOWN_BYTES = 32 * 1024 * 1024


class UnsafePath(ValueError):
    pass


def checked_rel(value):
    """Reject forbidden names lexically, before any filesystem operation."""
    if not isinstance(value, str) or not value or '\\' in value:
        raise UnsafePath('invalid relative path')
    parts = PurePosixPath(value).parts
    if value.startswith('/') or any(p in ('..', '.') for p in value.split('/')):
        raise UnsafePath('path is not a normalized repository-relative path')
    if any(p.casefold() == 'stone' or p.upper().startswith('MASTER_JURISPRUDENCE')
           for p in parts):
        raise UnsafePath('forbidden path component')
    if not parts:
        raise UnsafePath('empty path')
    return '/'.join(parts)


def safe_path(rel):
    rel = checked_rel(rel)
    path = ROOT
    # Never follow any symlink, including an intermediate directory symlink.
    for part in PurePosixPath(rel).parts:
        path = path / part
        try:
            mode = path.lstat().st_mode
        except FileNotFoundError:
            continue
        if stat.S_ISLNK(mode):
            raise UnsafePath('symlink path rejected: ' + rel)
    return path


def read_bytes(rel):
    path = safe_path(rel)
    with path.open('rb') as stream:
        before = os.fstat(stream.fileno())
        if not stat.S_ISREG(before.st_mode):
            raise UnsafePath('not a regular file: ' + rel)
        data = stream.read()
        after = os.fstat(stream.fileno())
    current = path.stat()
    ident = lambda s: (s.st_dev, s.st_ino, s.st_size, s.st_mtime_ns)
    if ident(before) != ident(after) or ident(after) != ident(current):
        raise UnsafePath('file changed during inspection: ' + rel)
    return data


def identity(rel):
    data = read_bytes(rel)
    return {'path': rel, 'bytes': len(data),
            'sha256': hashlib.sha256(data).hexdigest()}


def load_receipt(rel):
    raw = read_bytes(rel)
    data = json.loads(raw)
    entries = {}
    for entry in data['files']:
        name = checked_rel(entry['path'])
        if name in entries:
            raise ValueError('duplicate receipt entry: ' + name)
        if not re.fullmatch(r'[0-9a-f]{64}', entry['sha256']):
            raise ValueError('invalid receipt SHA256: ' + name)
        entries[name] = {'path': name,
                         'bytes': entry.get('size', entry.get('bytes')),
                         'sha256': entry['sha256']}
    return data, entries, {'path': rel, 'bytes': len(raw), 'sha256': hashlib.sha256(raw).hexdigest()}


def remember_parsed(identities, rel, raw):
    actual = {'path': rel, 'bytes': len(raw), 'sha256': hashlib.sha256(raw).hexdigest()}
    previous = identities.setdefault(rel, actual)
    if previous != actual:
        raise ValueError('input changed between inventory reads: ' + rel)


def term_allowed(rel):
    parts = PurePosixPath(checked_rel(rel)).parts
    return (len(parts) >= 3 and parts[0] == 'terms' and
            re.fullmatch(r'OT\d{4}', parts[1]) and
            (parts[2] in ALLOWED_DIRS or
             (len(parts) == 3 and parts[2] == 'case-list.md')))


def excluded(rel, final_name):
    parts = PurePosixPath(rel).parts
    name = parts[-1]
    if rel == final_name:
        return 'manifest_itself'
    if rel in BROAD:
        return 'unused_broad_retrieval'
    if any(p in CACHE_PARTS for p in parts) or name.endswith(('.pyc', '.pyo', '.tmp', '.temp', '.swp', '~')):
        return 'cache_or_temporary'
    if name.upper().endswith(('_ASSEMBLY_DRAFT.MD', '_RECORD_DRAFT.MD')):
        return 'preparatory_draft'
    return None


def scan_term():
    """Scan only explicitly allowed directories, pruning before descent."""
    for dirname in sorted(ALLOWED_DIRS):
        relbase = TERM + '/' + dirname
        base = safe_path(relbase)
        if not base.exists():
            continue
        for directory, dirs, files in os.walk(base, topdown=True, followlinks=False):
            kept = []
            for name in sorted(dirs):
                if name.casefold() == 'stone' or name.upper().startswith('MASTER_JURISPRUDENCE') or name in CACHE_PARTS:
                    continue
                child = Path(directory) / name
                if child.is_symlink():
                    raise UnsafePath('symlink directory rejected: ' + child.relative_to(ROOT).as_posix())
                kept.append(name)
            dirs[:] = kept
            for name in sorted(files):
                if name.casefold() == 'stone' or name.upper().startswith('MASTER_JURISPRUDENCE'):
                    continue
                yield checked_rel((Path(directory) / name).relative_to(ROOT).as_posix())


def authorized_new(rel, extra):
    if rel in extra:
        return True
    parts = PurePosixPath(rel).parts
    if len(parts) < 4 or '/'.join(parts[:2]) != TERM:
        return False
    if parts[2] in ('records', 'entering-law') and parts[-1] in CURRENT_RECORDS:
        return True
    if parts[2] == 'research' and parts[-1].startswith('JONES_FRESH_HISTORICAL'):
        return True
    return (parts[2] in ALLOWED_DIRS - {'briefs', 'workspace', 'records'} and
            bool(CHUNK10.search('/'.join(parts[3:]))))


def markdown_text(data, strip_inline=True):
    text = data.decode('utf-8-sig')
    # Code is not a rendered Markdown link. Keep newlines for line locations.
    lines = text.splitlines(keepends=True)
    fence = None
    for i, line in enumerate(lines):
        match = re.match(r'^\s{0,3}(`{3,}|~{3,})', line)
        if match:
            marker = match.group(1)
            if fence is None:
                fence = marker
            elif marker[0] == fence[0] and len(marker) >= len(fence):
                fence = None
            lines[i] = '\n' if line.endswith('\n') else ''
        elif fence is not None:
            lines[i] = '\n' if line.endswith('\n') else ''
    text = ''.join(lines)
    return re.sub(r'(`+)([^`\n]*?)\1', '', text) if strip_inline else text


def destinations(data):
    """Bounded Markdown inline and reference-definition target extraction."""
    text = markdown_text(data)
    found = []
    # Only used reference definitions create dependencies. Footnotes do not.
    normalize_label = lambda value: ' '.join(value.casefold().split())
    definitions, definition_spans = {}, []
    for match in re.finditer(r'^\s{0,3}\[([^\]\n]+)\]:\s*(<[^>\n]*>|\S+)[^\n]*', text, re.M):
        if not match.group(1).startswith('^'):
            definitions.setdefault(normalize_label(match.group(1)), match.group(2).strip('<>'))
        definition_spans.append(match.span())
    for match in re.finditer(r'(?<!\\)\[([^\]\n]+)\](?:\[([^\]\n]*)\])?', text):
        if any(start <= match.start() < end for start, end in definition_spans):
            continue
        if text[match.end():match.end() + 1] == '(':
            continue
        label = normalize_label(match.group(2) or match.group(1))
        if label in definitions:
            found.append((match.start(), definitions[label]))
    # Inline links/images: balance parentheses and support angle destinations.
    for start in re.finditer(r'(?<!\\)\]\(', text):
        pos = start.end()
        while pos < len(text) and text[pos] in ' \t':
            pos += 1
        if pos >= len(text):
            continue
        if text[pos] == '<':
            end = text.find('>', pos + 1)
            if end >= 0 and '\n' not in text[pos:end]:
                found.append((start.start(), text[pos + 1:end]))
            continue
        end, depth = pos, 0
        while end < len(text):
            char = text[end]
            if char == '\\' and end + 1 < len(text):
                end += 2
                continue
            if char == '(':
                depth += 1
            elif char == ')':
                if depth == 0:
                    break
                depth -= 1
            elif char.isspace() and depth == 0:
                break
            end += 1
        if end > pos:
            found.append((start.start(), text[pos:end]))
    return [(html.unescape(re.sub(r'\\([\\() ])', r'\1', target)),
             text.count('\n', 0, pos) + 1) for pos, target in sorted(set(found))]


def resolve_target(source, target):
    if SCHEME.match(target) or target.startswith('//'):
        return None
    parsed = urlsplit(target)
    raw = unquote(parsed.path)
    anchor = unquote(parsed.fragment)
    if raw.startswith(str(ROOT) + '/'):
        rel = raw[len(str(ROOT)) + 1:]
    elif raw.startswith('/'):
        rel = raw.lstrip('/')
    else:
        rel = posixpath.normpath(posixpath.join(posixpath.dirname(source), raw)) if raw else source
    return checked_rel(rel), anchor


def anchors(data):
    text = markdown_text(data, strip_inline=False)
    result = set(re.findall(r'<[^>]+\b(?:id|name)=["\']([^"\']+)["\']', text))
    repeats = Counter()
    for match in re.finditer(r'^\s{0,3}#{1,6}\s+(.+?)\s*#*\s*$', text, re.M):
        label = re.sub(r'\[([^\]]+)\]\([^)]*\)', r'\1', match.group(1))
        label = re.sub(r'<[^>]+>', '', html.unescape(label)).strip().lower()
        slug = ''.join(c for c in label if c.isalnum() or c in '_- ')
        slug = slug.replace(' ', '-')
        suffix = repeats[slug]
        repeats[slug] += 1
        result.add(slug + ('-' + str(suffix) if suffix else ''))
    return result


def run(args):
    final_name = checked_rel(args.manifest)
    if final_name != FINAL:
        raise ValueError('manifest output must use the fixed designated publication-manifest path')
    extra = {checked_rel(p) for p in args.allow_new}
    if any(not p.startswith(TERM + '/') or not term_allowed(p) for p in extra):
        raise ValueError('--allow-new must name an exact allowed OT1998 file')
    metadata, baseline, baseline_receipt_identity = load_receipt(RECEIPT)
    prior_metadata, prior, prior_receipt_identity = load_receipt(PRIOR)
    if metadata['source_commit'] != prior_metadata['source_commit']:
        raise ValueError('receipts have different source commits')
    prior_record_metadata, prior_records, prior_record_receipt_identity = load_receipt(PRIOR_RECORDS)
    if metadata['source_commit'] != prior_record_metadata['source_commit']:
        raise ValueError('prior Record receipt has a different source commit')
    if final_name in baseline or final_name in prior or final_name in prior_records:
        raise ValueError('designated manifest unexpectedly belongs to protected baseline')
    report = {
        'mode': 'final' if args.emit_final else 'dry-run',
        'source_commit': metadata['source_commit'],
        'baseline_file_count': len(baseline),
        'prior_public_source_count': len(prior),
        'prior_record_dependency_count': len(prior_records),
        'baseline_mutations': [], 'baseline_missing': [],
        'prior_public_mutations': [], 'prior_public_missing': [],
        'prior_record_mutations': [], 'prior_record_missing': [],
        'authorized_workspace_changes': [], 'excluded_files': [],
        'unclassified_new_files': [], 'dependency_files': [],
        'missing_linked_term_targets': [], 'missing_target_references': [],
        'missing_anchors': [], 'outside_term_link_count': 0,
        'forbidden_or_unsafe_links': [], 'snapshot_context_links': [],
        'inventory_changed_during_scan': [],
        'snapshot_context_policy': 'Controller-authorized: byte-identical opening snapshots retain original workspace link context; literal relocated targets are disclosed separately.',
    }
    current = {}
    for collection, changes, missing in (
        (baseline, 'baseline_mutations', 'baseline_missing'),
        (prior, 'prior_public_mutations', 'prior_public_missing'),
        (prior_records, 'prior_record_mutations', 'prior_record_missing')):
        for rel, expected in sorted(collection.items()):
            try:
                actual = identity(rel)
            except FileNotFoundError:
                report[missing].append(rel)
                continue
            current[rel] = actual
            if actual['bytes'] != expected['bytes'] or actual['sha256'] != expected['sha256']:
                item = {'path': rel, 'expected': expected, 'actual': actual}
                if collection is baseline and rel in WORKSPACE:
                    report['authorized_workspace_changes'].append(rel)
                else:
                    report[changes].append(item)
    selected = {p for p in report['authorized_workspace_changes']}
    for rel in scan_term():
        if rel in baseline or rel in prior:
            continue
        reason = excluded(rel, final_name)
        if reason:
            report['excluded_files'].append({'path': rel, 'reason': reason})
        elif authorized_new(rel, extra):
            selected.add(rel)
        else:
            report['unclassified_new_files'].append(rel)
    if len(selected) > MAX_FILES:
        raise ValueError('file inventory bound exceeded')
    # Verify opening snapshots against receipt bytes before using them to
    # distinguish original workspace links from newly introduced links.
    old_targets, snapshot_context = {}, {}
    parsed_identities = {item['path']: item for item in (
        baseline_receipt_identity, prior_receipt_identity, prior_record_receipt_identity)}
    for snap, original in SNAPSHOTS.items():
        raw = read_bytes(snap)
        remember_parsed(parsed_identities, snap, raw)
        if hashlib.sha256(raw).hexdigest() != baseline[original]['sha256']:
            raise ValueError('opening snapshot does not match baseline: ' + snap)
        old_targets[original] = {target for target, _ in destinations(raw)}
        snapshot_context[snap] = original
    pending = deque(sorted(selected))
    inspected, anchor_cache, missing = set(), {}, set()
    while pending:
        rel = pending.popleft()
        if rel in inspected:
            continue
        inspected.add(rel)
        if len(inspected) > MAX_FILES:
            raise ValueError('dependency inventory bound exceeded')
        if not rel.lower().endswith('.md'):
            continue
        raw = read_bytes(rel)
        remember_parsed(parsed_identities, rel, raw)
        if len(raw) > MAX_MARKDOWN_BYTES:
            raise ValueError('Markdown inventory byte bound exceeded: ' + rel)
        source = snapshot_context.get(rel, rel)
        for target, line in destinations(raw):
            inherited = (rel in snapshot_context or target in old_targets.get(rel, set()))
            origin = 'baseline-existing' if inherited else 'new'
            ref = {'source': rel, 'line': line, 'link': target, 'origin': origin}
            try:
                resolved = resolve_target(source, target)
                if resolved is None:
                    continue
                dest, anchor = resolved
                if rel in snapshot_context and source != rel:
                    literal = resolve_target(rel, target)
                    if literal != resolved:
                        report['snapshot_context_links'].append({**ref, 'baseline_source': source,
                                                                 'literal_target': literal[0],
                                                                 'baseline_target': dest})
                if not dest.startswith('terms/'):
                    report['outside_term_link_count'] += 1
                    continue
                if not term_allowed(dest):
                    raise UnsafePath('term target is outside known allowed directories')
                path = safe_path(dest)
                if not path.is_file():
                    missing.add(dest)
                    report['missing_target_references'].append({**ref, 'target': dest, 'anchor': anchor})
                    continue
                reason = excluded(dest, final_name)
                if reason and reason != 'preparatory_draft':
                    raise UnsafePath('linked target is excluded: ' + reason)
                if dest.startswith(TERM + '/') and dest not in baseline and dest not in selected:
                    selected.add(dest)
                    pending.append(dest)
                    report['dependency_files'].append(dest)
                if anchor and dest.lower().endswith('.md'):
                    if dest not in anchor_cache:
                        anchor_raw = read_bytes(dest)
                        remember_parsed(parsed_identities, dest, anchor_raw)
                        anchor_cache[dest] = anchors(anchor_raw)
                    if anchor not in anchor_cache[dest]:
                        report['missing_anchors'].append({**ref, 'target': dest, 'anchor': anchor})
            except (UnsafePath, ValueError) as exc:
                report['forbidden_or_unsafe_links'].append({**ref, 'reason': str(exc)})
    report['missing_linked_term_targets'] = sorted(missing)
    report['dependency_files'].sort()
    report['unclassified_new_files'] = [p for p in report['unclassified_new_files'] if p not in selected]
    report['excluded_files'] = [e for e in report['excluded_files'] if e['path'] not in selected]
    files = [identity(rel) for rel in sorted(selected)]
    for rel, parsed in parsed_identities.items():
        if identity(rel) != parsed:
            report['inventory_changed_during_scan'].append(rel)
    report['files'] = files
    report['file_count'] = len(files)
    report['total_bytes'] = sum(f['bytes'] for f in files)
    report['selected_directory_counts'] = dict(sorted(Counter(PurePosixPath(f['path']).parts[2] for f in files).items()))
    report['markdown_files_inspected'] = sum(p.lower().endswith('.md') for p in inspected)
    blocking = ('baseline_mutations', 'baseline_missing', 'prior_public_mutations',
                'prior_public_missing', 'prior_record_mutations', 'prior_record_missing',
                'missing_linked_term_targets', 'forbidden_or_unsafe_links',
                'unclassified_new_files', 'missing_anchors', 'inventory_changed_during_scan')
    report['blocking_issue_count'] = sum(len(report[k]) for k in blocking)
    if args.emit_final:
        if not args.writers_finished:
            raise ValueError('--emit-final requires controller confirmation via --writers-finished')
        if report['blocking_issue_count']:
            raise ValueError('final emission blocked; run dry-run and inspect report')
        # Recheck every selected identity to catch changes during the inventory.
        for item in files:
            if identity(item['path']) != item:
                raise ValueError('selected file changed during final inventory: ' + item['path'])
        for rel, expected in {**baseline, **prior, **prior_records}.items():
            if rel not in WORKSPACE and identity(rel) != expected:
                raise ValueError('protected file changed during final inventory: ' + rel)
        for rel, parsed in parsed_identities.items():
            if identity(rel) != parsed:
                raise ValueError('Markdown input changed after link inventory: ' + rel)
        manifest = {'files': files, 'file_count': report['file_count'],
                    'total_bytes': report['total_bytes'], 'missing_linked_term_targets': []}
        encoded = (json.dumps(manifest, indent=2, ensure_ascii=False) + '\n').encode()
        output = safe_path(final_name)
        temporary = safe_path(final_name + '.tmp')
        temporary.write_bytes(encoded)
        os.replace(temporary, output)
        report['manifest_identity'] = identity(final_name)
    return report


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--dry-run', action='store_true', help='default; never emits a manifest')
    parser.add_argument('--emit-final', action='store_true')
    parser.add_argument('--writers-finished', action='store_true')
    parser.add_argument('--manifest', default=FINAL)
    parser.add_argument('--allow-new', action='append', default=[], metavar='EXACT_REPO_PATH')
    parser.add_argument('--report', help='optional dry-run/detail report, only under /tmp')
    args = parser.parse_args()
    if args.dry_run and args.emit_final:
        parser.error('--dry-run and --emit-final are mutually exclusive')
    try:
        report = run(args)
        if args.report:
            output = Path(args.report).absolute()
            if '/tmp' not in [str(p) for p in output.parents] or '..' in output.parts:
                raise ValueError('--report must be under /tmp')
            if output.is_symlink():
                raise UnsafePath('symlink report rejected')
            if any(parent.is_symlink() for parent in output.parents):
                raise UnsafePath('symlink report parent rejected')
            output.write_text(json.dumps(report, indent=2, ensure_ascii=False) + '\n')
        summary = {k: v for k, v in report.items() if k not in ('files', 'missing_anchors', 'snapshot_context_links', 'excluded_files', 'missing_target_references')}
        summary['missing_anchor_count'] = len(report['missing_anchors'])
        summary['snapshot_context_link_count'] = len(report['snapshot_context_links'])
        summary['excluded_file_count'] = len(report['excluded_files'])
        if args.report:
            summary['detail_report'] = args.report
        print(json.dumps(summary, indent=2, ensure_ascii=False))
        return 0 if not report['blocking_issue_count'] else 2
    except (ValueError, OSError, UnicodeError) as exc:
        print('publication inventory failed: ' + str(exc), file=sys.stderr)
        return 2


if __name__ == '__main__':
    raise SystemExit(main())
