"""Complete internal integration status and copy the public coalition declaration."""
from pathlib import Path
import re

term = Path(__file__).resolve().parents[1]
record = term / 'records/In_re_Vey_financial_leave_1997-04-14.md'
data = record.read_bytes()
text = data.decode('utf-8')
newline = '\r\n' if '\r\n' in text else '\n'
normalized = text.replace('\r\n', '\n')
public = normalized.split('## Public Projection\n', 1)[1]
topology = re.search(r'^## Opinion Topology\n(.*?)(?=^## )', public, re.M | re.S)[1].strip()
authority = 'Authority: [Record](../records/' + record.name + ').'
old = authority + '\n\n#### Holdings'
new = authority + '\n\n#### Opinion Topology\n\n' + topology + '\n\n#### Holdings'
for name in ['continuity.md', 'neutral-projection.md']:
    path = term / 'workspace' / name
    doc = path.read_text(encoding='utf-8')
    assert doc.count(old) == 1
    path.write_text(doc.replace(old, new), encoding='utf-8')

pending = re.search(r'^Durably written for root final review and integration\..*$', normalized, re.M)
assert pending and 'pending root integration' in pending[0]
completed = (
    '**Date applied to Current Term State: October 13, 2026, effective April 14, 1997.** '
    'The manifest, ledger, continuity and neutral projection now include this completed event; '
    'the generated chunk 6 Render Input contains all twelve Records with no stopped-matter notice. '
    'The [independent dependency review](../freeze/OT_1996CHUNK6_68_DEPENDENCY_REVIEW.md) '
    'found no material effect on any later adjudication; only three internal entering-law notes were corrected. '
    'The [resumption validation](../freeze/OT_1996CHUNK6_68_RESUMPTION_VALIDATION.md) '
    'records the completed non-Git checks and protected-file comparisons. '
    'No Git command was run: repository commitment and Git-object/provenance verification remain for the operator. '
    'This administrative integration supplies no additional judicial action or event date. '
    'No substantive blocker remains for the financial event; the underlying requests remain pending as stated above.'
)
updated = normalized.replace(pending[0], completed)
assert updated.split('## Public Projection\n', 1)[1] == public
record.write_bytes(updated.replace('\n', newline).encode('utf-8'))
print('Copied public opinion topology into both law projections; completed internal integration status only.')
