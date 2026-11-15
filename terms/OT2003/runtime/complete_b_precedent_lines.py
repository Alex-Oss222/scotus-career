import json,hashlib
import finalize_chunk2_b_remaining as f

f.restore()
changes={
 'DEATON':{
 '- United States v. Haggar Apparel Co. and United States v. Mead Corp.: applied to actual delegation, its exercise and independent enforcement of statutory limits before controlling deference.':
 '- United States v. Haggar Apparel Co.: applied to actual delegated authority and independent enforcement of statutory limits before controlling deference.\n- United States v. Mead Corp.: applied to actual delegation and its exercise through a mechanism carrying the force of law before controlling deference.',
 '- United States v. Rio Grande Dam & Irrigation Co., United States v. Appalachian Electric Power Co., Oklahoma ex rel. Phillips v. Guy F. Atkinson Co., United States v. Grand River Dam Authority and Caminetti v. United States: applied to protecting navigable channels against harmful uses and upstream interference through relevant nonnavigable reaches.':
 '- United States v. Rio Grande Dam & Irrigation Co.: applied to protection of navigable water against upstream interference.\n- United States v. Appalachian Electric Power Co.: applied to protection of navigable waters through relevant nonnavigable reaches.\n- Oklahoma ex rel. Phillips v. Guy F. Atkinson Co.: applied to protection of navigable waters through relevant nonnavigable reaches.\n- United States v. Grand River Dam Authority: applied to protection of navigable waters through relevant nonnavigable reaches.\n- Caminetti v. United States: applied to protection of navigable channels against harmful uses.'},
 'PRINGLE':{
 '- Illinois v. Wardlow and United States v. Valentine: applied to the requirement of a supported personal connection to wrongdoing; the actual cocaine and common-transport evidence meet that requirement here under the higher probable-cause threshold.':
 '- Illinois v. Wardlow: applied to the requirement of a supported personal connection to wrongdoing; the actual cocaine and common-transport evidence meet that requirement here under the higher probable-cause threshold.\n- United States v. Valentine: applied to the requirement of a supported personal connection to wrongdoing; the actual cocaine and common-transport evidence meet that requirement here under the higher probable-cause threshold.'}
}
for key,replacements in changes.items():
    item=next(x for x in f.VALIDATION if x['case']==key)
    p=f.BASE/'records'/item['record'];old=p.read_text(encoding='utf-8');updated=old
    old_record_hash=f.sha(p);old_public_hash=item['public_sha256']
    if key=='PRINGLE':
        saved=f.BASE/'runtime/OT_2003CHUNK2_PRINGLE_RECORD_BEFORE_COMPLETENESS.md';assert not saved.exists();saved.write_bytes(p.read_bytes())
        item['initial_record_sha256']=old_record_hash;item['original_public_sha256']=old_public_hash
    if key=='DEATON':
        updated=updated.replace('Ordinary explanation counts: 225, 218, 160, 141','Ordinary explanation counts: 225, 260, 160, 141')
        updated=updated.replace('initial-validation completeness pass states the preserved Home Builders qualification in full.','initial-validation completeness pass states the preserved Home Builders qualification in full and gives each materially used precedent its own treatment line.')
    else:
        updated=updated.replace('**Version / lineage:** Original decision.','**Version / lineage:** Original decision; initial-validation completeness pass gives Wardlow and Valentine separate precedent-treatment lines. Judgment, grounds, joins, author and remedy are unchanged.',1)
    data_path=f.BASE/f'runtime/OT_2003CHUNK2_{key}_FINAL_ASSEMBLY_DATA.json';d=json.loads(data_path.read_text(encoding='utf-8'))
    for before,after in replacements.items():
        assert updated.count(before)==2,(key,before,updated.count(before))
        updated=updated.replace(before,after)
        assert d['public']['Precedent Treatment'].count(before)==1
        d['public']['Precedent Treatment']=d['public']['Precedent Treatment'].replace(before,after)
    p.write_text(updated,encoding='utf-8',newline='\n')
    data_path.write_text(json.dumps(d,ensure_ascii=False,indent=2),encoding='utf-8',newline='\n')
    pub=updated.split('## Public Projection\n\n',1)[1]
    basename=f'OT_2003CHUNK2_{key}_PUBLIC_COMPLETENESS.md'
    for directory in ['runtime','freeze']:
        (f.BASE/directory/basename).write_text(pub,encoding='utf-8',newline='\n')
        assert f.sha(f.BASE/directory/f'OT_2003CHUNK2_{key}_PUBLIC.md')==item['original_public_sha256']
    item['record_sha256']=f.sha(p);item['public_sha256']=hashlib.sha256(pub.encode()).hexdigest();item['final_public_basename']=basename
    if key=='DEATON':
        receipt=(f.BASE/'runtime/OT_2003CHUNK2_DEATON_PUBLIC_COMPLETENESS_VALIDATION.md').read_text(encoding='utf-8')
        assert old_record_hash in receipt
        receipt=receipt.replace(old_record_hash,item['record_sha256']).replace(old_public_hash,item['public_sha256'])
        receipt+='\nThe same initial-validation pass separates Haggar, Mead and each of the five channel authorities into individual precedent-treatment lines. Each line states its already-adopted role; no new rationale, vote or remedy is added. The internal and public treatment lists match.\n'
    else:
        receipt='''# Pringle — initial-validation public completeness

Wardlow and Valentine now each receive a separate precedent-treatment line. Each carries the identical supported treatment from the former combined line. No proposition, explanation, vote, join, author, remedy, remand limit or historical-rationale departure changes. The final Record and new completeness twins match; the original public snapshots and a pre-completeness Record copy remain intact.

This formatting completion changes no premise of any later decision. The final additive model, historical reconciliation and current-law receipts remain byte-identical and authoritative at their respective stages.

| Artifact | SHA256 |
|---|---|
'''+f"| Saved pre-completeness Record | {item['initial_record_sha256']} |\n| Preserved original public snapshots | {item['original_public_sha256']} |\n| Final Record | {item['record_sha256']} |\n| New public completeness twins | {item['public_sha256']} |\n"
    for directory in ['runtime','freeze']:(f.BASE/directory/f'OT_2003CHUNK2_{key}_PUBLIC_COMPLETENESS_VALIDATION.md').write_text(receipt,encoding='utf-8',newline='\n')
    print(json.dumps({'case':key,'record_sha256':item['record_sha256'],'final_public_basename':basename,'public_sha256':item['public_sha256']},ensure_ascii=False))
f.save_progress()
