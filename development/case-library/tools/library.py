#!/usr/bin/env python3
"""Isolated, fail-closed source catalogue. Never writes authoritative sources."""
from __future__ import annotations

import argparse
from contextlib import contextmanager
from copy import deepcopy
import fcntl
import hashlib
import json
import math
import os
from pathlib import Path, PurePosixPath
import re
import shutil
import sys
import uuid

from jsonschema import Draft202012Validator, FormatChecker
from ingest import build_catalogue
from presentation import render

TERMS = ('OT1991', 'OT1992', 'OT1993', 'OT1994', 'OT1995')
BASE = 'development/case-library'
HEX = re.compile(r'^[a-f0-9]{64}$')


class LibraryError(ValueError):
    pass


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def json_bytes(value) -> bytes:
    return (json.dumps(value, ensure_ascii=False, sort_keys=True, indent=2, allow_nan=False) + '\n').encode('utf-8')


def _pairs(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise LibraryError(f'Duplicate JSON key: {key}')
        result[key] = value
    return result


def _constant(value):
    raise LibraryError(f'Non-finite JSON number: {value}')


def _float(value):
    parsed = float(value)
    if not math.isfinite(parsed):
        raise LibraryError(f'Non-finite JSON number: {value}')
    return parsed


def read_json(path: Path):
    try:
        return json.loads(path.read_bytes(), object_pairs_hook=_pairs, parse_constant=_constant, parse_float=_float)
    except (UnicodeError, json.JSONDecodeError, OSError) as exc:
        raise LibraryError(f'Cannot read JSON {path}: {exc}') from exc


def safe_path(root: Path, relative: str, *, must_exist=True) -> Path:
    if not isinstance(relative, str) or not relative or '\\' in relative or '\x00' in relative:
        raise LibraryError(f'Invalid repository path: {relative!r}')
    pure = PurePosixPath(relative)
    if pure.is_absolute() or '..' in pure.parts or pure.as_posix() != relative:
        raise LibraryError(f'Noncanonical repository path: {relative!r}')
    root = root.resolve(strict=True)
    current = root
    for part in pure.parts:
        current = current / part
        if current.is_symlink():
            raise LibraryError(f'Symlink is not permitted: {relative}')
    if must_exist and not current.exists():
        raise LibraryError(f'Missing repository path: {relative}')
    if not current.resolve().is_relative_to(root):
        raise LibraryError(f'Path escapes repository: {relative}')
    return current


def _schema(root: Path, filename: str):
    schema = read_json(safe_path(root, f'{BASE}/schemas/{filename}'))
    Draft202012Validator.check_schema(schema)
    return Draft202012Validator(schema, format_checker=FormatChecker())


def validate_catalogue(root: Path, catalogue: dict):
    errors = sorted(_schema(root, 'catalogue.schema.json').iter_errors(catalogue), key=lambda e: str(e.path))
    if errors:
        raise LibraryError('Catalogue schema: ' + '; '.join(f'{list(e.path)}: {e.message}' for e in errors[:5]))
    record_ids = [r['record_id'] for r in catalogue['records']]
    paths = [r['path'] for r in catalogue['records']]
    if len(record_ids) != len(set(record_ids)) or len(paths) != len(set(paths)):
        raise LibraryError('Duplicate Record identity or path')
    known = set(record_ids)
    for record in catalogue['records']:
        if record['term'] not in catalogue['scope']['terms']:
            raise LibraryError('Record crosses selected term scope')
        if record['path'] not in catalogue['sources'] or catalogue['sources'][record['path']]['sha256'] != record['sha256']:
            raise LibraryError('Record fingerprint is not bound to source')
        safe_path(root, record['path'], must_exist=False)
        for pointer in record['references']:
            if pointer['source_path'] not in catalogue['sources']:
                raise LibraryError('Reference provenance is not fingerprinted')
            if pointer['kind'] == 'repository':
                safe_path(root, pointer['target'].partition('#')[0], must_exist=False)
            elif pointer['kind'] == 'external':
                from urllib.parse import urlsplit
                parts = urlsplit(pointer['target'])
                if parts.scheme not in ('http', 'https') or not parts.hostname or parts.username or parts.password or any(c.isspace() for c in pointer['target']):
                    raise LibraryError('Unsafe external reference URL')
    for row in catalogue['inventory']:
        if not set(row['resolved_record_ids']) <= known:
            raise LibraryError('Inventory links an unknown Record')
    for summary in catalogue['terms']:
        entries = [r for r in catalogue['records'] if r['term'] == summary['term']]
        rows = [r for r in catalogue['inventory'] if r['term'] == summary['term']]
        expected = (len(entries), sum(r['kind'] == 'court_event' for r in entries), sum(r['kind'] == 'admitted_source' for r in entries), len(rows), sum(bool(r['resolved_record_ids']) for r in rows))
        actual = tuple(summary[k] for k in ('record_count', 'court_event_count', 'admitted_source_count', 'inventory_count', 'mapped_inventory_count'))
        if actual != expected:
            raise LibraryError(f'Incorrect coverage counts: {summary["term"]}')


def _membership(root: Path, directory: str) -> list[str]:
    path = safe_path(root, directory)
    result = []
    for child in sorted(path.iterdir()):
        if child.is_symlink():
            raise LibraryError(f'Symlink in input directory: {child}')
        if child.is_file() and (child.suffix == '.md' if directory.startswith('terms/') else child.suffix in ('.py', '.json')):
            result.append(child.relative_to(root).as_posix())
    return result


def collect(root: Path, terms=TERMS) -> dict:
    root = root.resolve()
    terms = tuple(terms)
    if not terms or len(set(terms)) != len(terms) or any(t not in TERMS for t in terms):
        raise LibraryError('Invalid term scope')
    config = read_json(safe_path(root, f'{BASE}/inputs/config.json'))
    if set(config) != {'schema_version', 'source_revision', 'terms'} or type(config['schema_version']) is not int or config['schema_version'] != 2 or config['terms'] != list(TERMS):
        raise LibraryError('Invalid rebuild configuration')
    annotations_path = safe_path(root, f'{BASE}/inputs/annotations.json')
    annotations = read_json(annotations_path)
    errors = list(_schema(root, 'annotations.schema.json').iter_errors(annotations))
    if errors:
        raise LibraryError('Annotations schema: ' + errors[0].message)
    try:
        data = build_catalogue(root, list(terms))
    except (ValueError, OSError, KeyError, AssertionError) as exc:
        raise LibraryError(f'Cannot collect canonical inputs: {exc}') from exc
    known = {r['record_id'] for r in data['records']}
    if set(annotations['entries']) - known:
        raise LibraryError('Annotations refer to unknown or out-of-scope Record identities')
    for record in data['records']:
        record['curation'] = deepcopy(annotations['entries'].get(record['record_id'], {'aliases': [], 'notes': [], 'extensions': {}}))
    citation_index = {}
    for record in data['records']:
        for mention in record['citations']:
            key = ' '.join(mention['text'].split())
            citation_index.setdefault(key, []).append({'record_id': record['record_id'], **mention})
    directories = [f'terms/{t}/{folder}' for t in terms for folder in ('records', 'render-inputs', 'output')]
    directories += [f'{BASE}/{folder}' for folder in ('tools', 'schemas', 'inputs')]
    memberships = {d: _membership(root, d) for d in directories if safe_path(root, d, must_exist=False).exists()}
    for directory, names in memberships.items():
        if directory.startswith(BASE):
            for name in names:
                raw = safe_path(root, name).read_bytes()
                data['sources'][name] = {'sha256': digest(raw), 'size': len(raw)}
    result = {'schema_version': 2, 'development_only': True, 'production_integration': False,
              'scope': {'terms': list(terms), 'source_revision': config['source_revision']},
              **data, 'directory_memberships': memberships, 'citation_index': citation_index}
    validate_catalogue(root, result)
    _fresh(root, result)
    return result


def _fresh(root: Path, catalogue: dict):
    for relative, expected in catalogue['sources'].items():
        raw = safe_path(root, relative).read_bytes()
        if len(raw) != expected['size'] or digest(raw) != expected['sha256']:
            raise LibraryError(f'Stale source: {relative}')
    for directory, expected in catalogue['directory_memberships'].items():
        if _membership(root, directory) != expected:
            raise LibraryError(f'Input directory membership changed: {directory}')


def _pointer(root: Path):
    path = safe_path(root, f'{BASE}/CURRENT.json')
    pointer = read_json(path)
    if not isinstance(pointer, dict) or set(pointer) != {'schema_version', 'build_id', 'manifest_sha256'} or type(pointer['schema_version']) is not int or pointer['schema_version'] != 2 or not all(isinstance(pointer[k], str) and HEX.fullmatch(pointer[k]) for k in ('build_id', 'manifest_sha256')):
        raise LibraryError('Invalid current snapshot pointer')
    return pointer


def _verify(root: Path, folder: Path, pointer: dict) -> dict:
    if folder.name != pointer['build_id'] or folder.is_symlink():
        raise LibraryError('Snapshot identity/path mismatch')
    manifest_path = safe_path(root, (folder / 'manifest.json').relative_to(root).as_posix())
    raw = manifest_path.read_bytes()
    if digest(raw) != pointer['manifest_sha256']:
        raise LibraryError('Snapshot manifest checksum mismatch')
    manifest = read_json(manifest_path)
    if not isinstance(manifest, dict) or set(manifest) != {'schema_version', 'build_id', 'content_id', 'files'} or type(manifest['schema_version']) is not int or manifest['schema_version'] != 2 or manifest['build_id'] != folder.name or not isinstance(manifest['content_id'], str) or not HEX.fullmatch(manifest['content_id']):
        raise LibraryError('Invalid snapshot manifest')
    if not isinstance(manifest['files'], dict) or set(manifest['files']) != {'catalogue.json', 'index.html'}:
        raise LibraryError('Unexpected snapshot manifest layout')
    if {p.name for p in folder.iterdir()} != {'catalogue.json', 'index.html', 'manifest.json'}:
        raise LibraryError('Unexpected snapshot files')
    files = {}
    for name, expected in manifest['files'].items():
        path = safe_path(root, (folder/name).relative_to(root).as_posix())
        raw = path.read_bytes()
        if not isinstance(expected, str) or not HEX.fullmatch(expected) or digest(raw) != expected:
            raise LibraryError(f'Snapshot output checksum mismatch: {name}')
        files[name] = raw
    if digest(files['catalogue.json'] + b'\0' + files['index.html']) != manifest['content_id']:
        raise LibraryError('Snapshot content identity mismatch')
    catalogue = read_json(folder/'catalogue.json')
    validate_catalogue(root, catalogue)
    if render(catalogue).encode('utf-8') != files['index.html']:
        raise LibraryError('Snapshot browser differs from catalogue')
    return catalogue


def load_current(root: Path, require_fresh: bool = True):
    root = root.resolve()
    pointer = _pointer(root)
    folder = safe_path(root, f'{BASE}/builds/{pointer["build_id"]}')
    catalogue = _verify(root, folder, pointer)
    if require_fresh:
        _fresh(root, catalogue)
        expected = collect(root, tuple(catalogue['scope']['terms']))
        if json_bytes(expected) != json_bytes(catalogue):
            raise LibraryError('Snapshot metadata differs from current source extraction')
        _fresh(root, catalogue)
    if _pointer(root) != pointer:
        raise LibraryError('Current snapshot changed during read; retry')
    return folder, catalogue


@contextmanager
def _writer(root: Path):
    base = safe_path(root, BASE)
    path = safe_path(root, f'{BASE}/.writer.lock', must_exist=False)
    fd = os.open(path, os.O_CREAT | os.O_RDWR | os.O_NOFOLLOW, 0o600)
    try:
        try:
            fcntl.flock(fd, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError as exc:
            raise LibraryError('Another library writer is active; retry after it finishes') from exc
        yield base
    finally:
        os.close(fd)


def _write(path: Path, data: bytes):
    with path.open('xb') as stream:
        stream.write(data)
        stream.flush()
        os.fsync(stream.fileno())


def _sync_dir(path: Path):
    fd = os.open(path, os.O_RDONLY | os.O_DIRECTORY)
    try:
        os.fsync(fd)
    finally:
        os.close(fd)


def _replace_pointer(base: Path, data: bytes):
    temporary = base / ('.CURRENT-' + uuid.uuid4().hex + '.tmp')
    try:
        _write(temporary, data)
        os.replace(temporary, base/'CURRENT.json')
        _sync_dir(base)
    finally:
        temporary.unlink(missing_ok=True)


def build(root: Path, terms=TERMS, recover: bool=False):
    root = root.resolve()
    with _writer(root) as base:
        current = safe_path(root, f'{BASE}/CURRENT.json', must_exist=False)
        previous = current.read_bytes() if current.exists() else None
        damaged = None
        if previous is not None:
            try:
                _old_folder, old_catalogue = load_current(root, require_fresh=False)
                try:
                    _fresh(root, old_catalogue)
                except (LibraryError, OSError):
                    # An ordinary source update may replace an older snapshot.
                    # Invalid current inputs still fail in collect() below.
                    pass
                else:
                    if json_bytes(collect(root, tuple(old_catalogue['scope']['terms']))) != json_bytes(old_catalogue):
                        raise LibraryError('Current snapshot metadata differs from its unchanged inputs')
            except (LibraryError, OSError) as exc:
                damaged = exc
                if not recover:
                    raise LibraryError(f'Current snapshot is damaged; use build --recover after review: {exc}') from exc
        catalogue = collect(root, terms)
        body = json_bytes(catalogue)
        html = render(catalogue).encode('utf-8')
        content_id = digest(body + b'\0' + html)
        builds = safe_path(root, f'{BASE}/builds', must_exist=False)
        builds.mkdir(exist_ok=True)
        build_id = content_id
        folder = safe_path(root, f'{BASE}/builds/{build_id}', must_exist=False)
        pointer = None
        if folder.exists():
            try:
                manifest_path = safe_path(root, (folder/'manifest.json').relative_to(root).as_posix())
                candidate = {'schema_version': 2, 'build_id': build_id, 'manifest_sha256': digest(manifest_path.read_bytes())}
                existing = _verify(root, folder, candidate)
                if json_bytes(existing) != body:
                    raise LibraryError('Existing snapshot has different metadata')
                pointer = candidate
            except (LibraryError, OSError) as exc:
                if not recover:
                    raise LibraryError(f'Existing retained snapshot is damaged; use --recover: {exc}') from exc
                build_id = digest((content_id + uuid.uuid4().hex).encode())
                folder = safe_path(root, f'{BASE}/builds/{build_id}', must_exist=False)
        if pointer is None:
            stage = base / ('.stage-' + uuid.uuid4().hex)
            stage.mkdir()
            try:
                _write(stage/'catalogue.json', body)
                _write(stage/'index.html', html)
                manifest = {'schema_version': 2, 'build_id': build_id, 'content_id': content_id,
                            'files': {'catalogue.json': digest(body), 'index.html': digest(html)}}
                _write(stage/'manifest.json', json_bytes(manifest))
                _sync_dir(stage)
                _fresh(root, catalogue)
                os.rename(stage, folder)
                _sync_dir(builds)
                pointer = {'schema_version': 2, 'build_id': build_id, 'manifest_sha256': digest(json_bytes(manifest))}
                _verify(root, folder, pointer)
            finally:
                if stage.exists():
                    shutil.rmtree(stage)
        _fresh(root, catalogue)
        # Re-extract to bind metadata to reviewed inputs, not only matching hashes.
        if json_bytes(collect(root, terms)) != body:
            raise LibraryError('Inputs changed during extraction; previous snapshot retained')
        next_bytes = json_bytes(pointer)
        if previous == next_bytes:
            return folder, catalogue, False
        if damaged is not None and previous is not None:
            backups = safe_path(root, f'{BASE}/recovery/pointers', must_exist=False)
            backups.mkdir(parents=True, exist_ok=True)
            _write(backups/(uuid.uuid4().hex + '.json'), previous)
            _sync_dir(backups)
        try:
            _replace_pointer(base, next_bytes)
            _fresh(root, catalogue)
            if json_bytes(collect(root, terms)) != body:
                raise LibraryError('Inputs changed during publication')
        except Exception:
            if previous is None:
                current.unlink(missing_ok=True)
            else:
                _replace_pointer(base, previous)
            raise
        return folder, catalogue, True


def search(catalogue, query: str, term=None, chunk=None, kind=None):
    if not isinstance(query, str) or len(query) > 4096:
        raise LibraryError('Search must be text of at most 4096 characters')
    if term is not None and term not in catalogue['scope']['terms']:
        raise LibraryError('Term is not in this catalogue')
    if chunk is not None and (type(chunk) is not int or chunk < 1):
        raise LibraryError('Chunk must be a positive integer')
    if kind is not None and kind not in ('court_event', 'admitted_source'):
        raise LibraryError('Unknown Record kind')
    needle = query.casefold().strip()
    return [r for r in catalogue['records'] if (term is None or r['term'] == term)
            and (chunk is None or chunk in r['chunks']) and (kind is None or r['kind'] == kind)
            and needle in json.dumps(r, ensure_ascii=False, sort_keys=True).casefold()]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=Path(__file__).resolve().parents[3])
    subs = parser.add_subparsers(dest='command', required=True)
    build_parser = subs.add_parser('build')
    build_parser.add_argument('--recover', action='store_true')
    subs.add_parser('check')
    subs.add_parser('status')
    lookup = subs.add_parser('search')
    lookup.add_argument('query', nargs='?', default='')
    lookup.add_argument('--term', choices=TERMS)
    lookup.add_argument('--chunk', type=int)
    lookup.add_argument('--kind', choices=('court_event', 'admitted_source'))
    lookup.add_argument('--json', action='store_true')
    citation_lookup = subs.add_parser('citations')
    citation_lookup.add_argument('query', nargs='?', default='')
    args = parser.parse_args()
    try:
        if args.command == 'build':
            folder, catalogue, changed = build(args.root, recover=args.recover)
            print(('Published ' if changed else 'Reused ') + str(folder))
        else:
            folder, catalogue = load_current(args.root)
        if args.command == 'citations':
            if len(args.query) > 4096:
                raise LibraryError('Citation query is too long')
            query = ' '.join(args.query.split()).casefold()
            matches = {citation: locations for citation, locations in catalogue.get('citation_index', {}).items()
                       if query in citation.casefold()}
            print(json.dumps(matches, ensure_ascii=False, indent=2))
        elif args.command == 'search':
            matches = search(catalogue, args.query, args.term, args.chunk, args.kind)
            if args.json:
                print(json.dumps(matches, ensure_ascii=False, indent=2))
            else:
                for record in matches:
                    print(f'{record["term"]} | {record["title"]} | {record["path"]}')
                print(f'{len(matches)} Record(s)')
        else:
            print(json.dumps({'production_integration': False, 'snapshot': folder.name,
                              'terms': catalogue['terms'], 'carryovers': len(catalogue['carryovers']),
                              'warnings': {'inventory': len(catalogue['warnings']),
                                           'record_notes': sum(len(r['warnings']) for r in catalogue['records'])},
                              'distinct_citation_strings': len(catalogue.get('citation_index', {}))}, ensure_ascii=False, indent=2))
    except (LibraryError, OSError, ValueError) as exc:
        parser.exit(2, f'Library check failed: {exc}\n')


if __name__ == '__main__':
    main()
