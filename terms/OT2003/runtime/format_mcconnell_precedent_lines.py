from pathlib import Path
import re,hashlib,json

T=Path('terms/OT2003'); R=T/'runtime'; F=T/'freeze'
record=T/'records/mcconnell_v_federal_election_commission_merits_2003-12-10.md'
before_bytes=record.read_bytes()
assert before_bytes.count(b'\n')==before_bytes.count(b'\r\n')
before=before_bytes.decode('utf-8').replace('\r\n','\n')
def same_bytes(text): return text.replace('\n','\r\n').encode('utf-8')
stage_paths=[d/name for d in [R,F] for name in ['OT_2003CHUNK2_MCCONNELL_PUBLIC.md','OT_2003CHUNK2_MCCONNELL_ASSEMBLY_VALIDATION.md']]
stage_hashes={str(p.relative_to(T)):hashlib.sha256(p.read_bytes()).hexdigest() for p in stage_paths}
public=before.split('## Public Projection\n\n',1)[1]
a=public.index('## Precedent Treatment\n\n')+len('## Precedent Treatment\n\n')
b=public.index('## Law After Decision\n',a)
old=public[a:b].rstrip()
entries=re.findall(r'(?ms)^\*\*(.+?):\*\* (.*?)(?=^\*\*|\Z)',old)
assert len(entries)==30

# Each item carries the existing holding label forward from saved bytes.
# Only the treatment prose is separated by already named decision.
layout=[
([
('Lamb','Applied to supported preventive control without a completed local scandal; its separate fit requirement remains.'),
('Colorado II','Applied to demonstrated circumvention.'),
('Colorado I','Retains protection for genuinely independent expenditure.'),
('Shrink Missouri','Retains its objective-justification limit.'),
('Day','Retains its meaningful-association limit.'),
('Mariani','Retains its actual-source limit.'),
('Daggett','Its voluntary capped public-financing permission supplies neither an equalization power nor a public-funding mandate.')],[]),
([
('Colorado II','Applied to the identified transfer and shared-operation mechanism.'),
('Lamb','Applied to the identified transfer and shared-operation mechanism.'),
('Day','Its meaningful-chosen-association requirement remains independently binding.')],
['The accommodation does not create a universal permissible contribution amount.']),
([
('Bartlett','Supplies the distinction between electoral campaigning and incidental issue influence.'),
('Clifton','Preserves independent issue inquiries.'),
('Colorado I','Remains effective for actual independence.'),
('Colorado II','Supports the separately established financing safeguard.'),
('Lamb','Supports the separately established financing safeguard.')],[]),
([
('Lamb','Its separate government-borne fit requirement is applied.'),
('Stengel','Its operation-specific inquiry is applied.')],
['The accepted federal-election source does not settle the independent speech burden.']),
([
('Day','Retains protection for meaningful use of the lawful chosen channel.'),
('Mariani','Retains protection for meaningful use of the lawful chosen channel.'),
('Lamb','Supports the distinct nonfederal conduit rule.'),
('Colorado II','Supports the distinct nonfederal conduit rule.')],
['Section 401 operates through application severance, not deletion of statutory coverage words.']),
([
('Lamb',"Applied to the official's own supported fundraising relation."),
('Mariani',"Applied to the official's own supported fundraising relation."),
('Colorado I','Continues to protect independent expression outside that relation.'),
('Clifton','Continues to protect ordinary issue cooperation outside that relation.')],[]),
([
('Austin','Retained within its independent electoral-treasury setting.'),
('Bartlett','Its genuine-issue protection remains effective.'),
('Maine Right to Life','Its definite, non-slogan-only approach remains effective.'),
('Beaumont','Its direct-contribution holding is distinguished.'),
('Stengel','Its direct-contribution holding is distinguished.'),
('Buckley','Retains independent-expenditure protection.'),
('Colorado I','Retains independent-expenditure protection.')],[]),
([
('MCFL','Applied through the actual-characteristics protection stated here.'),
('Day','Its actual-characteristics protection applies, including incidental-receipt and formal-defect limits.'),
('Stengel','Continues to distinguish this independent-spending protection from direct candidate contributions.')],[]),
([
('Maine Right to Life','Its cumulative contextual construction remains applicable in its own setting.')],
['The fallback remains inactive under its enacted trigger.']),
([
('Colorado I','Retains its independence function.'),
('Colorado II','Retains its contribution function.'),
('Lamb','Retains its actual-resource function.'),
('Akins','Retains its actual-resource function.'),
('Clifton','Its ordinary-inquiry and independent-editing boundary remains.')],
['No contribution classification arises from party identity alone.']),
([
('Colorado I','Remains an independent constitutional protection.'),
('Clifton','Remains an independent constitutional protection.'),
('Lamb','Continues to permit genuine financial-resource treatment.')],
['The definitions neither broaden nor repeal those holdings.']),
([
('Maine Right to Life','Its permissive advisory procedure remains.'),
('Lee','Its present-civil-duty rule remains.'),
('National Park Hospitality','Distinguished by its nonbinding policy.'),
('Barnhart','Requires an actual statutory assignment and its lawful exercise.')],[]),
([
('Colorado I','Its independence rule is applied.'),
('Colorado II','Its actual-coordination limit is applied.'),
('Day','Preserves meaningful association in the reciprocal choice presented here.'),
('Lamb','Preserves meaningful association in the reciprocal choice presented here.')],[]),
([
('Buckley','Its supported-reprisal protection remains.'),
('Brown','Its supported-reprisal protection remains.'),
('Stengel','Supports financial-source reporting.'),
('Akins','Supports financial-source reporting.'),
('Mariani','Supports financial-source reporting.'),
('McIntyre','Its individual-anonymity protection is preserved and distinguished.'),
('Bartlett','Its issue-expression and full-committee limits are preserved and distinguished.')],[]),
([
('Stengel','Applied to actual obligations.'),
('Akins','Applied to actual obligations.'),
('Mariani','Applied to actual obligations.'),
('Clifton','Its independent editorial protection remains distinct.')],[]),
([
('Lee','Preserves review of concrete civil duties.'),
('Maine Right to Life','Preserves review of concrete civil duties.'),
('National Park Hospitality','Its policy setting supplies no contrary categorical bar.')],
['The actual-obligation reasoning of the section 201 holding governs this parallel claim.']),
([
('Lujan','Applied to the actual temporal and personal nexus.'),
('Raines','Applied to the actual temporal and personal nexus.'),
('Lee','Its recognition of civil-duty and lost-benefit injury is preserved.')],
['Section 403 permission does not replace Article III.']),
([
('Lujan','Its injury and redressability elements remain separate.'),
('Mariani','Its section 437h route is applied without automatic certification or conversion of this direct appeal into review of every FECA restriction.')],[]),
([
('Lujan','Applied to particularization and causation.'),
('Raines','Applied to particularization and causation.'),
('Akins','Its recognition of concrete shared injury remains.')],
['No categorical competitor-standing bar follows.']),
([
('Lujan','Supplies the claimant-specific threshold.'),
('Raines','Supplies the claimant-specific threshold.'),
('Day','Its public-financing position does not determine the merits or create injury under this formula.'),
('Daggett','Its different public-financing position does not determine the merits or create injury under this formula.')],[]),
([
('Stengel','Its source-identification distinction is applied.'),
('Clifton','Its separate-disclosure reservation is applied.'),
('McIntyre','Its individual-pamphlet protection remains.'),
('Bartlett','Its prohibition/full-committee boundary is not converted into a universal reporting boundary.')],[]),
([
('Buckley','Its contribution fit standard is applied.'),
('Shrink Missouri','Its contribution fit standard is applied.'),
('Day','Its chosen-channel protection is applied.'),
('Russell','Its chosen-channel protection is applied.'),
('Lamb','Its chosen-channel protection is applied.'),
('Mariani','Its true-source restrictions remain independently enforceable.'),
('Tinker',"Supports the existence of minors' rights without replacing the contribution inquiry.")],[]),
([
('Stengel','Supports connected transaction information.'),
('Akins','Supports connected transaction information.'),
('Clifton','Preserves the distinct editorial interest.'),
('McIntyre','Preserves the distinct anonymity interest.')],
['Existing administrative practice is evidence of fit rather than an independently adjudicated constitutional safe harbor.']),
([
('Bellotti','Retains full expressive protection for noninstitutional publishers.'),
('McIntyre','Retains full expressive protection for noninstitutional publishers.'),
('Stengel','Supplies the distinct financing function.'),
('Akins','Supplies the distinct financing function.'),
('Clifton','Supplies the distinct editorial function.'),
('Mariani','Supplies the distinct source function.')],
['These distinctions supply no institutional press supremacy.']),
([
('Lujan',"Applied to the plaintiffs' own duties."),
('Printz',"Applied to the plaintiffs' own duties."),
('Guillen','Its reserved question remains reserved beyond this direct-regulation setting.'),
('Tennessee Electric','Distinguished by its competitive-injury setting.')],[]),
([
('Voting Rights Coalition','Supplies the election-specific sources.'),
('Smiley','Supplies the election-specific source applied here.'),
('Siebold','Supplies the election-specific source applied here.'),
('Burroughs','Supplies the election-specific source applied here.'),
('Thornton','Preserves qualifications and representative-structure limits.'),
('Cook','Preserves qualifications and representative-structure limits.'),
('Lopez','Supplies source discipline by analogy without creating an interstate-commerce element or an alternative commerce holding.'),
('Holston','Supplies source discipline by analogy without creating an interstate-commerce element or an alternative commerce holding.'),
('Ho','Supplies source discipline by analogy without creating an interstate-commerce element or an alternative commerce holding.')],[]),
([
('New York','Retains the direct-regulation/compulsory-government distinction.'),
('Condon','Retains the direct-regulation/compulsory-government distinction.'),
('Printz','Neither its actual holding nor its structural separate position is enlarged to prohibit this different arrangement.'),
('Voting Rights Coalition','Preserves state qualifications and the source-specific election rule.')],[]),
([
('Day','Preserves actual rather than label-based distinctions.'),
('Lamb','Preserves actual rather than label-based distinctions.'),
('Valeria','Its racial-classification, proxy or selective-barrier rule is applied; an animus-only substitute is rejected.')],
['The other governing financing decisions likewise preserve actual rather than label-based distinctions.']),
([
('Bartlett','Supplies the actual coverage limits.'),
('Maine Right to Life','Supplies the actual coverage limits.'),
('Clifton','Supplies the actual coverage limits.'),
('Greenville','Its distinction between contextual notice and an independent branch lacking an operative standard remains effective.')],[]),
([],['Ordinary injury and remedial requirements remain applicable to the actual claim and relief.'])
]
assert len(layout)==len(entries)
new_blocks=[]; decisions_by_holding=[]
for (title,old_body),(cases,other) in zip(entries,layout):
    assert len({case for case,_ in cases})==len(cases)
    for case,_ in cases: assert case in old_body,(title,case)
    treatment='\n'.join(f'- **{case}:** {text}' for case,text in cases)
    body='\n\n'.join(part for part in [treatment,*other] if part)
    new_blocks.append(f'**{title}:**\n\n{body}')
    decisions_by_holding.append({'holding':title,'decisions':[case for case,_ in cases]})
new='\n\n'.join(new_blocks)
internal_start='## Precedent treatment and present force\n\n'
ia=before.index(internal_start)+len(internal_start)
ib=before.index('## Law after the decision\n',ia)
assert before[ia:ib].rstrip()==old
assert before.count(old)==2
after=before.replace(old,new)
after_public=after.split('## Public Projection\n\n',1)[1]
expected=['Event','Participation','Public Action','Judgment & Remedy','Opinion Topology','Holdings','Precedent Treatment','Law After Decision','Separate Writings','Procedure After Action','Source Notes']
assert re.findall(r'^## (.+)$',after_public,re.M)==expected
def blocks(text):
    return {m.group(1):m.group(2) for m in re.finditer(r'(?ms)^## (.+?)\n\n(.*?)(?=^## |\Z)',text)}
pb=blocks(public); pa=blocks(after_public)
assert all(pb[label]==pa[label] for label in expected if label!='Precedent Treatment')
assert before.replace(old,'<TREATMENT>')==after.replace(new,'<TREATMENT>')
after_bytes=same_bytes(after)
assert before_bytes.replace(same_bytes(old),b'<TREATMENT>')==after_bytes.replace(same_bytes(new),b'<TREATMENT>')
for path,sha in stage_hashes.items(): assert hashlib.sha256((T/path).read_bytes()).hexdigest()==sha
for text in [after,after_public,Path(__file__).read_text(encoding='utf-8')]:
    for banned in ['one'+'drive','git'+'hub','fi'+'le://','c:'+'/'+'users/']: assert banned not in text.lower()

record.write_bytes(after_bytes)
for directory in [R,F]:
    (directory/'OT_2003CHUNK2_MCCONNELL_PUBLIC_FINAL_LAYOUT.md').write_bytes(same_bytes(after_public))
record_after_sha=hashlib.sha256(record.read_bytes()).hexdigest()
final_sha=hashlib.sha256((F/'OT_2003CHUNK2_MCCONNELL_PUBLIC_FINAL_LAYOUT.md').read_bytes()).hexdigest()
receipt=f'''# McConnell final precedent-treatment layout validation

**Result:** Passed. This is the expressly authorized initial-presentation layout correction to McConnell's current Record. No older baseline Record was edited.

The 30 existing holding labels remain. Each named earlier decision now receives its own treatment line under its existing label: {sum(len(cases) for cases,_ in layout)} individual decision lines. Combined grammatical subjects were separated without adding an authority or changing the existing treatment, operative scope or consequence. Present-case statutory, transition and scope sentences remain separate from those decision lines. The matching internal treatment block and Public Projection treatment block contain the identical final text.

**Unchanged substance:** Every public block other than Precedent Treatment is byte-identical to its pre-layout Record block, including all holding rules and explanations, coalitions, authors, judgments, remedies and separate writings. Replacing the two treatment blocks with the same sentinel makes the before and after complete Records byte-identical. The four opening labels and original-decision lineage remain unchanged. The eleven level-two public blocks retain their exact order. No new argument, statutory construction, legal ground or authority has been introduced; no Associate commitment or approved Chief position has changed. The prior section 8 and section 15 substantive results therefore remain applicable; the present section 15 layout/interface check passed.

The original runtime/freeze `MCCONNELL_PUBLIC` and `MCCONNELL_ASSEMBLY_VALIDATION` snapshots were hash-checked before and after and remain unchanged for the screens that already consumed them. The new final-layout handoff is copied exactly from the current Record's bounded Public Projection, without a stage header. Runtime/freeze final-layout public files and validation receipts are byte-identical. No workspace, generated Render Input or public render was edited.

## Saved-byte hashes

| Artifact | SHA-256 |
|---|---|
| Record before layout | `{hashlib.sha256(before_bytes).hexdigest()}` |
| Record after layout | `{record_after_sha}` |
| Final-layout public handoff | `{final_sha}` |
'''
receipt+='\n'.join(f'| `{path}` (preserved) | `{sha}` |' for path,sha in stage_hashes.items())
receipt+='\n\n**Final artifacts:** `records/mcconnell_v_federal_election_commission_merits_2003-12-10.md`; runtime/freeze `OT_2003CHUNK2_MCCONNELL_PUBLIC_FINAL_LAYOUT.md`; runtime/freeze `OT_2003CHUNK2_MCCONNELL_FINAL_LAYOUT_VALIDATION.md`.\n'
for directory in [R,F]:
    (directory/'OT_2003CHUNK2_MCCONNELL_FINAL_LAYOUT_VALIDATION.md').write_text(receipt,encoding='utf-8')
for path,sha in stage_hashes.items(): assert hashlib.sha256((T/path).read_bytes()).hexdigest()==sha
assert (R/'OT_2003CHUNK2_MCCONNELL_PUBLIC_FINAL_LAYOUT.md').read_bytes()==(F/'OT_2003CHUNK2_MCCONNELL_PUBLIC_FINAL_LAYOUT.md').read_bytes()
assert (R/'OT_2003CHUNK2_MCCONNELL_FINAL_LAYOUT_VALIDATION.md').read_bytes()==(F/'OT_2003CHUNK2_MCCONNELL_FINAL_LAYOUT_VALIDATION.md').read_bytes()
assert record.read_text(encoding='utf-8').split('## Public Projection\n\n',1)[1]==(F/'OT_2003CHUNK2_MCCONNELL_PUBLIC_FINAL_LAYOUT.md').read_text(encoding='utf-8')
print('Final layout verified:',sum(len(cases) for cases,_ in layout),'individual precedent lines under',len(layout),'unchanged holding labels.')
print('Record SHA-256:',record_after_sha)
print('Final-layout public SHA-256:',final_sha)
