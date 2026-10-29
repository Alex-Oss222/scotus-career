"""Publish an explicit OT1998 stage manifest using only GitHub's REST API.

Manifest: {"schema": 1, "base_commit": "<40 hex>", "files": [
  {"path": "terms/OT1998/close/example.md", "bytes": 123,
   "sha256": "<64 hex>"}], "deletions": [
  {"path": "terms/OT1998/close/obsolete.md", "old_blob_sha": "<40 hex>"}]}
Deletion rows may also be explicit path strings; old_blob_sha is optional.
The manifest is local orchestration data unless --include-manifest is passed.
"""
import argparse
import base64
from collections import Counter
import hashlib
import json
import os
from pathlib import Path, PurePosixPath
import re
import stat
import sys
import urllib.error
import urllib.parse
import urllib.request


REPOSITORY = 'Alex-Oss222/scotus-career'
CLOSE = 'terms/OT1998/close/'
EXACT_PATHS = {
    'terms/OT1998/workspace/manifest.md', 'terms/OT1998/INDEX.md',
    'state/HOLDINGS.md', 'state/STANDARDS_AND_TESTS.md', 'state/STANDING_STATE.md',
    'state/holdings/INDEX.md',
}
AREAS = (
    'constitutional-structure', 'federal-courts', 'criminal-procedure',
    'civil-rights', 'first-amendment', 'election-law', 'administrative-law',
    'immigration', 'federal-indian-law', 'labor-and-employment', 'maritime-law',
    'bankruptcy', 'federal-taxation', 'tort-law', 'environmental-law',
    'business-and-commercial-law', 'property-and-economic-rights', 'antitrust',
)
EXACT_PATHS.update('state/holdings/' + area + '.md' for area in AREAS)
INLINE_LIMIT = 128 * 1024
TREE_PAYLOAD_LIMIT = 3 * 1024 * 1024


def require(condition, message):
    if not condition:
        raise ValueError(message)


def digest_ok(value, length):
    return isinstance(value, str) and re.fullmatch('[0-9a-f]{' + str(length) + '}', value) is not None


def blob_sha(data):
    return hashlib.sha1(b'blob ' + str(len(data)).encode('ascii') + b'\0' + data).hexdigest()


def progress(**values):
    print(json.dumps(values, sort_keys=True), flush=True)


class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        return None


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--manifest', required=True)
    parser.add_argument('--base', required=True)
    parser.add_argument('--message', required=True)
    parser.add_argument('--verify-commit')
    parser.add_argument('--include-manifest', action='store_true')
    args = parser.parse_args()
    require(digest_ok(args.base, 40), 'Base must be a lowercase 40-character commit SHA.')
    require(args.verify_commit is None or digest_ok(args.verify_commit, 40),
            'Verification commit must be a lowercase 40-character commit SHA.')
    require(bool(args.message.strip()), 'Commit message must not be empty.')
    root = Path(os.path.abspath(__file__)).parents[4]

    def safe_path(name, deletion=False):
        require(isinstance(name, str) and bool(name), 'A path must be a nonempty string.')
        path = PurePosixPath(name)
        require(not path.is_absolute() and path.as_posix() == name and
                '..' not in path.parts and '\\' not in name and '\x00' not in name,
                'Noncanonical path rejected.')
        require(all(part.casefold() not in ('stone', '.git') and
                    not part.upper().startswith('MASTER_JURISPRUDENCE')
                    for part in path.parts), 'Protected path rejected.')
        require(name.startswith(CLOSE) or (not deletion and name in EXACT_PATHS),
                'Path outside the publication allowlist.')
        require(not deletion or name.startswith(CLOSE), 'Deletion must be within close/.')
        # Check each explicit component without resolving or traversing symlinks.
        target = Path(root.anchor)
        for part in root.parts[1:] + path.parts:
            target /= part
            require(not target.is_symlink(), 'Symlink path rejected.')
        return target

    require(args.manifest.startswith(CLOSE + 'preflight/'),
            'Manifest must be an explicit close/preflight/ path.')
    safe_path(args.manifest)

    def read_regular(name):
        target = safe_path(name)
        require(stat.S_ISREG(target.stat(follow_symlinks=False).st_mode),
                'Source must be a regular file.')
        # O_NOFOLLOW closes the final-component symlink race on supported systems.
        descriptor = os.open(target, os.O_RDONLY | getattr(os, 'O_NOFOLLOW', 0))
        with os.fdopen(descriptor, 'rb') as source:
            require(stat.S_ISREG(os.fstat(source.fileno()).st_mode),
                    'Source must be a regular file.')
            return source.read()

    manifest_bytes = read_regular(args.manifest)
    manifest = json.loads(manifest_bytes)
    require(isinstance(manifest, dict), 'Manifest must be an object.')
    require(manifest.get('base_commit') == args.base, 'Manifest base differs from --base.')
    require('schema' not in manifest or type(manifest['schema']) is int and manifest['schema'] == 1,
            'Unsupported manifest schema.')
    require('repository' not in manifest or manifest['repository'] == REPOSITORY,
            'Manifest repository mismatch.')
    require(isinstance(manifest.get('files'), list), 'Manifest files must be a list.')
    files = {}
    for row in manifest['files']:
        require(isinstance(row, dict), 'Each file row must be an object.')
        name = row.get('path')
        safe_path(name)
        require(name not in files and name != args.manifest, 'Duplicate or self-referencing file row.')
        require(type(row.get('bytes')) is int and row['bytes'] >= 0 and
                digest_ok(row.get('sha256'), 64), 'Invalid source identity.')
        data = read_regular(name)
        require(len(data) == row['bytes'] and hashlib.sha256(data).hexdigest() == row['sha256'],
                'Source identity mismatch: ' + name)
        files[name] = data
    if args.include_manifest:
        files[args.manifest] = manifest_bytes
    deletions = {}
    require(isinstance(manifest.get('deletions', []), list), 'Deletions must be a list.')
    for row in manifest.get('deletions', []):
        require(isinstance(row, (str, dict)), 'Invalid deletion row.')
        name = row if isinstance(row, str) else row.get('path')
        safe_path(name, deletion=True)
        require(name not in files and name not in deletions and name != args.manifest,
                'Duplicate, conflicting, or manifest deletion.')
        old_sha = None if isinstance(row, str) else row.get('old_blob_sha')
        require(old_sha is None or digest_ok(old_sha, 40), 'Invalid old_blob_sha.')
        deletions[name] = old_sha
    require(bool(files or deletions), 'Manifest contains no publication operations.')
    expected = {name: blob_sha(data) for name, data in files.items()}

    def recheck_sources():
        require(read_regular(args.manifest) == manifest_bytes, 'Manifest changed during publication.')
        for name, original in files.items():
            require(read_regular(name) == original, 'Source changed during publication: ' + name)
        for name in deletions:
            safe_path(name, deletion=True)

    token = os.environ.get('GH_TOKEN')
    require(bool(token), 'GH_TOKEN is required.')
    headers = {
        'Authorization': 'Bearer ' + token,
        'Accept': 'application/vnd.github+json',
        'Content-Type': 'application/json',
        'User-Agent': 'Codex-OT1998-close-stage',
        'X-GitHub-Api-Version': '2022-11-28',
    }
    opener = urllib.request.build_opener(NoRedirect())

    def call(method, path, data=None, missing_ok=False):
        body = None if data is None else json.dumps(data, ensure_ascii=True).encode('utf-8')
        request = urllib.request.Request('https://api.github.com/repos/' + REPOSITORY + path,
                                         data=body, headers=headers, method=method)
        try:
            with opener.open(request, timeout=60) as response:
                return json.load(response)
        except urllib.error.HTTPError as error:
            if missing_ok and error.code == 404:
                return None
            raise RuntimeError('GitHub API ' + method + ' failed: HTTP ' + str(error.code)) from None
        except urllib.error.URLError:
            raise RuntimeError('GitHub API connection failed.') from None

    def main_is(commit):
        require(call('GET', '/git/ref/heads/main')['object']['sha'] == commit,
                'Main differs from the expected commit; stop.')

    def contents(name, commit):
        safe_path(name, deletion=name in deletions)
        result = call('GET', '/contents/' + urllib.parse.quote(name, safe='/') +
                      '?ref=' + commit, missing_ok=True)
        if result is not None:
            require(isinstance(result, dict) and result.get('type') == 'file' and
                    result.get('path') == name and 'target' not in result and
                    not result.get('submodule_git_url') and digest_ok(result.get('sha'), 40),
                    'Unexpected remote file identity.')
        return result

    main_is(args.verify_commit or args.base)
    parent = call('GET', '/git/commits/' + args.base)
    require(parent.get('sha') == args.base and digest_ok(parent.get('tree', {}).get('sha'), 40),
            'Base commit identity mismatch.')
    statuses = {}
    deleted_blob_shas = {}
    for name, sha in expected.items():
        prior = contents(name, args.base)
        if prior is None:
            statuses[name] = 'added'
        elif prior['sha'] != sha:
            statuses[name] = 'modified'
    for name, old_sha in deletions.items():
        if old_sha is None:
            prior = contents(name, args.base)
            require(prior is not None, 'Deletion path absent at the manifest base: ' + name)
            old_sha = prior['sha']
        statuses[name] = 'removed'
        # Supplied identities come from already-verified publication manifests.
        # The complete commit diff checks every old blob before main can move.
        deleted_blob_shas[name] = old_sha

    def verify(commit_sha):
        changed = {}
        page = 1
        while True:
            response = call('GET', '/commits/' + commit_sha + '?per_page=100&page=' + str(page))
            require(response.get('sha') == commit_sha and
                    [item['sha'] for item in response.get('parents', [])] == [args.base],
                    'Commit identity or parent mismatch.')
            rows = response.get('files')
            require(isinstance(rows, list), 'Missing commit file diff.')
            for row in rows:
                name = row.get('filename')
                require(name in statuses and name not in changed, 'Unexpected or duplicate changed path.')
                require(row.get('status') == statuses[name] and 'previous_filename' not in row,
                        'Changed file status mismatch: ' + name)
                if name in expected:
                    require(row.get('sha') == expected[name], 'Changed blob SHA mismatch: ' + name)
                else:
                    require(row.get('sha') == deleted_blob_shas[name],
                            'Deleted blob SHA mismatch: ' + name)
                changed[name] = row['status']
            if len(rows) < 100:
                break
            require(page < 30, 'Commit diff pagination limit exceeded; verification incomplete.')
            page += 1
        require(changed == statuses, 'Changed-file set differs from the manifest.')
        # The exact diff proves changed blobs and deletions. Read unchanged
        # targets explicitly; avoid duplicating hundreds of verified operations.
        for name, sha in expected.items():
            if name not in changed:
                result = contents(name, commit_sha)
                require(result is not None and result['sha'] == sha, 'Target blob SHA mismatch: ' + name)

    commit_sha = args.verify_commit
    if commit_sha is None:
        require(bool(statuses), 'All manifest files are unchanged; no commit created.')
        recheck_sources()
        counts = Counter(expected[name] for name in statuses if name in expected)
        prepared = set()
        tree = []
        payload_size = len(json.dumps({'base_tree': parent['tree']['sha'], 'tree': []}).encode())
        for name in sorted(statuses):
            entry = {'path': name, 'mode': '100644', 'type': 'blob'}
            if name in deletions:
                entry['sha'] = None
            else:
                data, sha = files[name], expected[name]
                try:
                    content = data.decode('utf-8')
                except UnicodeDecodeError:
                    content = None
                inline = dict(entry, content=content)
                inline_size = len(json.dumps(inline, ensure_ascii=True).encode()) + 2
                if sha not in prepared and counts[sha] == 1 and content is not None and \
                        len(data) <= INLINE_LIMIT and payload_size + inline_size <= TREE_PAYLOAD_LIMIT:
                    entry = inline
                else:
                    if sha not in prepared:
                        blob = call('POST', '/git/blobs', {
                            'content': base64.b64encode(data).decode('ascii'), 'encoding': 'base64'})
                        require(blob.get('sha') == sha, 'Created blob SHA mismatch.')
                        prepared.add(sha)
                    entry['sha'] = sha
            payload_size += len(json.dumps(entry, ensure_ascii=True).encode()) + 2
            require(payload_size <= TREE_PAYLOAD_LIMIT, 'Explicit tree payload exceeds the bounded limit.')
            tree.append(entry)
        result = call('POST', '/git/trees', {'base_tree': parent['tree']['sha'], 'tree': tree})
        require(digest_ok(result.get('sha'), 40), 'Invalid created tree identity.')
        commit = call('POST', '/git/commits', {'message': args.message, 'tree': result['sha'],
                                             'parents': [args.base]})
        commit_sha = commit.get('sha')
        require(digest_ok(commit_sha, 40) and commit.get('tree', {}).get('sha') == result['sha'] and
                [item['sha'] for item in commit.get('parents', [])] == [args.base],
                'Created commit identity mismatch.')
        progress(created_commit=commit_sha)
        verify(commit_sha)
        recheck_sources()
        main_is(args.base)
        result = call('PATCH', '/git/refs/heads/main', {'sha': commit_sha, 'force': False})
        require(result.get('object', {}).get('sha') == commit_sha, 'Published ref identity mismatch.')
    else:
        verify(commit_sha)
        recheck_sources()
    main_is(commit_sha)
    progress(verified=True, commit=commit_sha, base=args.base, files=len(files),
             changed_files=len(statuses), deleted_files=len(deletions),
             unchanged_files=len(files) - sum(name in expected for name in statuses),
             manifest_sha256=hashlib.sha256(manifest_bytes).hexdigest(),
             manifest_included=args.include_manifest)


if __name__ == '__main__':
    try:
        main()
    except (ValueError, RuntimeError, OSError, KeyError, TypeError) as error:
        # Never emit HTTP bodies, credentials, request headers, or tracebacks.
        if isinstance(error, OSError):
            message = 'Local file access or network I/O failed.'
        elif isinstance(error, (KeyError, TypeError)):
            message = 'Invalid manifest or GitHub API response structure.'
        else:
            message = str(error)
        progress(error=message)
        sys.exit(1)
