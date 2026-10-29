#!/usr/bin/env python3
"""First close preflight: unchanged canonical checks with guarded API-receipt adapter.

No Git, subprocess, forbidden source, or write outside this preflight directory.
The immutable six-reference API receipt replaces only git_object_exists. The
two exact reporter filenames retain the established non-commit classification.
"""
import contextlib
import hashlib
import io
import json
import os
from pathlib import Path
import re
import runpy
import subprocess
import sys

sys.dont_write_bytecode = True
os.environ['PYTHONDONTWRITEBYTECODE'] = '1'
ROOT = Path(__file__).absolute().parents[4]
TERM = ROOT / 'terms/OT1998'
OUT = TERM / 'close/preflight'

def forbidden(path):
    return any(p.casefold() in ('stone', '.git') or p.upper().startswith('MASTER_JURISPRUDENCE')
               for p in Path(os.path.abspath(os.fsdecode(path))).parts)

def guard(event, args):
    if event in {'subprocess.Popen', 'os.system', 'os.posix_spawn'} or event.startswith(('os.exec', 'os.spawn')):
        raise PermissionError('No subprocess or shell execution is authorized')
    if event in {'open', 'os.listdir', 'os.scandir'} and args and isinstance(args[0], (str, bytes, os.PathLike)):
        if forbidden(args[0]):
            raise PermissionError('Forbidden source access blocked')
    if event == 'open':
        path, mode, flags = args
        writing = (isinstance(mode, str) and any(c in mode for c in 'wax+')) or (
            isinstance(flags, int) and flags & (os.O_WRONLY | os.O_RDWR | os.O_CREAT | os.O_TRUNC | os.O_APPEND))
        if writing and (not isinstance(path, (str, bytes, os.PathLike)) or
                        not Path(os.path.abspath(os.fsdecode(path))).is_relative_to(OUT)):
            raise PermissionError('Write outside preflight blocked')
    if event in {'os.remove', 'os.unlink', 'os.rmdir', 'os.mkdir', 'os.rename', 'os.replace', 'os.link', 'os.symlink', 'os.truncate', 'os.chmod'}:
        raise PermissionError('Filesystem mutation blocked')

sys.addaudithook(guard)

def safe_rglob(self, pattern):
    if self != TERM or pattern != '*.md':
        raise PermissionError('Unexpected recursive traversal')
    for dirname, dirs, files in os.walk(self, topdown=True, followlinks=False):
        dirs[:] = [n for n in dirs if not forbidden(Path(dirname) / n)
                   and not (Path(dirname) / n).is_symlink()]
        for name in files:
            path = Path(dirname) / name
            if name.endswith('.md') and not forbidden(path) and not path.is_symlink():
                yield path

Path.rglob = safe_rglob
adapter_path = TERM / 'audit/ot1998_chunk11_no_git.py'
adapter = runpy.run_path(str(adapter_path), run_name='preflight_adapter_library')
tool = adapter['load_tool']('check_term.py')
subprocess.run = adapter['helper_in_process']
receipt_path = TERM / 'freeze/OT_1998CHUNK10_COMMIT_REFERENCE_API_RECEIPT.json'
raw = receipt_path.read_bytes()
assert hashlib.sha256(raw).hexdigest() == 'd35f4ddb8ddaa8c16bca5402e1219b7bbc53c872acdd7196075695c0423ae961'
receipt = json.loads(raw)
assert receipt['repository'] == 'Alex-Oss222/scotus-career' and receipt['all_resolved']
verified = {}
for item in receipt['checks']:
    assert item['exists'] and item['http_status'] == 200
    assert re.fullmatch('[0-9a-f]{40}', item['resolved_sha']) and item['resolved_sha'].startswith(item['reference'])
    verified[item['reference']] = item['resolved_sha']

original_refs = tool.commit_refs
encountered, classified = set(), set()
def refs(text):
    stripped = text
    for filename in ('lower_90f3d963.txt', 'lower_134f3d668_sanitized.txt'):
        stripped = stripped.replace(filename, '')
    actual = original_refs(stripped)
    classified.update(original_refs(text) - actual)
    encountered.update(actual)
    return actual

tool.commit_refs = refs
tool.git_object_exists = lambda root, sha: sha in verified
stdout, stderr = io.StringIO(), io.StringIO()
sys.argv = [str(ROOT / 'tools/check_term.py'), 'OT1998', '--root', str(ROOT)]
code = 0
with contextlib.redirect_stdout(stdout), contextlib.redirect_stderr(stderr):
    try:
        tool.main()
    except SystemExit as exc:
        code = exc.code if isinstance(exc.code, int) else 1
result = {
    'canonical_check_invocations': 1,
    'command': 'python -B terms/OT1998/close/preflight/check_once.py',
    'exit_code': code,
    'stdout': stdout.getvalue(), 'stderr': stderr.getvalue(),
    'holdings_check': 'Included by canonical check_term.py; no duplicate invocation',
    'actual_commit_references': {ref: verified.get(ref) for ref in sorted(encountered)},
    'unverified_commit_references': sorted(encountered - verified.keys()),
    'source_filename_fragments_not_commits': sorted(classified),
    'api_receipt': str(receipt_path.relative_to(ROOT)),
    'api_receipt_sha256': hashlib.sha256(raw).hexdigest(),
    'commit_verification': 'Reuse exact prior SHA-only HTTP 200 API receipt; no duplicate network calls',
    'guard': 'No subprocess, Git metadata, forbidden source access, or writes outside close/preflight',
}
(OUT / 'canonical_check.json').write_text(json.dumps(result, indent=2) + '\n')
print(json.dumps(result, indent=2))
