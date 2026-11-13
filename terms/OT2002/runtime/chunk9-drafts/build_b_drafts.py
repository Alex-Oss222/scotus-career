from pathlib import Path
import json
import re

BASE = Path('terms/OT2002')
OUT = BASE / 'runtime/chunk9-drafts'
REC = (BASE / 'freeze/OT_2002CHUNK9_B_RECONCILED.md').read_text(encoding='utf-8-sig')
STONE = (BASE / 'runtime/OT_2002CHUNK9_B_STONE.md').read_text(encoding='utf-8-sig')
ALL = ['Stone-Zsela', 'Stevens', "O'Connor", 'Scalia', 'Kennedy', 'Souter', 'Thomas', 'Ginsburg', 'Breyer']

def case_slice(text, number, end_number=None):
    begin = text.index(f'## {number}. ')
    end = text.find(f'## {end_number}. ', begin) if end_number else text.find('## Assembly boundaries', begin)
    if end < 0:
        end = len(text)
    return text[begin:end].strip()

def make(case, number, next_number, file, identity, result, event, judgment, topology, holdings,
         precedent, law, separate, procedure, notes, stone_summary, compatibility, continuity, source):
    audit = case_slice(REC, number, next_number)
    stone_source = case_slice(STONE, number, next_number)
    # Source text is copied from the frozen/approved files, never retyped.
    text = f'''**Case and dockets:** {identity}
**Event and date:** Plenary merits decision; 2003-04-29; October Term 2002, chunk 9.
**Result:** {result}
**Version / lineage:** Original decision record; supersedes no completed adjudication.

## Event, record and chronology

{event}

{source}

## Participation and entering law

All nine seated Justices participate at submission or argument and decision: Stone-Zsela, Stevens, O'Connor, Scalia, Kennedy, Souter, Thomas, Ginsburg and Breyer. No case-specific nonparticipation is established. The Court has a nine-member quorum; five votes establish a majority. Review proceeds through the supplied merits inventory and the identified appellate judgment. The added-case inventory establishes lawful arrival without an invented docket or oral-argument date. The three supported group B decisions and stopped Demore matter share a common entering baseline and supply no law to one another.

Research cutoff: immediately before April 29, 2003. Entering law is supplied in `../entering-law/OT_2002CHUNK9_B_SELECTED.md`, `../entering-law/OT_2002CHUNK9_B_EXTRA_SELECTED.md`, `../entering-law/OT_2002CHUNK9_B_CURRENT.md`, `../entering-law/OT_2002CHUNK9_B_PRIOR_PUBLIC.md` and `../entering-law/OT_2002CHUNK9_B_TEXTS.md`; Herring additionally uses `../entering-law/OT_2002CHUNK9_HERRING_LAW.md` and `../entering-law/OT_2002CHUNK9_HERRING_CURRENT.md`. These are reading copies of the identified authority. No later law enters the decision. The current-law treatment and precise authority appear below.

## Stone: approved position and final compatibility

{stone_summary}

## Judgment, opinions and assignment

{judgment}

The publication form was fixed as one signed plenary lead opinion before assignment. It is not changed to affect the term balance.

{topology}

__ASSIGNMENT_BLOCK__

## Final compatibility by opinion part

{compatibility}

## Controlling holdings

{holdings}

## Precedent and current law

{precedent}

{law}

## Continuity and published noncontrolling positions

{continuity}

{separate}

## Source and validation annex

The neutral sources are `../freeze/OT_2002CHUNK9_B_VALIDATED_NEUTRAL.md` and `../freeze/OT_2002CHUNK9_B_VALIDATED_SUPPLEMENT.md`; Roell uses the superseding `../freeze/OT_2002CHUNK9_ROELL_FRESH_VALIDATED_NEUTRAL.md`; Herring uses `../freeze/OT_2002CHUNK9_HERRING_VALIDATED_NEUTRAL.md`. The final non-Stone positions are frozen in `../freeze/OT_2002CHUNK9_B_RECONCILED.md`. Stone's approved position is in `../runtime/OT_2002CHUNK9_B_STONE.md`. The neutral packet's supported historical facts, the supplied calendar premise for added cases, existing law and this event's adjudicative inference retain their separate status. No unavailable source is treated as litigant default. No actual circulation, bargaining or concessions are invented; the compatibility assessment tests the final formulation against existing commitments. No non-Stone commitment changes in assembly.

Qualitative validation completed in drafting: the named judgment coalition is distinct from every rationale coalition; partial joins and separate grounds remain explicit; statutory permissions and obligations remain distinct; every operative qualification and sufficient ground retained in the final formulation is stated in its own terms. Engine section 8 negative-statement review retains only adopted scope limits, actual open questions with their ground, requested-relief denials and surviving judgments. It omits hypothetical relief, unasked applications and repeated statements that separate proposals lack adoption. Ordinary controlling explanations remain within 350 words each. The internal controlling-holdings text is copied unchanged by this script into Public Projection Holdings.

This is an assembly draft: final serial author selection, balance recount, ledger/manifest rebuild, generated Render Input, link validation and term-wide deterministic checks remain for the operator. No completion of those pending checks is claimed here.

### Frozen non-Stone commitments and historical reconciliation — exact source copy

{audit}

### Approved Stone source — exact source copy

{stone_source}

## Public Projection

## Event

{event}

## Participation

Chief Justice Stone-Zsela and Justices Stevens, O'Connor, Scalia, Kennedy, Souter, Thomas, Ginsburg and Breyer participate.

## Public Action

{result}

## Judgment & Remedy

{judgment}

## Opinion Topology

{topology}

## Holdings

{holdings}

## Precedent Treatment

{precedent}

## Law After Decision

{law}

## Separate Writings

{separate}

## Procedure After Action

{procedure}

## Source Notes

{notes}
'''
    (OUT/file).write_text(text, encoding='utf-8')
    return text

roell_event = '''Roell v. Withrow, No. 02-69. Plenary merits decision, April 29, 2003. Argued February 26, 2003. On writ of certiorari to the United States Court of Appeals for the Fifth Circuit, 288 F.3d 199. The question is whether informed participation before judgment can establish consent to final civil adjudication by a magistrate judge under 28 U.S.C. §636(c)(1), despite failure to follow the prescribed written-consent procedure, or whether later confirmation alone can create consent.

Withrow consented orally and in writing; one defendant also gave written consent. Roell and Garibay participated throughout after notice of the right to refuse. The magistrate judge mistakenly believed that the consent forms already existed. After the jury returned a defense verdict, appellate inquiry produced later consent letters. The Fifth Circuit treated the absence of express consent before judgment as a nonwaivable defect and nullified the judgment. The defendants seek recognition of their earlier choice and consideration of the remaining appellate issues. Withrow maintains that the advance safeguards are indispensable.'''

roell_judgment = '''**Reversed and remanded, 5–4.**

**Supporting:** Stone-Zsela, O'Connor, Souter, Ginsburg and Breyer.
**Opposing:** Stevens, Scalia, Kennedy and Thomas.

The Fifth Circuit's nullification for absent express consent is reversed. The case returns for resolution of the remaining appellate issues on the valid consent basis established here. The four dissenters would instead vacate the appellate judgment and remand with instructions to dismiss the direct appeal for lack of appellate subject-matter jurisdiction.'''

roell_topology = '''__LEAD_AUTHOR__ delivers the opinion of the Court, joined by __LEAD_JOINERS__. Thomas files a dissenting opinion, joined by Stevens, Scalia and Kennedy. The Court opinion's complete coalition is Stone-Zsela, O'Connor, Souter, Ginsburg and Breyer; all five join both holdings and the mandate.'''

roell_holdings = '''### I. Knowing voluntary participation can establish contemporaneous consent

**Holding and operative rule:** Under the first sentence of §636(c)(1), a specially designated full-time magistrate judge may exercise final civil authority when every party actually consents; informed, voluntary participation before judgment after notice of the need for consent and the right to refuse can establish that consent despite deficient written documentation. The party invoking that authority must establish the contemporaneous knowing choice; silence without notice and later willingness alone cannot supply it.

**Authority:** The complete five-Justice Court-opinion coalition identified in Opinion Topology directly adopts this statutory rule and its application.

**Controlling explanation:** Congress conditioned this authority on consent but did not require a specific written request in the first sentence of §636(c)(1), as it expressly did for the different category of other part-time magistrate judges. The distinction between an actual choice and its documentation gives effect to both the substantive condition and the mandatory procedural safeguards. Peretz recognizes the importance of consent in the additional-duties setting, and Schor distinguishes personal Article III choice from structural limits; neither supplies a consent missing from this record.

Roell and Garibay knew that they could insist on an Article III judge and voluntarily continued before the magistrate judge until judgment. That informed course supplies consent. The judge's mistaken belief about existing forms does not establish express consent, and the later letters do not create a new prejudgment choice. Avoiding strategic objections after an adverse result reinforces the enacted distinction but cannot replace actual consent. The dissent's express-election reading gives the recording procedure the same substantive effect as Congress's different specific-written-request provision; the first sentence instead turns on the actual informed choice. Because that condition was met, §636(c)(3) supplies ordinary direct appellate review.

**Precedent treatment:** Peretz is distinguished as an additional-duties decision and supplies no automatic civil consent. Schor informs the personal-choice and structural distinction without displacing §636's conditions.

### II. The prescribed consent safeguards remain mandatory

**Holding and operative rule:** Section 636(c)(2) and Rule 73 require clerk notice when the action is filed, communication of the parties' decisions to the clerk, and execution and filing of joint or separate consent forms within the period specified by local rule. Renewed advice must preserve freedom to refuse without adverse substantive consequences; judges may not learn an individual response unless all parties consent, and the referral procedures must protect voluntariness.

**Authority:** The same five-Justice Court-opinion coalition directly adopts the complete rule and the distinction between its breach and genuinely absent consent. The dissent also treats these procedural commands as mandatory but gives their breach a different effect on final adjudicative and appellate authority.

**Controlling explanation:** The notice, recording and nondisclosure commands protect a free choice and must be followed by courts and parties. Recognizing actual informed consent does not make those commands optional. Their violation does not, however, negate the choice already made on this record. The statutory special-designation requirement remains an independent condition. Section 636(c)(4) separately permits the court to vacate a reference for good cause on its own initiative or for extraordinary circumstances shown by a party; those distinct conditions are not substitutes for the consent question decided here.

**Precedent treatment:** Peretz and Schor leave the enacted protections for this civil referral in force; neither authorizes disregarding the mandatory consent procedure.'''

roell_precedent = '''- Peretz v. United States concerns consent to an additional magistrate duty; its consent analysis informs but does not decide the different requirements for final civil adjudication.
- Commodity Futures Trading Commission v. Schor preserves the distinction between a personal Article III choice and structural limitations; the Court applies the actual statutory conditions rather than deriving consent from efficiency.
- Harper v. Virginia Department of Taxation supplies application of this construction to still-open cases on direct review. Reynoldsville Casket Co. v. Hyde preserves genuine independent defenses without permitting selective withholding based on reliance alone.'''

roell_law = '''A missing consent form does not invalidate a final civil judgment when actual, informed and voluntary consent existed before judgment under §636(c)(1)'s first sentence. Courts must continue to use the mandatory notice, recording and voluntariness protections. A genuinely disputed record requires determination of knowledge and voluntariness before authority can be sustained. The construction governs still-open direct-review cases within its scope; later assent cannot manufacture an earlier choice. The express written-request provision for other part-time magistrate judges retains its own requirements.'''

roell_separate = '''**Thomas, dissenting, joined by Stevens, Scalia and Kennedy.** The statute and Rule 73 require an affirmative election before a magistrate judge exercises final civil authority. Communication to the clerk, the protected consent process and an explicit election are substantive safeguards, not merely evidence of a choice inferred from participation. Congress's separate requirement of a specific written request for other part-time magistrates adds to, rather than eliminates, the generally required express election. The judge's mistaken assumption and the defendants' later letters cannot supply the missing act. Peretz's affirmative assent to an additional duty does not resolve this final-civil-judgment question, and Schor's personal-waiver principle cannot replace the enacted condition. Without valid statutory consent there is no final magistrate judgment qualifying for direct appeal under §636(c)(3); the proper action is to vacate the Fifth Circuit's judgment and direct dismissal of that appeal. This concerns the particular appellate route, not the district court's original jurisdiction over the civil action. The de facto officer doctrine cannot cure the missing condition on the appellate route. The dissent neither rejects consensual magistrate adjudication generally nor decides the prison medical-care claim.'''

make('Roell v. Withrow', 108, 109, 'Roell-v-Withrow_merits_2003-04-29.md',
     'Roell v. Withrow; No. 02-69; judgment below, 288 F.3d 199.',
     'The judgment is reversed and the case remanded, 5–4.', roell_event, roell_judgment,
     roell_topology, roell_holdings, roell_precedent, roell_law, roell_separate,
     'The Fifth Circuit must consider the remaining appellate issues under the valid contemporaneous consent established here. The medical-care verdict remains subject to that ordinary appellate review; absent advance writing alone is no basis to nullify it.',
     '28 U.S.C. §636(c)(1)–(4); Federal Rule of Civil Procedure 73; Withrow v. Roell, 288 F.3d 199. The later consent letters follow judgment and confirm, rather than create, the informed prejudgment participation found sufficient here.',
     'Stone joins the full statutory consent/documentation distinction, the mandatory safeguards, reversal and remaining-issues remand. His approved construction supports each governing proposition; no standing fallback is used. The public holding preserves the party invoking authority\'s obligation to establish contemporaneous knowing consent, not mere silence or postjudgment ratification. His direct-review transition is retained without reopening final judgments.',
     '''| Opinion or ground | Direct joins | Compatibility result |
|---|---|---|
| Court opinion, both holdings and remand | Stone-Zsela, O'Connor, Souter, Ginsburg, Breyer | All support actual informed prejudgment choice and mandatory documentation as distinct conditions; full lead eligibility is these five. |
| Dissent, express election and appellate dismissal | Stevens, Scalia, Kennedy, Thomas | All reject implied statutory consent and require vacatur with dismissal of the direct appeal. Thomas's own whole-scheme reading supplies the writing's legal organization; no historical authorship is treated as an assignment. |

The strongest dissent ground is answered in Holding I. No material notice or voluntariness dispute remains under the validated packet. No new factfinding or postjudgment ratification route is substituted. Every Justice's formal disposition is preserved.''',
     'The direct appeal resumes on its remaining issues. The dissent is a published noncontrolling express-election and appellate-route position of its four named Justices. It supplies no controlling change. No related institutional or roster consequence follows.',
     'Historical argument and event dates come from the validated neutral handoff. The complete lower opinion and operative Rule 73 source were validated before modeling; the fresh Roell handoff supersedes the earlier Rule 73 source gap. The original full trial transcript is not represented as recovered. The actual informed-participation predicate is the validated fact, not an inference from the defense verdict.')

herring_event = '''Herring v. Keenan. Plenary merits decision, April 29, 2003. On review of the United States Court of Appeals for the Tenth Circuit, 218 F.3d 1171, No. 99-1263. The questions concern constitutional protection against a federal probation officer's disclosure of intimate HIV information to employers and family, and qualified immunity for conduct in December 1993 and January 1994.

The complaint alleges that Herring, on federal probation for driving while intoxicated on federal property, told Keenan he had taken an HIV test and thought he might be infected but had not received a result. Without authorization, she allegedly told restaurant employers he was positive, pressed for his termination under an asserted legal prohibition, and told his sister that he had been tested and/or was positive. Herring died in 1996, and his estate continues this individual federal-officer damages action. These are pleading assumptions, not findings of confirmed infection, actual purpose, transmission risk or injury. The district court refused to dismiss the informational-privacy claim; the Tenth Circuit reversed on qualified-immunity grounds. The estate seeks continuation of that claim, and Keenan seeks immunity.'''

herring_judgment = '''**Vacated and remanded, 5–4.**

**Supporting:** Stone-Zsela, Stevens, Souter, Ginsburg and Breyer.
**Opposing:** O'Connor, Scalia, Kennedy and Thomas.

The appellate immunity judgment is vacated. On the pleaded account of intimate disclosures without sufficient official justification, the asserted legal qualified-immunity defense is rejected, and the informational-privacy claim returns for ordinary further proceedings. That legal defense is not remanded merely for reconsideration on the same assumed facts. Actual disclosure, justification, personal responsibility, causation, injury and any properly preserved independent objection to an authorized individual damages action remain for adjudication. The separately dismissed Eighth Amendment, distinct liberty and declaratory claims remain dismissed; the withdrawn roommate allegation remains outside the case.'''

herring_topology = '''__LEAD_AUTHOR__ announces the judgment of the Court and delivers the opinion of the Court as to Part I and an opinion as to Part II, joined throughout by __LEAD_JOINERS__. Stone-Zsela joins Part I and files an opinion concurring in part and concurring in the judgment. O'Connor files a dissenting opinion, joined by Scalia, Kennedy and Thomas. Scalia files a further dissenting opinion, joined by Thomas.

| Writing or part | Author | Direct coalition, including author | Relationship and scope |
|---|---|---|---|
| Part I, current intimate-information rule | __LEAD_AUTHOR__ | Stone-Zsela, Stevens, Souter, Ginsburg, Breyer | Five direct joins in the substantive protection and plaintiff-favorable application. |
| Part II, conduct-date notice under existing objective immunity | __LEAD_AUTHOR__ | Stevens, Souter, Ginsburg, Breyer | Four-Justice rationale rejecting the legal defense; supports vacatur and ordinary proceedings. |
| Partial concurrence and concurrence in the judgment | Stone-Zsela | Stone-Zsela | Joins Part I; supports vacatur on an authoritative-reliance replacement for the existing personal defense. |
| Notice-ground dissent | O'Connor | O'Connor, Scalia, Kennedy, Thomas | Would affirm immunity on the assumed facts under pre-1994 law; a new merits ruling is unnecessary to this disposition. |
| Further merits dissent | Scalia | Scalia, Thomas | Opposes the present informational-privacy extension as well as joining the notice-ground dissent. |

No opinion commands five votes for its immunity rationale. The five votes for vacatur and the five direct joins in Part I have different legal functions.'''

herring_holdings = '''### I. Probation does not erase protection against unjustified outside disclosure of intimate medical information

**Holding and operative rule:** The Fifth Amendment protects a probationer's objectively intimate medical testing and status information against intentional disclosure to an employer or family without sufficient lawful official justification. The claimant must establish the protected disclosure and the officer's personal responsibility; the asserted official need must sufficiently connect the information, recipient and supervisory function, with scope, use and safeguards fitted to that need.

**Authority:** Part I is the opinion of the Court, directly joined by Stone-Zsela, Stevens, Souter, Ginsburg and Breyer. These five adopt the rule at the stated level of generality and its application to the pleaded account.

**Controlling explanation:** Sheets protects intimate information against unjustified official dissemination. Denius requires an actual functional connection and fitted safeguards for government access to medical information. Paul P. and Lawall require attention to the particular audience and use; lawful acquisition for a confidential task does not by itself justify an additional transfer. Sterling confirms the constitutional importance of intimate family exposure, while its coercive-disclosure trigger remains distinct from the actual disclosures alleged here. Doe v. SEPTA preserved a confined benefits use, which supplies no permission for an unrelated employer or family disclosure.

Probation permits genuine supervision, not every use of information acquired through that relationship. Voluntarily telling an officer about a test is not general consent to publication. Neither a limited number of recipients nor the public-safety label establishes a sufficient connection to these disclosures. Each employer or sister communication must be assessed separately; a justification for one does not justify the other. The allegations of unconfirmed status, termination pressure and absence of adequate official need therefore state the protected invasion, subject to factual proof by a preponderance. The privacy rule permits justified protective action and does not turn every administrative confidentiality breach into a constitutional violation. The guidance supplies relevant context rather than the constitutional right.

**Precedent treatment:** Sheets and Denius are applied to intimate medical disclosure in federal supervision; Paul P. and Lawall supply the recipient-and-function limits. Sterling's distinct compelled-disclosure holding is preserved. Doe's confined benefits application and Whalen's safeguarded administration remain permissible at their actual scope.

### II. The immunity judgment is set aside without a common controlling immunity rationale

**Judgment and operative effect:** The five-Justice judgment rejects the asserted legal qualified-immunity dismissal on the pleaded no-justification account and returns the claim for ordinary proceedings. The same assumed account cannot be dismissed again on the legal defense rejected by this judgment; materially different proved facts and properly preserved independent defenses retain their force.

**Authority:** Stevens, Souter, Ginsburg and Breyer reach that result under the existing objective notice defense. Stone-Zsela reaches it under his distinct proposed authoritative-reliance defense. Their common judgment binds this case; Part I independently supplies the five-Justice substantive rule. No common narrower immunity rationale is established under Marks.

**Explanation of authority:** The four-Justice rationale finds that preconduct intimate-information and limited-supervision decisions gave sufficient warning on these allegations. Stone-Zsela would replace uncertainty-based immunity with protection for genuine reasonable reliance on directly authorizing binding precedent or enacted authority. One asks what a reasonable officer was objectively warned against; the other asks whether actual reliance on valid applicable permission is proved. Their agreement in rejecting this dismissal does not establish a shared rule for deciding other cases. The Court's existing objective immunity law remains the general governing law, while this case proceeds under the binding judgment.

**Precedent treatment:** Marks supplies no basis to turn these different grounds into a single immunity rationale. Harlow and Anderson retain their existing force. Meyer preserves the separate question of an authorized cause of action, which recognition of the substantive right does not resolve.'''

herring_precedent = '''- Sheets v. Salt Lake County supplies protection against unjustified intentional disclosure of intimate information, applied to the disclosed medical testing and status alleged here.
- Denius v. Dunlap supplies the actual-need, scope, use and safeguards inquiry for intimate medical information; its distinct objective immunity holding retains its force.
- Paul P. v. Verniero supplies the connection among protected information, audience and official purpose, applied to the particular outside recipients.
- Planned Parenthood of Southern Arizona v. Lawall distinguishes necessary confidential handling from an additional transfer requiring its own justification and safeguards; that distinction applies to supervisory acquisition and outside disclosure.
- Sterling v. Borough of Minersville preserves protection against an operative intimate family-disclosure ultimatum. The present actual-disclosure claim applies the privacy interest without merging the two triggers.
- Doe v. Southeastern Pennsylvania Transportation Authority and Whalen v. Roe preserve justified, safeguarded governmental information uses; those decisions do not supply the missing connection on the assumed allegations.
- Harlow v. Fitzgerald and Anderson v. Creighton retain objective, particularized conduct-date immunity; Elder v. Holloway requires all relevant preconduct authority. Clanton v. Cooper and Hope v. Pelzer preserve obvious-application notice without requiring a factual twin; Saucier v. Katz supplies no mandatory merits-first sequence.
- FDIC v. Meyer preserves the distinction between a substantive right, an individual-officer action and an unauthorized direct-agency damages action. The properly preserved source question remains independent.
- Marks v. United States supplies no common immunity rationale for the different judgment-supporting grounds.'''

herring_law = '''The substantive protection now applies to unjustified intentional outside disclosure of a probationer's intimate medical testing and status information. Genuine supervisory need must fit the particular information, audience, use and safeguards. The judgment conclusively removes the asserted legal immunity dismissal on the pleaded account; ordinary factual and remedial adjudication remains. The governing objective immunity framework continues for other cases, and the four-Justice notice application here supplies no broader controlling immunity rule. Present privacy decisions do not themselves give officials notice in December 1993 or January 1994.'''

herring_separate = '''**The Part II opinion, joined by Stevens, Souter, Ginsburg and Breyer.** Existing law sufficiently warned against these disclosures on the complaint's assumed absence of a legitimate purpose. Eastwood protected against unjustified intimate intrusion and required application of law to analogous facts. Woods, Barrington and Plymouth addressed unjustified medical exposure in their own settings. Griffin permitted a search tied to valid supervision; Harris addressed supported transmission risks, and Stine upheld a related counseling condition. Those decisions supply meaningful limits rather than a general probation exception. Whalen and Nixon's approval of safeguarded uses does not justify purposeless outside disclosure. Mangels concerns accurate unlawful-drug information, and DeSanti's contrary general approach is considered at its own hierarchy and scope. The cumulative preconduct boundary, applied under Elder, Clanton and Hope's present method, supplies sufficient warning despite the lack of an identical HIV-probation case. The guidance reinforces context but creates no constitutional right, and later privacy holdings supply no retrospective notice. The four reject the legal defense finally on these assumptions while leaving actual conduct, justification and the independent remedial questions for ordinary adjudication.

**Stone-Zsela, concurring in part and concurring in the judgment.** He joins the substantive privacy rule and would vacate the immunity dismissal by replacing Harlow and Anderson's uncertainty-based defense. After a violation under the full substantive rule, an officer would have a distinct personal defense only by identifying binding precedent or enacted authority directly authorizing the challenged conduct and proving genuine reasonable reliance on its valid, applicable permission. The officer would bear that factual showing by a preponderance; silence, title, custom and lack of a factual twin would not suffice. A faithful instruction could convey actual authority, while reasonable factual mistakes would remain part of the substantive rule. Genuine substantive discretion, source-specific absolute immunity, personal responsibility and independently authorized damages channels would remain. He would correspondingly displace Denius's contrary immunity rule and Clanton, Hope and Saucier only within that replacement's scope, preserving their substantive holdings and remedial limits. The allegation of an unestablished employment prohibition and contrary guidance permits no assumed reliance dismissal. Harper would apply his replacement to still-open direct-review claims, including earlier conduct; Reynoldsville would preserve genuine independent defenses, with final judgments and collateral authorization retaining their force. He would require separate determination of any preserved damages-source objection and then adjudication of the alleged disclosures, actual justification, responsibility, reliance and compensable injury. Lawall supplies neither earlier permission nor pre-1994 notice.

**O'Connor, dissenting, joined by Scalia, Kennedy and Thomas.** Current medical-privacy protection and sufficiently particular pre-1994 warning are different inquiries. The earlier cases arose in materially different investigatory, medical, prison or general-information settings, with competing approaches and a distinct supervisory relationship here. Even on the assumed absence of an adequate actual purpose, those authorities did not sufficiently settle the application to this probation officer's limited employer and family disclosures. Hodge and Denius preserve objective immunity for an unsettled application even where a present interest is recognized. The dissent considers all relevant preconduct law rather than demanding a factual twin, and it does not treat administrative guidance as constitutional notice. O'Connor and Kennedy accept the confined current interest reflected in Sheets, Denius, Sterling and Lawall but would decide this case on notice alone; their immunity votes do not find the alleged conduct lawful. All four would affirm the immunity judgment without crediting a disputed protective-purpose account.

**Scalia, further dissenting, joined by Thomas.** In addition to the notice defense, they oppose extending substantive informational privacy to these limited disclosures. Their Sheets, Paul P. and Lawall positions distinguish the actual holdings they must respect from a broader right inferred from confidentiality or official possession. The claim's intimate medical character and guidance do not by themselves supply the proposed constitutional extension. They adopt neither a universal denial of medical privacy nor a blanket probation exemption. Meyer likewise does not authorize automatic dismissal merely by treating an individual officer as a federal agency.'''

make('Herring v. Keenan', 109, 110, 'Herring-v-Keenan_merits_2003-04-29.md',
     'Herring v. Keenan; Tenth Circuit No. 99-1263; judgment below, 218 F.3d 1171; no separate Supreme Court docket supplied.',
     'The appellate immunity judgment is vacated and the case remanded, 5–4.', herring_event,
     herring_judgment, herring_topology, herring_holdings, herring_precedent, herring_law,
     herring_separate,
     'The case returns through the Tenth Circuit for ordinary adjudication of the surviving informational-privacy damages claim under the substantive rule and the judgment rejecting the asserted legal defense on the assumed account. The court must address any properly preserved objection to the individual damages channel independently, and then the supported factual and remedial issues. The separately dismissed claims and withdrawn roommate allegation remain outside the proceedings.',
     'Herring v. Keenan, 218 F.3d 1171; Tenth Circuit No. 99-1263. Fifth Amendment; Guide to Judiciary Policies and Procedures, Volume X, Chapter IV. The allegations concern December 1993 and January 1994; the sister disclosure concerns testing and/or positive status. Confirmed infection and an adequate official purpose are not established facts.',
     'Stone joins the present substantive privacy holding and the vacatur/remand judgment. He does not join the four Associates\' application of the retained objective notice defense; his express proposed replacement supplies his different judgment ground. His approved position supports addressing any properly preserved damages-source objection independently and ordinary factual adjudication, not a prescribed new discovery order. No standing fallback supplies a Herring position. His reliance-rule proof quantum, authority, valid-applicable-permission condition, factual-mistake allocation, temporal scope and preserved absolute/source limits are retained in his published concurrence.',
     '''| Opinion part or position | Direct joins | Final compatibility |
|---|---|---|
| Part I present privacy rule | Stone-Zsela, Stevens, Souter, Ginsburg, Breyer | Five share the confined rule and its assumed-fact application. O'Connor and Kennedy's conditional current-interest acceptance is not silently converted into an automatic opinion join. |
| Part II existing-law notice rejection | Stevens, Souter, Ginsburg, Breyer | Four full joins to a final legal rejection of this asserted defense, followed by ordinary proceedings. These four can author the complete lead. |
| Judgment vacating the immunity ruling | Stone-Zsela, Stevens, Souter, Ginsburg, Breyer | Common final rejection of this dismissal on its assumed account; the four Associates' frozen remand expressly permits this vacatur wording. Stone's ground is distinct. |
| Notice-only affirmance | O'Connor, Scalia, Kennedy, Thomas | All retain the ordinary objective defense and find the preconduct boundary insufficiently particular even on the plaintiff-favorable account. |
| Additional objection to current privacy extension | Scalia, Thomas | Preserved independently of the notice-only ground. |

All eight Associates retain Harlow–Anderson but divide equally on its application. Stone cannot author Part II because his approved position rejects its operative defense. The Chief is nevertheless in the actual judgment majority and assigns the signed lead from the four complete joiners. No second lead or changed form is needed.

The Marks inquiry compares the rules rather than the shared result. The four Associates apply objective warning without requiring consultation or actual reliance; Stone requires proved reliance on valid directly permissive authority after the full substantive inquiry. The absence of clear warning and the presence of genuine authoritative reliance are different predicates, and the frozen sources establish no general equivalence or logical-subset relationship that yields one operative rule accepted by five. The same result on these allegations alone cannot establish that relation. Eight votes preserve existing objective immunity as general law, but their 4–4 application split supplies no majority present-case notice rationale. The supported case mandate does not leave that same legal dismissal open for renewed selection below. No new generalized reliance defense or universal privacy notice rule is extracted.''',
     'This is an added merits event, not a departure from historical Supreme Court votes. The lower court\'s Alarcón/Baldock majority and Seymour dissent are different historical sources, not a Supreme Court lineup. The case returns under a five-vote binding judgment and five-vote privacy rule, while its notice reasoning remains fractured. Each published position below is noncontrolling except Part I and the exact judgment.',
     'The added event date is an inventory scheduling premise. The source cutoff for constitutional warning is separately fixed at December 1993 and January 1994. The complete lower opinion and guidance appendix were validated; no additional original filing is represented as recovered. The guidance permits informed written-consent disclosures, state-law-permitted public-health notice, defined custody transfers, legitimate professional staff access, relevant presentence information and confidential court advice. Its separate third-party-risk provisions require a reasonably foreseeable relationship-specific risk, specified supervisory approval and court involvement for opposed employment exclusion or warning. Those contextual provisions are not constitutional commands. No state-law criminality, positive test result, transmission risk, consent, actual motive or remedial-source ruling is invented.')

miami_event = '''United States v. Miami University. Plenary merits decision, April 29, 2003. On review of the United States Court of Appeals for the Sixth Circuit, 294 F.3d 797, which affirmed summary judgment and a permanent injunction against Miami University and Ohio State University. The Chronicle of Higher Education, an intervening defendant, seeks dissolution of the injunction, access to the requested records, or further discovery. The universities do not press this appeal.

The questions concern FERPA coverage of retained internal disciplinary records involving conduct that may also be criminal, the United States' authority to enforce accepted confidentiality obligations through an injunction, and the asserted First Amendment right to substantially unredacted disciplinary files. The Chronicle requested records of internal disciplinary proceedings for 1995 and 1996, including names. The universities released virtually unredacted November records and announced further releases; Miami adopted a third-party release policy. The requested files belong to internal disciplinary systems, not a request confined to original campus-police records. The prior state mandamus concerned a different requester and permitted specified redactions. The federal decree preserves FERPA-authorized and properly anonymized disclosures.'''

miami_judgment = '''**Affirmed, 9–0.**

**Supporting:** Stone-Zsela, Stevens, O'Connor, Scalia, Kennedy, Souter, Thomas, Ginsburg and Breyer.

The summary judgment, limited permanent injunction and denial of the identified further discovery are affirmed. The named universities remain bound against their proved policy or practice of releasing protected identifiable disciplinary information without consent or another FERPA permission. Effective anonymization, permitted disciplinary results and qualifying independent law-enforcement records remain available. The decree regulates the universities' covered disclosures and does not restrain the Chronicle's independent publication of lawfully obtained information. A material change in funding obligations or governing law must be presented through a supported motion to modify the injunction.'''

miami_topology = '''__LEAD_AUTHOR__ delivers the opinion of the Court, joined throughout by __LEAD_JOINERS__. Stone-Zsela joins Parts I–IV and the criminal-overlap portion of Part V, concurs in the remaining discovery judgment, and files a concurring opinion.

| Writing or part | Author | Direct coalition, including author | Relationship and scope |
|---|---|---|---|
| Parts I–IV, coverage, public enforcement, ordinary equity and access | __LEAD_AUTHOR__ | Stone-Zsela, Stevens, O'Connor, Scalia, Kennedy, Souter, Thomas, Ginsburg, Breyer | All nine join these rules and the limited affirmance. |
| Part V, discovery concerning conceded criminal overlap | __LEAD_AUTHOR__ | All nine Justices | The conceded criminal subject matter creates no material dispute about the maintained internal files' statutory function. |
| Part V, remaining identified discovery concerning injury and crime statistics | __LEAD_AUTHOR__ | Stevens, O'Connor, Scalia, Kennedy, Souter, Thomas, Ginsburg, Breyer | Eight join the complete discovery rationale; Stone-Zsela agrees in this result without adding a ground. |
| Concurrence | Stone-Zsela | Stone-Zsela | Joins the ordinary-equity disposition and proposes a broader presumption concerning the cure of a proved common unlawful practice. |'''

miami_holdings = '''### I. Retained internal disciplinary files fall within FERPA, subject to its actual exclusions and disclosure permissions

**Holding and operative rule:** Records directly relating to a student and maintained by an educational institution or its agent in the institutional recordkeeping capacity are education records under 20 U.S.C. §1232g(a)(4)(A), including the internal disciplinary files requested here. Criminal subject matter does not itself establish the law-enforcement exclusion: that exclusion requires records created by a law-enforcement unit for law-enforcement purposes and maintained by that unit.

**Authority:** Part I; all nine Justices directly join the coverage rule and its following qualifications.

**Controlling explanation:** Owasso gives separate force to institutional maintenance; these retained files satisfy the condition missing from temporary peer grading. The text reaches disciplinary information as well as academic information, and Congress's express final-result permissions confirm that disciplinary files otherwise fall within coverage. The requested files determine the student-institution relationship. A unit's additional disciplinary functions do not destroy its law-enforcement status, but records created and maintained exclusively for discipline are not thereby police files. A school-maintained disciplinary copy differs from an original qualifying police file; transferring an education record to police does not extinguish its protection. The definition and these statutory predicates decide coverage, with the promulgated regulations confirming the distinction. Christensen requires attention to an interpretation's actual authority and gives no automatic controlling weight to an advisory letter.

**Operative disclosure qualifications:** Written consent must identify the records, reasons and recipients; under §1232g(d), the required consent and parental rights transfer to a student who is eighteen or attends a postsecondary institution. Section (b)(6)(A) permits final results to the alleged victim of a crime of violence or nonforcible sex offense without requiring a violation finding. Section (b)(6)(B) permits public final results only when the institution finds that the alleged perpetrator violated its rules or policies with respect to that qualifying crime or offense. Under (b)(6)(C), final results include only the student's name, violation and sanction; another student's identity, including a victim or witness, requires that student's written consent. These provisions permit disclosure; they do not require it or open the underlying file.

Section (h) separately permits inclusion of appropriate disciplinary information about conduct posing a significant safety or well-being risk to the student or school community, and disclosure of that information to teachers and school officials, including those in other schools, with legitimate educational interests in the student's behavior. Section (i) separately permits disclosure to a parent or legal guardian of an under-21 student's alcohol or controlled-substance law, rule or policy violation when the institution determines a disciplinary violation; its express saving of state-law prohibitions remains. Effective anonymization and any other disclosure satisfying FERPA's applicable permission remain outside the decree's prohibition. The institution must identify the factual and statutory predicates of the exclusion or permission it invokes.

**Precedent treatment:** Owasso's maintenance requirement is applied to retained disciplinary files, preserving its distinct temporary-grading result. Christensen preserves the distinction between an authoritative legal rule and nonbinding advice.

### II. The United States may enforce these accepted grant obligations through this public action

**Holding and operative rule:** The United States may seek judicial enforcement of the named funding recipients' accepted FERPA confidentiality obligations through its established grant-enforcement authority, which the statutory scheme preserves. Section 1345 supplies jurisdiction for the authorized United States action; §1232g(f) directs appropriate enforcement, and §1234c(a)(4) preserves otherwise legally authorized action rather than independently creating an unlimited cause of action.

**Authority:** Part II; all nine Justices directly join this source-specific enforcement rule.

**Controlling explanation:** Pennhurst identifies the obligations attached to accepted federal funding, and King v. Smith and Wheeler v. Barrera support their binding force. The United States' traditional enforcement of accepted grant obligations protects that concrete federal interest. The statute authorizes administrative responses but also retains otherwise authorized enforcement; Congress did not make funding withdrawal the exclusive means of protecting these obligations. Section 1232g(f) permits termination only after a failure to comply and a determination that voluntary compliance cannot be secured, a condition on that remedy rather than a prohibition of the present judicial action. Section 1234c allows withholding, a compliance complaint, a compliance agreement or another legally authorized action, and separately preserves recovery of funds. Its final alternative presupposes rather than supplies authority.

Newport News requires compliance with the actual route invoked and rejects an agency's abstract administrative interest as enough for a different statutory appeal. The United States here relies on its accepted-obligation enforcement interest and an available judicial route. Gonzaga rejected a particular private §1983 nondisclosure entitlement; its statute-specific holding does not displace this distinct public enforcement source. Section 1232a's restriction on federal direction or control of schools does not bar this fitted enforcement of the confidentiality obligation the recipients accepted.

**Precedent treatment:** Newport News is distinguished by this concrete public grant-enforcement source. Gonzaga's private-action holding retains its force and does not bar this United States action. Pennhurst, King v. Smith and Wheeler v. Barrera supply the binding effect of accepted federal obligations.

### III. The proved continuing policy satisfies ordinary requirements for this limited injunction

**Holding and operative rule:** An authorized FERPA enforcement claim supports an injunction only upon proof of the violation and continuing threat, irreparable injury, inadequacy of legal relief, and equitable balance and public interest supporting relief fitted to the accepted obligation. The established identifiable disclosures and announced continuing policy satisfy those requirements here; the limited injunction against further unauthorized covered disclosures is affirmed.

**Authority:** Part III; all nine Justices directly join the ordinary-equity rule and its application.

**Controlling explanation:** Hecht and Weinberger preserve independent equitable judgment even when a statute has been violated. The universities' actual releases and intended continuation establish the threatened conduct; once intimate identifying information is released, confidentiality cannot be restored. Damages and eventual funding termination do not avert that loss, and the identified administrative alternatives do not adequately protect against the continuing release policy on this record. These are proved predicates for relief, not an injury presumption inferred from statutory coverage.

The balance and public interest support enforcement of accepted conditions while retaining every lawful disclosure route. The order permits proper redaction, the actual final-result permissions and qualifying police records, leaving the Chronicle's independent reporting unrestrained. Its reach follows the named recipients' established policy and obligations. A legally material change may support modification of the decree; the order's present force cannot be defeated by unilateral noncompliance.

**Precedent treatment:** Hecht Co. v. Bowles and Weinberger v. Romero-Barcelo are applied to preserve ordinary equitable predicates and fitted relief independently of statutory violation.

### IV. The claimed constitutional access right does not reach these substantially unredacted internal files

**Holding and operative rule:** A qualified First Amendment access right depends on the relevant kind of proceeding's history and the functional role of openness. The Chronicle has not established the necessary historical and functional basis for access to the substantially unredacted internal disciplinary files at issue; possible criminal subject matter does not transform the institution's discipline into the sovereign's criminal adjudication.

**Authority:** Part IV; all nine Justices directly join the rule and rejection of this access claim.

**Controlling explanation:** Richmond Newspapers and Press-Enterprise supply the experience-and-function inquiry. El Vocero applies it to the actual kind of trial-like preliminary hearing, rather than relying on a local label or tradition. University discipline here regulates the student-institution relationship, does not determine criminal guilt for the sovereign and does not preclude a later prosecution. The public value of campus oversight does not establish the required access tradition and function for these different files. Houchins supplies no general entitlement to government information. United Reporting requires scrutiny when access conditions select among speakers or intended expression, but does not convert a neutral confidentiality rule into a universal files-access entitlement. The inquiry therefore respects the potential value of public scrutiny without treating criminal allegations as dispositive of access.

**Precedent treatment:** El Vocero's functional inquiry is applied while its criminal-hearing result is distinguished. Houchins retains the absence of a general records entitlement. United Reporting preserves scrutiny of speech-selected conditions at its own scope.

### V. The identified discovery would not create a material dispute requiring further proceedings

**Holding and operative rule:** The denial of the Chronicle's identified additional discovery is affirmed because criminal overlap is conceded and the requested exploration of disciplinary proceedings, injury and crime statistics would not change the material statutory function, established releases or announced continuing policy on this record. Summary judgment rests on those undisputed predicates and independent legal and equitable review.

**Authority:** Part V's complete explanation has eight direct joins: Stevens, O'Connor, Scalia, Kennedy, Souter, Thomas, Ginsburg and Breyer. Stone-Zsela additionally joins the criminal-overlap conclusion and its maintained-record rationale; he agrees in the remaining discovery result without an additional ground.

**Controlling explanation:** Establishing that some conduct could be criminal would add a conceded fact, not change who created and maintained these internal disciplinary records or their purpose. The acknowledged identifiable releases and continuing policy establish the pertinent threat; crime statistics do not alter the loss of confidentiality when those identified records are disclosed. The actual requests therefore identify no material factual dispute requiring the proposed further inquiry.

**Precedent treatment:** Owasso's separate maintenance condition confirms why criminal subject matter does not create the asserted coverage dispute. The ordinary-equity authorities remain independently applied to the established disclosure threat.'''

miami_precedent = '''- Owasso Independent School District No. I-011 v. Falvo supplies the independent institutional-maintenance requirement; retained disciplinary records satisfy it, while its temporary-peer-grading holding remains intact.
- Christensen v. Harris County requires attention to interpretive authority and preserves persuasive rather than automatically controlling treatment of nonbinding advice.
- Pennhurst State School & Hospital v. Halderman, King v. Smith, and Wheeler v. Barrera supply the binding effect of accepted federal grant obligations.
- Director, OWCP v. Newport News Shipbuilding & Dry Dock Co. retains its requirement of an actual statutory route or cognizable interest; this authorized United States grant-enforcement action is distinct from the agency's rejected administrative-interest appeal.
- Gonzaga University v. Doe retains its statute-specific rejection of the asserted private §1983 FERPA entitlement; the public enforcement source is separate.
- Hecht Co. v. Bowles and Weinberger v. Romero-Barcelo preserve independent equitable judgment, applied to the continuing disclosure threat and this fitted decree.
- Richmond Newspapers, Press-Enterprise and El Vocero supply the inquiry into experience and the actual function of the proceeding; these internal files differ from trial-like criminal adjudication.
- Houchins v. KQED supplies no general constitutional access to government files. United Reporting preserves scrutiny of speech-selected conditions without creating the access entitlement asserted here.'''

miami_law = '''FERPA covers these retained internal disciplinary records despite possible criminal conduct, with the law-enforcement exclusion and each disclosure permission applied on its own predicates. The United States may enforce the accepted grant confidentiality obligation through this preserved public channel, and a proved continuing release policy can support a properly fitted injunction under ordinary equity. The claimed constitutional right to substantially unredacted internal disciplinary files fails under the actual experience-and-function inquiry. The affirmed decree preserves lawful disclosure, effective anonymization and independent reporting, and remains enforceable against the two named recipients subject to supported modification.'''

miami_separate = '''**Stone-Zsela, concurring.** He joins the text-and-function classification, the distinct public enforcement source, ordinary equity and the rejection of this access claim. He also joins the conclusion that conceded criminal overlap does not create a material discovery dispute about these maintained internal files. He would additionally presume that relief against a proved common unlawful disclosure practice must cure that practice for those governed unless the violators show a narrower remedy fully protects the accepted confidentiality obligation. The proposal rests on the demonstrated common practice, adds no decree against other institutions or the press, and preserves lawful redaction, permitted final results and independent police records. If applied, Harper would govern nonfinal cases within that proved-practice scope; Reynoldsville would preserve genuine legal defenses, with finality and independent jurisdictional limits retained. His agreement with the actual injunction rests on the ordinary equitable findings independently established here.'''

make('United States v. Miami University', 110, None, 'United-States-v-Miami-University_merits_2003-04-29.md',
     'United States v. Miami University; judgment below, 294 F.3d 797; no separate Supreme Court docket supplied.',
     'The judgment, limited permanent injunction and discovery ruling are affirmed, 9–0.', miami_event,
     miami_judgment, miami_topology, miami_holdings, miami_precedent, miami_law, miami_separate,
     'The limited permanent injunction remains in force against Miami University and Ohio State University. Further covered disclosures must satisfy the applicable consent or statutory permission, or effectively remove personally identifying information. Any legally material changed condition affecting the decree must be presented through a supported modification motion. The federal action independently construes FERPA; the different state mandamus requester and state-law meanings are not displaced by this judgment.',
     'United States v. Miami University, 294 F.3d 797. 20 U.S.C. §§1232g(a)(4), (b)(1)–(2), (b)(6), (d), (f), (h), (i), 1234c; 28 U.S.C. §1345; 34 C.F.R. §§99.3 and 99.8. The requested records are institutionally maintained internal disciplinary files, and the decree expressly permits lawful statutory disclosures and effective redaction.',
     'Stone fully joins Parts I–IV. His approved Issue 1 threshold expressly says conceded criminal subject matter creates no material discovery dispute about the institutional function, so he joins that Part V ground. The distinct requests concerning irreparable injury and available crime statistics are not expressly addressed; his standing fallback supplies affirmance of that discovery disposition only, adding no ground. He therefore does not fully join Part V and is not eligible to author the complete lead. His separate proposed common-practice-cure presumption is preserved as a qualified noncontrolling concurrence; ordinary equity independently supports his complete injunction join.',
     '''| Opinion part or position | Direct joins | Final compatibility |
|---|---|---|
| Parts I–IV | All nine | Actual coverage predicates, accepted-obligation enforcement source, ordinary equity and the bounded access inquiry have complete direct agreement. |
| Part V, criminal-overlap discovery | All nine | Stone's expressly addressed institutional-function ground joins the Associates' conclusion. |
| Part V, injury/statistics discovery rationale | All eight Associates | All eight frozen commitments support the actual discovery denial and complete rationale. Stone's fallback adds his disposition vote only for these unaddressed requests. |
| Separate proposed cure presumption | Stone-Zsela only | His proposed burden is not placed in the controlling equity holding. The independently satisfied ordinary predicates secure his full Part III join without inventing a compromise. |

All eight Associates can carry the whole lead; Stone's partial Part V join does not qualify him for the complete opinion. The Chief belongs to the actual judgment coalition and assigns from those eight. The strongest adverse arguments—academic-only coverage, criminal subject matter, administrative exclusivity, presumed equity and criminal-proceeding access—are answered in the controlling explanations at their actual scope. No separate privacy constitutional holding or broad administrative-deference rule is added. No Marks synthesis is necessary.''',
     'The injunction continues within its statutory bounds. It does not operate as appellate review of the earlier state mandamus and binds no different requester. No historical Supreme Court comparator exists. Stone\'s qualified cure-presumption concurrence is a published noncontrolling position; it does not change the ordinary-equity rule.',
     'The assigned event date is the inventory scheduling premise, not a historical Supreme Court merits date. The lower judgment of June 27, 2002 supplies the maintained-record facts, actual releases, announced policy, discovery requests and limited decree. The original university files and full discovery submissions are not represented as recovered. The packet treats criminal overlap as conceded while declining to adopt the lower opinion\'s categorical assertions that public oversight can never benefit discipline.')

specs = [
    dict(case='Herring v. Keenan', date='2003-04-29', file='Herring-v-Keenan_merits_2003-04-29.md',
         eligible_authors=['Stevens', 'Souter', 'Ginsburg', 'Breyer'], full_joiners=['Stevens', 'Souter', 'Ginsburg', 'Breyer'],
         assigner='Stone-Zsela', components=[dict(name='Vacate immunity judgment and remand with asserted legal defense rejected on the pleaded account', supporting=['Stone-Zsela', 'Stevens', 'Souter', 'Ginsburg', 'Breyer'], opposing=["O'Connor", 'Scalia', 'Kennedy', 'Thomas'])]),
    dict(case='Roell v. Withrow', date='2003-04-29', file='Roell-v-Withrow_merits_2003-04-29.md',
         eligible_authors=['Stone-Zsela', "O'Connor", 'Souter', 'Ginsburg', 'Breyer'], full_joiners=['Stone-Zsela', "O'Connor", 'Souter', 'Ginsburg', 'Breyer'],
         assigner='Stone-Zsela', components=[dict(name='Reverse jurisdictional nullification and remand for remaining appellate issues', supporting=['Stone-Zsela', "O'Connor", 'Souter', 'Ginsburg', 'Breyer'], opposing=['Stevens', 'Scalia', 'Kennedy', 'Thomas'])]),
    dict(case='United States v. Miami University', date='2003-04-29', file='United-States-v-Miami-University_merits_2003-04-29.md',
         eligible_authors=ALL[1:], full_joiners=ALL[1:], assigner='Stone-Zsela',
         components=[dict(name='Affirm summary judgment and limited permanent injunction', supporting=ALL, opposing=[]),dict(name='Affirm discovery denial', supporting=ALL, opposing=[])])
]
(OUT/'B_specs.json').write_text(json.dumps(specs, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')

for spec in specs:
    content = (OUT/spec['file']).read_text(encoding='utf-8')
    internal = content.split('## Controlling holdings\n\n',1)[1].split('\n## Precedent and current law',1)[0].rstrip()
    public = content.split('## Public Projection\n',1)[1]
    projected = public.split('## Holdings\n\n',1)[1].split('\n## Precedent Treatment',1)[0].rstrip()
    assert internal == projected
    assert content.count('__ASSIGNMENT_BLOCK__') == 1
    headings = re.findall(r'^## (.+)$', public, re.M)
    assert headings == ['Event','Participation','Public Action','Judgment & Remedy','Opinion Topology','Holdings','Precedent Treatment','Law After Decision','Separate Writings','Procedure After Action','Source Notes'], headings
    for component in spec['components']:
        names = component['supporting'] + component['opposing'] + component.get('not_reached', [])
        assert len(names) == len(set(names)) == 9 and set(names) == set(ALL)
    print(spec['file'], len(content), 'characters; projection and component checks passed')
