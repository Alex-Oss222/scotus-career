from pathlib import Path
import hashlib

base = Path('terms/OT1999')
freeze = base / 'freeze'
neutral_path = base / 'runtime/OT_1999CHUNK6_NEUTRAL.md'
objective_path = freeze / 'OT_1999CHUNK6_OBJECTIVE_RECORD_EXTRACT.md'
neutral = neutral_path.read_text(encoding='utf-8-sig')

def read(path):
    return path.read_text(encoding='utf-8-sig')

def hash_file(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def section(text, start, end):
    return text.split(start, 1)[1].split(end, 1)[0].strip()

def freeze_packet(key, text, sources, validation):
    packet = freeze / f'OT_1999CHUNK6_{key}_NEUTRAL_VALIDATED.md'
    receipt = freeze / f'OT_1999CHUNK6_{key}_NEUTRAL_VALIDATION.md'
    if packet.exists() or receipt.exists():
        raise SystemExit(f'Refusing to overwrite frozen {key} handoff')
    packet.write_text(text, encoding='utf-8')
    receipt_text = f'# {key}: fresh neutral validation receipt\n\n{validation}\n\n'
    receipt_text += 'The validator received no current matter historical Supreme Court outcome, comparator, Stone supplement, commitment, reconciliation, raw Record, ledger, control validation or private core. No Git command was used. This receipt validates neutral framing and source scope only and supplies no vote. A distinct independent context performs modeling.\n\n## Integrity receipts\n\n'
    for path in [neutral_path, *sources, packet]:
        receipt_text += f'- `{path.as_posix()}` — SHA-256 `{hash_file(path)}`\n'
    receipt.write_text(receipt_text, encoding='utf-8')
    print(packet.as_posix())
    print(receipt.as_posix())

roster = '''The supplied public institutional setting identifies the seated nine-member Court: Stone-Zsela, Stevens, O'Connor, Scalia, Kennedy, Souter, Thomas, Ginsburg and Breyer. No case-specific nonparticipation or roster change is supplied. Six qualified Justices constitute a quorum; the majority of participants determines an appellate judgment. No recusal is invented. The modeling stage addresses only the eight Associates.\n\n'''

carmell_law = base / 'entering-law/OT_1999CHUNK6_CARMELL.md'
carmell_sources = [base / f'sources/chunk6-neutral/{name}-official.txt' for name in ['collins','hopt','thompson-missouri','calder']]
carmell_objective = section(read(objective_path), '## Carmell v. Texas', '## Fischer v. United States')
carmell = '''# Carmell v. Texas: freshly validated neutral packet

Engine stage 3A only. No proposed judgment, vote or opinion assignment. The cutoff is immediately before May 1, 2000. This packet replaces the original neutral brief's outcome-suggesting issue title and its unconditional description of evidentiary insufficiency with the disputed-record qualification below.

## Event, posture and scope

Carmell v. Texas, No. 98-7540, is before the Court on certiorari to the Texas Court of Appeals, Second District. Argument/submission is November 30, 1999; the supplied decision calendar is May 1, 2000. The question is whether applying the 1993 Article 38.07 amendment to the challenged earlier offenses violates the Ex Post Facto Clause by reducing the proof legally sufficient for conviction. The appellate court sustained the amendment's application while assuming lack of corroboration for its legal analysis. The defendant seeks relief from the affected convictions; Texas defends the judgment and separately preserves its contention that corroborating evidence existed. No other threshold defect or recusal is established. The question is not whether every retrospective rule of evidence is invalid.

'''+roster+'''## Validated objective record recitations

The following bounded extract is copied mechanically from the supplied objective handoff. It is accepted as a published record recitation under Engine 14(2), not as an independent examination of the underlying state trial record or the source opinion's current historical reasoning. The linked current Supreme Court sources may not be opened by the independent model; this extract alone supplies their permitted objective facts.

'''+carmell_objective+'''

## Entering-law distinctions

Article I, section 10's prohibition applies to state penal legislation. Calder v. Bull, 3 U.S. (3 Dall.) 386 (1798), rejected an Ex Post Facto Clause challenge to a civil probate rehearing; Chase's four-category explanation includes retrospective reduction of the evidence legally required for conviction. That category's authority and limits must be read through the later controlling cases, rather than treating every phrase of an individual seriatim opinion as an unlimited rule.

Collins v. Youngblood, 497 U.S. 37 (1990), allows the later correction of an unauthorized fine while preserving an otherwise lawful conviction and life sentence. Its majority rejects a free-standing rule against every retrospective loss of a substantial procedural protection, reiterates Calder's categories and says a procedural label does not immunize a prohibited change. Its footnote 3 distinguishes new evidentiary rules and invokes Hopt and Thompson v. Missouri; it cannot be read as either a categorical ban on all new evidence or an express decision about this corroboration amendment. Collins overrules Kring and Thompson v. Utah's Ex Post Facto reasoning. Those overruled propositions must not be revived through their quotation in an older case.

Hopt v. Utah, 110 U.S. 574 (1884), permits removing a convicted felon's witness incompetency for a later trial of an earlier offense, while distinguishing changes that lessen the amount or degree of proof essential to conviction. The opinion's separate trial-presence, hearsay, jury-function and confession rulings do not decide Carmell. Thompson v. Missouri, 171 U.S. 380 (1898), permits admitting genuine handwriting exemplars for comparison: the ultimate facts, reasonable-doubt burden and jury's assessment remain. It does not approve a legislature directing a lesser quantum of proof sufficient; its reliance on the older Kring/Thompson v. Utah formulations is qualified by Collins.

The defendant's supported path characterizes Article 38.07 as an independent sufficiency condition: the complainant could testify under either version, but the older law did not permit conviction on that testimony alone absent the prescribed timely report or age exception. On the assumed record, the amendment removes the additional proof formerly indispensable. Hopt's witness-competence change and Thompson's new admissible exemplar can therefore be distinguished without freezing ordinary trial practice.

The State's supported path characterizes the amendment as removal of a witness-specific credibility handicap comparable to a competence or admissibility restriction, leaving the offense, permissible sentence, elements, ultimate facts and reasonable-doubt standard unchanged. Collins forecloses relying merely on disadvantage or a procedural protection's importance. The principal obstacle is the described state-law sufficiency consequence: the witness was already competent, and repeal may make a previously inadequate evidentiary basis legally enough. The precise constitutional significance of that difference remains for independent assessment.

The strongest response to the defendant is that many permissible evidence rules improve the prosecution's prospects and no defendant possesses every offense-date trial rule. The strongest response to Texas is that a distinction between new evidence becoming available and the existing evidence becoming legally sufficient need not equate every disadvantage with a constitutional violation. These are supported analytical alternatives under Engine 14(4), not invented historical briefs, concessions or a selected outcome.

## Date-eligible judicial positions

Collins's Court opinion was joined by O'Connor, Scalia and Kennedy among the currently seated Associates. They adopted its rejection of the broader substantial-protection theory, its Calder discussion and its concrete evidentiary qualifications. Stevens's concurrence, joined by Brennan and Marshall, preserves broader concern for substantial safeguards used to obtain a valid conviction or sentence, but agrees that the removable sentencing fine and new corrective remedy did not impair those protections. His separate ground is published evidence of his position; it is not controlling law and supplies no current vote. The other current Associates did not participate in Collins. Their current assessments must rest on actual available jurisprudence and the permitted simulated law, not invented joins.

Morales and Garner, copied below, govern the actual withdrawal of meaningful parole consideration. They identify the force and limits of existing simulated ex post facto law but do not decide trial corroboration, supply a new probability test for conviction or turn procedural disadvantage alone into a violation. The independent model must assess each Justice under the trial-proof question rather than mechanically transfer the parole coalitions.

## Remedy and uncertainties

Counts 7–10 alone are challenged. The six under-fourteen counts and five post-amendment counts, including the life-sentence counts, are unaffected by this review. If the amendment cannot govern the four earlier counts, the State's preserved corroboration contention requires disposition on the actual record under the older rule. The packet establishes neither actual corroboration nor its final absence. The described state sufficiency consequence permits no automatic new opportunity to add deficient prosecution proof; it does not permit this Court to order acquittal without resolving a material preserved sufficiency contention. A lawful remand must identify that task. If the amendment is constitutionally permissible, that conclusion defeats this federal challenge without adjudicating unpresented issues.

The source map establishes age, reporting and temporal predicates through the supplied official recitation. No underlying deposition, trial transcript, original briefing or fresh evidentiary finding is represented as read. No current Supreme Court outcome or rationale is imported. The available original source files may support additional neutral extraction through the proper separate context if a selected path needs more detail.

## Sources read for pre-divergence law

The complete relevant opinions in Calder, Hopt, Thompson v. Missouri and Collins, including Collins's footnotes and Stevens concurrence, were read from official Library of Congress reporter PDFs transcribed to text. The saved source receipts identify their official URLs and page counts. OCR imperfections are not corrected into invented quotations; no long exact quotation is retyped here. These are actual pre-divergence authorities. The packet uses their legal distinctions without importing a current Carmell comparator.

## Mechanically copied simulated entering law

'''+read(carmell_law)
freeze_packet('CARMELL', carmell, [objective_path,carmell_law,*carmell_sources], 'Validated the supplied objective Carmell recitations without opening the historical current-matter opinion. Material qualifications retained: assumed rather than finally found lack of corroboration; counts 7–10 only; six-month/one-year report limits and under-fourteen/under-eighteen exceptions; independent corroboration contention; no automatic repair trial. Read all four supplied pre-divergence opinions and the Carmell entering-law slice. No unresolved neutral-framing defect prevents independent modeling at this scope.')

mining_law = base/'entering-law/OT_1999CHUNK6_MINING.md'
mining_supp = base/'preparation/chunk6-mining-neutral-supplement.md'
mining_lower = base/'sources/chunk6-neutral/mining-lower.txt'
mining = '''# National Mining Association: freshly validated neutral packet

Engine stage 3A only. No proposed vote or outcome. Event cutoff: May 8, 2000. The source-supported supplement below replaces the original short brief's incomplete account of the rule, relief and finality. Its strongest paths are analytical alternatives, not assumptions about filings or a selected outcome.

## Authorized event and review boundary

National Mining Association v. United States Department of the Interior, 177 F.3d 1 (D.C. Cir. 1999), is a post-grant review of the federal appellate judgment. The supplied calendar sets grant February 22, 2000, argument/submission April 4, and decision May 8. These are authorized calendar premises. No historical Supreme Court petition treatment or unprovided docket is imported. The two granted questions concern (1) continued ownership/control permit consequences after the relationship ends and (2) retroactivity or asserted reopening based on pre-rule conduct. The short brief's generic petitioner-relief description cannot identify a historical petitioning party or enlarge the grant.

'''+roster+'''## Independent validation findings

The full lower opinion and all fourteen footnotes support the supplement's distinctions. The ordinary present-control provision and the separate former-control willful-pattern provision must remain distinct. In the latter, willfulness, pattern, nature and duration, resulting irreparable environmental damage, and indication of intent not to comply are all necessary terms; ordinary past ownership alone is not that statutory condition. The cure alternative includes violations in the process of correction to the satisfaction of the authority with jurisdiction, rather than requiring completion in every case.

The review source sustains general authority to suspend or rescind an improvidently issued permit. It does not identify a particular final agency merits adjudication whose reopening is before the Court. The proposed question therefore cannot be used to manufacture a final judgment, erase section 1211(c), or apply the Article III final-judgment rule to a different institution and posture. The source also preserves state-primacy procedures and unpresented procedural-rule disputes.

The lower court's retroactivity ruling concerns both pre-November 2, 1988 violations and pre-rule acquisition of control. Its footnote 12 expressly excludes a post-rule assumption of control merely because the underlying violation was older. Present violation, present application, completed control transaction and the actual new legal disability are separate matters for the model. Smiley permits qualified current statutory interpretation for antecedent transactions and therefore prevents treating every interpretation chosen after conduct as automatically forbidden legislative retroactivity; it does not create universal permission to add disabilities.

The source's current-rule proposals do not establish enactment, replacement or mootness. The supplied record supports the bounded statutory and retroactivity issues. Any specific permit-finality ruling or enlargement into separate appeals requires additional support.

## Validated source-supported supplement

'''+read(mining_supp)+'''

## Chronology validation

The supplied slice includes Christensen, effective May 1, unlike the uncoordinated May 1 matters themselves. No substantive May 1 decision from this packet is presumed completed. Before modeling or later reliance, the operator must check whether actually completed earlier chunk-6 public law adds any relevant rule. No presently identified unresolved early question is a necessary mining predicate. The snapshot cannot be retroactively treated as including later uncommitted law.

## Mechanically copied entering law

'''+read(mining_law)
freeze_packet('MINING',mining,[mining_supp,mining_lower,mining_law], 'Validated the full lower opinion including all fourteen footnotes against the neutral supplement and the material entering-law distinctions. The bounded grant is ready for independent modeling, subject to the ordinary effective-law refresh after any materially relevant earlier event. No particular final permit or post-control universal exemption is assumed; cure, willful-pattern, retroactivity and unpresented-component limits are explicit.')

saenz_law = base/'entering-law/OT_1999CHUNK6_SAENZ.md'
saenz_supp = base/'preparation/chunk6-saenz-neutral-supplement.md'
saenz_lower = base/'sources/chunk6-neutral/saenz-lower.txt'
saenz_positions = [base/'entering-law/OT_1999CHUNK6_SAENZ_PINDER_PUBLIC.md', base/'entering-law/OT_1999CHUNK6_SAENZ_LEWIS_PUBLIC.md']
saenz = '''# Saenz v. Heldenfels Brothers: freshly validated neutral packet

Engine stage 3A only. No vote, judgment or assignment. Current-law cutoff: May 9, 2000. Individual conduct-time notice cutoff: June 19, 1995. The supplement below replaces the original brief's missing date and incomplete account of the evidence and lower grounds.

## Authorized event and review boundary

Saenz v. Heldenfels Brothers, Inc., 183 F.3d 389 (5th Cir. 1999), reviews summary judgment for Deputy Beto Gonzalez and Brooks County. The user-authorized post-grant proceeding needs no invented historical Supreme Court petition or docket. The assigned grant is February 7, 2000; argument/submission March 27; decision May 9. The question asks whether an officer's direction that another officer leave a dangerous third party undisturbed can be state creation or enhancement of danger to later unidentified victims under DeShaney. Plaintiffs seek vacatur of the adverse constitutional judgment and further proceedings; no established liability or damages amount is supplied.

'''+roster+'''## Independent validation findings

The complete lower opinion and all eight notes support the June 19, 1995 date, fifteen-minute interval, rank-based instruction, plaintiff-favorable account, absence of concrete pre-stop intoxication proof and later .21 test. The instruction is not an adjudicated fact merely because it must be accepted for this summary-judgment review. The driver and victims were not in custody at the relevant point. The specific victims were not known to Gonzalez, and the record identifies no obstructed private-rescue effort. These are material distinctions from the supplied Pinder and restraint precedents, not findings disposing of every possible affirmative-interference claim.

The individual and county judgments both rest below on absence of a constitutional deprivation. The lower court did not independently resolve every conduct-time immunity question. Personal immunity therefore cannot automatically sustain the county's judgment if the federal-deprivation ground is vacated. Conversely, pleaded custom, senior rank and the later injury do not prove policy attribution, causation or culpability. The private company in the caption is not an appellee on this federal appeal; state-law severance and remand remain independent.

Pinder preserves affirmative deprivation of otherwise available private protection; it does not already hold that a superior's decision to halt a junior officer's proposed discretionary police investigation is that deprivation. The model must examine that analogy rather than silently substitute public protection for the private protection reserved in Pinder. Likewise Stemler's actual restraint and involuntary transfer cannot be transformed into a general noncustodial rule, and Lewis's rapid-pursuit standard cannot be made universal merely because the later injury involved a vehicle.

The additional public Pinder and Lewis excerpts supply their separate positions. Ginsburg's Pinder dissent, joined by Stevens, Souter and Breyer, requires sufficiently culpable actual displacement of otherwise available protection, with causation and notice considered separately. Scalia and Thomas's Lewis position rejects adequate support for the particular reckless-pursuit constitutional right without categorically excluding direct intentional assaults outside custody. Stevens's Lewis immunity-only ground and Breyer's sequencing flexibility are also preserved. These prior opinions identify positions; they supply no vote here and no retroactive June 1995 notice.

The bounded merits question is ready. If the independent model chooses personal immunity as an independently sufficient ground, it must examine the actual relevant June 19, 1995 authorities, including the invoked Ross and Salas sources, and not rely on later Pinder, Uhlrig, Lewis, Lanier or Stemler as notice. The lower court's citations and summaries preserve those possible sources; they do not substitute for further source review if their precise scope determines the result.

## Validated source-supported supplement

'''+read(saenz_supp)+'''

## Chronology and source limits

The current neutral law includes Doe v. Rosenberg at its actual private-attribution scope; its separate medical setting supplies no finding about this police conduct or the absent private party. No uncommitted earlier chunk-6 result is presumed. Refresh materially relevant current law before modeling when necessary. The lower opinion is a sufficient published record recitation under Engine 14; the original deposition and trial record are not represented as read. Additional factual findings or a county-custom sufficiency decision cannot be reconstructed from the derivative lower rationale.

## Mechanically copied entering law

'''+read(saenz_law)
for path in saenz_positions:
    saenz += '\n\n## Mechanically copied additional published position\n\n'+read(path)
freeze_packet('SAENZ',saenz,[saenz_supp,saenz_lower,saenz_law,*saenz_positions], 'Validated the full lower opinion and all eight footnotes, the supplement, governing law and relevant separate-position passages. Ready for independent modeling at the granted merits scope. The incident-date gap is resolved; possible independently sufficient immunity requires its own actual conduct-time source assessment. The affirmative-private-protection/public-nonenforcement distinction, plaintiff-favorable record, separate county predicate and state-claim remand are preserved.')
