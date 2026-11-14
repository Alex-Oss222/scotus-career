from pathlib import Path
import json

base = Path('terms/OT2002')
out = base/'runtime/chunk13-drafts'
out.mkdir(exist_ok=True)
reconciled = (base/'freeze/OT_2002CHUNK13_B_RECONCILED.md').read_text(encoding='utf-8')
kernel = reconciled.split('# OT2002 chunk 13 B — independent non-Stone commitments',1)[1]
all9 = "Stone-Zsela, Stevens, O'Connor, Scalia, Kennedy, Souter, Thomas, Ginsburg and Breyer"
assoc = "Stevens, O'Connor, Scalia, Kennedy, Souter, Thomas, Ginsburg and Breyer"
specs = []

def saved_annex(number, next_number):
    s = kernel.index(f'## {number}.')
    e = kernel.index(f'## {next_number}.',s) if next_number else kernel.index('## Handoff readiness',s)
    return ('## Frozen Associate commitments and reconciliation audit\n\n'
            'The following issue-specific commitment kernel is copied exactly from the frozen reconciled handoff. Stage labels refer to the preserved independent handoff, not to a second deliberation. The reconciler confirmed every stated disposition, sufficient ground, alternative and join without change. Assembly preserves them.\n\n'
            +kernel[s:e].strip()+'\n\n'
            'No historical Supreme Court merits judgment or lineup exists for this added review. The lower appellate decision supplies record and comparison evidence, not individual Supreme Court votes. There is no same-matter Justice-specific historical departure. The specific prior public writings identified in each row support the present commitments. No circulation, changed vote or new concession is invented.\n\n')

def projection(blocks):
    keys=['Event','Participation','Public Action','Judgment & Remedy','Opinion Topology','Holdings','Precedent Treatment','Law After Decision','Separate Writings','Procedure After Action','Source Notes']
    return '## Public Projection\n\n'+'\n\n'.join('### '+k+'\n\n'+blocks.get(k,'') for k in keys)+'\n'

def publish(name, internal, blocks, spec):
    (out/name).write_text(internal+projection(blocks),encoding='utf-8')
    specs.append(dict(file=name,**spec))

bech_h = '''#### B1. Effective relief must remain available throughout review

**Holding and operative rule:** Review of an antecedent ruling is moot when an independently effective later judgment eliminates every remedial consequence available within the specified review. The December 6, 2002 judgment for the DEA rests on a separate statutory element and remains effective; deciding the earlier record-definition question cannot change the parties' operative rights in this proceeding.

**Authority:** The per curiam opinion, joined by all nine Justices identified in Opinion Topology, supplies a unanimous jurisdictional holding.

**Controlling explanation:** Arizonans for Official English requires an actual controversy throughout review, including relief the Court can lawfully provide. The April 2000 judgment returned this case for discovery. Discovery occurred, and the courts then entered and affirmed judgment for the DEA on the independent system-of-records requirement. The present review concerns only the antecedent record-definition ruling. The DEA already possesses the final judgment it sought, and Bechhoefer cannot overcome that independent judgment through a decision on another element. A disagreement with adverse reasoning, detached from an obtainable remedy, does not preserve this controversy. Garvey permits review of a necessary antecedent ruling through review of the later judgment; that route and dependence are absent here. The Court therefore dismisses this review as moot. The Privacy Act definition is not reached because constitutional jurisdiction has ended.

#### B2. The lower judgments remain in force

**Holding and operative rule:** Mootness does not automatically require vacatur of an antecedent judgment. Where an interlocutory remand has served its function and the petitioner has obtained an independent final judgment, with no surviving adverse command or other demonstrated equity requiring judgment clearing, dismissal leaves both judgments undisturbed.

**Authority:** The same unanimous per curiam opinion.

**Controlling explanation:** Arizonans treats vacatur as an equitable judicial act. The agency was not left subject to an adverse operative judgment that became unreviewable: the remand led to discovery and a final judgment in its favor. The earlier remand has completed its work. A preference to remove the earlier court's statutory reasoning is insufficient to erase that judgment. Leaving both judgments in place gives the later, independently sufficient judgment its existing effect and terminates only the review now before this Court.'''

bech_blocks={
'Event':'''Bechhoefer v. United States Department of Justice, DEA. October Term 2002. Dismissal for mootness, June 16, 2003. Review concerns the Second Circuit's April 3, 2000 judgment, 209 F.3d 57, vacating a Privacy Act summary judgment and remanding. The question presented is whether the author's personal information in a letter principally concerning others qualifies as a record under 5 U.S.C. §552a(a)(4). The agency seeks dismissal on that ground; Bechhoefer seeks continued adjudication of his disclosure claim. After the first remand and discovery, the Second Circuit affirmed an independent judgment for the agency on December 6, 2002, 312 F.3d 563. The operative effect of that later judgment controls the present threshold disposition. Decided on the merits submissions; no separate oral-argument date is stated.''',
'Participation':f'All nine Justices participated in submission and decision: {all9}.',
'Public Action':'The Court dismisses the review as moot, unanimously, and leaves both lower appellate judgments undisturbed.',
'Judgment & Remedy':f'''**Dismissed as moot, 9–0.**

**Supporting:** {all9}.

The April 3, 2000 and December 6, 2002 judgments remain undisturbed. The independent final judgment for the DEA continues in force.''',
'Opinion Topology':f'''Per curiam.

| Writing | Author | Joined by | Relationship to judgment | Scope joined |
|---|---|---|---|---|
| Opinion of the Court | Per curiam | {all9} | Dismissal for mootness | B1–B2, including the jurisdictional nonreach of the Privacy Act definition |''',
'Holdings':bech_h,
'Precedent Treatment':'''Arizonans for Official English is applied to continuing redressability and equitable vacatur; its requirement to clear judgments improperly entered after mootness does not make every earlier interlocutory ruling subject to erasure. Major League Baseball Players Association v. Garvey is distinguished because its antecedent-review rule operates through review of a later judgment and a ruling necessary to that judgment; it does not displace this independent final judgment.''',
'Law After Decision':'The continuing-controversy requirement governs review of an antecedent ruling even when the legal question remains disputed. The disposition preserves the existing lower judgments and ends this Court proceeding on jurisdictional grounds.',
'Procedure After Action':'This proceeding is concluded. The mandate dismisses the review as moot and leaves the independent judgment for the DEA effective.',
'Source Notes':'Bechhoefer v. United States Department of Justice, DEA, 209 F.3d 57 (2d Cir. 2000), and 312 F.3d 563 (2d Cir. 2002); 5 U.S.C. §552a(a)(4), (a)(5), and (b). The latter judgment followed discovery and rested on the system-of-records element.'}
bech_internal=f'''**Case and dockets:** Bechhoefer v. United States Department of Justice, DEA; 209 F.3d 57; lower dockets 96-6229 and 01-6244.
**Event and date:** Jurisdictional dismissal, 2003-06-16; October Term 2002, chunk 13, inventory 157.
**Result:** Unanimous dismissal of the specified review as moot; both lower judgments remain effective.
**Version / lineage:** Original decision for this event; no prior adjudication superseded.

## Event, route and chronology

The authorized additional-review schedule fixes June 16, 2003 as this event date. The approved packet supplies merits submissions but no distinct Supreme Court argument date; no argument event is invented. The reviewed judgment is the Second Circuit's April 3, 2000 remand on the Privacy Act record-definition question. The December 6, 2002 continuation after discovery affirmed an independent final agency judgment on the system-of-records element. The inventory's proper-arrival premise does not freeze those intervening proceedings. No stay, vacatur, amended grant or cross-review is presumed.

The agency requested restoration of dismissal and the claimant requested further adjudication of the disclosure claim. The later independent agency victory removes effective relief within the specified review. The final event closes this matter in the manifest; neither renewed discovery nor an additional pending threshold inquiry remains.

## Participation, entering law and decision form

Submission and decision participants: {all9}. Nine participate; quorum is six and an action requires five votes. The channel is the authorized review of the specified federal appellate judgment, subject to continuing Article III jurisdiction. The controlling baseline is the frozen B neutral packet and focused B_157 entering-law slice, including Arizonans, Garvey, and MacArthur's distinct action and remedy limits. No same-day decision supplies entering law.

**Form fixed before assignment:** A per curiam jurisdictional dismissal applies the settled continuing-controversy and equitable-vacatur rules to the established later judgment. Its function is to terminate an ineffective review, not decide the statutory merits after plenary consideration. The form follows that narrow procedural work. It is uncounted under Engine §8 and receives no signed lead assignment.

## Stone fixed-core and branch comparison

Stone's approved Section II requires determination of redressability on the two supplied opinions before statutory merits. It expressly directs termination if the later independent judgment leaves no effective relief and requires any vacatur to have an actual procedural basis. That condition is met: the system-of-records judgment remains operative and cannot be displaced within the definition grant. Stone joins the dismissal, the limited B1 grounds, and the B2 nonvacatur disposition. The conditional mixed-subject definition branch does not activate. His desired protection of personal information supplies no present merits vote. No standing fallback, substantive narrowing, changed burden, new remedy, or clerical correction is used. The frozen Associates reach exactly the same procedural ground, so no separate Stone writing performs additional legal work.

## Judgment, opinion and controlling law

All nine join the per curiam B1–B2 opinion. The actual disposition and complete controlling kernel are reproduced verbatim in the Public Projection's Judgment & Remedy and Holdings blocks below. There is no fragmented rationale or Marks inference. The Privacy Act merits are outside the Court's remaining constitutional jurisdiction. The mootness rule is applied without changing the existing jurisdictional or vacatur doctrines.

## Continuity

Both appellate judgments remain effective, and this Court review is terminal. There is no new Privacy Act construction or published noncontrolling position. No roster, allotment or standing-practice change occurs. No external event after the June 16, 2003 cutoff is admitted.

## Sources and validation

The frozen B neutral and reconciled packets identify the full 209 F.3d 57 and 312 F.3d 563 opinions. Saved sources: runtime/sources-B/Bechhoefer-2000.txt and Bechhoefer-2002.txt; applicable law: entering-law/OT_2002CHUNK13_B_157.md. The published opinions establish the original disclosure, completed discovery, independent judgment and unappealed retaliation claim. Their facts are historical source evidence; the present Article III disposition is this Court's legal application. No research omission is treated as party default. Research cutoff: 2003-06-16. No new reconstruction is used beyond the authorized additional-review event schedule.

Assembly checked the nine votes, common threshold and nonvacatur grounds, Stone's express branch, finality, and the distinction between actual record facts and procedural assumptions. Both lower judgments and their operative status reconcile to the mandate. The five named public blocks retain only the jurisdictional limit and surviving judgments; they contain no catalogue of unawarded relief or neighboring merits. Author assignment is inapplicable. Publication validation: __PUBLICATION_STATUS__.

'''+saved_annex(157,160)
publish('Bechhoefer_v_United_States_Department_of_Justice_DEA_dismissal_2003-06-16.md',bech_internal,bech_blocks,dict(case='Bechhoefer v. United States Department of Justice, DEA',date='2003-06-16',countable=False))

heim_h='''**Common authority:** The signed opinion of __LEAD_AUTHOR__ is joined by __LEAD_JOINERS__ throughout H1–H3. Those eight Associates supply direct majority authority for H1 and H2; Stone-Zsela additionally joins H3, making that independent statutory and certification holding unanimous. His distinct temporal ground appears in his separate concurrence. Each H1–H3 explanation below states only its supporting coalition's reasoning.

#### H1. This official interpretation exercises the statutory assignment

**Holding and operative rule:** HUD's 2001 national policy statement, issued through the Secretary's official-publication mechanism under 12 U.S.C. §2617(a) and 24 C.F.R. §3500.4(a)(1)(ii), is a permissible exercise of delegated interpretive authority entitled to controlling weight within the statute's bounds. Its adopted yield-spread-premium inquiry examines actual compensable goods, facilities or services and whether total direct and indirect compensation bears a reasonable relationship to their value, while preserving §2607(a)'s prohibition on purchased referrals.

**Controlling explanation:** Mead requires actual delegated authority and its exercise through the mechanism at issue. Congress expressly assigned rules, regulations and interpretations to HUD. The Secretary's designated, generally operative published interpretation differs from Mead's transaction-specific letters and Christensen's advisory response. The statutory good-faith protection corroborates that design but does not independently make every agency view controlling. Neither informality nor the policy-statement label settles the question. The Court independently enforces the referral prohibition, bona fide compensation exception and delegation's boundaries before sustaining this reasonable implementation.

The two-part inquiry gives both statutory commands effect. It considers borrower charges and lender payments together. No work, nominal work or duplicative work is not actual compensable service; the mortgage loan itself is not a good furnished by the broker that validates any premium. Conversely, compensation need not be allocated dollar by dollar to an itemized service or only to services benefiting one side of the transaction, and the prior service-list guidance creates no invariably required number of services. Performing some legitimate work or receiving reasonable total compensation does not cleanse a payment actually made to purchase a referral. Referral value cannot count as lawful service value. These qualifications answer the borrowers' concern that aggregate compensation could shelter the prohibited transaction.

#### H2. Judicial use for the earlier transactions

**Holding and operative rule:** The Court may use this authoritative interpretation in adjudicating the earlier transactions because the 1999 official account already required actual services and reasonable aggregate compensation, and the 2001 statement explains the application of that existing structure. That judicial use does not retroactively create legislative obligations or give an agency a general power to displace a binding judicial construction of enacted text.

**Controlling explanation:** Smiley permits judicial use of a current authoritative interpretation for antecedent transactions where it does not displace clear contrary agency guidance. The earlier official account already supplied the service-and-value structure. The 2001 account explains rate-sheet payments and lender knowledge within it. The earlier circuit reasoning construed ambiguity in the 1999 account; it did not establish a statutory command that every premium lacking itemized linkage is unlawful. The Court independently rejects that per se inference. Lechmere's protection of binding judicial construction therefore remains intact. The statement's later date, its clarification label and disagreement with the circuit do not substitute for this inquiry. On this record no supported clear contrary official assurance or changed legislative obligation supplies the claimed temporal bar. The interpretation concerns existing duties; it is not retrospective legislative rulemaking.

#### H3. Independent statutory construction requires vacatur of this certification

**Holding and operative rule:** Independently of the statement's controlling force, §2607(a)'s referral-agreement requirement and §2607(c)(2)'s protection of bona fide compensation prevent a rate-sheet premium and the absence of itemized service linkage, standing alone, from conclusively establishing a violation. A class proponent must demonstrate an actual common method satisfying Rule 23(a) and (b)(3) that proves the material statutory elements and addresses material differences in services, compensation and defenses; the present certification's incomplete liability premise fails that requirement.

**Controlling explanation:** The statute distinguishes payment for referrals from bona fide payment for actual work. A uniform premium practice may be evidence of the former, but its label and calculation method alone do not establish what the payment purchases. Actual work and total reasonable service compensation remain relevant, and an actual purchased referral remains prohibited even where a broker also performs legitimate work. This independent construction is sufficient to sustain vacatur without treating every detail of the administrative implementation as the only interpretation the text permits.

Castano and Amchem require certification under the governing substantive elements. Bridgestone/Firestone requires a workable proof and trial arrangement addressing material variation and defenses. The present certification used the payment formula and missing itemization to bypass that inquiry. The possibility that different common evidence could establish a referral arrangement does not repair the certification actually entered. The Eleventh Circuit correctly vacated it. On remand, the district court considers individual claims and any properly supported revised class, identifies the substantive elements and actual common evidence, and makes the required Rule 23 findings. Material individual issues matter because of their effect on that proof; their mere existence creates no categorical bar to RESPA classes. The §8(b) issue is outside the granted yield-spread-premium questions.'''

heim_blocks={
'Event':'''Heimmermann v. First Union Mortgage Corp., 305 F.3d 1257. October Term 2002. Merits decision, June 16, 2003. Review of the Eleventh Circuit's September 18, 2002 judgment vacating a district-court class certification under Rule 23(f). The questions are whether HUD's 2001 yield-spread-premium statement warrants controlling judicial weight and may inform adjudication of earlier transactions, and whether the substantive services-and-compensation inquiry defeats the certification based on uniform lender payments. Borrowers seek restoration of certification; the lender seeks to preserve vacatur. Decided on the merits submissions; no separate oral-argument date is stated.''',
'Participation':f'All nine Justices participated in submission and decision: {all9}.',
'Public Action':'The Court affirms the judgment vacating class certification and remanding for further proceedings.',
'Judgment & Remedy':f'''**Affirmed, 9–0.**

**Supporting:** {all9}.

The existing class certification remains vacated. The case returns for proceedings on the individual claims and any properly supported revised class under the statutory and Rule 23 standards in H3.''',
'Opinion Topology':'''__LEAD_AUTHOR__ delivered the opinion of the Court, in which __LEAD_JOINERS__ joined, and in which STONE-ZSELA, C. J., joined as to H3. STONE-ZSELA, C. J., filed an opinion concurring in part and concurring in the judgment.

| Writing | Author | Joined by | Relationship to judgment | Scope joined |
|---|---|---|---|---|
| Opinion of the Court | __LEAD_AUTHOR__ | __LEAD_JOINERS__; Stone-Zsela as to H3 | Supports affirmance throughout | Eight Associates join H1–H3; Stone-Zsela joins H3 only |
| Concurrence in part and in the judgment | Stone-Zsela | No other Justice | Supports affirmance on the independent statutory and certification ground | Joins H3; applies the Court's independent statutory construction to the earlier transactions while withholding H1–H2's administrative ground |''',
'Holdings':heim_h,
'Precedent Treatment':'''Mead is applied to the actual statutory assignment and official mechanism; its treatment of transaction-specific letters remains intact. Christensen's distinction between advisory interpretation and delegated authority is preserved. Chevron supplies reasonable-choice treatment within established delegation; it does not dispense with statutory boundaries. Skidmore retains consideration of an interpretation's persuasive reasons where controlling force is absent. Smiley is applied to judicial use of an authoritative current interpretation for antecedent transactions, with its reservation concerning clear contrary prior guidance preserved. Lechmere continues to protect binding judicial statutory construction. Landgraf and Bowen retain their separate limits on new retrospective legislative obligations; those limits are not converted into a prohibition on judicial interpretation of existing duties. Castano, Amchem and Bridgestone/Firestone are applied to an actual proof method under the complete substantive elements, preserving the possibility of a properly supported narrower class.''',
'Law After Decision':'''The stated official HUD mechanism qualifies for delegated interpretive treatment within RESPA's prohibition and bona fide-compensation allowance. Its permissible use for these earlier transactions follows the interpretive continuity identified in H2. Independently, courts must reject automatic liability based only on premium existence and missing itemization and must test proposed common proof against the actual referral and compensation elements. These rules govern the pending proceedings and other still-open claims presenting them. The proof required to establish a particular violation and the findings needed for a renewed class are ordinary adjudicative work under the settled standards.''',
'Separate Writings':'''Stone-Zsela concurs in part and in the judgment. He joins H3's independent construction and certification disposition because the existing certification rests on premium existence and missing itemization without an adequate common method proving the statutory wrong. A supported revised class remains available. He would apply that judicial construction to the earlier transactions under Harper, with Reynoldsville preserving independent procedural and remedial defenses. He considers §2617(a) and HUD's official mechanism substantial evidence of delegated authority under Mead, but would resolve the case without deciding this statement's independent controlling force. A later publication date supplies neither automatic new liability nor immunity. His disagreement therefore concerns the administrative basis of H1–H2, not H3's independent statutory rule or the judgment.''',
'Procedure After Action':'The mandate affirms the Eleventh Circuit judgment. The district court proceeds with the individual claims and considers any revised class using a demonstrated proof arrangement and the required Rule 23 findings; the present certification remains vacated.',
'Source Notes':'Heimmermann v. First Union Mortgage Corp., 305 F.3d 1257 (11th Cir. 2002); 12 U.S.C. §§2607(a), 2607(c)(2), 2617(a)–(b); 24 C.F.R. §3500.4(a)(1)(ii); HUD statements, 64 Fed. Reg. 10080 (1999), 66 Fed. Reg. 53052 (2001); Federal Rule of Civil Procedure 23(a), (b)(3), and (f).'}
heim_internal=f'''**Case and dockets:** Heimmermann v. First Union Mortgage Corp.; 305 F.3d 1257; lower docket 99-14066.
**Event and date:** Merits decision, 2003-06-16; October Term 2002, chunk 13, inventory 155.
**Result:** Affirm certification vacatur and remand, 9–0; eight Associates join H1–H3, Stone-Zsela joins H3 and gives a distinct temporal ground.
**Version / lineage:** Original decision for this event; no prior adjudication superseded.

## Event, route and chronology

The authorized additional-review schedule fixes June 16, 2003. Plenary merits submissions address the preserved federal questions arising from the Eleventh Circuit's Rule 23(f) decision of September 18, 2002. No separate Supreme Court oral-argument date is established. Borrowers seek restoration of certification on the referral theory; the lender seeks affirmance of vacatur. The legal defect concerns the actual certification's reliance on rate-sheet premiums and missing itemized service linkage. Loan-level liability is not the appellate judgment under review.

## Participation, entering law and form

Submission and decision participants: {all9}. Nine participate, satisfying the six-member quorum; five votes establish a Court proposition. The authorized merits review is confined to the preserved yield-spread-premium and certification questions. The frozen B_155 slice supplies Mead, Christensen, Lechmere, Smiley, the legislative/judicial temporal distinction, the operative statute and class-certification law. Bridgestone/Firestone, November 5, 2002, governs before this date. No same-day decision supplies entering law.

**Form fixed before assignment:** Signed plenary merits opinion stating H1's mechanism-specific administrative holding, H2's confined temporal use, and independently sufficient H3 statutory/class ground. One opinion can carry all three because each Associate joins each proposition in full. Stone's different ground receives a concurrence in part and in the judgment. The legal components are fixed without using counts, and none is divided or combined to affect eligibility.

## Stone fixed-core and branch comparison

The initial Section II disposition would vacate a mandate understood to impose automatic decertification, but its express conditional branch directs affirmance when the existing certification rests solely on premiums and missing itemization without sufficient common proof of the actual wrong. The frozen neutral and reconciled accounts establish precisely that condition. The branch therefore supplies Stone's affirmance; it is not the standing fallback and not a conversion caused merely by disagreement from colleagues.

Stone's independent statutory construction requires actual services, total compensation, reasonable service value and attention to what the payment buys. His Rule 23 position requires a workable proof method and preserves genuine revised classes and individual claims. H3 states those propositions at a compatible level, so he joins the entire independently sufficient H3 rather than being recorded as judgment-only throughout. He does not join H1's decision to give the statement independent controlling force or H2's reliance on that authoritative interpretation. His separate writing instead applies the Court's existing-statute construction to antecedent transactions under Harper, preserves Reynoldsville's independent defenses and recognizes the actual delegation question without deciding it. No new agency obligation, numerical burden or class entitlement is attributed to him. The merits preponderance requirement in his supplement is retained as his fixed position; this certification decision does not create a new ultimate burden. No clerical correction or standing-fallback use occurs.

## Coalitions, joins and assignment

Judgment: {all9} affirm certification vacatur and remand. H1 and H2: the eight Associates, {assoc}, join the full grounds and qualifications. H3: all nine join the independently sufficient statutory and Rule 23 ground. Scalia's broader Mead view, and Scalia, Kennedy and Thomas's different Landgraf methods, do not prevent their exact joins to these narrower adopted propositions. No additional methodological concession is invented. The final opinion adopts no automatic immunity for actual referral fees, invariant service count, mandatory allocation per dollar, general agency supremacy, or categorical class ban. The existing joins therefore remain compatible; no circulation or changed non-Stone ground is claimed.

Eligible lead authors are the eight Associates, each of whom joins H1–H3 in full. Stone assigns as a member of the unanimous judgment coalition but is not eligible to carry propositions he withholds. __ASSIGNMENT_BLOCK__

## Decision kernel and continuity

The complete controlling rules, adopted explanations, precedent treatment, judicial effect and mandate are stated without alteration in the Public Projection below. H3 remains an independent alternative ground even though H1 and H2 also command a majority. No Marks synthesis is needed. The earlier circuit's per se inference yields to the Court's own construction, not a general administrative power to overrule judicial law. The Rule 23 defect is the actual incomplete proof theory; a supported revised proposal receives normal consideration.

Stone-Zsela's published concurrence is noncontrolling only as to his independent temporal path and refusal to resolve administrative force. It supports judicial application of existing statutory meaning to earlier transactions under Harper, subject to independent defenses under Reynoldsville; it does not erase the majority's H1–H2 holdings. This specific position and full H3 join belong in continuity. There are no other published separate positions, roster changes or institutional changes. The merits review is completed; ordinary lower-court proceedings follow the mandate.

## Sources and validation

Research cutoff: 2003-06-16. The full published lower opinion identified in the frozen packets is saved at runtime/sources-B/Heimmermann.txt. Official period §§2607 and 2617, §3500.4 and the 1999 HUD statement are identified in the B_STATUTORY selection and saved source files. The lower opinion supplies the certification theory, September 2002 disposition and 2001 statement's relevant terms; no complete administrative archive, actual borrower reliance or new transaction finding is claimed. The frozen neutral packet's source map separates historical facts from the entering simulated authorities. The scheduling premise establishes this added review's date only.

Assembly checked Stone's express branch, nine judgment votes, eight complete H1–H3 supporters, Stone's severable H3 join, preservation of independent H3, certification posture, and mandate. Each public explanation is within 350 words. The five named blocks retain statutory qualifications, the §8(b) grant boundary and existing-certification status; they omit redundant unawarded-relief statements. Assignment and chronological publication remain for the root's serial procedure. Publication validation: __PUBLICATION_STATUS__.

'''+saved_annex(155,157)
publish('Heimmermann_v_First_Union_Mortgage_Corp_merits_2003-06-16.md',heim_internal,heim_blocks,dict(case='Heimmermann v. First Union Mortgage Corp.',date='2003-06-16',countable=True,assigner='Stone-Zsela',eligible_authors=["Stevens","O'Connor","Scalia","Kennedy","Souter","Thomas","Ginsburg","Breyer"],full_joiners=["Stevens","O'Connor","Scalia","Kennedy","Souter","Thomas","Ginsburg","Breyer"],assignment_authority_text="Stone-Zsela assigns as Chief in the unanimous judgment coalition. The signed H1–H3 form and propositions were fixed before counts. All eight Associates join every proposition; Stone-Zsela joins only the independent H3 ground. Fit concerns precise delegated authority, temporal interpretation and certification proof, preserving the independent statutory ground."))

(out/'B_specs.json').write_text(json.dumps(specs,indent=2),encoding='utf-8')
