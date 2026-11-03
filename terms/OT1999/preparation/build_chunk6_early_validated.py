from pathlib import Path
import hashlib

base = Path('terms/OT1999')
freeze = base / 'freeze'

def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def paragraph(text, number, next_number):
    return text.split(f'\n{number}\n', 1)[1].split(f'\n{next_number}\n', 1)[0].strip()

law_path = base / 'entering-law/OT_1999CHUNK6_NCRL.md'
supp_path = base / 'preparation/chunk6-ncrl-neutral-supplement.md'
lower_path = base / 'sources/chunk6-neutral/ncrl-lower.txt'
positions_path = base / 'entering-law/OT_1999CHUNK6_NCRL_PUBLIC_POSITIONS.md'
lower = lower_path.read_text(encoding='utf-8-sig')
packet = '''# North Carolina Right to Life: freshly validated neutral packet

Stage: Engine 3A neutral validation. No vote, commitment, historical comparison, opinion assignment or Stone position is supplied. Source cutoff: immediately before May 1, 2000. The separate modeling context must make its own assessments.

## Event, channel and participation

North Carolina Right to Life, Inc. v. Bartlett, review of 168 F.3d 705 (4th Cir. 1999), is scheduled for post-grant merits decision on May 1, 2000. The supplied calendar places the grant on February 22 and argument/submission on April 3, 2000. These are authorized calendar premises, not recovered historical Supreme Court actions. The route is review of the federal appellate judgment; no separate Supreme Court docket number is supplied. The caption alone does not establish which party filed a historical petition. The two granted questions, rather than a guessed petitioner identity, delimit review.

The granted questions ask (1) whether a State may impose political-committee registration, reporting and disclosure on an issue organization whose major purpose is not nominating or electing candidates, and (2) whether regulated campaign expenditures may extend beyond express electoral advocacy without unconstitutional vagueness or overbreadth. The first question permits assessment of both organizational coverage and the actual burden; it does not presuppose a categorical major-purpose exemption. The second does not equate express advocacy with a mandatory list of words.

The supplied neutral materials identify no recusal or participation change. The sitting Court consists of Chief Justice Stone-Zsela and Justices Stevens, O'Connor, Scalia, Kennedy, Souter, Thomas, Ginsburg and Breyer; six qualified Justices are required for a quorum and a majority of those participating controls an appellate judgment. No reason for nonparticipation is inferred.

## Record and lower judgment

NCRL, its separate political action committee NCRLPAC, and Barbara Holt sought declaratory and injunctive relief. The Fourth Circuit describes NCRL as a nonprofit issue organization unassociated with a candidate, party or campaign committee, without a major purpose of electing candidates. NCRLPAC expressly supports candidates through contributions and independent expenditures. Holt supervises both entities and is a registered lobbyist. Their different functions cannot be collapsed into an assumed transaction by NCRL.

NCRL submitted two sample voter guides to the Elections Board. The first accidentally included NCRLPAC's endorsement sheet. The second omitted endorsements. The official told NCRL that distribution of the second guide would still violate the corporate political-purpose expenditure prohibition. NCRL refrained from distribution; NCRLPAC ceased soliciting without a disclaimer. These are the lower opinion's record recitations. The exact second guide is not reproduced, so neither its complete wording nor a finding satisfying Maine Right to Life's contextual standard may be invented.

The State argued that its construction limited coverage to electoral advocacy and that no credible prosecution threat existed. The Fourth Circuit found a live pre-enforcement controversy: the criminal statutes facially reached the activity, an official had applied the corporate prohibition to the endorsement-free guide, and the State supplied only its litigation position rather than a promulgated binding rule or an established prosecutorial undertaking. It rejected abstention; the opinion identifies neither a state supreme court certification procedure nor authority for a federal court to certify the construction to the Elections Board. That disposition and its supporting facts are available for independent threshold review, without treating a lower court's general presumption as newly controlling Supreme Court law.

The Fourth Circuit affirmed facial invalidation of the section 163-278.6(14) political-committee definition. It reasoned that the primary-or-incidental language and the separate influence-an-election limb swept issue organizations into comprehensive registration, recordkeeping and reporting backed by criminal penalties. It rejected a narrowing construction requiring removal of the incidental-purpose language or the separate election-influence limb. Its account of Buckley as mandating an organization-wide major purpose and listed electoral words must be assessed against the intervening simulated authorities appended below.

The lower court also affirmed invalidation of sections 163-269, 163-278.6(16) and 163-278.19's corporate contribution/expenditure prohibition. It concluded that NCRL fit MCFL on its actual nonprofit characteristics: no profit-making activity, shareholders or other economic claimants, and zero-to-eight-percent corporate receipts in 1993–1995 arising from individual telephone customers' decisions to direct refunds to the organization. Those are facts supporting the lower court's conclusion, not an independent Supreme Court finding that every nonprofit or every direct candidate gift is exempt.

The lower court reversed invalidation of section 163-278.13B's session-time lobbyist and employing-PAC contribution/solicitation restrictions. The donor-identification declaration under section 163-278.20(a) remained; on appeal the State contested controversy but did not contest the declaration's merits. These are separate lower-judgment components. The supplied grant does not reopen them automatically. An opinion must identify precisely which reviewed provision and relief answer the two questions; it may not issue an independent direct-contribution, session-ban or donor-disclaimer judgment without a supported review basis.

## Exact statutory recitations in the permitted lower opinion

The following are copied mechanically from paragraphs 19 and 26 of the judicial opinion. Paragraph 19 supplies the quoted committee definition and identifies associated duties. Paragraph 26 quotes the relevant political-purpose language, expressly as a quotation in relevant part. Neither is represented as a complete enrolled statute or an independently recovered full statutory compilation.

'''
packet += paragraph(lower,19,20) + '\n\n' + paragraph(lower,26,27)
packet += '''

## Supported competing paths and remedies

The issue organization may defend relief against coverage triggered merely by incidental electoral influence and full committee duties imposed on independent issue discussion. Its strongest obstacle is that Akins rejects a categorical organization-wide exemption for genuinely covered candidate financing, while Maine Right to Life permits tightly confined contextual express advocacy. A defensible path must separate protection of the supported activity from those categorical propositions.

The State may defend regulation of actual candidate financing and a determinate electoral boundary, invoking Buckley's narrowing approach, Akins's transaction-specific construction and Maine Right to Life's cumulative restrictions. Its strongest obstacle is the North Carolina text itself, the lack of an authoritative narrowing construction and the concrete official response to an endorsement-free guide. A proposed construction must be legally available under the state text; a litigation assurance cannot by itself rewrite the statute or cure a credible threat.

A narrower path may reject both an organization-wide immunity rule and a literal-magic-words rule while preserving relief against the actual issue-advocacy coverage. The independent model must decide whether a supported facial judgment, narrower application judgment or construction remand is warranted. A remand must identify the material undecided task; it does not automatically restore invalid burdens or require a new factual study. Genuine candidate-connected financing, distinct corporate direct gifts, sponsor disclosure and the ungranted session restrictions retain their own predicates.

No outcome follows from these alternatives. No registration order, donor list, penalty, damages, rewritten statute or generic entitlement to amendment is supplied. Preservation or remedial expansion beyond the questions and lower judgment requires an additional source. An unresolved factual issue requires remand only if it is material to the selected lawful path; a record gap does not compel a remand when a supported legal disposition avoids it.

## Entering law and chronology

The appended entering-law slice supplies the exact copied holdings and Standards and Tests entries. Akins governs actual candidate-financing coverage; Maine Right to Life governs its limited contextual statutory construction while reserving constitutional vagueness; Clifton protects mere candidate inquiry without immunizing actual coordinated campaign services; Day and Stengel distinguish nonprofit independent spending from direct candidate gifts; McIntyre preserves the distinction between individual leaflets and organizational campaign finance. Russell and Nixon/Shrink concern contribution limits and cannot substitute their specific fit judgments for this coverage inquiry. No later or uncoordinated May 1 event, including Christensen, enters the baseline.

## Source map and limits

- The approved neutral split's NCRL entry supplies the two questions and authorized calendar. Its generic assertions that no earlier same-term law exists and that there is no unresolved doctrinal component are replaced by the actual entering-law slice and issues stated here.
- The permitted published lower opinion, 168 F.3d 705, was read in full, including all three footnotes. The preparation supplement identifies the Public.Resource.Org reproduction and its OpenJurist cross-check. No original petition, merits brief, full statutory compilation or exact guide is represented as read here.
- The full current neutral projection is available only as a sanitized source; relevant chronology and Nixon/Shrink passages are reflected in the slice. Records, ledger, private material, current historical Supreme Court disposition and comparator were not opened.
- The additional public-position slice supplies the substantive Akins and Maine Right to Life separate writings. In Akins, Scalia and Thomas do not decide the statutory merits; their dissent concerns informational standing. Kennedy distinguishes actual candidate cash and conduits from the association's own expression. The Maine dissent permits ordinary context explaining explicit electoral words but rejects external events supplying an absent electoral command. These are published prior positions, not votes in this matter.
- Additional precision about the second guide is required only for a judgment that turns on its exact language. Its absence does not defeat the supported statutory-coverage inquiry.

Fresh neutral validation approves this framing and the supported facts at the defined scope. It supplies no modeling conclusion. Research limits remain distinct from litigant default, waiver or failure of proof.

## Mechanically copied entering-law slice

'''
packet += law_path.read_text(encoding='utf-8-sig')
packet += '\n\n## Mechanically copied additional published positions\n\n' + positions_path.read_text(encoding='utf-8-sig')
out = freeze / 'OT_1999CHUNK6_NCRL_NEUTRAL_VALIDATED.md'
if out.exists():
    raise SystemExit(f'Refusing to overwrite frozen packet: {out}')
out.write_text(packet, encoding='utf-8')
receipt = '''# NCRL fresh neutral validation receipt

Engine stage: 3A only. Result: framing and objective record validated for the two granted questions, subject to the specific source limits in the packet. No commitments generated. The next substantive stage must be a distinct independent modeling context.

The validator read the approved neutral NCRL section, the opening sanitized projection's relevant chronology/current law, the NCRL entering-law slice, the NCRL preparation supplement and the complete permitted lower opinion including footnotes. The validator did not read Stone supplements, comparators, commitments, reconciliations, raw Records, ledger, control-validation files or the current matter's historical Supreme Court outcome. No Git command or tool was used.

Corrections retained: separate NCRL/NCRLPAC identities and activities; actual facial committee invalidation; separate corporate, session-restriction and donor-identification components; nonbinding litigation assurances; distinction between lower reasoning and current simulated law; scope of grant; limited-context express advocacy; exact-guide limitation; no invented original filing or party designation.

The separate-writing source limitation identified during validation was resolved before freezing by the mechanically copied public Akins and Maine Right to Life entries. No proposed vote follows from those writings. The exact-guide and additional-review-scope limits remain as stated in the packet.

## Integrity receipts

'''
for path in [base/'runtime/OT_1999CHUNK6_NEUTRAL.md', base/'freeze/OT_1999CHUNK6_OPENING_NEUTRAL_PROJECTION.md', law_path, supp_path, lower_path, positions_path, out]:
    receipt += f'- `{path.as_posix()}` — SHA-256 `{digest(path)}`\n'
receipt_path = freeze / 'OT_1999CHUNK6_NCRL_NEUTRAL_VALIDATION.md'
if receipt_path.exists():
    raise SystemExit(f'Refusing to overwrite frozen receipt: {receipt_path}')
receipt_path.write_text(receipt, encoding='utf-8')
print(out.as_posix())
print(receipt_path.as_posix())
