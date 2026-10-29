#!/usr/bin/env python3
"""Run canonical manifest builder while preserving unrelated completed/open classifications."""
from pathlib import Path
import sys
import types
sys.dont_write_bytecode = True
ROOT = Path(__file__).absolute().parents[3]
path = ROOT / 'tools' / 'rebuild_manifest.py'
tool = types.ModuleType('chunk11_manifest_tool')
tool.__file__ = str(path)
exec(compile(path.read_text(), str(path), 'exec'), tool.__dict__)
original = tool.status
def current_chunk_status(row, done, stopped, carried, previous=''):
    # The generic tool cannot distinguish a completed component from an open
    # original-leave matter, or a reconciliation-only row from an unrun case.
    # This Run authorizes changes only to Chunk11 inventory statuses.
    if row[1] != 'OT_1998CHUNK11' and previous:
        return previous
    return original(row, done, stopped, carried, previous)
tool.status = current_chunk_status
sys.argv = [str(path), 'OT1998', '--root', str(ROOT), *sys.argv[1:]]
tool.main()
print('Unrelated inventory rows retain their exact existing status, including Germany original leave and Del Monte Dunes reconciliation.')
