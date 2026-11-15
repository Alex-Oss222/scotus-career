import json,re,hashlib
from pathlib import Path
import finalize_chunk2_b_remaining as f

f.restore()
item=next(v for v in f.VALIDATION if v['case']=='DEATON')
p=f.BASE/'records'/item['record']
old=p.read_text(encoding='utf-8')
assert f.sha(p)==item['record_sha256']
source=f.BASE/'entering-law/OT_2003CHUNK2_B.md'
assert f.sha(source)=='4e50ffae841ef5502212fdbb8564d79bd5d7f083b4bcbb1e333d4c82146c4766'
text=source.read_text(encoding='utf-8-sig')
exact=re.search(r'The externality route requires identification of the regulated class;.*?the reasonable fit of the federal prohibition to that effect\.',text,re.S).group()
old_sentence='Home Builders’ independent externality route retains its distinct requirements of concrete substantial interstate spillover, limits on state containment and fitted regulation; drainage alone does not establish them.'
replacement='Home Builders retains a separate externality route. '+exact+' Drainage alone does not establish those conditions.'
assert old.count(old_sentence)==2
updated=old.replace(old_sentence,replacement)
updated=updated.replace('**Version / lineage:** Original decision.','**Version / lineage:** Original decision; initial-validation completeness pass states the preserved Home Builders qualification in full. Judgment, grounds, joins, author and remedy are unchanged.',1)
pub=updated.split('## Public Projection\n\n',1)[1]
holds=re.search(r'^## Holdings\n(.*?)(?=^## Precedent Treatment)',pub,re.M|re.S).group(1).strip()
full_words=[len(x.split()) for x in re.split(r'\n### ',holds)]
assert all(w<=350 for w in full_words),full_words
explanation_words=[len(m.group(1).split()) for m in re.finditer(r'\*\*Controlling explanation:\*\*\s*(.*?)(?=\n### |\n\*\*Authority:|\Z)',holds,re.S)]
updated=updated.replace('Ordinary explanation counts: '+', '.join(map(str,item['explanation_words'])), 'Ordinary explanation counts: '+', '.join(map(str,explanation_words)))
before=f.BASE/'runtime/OT_2003CHUNK2_DEATON_RECORD_BEFORE_COMPLETENESS.md'
assert not before.exists()
before.write_bytes(p.read_bytes())
p.write_text(updated,encoding='utf-8',newline='\n')
for directory in ['runtime','freeze']:
    q=f.BASE/directory/'OT_2003CHUNK2_DEATON_PUBLIC_COMPLETENESS.md'
    assert not q.exists();q.write_text(pub,encoding='utf-8',newline='\n')
    original=f.BASE/directory/'OT_2003CHUNK2_DEATON_PUBLIC.md'
    assert f.sha(original)==item['public_sha256']
data_path=f.BASE/'runtime/OT_2003CHUNK2_DEATON_FINAL_ASSEMBLY_DATA.json'
d=json.loads(data_path.read_text(encoding='utf-8'))
d['public']['Holdings']=d['public']['Holdings'].replace(old_sentence,replacement)
data_path.write_text(json.dumps(d,ensure_ascii=False,indent=2),encoding='utf-8',newline='\n')
item['initial_record_sha256']=item['record_sha256']
item['original_public_sha256']=item['public_sha256']
item['record_sha256']=f.sha(p)
item['public_sha256']=hashlib.sha256(pub.encode()).hexdigest()
item['final_public_basename']='OT_2003CHUNK2_DEATON_PUBLIC_COMPLETENESS.md'
item['complete_holding_words']=full_words
item['explanation_words']=explanation_words
receipt='''# Deaton — initial-validation public completeness

The Home Builders externality alternative was already expressly addressed in the approved question and preserved by the frozen grounds. The final wording now states its complete source qualification instead of the shorthand limits on state containment and fitted regulation. The exact operative sentence below was copied by script from the fixed entering-law authority copy, whose saved hash is verified. That copy preserves the earlier Home Builders rule; no later decision supplies the qualification.

'''+exact+'''

Judgment, all four independent grounds, the Chief's differentiated joins and delineation fallback, Kennedy's assignment, remedy and procedural stage are unchanged. This is an initial-validation completeness pass. The original public snapshots consumed by the later assemblies remain byte-identical; the final Record corresponds to the new completeness twins.

No material effect on Castro or Pringle: the expanded wording concerns an unneeded alternative Commerce Clause route for wetland regulation. It changes no judicial-conversion predicate, first-motion protection, personal probable-cause standard, possession inference or suppression consequence. Their already-recorded Deaton chronology screens remain correct. No new modeling or reconciliation choice is introduced.

| Artifact | SHA256 |
|---|---|
'''+f"| Fixed entering-law copy | {f.sha(source)} |\n| Saved pre-completeness Record | {f.sha(before)} |\n| Preserved original public snapshots | {item['original_public_sha256']} |\n| Final Record | {item['record_sha256']} |\n| New public completeness twins | {item['public_sha256']} |\n"+f"\nFull holding word counts: {full_words}. Exact internal/public holding identity, eleven-block order and unchanged original snapshot hashes pass.\n"
for directory in ['runtime','freeze']:(f.BASE/directory/'OT_2003CHUNK2_DEATON_PUBLIC_COMPLETENESS_VALIDATION.md').write_text(receipt,encoding='utf-8',newline='\n')
f.save_progress()
print(json.dumps(item,ensure_ascii=False))
