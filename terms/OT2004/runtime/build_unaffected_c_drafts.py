from pathlib import Path
import re

base = Path('terms/OT2004')
commitments = (base / 'freeze/OT_2004CHUNK2_COMMITMENTS_C.md').read_text(encoding='utf-8-sig')
reconciled = (base / 'freeze/OT_2004CHUNK2_RECONCILED_C_UNAFFECTED.md').read_text(encoding='utf-8-sig')

def case_section(text, start):
    at = text.index(start)
    end = text.find('\n## ', at + len(start))
    return text[at:end if end >= 0 else len(text)].strip()

def subsection(text, heading):
    at = text.index(heading)
    end = text.find('\n### ', at + len(heading))
    return text[at:end if end >= 0 else len(text)].strip()

def audit(name, start):
    c = case_section(commitments, start)
    r = case_section(reconciled, start)
    ctable = subsection(c, '### Justice-specific commitments')
    rtable = subsection(r, '### Justice-specific reconciliation')
    return ('## Adaptive audit annex\n\nThe following frozen commitment and reconciliation material is copied verbatim from the authorized handoffs. It remains internal. Final compatibility is recorded separately above.\n\n' + ctable + '\n\n' + rtable + '\n')

all_names = "Stone-Zsela, Stevens, O'Connor, Scalia, Kennedy, Souter, Thomas, Ginsburg and Breyer"
majority_names = "Stone-Zsela, Stevens, O'Connor, Scalia, Kennedy, Thomas and Breyer"

banks_holdings = '''### I. A contingent fee remains part of the client's otherwise taxable recovery

**Holding and operative rule:** When a client retains ownership and control of an income-producing legal claim and counsel acts as the client's agent, the client's gross income under 26 U.S.C. §61 includes the contractual contingent fee paid from an otherwise taxable recovery, whether the payment passes through the client or goes directly to counsel and whether a state-law lien secures it. A taxpayer seeking exclusion must identify an applicable statutory exclusion or a genuinely different ownership arrangement; uncertainty about the recovery's value and the lawyer's labor do not alone transfer the claim.

**Authority:** AUTHOR_PENDING's opinion of the Court, joined in full by every other participating Justice. The common coalition identified in Opinion Topology adopts the rule, both docket-specific applications and the explanation below.

**Controlling explanation:** The claim arising from the client's legal injury produces the recovery. The client retains ultimate control, including whether to settle, while counsel acts for the client. *Lucas v. Earl*, 281 U.S. 111, prevents advance allocation of earnings from changing their attribution; *Helvering v. Horst*, 311 U.S. 112, attributes diverted proceeds to the person who retains the income-producing source and obtains the benefit of its disposition. Payment to counsel satisfies the client's contractual obligation.

The taxpayers emphasize that recovery was uncertain and that counsel supplied the skill, work and risk needed to obtain it. Those features explain the compensation arrangement. They do not change ownership of the claim or turn this agency into a partnership. The attribution rule does not depend on a known recovery amount when the contract is signed or on proof that a particular taxpayer sought to avoid tax.

The same inquiry resolves Banaitis's Oregon argument. State law gives counsel a superior lien securing compensation, but the accepted rights leave prosecution and ultimate settlement control with the client. Priority in payment therefore does not transfer the income-producing claim. Banks's contractual fee and Banaitis's directly paid, lien-protected fee are both included.

The mismatch between inclusion and restricted deductions can impose a substantial tax burden. *Commissioner v. Schleier* and *O'Gilvie v. United States* require the actual statutory conditions for excluding particular receipts; they provide no equitable exclusion for this fee payment. Inclusion and deductibility perform separate statutory functions.

**Material limits and questions not reached:** The holding concerns the principal-agent relationship established in these records. The Court leaves separately awarded statutory fees unresolved because Banks's settlement produced a contractual contingent fee, without a separate statutory award or an established payment in its place. Supplementary partnership, capital-expense and reimbursed-employee-expense theories were not developed below and are not reached on that preservation ground. A genuinely separate ownership arrangement is outside the presented arrangements.

### II. Each tax liability is calculated under the law for its tax year

**Holding and operative rule:** Both fee-exclusion judgments are reversed, and each docket returns for the lawful tax calculation using the full otherwise taxable recovery and deductions available under the applicable tax-year provisions. Section 703(c) of the American Jobs Creation Act of 2004 makes both payment of the fees and costs after October 22, 2004, and a judgment or settlement after that date necessary to the new deduction; these earlier transactions remain governed by their tax-year law.

**Authority:** The same whole-Court opinion and common coalition identified in Opinion Topology.

**Controlling explanation:** Gross-income attribution answers whose taxable recovery includes the fee. The deduction and alternative-minimum-tax provisions then determine their separate consequences. Congress placed the new deduction in §62 but expressly made its operation prospective through two temporal conditions. Both matters involve earlier transactions. The courts on remand must apply the old-year provisions to the actual payment and return records, giving effect to the inclusion rule in each docket.
'''

banks_precedent = '''- *Lucas v. Earl*, 281 U.S. 111: Applied to advance diversion of contingent proceeds while the taxpayer retains the source; uncertainty of the eventual amount does not defeat attribution.
- *Helvering v. Horst*, 311 U.S. 112: Applied to a client's retained legal claim and the benefit obtained when its proceeds satisfy the client's fee obligation.
- *Commissioner v. Schleier*, 515 U.S. 323: Preserved as requiring the actual statutory conditions for a receipt-specific exclusion; those conditions supply no fee-payment exclusion here.
- *O'Gilvie v. United States*, 519 U.S. 79: Preserved for receipt-specific causation under its applicable exclusion provision; the present attribution rule does not alter that inquiry.
- *United States v. Burke*, 504 U.S. 229: Its fractured judgment retains its existing force. This decision draws no general remedial-menu rule from it.
'''

banks_event = '''Commissioner of Internal Revenue v. Banks, No. 03-892, and Commissioner of Internal Revenue v. Banaitis, No. 03-907; 543 U.S. 426. Merits decision, January 24, 2005. Argued November 1, 2004. On writs of certiorari to the United States Courts of Appeals for the Sixth and Ninth Circuits, consolidated for disposition.

The Sixth Circuit, 345 F.3d 373, excluded Banks's contractual fee from his otherwise taxable litigation recovery. The Ninth Circuit, 340 F.3d 1074, excluded Banaitis's fee because Oregon law gave counsel a superior lien. The question is whether an otherwise taxable litigation recovery includes the contingent-fee portion paid to counsel, including under that state-law protection. The Commissioner seeks reversal and inclusion in both dockets; the taxpayers defend their exclusions.'''

banks_judgment = f'''| Docket | Disposition and vote | Supporting Justices | Remedy |
|---|---|---|---|
| No. 03-892, Banks | Sixth Circuit reversed and case remanded, 9–0 | {all_names} | Include the contractual fee portion and calculate the affected liability under the applicable tax-year provisions. |
| No. 03-907, Banaitis | Ninth Circuit reversed and case remanded, 9–0 | {all_names} | Include the directly paid, lien-protected contractual fee portion and calculate the affected liability under the applicable tax-year provisions. |'''

banks_topology = f'''One signed opinion of the Court resolves both consolidated dockets. AUTHOR_PENDING delivers the opinion, joined in full by every other participating Justice. The complete opinion coalition is {all_names}.'''

banks_internal = f'''**Case and dockets:** Commissioner of Internal Revenue v. Banks, No. 03-892; Commissioner of Internal Revenue v. Banaitis, No. 03-907.
**Event and date:** Merits decision; 2005-01-24; October Term 2004, chunk 2.
**Result:** Draft substantive resolution: reverse both fee-exclusion judgments and remand, 9–0 in each docket.
**Version / lineage:** Assembly preparation draft only; supersedes no adjudication and supplies no current law. AUTHOR_PENDING and ASSIGNMENT_PENDING require sequential assembly completion.

## Event, chronology and record

{banks_event}

The frozen neutral record establishes that each taxpayer retained the claim and its ultimate settlement control. Banks paid counsel from his employment settlement; Banaitis's defendants paid the agreed contingent portion directly to counsel. Oregon's lien secures the lawyer's compensation. The taxable character of the underlying recoveries is accepted for the attribution question. The lower courts' contrary fee-exclusion judgments require separate remands. The historical source corroborates the dates and lower-court premises; it supplies no controlling simulated law or authorship.

## Participation and entering law

All nine members participate at argument and decision: {all_names}. No case-specific absence or disqualification is established. The merits channel is certiorari; nine participants furnish a quorum and five votes suffice for a judgment or proposition majority.

The authorized entering-law C slice carries the §61 attribution setting and the actual simulated holdings in Burke, Schleier and O'Gilvie. Earl and Horst govern retained-source attribution. The October 22, 2004 enactment is current noncase law, with §703(c)'s prospective conditions. Its separate admission must be linked by the assembling operator before final validation. No January 24 event supplies antecedent law. Prior same-term arrest, counsel and sentencing decisions supply no changed material premise for this tax question.

## Stone's fixed position and final compatibility

The approved Section II dated November 22, 2026 expressly supports reversal in both dockets, gross inclusion under retained-claim agency principles, the separate Oregon application and calculation under the actual tax-year rules. Its discretion permits nonmaterial wording only. Every proposition in the drafted Court opinion is compatible with that fixed core; the majority adopts the exclusion claimant's actual statutory-or-ownership showing, without prescribing a new evidentiary burden. The independently developed alternative theories and statutory-fee questions retain their stated preservation and record limits. Stone-Zsela joins the complete opinion and each reversal; no standing fallback is used, and no clerical correction or material narrowing is made. A separate writing would perform no additional legal work.

All eight frozen Associate commitments support the whole rule and each application. The explanation answers uncertain-value and lawyer-contribution arguments through retained ownership, and it answers Oregon priority through the lien's actual payment-security operation. It preserves the separation of inclusion and deduction. No Associate commitment changes during assembly compatibility.

## Opinion form and assignment

Form determined on legal grounds before any counts or authorship choice: one signed Court opinion for the consolidated plenary merits review. A common agency-attribution question supports one opinion, while the Oregon lien receives its distinct application and both dockets keep their separate judgments and calculations. Two substantive divisions organize attribution and the governing remand law; neither is created to affect assignment eligibility. Every participating Justice fully supports both divisions. No separate writing is required.

ASSIGNMENT_PENDING. The Chief belongs to both judgment coalitions and therefore has assignment authority. This draft has inspected no counted-opinion table and makes no author choice. Sequential assembly must recount and assign under Engine §8 before replacing AUTHOR_PENDING.

## Judgment and opinions

{banks_judgment}

{banks_topology}

## Controlling holdings

{banks_holdings}
## Precedent treatment

{banks_precedent}
## Law after decision and continuity

Ordinary contingent-fee arrangements retaining client ownership and control now receive a uniform §61 attribution rule, including direct payment and state-law fee security that leaves agency intact. Earlier law supplied retained-source attribution but had not decided these contingent-fee applications. The new application is effective January 24, 2005. The applicable exclusion, deduction and alternative-minimum-tax provisions continue to do their separate work. The two tax proceedings return under corrected inclusion rules. There is no published noncontrolling position to register and no displaced predicate of another identified matter.

## Sources and status

Research cutoff: immediately before January 24, 2005. Facts and dates are the frozen neutral packet, corroborated by the complete primary opinion at https://www.law.cornell.edu/supct/html/03-892.ZO.html and official reporter text retained in research/chunk2-comparison/banks_official.txt. The source's historical lineup and author are comparator evidence only. The operative statutory temporal language is Public Law 108-357, §703(c), 118 Stat. 1548, at https://www.govinfo.gov/content/pkg/PLAW-108publ357/html/PLAW-108publ357.htm; the exact saved provision was read in full. The controlling simulated precedents are read from entering-law/OT_2004CHUNK2_C.md. The frozen commitments and unaffected reconciliation remain authoritative handoffs.

Completed here: both docket/coalition checks; fixed-core compatibility; all eight Associate scope checks; separate Oregon application; effective-date treatment; legal form before assignment; negative-statement review in the five specified blocks; and script identity between the internal controlling holdings and Public Projection Holdings. Pending: sequential assignment, new-enactment admission reference, canonical record placement, same-term entering-law refresh and term-wide deterministic validation. No current-state commitment is claimed. The final canonical location and commitment date are assembly responsibilities.

'''

caballes_holdings = '''### The limited exterior canine examination during an independently lawful traffic stop

**Holding and operative rule:** An exterior examination by a properly trained narcotics dog that is actually confined to detecting contraband requires no separate drug suspicion when officers have lawful access and the examination adds no unlawful restraint or other protected intrusion. The State must establish those predicates and ordinary probable cause for any later physical search; the dog's label and the later discovery of drugs do not substitute for them.

**Authority:** AUTHOR_PENDING's opinion of the Court. The common whole-opinion coalition identified in Opinion Topology adopts the rule, its qualifications, this application and the vacatur-and-remand remedy.

**Controlling explanation:** *United States v. Place*, 462 U.S. 696, distinguishes a canine examination confined to contraband from the detention that enables it. *United States v. Jacobsen*, 466 U.S. 109, distinguishes detection of contraband alone from disclosure of lawful private information. Those distinctions govern the exterior examination here.

Authority must exist for each stage. *Whren v. United States* supplies the objective traffic predicate, and *Ohio v. Robinette* requires independent grounds for restraint after traffic justification ends. *Knowles v. Iowa* requires an independent basis for a physical search following a citation. The later alert must satisfy ordinary probable-cause requirements. *City of Indianapolis v. Edmond* requires antecedent authority for a seizure before a canine examination; here the traffic offense supplies that authority. *Kyllo v. United States* protects concealed domestic information acquired by a targeted examination; the limited method here is confined to contraband.

The grant accepts the lawfulness of the traffic detention's duration. The trial court separately found this alert sufficiently reliable for probable cause. The dissenters object that a dog can err and that a compulsory drug investigation changes the encounter's character. Reliability for probable cause and the information revealed by the examination are distinct questions. A possible erroneous alert does not itself expose lawful private information; the later physical search remains subject to its own justification. On the accepted exterior-examination and lawful-duration premises, an unrelated investigative aim alone supplies neither a protected privacy intrusion nor unlawful added restraint.

The Illinois Supreme Court therefore erred in requiring separate drug suspicion solely because this examination added a drug-investigation purpose to the lawful traffic encounter.

**Operative limits:** The rule requires actual informational confinement, lawful access and lawful restraint. It does not authorize delay after traffic justification ends or entry into a protected area; physical searches retain their independent constitutional predicates. Reliability rests on the trial court's finding about this alert.
'''

caballes_precedent = '''- *United States v. Place*, 462 U.S. 696: Applied to contraband-confined detection while retaining its independent limits on detention.
- *United States v. Jacobsen*, 466 U.S. 109: Applied for the distinction between contraband-only information and lawful private contents; constitutional classification remains separate from a later physical search.
- *Whren v. United States*, 517 U.S. 806: Applied to the independently justified traffic stop, preserving separate manner, scope and duration limits.
- *Ohio v. Robinette*: Preserved for the requirement of independent authority when traffic justification ends; lawful initial detention supplies no continuing authority by itself.
- *Knowles v. Iowa*, 525 U.S. 113: Preserved for the independent justification required for a physical search following a traffic citation.
- *City of Indianapolis v. Edmond*, 531 U.S. 32: Distinguished because the present traffic offense supplies the seizure authority absent from the narcotics checkpoint; the canine-classification question reserved there is resolved here for this defined setting.
- *Kyllo v. United States*, 533 U.S. 27: Distinguished because its examination acquired concealed lawful domestic information. Its protection of that information and its separate warrant requirement remain in force.
'''

caballes_separates = '''**Souter, dissenting:** The dog was used to investigate concealed effects and to establish grounds for opening the trunk. Souter would treat that investigative examination as a search requiring an independent lawful basis beyond the speeding detention. *Place* supplies a special privacy distinction only when the method is genuinely confined to contraband; sufficient reliability for probable cause does not establish the absolute informational exemption asserted here. *Jacobsen* concerned a test of material already lawfully obtained, whereas this examination began an investigative process directed at a closed enclosure. *Kyllo* supports scrutiny of acquisition of concealed information, and *Edmond* requires authority for the actual intrusion. Souter accepts the individual reliability finding but rejects its use to settle constitutional classification. He would affirm suppression and also joins Ginsburg's separate seizure ground.

**Ginsburg, dissenting, joined by Souter:** A traffic seizure is limited in scope as well as time. The compulsory canine investigation materially expands that seizure from traffic enforcement to a drug inquiry, even though the accepted duration remains lawful. *Robinette* preserves the limited authority conferred by the traffic encounter, *Edmond* distinguishes ordinary crime investigation from an independently justified seizure, and *Knowles* rejects treating a citation as general search authority. Ginsburg agrees that probable-cause reliability does not by itself establish an all-purpose contraband-only exemption, but her sufficient ground concerns the scope of this seizure. She would require articulable drug suspicion for the added investigation and affirm the Illinois judgment. Her agreement with the limited privacy objection is not a whole-opinion join in Souter's separate search rationale.
'''

caballes_event = '''Illinois v. Caballes, No. 03-923; 543 U.S. 405. Merits decision, January 24, 2005. Argued November 10, 2004. On writ of certiorari to the Supreme Court of Illinois, 207 Ill. 2d 504, 802 N.E.2d 202.

A trooper stopped Caballes for speeding. During the traffic business another officer walked a narcotics dog around the car; its alert led to a trunk search and discovery of marijuana. The trial court found the duration lawful and the alert sufficiently reliable for probable cause. The Illinois Supreme Court reversed the conviction because the canine examination expanded the investigation without reasonable, articulable drug suspicion. The granted question accepts lawful traffic duration and asks whether the Fourth Amendment independently requires that suspicion for this exterior examination. Illinois seeks removal of that requirement; Caballes seeks preservation of suppression.'''

caballes_judgment = f'''**Vacated and remanded, 7–2.**

**Supporting:** {majority_names}.
**Opposing:** Souter and Ginsburg.

The state court must apply the limited nonsearch rule to the accepted lawful-stop premises and resolve genuinely preserved independent grounds. If no independent defect remains, lack of separate drug suspicion does not justify excluding the evidence.'''

caballes_topology = f'''| Writing | Author | Full support or joins | Relationship to judgment and scope |
|---|---|---|---|
| Opinion of the Court | AUTHOR_PENDING | {majority_names}; each Justice other than the author joins in full | Complete limited nonsearch rule, application and vacatur-and-remand remedy |
| Search-ground dissent | Souter | Souter | Would affirm suppression because the examination is a search lacking an independent lawful basis |
| Seizure-scope dissent | Ginsburg | Souter joins in full | Would affirm because the compulsory investigation materially expands the limited traffic seizure |'''

caballes_internal = f'''**Case and dockets:** Illinois v. Caballes, No. 03-923.
**Event and date:** Merits decision; 2005-01-24; October Term 2004, chunk 2.
**Result:** Draft substantive resolution: vacate the Illinois Supreme Court's judgment and remand, 7–2.
**Version / lineage:** Assembly preparation draft only; supersedes no adjudication and supplies no current law. AUTHOR_PENDING and ASSIGNMENT_PENDING require sequential assembly completion.

## Event, chronology and record

{caballes_event}

The stop occurred November 12, 1998. Its date creates no independent reliance defense. The accepted lawful-duration and individualized-reliability findings are retained, with no universal factual claim about dogs and no additional historical fact reconstructed. The constitutional question addresses the canine examination itself. The federal basis of the state judgment permits certiorari review; genuinely independent preserved state-law protection remains for the state court.

## Participation and entering law

All nine members participate at argument and decision: {all_names}. No case-specific absence or disqualification is established. The certiorari merits channel is lawful; nine participants furnish a quorum and five votes suffice for judgment or a controlling proposition.

The relevant entering-law slice contains Whren's independent initial-stop authority, Robinette's continued-restraint rule, Knowles's separate physical-search predicates, Edmond's antecedent-seizure rule and express canine-classification reservation, and Kyllo's concealed-domestic-information rule without a market-availability limitation. Place and Jacobsen retain their confined informational distinction. The same-term Devenpeck arrest rule and the sentencing decisions do not decide this search question. No January 24 event supplies antecedent law.

## Stone's fixed position and final compatibility

The approved Section II dated November 22, 2026 supports vacatur and remand under the actual-confined-detection rule, conditioned on lawful access and restraint and the independent justification for physical search. It assigns the State the actual predicates of its no-additional-intrusion claim. This is the ordinary justification inquiry already supplied by the neutral packet, not a new evidentiary procedure or an inference from discovery of contraband. The mandate preserves independently existing grounds and makes absence of drug suspicion insufficient by itself to exclude the evidence. The Chief joins the complete opinion and judgment. No standing fallback, clerical correction or substantive narrowing is used, and a separate Chief writing performs no distinct legal work.

The six supporting Associates fully join that formulation. It adopts the informational confinement and actual duration conditions their frozen positions require; neither an extra-time allowance nor general technology balancing enters the reasoning. Souter and Ginsburg retain their contrary judgments and separate sufficient grounds. Souter's reconciled commitment expressly supports the limited-seizure objection, so he joins Ginsburg's confined opinion. Ginsburg shares the reliability/privacy qualification but has no established complete commitment to Souter's broader search classification; she therefore does not join his opinion. This specifies the final compatible writings without importing historical cross-joinders or changing a frozen commitment.

## Opinion form and assignment

Form determined on legal grounds before any counts or authorship choice: one signed Court opinion resolves the recurring question after plenary argument. Its single governing proposition contains necessary access, information, restraint and later-search conditions, followed by the application and corrective remand. Two separate dissents perform distinct legal work: Souter's search classification and Ginsburg's scope-of-seizure ground. Their scopes follow their frozen commitments rather than historical opinion labels.

ASSIGNMENT_PENDING. The Chief belongs to the majority and assigns the Court's opinion. This draft has inspected no opinion counts or current assignment tables. The eligible substantive coalition is the seven members named in the Court-opinion row, all of whom fully support its propositions and remedy. The author must be selected sequentially under Engine §8 before AUTHOR_PENDING is replaced. Separate-writing attributions identify their supported substantive positions and are not counted lead assignments.

## Judgment and opinions

{caballes_judgment}

{caballes_topology}

## Controlling holdings

{caballes_holdings}
## Precedent treatment

{caballes_precedent}
## Law after decision and continuity

The Court now settles the canine-classification question for a contraband-confined exterior examination during independently lawful traffic detention. Separate reasonable drug suspicion is unnecessary when the stated predicates hold. Existing search and seizure law continues to govern lawful access, duration, additional protected intrusions and the later physical search. The Illinois judgment's categorical suspicion premise is removed; the case returns for application and disposition of genuinely independent preserved issues. No same-day case enters the doctrinal chain.

Published noncontrolling positions for future continuity are the two dissenting grounds summarized below, each effective January 24, 2005. Souter's search-classification position belongs to him alone; Ginsburg's seizure-scope position is joined by Souter. Neither changes controlling law. No later identified matter's predicate is expressly displaced.

## Separate writings and continuity propositions

{caballes_separates}
## Sources and status

Research cutoff: immediately before January 24, 2005; conduct occurred November 12, 1998. The frozen neutral packet supplies the accepted record and grant. The full primary writings at https://www.law.cornell.edu/supct/html/03-923.ZO.html, https://www.law.cornell.edu/supct/html/03-923.ZD.html and https://www.law.cornell.edu/supct/html/03-923.ZD1.html, including footnotes, and the official reporter text in research/chunk2-comparison/caballes_official.txt corroborate facts, dates and historical grounds. Historical empirical assertions, respondent concessions, authorship and cross-joins are not imported as new adjudicative premises. The actual simulated authorities come from entering-law/OT_2004CHUNK2_C.md. The frozen unaffected reconciliation confirms no material Associate departure.

Completed here: fixed-core compatibility; eight Associate scope checks; seven/two judgment arithmetic; proposition coalition; separate-writing scopes and cross-join test; legal form before assignment; negative-statement review in the five specified blocks; and script identity of internal and public Holdings. Pending: sequential assignment, canonical placement, entering-law refresh and term-wide validation. No current-state commitment is claimed; the final canonical location and commitment date remain assembly responsibilities.

'''

howell_holdings = '''### Ground of the dismissal: the actual state submission did not identify the federal claim

**Operative procedural determination:** Howell's state-law instruction argument and its indirect chain of citations did not meaningfully identify his federal constitutional claim, and the Mississippi Supreme Court did not decide that claim. The writ is dismissed as improvidently granted on that actual-record ground.

**Authority:** The Court's per curiam explanation of this dismissal applies the existing federal-presentation requirement and meaningful-notice principle to the submission before it.

**Controlling explanation:** Under 28 U.S.C. §1257, federal review of a final state judgment requires a properly reviewable federal question. *Illinois v. Gates*, 462 U.S. 213, preserves the requirement that the state court have the federal claim before it. *Baldwin v. Reese* explains meaningful notice in the exhaustion context: a constitutional provision, pertinent authority, understandable description or valid incorporation can identify the federal basis, without mandatory words. Its notice reasoning is pertinent here, while its separate habeas posture remains distinct.

Howell's state appellate argument invoked Mississippi's evidentiary rule for lesser-offense instructions. His description of an all-or-nothing choice must be read in that context. A citation to a state decision, which cited another decision that referred to *Beck v. Alabama*, did not itself identify a federal restriction on the capital verdict. The generally applicable state rule was not established as identical to the federal rule, and the state court decided the evidentiary state-law issue. Opportunity to discover another theory is different from its presentation or adjudication.

The Court therefore dismisses review. The constitutional instruction merits are not reached because the antecedent presentation requirement is unsatisfied. Whether genuinely identical state and federal standards could supply notice is left open because that premise is absent here. The jurisdictional or prudential character of the presentation requirement is also left open: the record supplies no justified exception under either treatment.
'''

howell_precedent = '''- *Illinois v. Gates*, 462 U.S. 213: Applied for the state-review requirement of actual presentation or adjudication of the federal claim.
- *Baldwin v. Reese*, 541 U.S. 27: Its meaningful-notice reasoning informs this direct-review disposition, preserving understandable identification without compulsory words and its unresolved equivalence question.
- *Beck v. Alabama*, 447 U.S. 625: Its substantive capital-instruction protection remains unchanged because the federal merits are unavailable in this review.
- *Schad v. Arizona*, 501 U.S. 624, and *Hopkins v. Reeves*, 524 U.S. 88: Their existing available-alternative and actual lesser-included-offense requirements remain in force; the Court makes no instruction-merits application here.
'''

howell_event = '''Howell v. Mississippi, No. 03-9560; 543 U.S. 440. Writ dismissed as improvidently granted, January 24, 2005. Argued November 29, 2004. On writ of certiorari to the Supreme Court of Mississippi, 860 So. 2d 704.

Howell challenged his capital murder conviction and death sentence after the trial court refused requested simple-murder and manslaughter instructions. The state court found the requested instructions unsupported under its state-law evidentiary rule. This Court granted review of the federal capital-instruction claim and expressly included whether that claim had been properly presented to or addressed by the state court for review under 28 U.S.C. §1257.'''

howell_internal = f'''**Case and dockets:** Howell v. Mississippi, No. 03-9560.
**Event and date:** Dismissal of writ as improvidently granted after plenary argument; 2005-01-24; October Term 2004, chunk 2.
**Result:** Draft substantive resolution: writ dismissed as improvidently granted; Mississippi judgment remains operative.
**Version / lineage:** Assembly preparation draft only; supersedes no adjudication and supplies no current law. No counted lead assignment is required for the reasoned per curiam dismissal.

## Event, chronology and record

{howell_event}

The charged killing occurred in May 2000; the reviewed state judgment issued in 2003. Howell disputed identity and attempted robbery and sought simple-murder and manslaughter instructions. His state appellate argument relied on state instruction cases, including an indirect chain to Beck. The actual federal-notice question comes before any instruction-merits inquiry. The supplied papers establish neither valid incorporation of a distinct federal theory nor actual federal adjudication by the Mississippi court. The posture and schedule are authorized; this federal-presentation inquiry is the judicial threshold expressly included in the grant, not a filing-verification stop.

## Participation and entering law

All nine members participate at argument and decision: {all_names}. No established case-specific absence or disqualification applies. There is a quorum. All nine internally support dismissal on the same sufficient ground; this procedural action publishes the per curiam disposition and reason without a numerical poll or named voting lineup.

The relevant entering-law slice contains Baldwin's March 2, 2004 meaningful-notice rule and its preserved equivalence question. Gates supplies the direct-state-review presentation principle. Beck, Schad and Hopkins retain their actual substantive scope should a properly presented instruction claim require decision. No same-term decision changes those premises, and no January 24 event supplies entering law.

## Stone's fixed position and final compatibility

The approved Section II dated November 22, 2026 expressly requires dismissal because the federal issue was not meaningfully presented or decided. It permits a reasoned actual-record explanation applying Baldwin's notice reasoning without making a mandatory-citation rule or treating its habeas holding as an already decided §1257 application. Stone-Zsela joins that per curiam explanation and the dismissal. The constitutional instruction merits, the broader identical-standards question and the jurisdictional characterization retain their stated limits. The state judgment remains operative. No standing fallback, clerical correction or substantive narrowing is used. Silent compliance with the prohibitions on unrequested relief creates no separate-writing function.

Every Associate's frozen commitment is compatible with this ground. Stevens's actual Baldwin dissent relied on materially different contextual federal identification; it does not require a different vote here. The draft adopts no mandatory formula and does not equate the state's understanding of Beck with this Court's constitutional merits. No Associate changes a reconciled commitment.

## Opinion form and assignment

Form determined on legal grounds before counts or an author: reasoned per curiam dismissal as improvidently granted. The actual federal-presentation defect resolves the granted review at a threshold and calls for a short institutional explanation. A signed merits opinion would misstate the act performed. No published separate opinion is necessary because all nine support this actual-record explanation. Engine §8 excludes this procedural per curiam action from counted lead opinions; no balance calculation or lead-author assignment is made.

## Public action and procedural effect

The writ is dismissed as improvidently granted. Supreme Court review ends, leaving the Mississippi judgment operative. The public action does not publish the internal modeled tally. There is no judgment on the constitutional instruction merits; that genuine nonreach follows from the unsatisfied review threshold.

## Controlling holdings

{howell_holdings}
## Precedent treatment

{howell_precedent}
## Law after decision and continuity

The existing requirement of meaningful federal presentation governs this dismissal. The Court's explanation supplies the actual-record ground rather than a new capital-instruction rule or a freestanding enlargement of Baldwin. The state judgment remains effective. No published noncontrolling position or unresolved Supreme Court proceeding is created. Independent proceedings, if lawfully brought, remain subject to their own requirements.

## Sources and status

Research cutoff: immediately before January 24, 2005. The frozen packet supplies the state-submission and review premises. The complete primary text at https://www.law.cornell.edu/supremecourt/text/543/440, including footnotes, and the official reporter text saved in research/chunk2-comparison/howell_official.txt corroborate argument and decision dates, the state citation chain and the actual state adjudication. Historical language suggesting an indispensable form of citation is not substituted for the actual Baldwin law. No historical merits position about the sentencing-stage life option is adopted. The frozen commitments and unaffected reconciliation establish the eight Associate grounds; the authorized Chief supplement supplies his fixed position.

Completed here: fixed-core compatibility; eight Associate scope checks; actual-notice and nonidentity premises; per curiam form determined independently of counts; public/private poll separation; negative-statement review in the five specified blocks; and script identity between the internal procedural determination and Public Projection Holdings. Pending: canonical placement, refreshed same-term check and deterministic term validation. No current-state commitment is claimed; final location and commitment date remain assembly responsibilities.

'''

def projection(event, action, judgment, topology, holdings, precedent, law, separate, procedure, sources, participation=None):
    blocks = [
        ('Event', event),
        ('Participation', participation or f'All nine Justices participate: {all_names}.'),
        ('Public Action', action),
        ('Judgment & Remedy', judgment),
        ('Opinion Topology', topology),
        ('Holdings', holdings.strip()),
        ('Precedent Treatment', precedent.strip()),
        ('Law After Decision', law),
        ('Separate Writings', separate),
        ('Procedure After Action', procedure),
        ('Source Notes', sources),
    ]
    return '## Public Projection\n\n' + '\n\n'.join('### ' + title + '\n\n' + body for title, body in blocks).rstrip() + '\n'

banks_public = projection(
    banks_event,
    'The judgments of the Sixth and Ninth Circuits are reversed, and both cases are remanded.',
    banks_judgment,
    banks_topology,
    banks_holdings,
    banks_precedent,
    'The full otherwise taxable recovery is attributed to the client in ordinary contingent-fee representation that preserves client ownership and ultimate control, including arrangements with direct payment and a superior payment lien. Exclusions and deductions depend on their own statutory requirements. Each liability is calculated under its governing tax-year rules.',
    '',
    'Both tax cases return for further proceedings consistent with the inclusion rule. Each court must calculate the affected liability from the actual payment and return records under the applicable tax-year law.',
    'Nos. 03-892 and 03-907; 543 U.S. 426. Judgments below: 345 F.3d 373 and 340 F.3d 1074. 26 U.S.C. §§61, 62, 67–68 and 56(b)(1)(A)(i); American Jobs Creation Act of 2004, Pub. L. 108-357, §703, 118 Stat. 1546–1548. Banks\'s settlement paid the contractual contingent fee without a separately awarded statutory fee or an established fee payment in its place.'
)

caballes_public = projection(
    caballes_event,
    'The Illinois Supreme Court\'s judgment is vacated, and the case is remanded.',
    caballes_judgment,
    caballes_topology,
    caballes_holdings,
    caballes_precedent,
    'A contraband-confined exterior canine examination during an independently lawful traffic detention requires no separate drug suspicion when the State establishes the stated access, information and restraint predicates. Existing search and seizure rules independently govern detention duration, protected intrusions and the physical search following an alert.',
    caballes_separates.strip(),
    'The case returns to the Illinois courts to apply the corrected federal rule to the accepted lawful-stop premises and resolve genuinely preserved independent grounds. If no independent defect remains, the absence of separate drug suspicion supplies no basis for suppression.',
    'No. 03-923; 543 U.S. 405. Judgment below: 207 Ill. 2d 504, 802 N.E.2d 202. U.S. Const., amend. IV. The granted question accepts lawful traffic duration and absence of independent drug suspicion. The trial court found this alert sufficiently reliable for probable cause.'
)

howell_public = projection(
    howell_event,
    'The writ of certiorari is dismissed as improvidently granted because Howell\'s federal instruction claim was neither meaningfully presented to nor addressed by the Mississippi Supreme Court. The Court issues a reasoned per curiam disposition without publishing a voting tally.',
    'The dismissal ends this review and leaves the Mississippi judgment operative.',
    'Per curiam opinion explaining dismissal of the writ as improvidently granted.',
    howell_holdings,
    howell_precedent,
    'The meaningful-presentation requirement governs this review. The existing substantive rules for capital lesser-included-offense instructions remain in force, with a supported noncapital alternative assessed under Beck, Schad\'s available-alternative analysis and Hopkins\'s requirement of an actual lesser-included offense.',
    '',
    'Proceedings on this writ are concluded. The Mississippi judgment remains operative, subject to the requirements of any independently available lawful proceeding.',
    'No. 03-9560; 543 U.S. 440. Judgment below: 860 So. 2d 704. 28 U.S.C. §1257; U.S. Const., amends. VIII and XIV. The pertinent state appellate submission argued the state evidentiary instruction rule; the state decision addressed that issue.'
)

for name, internal, start, public, holdings in [
    ('BANKS', banks_internal, '## Commissioner v. Banks and Commissioner v. Banaitis', banks_public, banks_holdings),
    ('HOWELL', howell_internal, '## Howell v. Mississippi', howell_public, howell_holdings),
    ('CABALLES', caballes_internal, '## Illinois v. Caballes', caballes_public, caballes_holdings),
]:
    text = internal + audit(name, start) + '\n' + public
    path = base / f'runtime/OT_2004CHUNK2_DRAFT_{name}.md'
    path.write_text(text, encoding='utf-8')
    # The identical string supplies both internal kernel and downstream block.
    assert text.count(holdings.strip()) == 2, name
    projection_text = text.split('## Public Projection\n', 1)[1]
    headings = re.findall(r'^### (Event|Participation|Public Action|Judgment & Remedy|Opinion Topology|Holdings|Precedent Treatment|Law After Decision|Separate Writings|Procedure After Action|Source Notes)$', projection_text, re.M)
    assert headings == ['Event', 'Participation', 'Public Action', 'Judgment & Remedy', 'Opinion Topology', 'Holdings', 'Precedent Treatment', 'Law After Decision', 'Separate Writings', 'Procedure After Action', 'Source Notes'], (name, headings)
    print(f'{name}: wrote draft; eleven-block order and exact internal/public holdings identity verified')
