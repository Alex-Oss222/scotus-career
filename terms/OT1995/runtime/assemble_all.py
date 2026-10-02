from pathlib import Path
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[3]
TERM = ROOT / 'terms/OT1995'
OUT = TERM / 'runtime/assembly'
OUT.mkdir(exist_ok=True)
NAME = 'American_Life_League_v_Reno_merits_1995-11-13'
ALL = ['Stone-Zsela', 'Stevens', "O'Connor", 'Scalia', 'Kennedy', 'Souter', 'Thomas', 'Ginsburg', 'Breyer']
ASSOC = ALL[1:]
RFRA = ["O'Connor", 'Scalia', 'Kennedy', 'Souter', 'Thomas']
AFFIRM_RFRA = ['Stone-Zsela', 'Stevens', 'Ginsburg', 'Breyer']
SMITH = ['Stevens', 'Scalia', 'Kennedy', 'Thomas', 'Ginsburg', 'Breyer']
BLOCKS = ['Event','Participation','Public Action','Judgment & Remedy','Opinion Topology','Holdings','Precedent Treatment','Law After Decision','Separate Writings','Procedure After Action','Source Notes']

def names(items):
    return ', '.join(items)

def writing(author, supporters, scope, controlling=True):
    return dict(author=author, joiners=[j for j in supporters if j != author], scope=scope, controlling=controlling)

inputs = [
    'freeze/OT_1995CHUNK1_ALL_TEXT_NEUTRAL_SUPPLEMENT.md',
    'freeze/OT_1995CHUNK1_ALL_TEXT_REFRESH_COMMITMENTS.md',
    'freeze/OT_1995CHUNK1_ALL_TEXT_RECONCILED.md',
    'freeze/ALL_TEXT_RECONCILIATION_RECEIPT.json',
    'freeze/ALL_TEXT_REFRESH_CONTEXT_CLARIFICATION.md',
    'freeze/OT_1995CHUNK1_B_RECONCILED.md',
    'freeze/OT_1995CHUNK1_B_NEUTRAL_VALIDATED.md',
    'freeze/OT_1995CHUNK1_B_STONE_INPUT.md',
    'freeze/OT1994_ASSIGNMENT_REVIEW.md',
    'entering-law/OT_1995CHUNK1_B.md',
    'entering-law/OT_1995CHUNK1_B_SUPPLEMENT.md',
    'sources/B_AMERICAN_LIFE_LEAGUE_OBJECTIVE_SOURCE_ADDENDUM.md',
    'sources/preflight_b/B_FACE_1994.txt',
    'entering-law/PUBLIC_Wood_v_Bartholomew_summary_merits_1995-10-10.md',
    'entering-law/PUBLIC_Doe_v_Taylor_ISD_merits_1995-10-16.md',
    'entering-law/PUBLIC_Hodge_v_Jones_merits_1995-10-23.md',
]
hashes = {p: hashlib.sha256((TERM/p).read_bytes()).hexdigest() for p in inputs}
assert hashes['freeze/OT_1995CHUNK1_ALL_TEXT_RECONCILED.md'] == '648a1c4e8cfbe1add1db2f6dd750676431d951f7771738783e40f760ac7371eb'

statute = '''The challenged reproductive-service provisions of the Freedom of Access to Clinic Entrances Act, 18 U.S.C. §248, apply to conduct on or after May 26, 1994. Section (a)(1) requires force, threat of force or physical obstruction; intentional injury, intimidation, interference or attempt; and either action because a person is or has been obtaining or providing reproductive health services, or action intended to intimidate that person, another person or a class from doing so. Section (a)(3)'s challenged branch separately covers intentional damage or destruction of a facility's property, or attempt, because the facility provides those services. The parallel worship branches are outside this review.

Interference means restricting freedom of movement; intimidation means reasonable apprehension of bodily harm to oneself or another; physical obstruction means making ingress to or egress from a reproductive-service facility or place of worship impassable, or passage to or from it unreasonably difficult or hazardous. Services include medical, surgical, counseling and referral services relating to reproduction, pregnancy or its termination, provided in a hospital, clinic, physician's office or other facility. The inclusive facility definition covers those reproductive-service establishments and the building or structure in which the facility is located; it does not separately add grounds or worship premises. The passage provisions do not depend on that addition and create no indoor-only limit or outdoor immunity. A parent or legal guardian is exempt from **all penalties and civil remedies under §248**, including private damages and governmental or private injunctions, for the described activities insofar as they are directed **exclusively at that minor**. This grants no immunity under other law or constitutional parental veto.

The ordinary criminal maximum is one year for a first offense and three years after a prior conviction under the section, with the applicable title 18 fine or both. Exclusively nonviolent physical obstruction instead carries maxima of six months and $10,000 for the first offense, and eighteen months and $25,000 for a subsequent offense, with imprisonment, fine or both. If bodily injury results, imprisonment may reach ten years; if death results, any term of years or life. No criminal sentence is before the Court.

An aggrieved person's §248(a)(1) civil action is limited to persons providing or seeking to provide, or obtaining or seeking to obtain, services in a reproductive-health facility. A court may award appropriate injunctive relief, compensatory and punitive damages, costs and reasonable attorney and expert fees. Before final judgment, the claimant may elect $5,000 per violation in lieu of actual compensatory damages. All of these remedies remain subject to the full parent/guardian exception. Federal enforcement requires the Attorney General's reasonable cause to believe a person or group is being, has been or may be injured by a violation; state Attorneys General may proceed on that basis as parens patriae for natural-person residents. Government civil relief may include injunctions and compensation; civil-penalty maxima are $10,000 for a first nonviolent obstruction and $15,000 for a subsequent one, or $15,000 and $25,000 for other first and subsequent violations. These are distinct from private elected damages and criminal punishment. The unchallenged §248(a)(2) branch concerns force, threats or obstruction of lawful religious exercise at a place of worship; its private action is limited to persons lawfully exercising or seeking that right or the entity owning or operating the place. Section (a)(3) separately addresses worship-property damage or destruction; these branches are described, not adjudicated.

Section 248(d) preserves First Amendment-protected expressive conduct, including peaceful picketing and demonstrations; creates no new remedy for interference with protected speech or religious exercise outside a facility, regardless of viewpoint, and limits no existing remedy; makes neither penalties nor civil remedies exclusive and preempts no state or local penalties or remedies; and does not interfere with state or local regulation of abortion or other reproductive services. Severability covers provisions and applications. None of these clauses alone establishes the validity of every possible enforcement.'''

holdings = []
explanations = {}
def holding(title, rule, authority, explanation, treatment):
    if title == 'Elected statutory damages are not categorically barred by the First Amendment':
        rule = rule.replace('An eligible claimant', 'For conduct outside the parent/legal-guardian exception, an otherwise eligible claimant')
        explanation += ' No private damages, elected sum, injunction or other FACE civil remedy is available when the actor is the minor\'s parent or legal guardian and the described activity is directed exclusively at that minor; no qualifying application is found here.'
    if title == 'RFRA requires further adjudication of the prospective-enforcement claim':
        explanation = explanation.replace('including proper consideration of the parent/minor qualification.', 'including the parent/minor exception\'s complete exclusion of penalties and civil remedies, even preventive FACE injunctions. That exclusion defeats a premise of universal access enforcement and requires a genuine comparison; it does not itself establish that an outsider blockade and the exclusively parent-to-own-minor relation are comparable. No equivalent state remedy is presumed.')
    if title == 'The presented facial religious-targeting claim fails':
        explanation += ' Congress withheld even preventive FACE civil relief for qualifying own-minor conduct. The Court weighs that full distinction, not a lesser-penalty exception; it establishes no universal rule that family status defeats comparison and no fact about a plaintiff\'s qualification in a different encounter.'
    explanations[title] = len(re.findall(r"\S+", explanation))
    holdings.append(f'### {title}\n\n**Holding and operative rule:** {rule}\n\n**Authority:** {authority}\n\n**Controlling explanation:** {explanation}\n\n**Precedent treatment:** {treatment}')

holding('Congress may protect this medical-services market',
    'Congress may regulate the challenged class of targeted force, threats, physical obstruction and facility destruction directly interfering with provision or receipt of reproductive health services in an interstate medical-services market. The absence of a separate interstate-crossing element for each actor does not defeat this class-based ground; direct regulation of private conduct also presents no compelled state legislation or administration.',
    'Kennedy, Part I, joined by Stone-Zsela, Stevens, O\'Connor, Scalia, Souter, Thomas, Ginsburg and Breyer: nine direct votes.',
    'The Court distinguishes the commercial service being obstructed from the objector\'s ideological purpose. Lopez rejects the remote chain from stand-alone school firearm possession through education and productivity; it does not disable protection of an actual services market. Harris applies the retained economic-class principle, while preserving the particular-vehicle nexus Congress enacted there. Reported legislative evidence here concerns interstate patients, personnel and supplies, and actual loss of service through obstruction and closure. That connection is direct, rather than a general crime-cost theory. Local participation does not sever the regulated class from its commercial setting. Robertson confirms the significance of actual commercial operation without making every protester an interstate enterprise. The Court adds no element Congress omitted, treats no legislative statistic as conclusive, and adopts no exhaustive commerce formula. The separate persons-or-things-in-commerce theory and Fourteenth Amendment §5 ground need not be decided. New York\'s anti-compulsion rule remains intact: FACE regulates private actors rather than ordering States to legislate or administer a federal program.',
    'Lopez (April 26, 1995) is distinguished at its inadequate downstream-effects chain; Harris (April 27, 1995) supplies the bounded economic-class ground; Robertson (May 1, 1995) remains a distinct direct-enterprise holding; New York v. United States (June 19, 1992) retains its anti-compulsion limit.')

holding('The defined access restrictions survive the facial speech challenge',
    'FACE\'s challenged service-related force, threat, obstruction and intentional-property-damage provisions, with their physical-harm definitions, intent and alternative service-related motives, regulate access-related conduct without selecting a protected message. When that conduct is expressive, the provisions satisfy intermediate scrutiny because they advance substantial access and safety interests unrelated to suppression and do not burden substantially more speech than necessary, while leaving usable nonobstructive communication.',
    'Kennedy, Part II, joined by every other Justice: nine direct votes.',
    'Both motive branches concern obtaining or providing services, not an antiabortion message or religious belief. Reproductive services include carrying pregnancy to term, counseling and referral as well as termination. Mitchell permits relevant motive to accompany independently proscribable conduct; it does not eliminate scrutiny of peaceful expressive obstruction. Under O\'Brien and Ward, protecting passage and bodily safety is substantial and nonsuppressive. The law addresses impassable or unreasonably difficult or hazardous passage, force, threats and destruction, while preserving nonobstructive prayer, signs, leafleting, demonstrations and willing conversation. It imposes no numerical buffer, advance invitation requirement or compulsory silence. Turner requires examination of actual selection and fit; a benign purpose alone would not suffice. The connection between obstruction and denied access is direct here. Labor or environmental views receive no general exemption: coverage depends on the enacted purpose and physical predicates. The parent/guardian exception covers penalties and civil remedies only for conduct directed exclusively at the actor\'s own minor; it neither selects an abortion viewpoint nor permits general interference with other patients. Madsen\'s more demanding injunction standard and case-specific distances are not transplanted to this statute. Hurley protects private expressive composition, which is not compelled here. Discriminatory enforcement and materially different mixed-motive applications remain open.',
    'Mitchell (June 11, 1993) supplies motive/conduct and protected-belief limits; O\'Brien and Ward supply ordinary intermediate review; Turner (June 27, 1994) supplies classification and fit; Madsen (June 30, 1994) is distinguished as injunction review; Hurley (June 19, 1995) remains a private-expression holding.')

holding('The presented substantial-overbreadth challenge fails',
    'The intentional-act and service-related-purpose requirements, defined physical access or bodily-harm predicates, and textually available protection for First Amendment expression do not reach substantial protected expression relative to FACE\'s legitimate sweep on this facial challenge. Political offense, successful persuasion and abstract belief alone are not statutory violations; protected expression cannot become punishable merely because it supplies evidence of a legally relevant motive.',
    'Kennedy, Part III-A, joined by every other Justice: nine direct votes.',
    'R.A.V. invalidates substantial protected coverage that permissible construction cannot cure. Its controlling rule concerns overbreadth, not the separate proposed content-selection theory within unprotected categories. FACE\'s enacted definitions restrict interference to movement and intimidation to reasonable apprehension of bodily harm. Section 248(d)(1) reinforces those available limits rather than supplying an unexplained assurance of validity. Mitchell distinguishes speculative future evidentiary chilling from a statute that directly punishes protected belief. Relevant statements remain subject to ordinary safeguards, and abstract belief is not itself an offense. True threats of force remain distinct from harsh political hyperbole. The Court announces no universal threat mental-state rule and adjudicates no uncharged statement; an application that actually punishes protected advocacy remains challengeable.',
    'R.A.V. (June 22, 1992) is applied at its controlling substantial-overbreadth rule, with its distinct content-selection opinion left noncontrolling; Mitchell preserves relevant-motive evidence and the bar on abstract-belief punishment.')

holding('The defined conduct is not facially vague',
    'FACE\'s movement, passage and reasonable-apprehension-of-bodily-harm definitions, together with intentional conduct and the required service-related purpose, provide ascertainable boundaries sufficient to reject the presented facial due-process vagueness claim. Mere offense, disagreement, resentment or persuasion does not satisfy those predicates.',
    'Kennedy, Part III-B, joined by Stevens, O\'Connor, Scalia, Souter, Thomas, Ginsburg and Breyer: eight direct rationale votes. Stone-Zsela joins this component\'s disposition only.',
    'The challenged words operate within definitions of physical effects and an intentional service-related act, rather than an unrestricted prohibition of upsetting political debate. Whether passage is impassable or unreasonably difficult or hazardous is a conduct boundary; apprehension must concern bodily harm and be reasonable. Cameron supports the intelligibility of physical-obstruction restrictions in their statutory setting. R.A.V. did not decide vagueness, and its overbreadth holding is not substituted for this inquiry. Particular enforcement questions remain possible, but they do not establish that this enacted scheme lacks facially intelligible limits. No person\'s criminal liability or specific threatening statement is decided.',
    'Cameron v. Johnson is applied to the defined physical-obstruction setting; R.A.V.\'s express vagueness reservation remains intact.')

holding('Elected statutory damages are not categorically barred by the First Amendment',
    'An eligible claimant may elect §248(c)(1)(B)\'s $5,000 per violation before final judgment in lieu of actual compensatory damages; the First Amendment does not categorically require such violation-based statutory damages to equal proved actual loss. This rejects the categorical remedy challenge without deciding the reasonableness of that amount, a particular entitlement or award, the number of violations, punitive damages or a criminal sentence.',
    'Kennedy, Part IV-A, joined by all seven other Associates: eight direct rationale votes. Stone-Zsela agrees in rejecting the categorical speech challenge without adding a statutory-damages theory.',
    'Claiborne forbids charging a defendant for protected persuasion and the unlawful acts of others without the necessary attribution; it does not categorically forbid a legislatively selected substitute for actual compensatory loss caused by an attributable statutory violation. The election is permissive, occurs before final judgment and replaces actual compensatory damages, not every other available remedy. A hypothetical mixed campaign does not establish that the statute requires damages for its protected portion. No award exists to review here, and the amount\'s reasonableness was expressly outside the lower decision. Those questions remain distinct from the categorical contention.',
    'NAACP v. Claiborne Hardware Co. is applied to responsibility and protected persuasion, without extending it into a categorical ban on elected statutory damages.')

holding('A damages defendant must be responsible for the violation',
    'FACE liability must rest on a defendant\'s legally attributable violation; shared belief, organizational membership, independent advocacy or another person\'s unlawful act alone does not establish that liability. Protected persuasion that reduces demand cannot itself supply the unlawful injury for an award.',
    'Kennedy, Part IV-B, joined by every other Justice: nine direct votes.',
    'Claiborne preserves responsibility for unlawful conduct while protecting association and persuasion. Those requirements remain operative when a legislature permits statutory damages. An injunction\'s actual-concert principle is not a substitute for the legal predicates of a damages action. Madsen similarly does not permit an injunction to bind a viewpoint or independent advocate merely by association. The Court adjudicates no organizational attribution, civil conspiracy, actual-concert finding or individual award in this pre-enforcement case.',
    'Claiborne\'s attribution rule is preserved; Madsen\'s responsible-party and actual-concert limits are retained within injunction procedure and do not become a new damages theory.')

holding('The presented facial religious-targeting claim fails',
    'The challenged text does not establish religious targeting or a substantial exemption for comparable general secular blockades: its predicates concern service-related acts and access, not religious identity. Its parent/guardian exception for penalties and civil remedies reaches conduct directed exclusively at that person\'s own minor and does not itself establish that outsiders may obstruct other persons\' access on secular grounds.',
    'Kennedy, Part V-A, joined by all seven other Associates: eight direct rationale votes. Stone-Zsela joins the constitutional free-exercise disposition only.',
    'Lukumi requires scrutiny of objective text, exemptions and operation, including comparable secular harm. Religious prominence among opponents does not alone prove targeting, just as a secular description of purpose would not defeat an actually discriminatory scheme. FACE does not exempt labor or environmental viewpoints from its enacted predicates; conduct with a different object may fall outside them. The limited own-minor relationship does not resemble the substantial secular underinclusion in Lukumi. The Court rejects the presented facial inference, without deciding discriminatory enforcement or declaring the exception irrelevant to RFRA\'s separate application-specific inquiry.',
    'Lukumi (June 11, 1993) is applied at its objective-targeting and comparable-secular-harm holdings, without turning its noncontrolling legislative-purpose discussion into the governing test.')

holding('The broader constitutional exemption is rejected on the pleaded frame',
    'Under Smith\'s constitutional neutral-law rule as bounded by Lukumi, the asserted religious obligation to engage in the covered physical obstruction supplies no constitutional exemption on the pleaded frame after the presented targeting and comparable-secular-exemption challenges fail. This conclusion does not dispose of RFRA, decide every different application or overrule any constitutional protection against discriminatory enforcement.',
    'Kennedy, Part V-B, joined by Stevens, Scalia, Thomas, Ginsburg and Breyer: six direct rationale votes. O\'Connor and Souter reserve this broader question; Stone-Zsela supplies a disposition-only vote and no ground.',
    'Smith distinguishes a neutral, generally applicable conduct rule from a law singling out religious exercise, and Lukumi preserves the objective targeting and comparability inquiry. On this pleading, the asserted exemption from the defined conduct prohibition does not follow as a constitutional matter. The parent/guardian qualification is retained with its own-minor and exclusive-direction limits; it is not a general secular blockade entitlement. Congress has independently imposed RFRA\'s more demanding standard, which remains fully applicable and requires the separate disposition below. The Court neither decides RFRA\'s constitutionality nor substitutes this constitutional rule for its statutory burden sequence.',
    'Smith remains the constitutional neutral-law rule; Lukumi retains its targeting and general-applicability limits; Clearwater and Swanner require the separate statutory inquiry.')

holding('RFRA requires further adjudication of the prospective-enforcement claim',
    'The dismissal of the RFRA prospective-enforcement claim is vacated. The district court must identify each live claimant and threatened application, determine a genuinely contested substantial burden, and, if the burden is established, require the government to produce evidence and persuade that applying it to that person furthers a compelling interest by the least restrictive means, considering concrete alternatives and legally comparable exceptions.',
    'O\'Connor\'s RFRA opinion, joined by Scalia, Kennedy, Souter and Thomas: five direct votes for the rule, its application and vacatur/remand. Stone-Zsela, Stevens, Ginsburg and Breyer dissent from that disposition.',
    'Clearwater and Swanner require a distinct inquiry into the actual person and application. The Court assumes the sufficiently pleaded religious burden solely to review dismissal; the government disputes it and no sincerity or doctrinal-necessity finding is made. General appeals to access, health and safety, even with successful intermediate speech scrutiny, do not complete RFRA\'s least-restrictive-means showing. Reliable medical access and bodily safety carry compelling weight, and an accommodation may fail because it leaves the very access injury the statute prevents. But this generalized dismissal did not complete that showing for the claimants\' actual conduct and legally material alternatives, including proper consideration of the parent/minor qualification. The government bears production and persuasion; claimants do not bear a universal duty to prove an alternative. Remand neither requires a hearing whenever religion is asserted nor grants an entitlement to block a clinic or divert patients elsewhere. A claim may fail on its actual pleadings and a sufficient showing, or at the substantial-burden threshold. RFRA applies to later federal enactments unless expressly excluded by reference, and FACE contains no such exclusion. Ordinary standing, appropriate relief, religious-belief protection and the Establishment Clause remain. The statute stays in force; no injunction or final exemption follows.',
    'Clearwater (December 5, 1994) and Swanner (March 27, 1995) are applied without changing their burden sequence or treating third-party harm as irrelevant; Smith does not replace RFRA; Lee and Roberts retain the weight of direct injury without creating a categorical exception to the statute.')

common_scope = '''Every holding below retains the following enacted qualifications. A parent or legal guardian of a minor is subject to **no penalty or civil remedy under §248** for the described activities insofar as they are directed **exclusively at that minor**; this includes private damages and private or governmental injunctive relief. No FACE civil remedy survives for that excepted conduct. Other law is not preempted, but no equivalent state remedy, general parental immunity or constitutional veto is presumed.

The facility definition **includes** a hospital, clinic, physician's office or other reproductive-service facility and the building or structure in which it is located; it adds neither grounds nor worship premises. The separate physical-obstruction definition covers impassable ingress or egress, or unreasonably difficult or hazardous passage, **to or from** a service facility or place of religious worship. The worship branches remain unchallenged. These distinct provisions establish no property-line rule, new buffer, interior-only prohibition or immunity for all outdoor conduct. Section 248(d)(1)'s protected-expression limitation and (d)(2)'s separate preservation of outside-facility speech/religion remedies retain their own terms.'''
HOLDINGS = common_scope + '\n\n' + '\n\n'.join(holdings)

topology = '''| Writing / portion | Author | Joins at the stated level | Status |
|---|---|---|---|
| Parts I, II, III-A and IV-B: commerce/federalism, speech, overbreadth and attribution | Kennedy | Stone-Zsela, Stevens, O'Connor, Scalia, Souter, Thomas, Ginsburg, Breyer | Opinion of the Court, nine |
| Parts III-B, IV-A and V-A: vagueness, elected-damages rationale and facial religious targeting | Kennedy | Stevens, O'Connor, Scalia, Souter, Thomas, Ginsburg, Breyer | Opinion of the Court, eight; Stone-Zsela agrees only in the relevant dispositions |
| Part V-B: broader constitutional exemption | Kennedy | Stevens, Scalia, Thomas, Ginsburg, Breyer | Opinion of the Court, six; O'Connor and Souter reserve the question |
| RFRA rule, application and remand | O'Connor | Scalia, Kennedy, Souter, Thomas | Opinion of the Court, five |
| Constitutional-exemption reservation | O'Connor | Souter | Concurrence in part; no new constitutional rule |
| RFRA application and opposition to remand | Stone-Zsela | Stevens, Ginsburg, Breyer | Dissent in part; accepts RFRA's governing standard |

Stone-Zsela joins the disposition only on the constitutional free-exercise and due-process vagueness components, adding no ground. His rejection of the categorical damages speech challenge adds no general statutory-damages rationale; he joins the stated attribution limit. O'Connor and Souter agree with the facial constitutional judgment while reserving the broader exemption question. Every controlling proposition has the direct majority identified above; no combination of distinct opinions supplies an additional rule.'''

judgment = '''The Fourth Circuit's judgment is **affirmed in part, vacated in part, and remanded**.

| Component | Disposition | Supporting | Opposing | Count |
|---|---|---|---|---|
| Presented facial constitutional challenges: commerce/federalism, speech and overbreadth, due-process vagueness and constitutional free exercise | Affirm dismissal | Stone-Zsela, Stevens, O'Connor, Scalia, Kennedy, Souter, Thomas, Ginsburg, Breyer | No opposition | 9–0 |
| Categorical First Amendment objection to elected statutory damages, with attribution limits | Affirm dismissal | Stone-Zsela, Stevens, O'Connor, Scalia, Kennedy, Souter, Thomas, Ginsburg, Breyer | No opposition | 9–0 |
| RFRA prospective-enforcement claim | Vacate dismissal and remand for the separate statutory inquiry | O'Connor, Scalia, Kennedy, Souter, Thomas | Stone-Zsela, Stevens, Ginsburg, Breyer | 5–4 |

The district court must identify the live person-and-application claim, resolve a genuinely contested substantial burden, and, if necessary, require the government's compelling-interest and least-restrictive-means showing. The remaining dismissals stay in place. FACE remains operative; the Court grants no exemption, injunction, damages, penalty or finding of unlawful conduct. The unchallenged worship branches, the reasonableness of the elected amount and any particular award remain outside this judgment. A materially different application has its own claim and ordinary procedural requirements.'''

separates = '''**O'Connor, joined by Souter, concurring in part.** They join the rejection of demonstrated facial targeting, the commerce and speech holdings and the RFRA remand. They do not join Part V-B's broader constitutional rejection under Smith. Their respective Lukumi positions preserve the substantial-burden constitutional question and reconsideration of Smith's foundation; the statutory remand makes its resolution unnecessary here. They recognize the own-minor exception's actual limits and do not create a constitutional exemption, invalidate FACE or dispute the present facial constitutional disposition. Their RFRA inquiry leaves open a justified denial of an exemption on a sufficient claimant-specific showing.

**Stone-Zsela, joined by Stevens, Ginsburg and Breyer, dissenting in part.** They accept Clearwater and Swanner as governing and would affirm the RFRA dismissal on the pleaded assumption that religious exercise requires the defined physical obstruction. Their disagreement concerns whether that application already supplies sufficient justification, not RFRA's validity, burden sequence or the weight of religious exercise. Allowing the requested outsider obstruction would leave the affected person facing impassable or unreasonably difficult or hazardous access because of another person's religious choice. A violence-only rule leaves deliberate blockage untouched; later damages cannot restore a missed service. Nonobstructive prayer, counseling, signs, demonstrations and persuasion remain available. Notice, referral or a demand that the patient find another route does not preserve the same access in the affected encounter.

The parent/guardian exception removes penalties and every civil remedy, including preventive FACE injunctions, for the covered conduct directed exclusively at that person's own minor. This defeats any claim of universally overriding federal access enforcement. It does not, however, supply the asserted outsider exemption for obstruction directed at other service-seekers: the exclusive relationship and target, not supposed surviving civil FACE relief, supply the distinction. The dissent neither validates abuse nor presumes an equivalent state remedy. It reserves a genuinely qualifying parent/guardian application and makes no finding that a named plaintiff has or lacks that relationship in a different encounter.

The dissent retains the government's production and persuasion burden, assumes rather than finds substantial burden, and makes no finding about sincerity, exact acts, violence or prior guilt. Its position applies the governing test to the asserted access-denying immunity, not a categorical rule that medical access, commerce or third-party harm always defeats RFRA. Materially different nonobstructive practices, enforcement threats and accommodations remain for their own claims. Stevens, Ginsburg and Breyer join this common formulation of the assumed-obstruction ground; no distinct theory belonging to the Chief alone is incorporated. They otherwise support the judgments rejecting the presented constitutional and categorical damages challenges.'''

precedents = '''- **Lopez:** preserves the required commercial connection and prohibition against adding an unexpressed element; the school-possession/productivity chain does not govern direct interference with this services market.
- **Harris:** applies its economic-class rationale without making its enacted particular-vehicle nexus a universal condition of class regulation.
- **Robertson:** retains its direct-enterprise rule; no protester is classified as an interstate business merely by inference.
- **New York v. United States:** preserves the bar on compelled state legislation or administration; private conduct regulation is distinct.
- **O'Brien and Ward:** apply the substantial nonsuppressive-interest and proportionate-burden standard for expressive conduct; no least-restrictive-conceivable-means requirement is added to speech scrutiny.
- **Turner:** applies actual content classification, independent fit review and qualified deference; benign purpose and legislative findings are not conclusive.
- **Mitchell:** applies lawful motive proof and protected-belief limits; potentially expressive peaceful obstruction still receives the applicable scrutiny.
- **R.A.V.:** applies the controlling substantial-overbreadth holding. The separate within-category content-selection theory is not adopted as Court law, and the earlier vagueness reservation is not rewritten.
- **Cameron:** supports ascertainable physical-obstruction boundaries in their statutory setting, without deciding any particular FACE prosecution.
- **Madsen:** preserves responsible-party attribution and its distinct, more demanding injunction standard; its distances and actual-concert rules are not general statutory or damages rules.
- **Hurley:** preserves private expressive choice; the present statute does not compel inclusion of a message.
- **Claiborne Hardware:** preserves personal responsibility and protection against damages for lawful persuasion, without imposing a categorical actual-loss ceiling on elected statutory damages.
- **Smith and Lukumi:** preserve constitutional neutral-law, objective-targeting and comparable-secular-harm rules. The six-Justice exemption rationale does not turn the two reserving Justices into Smith adherents.
- **Clearwater and Swanner:** apply RFRA's separate person-and-application inquiry, with claimant substantial burden followed by government production and persuasion; no categorical third-party-harm or commerce exception replaces it.
- **Lee and Roberts:** retain the legal weight of injury to other persons without eliminating RFRA's application-specific inquiry.
- **Bray:** its distinct private-conspiracy and privately protected-right limits neither defeat FACE's commerce basis nor establish a new Fourteenth Amendment §5 ground; that alternative is not reached.'''

law = '''The challenged reproductive-service provisions survive the presented facial constitutional and categorical damages objections within their enacted definitions, motives, own-minor exception and protected-expression limits. Their commercial connection rests on direct interference with an actual medical-services market, not generalized social costs. Elected statutory damages remain possible for legally attributable, nonexcepted violations; the parent/guardian exception bars all FACE civil remedies, including injunctions, for qualifying exclusively own-minor conduct. No amount-specific award is adjudicated. The inclusive facility definition and separate ingress/egress/passage rules create no invented grounds coverage or outdoor immunity. Six Justices reject the broader constitutional exemption under Smith/Lukumi, while RFRA independently requires the five-Justice remand. The government must satisfy that statute for the identified person and application after a substantial burden is established; the Act's continued force does not establish every future enforcement as lawful. No new true-threat rule, worship holding, Fourteenth Amendment §5 power, automatic religious exemption or general damages-attribution theory is created.'''

sources_public = '''The lower judgments are American Life League, Inc. v. Reno, 47 F.3d 642 (4th Cir. February 13, 1995), No. 94-1869, and 855 F. Supp. 137 (E.D. Va. June 16, 1994), No. 94-700-A. The [primary appendix and party papers](https://archive.org/details/micro_IA40386012_1752) document those judgments and the adversarial claims. The [enacted FACE text, 108 Stat. 694–697](https://www.govinfo.gov/content/pkg/STATUTE-108/pdf/STATUTE-108-Pg694.pdf) supplies its separate definitions, remedies, exception, savings clauses, severability and effective date; [RFRA, 107 Stat. 1488–1490](https://www.govinfo.gov/content/pkg/STATUTE-107/pdf/STATUTE-107-Pg1488.pdf) supplies the statutory burden and express later-law rule.

This is a pre-enforcement pleading case. Substantial burden is assumed for review of dismissal, not found as a fact; the actual threatened application and a contested burden remain for the remand. Legislative evidence of interstate patients, personnel, supplies and service disruption is reported in the lower opinion, not an individual finding that each plaintiff crossed state lines. The Court decides no specific liability, criminal punishment, damages award, reasonableness of the $5,000 amount, or challenge to the worship provisions.'''

public = {
    'Event': '''**American Life League v. Reno. Decided November 13, 1995.** On review of the Fourth Circuit's judgment in No. 94-1869, affirming dismissal with prejudice of the second amended complaint under Rule 12(b)(6). The questions concern congressional authority, speech and association, facial vagueness and overbreadth, constitutional religious exercise, and RFRA's distinct protection against threatened enforcement. The plaintiffs allege future prayer, counseling, demonstrations and peaceful physical obstruction; this is not a prosecution of adjudged violent conduct.

''' + statute,
    'Participation': 'Chief Justice Stone-Zsela and Justices Stevens, O\'Connor, Scalia, Kennedy, Souter, Thomas, Ginsburg and Breyer participated in submission and decision. All nine participated; no recusal or absence applies.',
    'Public Action': 'The Court decides the merits of the presented challenges and returns only the RFRA prospective-enforcement claim for further adjudication.',
    'Judgment & Remedy': judgment,
    'Opinion Topology': topology,
    'Holdings': HOLDINGS,
    'Precedent Treatment': precedents,
    'Law After Decision': law,
    'Separate Writings': separates,
    'Procedure After Action': 'The mandate returns the case through the Fourth Circuit for district-court proceedings on the RFRA prospective-enforcement claim alone, with ordinary standing and appropriate-relief requirements. A remand is not interim injunctive relief: any such request needs its own legal showing. No further Supreme Court event is set, no deadline is invented, and no unchallenged worship provision or previously unpresented damages application is adjudicated.',
    'Source Notes': sources_public,
}

recon = (TERM/'freeze/OT_1995CHUNK1_B_RECONCILED.md').read_text(encoding='utf-8')
case_recon = recon[recon.index('## American Life League v. Reno'):]
audit_table = case_recon[case_recon.index('| Justice |'):case_recon.index('### Component inventory')].strip()
text_recon = (TERM/'freeze/OT_1995CHUNK1_ALL_TEXT_RECONCILED.md').read_text(encoding='utf-8')
refresh_table = text_recon[text_recon.index('| Associate |'):text_recon.index('## Final inventory')].strip()

compat = '''| Justice | Final opinion joins and judgment | Preserved barrier; accommodation and remaining disagreement |
|---|---|---|
| Stone-Zsela | Kennedy I, II, III-A, IV-B; other constitutional and categorical speech dispositions; dissents from RFRA remand | Actual-market ground leaves his six-route framework unadopted. No ground is added on constitutional free exercise or vagueness. He supplies attribution, not a new elected-damages theory. RFRA justification is limited to the assumed access-denying conduct, not a categorical exception. |
| Stevens | All Kennedy portions; joins Stone's RFRA dissent | His broader Lopez position remains a reservation compatible with the narrower common ground. No protected-persuasion damages, belief liability or automatic commerce-forfeits-religion rule. His RFRA application remains a dissent under Swanner. |
| O'Connor | Kennedy I–IV and V-A; writes RFRA remand and constitutional reservation | Her Turner/Madsen objections are met by actual conduct classification and fitted statutory review; broader Smith endorsement remains withheld. Swanner's actual statutory inquiry, not a guaranteed exemption, governs the remand. |
| Scalia | All Kennedy portions; joins RFRA remand | No adoption of the Lopez dissent, no automatic benign-purpose neutrality and no conversion of his R.A.V. separate view into governing law. No mandatory hearing for every assertion, and no religious exemption follows by default. |
| Kennedy | Writes all constitutional portions; joins RFRA remand | The opinion performs direct commercial-connection, actual selection/fit and objective-comparability analysis. Section 5, untried enforcement and a generic cost-of-crime ground remain outside it. |
| Souter | Kennedy I–IV and V-A; joins RFRA remand and O'Connor's constitutional reservation | Preserves attribution and private expressive choice, his broader Lopez reservation, and nonreach of the broader constitutional exemption. Generalized access interests do not replace the claimant/application inquiry. |
| Thomas | All Kennedy portions; joins RFRA remand | No inherited intermediate-tailoring writing or general aggregate-crime rule; actual service harm and defined conduct supply his join. RFRA remains statutory and claimant-specific, with no automatic exemption or compulsory hearing. |
| Ginsburg | All Kennedy portions; joins Stone's RFRA dissent | Her Turner warning against benign-purpose camouflage is retained by selection/fit analysis; amount-specific damages and sincerity remain open. Her RFRA join extends only to the supported assumed-obstruction application, not every Chief sentence or categorical harm rule. |
| Breyer | All Kennedy portions; joins Stone's RFRA dissent | Preserves broader Lopez view while accepting this sufficient direct connection; inherits no preappointment separate writing. Applies Swanner's controlling burden but finds it satisfied on the pleaded obstruction assumption, reserving materially different conduct. |

These are final compatibility determinations, not invented circulation dialogue. No non-Stone judgment or operative ground changes from reconciliation. The only formulation choices make the frozen limits explicit; they do not create a new join or erase a recorded objection. O'Connor/Souter's constitutional reservation changes opinion support, not the agreed facial constitutional disposition.''' 

internal = f'''**Case and dockets:** American Life League v. Reno; Fourth Circuit No. 94-1869, 47 F.3d 642; E.D. Virginia No. 94-700-A, 855 F. Supp. 137. Research petition No. 94-1867 is not adopted as an invented plenary merits docket.
**Event and date:** Merits decision, 1995-11-13.
**Result:** Affirm the presented constitutional and categorical damages dismissals, 9–0; vacate the RFRA prospective-enforcement dismissal and remand, 5–4.
**Version / lineage:** Initial adjudication; no prior Record superseded; operator Git commitment pending.

## Event, vehicle, facts and questions

This is the expressly assigned Supreme Court appellate merits review of the Fourth Circuit's February 13, 1995 affirmance, not a historical certiorari action. The district court dismissed the second amended complaint with prejudice on June 16, 1994 under Rule 12(b)(6). The plaintiffs sued on enactment day, May 26, 1994; their pleaded prospective prayer, counseling, demonstration and peaceful obstruction present the challenged enforcement. The circuit assumed sufficient substantial religious burden; the government disputes it. Neither peacefulness nor religious motivation establishes unobstructed passage, actual violence, sincerity, statutory liability or entitlement to an exemption. No historical cert vote, grant date, Supreme Court merits docket or argument date is invented. An argument date is not established by the authorized input; this makes no claim that argument did not occur.

The questions are congressional power and the distinct anti-compulsion objection; content/viewpoint classification and expressive-conduct fit; overbreadth and due-process vagueness; the categorical First Amendment objection to private elected damages and attribution; constitutional targeting and the broader constitutional exemption; and the separate RFRA prospective-enforcement claim. Worship protections, amount-specific reasonableness, particular penalties and the unadjudicated §5 alternative are outside the determination.

## Participation, threshold and source cutoff

All nine rostered Justices participate at submission and decision: {names(ALL)}. No participation change, recusal or death appears. The quorum is six; nine participate and five votes establish a majority. There is no equal-division event. No submission or oral-argument calendar beyond the supplied November 13 decision date is fabricated. Research uses only legal authority effective by that event, with the actual earlier current-term law checked below; modern retrieval dates are provenance, not effective dates.

## Entering law and chronology

The [B entering-law slice](../entering-law/OT_1995CHUNK1_B.md) and [supplement](../entering-law/OT_1995CHUNK1_B_SUPPLEMENT.md) copy authority and are not themselves law. Exact relevant Standards titles are **Required commercial connection and distinct economic-class regulation** (Lopez, April 26, 1995; Harris, April 27, 1995), **Direct enterprise engagement in interstate commerce** (Robertson, May 1, 1995), **RFRA review of prospective enforcement** (Clearwater, December 5, 1994; Swanner, March 27, 1995), and **Speech burdens in a content-neutral injunction** (Madsen, June 30, 1994). Turner (June 27, 1994), Mitchell and Lukumi (June 11, 1993), R.A.V. (June 22, 1992), Hurley (June 19, 1995), surviving O'Brien/Ward, Smith, Claiborne, Cameron, New York and the source-described Bray limits supply their actual propositions.

R.A.V.'s controlling law is Stone's five-Justice substantial-overbreadth opinion; the four-Justice within-category content-selection position is not substituted for it. Lopez is Kennedy's bounded commercial-connection rule, not the Chief's separate six-route framework. Harris's eight-Associate economic-class rationale is controlling notwithstanding Stone's distinct instrumentality ground there. Swanner's five-Justice application-specific remand controls despite the current dissenters' earlier separate application. Later appointment supplies no predecessor's personal position.

Actual earlier A public law is read through the bounded [Wood](../entering-law/PUBLIC_Wood_v_Bartholomew_summary_merits_1995-10-10.md), [Doe](../entering-law/PUBLIC_Doe_v_Taylor_ISD_merits_1995-10-16.md) and [Hodge](../entering-law/PUBLIC_Hodge_v_Jones_merits_1995-10-23.md) projections. Wood's supported collective Brady inquiry, Doe's knowing causal supervisory-acquiescence and bodily-integrity scope, and Hodge's Court immunity-only and mootness grounds create no new FACE, commerce, speech or RFRA rule. Hodge's noncontrolling Stone family/record merits cannot supply such a rule. No Tuggle event enters.

**Final root refresh reference:** Before preservation, the operator must insert the actual October 31 and November 7 B effective-law and assignment review. This proposed Record does not represent those future-to-assembly checks as completed. It uses no later November 20–29 C event as entering law.

## Statute and adjudicative scope

{statute}

RFRA's original §3 allocates substantial burden to the claimant, then both production and persuasion to the government on compelling interest and least restrictive means as applied to the person. Its claim/defense and appropriate-relief route preserves Article III standing. Later federal laws remain subject unless expressly excluded by reference to RFRA; FACE contains no exclusion. Belief protection and the Establishment Clause remain distinct.

**Corrected-text stage chain:** The separately frozen [neutral statutory supplement](../freeze/OT_1995CHUNK1_ALL_TEXT_NEUTRAL_SUPPLEMENT.md), [independent refresh](../freeze/OT_1995CHUNK1_ALL_TEXT_REFRESH_COMMITMENTS.md) and [renewed reconciliation](../freeze/OT_1995CHUNK1_ALL_TEXT_RECONCILED.md) now control the accurate statute and its explicitly reconsidered consequences. The [receipt](../freeze/ALL_TEXT_RECONCILIATION_RECEIPT.json) and [context clarification](../freeze/ALL_TEXT_REFRESH_CONTEXT_CLARIFICATION.md) disclose same-context fallback and preservation of earlier freezes. The whole civil-remedy exclusion is substantive, not a punctuation repair; the renewed comparison retains each Associate's outcome while rejecting surviving FACE relief against exempt conduct. The inclusive facility definition adds no grounds or worship premises; separate passage/worship language remains. An unexecuted assembly script was paused before any Record or JSON generation. This assembly restarts after express authorization from the renewed handoff, whose SHA256 is 648a1c4e8cfbe1add1db2f6dd750676431d951f7771738783e40f760ac7371eb. No completed adjudication is amended.

## Stone fixed core and standing fallback

The fixed [B Stone input](../freeze/OT_1995CHUNK1_B_STONE_INPUT.md) supports affirming the facial commerce and speech dismissals on actual-market and fitted-conduct grounds, preserving attribution, and rejecting the assumed access-denying religious exemption under the actual RFRA standard while reserving genuinely different applications. It does not support a categorical RFRA harm exception, adoption of his entire six-route commerce framework, or remand of an already resolved application merely because a minority prefers the rule's application. His dissent accepts the governing standard and disputes this remand's necessity.

The user-approved standing fallback supplies **disposition-only support for the distinct constitutional free-exercise and due-process vagueness components**, on which his fixed supplement supplies no separate ground. It adds no reasoning or opinion join. His broad free-speech disposition covers overbreadth and rejection of the categorical damages speech challenge; his express organizational-attribution condition supports Part IV-B. It does not supply a new general elected-damages theory, so he does not join Part IV-A. No damages amount or unaddressed enforcement theory is selected for him. The public topology identifies these limits without approval or workflow terminology.

The corrected statutory exception is compatible with Stone's expressly limited outsider-access position: it defeats a universal-enforcement premise that he does not adopt and requires preserving qualifying parental applications as genuinely different claims. No residual FACE injunction against excepted conduct is assumed. His fixed religious application, not the standing fallback, supplies his RFRA dissent. The passage/facility correction likewise supplies no new geographic restriction for him to endorse.

## Final judgment and remedy

{judgment}

## Assignment and opinion architecture

On the unanimous constitutional and categorical-speech judgment, the Chief assigns Kennedy. Fit governs: his own Lopez opinion supplies the commercial-connection boundary, his Turner work supplies actual content selection and independent fit review, and his Lukumi work supplies objective targeting and comparable harm. These are the opinion's principal legal tasks. O'Connor is a strong alternative through Harris, Madsen and the RFRA cases; Stone is also capable of the direct-market and access-protection work and of preserving his R.A.V. rule. Neither offers a material advantage over Kennedy in coordinating these three inherited frameworks while reserving Stone's six-route theory and the two Associates' broader Smith questions. Stone's interest in access does not itself support self-assignment. The common grounds are already settled; no coalition expansion or fictitious negotiation is required.

On RFRA, Stone and Stevens oppose remand; **O'Connor is the most senior member of the five-Justice remand coalition and assigns that component to herself**. Her Clearwater and Swanner opinions supply the precise statutory task and existing coalition boundaries. Souter is the strongest alternative, with his claimant-specific and attribution positions, but O'Connor's repeated authorship of the governing burden and remand rule provides the more direct fit. This Associate assignment is not imposed as Stone's preference and does not count as a Chief assignment. O'Connor and Souter's common constitutional reservation is stated separately. Stone writes the RFRA dissent; Stevens, Ginsburg and Breyer join only its shared assumed-obstruction reasoning, not an unexpressed Chief theory.

The [OT1994 assignment review](../freeze/OT1994_ASSIGNMENT_REVIEW.md) records 94 named Chief assignments and no author above one half; the consecutive-term ceiling is inactive. Completed A assignments are Wood/O'Connor, Doe/Ginsburg and Hodge/O'Connor, all by the Chief. Root will insert intervening B assignment counts before preservation; workload does not decide this assignment. Each opinion is counted once, as Chief-assigned if the Chief assigned any part; the distinct RFRA opinion is Associate-assigned.

## Opinion topology and compatibility

{topology}

{compat}

## Controlling holdings

{HOLDINGS}

## Published separate positions and continuity

{separates}

These published grounds, not additional private commitments, supply continuity. The constitutional reservation is noncontrolling; the RFRA dissent's specific justification remains noncontrolling. The unanimous constitutional disposition does not make all reasons unanimous, and the five-Justice RFRA rule is not diluted by the four's agreement on its abstract burden sequence.

## Adaptive audit annex

Frozen authorities: [validated B packet](../freeze/OT_1995CHUNK1_B_NEUTRAL_VALIDATED.md), [B reconciliation](../freeze/OT_1995CHUNK1_B_RECONCILED.md), and the corrected-text neutral/independent/reconciled chain identified above. The following eight-Justice table preserves the prior sufficient grounds and own authorities; its statutory shorthand is superseded by the complete correction-specific table that follows. Both describe the Associates before Stone enters; the final nine-Justice accounting is above.

{audit_table}

**Final corrected-text reconciliation by Justice:**

{refresh_table}

The historical comparator contains no Supreme Court plenary merits opinion for this assigned review. The historical petition action supplies neither a present merits lineup nor undisclosed cert votes. The Fourth Circuit opinion is the judgment under review. The changed intervening Lopez/Harris commerce and Clearwater/Swanner statutory law is actually applied, not presented as a historical Supreme Court merits departure. No historical author is imported. There is no material changed non-Stone commitment requiring return for a new reconciliation; no Historical departure label is manufactured for a comparison that has no merits baseline.

Adversarial checks retain the strongest alternatives: ideological local protest versus direct services-market harm under Lopez; motive-selective suppression versus defined physical access harm under Turner/Mitchell; and immediate RFRA justification versus incomplete person-and-application review under Swanner. The final holdings answer those objections within the frozen limits. No appellate fact finding resolves sincerity, precise conduct, exact financial loss, statistics or an individual violation. No omission in unread party material is used as a concession.

## Source map, limits and performed validation

The [objective source addendum](../sources/B_AMERICAN_LIFE_LEAGUE_OBJECTIVE_SOURCE_ADDENDUM.md) identifies the primary IA docket and complete lower-court opinions, official FACE and RFRA texts, and bounded party-brief reads. The exact second amended complaint, some petition speech passages, intervenor opposition, reply and congressional reports were not fully read by the source agent. They are not declared unavailable. The selected pleading-level remand and facial legal holdings do not depend on an absence or concession from those unread materials; a new threshold factual or amount-specific ruling would require them.

Assembly reread the complete existing four-page official FACE extraction and relevant verbatim entering-law portions, the entire reconciled ALL section and validated scope, and the existing source digest. No new network research, raw historical current-matter opinion, private core or locked top-level directory was used. The legal cutoff is November 13, 1995. This is disclosed assembly context with Stone exposed, not a claim of blind modeling. Initial independent and reconciliation bytes remain untouched.

Local generation checks verify the exact eleven projection blocks, byte-identical internal/public Holdings, participants and each component's nine named positions, opinion membership and controlling majority, all eight Associate audit rows, and each ordinary explanation below 350 words. Input hashes are preserved in the companion receipt. These are clerical consistency checks, not substitutes for the operator's final legal review, actual B chronology refresh or preservation. The objective text confirmation and renewed neutral/model/reconciliation phases are complete in the named frozen chain.

## Public Projection

'''

record = internal + '\n\n'.join(f'## {b}\n\n{public[b]}' for b in BLOCKS) + '\n'
path = OUT/(NAME+'.md')
path.write_text(record, encoding='utf-8', newline='\n')

metadata = {
    'record': NAME+'.md', 'record_filename': NAME+'.md',
    'case': 'American Life League v. Reno', 'date': '1995-11-13',
    'disposition': 'Affirm constitutional and categorical damages dismissals, 9–0; vacate RFRA prospective-enforcement dismissal and remand, 5–4.',
    'disposition_summary': 'Affirm constitutional and categorical damages dismissals, 9–0; vacate RFRA prospective-enforcement dismissal and remand, 5–4.',
    'participants': ALL,
    'judgments': [
        dict(component='Facial constitutional challenges',disposition='Affirm dismissal',support=ALL,oppose=[],other=[],printed_tally='9–0'),
        dict(component='Categorical elected-damages speech challenge',disposition='Affirm dismissal with attribution limits',support=ALL,oppose=[],other=[],printed_tally='9–0'),
        dict(component='RFRA prospective-enforcement claim',disposition='Vacate dismissal and remand',support=RFRA,oppose=AFFIRM_RFRA,other=[],printed_tally='5–4')],
    'writings': [
        writing('Kennedy', ALL, 'Parts I, II, III-A, IV-B: commerce/federalism, speech, overbreadth, attribution'),
        writing('Kennedy', ASSOC, 'Parts III-B, IV-A, V-A: vagueness, elected-damages rationale, facial religious targeting'),
        writing('Kennedy', SMITH, 'Part V-B: constitutional exemption under Smith/Lukumi'),
        writing("O'Connor", RFRA, 'RFRA rule, application and remand'),
        writing("O'Connor", ["O'Connor",'Souter'], 'Concurrence in part reserving broader constitutional exemption',False),
        writing('Stone-Zsela',AFFIRM_RFRA,'Dissent from RFRA remand on the common assumed-obstruction application',False)],
    'blockers': [],
    'law_summary': law,
    'published_positions': [
        "O'Connor, joined by Souter, reserves the broader constitutional substantial-burden exemption under Smith while joining rejection of facial targeting and the statutory remand; no exemption or new constitutional rule follows.",
        'Stone-Zsela, joined by Stevens, Ginsburg and Breyer, accepts RFRA and would affirm on the assumed access-denying obstruction: immunity defeats the affected person\'s access, while nonobstructive advocacy remains available. The own-minor exception does not cover outsider blockade; materially different applications remain open.'],
    'next_stage': 'District-court RFRA person-and-application inquiry through the Fourth Circuit; no exemption or injunction follows, and other dismissals remain. No further Supreme Court event set.',
    'assignment': [
        dict(assigner='Stone-Zsela',author='Kennedy',scope='Constitutional and categorical damages opinion',basis='Chief in judgment majority; Lopez/Turner/Lukumi fit',count_pending_root=True),
        dict(assigner="O'Connor",author="O'Connor",scope='RFRA remand opinion',basis='Most senior Associate in remand majority; Clearwater/Swanner fit',chief_assignment=False)],
    'status': 'proposed; root preservation review pending',
    'final_root_refresh_reference': 'Pending root insertion before preservation: actual October31/November7 B law and assignment counts. Corrected FACE neutral/model/reconciliation chain complete.'
}
(OUT/(NAME+'.json')).write_text(json.dumps(metadata,ensure_ascii=False,indent=2)+'\n',encoding='utf-8',newline='\n')

pp = record.split('## Public Projection\n\n',1)[1]
(OUT/('PUBLIC_DRAFT_'+NAME+'.md')).write_text(pp,encoding='utf-8',newline='\n')
assert re.findall(r'^## (.+)$',pp,re.M)==BLOCKS
kernel = record.split('## Controlling holdings\n\n',1)[1].split('\n\n## Published separate positions',1)[0]
projected = pp.split('## Holdings\n\n',1)[1].split('\n\n## Precedent Treatment',1)[0]
assert kernel == projected == HOLDINGS
for j in metadata['judgments']:
    assert len(j['support']+j['oppose'])==9 and set(j['support']+j['oppose'])==set(ALL)
    assert len(set(j['support']+j['oppose']))==9
for w in metadata['writings']:
    assert w['author'] in ALL and w['author'] not in w['joiners']
    assert len(set(w['joiners']))==len(w['joiners']) and set(w['joiners']).issubset(ALL)
    assert not w['controlling'] or len(w['joiners'])+1>=5
assert all(v<=350 for v in explanations.values()), explanations
assert all('| **'+j+'** |' in audit_table for j in ASSOC)
assert all(hashlib.sha256((TERM/p).read_bytes()).hexdigest()==digest for p,digest in hashes.items())
assert not re.search(r'\b(simulated|approved|fallback|workflow|commitment|operator|draft)\b',pp,re.I)
receipt = dict(record=NAME+'.md',record_sha256=hashlib.sha256(path.read_bytes()).hexdigest(),
    record_bytes=path.stat().st_size,input_sha256=hashes,explanation_word_counts=explanations,
    checks='Eleven blocks, exact Holdings identity, component arithmetic, controlling joins, eight Associate rows, explanation ceilings, input preservation, public workflow exclusion passed.',
    public_draft_sha256=hashlib.sha256((OUT/('PUBLIC_DRAFT_'+NAME+'.md')).read_bytes()).hexdigest(),
    restarted_from='Corrected neutral, independent refresh and ALL-only reconciliation frozen before this authorized restart; original freezes unchanged.',
    pending='Root actual B effective-law/assignment refresh and final preservation review; no output render created.')
(OUT/'ALL_ASSEMBLY_RECEIPT.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n',encoding='utf-8',newline='\n')
print(json.dumps(dict(record=str(path.relative_to(ROOT)),bytes=path.stat().st_size,checks='passed',explanation_words=explanations),ensure_ascii=False))
