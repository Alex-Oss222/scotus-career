from pathlib import Path
import hashlib
import re

BASE = Path('terms/OT1996')
OUT = BASE / 'runtime/assembly'
OUT.mkdir(parents=True, exist_ok=True)

def read(rel):
    return (BASE / rel).read_text(encoding='utf-8-sig')

def sha(rel):
    return hashlib.sha256((BASE / rel).read_bytes()).hexdigest()

recon = 'freeze/OT_1996CHUNK1_RECONCILED_B_REPAIRS_VALIDATED.md'
assert sha(recon) == '70bf119ce28dd2b25106e909df0c8ee9818a2bf0f5aa4747bee9126f6c5c60ed'

YH = '''### I. Review under the corrected 1996 transition provisions

**Holding and operative rule.** Review of this existing deportation proceeding remains available under former INA §106 and 28 U.S.C. §1254(1) on November 13, 1996. Corrected IIRIRA §306(c)(1) gives new §242(g) reach across past, pending and future proceedings when that provision commences; it does not advance commencement of the new jurisdictional rule from April 1, 1997, and the other review restrictions establish no present bar on this record.

**Authority.** Part I of Justice Souter's opinion, joined by Stevens, O'Connor, Scalia, Kennedy, Thomas, Ginsburg and Breyer, supplies an eight-Justice controlling rationale. Stone-Zsela concurs only in this threshold resolution and does not join its reasons.

**Controlling explanation.** The Court reads the enacted timing instructions together. Section 309(a) sets April 1, 1997 as the general commencement date, expressly excepting §309 and §§303(b)(2), 306(c), 308(d)(2)(D) and 308(d)(5). Corrected §306(c)(1) applies the amendments as provided in §309, then separately extends §242(g) to old as well as new proceedings. The immediate-operation argument relies on those exceptions and the unrestricted reference to pending claims. But the exceptional clause specifies covered proceedings without supplying a replacement commencement date. Its present operation as an applicability instruction has independent work: after commencement, §242(g) reaches proceedings otherwise protected by grandfathering. This reading does not presume that jurisdiction can never change during litigation.

Corrected §309(c)(1), subject to its succeeding provisions, preserves the earlier proceedings and judicial review. No paragraph (2) or (3) agency election is established. Paragraph (4) requires a final exclusion or deportation order entered more than thirty days after September 30, 1996; it lists §§212(c), 212(h), 212(i), 244 and 245. The 1995 posture supplies no new triggering order, and that list omits former §241(a)(1)(H). Permanent §242(a)(2)(B)(i) instead lists §§212(h), 212(i), 240A, 240B and 245; clause (ii) separately addresses other statutorily discretionary authority, except §208(a) grants. Neither permanent clause governs this event.

Section 306(c)(2) protects existing §106 judgments and orders from invalidation or compelled reconsideration by paragraph (1); it does not independently establish appellate jurisdiction. Section 306(d)'s AEDPA-related criminal amendment supplies no bar without a covered conviction, which this record does not establish. The Court leaves open §242(g)'s scope after commencement, including its three subjects—commencing proceedings, adjudicating cases and executing removal orders—and its exception for review provided in §242. *Landgraf* and *Rivers* supply attention to Congress's actual temporal directions, not a new unanimous adoption of every earlier temporal rationale.

### II. Eligibility does not exclude the continuing fraud pattern from discretion

**Holding and operative rule.** Former INA §241(a)(1)(H), 8 U.S.C. §1251(a)(1)(H), permits the Attorney General to consider a continuing pattern of immigration fraud when choosing among eligible waiver applicants, even though particular acts are connected with entry. Eligibility does not erase that conduct or compel a waiver; the Court neither permits automatic denial to every eligible applicant because of the qualifying fraud nor decides whether the minimum qualifying fraud alone could sustain a particular individualized denial.

**Authority.** Part II of Justice Souter's opinion, joined by Stone-Zsela, Stevens, O'Connor, Scalia, Kennedy, Thomas, Ginsburg and Breyer, controls unanimously.

**Controlling explanation.** The statute makes eligibility and favorable discretion distinct. It reaches covered entry fraud or misrepresentation, whether willful or innocent. An applicant must be the spouse, parent, son or daughter of a citizen or lawful permanent resident, have possessed an immigrant visa or equivalent document, and otherwise have been admissible at entry. The exceptions for labor-certification and immigrant-documentation grounds under §§1182(a)(5)(A) and (7)(A) apply only when those grounds directly resulted from the fraud. The separate exclusion for assistance in Nazi persecution or participation in genocide remains. An actually granted waiver also reaches entry-inadmissibility grounds directly resulting from the fraud. These provisions define eligibility and the consequence of relief; they do not remove conduct from the discretionary decision.

*Jay v. Boyd* supplies the distinction between statutory eligibility and discretionary selection. *INS v. Errico* construed a mandatory predecessor; its family-preservation concern does not convert the later discretionary provision into an entitlement. *National Center for Immigrants' Rights* supports discretion exercised within the statute while preserving required individual consideration.

The Board accepted eligibility and expressly disregarded the initial entry fraud. It considered the wife's false-identity scheme and sham marital arrangements, the later naturalization fraud, further marital arrangements and lack of candor, together with favorable residence, business, property, family and health considerations and Taiwan connections. Those are the Board's findings and assessments. The Ninth Circuit allowed dishonest testimony to count but wrongly excluded collaboration and naturalization conduct because of their connection with entry. The argument that waiver discretion must remain meaningful therefore does not justify its categorical rule. A continuing pattern distinguishes applicants without making every eligible applicant lose. The Court does not reweigh the balance.

### III. Permissible factors remain subject to reasoned and consistent administration

**Holding and operative rule.** Statutory permission to consider a factor does not excuse arbitrary decisionmaking, pretext, disregard of a binding rule, or an unexplained departure from a genuinely settled agency policy. Here the Board rationally distinguished continuing immigration fraud from the initial entry fraud it disregarded; the record supplies no policy reversal requiring a new administrative balance.

**Authority.** Part III of Justice Souter's opinion, joined by Stone-Zsela, Stevens, O'Connor, Scalia, Kennedy, Thomas, Ginsburg and Breyer, controls unanimously.

**Controlling explanation.** The Court separates statutory authority from the lawfulness of its exercise. *Smiley*, applying the administrative-change principles preserved from *Good Samaritan*, requires examination of the agency's actual reasons, prior guidance and legitimate reliance. A court cannot supply a litigation explanation for an unexplained change. An agency may revise a policy openly with adequate explanation, subject to binding law; the existence of discretion alone supplies no answer.

The Board retained its initial-fraud distinction and explained the significance of the continuing pattern. Its actual reasons defeat the claim that this decision irrationally abandoned that distinction. The Court neither finds a different binding policy nor commands a new explanation for an unproved reversal. The mandate removes the Ninth Circuit's compelled reweighing based on categorical exclusion. Any genuinely remaining preserved objection is for ordinary proceedings within the record and mandate; the Court directs neither a waiver nor its denial, reopening, a new hearing, or a fresh Board balance. This decision concerns the statutory immigration function presented, not classifications outside it.
'''

YP = '''- *Landgraf v. USI Film Products* and *Rivers v. Roadway Express*: applied to the actual congressional timing instructions; their distinct temporal rationales are not combined into a broader unanimous framework.
- *Jay v. Boyd*, 351 U.S. 345: applied for eligibility's separation from discretionary selection; it remains authority for that distinction.
- *INS v. Errico*, 385 U.S. 214: distinguished because its mandatory predecessor differs from the discretionary text here; its own construction is not overruled.
- *INS v. National Center for Immigrants' Rights* (December 16, 1991): applied by analogy for statutory boundaries and legally required individual consideration; its release-condition holding is not transformed into a waiver decision.
- *Good Samaritan Hospital v. Shalala* and *Smiley* (June 3, 1996): applied for reasoned administrative interpretation and explained treatment of settled policy and reliance; statutory discretion does not displace those limits.
- *INS v. Doherty* (January 15, 1992): its fractured disposition supplies no controlling substantive reopening rationale for this waiver question; no separate rationale is promoted to Court law.
'''

YL = '''Effective November 13, 1996, courts may not exclude a continuing immigration-fraud pattern from former §241(a)(1)(H) discretion merely because its acts are connected with entry. The eligibility conditions, the distinct consequence of a granted waiver, meaningful individual discretion and ordinary review of actual agency reasons remain operative. The Court leaves the minimum-fraud-only individualized case unresolved and permits no universal eligibility-based denial. The specific transition construction preserves review at this event; it decides no post-April §242(g) scope question. No waiver is awarded or denied by this Court, and the agency balance is not judicially redone.'''

YT = '''| Writing | Author | Joined by | Scope and relationship to judgment |
|---|---|---|---|
| Opinion of the Court | Souter | Stevens, O'Connor, Scalia, Kennedy, Thomas, Ginsburg, Breyer in full; Stone-Zsela in Parts II and III and the disposition | Part I supplies the eight-Justice review rationale; Parts II and III state the unanimous permissible-factor and policy rules. |
| Concurrence only in the threshold resolution | Stone-Zsela | No additional joins | Agrees that the merits may be reached but does not join Part I; no separate written opinion. |
'''

YE = '''INS v. Yueh-Shaio Yang, No. 95-938. October Term 1996. On writ of certiorari to the United States Court of Appeals for the Ninth Circuit. Argued October 15, 1996; decided November 13, 1996.

The Ninth Circuit's June 22, 1995 judgment vacated the Board of Immigration Appeals' discretionary waiver denial and required reconsideration excluding fraud it regarded as intertwined with entry; rehearing was denied October 5, 1995. The INS seeks reversal, and Yang seeks affirmance of the restriction on discretionary consideration. The question is whether former §1251(a)(1)(H) permits consideration of immigration fraud connected with and extending beyond the entry fraud that made the applicant deportable. The corrected 1996 immigration-review provisions also require a threshold determination of review authority.'''

YJ = '''**Reversed and remanded, 9–0.** Supporting: Stone-Zsela, Stevens, O'Connor, Scalia, Kennedy, Souter, Thomas, Ginsburg and Breyer.

The Ninth Circuit's categorical restriction is reversed. Further proceedings must recognize that the continuing fraud pattern is a permissible discretionary consideration, subject to the statute, binding agency rules and policies, and reasoned decisionmaking. The mandate removes compelled reweighing resting on the erroneous categorical exclusion. It does not itself grant or deny the waiver, require the Board to reopen or reconsider on a new ground, or direct removal.'''

YS = '''The [Government petition and reproduced agency and lower decisions](https://archive.org/details/micro_IA40385013_0678) and [Ninth Circuit opinion, 58 F.3d 452](https://openjurist.org/58/f3d/452) support the accepted eligibility, agency reasons, balance and judgment below. The [reported case chronology](https://www.law.cornell.edu/supct/html/95-938.ZS.html) supplies the argument and decision dates. Former §1251(a)(1)(H), IIRIRA §§306 and 309, and [Public Law 104-302 §2](https://www.govinfo.gov/content/pkg/PLAW-104publ302/html/PLAW-104publ302.htm) supply the enacted eligibility and transition provisions; the technical correction is effective September 30, 1996.

The Board's findings, rather than a disputed fine detail of the naturalization form, support the account of misconduct. No new final administrative order, agency election or covered criminal conviction is established. The case does not depend on an unproved change of binding policy or an unestablished removal event.'''

AH = '''**Common authority.** Justice Scalia's opinion is joined in full by Stevens, O'Connor, Kennedy, Souter, Thomas, Ginsburg and Breyer. Stone-Zsela joins only Parts II-A, III's completed-acquisition ruling, and IV's rejection of the categorical constitutional grounds. The precise eight- or nine-Justice authority of each holding is stated below.

### I. The contempt adjudication remains reviewable

**Holding and operative rule.** Completion of the underlying trial does not moot review when setting aside the outstanding civil-contempt adjudication can afford meaningful relief from identified collateral consequences. The possible effect on Askin's West Virginia Bar status and the already pending related criminal-contempt proceeding preserve a live controversy here without any assumption of continuing civil confinement.

**Authority.** Part I controls with the eight full-opinion joiners identified above. Stone-Zsela agrees only with proceeding to the merits and supplies no additional threshold rationale.

**Controlling explanation.** *Church of Scientology* permits review where some meaningful relief remains, and *Calderon v. Moore* applies that principle even when relief cannot undo every past event. Ending confinement would not alone supply prospective relief, and abstract reputational concern would not suffice. But the challenged adjudication still has the concrete consequences identified in this record. Vacating it can matter to those consequences. The Court decides neither the criminal-contempt charge nor professional status and assumes no later disposition of either matter.

### II-A. The former wire and electronic definitions exclude the acquired radio portion

**Holding and operative rule.** Former 18 U.S.C. §2510(1) and (12)(A) exclude the radio portion transmitted between a cordless handset and its base from the statutory wire and electronic categories, including both speakers' words acquired at that link. The other participant's use of a landline or cellular telephone does not overcome those particular exclusions; the ruling does not classify every segment of the complete call as unprotected.

**Authority.** Part II-A controls with all nine Justices joining.

**Controlling explanation.** The Court applies the statute to the portion the agents acquired. General language covering transmission in whole or part cannot erase the specific handset-to-base exclusions. Askin's protected endpoint therefore does not make the intercepted portion a wire or electronic communication under the former text. Former §2510(12) also separately excluded wire or oral communications, tone-only paging and tracking-device communications; those distinctions are not interchangeable. The oral category has separate terms and is addressed in Part II-B. This construction neither authorizes acquisition at another point nor decides constitutional privacy.

### II-B. The former oral definition requires its own inquiry

**Holding and operative rule.** The former exclusions from the wire and electronic categories do not categorically foreclose oral-communication coverage. Former §2510(2) requires an exhibited expectation against interception under circumstances justifying that expectation and excludes statutory electronic communication; because former §2510(12)(A) excludes this radio portion from that electronic category, the lower court must determine whether the distinct expectation requirements are met.

**Authority.** Part II-B controls with eight Justices; Stone-Zsela does not join and would affirm complete former-Title-III noncoverage of the acquired segment.

**Controlling explanation.** The electronic exclusion within the oral definition uses the statute's category, not the everyday description of technologically transmitted sound. Treating the radio portion as necessarily electronic would disregard the very statutory exclusion the Government invokes. Yet exclusion from one definition does not establish either of the oral definition's expectation requirements.

The strongest objection is that oral coverage would undo Congress's two express exclusions and make their 1994 deletion unnecessary. It does neither. Conditional oral protection requires additional personal expectation findings, whereas deletion later supplies category protection without those findings. The two exclusions retain their full operation.

The lower court's assertion that Congress treated cordless calls only as wire or electronic communications supplied no independent determination under the complete oral definition and a correct personal inquiry. Askin's chosen endpoint and private interpersonal conversation are relevant, as are actual signal accessibility and established knowledge. Neither knowledge nor ignorance may be presumed. The Court vacates the categorical ruling but finds neither that Askin had nor that he lacked the required expectation, and creates no mandatory multifactor test.

### III. The 1994 deletion does not reclassify completed acquisition

**Holding and operative rule.** Public Law 103-414 §202 does not make completed preenactment interception unlawful by retroactively deleting the former category exclusions. A genuinely distinct later disclosure, use, evidentiary reception or refusal must be assessed on its own actual date and statutory predicate; pending appellate review alone establishes no such later-act violation, and preexisting oral-communication protection remains available on its own terms.

**Authority.** Part III's completed-acquisition ruling has nine joins. Its treatment of unestablished later acts and preservation of the oral route has the eight full-opinion joiners; Stone-Zsela supplies no additional later-act rationale and rejects oral coverage here.

**Controlling explanation.** The October 25, 1994 amendment deleted the cordless exceptions but did not amend §2510(2). Title I §111(b)'s four-year delay names §§103 and 105, and §111(a) likewise concerns its own title; neither delays Title II §202. Immediate enactment, however, does not direct retrospective reclassification. The interception preceded the early January 1994 indictment. Applying new interception prohibitions to that completed acquisition would attach a new legal consequence without the necessary congressional direction. *Landgraf* and *Rivers* require attention to the actual regulated conduct; neither a corrective purpose nor a pending appeal supplies missing temporal direction. Agreement on this case-specific result does not eliminate the distinct temporal methods in those earlier opinions.

Disclosure, use, reception and refusal can be separate events. But §§2511(1)(c) and (d) ordinarily require knowledge or reason to know that the interception violated the subsection, and §2515 has its own chapter-violation condition. A later use therefore cannot simply be assumed to convert an acquisition outside coverage into an unlawful interception. No exact post-amendment use or refusal date is established; the April 6 subpoena is not that event. A preserved independently applicable later-act claim requires its actual predicate. The Court makes no such finding and orders no inquiry merely because review remained pending. The older oral category is a separate possible source of coverage, unaffected by rejection of retrospective expanded categories.

### IV. Statutory noncoverage and another caller's endpoint do not decide personal constitutional privacy

**Holding and operative rule.** A statute's failure to prohibit an interception is not affirmative constitutional permission, and the other speaker's vulnerable endpoint alone does not establish that Askin surrendered every legitimate privacy interest in his own conversation. If the constitutional question remains necessary after the statutory inquiry, the lower courts must assess his personal interest, actual exposure and any legally available justification on the record, without presuming his knowledge or ignorance.

**Authority.** Part IV's rejection of the two categorical grounds controls with all nine Justices joining. The eight full-opinion joiners adopt the stated sequence and reserve a final privacy determination; Stone-Zsela's further conditional privacy rule appears only in his separate writing.

**Controlling explanation.** *Katz* protects private conversation without requiring trespass. *Wellons* requires examination of the claimant's own legitimate interest; another person's relation to the medium cannot replace it. *Pinson*, as applied in *Myers*, rejects a receiver-location shortcut within its technological home-information setting, but protects neither every emission nor every cordless call. *Alderman* and *Rakas* keep the personal-interest inquiry distinct from another person's rights and from remedy.

The Government's strongest argument is that both sides of this call traveled over a signal readily received with ordinary equipment. *White* recognizes the risk of disclosure through an unreliable participant. But that analogy supplies no finding that a participant cooperated with the Government or that Askin knowingly exposed his words. Actual conversational content differs from an inference drawn from exterior warmth. Conversely, selecting a landline or cellular endpoint and asserting a private conversation do not alone establish an objectively justified expectation.

The lower court treated statutory exclusion as congressional permission and applied its constitutional deference and unitary-conversation reasoning categorically. Those legal shortcuts must be corrected; no invalidation of the former statute is necessary. The Court does not finally hold that a search occurred, that the acquisition was unjustified, or that suppression follows. No warrant is established, but other exceptions require their actual legal and factual predicates rather than presumptions either way.

### V. Statutory just cause is conditional; the constitutional remedial extension is reserved

**Holding and operative rule.** Under *Gelbard*, a witness may establish just cause under §1826(a) when his own covered wire or oral communication was intercepted in violation of Title III, after consideration of applicable authorization or exceptions, and §2515 prohibits reception of the compelled testimony as intercepted contents or derived evidence. The surviving potential category here is oral, and each refused question's derivation and the witness's personal remedial entitlement must be determined; the Court leaves unresolved whether independently unconstitutional acquisition alone supplies just cause for this immunized witness's criminal-trial refusal.

**Authority.** Part V and its bounded implementing remand control with the eight full-opinion joiners. Stone-Zsela agrees with *Gelbard*'s statutory principle but rejects oral coverage here and would adopt the separate constitutional just-cause rule described in his writing; he does not join Part V.

**Controlling explanation.** *Gelbard* supplies a statutory defense, not an automatic constitutional testimonial privilege. Section 2515 protects wire or oral communications on its own violation condition; electronic coverage alone does not obtain that remedy. Use immunity does not repeal it. The Government's admitted monitoring satisfies §3504's occurrence-response requirement without admitting illegality or derivation.

Askin refused questions about knowing McNulty, Brumbaugh and Dabbs, using cocaine, and receiving cocaine from McNulty. A subject's appearance in the calls does not establish exclusive derivation, independent source or attenuation. Each actual question requires the appropriate connection and personal entitlement; no blanket refusal follows. Naming an exception likewise does not prove it.

*Calandra* declines constitutional exclusion for grand-jury questioning and distinguishes injury from remedy; derivative questioning is not itself a new search. This case concerns a criminal trial, so its grand-jury holding supplies neither an automatic bar nor an automatic right to refuse. Direct exploitation of this speaker's words to coerce his testimony supports the proposed extension; his nonparty, immunized status and the usual personal-use limits support the objection. The potentially dispositive statutory inquiry permits reserving that constitutional remedial issue.

*Leon* and *Krull* establish no automatic good-faith result: there was no warrant, and the former coverage exclusions did not themselves direct a constitutionally valid search. Any preserved reliance claim must fit an existing exception on objective facts. Independent source, attenuation and other lawful grounds likewise require their own predicates. No subjective-bad-motive requirement or new technology exception is adopted. The remand permits lawful reinstatement or setting aside of the civil-contempt adjudication after the necessary inquiries; it commands neither final discharge nor a new hearing.
'''

AP = '''- *Church of Scientology* (November 16, 1992) and *Calderon v. Moore* (June 17, 1996): applied to concrete surviving relief from the outstanding adjudication; completion of trial is not itself dispositive.
- *Landgraf* and *Rivers*: applied to the completed acquisition and the distinct possibility of genuinely later conduct; the result does not merge their separate temporal methods or retrospectively add new joins to them.
- *Katz v. United States*, 389 U.S. 347: applied to the claimant's own conversational privacy; trespass and endpoint ownership are not prerequisites.
- *United States v. White*, 401 U.S. 745: distinguished as to willing-participant disclosure; its recipient-risk principle does not establish cooperation or knowing public exposure on this record and remains operative in its proper setting.
- *United States v. Pinson* (May 8, 1995), as applied in *United States v. Myers* (June 11, 1996): applied against categorical inference from external reception, preserving their limited home-information holdings; no universal emitted-information rule is adopted.
- *United States v. Wellons* (May 30, 1995): applied for separate personal-interest, justification and remedy inquiries; the relation of a third person to the medium does not decide the claimant's interest.
- *Alderman v. United States*, 394 U.S. 165, and *Rakas v. Illinois*, 439 U.S. 128: applied to personal rather than vicarious rights; neither establishes entitlement to exclusion in every proceeding.
- *Gelbard v. United States*, 408 U.S. 41: applied to the conditional statutory §2515/§1826(a) defense for the witness's own communications and derived testimony; it does not settle the independent constitutional extension.
- *United States v. Calandra*, 414 U.S. 338: its grand-jury rule remains intact; its injury/remedy distinction informs but does not decide the reserved criminal-trial constitutional issue.
- *United States v. Leon*, 468 U.S. 897, and *Illinois v. Krull*, 480 U.S. 340: remain potential objective reliance doctrines only within their actual legal and factual conditions; neither supplies an automatic defense here.
'''

AL = '''Effective December 9, 1996, the former cordless exceptions govern the acquired wire/electronic segment, but do not foreclose the old oral category's separately established expectation requirements. The 1994 amendment does not retroactively reclassify completed acquisition. Statutory coverage, constitutional privacy, justification, personal remedy, question-specific derivation and just cause remain separate inquiries. A new controlling rule rejects the lower court's categorical oral and personal-privacy shortcuts; no final privacy, illegality or suppression finding follows. The conditional *Gelbard* route remains available. No majority adopts a constitutional right for an immunized trial witness to refuse direct-fruit questions; Stone-Zsela's proposed extension is noncontrolling. The duty to answer lawfully compelled questions remains, subject to established just cause.'''

AT = '''| Writing | Author | Joined by | Scope and relationship to judgment |
|---|---|---|---|
| Opinion of the Court | Scalia | Stevens, O'Connor, Kennedy, Souter, Thomas, Ginsburg and Breyer in full | Parts I through V and the bounded implementing remand; eight-Justice controlling rationale throughout. |
| Partial join in the Court's opinion | Stone-Zsela | — | Joins II-A, III's completed-acquisition ruling, and IV's rejection of the two categorical constitutional grounds; concurs in the judgment vacating and remanding. Does not join I's reasons, II-B, III's later-act/oral-route discussion, IV's reserved broader application, or V and its distinct remand rationale. |
| Opinion concurring in part and in the judgment | Stone-Zsela | No other Justice | Agrees with the disposition, would affirm complete former-Title-III noncoverage of the acquired segment, and proposes a more definite conditional personal-privacy rule and an independent constitutional direct-fruit just-cause rule. |
'''

AE = '''In re Askin. October Term 1996. On granted merits review of the United States Court of Appeals for the Fourth Circuit's February 2, 1995 affirmance of a civil-contempt judgment, reported at 47 F.3d 100, lower-court No. 94-5428. Argued October 8, 1996; decided December 9, 1996.

The questions are whether warrantless reception of the other participant's cordless-radio link violates the noncordless participant's Fourth Amendment rights; whether interception and use were prohibited by the Title III provisions governing the acquisition; and whether a witness may refuse criminal-trial questions directly derived from unlawful interception of his own communications, with what findings, remedial limits and just-cause consequences for civil contempt. The refusal occurred at the criminal trial after use immunity, not before a grand jury. The related criminal prosecution is not consolidated. The attorney-client and Sixth Amendment theories mentioned in the lower history are outside the granted questions.'''

AJ = '''**Fourth Circuit's judgment affirming civil contempt vacated and cause remanded, 9–0.** Supporting: Stone-Zsela, Stevens, O'Connor, Scalia, Kennedy, Souter, Thomas, Ginsburg and Breyer.

The Fourth Circuit's categorical statutory-oral and constitutional rulings cannot sustain its affirmance. The former wire/electronic exclusions and the nonretroactive completed-acquisition ruling remain binding legal conclusions. The eight-Justice implementing remand requires lawful disposition of the preserved claim through the separate oral-coverage, necessary personal-interest, prohibition, remedy and question-specific derivation inquiries. Stone-Zsela concurs in vacatur and remand on his different statutory and constitutional-remedy grounds.

The remand may lead to lawful reinstatement or setting aside of the civil-contempt adjudication. The Court orders no automatic suppression, blanket testimonial privilege, disposition of the separate criminal-contempt indictment, bar-status change, damages, new confinement, release from unestablished current confinement, new hearing or fixed return date.'''

ASW = '''**Stone-Zsela, concurring in part and in the judgment; no joins.** He agrees that the former wire/electronic exclusions cover the intercepted radio segment carrying both voices and that the 1994 deletion cannot retroactively make completed surveillance unlawful. His statutory position treats the place of acquisition as controlling under the former cordless exclusion. He would affirm the lower court's complete former-Title-III noncoverage ruling for that acquired segment and does not join the Court's additional oral-coverage route. Statutory noncoverage, on his view, neither authorizes interception at another point nor determines constitutional privacy.

He joins rejection of the categorical Fourth Amendment ruling and would state a further conditional rule: absent participant consent, a willing informant or knowing exposure, a landline or cellular caller does not surrender privacy merely because the other participant uses a vulnerable cordless handset without the caller's knowledge. *Katz* protects the speaker's own private words. *White* assigns the risk that an interlocutor will reveal or transmit them; it does not eliminate privacy merely because unknown agents can independently intercept a retransmission the caller did not select or know about. This rule leaves knowing exposure, participant consent and the cordless user's own expectation distinct. The record does not establish Askin's knowledge, so he would not finally apply the rule.

He accepts *Gelbard*'s statutory just-cause principle, but proposes a separate constitutional ground for this criminal-trial setting. When compelled questions are direct fruits of unlawful acquisition of the witness's own protected calls, and no recognized exception provides a lawful basis, refusal should constitute just cause under §1826(a). Coercing this speaker's testimony through his own unlawfully intercepted words gives the exclusionary rule a direct deterrent function. Question-specific derivation, personal rights and ordinary remedial exceptions keep the proposal bounded. *Pinson* and *Wellons* do not themselves establish this extension; *Calandra*'s grand-jury rule is left intact.

He would require the lower court to determine knowledge or knowing exposure, direct derivation of each question, and any preserved independent source, attenuation, objectively reasonable good-faith reliance or other lawful basis. If the governing premises establish lack of knowledge and direct derivation from unlawful acquisition without an applicable exception, the contempt adjudication must be set aside. He grants no automatic immunity from questions and no final discharge on this record. The Court's eight-Justice opinion leaves that independent constitutional just-cause question unresolved.'''

ASS = '''The [Fourth Circuit opinion, 47 F.3d 100](https://openjurist.org/47/f3d/100) supplies the endpoints, monitoring, use immunity, refused questions, civil-contempt posture and identified collateral consequences. The [1994 Code's §2510 and amendment notes](https://www.govinfo.gov/content/pkg/USCODE-1994-title18/pdf/USCODE-1994-title18-partI-chap119-sec2510.pdf) identify the former category exclusions and the oral definition's electronic exclusion added in 1986. The main Code text already incorporates the later amendment and does not govern the earlier acquisition wholesale. [Public Law 103-414](https://www.govinfo.gov/content/pkg/STATUTE-108/pdf/STATUTE-108-Pg4279.pdf), §§111, 202 and 203, supplies the October 25, 1994 changes and their title-specific structure.

The acquisition preceded the early January 1994 indictment. The record does not establish exact interception dates, a material post-amendment use or refusal date, Askin's knowledge of the cordless endpoint, each question's derivation, the separate personal suppression-interest issue or predicates for a remedial exception. Those questions limit the judgment and remain for the lawful proceedings described above. The October 8 argument and December 9 decision are the merits-calendar dates; the Fourth Circuit docket is not a Supreme Court docket. No later criminal-contempt disposition or continuing confinement is established.'''

def block(title, body):
    return f'## {title}\n\n{body.strip()}\n\n'

def projection(event, judgment, topology, holdings, precedents, law, separate, procedure, sources):
    values = [event, 'Stone-Zsela, Stevens, O\'Connor, Scalia, Kennedy, Souter, Thomas, Ginsburg and Breyer participated. No case-specific nonparticipation is established.', '', judgment, topology, holdings, precedents, law, separate, procedure, sources]
    titles = ['Event', 'Participation', 'Public Action', 'Judgment & Remedy', 'Opinion Topology', 'Holdings', 'Precedent Treatment', 'Law After Decision', 'Separate Writings', 'Procedure After Action', 'Source Notes']
    return '## Public Projection\n\n' + ''.join(block(t,b) for t,b in zip(titles,values))

def extracted_commitments(rel, start, end):
    t=read(rel)
    return t.split(start,1)[1].split(end,1)[0].strip()

YROWS = extracted_commitments('freeze/OT_1996CHUNK1_COMMITMENTS_YANG_REPAIR.md', '## Individual commitments and enhanced comparisons', '## Reconciliation boundary')
AROWS = extracted_commitments('freeze/OT_1996CHUNK1_COMMITMENTS_ASKIN_REPAIR.md', '## Individual enhanced commitments', '## Coalition scope and downstream boundaries')

yintern = '''**Case and dockets:** INS v. Yueh-Shaio Yang, No. 95-938; October Term 1996.
**Event and date:** Merits decision, 1996-11-13; argued 1996-10-15.
**Result:** Ninth Circuit reversed and cause remanded, 9–0; eight-Justice threshold rationale and unanimous merits/policy holdings.
**Version / lineage:** Initial assembly draft from the validated Yang repair and final isolated reconciliation; supersedes no completed adjudication. Not committed. Git existence and commitment verification remain pending the operator under the user's no-Git instruction; source hashes below identify the handoffs without representing them as commit hashes.

## Event, authority and entering law

''' + YE + '''

The historical argument date is supported by the saved official case header in `sources/reconciliation-yang/yang-official.txt`; assembly read the header for that fact and relies on the reconciliation's stated complete-opinion audit rather than claiming a fresh complete read. The event's historical date is adopted by the approved calendar. No additional historical intermediate grant or filing date is admitted.

All nine Justices participate at the argued and decision stages; no exclusion is established. The quorum is nine, and five votes suffice for a majority. The lawful review channels are former INA §106 and §1254(1), subject to the specific threshold construction below. Research cutoff: November 13, 1996; modern retrieval/assembly date October 12, 2026 is internal provenance only.

Entering authority is the term-opening law through July 1, 1996, the corrected statutory transition admitted with September 30 effect, and any earlier effective current-term law validated by the operator. The current neutral projection contains LAVAS's limited remand and the separate admitted transition text; neither supplies Yang's new judicial construction. The temporal register, NCIR, Smiley/Good Samaritan, Jay and Errico are applied at the limits stated in the repaired commitments. Doherty supplies no controlling substantive reopening rationale. Root must complete the cumulative chronology check before promotion; this assembly does not treat pending Roy/Lopez judgments as already effective or their assignment statements as substantive law.

## Stone position and final compatibility

Approved source: `runtime/OT_1996CHUNK1_YANG_STONE.md`, approval October 11, 2026. Stone's fixed core reverses the categorical restriction, permits the broader pattern within lawful discretion, preserves statute/policy/reason review and forbids a directed waiver balance or an automatic eligibility-based denial. Parts II and III express that approved ground and the same bounded remedy. No new doctrine about classifications outside the immigration function is added.

The new detailed IIRIRA review component is not expressly addressed by Section II. **Standing fallback used: review availability under the corrected 1996 transition provisions.** It supplies Stone's agreement to the majority's threshold resolution and no ground; Stone does not join Part I. His expressly approved merits reach, reversal and remand are separately preserved, not replaced by fallback. No other fallback is used. There is no required Circuit Justice application statement because this is appellate merits review.

## Public disposition and topology

''' + YJ + '\n\n' + YT + '''

## Controlling Holdings

''' + YH + '''
## Precedent treatment and current law

''' + YP + '\n' + YL + '''

## Continuity and limits

The Supreme Court merits event is complete upon final validation and promotion; the case continues below under the mandate. No retained-jurisdiction return date is ordered. No separate writing adds a noncontrolling substantive position. Stone's threshold judgment-only agreement adds no new rationale. No new roster, allotment, institutional practice, removal event or actual administrative waiver result is created. The disputed form detail and unsupported policy-reversal theory are not resolved as factual defaults.

## Adaptive audit annex

### Frozen commitments and individual legal grounds

The following individual rows are mechanically copied from the repaired commitment handoff. Their common sections remain incorporated at their full stated limits; final reconciliation retained every commitment without change. These are frozen modeling conclusions, not a purported historical conference transcript.

''' + YROWS + '''

### Final join audit

Each of Stevens, O'Connor, Scalia, Kennedy, Souter, Thomas, Ginsburg and Breyer joins Parts I–III and the bounded reversal/remand. Their threshold methods differ historically, but the present text-based commencement/applicability distinction is common; no Justice is assigned a new join in the complete Landgraf framework. Every row's prohibition on post-April §242(g) holdings, automatic minimum-fraud outcomes, judicial reweighing, invented policy reversal and mandatory new BIA proceedings is respected. Stone joins II–III and the disposition and concurs only in I's result. No circulation history is invented, and no frozen non-Stone commitment is changed or expanded.

| Proposition or disposition | Final support | Scope |
|---|---|---|
| Review available | All nine in result; Stevens, O'Connor, Scalia, Kennedy, Souter, Thomas, Ginsburg, Breyer in reasons | Stone fallback adds no reason. |
| Continuing pattern permitted | All nine | No categorical entry-connection immunity; minimum-fraud-only result reserved. |
| Policy/reason limits and actual pattern distinction | All nine | No independently established changed-policy remand. |
| Reverse/remand | All nine | No directed waiver, denial, reweighing, reopening or removal. |

### Reconciliation and assignment

The final reconciliation confirms historical unanimous agreement with the pattern holding and statutory-policy distinction; there is no non-Stone merits departure. The detailed §242(g) temporal construction is independently grounded in corrected enactments and is not falsely attributed to the historical opinion or its footnote. The eight retained scope reservations narrow the question decided without contradicting the historical rejection of categorical immunity.

**Assignment:** The Chief is in the judgment coalition and assigns the coordinated opinion to Souter. Fit governs: Souter's Smiley explanation of actual agency reasons, permissible interpretation and settled policy directly addresses the central distinction, and his temporal-framework joins support careful separation of commencement from reach. Scalia is the strongest alternative for the statutory text; Stevens is a strong alternative for NCIR and temporal architecture. Neither supplies a necessary accommodation absent from Souter's already supported common formulation. Stone's fixed position can state the merits rule, but provides no special drafting advantage over Souter's directly relevant administrative-law work, and is silent on the new threshold reasons. No expansion or changed join is needed. This is one Chief assignment; root adds the ordinal and cumulative tally after Roy is resolved. The preceding-term baseline records 101 Chief assignments, maximum O'Connor 27 and Souter 23, so no consecutive-term majority concentration bar excludes an author. No later-career capability evidence is used.

### Sources, limitations and validation status

Authoritative final reconciliation: `freeze/OT_1996CHUNK1_RECONCILED_B_REPAIRS_VALIDATED.md`; the scope read here was its global receipt, Yang, Askin and final validation only. Original root reconciliation drafts were not consulted. Repaired neutral facts and statutes are `YANG_NEUTRAL_REPAIR_VALIDATED.md` and `YANG_TRANSITION_CORRECTION.md`, with the retained clean A material only where not superseded. The agency and Ninth Circuit reasons are supported by the petition appendices and complete lower opinion described in those receipts; assembly makes no claim of a new complete merits-brief or appendix audit. No exact primary-source passage is manually recreated.

Source hashes and deterministic validations are in `audit/REPAIRS_ASSEMBLY.md`. No Git command occurred. Current files are drafts only; canonical filename, effective-state update, ledger/manifest rebuilding, final cumulative chronology verification, Render Input generation and check_term remain operator tasks. These workflow limits are excluded from the Public Projection.

'''

aintern = '''**Case and dockets:** In re Askin; Fourth Circuit No. 94-5428, 47 F.3d 100; no separate Supreme Court docket supplied; October Term 1996.
**Event and date:** Merits decision, 1996-12-09; argued 1996-10-08.
**Result:** Fourth Circuit's judgment affirming civil contempt vacated and cause remanded, 9–0, with an eight-Justice controlling oral-coverage and bounded-remedy rationale; Stone-Zsela concurs in part and in the judgment on distinct grounds.
**Version / lineage:** Initial assembly draft from the validated Askin repair and final isolated reconciliation; supersedes no completed adjudication. Not committed. Git existence and commitment verification remain pending the operator under the user's no-Git instruction; source hashes below identify the handoffs without representing them as commit hashes.

## Event, authority and entering law

''' + AE + '''

The grant, questions and Supreme Court calendar dates are adopted entry/scheduling premises in the validated neutral packet. The lower-court event and record facts are historical source facts; the present Supreme Court disposition and joins are assembly determinations. No new historical Supreme Court docket, grant date, filing, trial date, actual later use or additional argument is invented.

All nine Justices participate at argument and decision; no exclusion is established. Nine supply a quorum and five a majority. Granted appellate merits review proceeds under the supplied final-judgment posture and the surviving-relief holding. This is not a Circuit Justice application. Research cutoff: December 9, 1996. Modern retrieval and assembly occurred October 12, 2026 and are internal provenance only.

Entering law is the term-opening register through July 1, 1996 and law effective before this event after ordinary chronology revalidation. The specific authorities are the temporal register, Pinson/Myers at their limited scope, Wellons, Katz, White, personal-rights doctrine, Gelbard/Calandra and conditional reliance doctrines. The complete statutory corrections govern over the abbreviated original oral definition. Yang's proposed timing result concerns a different enactment and supplies no backdated holding here until promoted. Root completes cumulative earlier-event revalidation; an uncoordinated Humane Society event on the same date supplies no intervening law.

The monitoring preceded the early January 1994 indictment. Agents acquired both voices from Brumbaugh's cordless handset/base link with ordinary reception equipment and without prior judicial authorization; Askin used a landline or cellular car telephone. The April 6 subpoena establishes neither the date of trial refusal nor a post-amendment use. The lower court's completed-trial and identified collateral-consequence facts do not establish current confinement or a later criminal disposition. No unknown fact is treated as litigant default.

## Stone position and final compatibility

Approved source: `runtime/OT_1996CHUNK1_ASKIN_STONE.md`, approval October 11, 2026. Stone expressly would affirm complete former-Title-III noncoverage, reverse the categorical constitutional ruling, vacate contempt and remand for knowledge, question-specific direct derivation and applicable remedial defenses. His independent constitutional just-cause proposal is retained as a separate, noncontrolling position. It is not narrowed into the eight-Justice statutory route and is not counted as an Associate join. He joins the precise common former wire/electronic and completed-acquisition conclusions and rejection of the two categorical constitutional grounds, but not the old-law oral route or the Court's reservation of his remedial proposal.

**Standing fallback used: live controversy despite completion of the criminal trial.** Section II does not address that component; fallback supplies agreement to proceed and no Part I reasons. It is not used for the expressly addressed statutory, constitutional or remedial issues. His silence concerning a hypothetical later-act statutory claim supplies no invented reason or concession; the common completed-acquisition ruling remains separated from the eight-Justice later-act and oral-route discussion. No other fallback use is needed for the disposition.

## Public disposition and topology

''' + AJ + '\n\n' + AT + '''

## Controlling Holdings

''' + AH + '''
## Precedent treatment and current law

''' + AP + '\n' + AL + '''

## Published separate position and continuity

''' + ASW + '''

This is Stone's only published separate position here, identified as noncontrolling at each disputed point. The other eight publish no separate opinion and preserve no additional public noncontrolling rule through this event. The Supreme Court merits event is complete upon validation and promotion; ordinary remand remains below. No separate criminal case is decided and no court-return date, confinement fact, bar consequence or institutional change is created.

## Adaptive audit annex

### Frozen commitments and individual legal grounds

The individual rows below are mechanically copied from the repaired commitment handoff; all its common components, alternative-path comparisons and limits remain incorporated. The final isolated reconciliation retained them without change. The rows describe source-based commitments, not private dialogue.

''' + AROWS + '''

### Final join audit

All eight Associates join the complete Court opinion and its lawful remand sequence. Each receives his or her own date-eligible source basis in the frozen rows. The complete oral exclusion is preserved; statutory noncoverage is not treated as constitutional permission; White's recipient-risk argument is answered without inventing willing disclosure or knowledge; and the direct acquisition of words distinguishes Kennedy/Breyer's narrow thermal dissents without changing those Justices' commitments. No Associate joins a final privacy, illegality, derivation, suppression or broad constitutional just-cause conclusion. The Court's source-specific remand respects every frozen boundary.

| Part or component | Eight Associates | Stone-Zsela | Final authority |
|---|---|---|---|
| I, surviving relief | Join on identified consequences | Threshold result only under fallback | Eight-Justice rationale; nine reach. |
| II-A, former wire/electronic exclusions | Join | Joins | Nine-Justice rule. |
| II-B, possible oral coverage | Join and remand for actual requirements | Does not join; would affirm complete statutory noncoverage | Eight-Justice rule; preserved substantive disagreement. |
| III, completed acquisition | Join at case-specific temporal scope | Joins | Nine-Justice completed-acquisition rule. |
| III, later acts and retained oral route | Join with actual-date and statutory-predicate limits | No join | Eight-Justice rule; no invented Stone later-act view. |
| IV, rejection of categorical grounds | Join | Joins the precise common rejection | Nine-Justice rule; no final application. |
| IV, broader conditional personal-privacy formulation | Reserve actual expectation determination | States his own conditional protection rule | Separate Stone proposition only. |
| V, conditional statutory route and reserved constitutional remedy | Join with derivation, personal entitlement and legal exceptions | Does not join; statutory principle accepted separately, constitutional extension adopted separately | Eight-Justice Court rationale. |
| Vacatur and remand | Support bounded statutory/personal inquiry | Supports same formal disposition, different instructions | Nine-Justice disposition. |

There is no change in a reconciled non-Stone vote and no newly accommodated objection requiring renewed reconciliation. No draft circulation, negotiation or private motive is invented. No Marks combination is necessary because each Court holding has at least eight express joins; Stone's additional rule is not counted toward any broader Court holding.

### Reconciliation and assignment

No historical Supreme Court merits vote is supplied for Askin. The final reconciliation compared the complete Fourth Circuit writing and its footnotes, including White's exposure analogy, statutory constitutional-deference rationale and reserved suppression-interest issue. A different Supreme Court disposition here is not a departure from an invented historical Associate vote. Kennedy and Breyer's prior dissents concerned inferred exterior heat, not actual captured words, and specifically left more revealing acquisition open. The repaired shared grounds therefore require no historical-departure label.

**Assignment:** The Chief belongs to the unanimous coalition for the single judgment vacating the Fourth Circuit's affirmance and remanding, and assigns the entire coordinated opinion to Scalia. Stone's disagreement with conditional oral coverage and the governing remand analysis concerns the legal grounds and the path to a lawful disposition below; it does not establish a separately entered remedial judgment with an eight-Justice coalition. The eight-Justice implementing analysis states the controlling reasons for the common remand, not a second decree. No Associate assignment follows from Stone's refusal to join those reasons. Fit governs: Scalia's actual Pinson/Myers authorship and his frozen attention to all three statutory definitions make him best placed to articulate the precise acquisition, personal-interest and remedy boundaries without converting the earlier technological holdings into universal privacy. Stevens is the strongest alternative through temporal and effectual-relief work. Stone's proposed constitutional extension does not supply the eight-Justice accommodation, and his authorship offers no comparable advantage in maintaining their expressly reserved question. No expansion is needed; the eight already share the supported ground. Keeping the portions in one opinion makes their actual joins visible rather than altering them.

The coordinated opinion counts once as a Chief assignment. Root supplies the ordinal and cumulative tally after Roy. The preceding-term baseline reports 101 Chief assignments and no recipient above one half; no consecutive-term concentration ceiling bars Scalia. Same-day Humane Society bookkeeping creates no substantive dependency. No later-career capability evidence is used.

### Sources, limitations and validation status

Authoritative final reconciliation is `freeze/OT_1996CHUNK1_RECONCILED_B_REPAIRS_VALIDATED.md`, at the verified hash recorded in the audit. The repaired neutral authorities are `ASKIN_NEUTRAL_REPAIR_VALIDATED.md` and `ASKIN_STATUTORY_SOURCE_CORRECTION.md`, with validated B's Askin facts only where not superseded. Complete lower-opinion and statutory-source reading is certified by those frozen receipts and the final reconciliation; assembly does not claim fresh full readings of the PDFs. Long exact statutory text remains only in mechanically copied source pages. This record uses paraphrase, not reconstructed quotation.

The legal remand rests on identified erroneous categorical rulings, not modern research inconvenience. Remaining unknowns—knowledge, later-use timing, actual derivation, personal suppression entitlement and exception predicates—are preserved as actual unresolved merits or remedy matters. No stronger disposition is selected by assuming them. Source hashes and checks appear in `audit/REPAIRS_ASSEMBLY.md`; no Git command occurred. Root must complete chronology, canonical promotion, state projections, Render Input generation and term checks. No public workflow statement is projected.

'''

yp = projection(YE,YJ,YT,YH,YP,YL,'','The Ninth Circuit receives the cause for proceedings consistent with the permissible-factor ruling and the mandate limits. The Supreme Court merits decision is complete; no retained-jurisdiction return, new deadline, stay or removal command is ordered.',YS)
ap = projection(AE,AJ,AT,AH,AP,AL,ASW,'The cause returns to the Fourth Circuit for proceedings consistent with the separate coverage, necessary constitutional, remedy and derivation inquiries. A lawful contempt disposition depends on the findings and legal predicates described above. No final discharge, new hearing, new confinement or fixed follow-up date is commanded.',ASS)

(OUT/'Yang_DRAFT.md').write_text(yintern+yp, encoding='utf-8')
(OUT/'Askin_DRAFT.md').write_text(aintern+ap, encoding='utf-8')

expected=['Event','Participation','Public Action','Judgment & Remedy','Opinion Topology','Holdings','Precedent Treatment','Law After Decision','Separate Writings','Procedure After Action','Source Notes']
checks=[]
for name,h in [('Yang',YH),('Askin',AH)]:
    text=(OUT/f'{name}_DRAFT.md').read_text(encoding='utf-8')
    pub=text.split('## Public Projection\n\n',1)[1]
    assert re.findall(r'^## (.+)$',pub,re.M)==expected
    held=pub.split('## Holdings\n\n',1)[1].split('## Precedent Treatment\n',1)[0].strip()
    assert held==h.strip()
    internal=text.split('## Controlling Holdings\n\n',1)[1].split('## Precedent treatment and current law',1)[0].strip()
    assert internal==held
    lengths=[len(x.split()) for x in re.findall(r'\*\*Controlling explanation\.\*\* (.*?)(?=\n### |\Z)',h,re.S)]
    assert all(n<=350 for n in lengths), (name,lengths)
    assert '## Public Projection' not in pub
    checks.append((name,lengths,len(text.split())))

inputs=[recon,'freeze/OT_1996CHUNK1_COMMITMENTS_YANG_REPAIR.md','freeze/OT_1996CHUNK1_COMMITMENTS_ASKIN_REPAIR.md','freeze/YANG_NEUTRAL_REPAIR_VALIDATED.md','freeze/YANG_TRANSITION_CORRECTION.md','freeze/ASKIN_NEUTRAL_REPAIR_VALIDATED.md','freeze/ASKIN_STATUTORY_SOURCE_CORRECTION.md','runtime/OT_1996CHUNK1_YANG_STONE.md','runtime/OT_1996CHUNK1_ASKIN_STONE.md','freeze/OT_1996CHUNK1_ASSIGNMENT_BASELINE.md']
audit='''# OT1996 chunk 1 — Yang and Askin fresh assembly audit

Scope: initial assembly drafts only. No Git operation, canonical Record replacement, workspace mutation, Render Input or public render occurred. Writes are confined to OT1996. The final validated reconciliation was read and hash-checked before either Stone supplement; only its global receipt, Yang/Askin sections and final transfer were used. No root-authored earlier reconciliation draft or top-level protected private directory was accessed. General model knowledge is not represented as erased.

## Results

- Yang: reverse/remand, 9–0; Souter opinion. Part I is eight-Justice temporal reasoning, with Stone result-only fallback. Parts II–III and the bounded disposition are unanimous. No new BIA hearing/rebalancing, waiver, removal or post-April §242(g) ruling.
- Askin: vacate/remand, 9–0; Scalia opinion, eight full joins, Stone precise partial joins and separate concurrence in part and in the judgment. Stone retains his complete former-statutory noncoverage and independent constitutional direct-fruit just-cause proposal. Neither enters Court law. No non-Stone commitment changes.
- Assignment ordinals and cumulative current-term counts remain for root after Roy. Prior-term baseline: 101 Chief assignments; no recipient above half. Source-specific fit supports Souter and Scalia. The Chief assigns the entire Askin opinion because he joins the single vacatur/remand judgment; the eight-Justice controlling remand analysis and Stone's contrary grounds do not establish a separate remedial decree. The earlier proposed Associate assignment was removed as an assignment-only correction, with no vote, public topology, holding, directive or Stone position changed. Each opinion counts once as a Chief assignment.

## Deterministic checks

'''
for name,lengths,w in checks:
    audit+=f'- {name}: four initial labels retained; exactly eleven level-two Public Projection blocks in order; internal/Public Holdings byte-equal after boundary whitespace; explanation word counts {lengths}, all at or below 350. Draft total {w} words.\n'
audit+='''
## Substantive checks

Judgment counts and partial joins were checked independently. Yang's detailed temporal rationale does not become a Stone reason through his approved merits reach; the fallback component is identified internally and its result-only scope is public. Askin's mootness fallback does not replace his express statutory or remedy positions. All eight repaired rows were mechanically copied with individual authorities and retained boundaries. The complete oral-definition electronic exclusion and former electronic-category cordless exclusion both remain; policy/reason constraints in Yang remain separate from statutory permission. No subsequent enacted rule or later judicial decision is imported. No full quoted primary-source text is manually recreated.

Askin's eight-Justice holdings keep coverage, prohibition, personal constitutional interest, justification, remedial entitlement, derivation and just cause distinct. The lower court's actual categorical reasoning supplies the remand ground. No unknown endpoint knowledge, later-use date, question derivation or exception predicate is presumed. All identified source limits appear in the internal kernel and public substance where material. His noncontrolling separate writing is carried in continuity and Public Projection with its grounds, direct-fruit limitation and conditional remedy.

Public source notes contain source support and legal limits only. No hashes, modern dates, approval history, mode, assignment bookkeeping or private instructions appear there. No workflow blocker remains in either proposed legal disposition. Operator promotion remains conditional on the ordinary cumulative earlier-event review and final record/projection checks.

## Verified input SHA-256 values

| Input | SHA-256 |
|---|---|
'''
for rel in inputs:
    audit+=f'| `{rel}` | `{sha(rel)}` |\n'
audit+='''
These are file-content hashes, not Git hashes. Git existence, freeze commitment and record commitment status are unverified under the explicit no-Git restriction. The drafts make no contrary certification. Root must supply final natural-key Record paths, effective-state application, cumulative chronology and assignment ordinals, generated handoffs, and check_term validation; this audit authorizes none of those as already complete.
'''
(BASE/'audit/REPAIRS_ASSEMBLY.md').write_text(audit,encoding='utf-8')
for row in checks:
    print(row)
