from pathlib import Path
import hashlib
root=Path('terms/OT1995')
source=(root/'freeze/OT_1995CHUNK9_MEDTRONIC_COMMITMENTS.md').read_text(encoding='utf-8-sig')
assert hashlib.sha256((root/'freeze/OT_1995CHUNK9_MEDTRONIC_COMMITMENTS.md').read_bytes()).hexdigest().upper()=='8718FF0E7D23A02E801EE234BD93C13ECF04934137F34F3107BB5803670DFE09'
prefix=(root/'research/chunk9_reconcile_med/RECONCILIATION_PREFIX.md').read_text(encoding='utf-8-sig')
suffix=(root/'research/chunk9_reconcile_med/RECONCILIATION_SUFFIX.md').read_text(encoding='utf-8-sig')
a=source.index('## Questions, claims and common remedial boundaries')
b=source.index('## Decisive actual precedents and individual evidence')
common=source[a:b]
old='Common-law liability can impose a requirement; it is neither categorically excluded nor automatically displaced. The actual duty is compared, rather than the negligence or strict-liability label.'
new='O\'Connor, Scalia, Thomas and Breyer affirmatively treat common-law duties as potentially preemptible requirements. Stevens, Kennedy, Souter and Ginsburg reserve that general express-preemption question while rejecting automatic displacement of these duties; they do not adopt categorical common-law immunity. Each compares the actual duty rather than relying on the negligence or strict-liability label.'
assert old in common
common=common.replace(old,new)
common=common.replace('## Statutory and regulatory qualifications integral to the commitments','## Statutory and regulatory qualifications integral to the commitments\n\nThese paragraphs retain the complete operative text qualifications and source boundaries from independent modeling. They do not attribute agreement on an added specificity prerequisite to O\'Connor, Scalia or Thomas: their statutory interpretation and alternative regulatory argument are distinguished above and below.')
common=common.replace('identity below','identity below')
suffix=suffix.replace('qualifications below','qualifications above')
out=prefix+common+'\n'+suffix
p=root/'freeze/OT_1995CHUNK9_MEDTRONIC_RECONCILED.md'
r=root/'runtime/OT_1995CHUNK9_MEDTRONIC_RECONCILED.md'
p.write_text(out,encoding='utf-8',newline='\n')
r.write_bytes(p.read_bytes())
assert p.read_bytes()==r.read_bytes()
print('chars',len(out),'words',len(out.split()))
print('SHA256',hashlib.sha256(p.read_bytes()).hexdigest().upper())
print('runtime identical: yes')
