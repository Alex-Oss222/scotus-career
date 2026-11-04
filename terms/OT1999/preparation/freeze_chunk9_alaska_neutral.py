from pathlib import Path
import hashlib
import re
import pymupdf

term = Path(__file__).resolve().parents[1]
pdf = term/'sources'/'chunk9'/'alaska'/'joint-motion-2000-06-07.pdf'
d = pymupdf.open(pdf)
pieces = [d[i].get_text() for i in range(17,23)]
pieces[0] = pieces[0][pieces[0].index('A. Alaska’s Motion'):]
terms = '\n'.join(pieces)
# Small OCR corrections verified against images of the actual predecision filing.
for old,new in [('Section 8&(g)','Section 8(g)'), ('48 U.S.C. \n§ 1387(g)', '43 U.S.C. \n§ 1337(g)'), ('§ 1318','§ 1313'), ('Huxisting','Existing'), ('Haisting','Existing'), ('\nce. \n','\nc. \n')]:
    terms = terms.replace(old,new)
assert '§ 1337(g)' in terms and '§ 1313' in terms
proposed = term/'preparation'/'OT_1999CHUNK9_ALASKA_PROPOSED_TERMS_FROM_FILING.md'
source = '''# Alaska — proposed terms copied from the actual predecision joint motion

Source: the June 7, 2000 joint motion, official Supreme Court Library PDF, printed pages 2a–7a (PDF pages 18–23). These are the parties' requested A–G terms, not a Court action. The text is copied from the saved PDF. Isolated OCR corrections to the 43 U.S.C. §§1337(g)/1313 citations, the Section 8(g) reference, the word Existing and the subsection c label were checked against source-page images. Other line wraps and page typography remain. The actual source PDF controls any residual OCR discrepancy.

'''+terms+'\n\n## Exhibit A\n\nThe complete proposed Exhibit A is the original PDF, printed pages 8a onward. Its NAD 83/WGS 84 coordinates are authoritative; NAD 27 conversions are convenience values. The schedule is preserved verbatim as part of the original source, not reconstructed or independently surveyed here. No coordinate is changed by this handoff.\n'
if proposed.exists():
    raise RuntimeError('Refusing to replace proposed-source copy')
proposed.write_text(source,encoding='utf-8',newline='\n')
paths = [term/'preparation'/'OT_1999CHUNK9_ALASKA_CONTROL_FACTS.md', term/'preparation'/'OT_1999CHUNK9_ALASKA_STATUTORY_SOURCE.md', term/'entering-law'/'OT_1999CHUNK9_ALASKA.md', term/'preparation'/'OT_1999CHUNK9_ALASKA_PENDING_FILING_NEUTRAL.md', proposed]
texts = [p.read_text(encoding='utf-8-sig').rstrip() for p in paths]
texts[0] = texts[0].replace('OT_1999CHUNK9_ALASKA_OPERATIVE_SOURCE.md','OT_1999CHUNK9_ALASKA_PROPOSED_TERMS_FROM_FILING.md')
intro = '''# Frozen neutral packet — United States v. Alaska, implementing decree

Fresh neutral validation completed November 3, 2026. No vote, assignment, Stone position or present Court action is supplied. The June 7 joint filing is now admitted as a party act through the copied sanitized filing update. It changes the stage from awaiting a proposal to having one available; it does not itself fix a boundary, issue an injunction, trigger payment or grant leave to plead.

## Event and independent completeness assessment

No. 84, Original; scheduled consideration June 29, 2000. This is original-jurisdiction implementation of the actual June 19, 1997 decision. It is not appellate review of a judgment below. No new argument or case-specific nonparticipation is established. The seated Court consists of Chief Justice Stone-Zsela and Justices Stevens, O'Connor, Scalia, Kennedy, Souter, Thomas, Ginsburg and Breyer. Independent modeling concerns the eight Associates, with their prior positions supplying context rather than a present vote.

The joint motion, full memorandum and proposed A–G provisions have been checked against the actual predecision filing. The requested terms conform in legal structure to the prior baseline, Dinkum, Petroleum Reserve and Refuge holdings. The State does not recover a Dinkum-generated belt. The memorandum expressly identifies the jointly agreed westward extension to Point Hope, unexcepted Harrison Bay/Arco matters and uncontroverted baseline principles; those representations support the proposed intersovereign settlement without creating new adjudicated historic-title findings.

The offshore state/federal line would be fixed under section 1301(b); the reserve/refuge coastal boundaries would remain ambulatory. Those are different boundaries. The Petroleum Reserve uses highest highwater and the named lagoon/barrier descriptions; the Refuge uses extreme low water and its described bars, reefs, islands and lagoon closures. The descriptive 1960 order does not replace the controlling 1957 legally operative segregation or import the 1980 enlargement. No absent survey or new title finding is inferred.

The proposed seaward federal right preserves section 1337(g) and Paragraph C; the shoreward state right preserves the reservations, section 1313 and Paragraph C. Reciprocal noninterference relief is subject to those actual qualifications. Statutory revenue sharing is not unqualified state title or a uniform award over all revenues. The exact statutory terms, including the Alaska partial-tract and disputed-escrow provisions, are copied below.

The three lease categories must remain separate: section 7 agreements control their leases and escrow; nonagreement leases intersected by the fixed line stay with their original lessor for administration and past/future lease revenue until expiration, relinquishment or termination; and agreement leases also intersected by the line retain agreement administration and distribution. Paragraph B controls subsequent area rights after those terminating events. Pre-entry expired leases' distributions are preserved at each applicable category. The 180-day escrow deadline runs only from a decree actually entered. Third-party and lessee rights, and present/future unitization, operating, enhanced-recovery, commingling and similar agreements, remain preserved by C(2).

Leave to file the counterclaim formally completes the existing pleading posture; no merits reopening follows. Retained jurisdiction permits implementation and supplementation, and the proposed decree is otherwise final. Neither agreement nor the absence of a presently filed objection substitutes for conformity review. Entry of the conforming joint proposal and withholding or requiring correction of a genuinely nonconforming provision are lawful paths; no new hostile contention or current accounting dispute is invented.

## Readiness and source limits

Ready for independent modeling of the proposed implementing decree. The only supported additional event is the admitted June 7 filing; no reconstructed response, waiver, submission deadline or default is used. Research cutoff is June 29, 2000. All June 28 matters are uncoordinated and their unrelated substantive decisions supply no assumed title change here; any actual intervening relevant change would require freshness review.

The complete coordinate appendix remains part of the exact original filed proposal. This validator has read the substantive joint motion, memorandum and A–G terms and checked relevant source-page images, but has not independently recomputed or certified every coordinate or performed a survey. No coordinate discrepancy is asserted or used. If a decision depends on changing a particular coordinate, the actual schedule, datum and survey basis must be examined before that change; current entry analysis preserves the submitted schedule without alteration.

The earlier authorized operative handoff contained later-reporter page headers. The frozen packet instead supplies a direct predecision-file extraction, with isolated image-verified OCR repairs. No later decree, historical target disposition, lineup or reasoning is opened or adopted as a Court action.

'''
packet = intro
for label,text in zip(['Validated objective facts','Exact statutory source text','Exact entering law','Exact admitted filing update','Proposed operative terms from the actual filing'],texts):
    packet += f'## {label}\n\n{text}\n\n'
out = term/'freeze'/'OT_1999CHUNK9_ALASKA_NEUTRAL.md'
receipt = term/'freeze'/'OT_1999CHUNK9_ALASKA_NEUTRAL_VALIDATION.md'
if out.exists() or receipt.exists():
    raise RuntimeError('Refusing to replace existing freeze')
out.write_text(packet,encoding='utf-8',newline='\n')
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
body='''# Alaska — fresh neutral validation receipt

Status: READY after receipt of the sanitized June 7 admitted-filing update. No vote or opinion assignment produced.

Allowed sources read: AGENTS.md and governing neutral Engine sections; Alaska Section I in the current runtime neutral; the control-facts, operative-source, statutory-source and focused law handoffs; the sanitized pending-filing update; the actual authorized predecision joint-motion PDF. Current neutral-projection institutional/chronology facts were previously consulted. No raw Record, commitment, comparator, current Stone supplement or target historical decree file was opened.

The initial authorized operative source had reporter page headers; its substantive material was framed as proposed terms. For downstream source clarity, the validator did not propagate that transcription. It directly extracted the actual June 7 filing's A–G proposal, read the full substantive motion/memorandum/operative text, and checked images of PDF pages 18, 19, 21 and 22 to resolve isolated OCR errors. It claims no independent numerical survey or line-by-line certification of the long Exhibit A schedule. The original PDF is retained intact and hashed; no coordinate was changed.

Conformity checks preserve: settled baseline/Dinkum holdings; separate clear-inclusion/title-defeat premises; 1957 segregation instead of retroactive 1960 effect; the agreed Point Hope extension's source status; fixed offshore versus ambulatory reservation boundaries; reciprocal injunction qualifications; exact statutory reservations; all three lease categories and their transition rules; preserved pre-entry distributions; third-party/agreement rights; the entry-triggered 180-day deadline; formal counterclaim leave; and retained jurisdiction without merits reopening.

Exact gaps: no independently recomputed coordinate schedule, parcel-specific section 1313 application, quantified section 1337(g) award, accounting dispute, lessee-rights adjudication or future coastal-boundary dispute is established. None is necessary for consideration of the submitted proposal at its supported scope. A proposed change relying on one of those propositions requires its specific source and fresh affected analysis. The joint filing is not approval and absence of an objection is not default. The sanitized admission establishes proposal availability only and reports no effect on other completed matters.

Source-copy fidelity: the control facts differ only in their local link to the direct filing extract; statutory, law and admitted-filing text are copied exactly. The isolated proposed-source OCR repairs are listed in that extract and grounded in source images.

Snapshot integrity:

'''
for p in paths+[pdf,out]:
    body+=f'- `{p.relative_to(term).as_posix()}`: SHA-256 `{sha(p)}`.\n'
receipt.write_text(body,encoding='utf-8',newline='\n')
assert all(t in out.read_text(encoding='utf-8') for t in texts)
print('Alaska direct proposal extract, neutral freeze and validation receipt created; exact copied sections verified.')
