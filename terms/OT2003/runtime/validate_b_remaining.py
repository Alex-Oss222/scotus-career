from pathlib import Path
import json,re,hashlib
import finalize_chunk2_b_remaining as f

f.restore()
assert len(f.CREATED)==3
counts,trace=f.recount()
assert len(trace)==23
assert sum(counts.values())==23
rows=[]
for item in f.VALIDATION:
    p=f.BASE/'records'/item['record']; s=p.read_text(encoding='utf-8')
    for line,label in zip(s.splitlines()[:4],['**Case and dockets:**','**Event and date:**','**Result:**','**Version / lineage:**']):assert line.startswith(label)
    pub=s.split('## Public Projection\n\n',1)[1]
    assert re.findall(r'^## (.+)$',pub,re.M)==f.BLOCKS
    for directory in ['runtime','freeze']:
        q=f.BASE/directory/item.get('final_public_basename',f"OT_2003CHUNK2_{item['case']}_PUBLIC.md")
        assert q.read_bytes()==pub.encode('utf-8')
        if 'original_public_sha256' in item:
            assert f.sha(f.BASE/directory/f"OT_2003CHUNK2_{item['case']}_PUBLIC.md")==item['original_public_sha256']
    assert f.sha(p)==item['record_sha256']
    assert hashlib.sha256(pub.encode()).hexdigest()==item['public_sha256']
    for rel,h in item['audit_inputs'].items():
        assert f.sha(f.BASE/rel)==h
        assert f.read(Path(rel)) in s
    holdings=re.search(r'^## Holdings\n(.*?)(?=^## Precedent Treatment)',pub,re.M|re.S).group(1).strip()
    internal=re.search(r'^## Controlling holdings\n(.*?)(?=^## Precedent treatment and resulting law)',s,re.M|re.S).group(1).strip()
    assert internal==holdings
    assert [len(x.split()) for x in re.split(r'\n### ',holdings)]==item['complete_holding_words']
    d=json.loads((f.BASE/f"runtime/OT_2003CHUNK2_{item['case']}_FINAL_ASSEMBLY_DATA.json").read_text(encoding='utf-8'))
    join_names=[x.split('|')[1].strip() for x in d['joins'].splitlines() if x.startswith('| ')][1:]
    assert sorted(join_names)==sorted(f.NAMES)
    for bad in ['One'+'Drive','Git'+'Hub','file://','C:\\Users']:assert bad not in s
    assert not re.search(r'(?i)reserved for final|authorship unassigned|workflow|reconcil|simulat|2026|runtime/|freeze/',pub)
    rows.append(f"| {item['case']} | {item['author']} | PASS | PASS | PASS | {', '.join(map(str,item['complete_holding_words']))} |")

deaton=f.read(Path('freeze/OT_2003CHUNK2_DEATON_PUBLIC_COMPLETENESS.md'))
castro=f.read(Path('freeze/OT_2003CHUNK2_CASTRO_PUBLIC.md'))
pringle=f.read(Path('freeze/OT_2003CHUNK2_PRINGLE_PUBLIC_COMPLETENESS.md'))
assert 'Holston' not in deaton and 'United States v. Ho' not in deaton
assert 'without adding a ground' in deaton and 'frequency and duration' in deaton
assert 'cannot reasonably internalize or control it through ordinary territorial authority' in deaton
assert 'Part I' in castro and 'without joining Parts II–III' in castro
assert 'voluntariness, waiver, suppression or trial' not in pringle
assert 'presume passenger guilt or a criminal enterprise' in pringle
assert 'the officer’s announcement that everyone would be arrested adds no probable cause' in pringle
assert '## Separate Writings\n\n\n\n' in pringle
assert '- Illinois v. Wardlow:' in pringle and '- United States v. Valentine:' in pringle
for key in ['DEATON','PRINGLE']:
    name=f'OT_2003CHUNK2_{key}_PUBLIC_COMPLETENESS_VALIDATION.md'
    assert (f.BASE/'runtime'/name).read_bytes()==(f.BASE/'freeze'/name).read_bytes()

base=f.read(Path('runtime/OT_2003CHUNK2_B_REMAINING_ASSEMBLY_VALIDATION.md')).split('\n## Final independent byte and completeness checks',1)[0]
extra='''
## Final independent byte and completeness checks

The validation script independently reread all twenty prior actual opinion tables and the three newly created Records. All refreshed prior topology snapshots match the current Records. Each final Record has the four exact opening labels, eleven ordered Public Projection blocks, identical internal and public controlling holdings, all nine named component rows, exact frozen audit-source inclusion and unchanged source hashes. Runtime/freeze public twins are byte-identical to the bounded Record section. No public assignment placeholder, process metadata, prohibited provider name or machine link remains.

| Case | Lead author | Record/public twins | Frozen source identity | Nine-Justice component rows | Complete holding words |
|---|---|---|---|---|---|
'''+ '\n'.join(rows)+'''

The counts below were derived again from all twenty-three actual topology tables after final assembly. They are an ending verification, never a substitute for the distinct before-assignment counts above.

'''+json.dumps(counts,ensure_ascii=False,indent=2)+'''

### Engine §15 and five-block §8 result

PASS at assembly scope. Each approved Chief proposition, limited join and remedy was checked; Deaton uses the standing fallback only for the genuinely silent delineation component. Castro and Pringle use no fallback. Deaton has nine disposition votes, eight complete grounds for I/III/IV and nine for II, with precise Chief coverage and operative-remedy assent. Castro has nine jurisdiction/disposition votes, seven warning-rule and warning-based application joins, and the two preserved independent-ground merits agreements. Pringle has nine complete P1–P3 joins after the additive model and reconciliation.

The negative-statement review separately covered Judgment & Remedy, Holdings, Precedent Treatment, Law After Decision and Procedure After Action. Deaton's contractor-market and neighboring Virginia comparisons remain internal; its actual Home Builders alternative, preserved Manual challenge and remedy dispute remain material. Castro retains only the actual authorization/classification distinction, noncounting consequence, earlier judgment status and ordinary first-motion limits. Pringle retains the actual Houghton limit, concealed-drug and contemporaneous-knowledge conditions, silence qualification and bounded arrest-derived remedy; hypothetical issue, vehicle-type and other-occupant catalogues are omitted. No public ground was added to manufacture a complete join.

The full proposition, authority and explanation for every ordinary holding, including its heading, remains below 350 words. Separate precedent treatment and resulting law remain distinct. Every final record contains a later-five public-law consequence screen after its own holdings were fixed; no necessary later premise was displaced. Neither later law nor same-day Castro supplied Pringle's merits.

The final Deaton public copy is OT_2003CHUNK2_DEATON_PUBLIC_COMPLETENESS.md. It script-copies the complete Home Builders externality qualification from the fixed entering-law authority and separates each materially used precedent into its own treatment line. The original DEATON_PUBLIC snapshots consumed by Castro and Pringle remain unchanged, with original and final hashes listed above. The expanded qualification changes neither later case's procedural predicate, personal-probability ground or remedy; both Deaton chronology screens remain correct. The final Pringle public copy is OT_2003CHUNK2_PRINGLE_PUBLIC_COMPLETENESS.md, which only separates Wardlow and Valentine treatment lines. Its original snapshots likewise remain unchanged. Castro's original PUBLIC twins are its final public copy. Each completeness receipt has identical runtime/freeze bytes and records final Record and public hashes. These initial-validation passes change no adjudication.

The final current-law reconciliation arrived after the Deaton and Castro Records were written and confirms their exact already-frozen grounds and joins without additional change. Its full text is copied below as additive assembly evidence. It does not silently alter those completed Records. Pringle includes that receipt directly in its internal annex. Workspace publication, Render Input generation, full term checks and operator commitment remain root integration tasks.

## Final current-law reconciliation receipt — exact additive copy

'''+f.read(Path('freeze/OT_2003CHUNK2_FINAL_PUBLIC_LAW_RECONCILED.md'))
for directory in ['runtime','freeze']:(f.BASE/directory/'OT_2003CHUNK2_B_REMAINING_ASSEMBLY_VALIDATION.md').write_text(base+extra,encoding='utf-8',newline='\n')
assert (f.BASE/'runtime/OT_2003CHUNK2_B_REMAINING_ASSEMBLY_VALIDATION.md').read_bytes()==(f.BASE/'freeze/OT_2003CHUNK2_B_REMAINING_ASSEMBLY_VALIDATION.md').read_bytes()
print(json.dumps({'records':f.CREATED,'final_counts':counts,'validation_sha256':f.sha(f.BASE/'freeze/OT_2003CHUNK2_B_REMAINING_ASSEMBLY_VALIDATION.md')},ensure_ascii=False))
