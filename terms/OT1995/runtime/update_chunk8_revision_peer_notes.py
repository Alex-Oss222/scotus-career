"""Apply the operator's completed legal dependency review as internal notes only."""
from pathlib import Path
import hashlib
import json

TERM = Path(__file__).resolve().parents[1]
assert (TERM / 'records/Leavitt_v_Jane_L_summary_merits_1996-06-17.md').exists()
review = '../freeze/OT_1995CHUNK8_REVISION_DEPENDENCY_REVIEW.md'
changes = {
 'Rise_v_Oregon_merits_1996-06-14.md': (
  'The completed Myers, Jaffee, Koon/Powell and Vera updates were checked in the clean stages;',
  'The original clean stages checked Myers, Jaffee, Koon/Powell and the then-standing-only Vera action;',
  'JUNE14',
  "The revised June 13 Vera merits decision applies the existing territorial-design boundary and terminates only relief dependent on that sole failed claim. Egelhoff concerns an unjustified bar on rebuttal of a retained homicide element, preserving ordinary evidentiary rules and actual state-law definitions. Neither decision supplies a DNA-search exception, biological privilege, hearing entitlement, personal-causation predicate or finding on Oregon statutory coverage. Their published separate grounds likewise change no material premise of this decision. This supplementary entering-law review adds no decisional ground or change to any result, opinion join or remedy."),
 'Melendez_v_United_States_merits_1996-06-17.md': (
  'The clean stages completed the earlier-law refresh through Rise.',
  'The original clean stages completed the then-existing earlier-law refresh through Rise.',
  'JUNE17',
  "The current common baseline additionally contains the revised Vera merits decision and Egelhoff's completed retained-element decision. Vera neither changes the separate statutory-motion requirement nor resolves an independent preserved plea theory. Egelhoff concerns state-defined homicide elements and their rebuttal, not authority to sentence below a federal statutory floor or the meaning of the actual assistance motion. Its majority and separate interpretive grounds do not alter the frozen statutory/Guidelines positions here. Leavitt is a June 17 peer and supplies no entering law. No result, decisional ground, opinion join or remedy changes."),
 'Calderon_v_Moore_summary_review_1996-06-17.md': (
  'The clean chronology gate includes the complete Rise decision.',
  'The original clean chronology gate included the complete Rise decision and the then-existing June 13 actions.',
  'JUNE17',
  "The revised Vera merits disposition and Egelhoff's completed decision are now included as earlier law. Vera's distinction between a failed substantive theory and jurisdiction, and its termination of wholly dependent relief, create no conflict with the existing effectual-appellate-relief inquiry. Egelhoff decides neither habeas mootness nor the Rule 39 appointed-counsel exception. Their published separate grounds change no relevant premise. Leavitt is excluded as a June 17 peer. This review supplies no new self-representation, compliance or habeas-merits ground and changes no result, join or remedy."),
 'Gray_v_Netherland_merits_1996-06-20.md': (
  'Egelhoff supplies no adjudication; Wood remains a grant.',
  'Egelhoff supplies its June 13 retained-element adjudication; Wood remains a grant.',
  'JUNE20',
  "The revised Vera merits rule concerns territorial design and wholly dependent relief, not the capital-sentencing opportunity claim. Egelhoff protects rebuttal of a retained homicide element while preserving legitimate evidence rules; it establishes no discovery deadline, automatic structural error or new finding concerning this sentencing record. Its 1996 holding does not itself supply law dictated at Gray's 1987 finality, and its separate writings do not alter the recorded Gardner/Weatherford comparison. Leavitt's June 17 summary severability disposition preserves independently supported constitutional protection while confining relief to established grounds; it neither decides this claim's presentation nor changes the sentencing-only writ, independent Brady dismissal, statutory gates or existing effect finding. No new authority is substituted for Gray's stated grounds, and no result, opinion join or remedy changes."),
}
receipt = []
for name, (old, new, group, note) in changes.items():
    path = TERM / 'records' / name
    before_bytes = path.read_bytes()
    newline = '\r\n' if b'\r\n' in before_bytes else '\n'
    before = before_bytes.decode('utf-8').replace('\r\n', '\n')
    assert before.count(old) == 1, name
    after = before.replace(old, new)
    old_baseline = f'OT_1995CHUNK8_PRE_{group}_NEUTRAL_PROJECTION.md'
    new_baseline = f'OT_1995CHUNK8_REVISION_PRE_{group}_NEUTRAL_PROJECTION.md'
    after = after.replace(old_baseline, new_baseline)
    if name.startswith('Gray_'):
        after = after.replace('and [June17 review receipt](../freeze/OT_1995CHUNK8_GRAY_JUNE17_PUBLIC_REVIEW.md) establish the preceding-law boundary.',
            'establishes the current preceding-law boundary. The [original June17 review receipt](../freeze/OT_1995CHUNK8_GRAY_JUNE17_PUBLIC_REVIEW.md) remains a record of the earlier Run\'s source review, supplemented below.')
    insertion = f'\n\n**Revised entering-law review:** {note} See the [completed dependency review]({review}).\n'
    if name.startswith('Gray_'):
        anchor = '\n- Gardner and Weatherford'
    else:
        anchor = '\n## Participation'
    assert anchor in after, name
    after = after.replace(anchor, insertion + anchor, 1)
    assert before.split('## Public Projection', 1)[1] == after.split('## Public Projection', 1)[1]
    after_bytes = after.replace('\n', newline).encode('utf-8')
    assert before_bytes.split(b'## Public Projection', 1)[1] == after_bytes.split(b'## Public Projection', 1)[1]
    path.write_bytes(after_bytes)
    receipt.append({'record': name, 'before_sha256': hashlib.sha256(before_bytes).hexdigest(), 'after_sha256': hashlib.sha256(after_bytes).hexdigest(), 'public_projection': 'byte-identical'})
(TERM / 'freeze/OT_1995CHUNK8_REVISION_PEER_NOTE_RECEIPT.json').write_text(json.dumps(receipt, indent=2)+'\n', encoding='utf-8')
print(json.dumps(receipt, indent=2))
