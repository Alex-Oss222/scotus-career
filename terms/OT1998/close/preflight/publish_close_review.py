"""Publish an explicit OT1998 close-review manifest through GitHub's API."""
import argparse
import base64
import hashlib
import json
import os
from pathlib import Path, PurePosixPath
import urllib.request


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--manifest', required=True)
    ap.add_argument('--base', required=True)
    ap.add_argument('--verify-commit')
    args = ap.parse_args()
    root = Path(__file__).resolve().parents[4]
    api = 'https://api.github.com/repos/Alex-Oss222/scotus-career'
    headers = {'Authorization': 'Bearer ' + os.environ['GH_TOKEN'],
               'Accept': 'application/vnd.github+json',
               'User-Agent': 'Codex-OT1998-close-review',
               'X-GitHub-Api-Version': '2022-11-28'}

    def call(method, path, data=None):
        body = None if data is None else json.dumps(data).encode()
        request = urllib.request.Request(api + path, data=body, headers=headers, method=method)
        with urllib.request.urlopen(request, timeout=60) as response:
            return json.load(response)

    def safe_path(name):
        p = PurePosixPath(name)
        assert not p.is_absolute() and '..' not in p.parts
        assert name.startswith('terms/OT1998/close/')
        assert all(x.casefold() not in ('stone', '.git') and
                   not x.upper().startswith('MASTER_JURISPRUDENCE') for x in p.parts)
        target = root
        for part in p.parts:
            target /= part
            assert not target.is_symlink()
        return target

    manifest_bytes = safe_path(args.manifest).read_bytes()
    manifest = json.loads(manifest_bytes)
    assert manifest['base_commit'] == args.base
    files = {}
    for row in manifest['files']:
        name = row['path']
        assert name not in files
        data = safe_path(name).read_bytes()
        assert len(data) == row['bytes']
        assert hashlib.sha256(data).hexdigest() == row['sha256']
        files[name] = data
    files[args.manifest] = manifest_bytes
    expected = {name: hashlib.sha1(b'blob ' + str(len(data)).encode() + b'\0' + data).hexdigest()
                for name, data in files.items()}
    commit_sha = args.verify_commit
    if not commit_sha:
        assert call('GET', '/git/ref/heads/main')['object']['sha'] == args.base, 'Main changed; stop.'
        parent = call('GET', '/git/commits/' + args.base)
        tree = []
        prepared = set()
        inline_bytes = 0
        for name, data in files.items():
            sha = expected[name]
            if sha in prepared:
                tree.append({'path': name, 'mode': '100644', 'type': 'blob', 'sha': sha})
            elif len(data) > 131072 or inline_bytes + len(data) > 3 * 1024 * 1024:
                blob = call('POST', '/git/blobs', {'content': base64.b64encode(data).decode(),
                                                 'encoding': 'base64'})
                assert blob['sha'] == sha
                prepared.add(sha)
                tree.append({'path': name, 'mode': '100644', 'type': 'blob', 'sha': blob['sha']})
            else:
                tree.append({'path': name, 'mode': '100644', 'type': 'blob', 'content': data.decode()})
                inline_bytes += len(data)
        result = call('POST', '/git/trees', {'base_tree': parent['tree']['sha'], 'tree': tree})
        commit = call('POST', '/git/commits', {'message': 'Stage OT1998 close candidates and first audit findings',
                                            'tree': result['sha'], 'parents': [args.base]})
        commit_sha = commit['sha']
        print(json.dumps({'created_commit': commit_sha}), flush=True)
        assert call('GET', '/git/ref/heads/main')['object']['sha'] == args.base, 'Main changed; stop.'
        result = call('PATCH', '/git/refs/heads/main', {'sha': commit_sha, 'force': False})
        assert result['object']['sha'] == commit_sha
        print(json.dumps({'published_commit': commit_sha}), flush=True)

    changed = {}
    page = 1
    while True:
        response = call('GET', f'/commits/{commit_sha}?per_page=100&page={page}')
        assert response['parents'][0]['sha'] == args.base
        rows = response['files']
        for row in rows:
            name = row['filename']
            assert name in expected, 'Unexpected path: ' + name
            assert row['status'] in ('added', 'modified')
            assert row['sha'] == expected[name], name
            changed[name] = row['sha']
        if len(rows) < 100:
            break
        page += 1
    assert set(changed) == set(files), 'Publication manifest mismatch'
    assert call('GET', '/git/ref/heads/main')['object']['sha'] == commit_sha
    print(json.dumps({'verified': True, 'commit': commit_sha, 'files': len(files),
                      'scope': 'Close candidates, first audit and preparation evidence only; state unchanged'}))


if __name__ == '__main__':
    main()
