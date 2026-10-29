#!/usr/bin/env python3
"""OT1998 Chunk11 check/ledger adapters. No subprocesses or Git metadata access.

Run with python -B. The check command executes unchanged governing checks,
except that commit-reference existence is explicitly deferred. Python check
helpers run in-process. The ledger command preserves existing local order and
first-record identifiers; it cannot reconstruct Git commitment order.
"""
from __future__ import annotations
import argparse
import contextlib
import io
import os
from pathlib import Path
import re
import runpy
import subprocess
import sys
import types

sys.dont_write_bytecode = True
os.environ['PYTHONDONTWRITEBYTECODE'] = '1'
ROOT = Path(__file__).absolute().parents[3]
TERM = ROOT / 'terms' / 'OT1998'


def normalized(path):
    return os.path.normcase(os.path.abspath(os.fsdecode(path)))


def install_guards(command):
    forbidden = [normalized(ROOT / name) for name in ('stone', '.git')]
    permitted_write = normalized(TERM / 'workspace' / 'ledger.md') if command == 'ledger' else None

    def audit(event, args):
        if event in {'subprocess.Popen', 'os.system', 'os.posix_spawn'} or event.startswith(('os.exec', 'os.spawn')):
            raise PermissionError('All subprocess and shell execution is prohibited by this adapter')
        if event in {'open', 'os.listdir', 'os.scandir'} and args and isinstance(args[0], (str, bytes, os.PathLike)):
            target = normalized(args[0])
            components = Path(target).parts
            if ('stone' in components or any(part.startswith('MASTER_JURISPRUDENCE') for part in components)
                    or any(target == item or target.startswith(item + os.sep) for item in forbidden)):
                raise PermissionError('Prohibited source or directory access blocked')
        if event == 'open':
            path, mode, flags = args
            writing = (isinstance(mode, str) and any(char in mode for char in 'wax+')) or (
                isinstance(flags, int) and flags & (os.O_WRONLY | os.O_RDWR | os.O_CREAT | os.O_TRUNC | os.O_APPEND))
            if writing and (not isinstance(path, (str, bytes, os.PathLike)) or normalized(path) != permitted_write):
                raise PermissionError('Write outside the permitted ledger target blocked')
        if event in {'os.remove', 'os.unlink', 'os.rmdir', 'os.mkdir', 'os.rename', 'os.replace',
                     'os.link', 'os.symlink', 'os.truncate', 'os.chmod'}:
            raise PermissionError('Filesystem mutation outside the permitted ledger write blocked')

    sys.addaudithook(audit)


def load_tool(name):
    path = ROOT / 'tools' / name
    module = types.ModuleType('ot1998_chunk11_' + path.stem)
    module.__file__ = str(path)
    exec(compile(path.read_text(encoding='utf-8'), str(path), 'exec'), module.__dict__)
    return module


def helper_in_process(command, **kwargs):
    if not isinstance(command, (list, tuple)) or len(command) < 2 or kwargs.get('shell'):
        raise PermissionError('Unexpected subprocess request blocked')
    command = [str(item) for item in command]
    if normalized(command[0]) != normalized(sys.executable):
        raise PermissionError('Unexpected executable request blocked')
    script, args = Path(command[1]).absolute(), command[2:]
    if script == ROOT / 'tools' / 'holdings_volumes.py':
        allowed = args == ['check', '--root', str(ROOT)]
    elif script == ROOT / 'tools' / 'split_chunk.py':
        allowed = (len(args) == 2 and args[1] in ('--check', '--parse-only')
                   and Path(args[0]).absolute().parent == TERM / 'briefs')
    else:
        allowed = False
    if not allowed:
        raise PermissionError('Unexpected helper request blocked')
    stdout, stderr = io.StringIO(), io.StringIO()
    old_argv = sys.argv
    code = 0
    try:
        sys.argv = [str(script), *args]
        with contextlib.redirect_stdout(stdout), contextlib.redirect_stderr(stderr):
            try:
                runpy.run_path(str(script), run_name='__main__')
            except SystemExit as exc:
                if isinstance(exc.code, int):
                    code = exc.code
                elif exc.code is not None:
                    print(exc.code, file=sys.stderr)
                    code = 1
    finally:
        sys.argv = old_argv
    return subprocess.CompletedProcess(command, code, stdout.getvalue(), stderr.getvalue())


def check():
    tool = load_tool('check_term.py')
    original_refs = tool.commit_refs
    encountered = set()
    source_filename_fragments = set()

    def deferred_refs(text):
        # The governing matcher also recognizes reporter citation fragments in
        # these exact validated lower-opinion filenames. Remove only those
        # literal filenames from the commit-reference extraction copy. All
        # substantive text and every other governing check remain unchanged;
        # any occurrence of the token outside that exact filename is retained.
        reference_text = text
        for name in ('lower_90f3d963.txt', 'lower_134f3d668_sanitized.txt'):
            reference_text = reference_text.replace(name, '')
        actual_refs = original_refs(reference_text)
        source_filename_fragments.update(original_refs(text) - actual_refs)
        encountered.update(actual_refs)
        return set()

    tool.commit_refs = deferred_refs
    tool.git_object_exists = lambda *_: (_ for _ in ()).throw(PermissionError('Git verification remains deferred'))
    subprocess.run = helper_in_process
    sys.argv = [str(ROOT / 'tools' / 'check_term.py'), 'OT1998', '--root', str(ROOT)]
    try:
        tool.main()
    finally:
        print('DEFERRED: Git commit-reference existence checks; ' + str(len(encountered)) + ' distinct token(s): ' + ', '.join(sorted(encountered)))
        if source_filename_fragments:
            print('CLASSIFIED NON-COMMIT SOURCE-FILENAME FRAGMENTS: ' + ', '.join(sorted(source_filename_fragments)))
        print('All non-Git check_term checks were enabled. Check helpers ran in-process; no subprocess, Git metadata access, or filesystem write was permitted.')


def ledger():
    tool = load_tool('rebuild_ledger.py')
    target = TERM / 'workspace' / 'ledger.md'
    records = {path.name: tool.parse(path) for path in sorted((TERM / 'records').glob('*.md'))
               if not path.name.startswith('.')}
    old_order, old_ids = [], {}
    for line in target.read_text(encoding='utf-8').splitlines():
        if not re.match(r'^\|\s*\d+\s*\|', line):
            continue
        cells = [item.strip() for item in line.strip().strip('|').split('|')]
        if len(cells) != 8:
            raise SystemExit('Unexpected existing ledger column count')
        match = re.fullmatch(r'\[record\]\(\.\./records/([^/)]+)\)', cells[-1])
        if not match or match[1] in old_ids or match[1] not in records:
            raise SystemExit('Invalid, duplicated, or missing existing ledger Record: ' + line)
        old_order.append(match[1])
        old_ids[match[1]] = cells[6]
    added = sorted(set(records) - set(old_order), key=lambda name: (records[name]['date'], records[name]['case'].casefold(), name))
    names = old_order + added
    lines = ['# OT1998 Term Working Ledger', '',
             'Generated from canonical Records without Git access. Existing ledger order and first-record commit cells are preserved; newly added Records follow in effective-date and case-name order. New entries have no verified commitment status, and prior commit identifiers have not been revalidated. Records control if this index conflicts with them.', '',
             '| Local entry order | Effective date | Case and dockets | Event | Result | Version / lineage | First-record commit | Record |',
             '|---:|---|---|---|---|---|---|---|']
    for number, name in enumerate(names, 1):
        data = records[name]
        first = old_ids.get(name, 'Deferred; Git prohibited by user')
        lines.append(f"| {number} | {data['date']} | {data['case']} | {data['event']} | {data['result']} | {data['version']} | {first} | [record](../records/{name}) |")
    target.write_text('\n'.join(lines) + '\n', encoding='utf-8')
    print(f'{target}: {len(names)} Records; {len(added)} appended; no Git invoked. Git commitment order and provenance remain unverified.')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('command', choices=('check', 'ledger'))
    args = parser.parse_args()
    install_guards(args.command)
    check() if args.command == 'check' else ledger()


if __name__ == '__main__':
    main()
