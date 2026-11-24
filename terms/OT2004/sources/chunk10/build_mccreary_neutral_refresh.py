from pathlib import Path
import hashlib
import re

root = Path(__file__).resolve().parents[4]
term = root / 'terms/OT2004'
source_path = term / 'sources/chunk10/control/MCCREARY_NEUTRAL_QUALIFICATION_REQUEST.md'
source = source_path.read_text(encoding='utf-8-sig')
recitations = re.findall(r'```text\n(.*?)\n```', source, flags=re.S)
assert len(recitations) == 2

body = '''# OT2004 chunk 10 — McCreary neutral refresh

## Scope and status

This additive handoff qualifies matter 103, McCreary County v. American Civil Liberties Union of Kentucky, No. 03-1693, for the June 27, 2005 event. The original neutral packet and frozen baseline remain unchanged. Read their descriptions of the county resolutions and identifying labels subject to the chronology below. Research cutoff: June 27, 2005. No present Justice commitment, disposition, or finding of current governmental function is supplied.

The validator read the exact authorized objective-source request, the original neutral packet for matter 103, and the relevant Agostini and Marshfield holdings and operative Standards in the C entering-law slice. The source request supplies two bounded published recitations under Engine §14(2). The underlying same-case Supreme Court opinion was not opened. No comparator, current commitments, current private position, reconciliation, or raw decision record was consulted. The two recitations below are mechanically copied from the authorized request, which reports that its own extraction normalized whitespace.

## Validated chronology and packet qualifications

| Proposition | Validated scope | Qualification needed |
|---|---|---|
| The earlier county resolutions were not repealed. | This describes the installation of the third display and the lower courts' review. | Do not carry this historical description forward as a statement that the resolutions remain in force at the June 27, 2005 event. The source reports that both county boards repealed them after Supreme Court argument. No exact repeal date is supplied. |
| The record includes continuing county resolutions. | The resolutions were operative during the display sequence and lower review described in the original packet. | The companion-case comparison must distinguish their earlier operative status from the later repeal. Their existence and content remain part of the documented sequence, but their present legal force cannot be assumed unchanged. |
| Plaintiffs argue that the counties retain the same official religious commitments. | This is the plaintiffs' position about the governmental presentation, not an independently established current fact. | The argument may rely on continuing display conduct and historical evidence, but cannot rest on the factual assertion that the repealed resolutions remain unrepealed. Whether the current presentation continues the asserted commitment is unresolved. |
| The Commandments carried a translation label and scriptural citation. | Before the modified district-court injunction, the counties removed the identifying translation label and the citation to Exodus. | The current challenged presentation must not be described as still carrying those removed identifiers solely because they appeared earlier. Removal of identifying labels does not remove the actual Commandments text. No further alteration of that text or the other exhibit materials is supplied. |

The later repeal does not change the reported fact that the resolutions were unrepealed when the lower courts evaluated the third display. The identifying-label removal preceded the modified injunction and therefore is not a newly reported postargument alteration. The two acts belong at their distinct points in the chronology. Neither establishes another display version, an additional county resolution, or an unreported change in the exhibit's operation.

## Governing law and strongest supported effects

Agostini, effective June 23, 1997, retains Lemon as one inquiry into the governmental act and its actual function. Purpose, effect, and institutional relationships are evidence within that inquiry. An independent purpose prong does not govern. Government may explain history but may not adopt religious doctrine as governmental truth or use public authority to solicit adherence. A religious motivation does not by itself make genuinely secular work devotional, and a secular description does not excuse prohibited conduct. The pertinent general component of the **Lemon test** Standards entry retains Agostini's effective date; the entry's later financed-function and civil-certification components supply no automatic answer to this display dispute.

Marshfield, effective February 27, 2001, supplies the operative **Municipal divestiture and continuing presentation of a religious display** rule. A genuine formal change can have real legal effects without ending a continuing governmental presentation; the inquiry asks what public conduct actually continues and whether a lawful correction effectively ends it. That decision's public-park, private-ownership, and operational-separation facts are not facts of this case. It creates no universal requirement of repeal, disclaimer, removal, or any other single corrective act.

**Counties' strongest supported position.** The later repeal is a genuine governmental act that removes the resolutions' ongoing formal force and must receive its actual legal significance. Together with the earlier removal of identifying labels and the existing historical arrangement and explanations, it may support the argument that the counties have changed what they publicly present. The unified rule does not permanently disqualify them from lawful historical instruction because of their earlier conduct. If an injunction continues to depend on the resolutions' unrepealed status or on labels absent from the reviewed exhibit, its factual premise and prospective scope require correction. Whether that warrants dissolution, modification, further findings, or no change depends on the actual current function and the procedural posture; repeal alone does not establish the answer.

**Plaintiffs' strongest supported position.** Formal repeal and removal of identifying labels need not end an official religious presentation that the display's actual content, arrangement, explanations, and documented development continue to establish. The repeal does not erase the earlier official acts or retroactively change the record on which preliminary relief was entered. Removal of the translation label and Exodus citation leaves the Commandments' actual text available for contextual evaluation. Plaintiffs may argue that effective interim relief remains necessary if the current governmental function continues. That argument must identify such a continuing function under Agostini; it cannot treat past purpose as an irrebuttable taint, deny repeal any possible significance, or infer illegality from sacred text alone.

**Current review and prospective relief.** Separate the correctness of preliminary relief on the lower-review record from what relief may now remain appropriate after the later repeal. A supported continuing prohibited function may justify effective, confined interim relief; a genuine changed function may support modification or dissolution; a material unresolved present fact may require an appropriately bounded further inquiry. These are analytical paths, not a selected disposition. No path authorizes a permanent prohibition of every future historical exhibit containing the Commandments. The actual injunction must remain tied to the identified governmental conduct and the preliminary posture.

## Remaining limits and readiness

No reconstruction premise is adopted. The exact repeal date and repeal instruments are not supplied here. There is no additional exhibit alteration, replacement resolution, finding about public understanding, or evidence of subsequent operation beyond the two bounded recitations. The source does not report whether or how the later act was presented to the reviewing court, any ruling accepting extra-record material or taking judicial notice, a preserved request based on the repeal, or a finding about its practical effect. These absences in the validation materials do not establish that a filing or event was absent from the actual proceeding.

The recitations supply no ruling on cure, mootness, current function, or the final scope of relief. A mootness or judicial-notice issue cannot be treated as already resolved by this source. If a proposed disposition depends on the exact repeal instrument, timing, procedural treatment, present operation, or full injunction wording, obtain that particular material or preserve the material issue for proper further proceedings rather than supply it by inference. The original preliminary-relief posture and its limits remain in place for modeling.

The additive handoff is ready for independent modeling with both temporal qualifications incorporated before affected commitments are frozen. It permits assessment of the later repeal's possible legal significance while preserving the absence of a supplied present-function outcome.

## Mechanically copied source recitations

These are the entire two bounded recitations in the authorized objective-source request. They are record and procedural facts, not a supplied reviewing-court appraisal.
'''

for title, citation, quote in (
    ('Later repeal', 'Authorized objective-source extraction, note 19 fragment; exact repeal date not supplied.', recitations[0]),
    ('Identifying-label and citation removal', 'Authorized objective-source extraction, note 6; 145 F. Supp. 2d 845, 847 (E.D. Ky. 2001).', recitations[1]),
):
    body += f'\n### {title}\n\n{citation}\n\n```text\n{quote}\n```\n'

output = term / 'freeze/OT_2004CHUNK10_MCCREARY_NEUTRAL_REFRESH.md'
output.write_text(body, encoding='utf-8', newline='\n')

receipt = '''# OT2004 chunk 10 — McCreary neutral refresh receipt

- **Event and cutoff:** Matter 103, McCreary, No. 03-1693; June 27, 2005; preliminary-injunction review.
- **Gap and supported facts:** The original packet's unrepealed-resolutions description belongs to installation and lower review. Both boards later repealed the resolutions after argument. Identifying translation labels and the Exodus citation had already been removed before the modified injunction. Two bounded recitations were supplied under Engine §14(2), with no source appraisal.
- **Inputs and boundary:** Exact authorized objective-source request; original neutral matter 103; relevant Agostini and Marshfield entering-law holdings and Standards. No underlying same-case opinion, comparator, current commitments, private position, reconciliation, or raw decision record opened. No commitments produced.
- **Premises:** No new factual or procedural reconstruction. No exact repeal date, further text change, additional resolution, cure, mootness, present-function finding, or selected remedy supplied.
- **Legal effect preserved:** Both genuine change and continuing governmental presentation remain possible under the unified current-function rule. Earlier review and present prospective relief must be distinguished. Neither permanent taint nor automatic cure is presumed.
- **Remaining limits:** Exact repeal instruments and date, procedural treatment of the later act, additional current operation, and the full injunction wording are not certified. A path requiring those facts needs the particular source or appropriate further proceedings; source absence is not litigant default.
- **Readiness:** Ready for independent modeling before affected commitments are frozen. Existing packets remain unchanged. The two quotations were copied by script and verified against the authorized request.
'''
for path in (source_path, term / 'entering-law/OT_2004CHUNK10_C.md', output):
    receipt += f'\n- **SHA-256 {path.relative_to(term).as_posix()}:** `{hashlib.sha256(path.read_bytes()).hexdigest()}`\n'
receipt_path = term / 'freeze/OT_2004CHUNK10_MCCREARY_NEUTRAL_REFRESH_RECEIPT.md'
receipt_path.write_text(receipt, encoding='utf-8', newline='\n')

for quote in recitations:
    assert quote in source and quote in body
for path in (output, receipt_path):
    text = path.read_text(encoding='utf-8')
    assert not any(''.join(map(chr, codes)) in text for codes in ((79, 110, 101, 68, 114, 105, 118, 101), (71, 105, 116, 72, 117, 98)))
    print(f'{path.relative_to(root).as_posix()}: {len(text)} characters')
print('Validated two mechanically copied objective recitations.')
