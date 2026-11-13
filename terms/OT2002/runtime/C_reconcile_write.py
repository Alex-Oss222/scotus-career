from pathlib import Path
import hashlib

term = Path('terms/OT2002')
source = term / 'freeze/OT_2002CHUNK3_C_COMMITMENTS.md'
original = source.read_bytes()
start = original.index(b'## 36. Norton')
end = original.index(b'## Source map and validation receipt')
retained = original[start:end]

prefix = '''# OT2002 chunk 3 — Group C reconciled commitments

## Reconciliation status and authorized scope

**Status:** All four matters are ready for assembly. Every Associate's frozen component disposition, operative ground, reservation and join barrier below is retained without a substantive change. No author, assignment or Chief Justice vote is supplied. No new neutral premise, amended claim, concession or factual finding is adopted.

This distinct historical-reconciliation context received the frozen C neutral packet and commitments, the C entering-law slice, the mandatory fresh-neutral validation and addendum for Meyer, and the C historical comparator. It did not receive the controlled position supplement, full brief, raw current-term Records or private control material. General model knowledge is not described as erased. The preserved neutral-source receipts establish the status of the lower-court records and the modeling stage's additional preconduct research. This stage independently read Meyer's complete historical syllabus and opinion, through its concluding disposition; it did not newly retrieve or claim a second complete reading of every underlying filing.

The retained component text below is copied directly from the frozen commitments. The reconciliation audit that follows identifies the relevant comparator, tests the legal and remedial grounds, and records the basis for retaining each Justice's position. The copied commitments' references to possible assembly action are prospective and are not assignments.

**Chronology and participation:** Stevens, O'Connor, Scalia, Kennedy, Souter, Thomas, Ginsburg and Breyer participate in all four matters. Norton and Newman use the law effective before January 15, 2003 independently of each other. Meyer uses law effective before January 22, 2003. Roe uses law effective before June 2, 2003; its personal-immunity notice inquiry remains fixed to July 10, 1999. All four scheduled matters are properly before the Court. No missing historical grant, docket or filing verification is a blocker.

## Retained frozen component commitments

'''

audit = '''## Historical reconciliation audit

### Norton — existing holdings control the facial questions

The historical anchor is the Sixth Circuit's July 31, 2002 affirmance, 298 F.3d 547. It supplies no Supreme Court merits vote or individual Associate position. The retained affirmance of the facial commerce and service-related expression challenges is consistent with that judgment, but rests on American Life League's actual controlling propositions and the present Lopez/Morrison architecture. The lower opinion's different articulation of commerce doctrine cannot replace that law.

The local, ideological character of a particular protest does not remove intentional direct interference from the actual interstate medical-services market identified by American Life League. The speech distinction addresses access-related force, threats and physical obstruction through their enacted predicates. It cannot make peaceful persuasion, offense, association or reduced demand an obstruction. The controlling intermediate-scrutiny rule and preserved nonobstructive communication answer the challenged service-purpose distinction. No new categorical commerce rule or criminal-threat rule is necessary.

Stevens, Souter, Ginsburg and Breyer's broader commerce positions in Morrison remain compatible with the sufficient direct-market ground they already joined. O'Connor, Scalia, Kennedy and Thomas's connection-before-aggregation commitments support the same result because this class has the required market connection. Kennedy's authorship and all eight Associates' joins in American Life League supply case-specific evidence, without predetermining authorship here. Scalia and Thomas's ACLA refusal to adopt an unnecessary constitutional culpability formula and Kennedy's distinct purpose-or-knowledge join remain intact; no Justice's ACLA attribution objection becomes a facial objection to FACE.

The limited mandate is essential. The Court's specified review reaches neither the separate ripeness ruling nor the warning letter's individual instructions. Thus all eight retain N1, N2 and N3 in full. No historical Justice departure exists and no changed commitment is warranted.

### Newman — protected entitlement does not predetermine process

The historical anchor is the Ninth Circuit's April 16, 2002 two-to-one judgment, 287 F.3d 786. That panel's division is not a Supreme Court alignment. Its reinstatement of the pleading-stage claim and express reservation of process and extraordinary circumstances are consistent with P1–P3. Its unnecessary suggestion that longstanding common-law property rights cannot be legislatively changed is not adopted.

The strongest competing route treats the removal authorization as a substantive definition of a limited burial interest. The retained result instead rests on the same law's continuing, enforceable objection right together with the disposition and gift rights. That is a substantive entitlement independent of a hoped-for notice procedure. Sullivan requires an actual entitlement and preserves it against procedural erasure; it does not require treating the coroner's lack of knowledge as extinguishing a refusal right the statute retains. Phillips separates ownership from market value and remedy. Neither case alone decides human-remains property. The combined statutory rights and pleading posture support the limited application here.

Stevens's Loudermill and Gilbert joins and his Sullivan concern for fair adjudication support recognition followed by an actual process inquiry. O'Connor, Scalia, Kennedy and Thomas's Phillips positions support honoring an existing legal interest despite nonmarket value, while their Sullivan positions require the exact retained entitlement. Souter and Ginsburg's Sullivan positions likewise distinguish actual substantive control from procedure alone. Breyer's Gilbert framework supports evaluating irreversibility and practical retrieval constraints together. These are independently sufficient bases for their retained votes; neither the panel's majority nor its dissent is imputed to an Associate.

All eight retain the join barriers against a universal body-property category, an immutable-property rule, an invariable consent requirement or an assumed emergency. The retained rights are subject to donor directions and the statutory claimant hierarchy. The different reasonable-contact provision for other tissue is not substituted for the corneal statute. The later amendment does not decide 1997 process.

Established procedure defeats the categorical Parratt/Hudson shortcut, not every conceivable postdeprivation justification. The actual Mathews assessment remains necessary, and Patsy's no-exhaustion rule does not itself prove a due-process violation. On the alleged planned and irreversible removal, the lower courts must determine actual urgency, contact opportunities, authorized consent and feasible safeguards. No final absence of urgency, lack of consent, inadequate process, institutional responsibility or damages is found. All eight retain P1–P3 without adjustment.

### Meyer — full same-matter comparator confirms the retained ordinary-law remit

The historical Supreme Court comparator is Meyer v. Holley, 537 U.S. 280, No. 01-1120, decided January 22, 2003. The complete syllabus identifies one unanimous opinion, and the complete opinion confirms ordinary agency and corporate principles, rejection of the circuit's control-alone and special nondelegable-duty rules, vacatur, and a remand allowing only arguments properly raised. Historical authorship is not carried into assignment.

The opinion's Part II requires an actual principal-agent or employer-employee relationship rather than control alone. It reads the former HUD regulation with its employee-or-agent and scope qualification and explains why the statute's important purpose cannot supply the omitted special personal duty. Its Part III rejects the California broker argument insofar as it rests solely on the right to control, while leaving the lower court to consider whether additional, properly raised aspects of that relationship establish ordinary agency. Veil piercing likewise remains subject to actual preservation and the applicable traditional requirements. These points confirm M1–M3 rather than supply a new automatic personal-liability theory.

The fresh validated neutral packet controls posture and source status: the reviewed judgment followed summary judgment certified under Rule 54(b); corporate and salesman claims remained pending; ownership in 1996 was disputed; no direct participation was alleged; compensatory attribution alone is in review. The historical opinion's simplified ownership account is not converted into a finding. Nor are newly encountered accounts of party concessions imported into neutral modeling. The retained result requires no such addition.

For each Associate, the historical position and operative grounds match the frozen result. Stevens and O'Connor's actual-attribution joins support corporate responsibility without automatic officer responsibility. Scalia's ordinary-background construction rejects an expansion based on purpose or isolated words. Kennedy's agency commitments preserve the corporation/individual distinction. Souter's Darden method supports common-law incorporation where Congress supplies no different rule. Thomas's Bestfoods opinion distinguishes ownership, derivative liability and direct statutory wrongdoing. Ginsburg's Bestfoods, Faragher and Ellerth joins preserve lawful remedies while rejecting a nonexistent individual-principal relationship. Breyer's Faragher and Bestfoods positions likewise permit effective remedies through actual agency and supported disregard of separateness. Their unanimous historical Meyer joins reinforce, rather than substitute for, these date-eligible grounds.

The simulated Faragher and Ellerth holdings differ from their historical counterparts in important employment details. Their common ordinary-agency premise remains compatible with Meyer, but their actual-authority/material-aid rules and reserved defenses are not imported as an FHA checklist or officer-liability rule. Darden remains an interpretive analogy, not an FHA holding; Ginsburg and Breyer are not attributed pre-service joins. Bestfoods does not select the state or federal veil-piercing rule.

M3's reference to other ordinary attribution includes only a genuinely preserved ordinary principal-agent claim, including any California broker relationship whose elements extend beyond title and control. It authorizes no invented allegation of personal discrimination, revived untimely claim, compulsory amendment, new discovery entitlement or finding of veil piercing. This is an explanation of the already recorded remit and barriers, not a new claim or change in commitment. All eight retain M1–M3. No Justice-specific historical departure exists.

### Roe — preserve the merits/notice division and the different claims

The historical anchor is the Fifth Circuit's July 17, 2002 judgment, 299 F.3d 395. It supplies no historical Supreme Court merits disposition or individual Associate vote. Its immunity conclusion therefore cannot be substituted for a Justice's independent assessment. The six-Justice notice position differs from that lower-court result, and the two-Justice position agrees with it; neither relationship alone validates a commitment.

R1 follows the acknowledged affirmative appointment and its objective interview scope, not a finding that the mother expressly invited Strickland through the doorway. It provides no consent to photography. R4 concerns the particular entry and examination acts and the claimants whose specific Fourth Amendment interests address them. It creates no general extinction of parental family liberty. R5 preserves Texas official immunity as a separate inquiry and does not restore the department or unappealed defendants. All eight directly support these distinctions.

For R2, the six independently examine the nonemergency intimate operation under the present Ferguson, Chandler and consent rules. A general protective purpose, a reporting duty or police contact is not dispositive. The degree and manner of intrusion, lack of asserted urgency and available lawful medical/judicial route support the ordinary-authorization rule on these assumed facts. Actual voluntary consent remains a factual issue. The disposition does not compel a finding that the mother refused, that Strickland threatened removal, or that liability is established. Scalia and Thomas's decision not to reach this merits question is compatible with the absence of compulsory merits-first sequencing; it supplies neither a constitutional join nor a conclusion that the search was lawful.

R3 requires a separate analysis under law existing before July 10, 1999. Hope supplies the adjudication method of objective fair warning through an obvious application, with attention to hierarchy and contrary authority. It does not itself supply conduct-date notice. Ferguson, Wallis, Calabretta, Tenenbaum and Saucier likewise supply no earlier notice. Wilson was already effective and requires particularized analysis without demanding a factual twin. No Justice adopts an actual-reliance substitute for the existing defense.

The six's strongest notice ground is the particular examination's excess under the preconduct bodily-privacy, scope and voluntary-consent rules shared even by the competing child-protection approaches. Darryl H. seriously undercuts a claim that every protective examination required a warrant, but retains scope/necessity limits, declines to make maternal assistance conclusive consent, and identifies a medical route for sexual-abuse examinations. Landstrom concerns a materially different nurse examination and a 1987 notice date. Wildauer concerns the investigative home visit. Doe v. Louisiana's Fourteenth Amendment holding and Fourth Amendment reservation require attention but do not affirmatively authorize the distinct assumed intrusion. The retained six-Justice rule does not deny those cases' actual immunity outcomes or turn a state protocol into federal law.

The two's strongest answer is that Darryl H. granted immunity despite serious necessity and consent doubts and that the local Fourth Amendment question remained expressly unresolved. In their assessment, the nonmedical photography distinction had not acquired sufficiently definite personal-damages consequences under the preconduct cases. The retained six-versus-two division reflects that actual dispute about the specificity and force of the existing warning, not different assumed facts or automatic preference for a broader or narrower rule.

| Justice | Reconciled notice position and Justice-specific basis |
|---|---|
| Stevens | Retain reversal. His Chandler and Vernonia search/no-waiver positions, disagreement with Wilson's immunity application, and Hope join support the obvious-excess application. He does not infer a universal child-search warrant rule from general privacy language. |
| O'Connor | Retain reversal. Her Robinette voluntariness analysis and Hope join support applying common consent and scope limits. Her Wilson and Saucier immunity positions remain a material counterweight, answered here by the assumed intrusion's excess even under special-needs balancing. No compulsory warning or categorical mixed-purpose rule is adopted. |
| Scalia | Retain immunity without reaching R2. His Anderson, Wilson and Saucier positions support treating the specific preconduct application as insufficiently settled despite his Chandler and Vernonia privacy rules. He does not find consent, approve the search, or exclude other-circuit law. |
| Kennedy | Retain reversal. His current operation-specific Ferguson rule supports R2; his preconduct Chandler and Robinette joins and subsequent Hope position support the distinct common-limits notice conclusion. Wilson and Saucier remain relevant and are distinguished by the assumed obvious excess, not disregarded. |
| Souter | Retain reversal. His Hope opinion requires confronting contrary authority and judicial hierarchy. Darryl H.'s actual limits and Doe's reservation support his distinction between an open categorical warrant question and an obviously excessive search. His Saucier position preserves the independent immunity inquiry. |
| Thomas | Retain immunity without reaching R2. His Wilson and Saucier immunity positions and accepted particularized-notice framework support the application-specific uncertainty. He accepts the substantive privacy limits but does not treat later clarification or intrusion severity alone as sufficient earlier notice. |
| Ginsburg | Retain reversal. Her Elder and Behrens opinions require all relevant preconduct law and proper assumed facts. Her Hope join permits the particular obvious-excess conclusion notwithstanding the open categorical question. Her Wilson join does not turn every disagreement into an automatic immunity rule. |
| Breyer | Retain reversal. His Johnson opinion preserves the legal/factual boundary, while his Vernonia, Chandler and Robinette positions distinguish supported protective operation from unrestricted bodily investigation. His Hope join supports the common-limits notice analysis without finding ultimate consent or liability. |

The six retain R2 and reversal on R3 on a shared sufficient rationale; Scalia and Thomas retain immunity and decline R2. The latter position has a substantive separate-writing function concerning conduct-date uncertainty, with authorship left to assembly. The disposition for the six affirms the entry and duplicative-due-process rulings, reverses the child's Fourth Amendment immunity judgment and remands. Any supplemental-jurisdiction decision must use the restored federal-claim posture. The two would affirm the federal judgment and preserve the independent state-law return. Neither path compels trial or damages.

## Final validation and assembly constraints

The reconciliation retains 8 Associate commitments on every Norton, Newman and Meyer component; 8 on Roe R1 and R4 and the independence of Texas immunity; 6 reaching and adopting Roe R2; and a 6–2 split on Roe R3. The two who decline R2 are not counted as dissenters on its constitutional rule. These are Associate counts only, not final Court totals. The full component tables above preserve every individual position and join barrier.

No same-matter historical Supreme Court Justice departure is found: Meyer matches; the other matters have only lower-court historical anchors. Roe's lower-court divergence is fully identified above, with both supported paths and each Associate's own grounds. No new neutral material requiring a fresh affected pipeline was needed. No adverse fact, urgency finding, consent finding, preservation finding, personal-participation claim or filing default has been introduced.

The mandatory Meyer fresh-neutral validation and addendum were used, preserving the earlier exposure receipt's provenance without using the excluded material for independent modeling. The C commitments remain unchanged in their authoritative source file. This handoff, identical in runtime and freeze, is the authoritative reconciled input for subsequent assembly; assembly must test any proposed opinion against these grounds and barriers and apply its separate assignment rules.

**Sources examined at this stage:** the authorized frozen C neutral packet and commitments; C entering-law slice; C comparator; C preflight receipt; Meyer portions of the fresh-neutral validation and addendum; and the complete [Meyer syllabus](https://www.law.cornell.edu/supct/html/01-1120.ZS.html) and [opinion](https://www.law.cornell.edu/supct/html/01-1120.ZO.html), supplied as saved text. The neutral and commitment source maps retain the status and locations of the previously verified lower opinions and preconduct sources. No new quotation, unsupported historical fact or modern doctrine is supplied by this audit.
'''

data = prefix.encode('utf-8') + retained + audit.encode('utf-8')
targets = [term / 'runtime/OT_2002CHUNK3_C_RECONCILED.md', term / 'freeze/OT_2002CHUNK3_C_RECONCILED.md']
for target in targets:
    target.write_bytes(data)
assert targets[0].read_bytes() == targets[1].read_bytes()
assert source.read_bytes() == original
assert retained in data
for banned in (bytes([79,110,101,68,114,105,118,101]), bytes([71,105,116,72,117,98]), bytes([102,105,108,101,58,47,47]), bytes([67,58,92,85,115,101,114,115,92])):
    assert banned not in data, banned
print('C reconciled handoffs identical; frozen commitments unchanged.')
print('bytes=' + str(len(data)))
print('sha256=' + hashlib.sha256(data).hexdigest())
