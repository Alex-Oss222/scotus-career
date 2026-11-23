from pathlib import Path
import hashlib
import re
import sys

TERM = Path(__file__).resolve().parents[2]
SOURCE = TERM / 'research/chunk5-neutral/Sabree-provisional-neutral.md'
text = SOURCE.read_text(encoding='utf-8')
text = text.replace('# Sabree: provisional independent Associate analysis', '# OT2004 chunk 5 Sabree: frozen independent Associate commitments', 1)
old_intro = 'NOT FROZEN. Prepared without a historical comparator or private present-case position. Final commitments await the exact completed March 22 Rancho Palos Verdes public law. These are provisional judicial choices, not an opinion assignment or a completed decision. Sherrill and Jackson are outside this document.'
new_intro = 'FROZEN NEUTRAL HANDOFF. The eight Associate commitments below are final for independent modeling, before historical reconciliation or any private present-case position. The completed March 7 and March 22 public-law supplements have been applied. This handoff is not a Canonical Decision Record, supplies no Chief Justice vote and selects no opinion author. Sherrill and Jackson remain outside this context and this document.'
assert old_intro in text
text = text.replace(old_intro, new_intro, 1)
text = text.replace('`Sabree-source-receipt.md` records the source boundary and verification;', '`freeze/OT_2004CHUNK5_SABREE_NEUTRAL_PREFLIGHT.md` records the completed source boundary and verification;', 1)
text = text.replace('This is the component directly awaiting the March 22 law.', 'The actual March 22 Rancho Palos Verdes holding supplies the completed same-term foreclosure rule.', 1)
text = text.replace('**A — provisional commitment:', '**A — frozen commitment:')
text = text.replace('**B — provisional commitment:', '**B — frozen commitment:')
text = text.replace('**D — provisional commitment:', '**D — frozen commitment:')

rancho = {
    'Stevens': """**C — frozen commitment: no congressional foreclosure.** Stevens joined Thomas's entire March 22 Rancho opinion, which assumes a right, assigns the defendant the burden, and finds a concrete conflict between the new thirty-day expedited personal judicial action and an ordinary parallel section 1983 suit. His Wright and Wilder joins and Blessing opinion already reject automatic displacement by funding withdrawal. The actual Medicaid comparison includes both section 1396c oversight and section 1396a(a)(3)'s personal fair hearing; neither separately nor together establishes a congressionally prescribed judicial timetable or another remedial limit that this action would bypass. The strongest contrary route is that hearings plus federal supervision form a complete system even without a distinct judicial action. He rejects that inference on these provisions because completeness of administration does not establish incompatibility with the pleaded prospective action. His join is limited to this demonstrated compatibility, not a rule that administrative remedies can never displace section 1983 or that an express judicial action is invariably necessary for foreclosure.""",
    "O'Connor": """**C — frozen commitment: no congressional foreclosure.** O'Connor joined the entire completed Rancho opinion. She accepts its defendant burden and actual-conflict test, not a presumption that any express remedy eliminates section 1983. Unlike the direct siting action's thirty-day filing requirement and mandatory expedition, Medicaid's federal sanction and beneficiary hearing identify no judicial condition that the present action would make optional. The strongest State argument combines the hearing's individual focus with the Secretary's enforcement authority; her Blessing and Rancho joins require that combination to be considered on its terms. It still establishes no incompatible substitute on the present statutory text. She would withhold assent from a rule that federal-state program hearings are universally nonexclusive, or that lack of an express judicial route automatically defeats every possible foreclosure claim. The conclusion rests on the particular mechanisms actually enacted here.""",
    'Scalia': """**C — frozen commitment: no congressional foreclosure.** Scalia's full join in completed Rancho supplies a concrete willingness to reject section 1983 where its ordinary operation would evade Congress's personal thirty-day expedited court action. His full Blessing join and the Wilder dissent he joined separately recognize the remedial inquiry once a congressional right exists. Section 1396c withholding and section 1396a(a)(3)'s beneficiary hearing are considered together, but the Secretary identifies no comparable evasion or other actual inconsistency. The strongest adverse argument is that the combined mechanisms imply Congress intended all individual relief to remain administrative. Neither their availability nor the statute's institutional setting supplies that missing incompatibility. He joins this provision-specific conclusion and refuses a categorical rule that express remedies always foreclose, that administrative remedies never do, or that a particular judicial-action format is indispensable to every finding of displacement. His reserved funding-contract question is not silently decided through this distinct component.""",
    'Kennedy': """**C — frozen commitment: no congressional foreclosure.** Kennedy joined Thomas's entire completed Rancho opinion and its distinction between general funding administration and a personal judicial action carrying conditions that an ordinary section 1983 suit would bypass. The fair-hearing provision gives the State a stronger argument than federal oversight alone, but its combination with section 1396c supplies no special judicial filing rule, mandatory judicial timetable or other identified congressional condition with which this action conflicts. His Blessing join and the Wilder dissent he joined do not demand a separate private-remedy-intent showing after an individual right is established. The lawful contrary path would require an actual incompatible remedial design, which Rancho confirms can be decisive even when a right is assumed. That proof is absent here. His join excludes both a presumption of foreclosure from any express remedy and a categorical administrative-remedies exception to foreclosure.""",
    'Souter': """**C — frozen commitment: no congressional foreclosure.** Souter joined the complete Rancho opinion. It distinguishes the assumed personal right from the statutory conflict in enforcement procedures: a parallel ordinary action would evade the particular thirty-day expedited court route. His Gonzaga concurrence join treats administrative consistency as relevant to interpreting a particular right, not as automatic extinction after a right has been established, and his Blessing join supplies the presumption and defendant burden. The strongest State path views the individual fair hearing and federal oversight as one coherent correction system. Considering their combination, neither text supplies a congressional judicial condition or another demonstrated incompatibility that the present prospective action would defeat. A hearing may resolve a claimant's problem without being Congress's exclusive substitute for section 1983. Souter joins that actual comparison, not a rule resolving every administrative system the same way or requiring an identical thirty-day action before foreclosure can ever occur.""",
    'Thomas': """**C — frozen commitment: no congressional foreclosure.** Thomas's own completed Rancho opinion is the principal current-term source. It places the burden on the defendant, preserves Blessing's separate right inquiry, and forecloses the additional action because the same statutory violation would escape Congress's specific personal thirty-day filing and expedited adjudication requirements. It expressly distinguishes Bruneau's funding administration and rejects a general presumption from the existence of any express remedy. Medicaid's funding sanction and beneficiary fair hearing must both be assessed, but neither separately nor in combination creates that conflict or another identified restriction the pleaded action would evade. The State's strongest objection is that the agency process was meant to be primary and comprehensive. Primacy and administrative detail do not establish exclusive incompatibility under the rule Thomas has just articulated. He therefore joins no foreclosure here, with no general right inferred from remedial desirability and no holding that administrative remedies are incapable of displacing section 1983.""",
    'Ginsburg': """**C — frozen commitment: no congressional foreclosure.** Ginsburg joined all of Rancho, including its express distinction between an available right and an incompatible parallel remedy. Her Blessing join and Gonzaga dissent join already resist treating central correction and funding sanctions as automatically exclusive. The fair hearing is an actual individual correction process and must not be ignored. The strongest State argument is that the process supplies the very relief these beneficiaries need and works with funding oversight to protect the program. Even considered together, the provisions reveal no congressionally limited court action or other remedial condition that the present section 1983 claim would bypass. Rancho's concrete thirty-day conflict is therefore absent. Her join concerns this statutory design and does not establish that administrative remedies can never foreclose or that a similar judicial filing period is the only possible source of incompatibility.""",
    'Breyer': """**C — frozen commitment: no congressional foreclosure.** Breyer joined Thomas's entire Rancho opinion without a separate writing. Its actual holding requires a demonstrated conflict, found there because an ordinary parallel action would avoid the personal thirty-day expedited judicial route; it leaves general funding oversight insufficient by itself. His Gonzaga concurrence distinguishes administrative consistency in interpreting a right from displacement after the right is found. The strongest State argument is practical coherence: individual hearings and federal supervision may jointly correct assistance failures, while another action could complicate administration. Yet overlap and possible inconvenience do not identify a congressional remedial limit that this action defeats. The two Medicaid mechanisms are therefore compatible with section 1983 on the stated claims. He joins this concrete comparison and excludes both automatic foreclosure from any express remedy and a universal rule that administrative systems cannot be exclusive.""",
}

for justice, replacement in rancho.items():
    section = text.index('\n## ' + justice + '\n')
    begin = text.index('**C — provisional commitment:', section)
    end = text.index('**D — frozen commitment:', begin)
    text = text[:begin] + replacement + '\n\n' + text[end:]

start = text.index('## Provisional convergence and remaining work')
text = text[:start] + """## Completed March 7 and March 22 integration

The March 7 public slice was read in full. The regenerated Shepard holding II was reread after its completeness expansion concerning preserved omitted charges, Rule 52(b), and lawful jury waiver; those sentencing details do not affect any Sabree component. Wilkinson v. Dotson, authored by O'Connor and joined by all nine, reinforces attention to the actual legal effect of relief and the separation between an available section 1983 vehicle and later proof of the right, violation and remedy. Its habeas boundary does not decide Medicaid foreclosure or import prison-specific requirements. Back, Ballard and Shepard supply no different Medicaid right or enforcement rule.

All four completed March 22 public projections were read in full. Rancho, authored by Thomas and joined by all nine without a separate writing, supplies the actual remedial-incompatibility rule applied individually in component C above. Its assumption of a right does not decide component A or B here. Its saving-clause ruling concerns the TCA's new siting entitlement; no Medicaid saving clause or hybrid cause of action is invented. The absence of an express fee provision and the request for extra damages were contextual features there, not universal foreclosure rules. The present claim seeks prospective assistance relief, and ordinary section 1983 remedies neither establish the statutory right nor excuse a proven incompatible scheme.

Black Political Task Force, Brown v. Payton and Muehler do not construe these Medicaid provisions or change their enforcement channel. Their distinct merits and remedy disagreements are not treated as proxies for a Sabree vote. In particular, the districting injunction's existing supported scope does not prove a Medicaid class violation, and the habeas statutory gateway does not become a general section 1983 standard. Muehler's separation of constitutional grounds and the actual relief supported by them is consistent with the component-specific analysis but supplies no new Medicaid holding.

## Statutory qualifications and actual remand

The payment definition, adopted covered category, actual eligibility and reasonable promptness remain distinct requirements. The reference to section 1396d(a)(15) identifies covered intermediate-care services other than an institution for mental diseases, for persons determined in accordance with section 1396a(a)(31) to need them. Section 1396a(a)(31) requires a written plan of care before admission or authorization of benefits and periodic independent professional review of continuing need. Section 1396d(d) supplies the qualifying facility's purpose, standards and active-treatment conditions. Its public-institution expenditure condition expressly concerns quarters before January 1, 1975; it is not a new present eligibility obstacle.

Those qualifications define covered payment and treatment at their actual stage. They do not require an eligible waiting-list claimant already to be receiving the treatment allegedly withheld before invoking the accepted eligibility and prompt-assistance claim. Nor does the absence of adjudicated details permit a new factual finding that a claimant failed the required care-plan or need-determination process. Other actual statutory coverage, timing and eligibility limits remain applicable according to their terms; the complete operative text and its exceptions are preserved in the script-copied source handoff, rather than silently replaced with a broader definition.

The official appellate opinion describes plaintiffs as a class but expressly reserves the assistance-versus-services remedy question. That description does not establish the precise terms of certification or support an immediate new common decree. The District Court must adjudicate the claimed breach, causation, responsible official, individual and any representative scope, compliance options and lawful prospective relief. No new proof of grant, filing or docket intake is required. No absent class order is made a reason to stop this enforceability decision.

The Court should not resolve the reserved remedy question by saying either that the State must furnish a preferred placement in every case or that nominal willingness to pay always discharges its duty. If a violation is proved, relief must enforce the particular dated obligation effectively and remain within lawful authority. No finding of breach follows merely from the enforceability holding. No fixed waiting period, budget exception, automatic placement, unlimited home-service entitlement, facility-construction order, general program redesign, damages award or retrospective treasury payment is adopted.

## Frozen component dispositions and joins

| Component | Final Associate disposition | Supporting Associates | Precise scope |
|---|---|---|---|
| A. Covered assistance | Affirm individual-right recognition | Stevens, O'Connor, Scalia, Kennedy, Souter, Thomas, Ginsburg, Breyer | Section 1396a(a)(10)'s assistance command, with the adopted benefit and accepted eligibility, read with the operative section 1396d(a) payment definition and paragraph (15)'s actual category; no freestanding universal right from a definition |
| B. Reasonable promptness | Affirm individual-right recognition | Stevens, O'Connor, Scalia, Kennedy, Souter, Thomas, Ginsburg, Breyer | Section 1396a(a)(8)'s reasonable promptness for that covered assistance; no aggregate-program right or predetermined breach finding |
| C. Section 1983 channel | Affirm availability; reject asserted foreclosure | Stevens, O'Connor, Scalia, Kennedy, Souter, Thomas, Ginsburg, Breyer | No express exclusion or actual incompatibility established by section 1396c oversight and section 1396a(a)(3) hearings, considered together under Blessing and completed Rancho |
| D. Judgment and remedy | Affirm the Third Circuit's reversal of dismissal and return for further proceedings | Stevens, O'Connor, Scalia, Kennedy, Souter, Thomas, Ginsburg, Breyer | Restore the action; retain the lower court's express remedy reservation and all ordinary violation, causation, defendant, class and prospective-relief inquiries |

These are eight Associate votes on each component, not a final nine-member Court tally. Each Associate can join the common reasons at precisely the scope recorded in the individual rows and this table. Scalia and Kennedy may preserve their Blessing original-meaning funding-contract reservation without withholding those joins; the reservation neither supplies a dismissal ground nor creates an extra condition on these claimants. No author, published separate-writing decision or final opinion architecture is selected in this handoff.

The strongest opposing paths have been considered independently for each Associate. The plan-only and universal spending-statute routes fail under the actual supplied law. A no-right conclusion about a demand for immediate physical placement would not dispose of the narrower pleaded assistance right. The actual incompatible-remedy route recognized by Rancho remains lawful but is not established by these Medicaid mechanisms. A proposal expanding the rights or narrowing the remedy beyond the stated boundaries requires a new part-specific join assessment; no later assembly may treat the eight votes as agreement with such a proposal merely because the disposition remains affirmance.

## Precedent treatment supported by these commitments

- Blessing is applied, including the provision-specific right test, separate foreclosure burden, state-plan rule and requirement that relief follow a proved individual right and violation. Its rejection of general administrative adequacy remains intact.
- Wright and Wilder remain effective examples of particular statutory benefit rights and of the independent foreclosure inquiry. The former rent-and-utility and reimbursement obligations are not converted into a right to every Medicaid service. The individual Associates' verified joins and dissents are stated above rather than imputed.
- Suter retains its actual section 671(a)(15) and related provision-specific limits; the later state-plan statutes do not erase its preserved result or independently create the present right.
- Gonzaga retains its FERPA-specific result and fractured reasoning. Its four-Justice formulation is not made controlling or equated with a requirement for an independently intended private remedy.
- Bruneau preserves a statutory section 1983 channel absent actual incompatible displacement; recognition of the channel does not create the underlying right.
- Rancho is applied to actual remedial incompatibility and distinguished on the enacted mechanisms. Its direct thirty-day expedited siting action remains exclusive for the restrictions it adjudicated; no general express-remedy presumption follows.
- Sea Clammers and Smith v. Robinson retain foreclosure where Congress supplies a sufficiently comprehensive incompatible remedial scheme. No categorical exception for all administrative remedies is created.
- Dotson is consistent with the limited legal effect of restoring a prospective action and with separate consideration of the remaining right and remedial predicates. Its habeas-specific holding is not extended into a new Medicaid test.

## Freeze scope

Final independent modeling is complete with law effective before March 29, 2005, including the authorized March 7 and March 22 public supplements. There is no remaining chronological or general source-gap blocker. The specified merits and remedy questions left to further proceedings are adjudicative limits, not missing authorization. The original group-C exposure history remains preserved in the preflight: this context supplies no Sherrill or Jackson commitments. These bytes must remain unchanged after exposure to a comparator or a private present-case position; later reconciliation receives this frozen handoff as its input.
"""

# The opening source list and common premises remain date-specific; component C
# now includes each Justice's actual completed same-term public join.
assert text.count('**A — frozen commitment:') == 8
assert text.count('**B — frozen commitment:') == 8
assert text.count('**C — frozen commitment:') == 8
assert text.count('**D — frozen commitment:') == 8
for forbidden in ['NOT FROZEN', 'provisional commitment:', 'await the exact', 'pending exact Rancho', 'pending Rancho', 'Provisional convergence']:
    assert forbidden not in text, forbidden

preflight = """# OT2004 chunk 5 Sabree: completed neutral preflight

FROZEN SOURCE AND CUTOFF RECEIPT. This is the Sabree-only neutral/model handoff for the scheduled March 29, 2005 event. Independent modeling is complete. No historical reconciliation, private present-case position, final Court coalition or opinion assignment is included.

## Context boundary and prior exposure history

Authorized substantive inputs were the Sabree section of the original group-C neutral packet; the group-C entering-law and public-prior slices; the originally authorized current-public slice and neutral projection; and the subsequently authorized completed March 7 and March 22 public-only supplements. Engine sections 1–8 and 14–15 supplied governing modeling rules. The initial governing-file read returned some additional Engine text in a truncated output; it contained no withheld substantive decision material.

This context was previously retired from Sherrill and Jackson after predecision briefs incidentally disclosed historical Supreme Court petition-stage treatment. Those exposures are recorded in the original group-C preflight and source-only handoffs. No Sherrill or Jackson commitments were frozen here, and those matters were not substantively repaired in this context. That history is preserved rather than recast as complete blindness across the group.

Sabree preparation remained separate and clean: no present-case historical Supreme Court disposition, rationale, vote, petition treatment or comparator was acquired. No present-case private position, reconciliation, raw current-term Decision Record, private prior artifact or locked directory was consulted. Public prior opinions in authorized slices were used for the Associates' own adopted reasons and joins, not as private instructions. No repository-history command was run; no inventory or brief was changed. New writes remain within OT2004 research, runtime and freeze artifacts.

## Cutoff, participation and completed dependencies

Substantive cutoff: immediately before March 29, 2005. All nine Justices participate under the authorized intake; this handoff models only the eight Associates. The user's scheduled event is properly before the Court without reconstruction of a historical grant, docket or filing event. No same-date case supplies entering law.

The full March 7 public supplement was read. After regeneration, Shepard holding II was reread in its expanded form specifying the preserved omitted-charge consequence, the complete Rule 52(b) alternatives and the lawful jury-waiver route. It changes no Sabree rule or proposed vote. Dotson's unanimous opinion supplies an additional actual public position distinguishing the legal effect of restoring an action from a hoped-for substantive result, while preserving the remaining right, violation and remedy inquiries. Its habeas classification does not decide Medicaid foreclosure. Back, Ballard and Shepard add no pertinent Medicaid right or enforcement rule.

The full March 22 public supplement was read: Black Political Task Force, Brown v. Payton, Muehler and Rancho Palos Verdes. The first three do not change the Medicaid right or remedial-foreclosure inquiry. No generic vote tendency is inferred from their disagreements. The actual Rancho opinion is authored by Thomas and joined by all nine without a separate writing. It assumes a right, applies the defendant's burden of showing incompatibility, and forecloses an ordinary parallel section 1983 action because it would evade the direct personal action's thirty-day filing period and mandatory expedition. It rejects a general presumption based on any express remedy and distinguishes compatible funding administration. Every Associate's final Sabree component C expressly applies that completed holding. No provisional account or historical Rancho result substitutes for it.

There is no remaining chronological dependency. The static original neutral packet's statement that no effective later decision was identified has been superseded by these actual public supplements.

## Verified judicial record and actual unresolved merits

The entire official Third Circuit opinion, including footnotes and the separate concurrence, was read from the saved PDF and complete text extraction: 367 F.3d 180, May 11, 2004, https://www2.ca3.uscourts.gov/opinarch/031226p.pdf. The full opinion is the primary source, not an aggregator's summary. Its historical descriptions of post-divergence Supreme Court precedents do not replace supplied simulated law; its separate concurrence's prediction about a future Court supplies no Associate position.

The named beneficiaries' eligibility for Pennsylvania's adopted intermediate-care benefit and years on waiting lists are accepted at the enforceability stage. The official opinion describes the plaintiffs as a class, but does not supply an adjudicated basis here for a new particular common decree. Footnote 1 expressly reserves the financing-versus-furnishing-services question and leaves the remedy to the District Court. The appellate judgment reverses dismissal; affirmance restores the action. It does not establish every element of breach, causation, the precise class terms, clinical or payment arrangements, compliance options, or a timetable. These are ordinary further-adjudication issues, not a generalized source gap or a reason to stop the event.

## Official statutory text and preserved qualifications

Full official 2004 Code pages were saved in HTML and decoded text for 42 U.S.C. sections 1396a, 1396d, 1396c, 1320a-2, 1320a-10 and 1983. Each saved text supplies its primary URL. The script-copied statutory handoff includes the complete section 1396a(a)(10), section 1396d(a), the distinct timing, hearing and care-plan clauses, the facility definition, funding oversight, state-plan statutes and section 1983. Long statutory text was copied by script from those saved sources, not manually reconstructed. The full source pages retain amendment and effective-date notes.

The operative definition of medical assistance is payment of part or all of covered costs, with its actual timing, eligibility and excluded-institution conditions. Later additions concerning care and services themselves are excluded. Relevant amendment notes disclose no change to the asserted promptness command, payment definition or intermediate-care/care-plan provisions affecting this conduct and event. The 1999 cross-reference correction directs section 1396d(a)(15) to section 1396a(a)(31); unrelated 2004 benefit and premium provisions are not imported into these claims. The October 1994 state-plan statutes apply to these later proceedings and already receive their actual treatment in the supplied Blessing law.

Section 1396a(a)(10) and its definitions identify covered assistance and eligible persons; it is not a requirement that every State adopt every optional service. Pennsylvania's adopted intermediate-care coverage and these claimants' eligibility are accepted here. Section 1396a(a)(8) separately requires reasonable promptness in furnishing that assistance. Section 1396d(a)(15) defines the category and excludes an institution for mental diseases; it requires the need determination in accordance with section 1396a(a)(31). That paragraph requires a written plan of care before admission or authorization of benefits and regular independent professional review, including medical evaluation, of continuing need. Section 1396d(d) supplies facility purpose, prescribed standards and active-treatment conditions; its expenditure-maintenance provision concerns public-institution quarters before January 1, 1975, not an invented present eligibility bar.

Those conditions govern their actual statutory subject and stage. Active treatment is not converted into a prerequisite that waiting-list claimants already receive the treatment allegedly withheld before invoking accepted eligibility. No new finding of a missing care plan or need determination is inferred. A statute-defined payment right neither automatically awards a preferred placement nor decides that nominal willingness to pay always satisfies a proved obligation. Effective lawful compliance remains an actual remedial question.

Section 1396c provides notice and a state-agency hearing before findings of plan noncompliance or substantial administrative noncompliance, followed by withholding until the Secretary is satisfied the failure will end, with discretion to limit withholding to affected categories or portions. The substantial-compliance threshold for that federal remedy does not amend the individual timing command. Section 1396a(a)(3) separately supplies a fair hearing to an individual whose claim is denied or not acted upon with reasonable promptness. Both mechanisms, including their combined operation, are assessed; the individual hearing is not ignored as merely an audit. Neither mechanism establishes the actual conflict found in Rancho or another incompatibility with this pleaded prospective action. The reasoning does not require an express judicial mechanism in every imaginable foreclosure case and does not hold all administrative remedies incapable of exclusivity.

Sections 1320a-2 and 1320a-10 remove state-plan placement as a categorical obstacle, retain other individual-right requirements, and preserve Suter's section 671(a)(15) result. They do not independently create this Medicaid right. Section 1983 provides the existing express remedial channel; no separate implied Medicaid action is invented. Its special judicial-officer injunction restriction does not concern this official defendant.

## Own-Justice source sufficiency and adverse paths

The complete official Wright report, 479 U.S. 418, and Wilder report, 496 U.S. 498, including all separate writings and footnotes, were read. Primary URLs are https://www.govinfo.gov/content/pkg/USREPORTS-479/pdf/USREPORTS-479-418.pdf and https://www.govinfo.gov/content/pkg/USREPORTS-496/pdf/USREPORTS-496-498.pdf. Stevens's actual majority joins, O'Connor's Wright dissent joined by Scalia, and the Wilder dissent joined by O'Connor, Scalia and Kennedy supply specific competing understandings of the congressional entitlement. No Justice receives a vote in a case before joining the Court.

The authorized public priors supply unanimous Blessing and Scalia's concurrence joined by Kennedy; Thomas's four-Justice Gonzaga lead joined by O'Connor, Scalia and Kennedy; Breyer's Gonzaga concurrence joined by Souter; and the Gonzaga dissent joined by Stevens and Ginsburg. Supplied Suter and Bruneau holdings supplement those actual positions. The completed Rancho and Dotson public opinions supply each Associate's fresh same-term join. No historical general Gonzaga formula is substituted for its actual fractured in-world result.

All eight commitments address four distinct components, with each Justice's concrete own sources, a lawful adverse path, strongest objection, join barriers and remedy. The asserted statutory payment and timing rights are tested separately from a requested placement or service arrangement. The remedial scheme is compared in combination rather than inferred from the program label. Scalia and Kennedy's original-meaning reservation remains reserved; it is not turned into a categorical rule contrary to their full Blessing join. No author is selected.

## Readiness and freeze

Final independent component results: all eight Associates recognize the narrow covered-assistance right, recognize its reasonable-promptness requirement, reject the asserted section 1983 foreclosure under the actual completed Rancho rule, and affirm restoration for further merits and remedy proceedings. No Chief Justice vote or full-Court tally is supplied. The eight do not award immediate placement, a particular class decree, damages or retrospective treasury relief; they do not decide that every long wait violates the statute or that a nominal financing promise necessarily cures a proved violation.

Source and chronological preflight is complete. The precise remaining adjudicative questions belong to the affirmed remand and do not prevent freezing. The original pending artifacts remain preparation history. New Sabree-only freeze files and byte-identical runtime copies preserve this completed state; the frozen files govern any later reconciliation. No substantive revision may follow exposure to withheld comparator or private present-case material within this context.

## Input and source integrity

The following SHA-256 values identify the actual authorized input and principal verification bytes used at finalization. Paths are relative to the term folder. The March 7 value reflects the regenerated completeness-expanded version.

"""

hash_inputs = [
    'runtime/OT_2004CHUNK5_NEUTRAL_C.md',
    'entering-law/OT_2004CHUNK5_C.md',
    'entering-law/OT_2004CHUNK5_C_PUBLIC_PRIORS.md',
    'entering-law/OT_2004CHUNK5_CURRENT_PUBLIC.md',
    'entering-law/OT_2004CHUNK5_MARCH7_PUBLIC.md',
    'entering-law/OT_2004CHUNK5_MARCH22_PUBLIC.md',
    'workspace/neutral-projection.md',
    'research/chunk5-c/sabree_ca3.pdf',
    'research/chunk5-c/sabree_ca3.txt',
    'research/chunk5-c/sabree_prior_wright.pdf',
    'research/chunk5-c/sabree_prior_wilder.pdf',
    'research/chunk5-neutral/Sabree-statutory-excerpts.md',
] + ['research/chunk5-c/sabree_2004_' + n + '.txt' for n in ['1396a','1396d','1396c','1320a-2','1320a-10','1983']]
for name in hash_inputs:
    preflight += '- `' + name + '`: `' + hashlib.sha256((TERM/name).read_bytes()).hexdigest() + '`\n'

outputs = [
    ('OT_2004CHUNK5_SABREE_NEUTRAL_PREFLIGHT.md', preflight),
    ('OT_2004CHUNK5_SABREE_COMMITMENTS.md', text),
]
if '--stage-only' in sys.argv:
    for name, body in outputs:
        destination = TERM / 'research/chunk5-neutral' / (name.removesuffix('.md') + '_FINAL_DRAFT.md')
        destination.write_text(body, encoding='utf-8', newline='\n')
        print(destination.name, 'staged', len(body.encode('utf-8')), 'bytes')
    raise SystemExit(0)
targets = [TERM / folder / name for name, _ in outputs for folder in ['freeze','runtime']]
assert all(not p.exists() for p in targets), 'A final target already exists; do not overwrite an immutable handoff.'
for name, body in outputs:
    data = body.encode('utf-8')
    frozen = TERM / 'freeze' / name
    runtime = TERM / 'runtime' / name
    frozen.write_bytes(data)
    runtime.write_bytes(data)
    assert frozen.read_bytes() == runtime.read_bytes()
    print(name, 'bytes', len(data), 'SHA-256', hashlib.sha256(data).hexdigest())
