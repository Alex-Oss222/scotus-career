#!/usr/bin/env python3
"""Publish an immutable Chunk 11 manifest using explicit GitHub API paths.

No Git executable, directory traversal, or adjudicative edits. The caller must
provide the released manifest/output identities and expected main revision.
Use --verify-commit to resume verification after a completed ref update.
"""
import argparse
import base64
import concurrent.futures
import hashlib
import json
import os
from pathlib import Path, PurePosixPath
import re
import time
import urllib.error
import urllib.parse
import urllib.request


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ('manifest', 'manifest-sha256', 'output', 'output-sha256', 'base'):
        parser.add_argument('--' + name, required=True)
    parser.add_argument('--manifest-bytes', required=True, type=int)
    parser.add_argument('--output-bytes', required=True, type=int)
    parser.add_argument('--prepared-blob', action='append', default=[])
    parser.add_argument('--verify-commit')
    args = parser.parse_args()
    root = Path(__file__).absolute().parents[3]
    api = 'https://api.github.com/repos/Alex-Oss222/scotus-career'
    headers = {
        'Authorization': 'Bearer ' + os.environ['GH_TOKEN'],
        'Accept': 'application/vnd.github+json',
        'User-Agent': 'Codex-OT1998-chunk11-publication',
        'X-GitHub-Api-Version': '2022-11-28',
    }
    assert re.fullmatch(r'[0-9a-f]{40}', args.base)
    for sha in args.prepared_blob:
        assert re.fullmatch(r'[0-9a-f]{40}', sha)
    if args.verify_commit:
        assert re.fullmatch(r'[0-9a-f]{40}', args.verify_commit)

    def call(method, path, data=None):
        body = None if data is None else json.dumps(data, ensure_ascii=False).encode()
        for attempt in range(3):
            try:
                req = urllib.request.Request(api + path, data=body,
                                             headers=headers, method=method)
                with urllib.request.urlopen(req, timeout=60) as response:
                    return json.load(response)
            except urllib.error.HTTPError as error:
                if method == 'GET' and error.code in (429, 500, 502, 503, 504) and attempt < 2:
                    time.sleep(2 ** attempt)
                    continue
                raise RuntimeError(f'{method} {path}: HTTP {error.code}') from None
            except (TimeoutError, urllib.error.URLError):
                if method == 'GET' and attempt < 2:
                    time.sleep(2 ** attempt)
                    continue
                raise

    def safe_file(name):
        rel = PurePosixPath(name)
        assert not rel.is_absolute() and '..' not in rel.parts and str(rel) == name, name
        assert name.startswith('terms/OT1998/'), name
        assert not any(part.casefold() in ('stone', '.git') or
                       part.upper().startswith('MASTER_JURISPRUDENCE')
                       for part in rel.parts), name
        target = root
        for part in rel.parts:
            target = target / part
            assert not target.is_symlink(), name
        assert target.is_file(), name
        return target

    def blob_sha(raw):
        return hashlib.sha1(b'blob ' + str(len(raw)).encode() + b'\0' + raw).hexdigest()

    manifest_raw = safe_file(args.manifest).read_bytes()
    assert len(manifest_raw) == args.manifest_bytes
    assert hashlib.sha256(manifest_raw).hexdigest() == args.manifest_sha256
    manifest = json.loads(manifest_raw)
    entries = manifest['files']
    assert len(entries) == manifest['file_count']
    assert sum(item['bytes'] for item in entries) == manifest['total_bytes']
    assert not manifest.get('missing_linked_term_targets')
    files = {}
    for item in entries:
        name = item['path']
        assert name not in files, name
        raw = safe_file(name).read_bytes()
        assert len(raw) == item['bytes'], name
        assert hashlib.sha256(raw).hexdigest() == item['sha256'], name
        files[name] = raw
    assert args.manifest not in files
    files[args.manifest] = manifest_raw
    output = files[args.output]
    assert len(output) == args.output_bytes
    assert hashlib.sha256(output).hexdigest() == args.output_sha256
    expected = {name: blob_sha(raw) for name, raw in files.items()}

    commit_sha = args.verify_commit
    if not commit_sha:
        assert call('GET', '/git/ref/heads/main')['object']['sha'] == args.base, \
            'main changed; no branch mutation performed'
        parent = call('GET', '/git/commits/' + args.base)
        prepared = set(args.prepared_blob)
        tree = []
        inline_bytes = 0
        inline_limit = 3 * 1024 * 1024
        for name, raw in files.items():
            sha = expected[name]
            entry = {'path': name, 'mode': '100644', 'type': 'blob'}
            try:
                decoded = None if b'\0' in raw else raw.decode('utf-8')
            except UnicodeDecodeError:
                decoded = None
            inline_size = 0 if decoded is None else len(json.dumps(decoded, ensure_ascii=False).encode())
            if sha in prepared:
                entry['sha'] = sha
            elif decoded is None or len(raw) >= 131072 or inline_bytes + inline_size > inline_limit:
                response = call('POST', '/git/blobs', {
                    'content': base64.b64encode(raw).decode(), 'encoding': 'base64'})
                assert response['sha'] == sha, name
                prepared.add(sha)
                entry['sha'] = sha
                print(json.dumps({'staged_blob': name, 'bytes': len(raw)}), flush=True)
            else:
                entry['content'] = decoded
                inline_bytes += inline_size
            tree.append(entry)
        new_tree = call('POST', '/git/trees', {'base_tree': parent['tree']['sha'], 'tree': tree})
        assert not new_tree.get('truncated')
        commit = call('POST', '/git/commits', {
            'message': 'Complete OT1998 chunk 11 adjudication and render',
            'tree': new_tree['sha'], 'parents': [args.base]})
        commit_sha = commit['sha']
        print(json.dumps({'created_commit': commit_sha, 'intended_files': len(files)}), flush=True)
        assert call('GET', '/git/ref/heads/main')['object']['sha'] == args.base, \
            'main changed before publication; new commit left unattached'
        published = call('PATCH', '/git/refs/heads/main', {'sha': commit_sha, 'force': False})
        assert published['object']['sha'] == commit_sha
        print(json.dumps({'published_commit': commit_sha}), flush=True)

    assert call('GET', '/git/commits/' + commit_sha)['parents'][0]['sha'] == args.base
    changed = {}
    page = 1
    while True:
        response = call('GET', f'/commits/{commit_sha}?per_page=100&page={page}')
        rows = response.get('files', [])
        for item in rows:
            name = item['filename']
            assert name in files, 'unexpected changed path: ' + name
            assert item['status'] in ('added', 'modified'), item['status']
            assert item['sha'] == expected[name], name
            changed[name] = item['sha']
        if len(rows) < 100:
            break
        page += 1

    def verify_explicit(name):
        response = call('GET', '/contents/' + urllib.parse.quote(name, safe='/') + '?ref=' + commit_sha)
        assert response['type'] == 'file' and response['sha'] == expected[name], name
        return name

    remaining = [name for name in files if name not in changed]
    with concurrent.futures.ThreadPoolExecutor(max_workers=6) as pool:
        checked = list(pool.map(verify_explicit, remaining))
    response = call('GET', '/contents/' + urllib.parse.quote(args.output, safe='/') + '?ref=main')
    assert response['encoding'] == 'base64'
    assert base64.b64decode(response['content']) == output, 'published render bytes mismatch'
    assert call('GET', '/git/ref/heads/main')['object']['sha'] == commit_sha
    print(json.dumps({
        'verified': True, 'commit': commit_sha, 'changed_files': len(changed),
        'unchanged_verified': len(checked), 'intended_files': len(files),
        'output_bytes': len(output), 'output_sha256': hashlib.sha256(output).hexdigest(),
        'url': 'https://github.com/Alex-Oss222/scotus-career/blob/main/' + args.output,
    }), flush=True)


if __name__ == '__main__':
    main()
