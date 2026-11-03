from pathlib import Path
import hashlib
import re
import sys
sys.dont_write_bytecode=True
T=Path(__file__).resolve().parents[1]
F=T/'freeze'
P='OT_1999CHUNK8_'

def read(name):
    return (F/(P+name+'.md')).read_text(encoding='utf-8')

def selected(name, prefixes):
    s=read(name)
    matches=list(re.finditer(r'^## (.+)$',s,re.M))
    parts=[s[:matches[0].start()].strip()]
    for i,m in enumerate(matches):
        if any(m[1].startswith(p) for p in prefixes):
            end=matches[i+1].start() if i+1<len(matches) else len(s)
            parts.append(s[m.start():end].strip())
    if len(parts)!=len(prefixes)+1:raise ValueError('Missing selected section: '+name)
    return '\n\n'.join(parts)+'\n'

groups={
 'NEUTRAL':[(n,None) for n in ['A_NEUTRAL','A_CARTER_NEUTRAL_CORRECTION','A_CARTER_ANALYTICAL_SUPPLEMENT_NEUTRAL','RAMDASS_NEUTRAL','RAMDASS_LOWER_GROUNDS_NEUTRAL','B_NEUTRAL','ARIZONA_NEUTRAL_SUPPLEMENT','C_NEUTRAL']],
 'COMMITMENTS':[
   ('A_COMMITMENTS',['Bradley','Pegram','Reeves']),('CARTER_COMMITMENTS_REVISED',None),('RAMDASS_COMMITMENTS',None),
   ('B_COMMITMENTS',['Common reading','2. Crosby','3. Hawkins','4. Miller','5. Santa Fe']),('ARIZONA_COMMITMENTS_REVISED',None),('B_JUNE12_LAW_REVIEW',None),('B_HARRIS_LAW_REVIEW',None),('C_COMMITMENTS',None),('C_FINAL_LAW_REVIEW',None)],
 'RECONCILED':[(n,None) for n in ['A_NONCARTER_RECONCILED','CARTER_RECONCILED','RAMDASS_RECONCILED','B_NONARIZONA_RECONCILED','ARIZONA_RECONCILED','B_FINAL_LAW_REVIEW','B_HARRIS_RECONCILIATION_REVIEW','C_RECONCILED','C_FINAL_RECONCILIATION_REVIEW']]
}
for kind,items in groups.items():
    parts=[f'# OT1999 chunk 8 — generated {kind.lower()} handoff index and reading copy','',
      'Assembled mechanically at Run completion from the separately preserved stage freezes below. The original stage files establish the actual sequence and remain authoritative. This aggregate creates no new commitment, changes no earlier freeze and does not claim an earlier creation time. Later completion receipts discharge the stated entering-law review conditions. Superseded Carter and Arizona commitment sections are omitted from the commitments copy. No Git operation or repository commitment is represented.','',
      'The generated raw runtime neutral split remains the unaltered approved-brief export. The frozen neutral copies and their scoped supplements supply the validated modeling packets.']
    for name,prefixes in items:
        p=F/(P+name+'.md')
        raw=p.read_bytes()
        body=selected(name,prefixes) if prefixes else read(name)
        parts+=['',f'## Source: {p.name}','',f'SHA256: {hashlib.sha256(raw).hexdigest()}',
                'Selected complete sections: '+', '.join(prefixes) if prefixes else 'Complete stage file copied.', '',body.strip()]
    out='\n'.join(parts).rstrip()+'\n'
    target=F/(P+kind+'.md')
    if target.exists() and target.read_text(encoding='utf-8')!=out:raise RuntimeError('Refusing frozen aggregate overwrite '+target.name)
    target.write_text(out,encoding='utf-8')
    if kind!='NEUTRAL':(T/'runtime'/(P+kind+'.md')).write_text(out,encoding='utf-8')
    print(target.name)
