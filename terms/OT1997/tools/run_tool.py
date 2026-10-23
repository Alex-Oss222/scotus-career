#!/usr/bin/env python3
"""Run existing repository tools with this term's unnumbered-case compatibility.

Does not edit tools/ or approved briefs. Blocks Git subprocesses and restricts
recursive scans to permitted paths. All ordinary tool behavior is retained.
"""
import pathlib
import re
import subprocess
import sys
import types

ROOT=pathlib.Path(__file__).resolve().parents[3]
SELF=pathlib.Path(__file__).resolve()
real_run=subprocess.run
real_rglob=pathlib.Path.rglob

def forbidden(path):
    return any(p.lower()=='stone' or p.upper().startswith('MASTER_JURISPRUDENCE') for p in pathlib.Path(path).parts)

def guarded_run(args,*pos,**kw):
    if isinstance(args,(str,bytes)) or kw.get('shell'):
        raise RuntimeError('Shell subprocesses are not allowed by this task adapter')
    values=[str(a) for a in args]
    if any(pathlib.Path(a).name.lower() in ('git','git.exe') for a in values[:2]):
        raise RuntimeError('Git commands prohibited by user')
    if len(values)>1 and pathlib.Path(values[1]).resolve()==ROOT/'tools/split_chunk.py':
        args=[sys.executable,'-B',str(SELF),'split_chunk',*values[2:]]
    return real_run(args,*pos,**kw)

def guarded_rglob(self,pattern,*pos,**kw):
    # walk() prunes before descending; never enumerate a protected directory.
    import os
    for directory,dirs,files in os.walk(self,followlinks=False):
        dirs[:]=[d for d in dirs if not forbidden(pathlib.Path(directory)/d) and not (pathlib.Path(directory)/d).is_symlink()]
        for name in files:
            path=pathlib.Path(directory)/name
            if not forbidden(path) and not path.is_symlink() and path.match(pattern):
                yield path

subprocess.run=guarded_run
pathlib.Path.rglob=guarded_rglob
name=sys.argv[1]
assert name in ('split_chunk','check_term','rebuild_ledger','rebuild_manifest','build_render_input')
source=ROOT/'tools'/f'{name}.py'
module=types.ModuleType('scoped_'+name)
module.__file__=str(source)
sys.modules[module.__name__]=module
exec(compile(source.read_text(),str(source),'exec'),module.__dict__)
if name=='split_chunk':
    module.TOP_CASE_RE=re.compile(r'^#\s+((?!SECTION\b|OT_\d{4}CHUNK)\S.*?)\s*$',re.M)
if name=='rebuild_ledger':
    import json
    order_paths=sorted((ROOT/'terms/OT1997/freeze').glob('OT_1997CHUNK*_RECORD_COMMIT_ORDER.json'), key=lambda p:int(re.search(r'CHUNK(\d+)',p.name).group(1)))
    order=[row for p in order_paths for row in json.loads(p.read_text())['records']]
    names=[row['file'] for row in order]
    if len(names)!=len(set(names)):
        raise RuntimeError('Duplicate Record in durable file commitment order')
    def file_commit(root,path):
        if path.name not in names:
            raise RuntimeError('Record absent from durable file commitment order: '+path.name)
        return (names.index(path.name),'durable file; Git prohibited')
    module.git_added=file_commit
sys.argv=[str(source),*sys.argv[2:]]
module.main()
if name=='rebuild_ledger':
    target=ROOT/'terms/OT1997/workspace/ledger.md'
    text=target.read_text().replace('Generated from canonical Records in Git commitment order.', 'Generated from canonical Records in the documented durable file commitment order; Git commands are prohibited for this run.').replace('First-record commit','Durable commitment')
    target.write_text(text)
