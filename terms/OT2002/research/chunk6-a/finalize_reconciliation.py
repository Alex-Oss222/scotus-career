from pathlib import Path
import hashlib

base = Path('terms/OT2002')
partial = (base / 'runtime/OT_2002CHUNK6_A_OTHER_RECONCILED.md').read_text(encoding='utf-8')
supplement = (base / 'freeze/OT_2002CHUNK6_A_SMITH_SUPPLEMENT_COMMITMENTS.md').read_text(encoding='utf-8')

def part(start, end):
    return partial[partial.index(start):partial.index(end, partial.index(start))].rstrip()

bach = part('## United States v. Bach', '## United States v. Wheat')
wheat = part('## United States v. Wheat', '## United States v. Buckland')
buckland = part('## United States v. Buckland', '## Partial handoff validation')
smith = supplement[supplement.index('## Additional facts'):supplement.index('## Completion checks')].rstrip()

def replace_once(old, new):
    global smith
    assert smith.count(old) == 1, (old[:90], smith.count(old))
    smith = smith.replace(old, new, 1)

replace_once('## Final Justice-specific commitments', '## Reconciled Justice-specific commitments')
replace_once(
    "Stevens, Ginsburg and Breyer likewise do not rest their punitive conclusion on codification alone. They can accept the intended civil public-protection character and find the clearest proof in the actual combined lifetime operation. The plea and judgment provisions strengthen the connection to the completed criminal adjudication but do not establish a sentencing term by themselves. Their conclusion survives the more precise account of public access for the reasons below.",
    "Stevens, Ginsburg and Breyer likewise do not rest their punitive conclusion on codification alone. They find the clearest proof in the actual combined lifetime operation even assuming the asserted civil intent. Ginsburg and Breyer preserve their separate assessment that the actual intent markers are ambiguous; their sufficient alternative under the demanding standard does not supply a join in the four reversal supporters' clear-civil-intent finding. Stevens can join the common effects ground without needing the actual intent characterization to decide his result. The plea and judgment provisions strengthen the connection to the completed criminal adjudication but do not establish a sentencing term by themselves. Their conclusion survives the more precise account of public access for the reasons below.")
replace_once(
    "Respondents still must establish that the challenged retrospective measure imposes punishment. The content and implementation persuade him that they have not established that conclusion even on this less deferential route.",
    "Respondents still must establish that the challenged retrospective measure imposes punishment. This remains a close balance of substantial punitive and civil indications for Souter. The ordinary presumption of constitutionality resolves the remaining doubt in the State's favor; he does not demand the heightened clearest-proof override or affirmatively find that the evidence unambiguously validates the scheme. The content and implementation support that bounded conclusion that respondents have not established punishment on the less deferential route.")
replace_once(
    "His decisive operational grounds are the record's noncustodial reporting arrangement, absence of compulsory in-person supervision or direct conduct prohibitions, the continuing informational protective function, and the accessible search service rather than forced public confrontation.",
    "The civil indications that prevent a punitive conclusion in this close balance are the record's noncustodial reporting arrangement, absence of compulsory in-person supervision or direct conduct prohibitions, the continuing informational protective function, and the accessible search service rather than forced public confrontation.")
replace_once(
    "Reverse the ex post facto judgment on an independent ambiguous-intent/direct-effects ground. Join the abstract sequential framework, but withhold the finding of clearly established civil intent and its clearest-proof application to this Act.",
    "Reverse the ex post facto judgment on an independent ambiguous-intent/direct-effects ground, with the ordinary presumption of constitutionality resolving the close balance. Join the abstract sequential framework, but withhold the finding of clearly established civil intent and its clearest-proof application to this Act.")
replace_once(
    "Her judgment and combined-operation ground remain unchanged. She does not adopt independent registration-only invalidity, an automatic privacy-to-punishment inference or a new hearing system.",
    "Her judgment and combined-operation ground remain unchanged. Reconciliation preserves her ambiguous-intent assessment and treats clearest-proof satisfaction as an independently sufficient alternative even assuming civil intent, not a finding that the mixed intent evidence is clearly civil. She does not adopt independent registration-only invalidity, an automatic privacy-to-punishment inference or a new hearing system.")
replace_once(
    "He accepts the civil-intent premise and finds its demanding rebuttal satisfied; he need not join Souter's less deferential route.",
    "He preserves the ambiguous-intent assessment shared with Ginsburg, while finding the demanding rebuttal satisfied even assuming civil intent. That independently sufficient alternative does not require joining Souter's nonpunitive effects conclusion.")
replace_once(
    "**Established civil-intent rationale:** O'Connor, Scalia, Kennedy and Thomas directly support finding civil intent established, applying the clearest-proof standard and rejecting the ex post facto claim under that analysis. Stevens, Ginsburg and Breyer accept the intended civil character and the same demanding standard but find punitive combined operation. Those seven share that framework and initial classification while disagreeing on its application. The four nonpunitive applications do not become five by adding Souter's judgment vote.",
    "**Common sequential method and distinct applications:** All eight accept examination of intended character followed by a real cumulative purpose-and-effect inquiry; an established civil choice receives the demanding clearest-proof override. O'Connor, Scalia, Kennedy and Thomas directly support finding civil intent established here, applying that standard and rejecting the ex post facto claim. Souter withholds the clear-civil-intent finding and heightened-deference application. Ginsburg and Breyer preserve ambiguity of intent but find punishment under direct effects review and, independently, even assuming civil intent under the clearest-proof standard. Stevens joins the latter sufficient cumulative-effects ground without requiring an actual civil-intent holding. There are four Associate full joins to the nonpunitive civil-intent rationale, not seven joins to its actual intent predicate and not five joins to its application. Souter's judgment vote adds neither missing proposition join.")
replace_once(
    "His independent direct-effects analysis supplies a judgment vote for reversal. His concurrence must explain why the new enactment facts make the intent characterization ambiguous and why the clarified operation nonetheless fails to establish punishment.",
    "His independent direct-effects analysis supplies a judgment vote for reversal. His concurrence must explain why the enactment facts make the intent characterization ambiguous, why the actual effects leave a close balance, and why the ordinary presumption of constitutionality resolves the remaining doubt for the State.")
replace_once(
    "The other seven retain their legal routes after treating those same facts as described in their rows.",
    "O'Connor, Scalia, Kennedy and Thomas retain their complete legal route; Stevens retains the sufficient cumulative-effects ground. Reconciliation further qualifies Ginsburg's and Breyer's intent joins: their historical ambiguous-intent assessment remains supported by the unchanged enactment facts, while this timeline's prior actual-operation holdings support their punitive conclusion even under the demanding standard. They therefore do not join an affirmative clear-civil-intent finding. Souter's direct-effects position is clarified as a close-case conclusion with the ordinary presumption of constitutionality supplying the residual rule of decision, rather than a confident affirmative validation.")

intro = '''# OT2002 chunk 6 A — reconciled non-Stone commitments

## Scope, authoritative handoffs and readiness

This is the completed historical-reconciliation handoff for United States v. Bach, Smith v. Doe, United States v. Wheat and United States v. Buckland. It supplies eight Associate Justices' reconciled disposition and proposition commitments, exact remedy positions, strongest objections, supported alternative grounds, join barriers and writing functions. It makes no assignment and supplies no controlled-position vote or assembled Court judgment.

The original frozen A neutral/preflight/commitments, Bach validation, Smith source and rehabilitation facts and validation, participation handoff, A comparator, A entering law and relevant prior-public selections were reviewed. After complete Smith source reading identified additional operation and intent facts, control produced SMITH_OPERATION_FACTS, a separate clean context validated them in SMITH_OPERATION_VALIDATED_NEUTRAL, and a fresh independent context produced A_SMITH_SUPPLEMENT_COMMITMENTS. Those supplemental commitments replace the original Smith modeling rows for this reconciliation; the original freeze remains unchanged. The other three matter sections are retained verbatim from the completed partial reconciliation. Prior published Ursery and Kurth Ranch entries were also read at their bounded public scope, along with the prior-public Hendricks, Hudson, W.P., Jones and entering-law Seling, Paul P., Angle, Harris and other relevant selections.

No private controlled supplement, full current brief, current raw Decision Record, assignment material or assembly product was opened. General model knowledge is not represented as erased. Research cutoffs are March 5, 2003 for Bach, Smith and Wheat, and March 10, 2003 for Buckland. Unrelated same-day results do not enter through processing order. All nine participate under the frozen neutral handoff, and the supplied full-merits review and event scheduling premises are accepted.

The Smith source verification read the complete Cornell syllabus, majority, Thomas concurrence, Souter concurrence, Stevens dissent and Ginsburg dissent, including every footnote. The official Reports text, 538 U.S. 84, independently confirms the complete historical topology and the material separate-writing grounds and footnotes. The short comparator omitted Thomas's concurrence; this handoff corrects that omission. No historical author or join is imported as a present assignment. Source verification supplies comparison evidence, while every material new neutral fact was routed through the fresh stages stated above.

All four matters are ready for assembly. All Associate judgment votes remain unchanged. Smith's proposition alignment is refined below: four full supporters of the nonpunitive civil-intent application; Souter supports reversal through a distinct close-case route; Stevens, Ginsburg and Breyer support the punitive combined-operation ground, with Ginsburg and Breyer retaining intent ambiguity and supporting the demanding-standard analysis as an alternative. No unsupported seven-Associate clear-intent coalition remains.
'''

smith_intro = '''## Smith v. Doe — March 5, 2003

The substantive supplemental modeling conclusions follow, with the explicitly identified reconciliation refinements to intent support and Souter's close-case ground. The source supplement and original commitments are preserved unchanged in their own files. These are final non-Stone commitments for assembly, not a final opinion topology chosen by historical authorship.
'''

smith_annex = '''## Smith historical reconciliation and exact proposition support

### Verified historical topology and grounds

Historically the Court reversed and remanded, six to three. Kennedy wrote an opinion joined by Rehnquist, O'Connor, Scalia and Thomas. Thomas also concurred, limiting his analysis to obligations imposed by the statute and objecting to implementation-based review of Internet dissemination. Souter concurred only in the judgment: he found the intent evidence mixed, declined special clearest-proof deference, found substantial punitive and civil indications in close balance, and relied on the ordinary presumption of constitutionality. Stevens dissented on a broader liberty-based account in which severe obligations triggered necessarily and sufficiently by conviction constitute punishment. Ginsburg, joined by Breyer, found intent ambiguous and punitive effects, with the lack of any response to rehabilitation carrying particular force. Her footnotes state the Mendoza-Martinez indicators and adopt Souter's response to the occupational-disability analogies. Stevens's footnote identifies the separate Connecticut case; that case and its disposition are not part of this review. Souter's footnote discusses evidence from other notification regimes; it does not supply a new finding of harm to these respondents.

The majority's full historical rationale does not become present governing law. Its approval of Hendricks custody and Hudson's statutory-face formulation are displaced in this timeline. The current nonpunitive commitments therefore do the actual-operation work required by the published holdings; they cannot rely on those historical propositions as if unchanged. All historical record details used substantively here are within the validated neutral handoffs. Historical general recidivism formulations, later law and unvalidated additional factual claims supply no premise.

### Justice-specific comparison and retained alternatives

| Justice | Historical evidence and present reconciliation | Concrete law or position bearing on the result and scope |
|---|---|---|
| Stevens | The judgment direction matches. His historical broader conviction-trigger/liberty theory supports the narrower cumulative lifetime holding he already accepted in modeling. No separate broader holding or second dissent is necessary to sustain his actual disposition. | His published W.P. dissent classifies affirmative offense-triggered notification as punitive even with greater safeguards. His Hendricks and Hudson joins supply adopted cumulative actual-operation analysis. Those prior positions support joining the common stronger-than-necessary effects ground while preserving the distinction between a conviction and compulsory current-information maintenance. His historical broader theory does not enlarge the case's disposition beyond these respondents. |
| O'Connor | Retain reversal and a full join in the bounded nonpunitive application. Her historical position is strong evidence; the changes in earlier law alter the analysis she must perform but do not compel a different result. | Her Hendricks dissent accepts a genuine-effects inquiry and demanding proof while finding serious civil burdens insufficient on that record. Her Hudson and W.P. joins permit protective regulation while weighing actual adverse effects. The noncustodial searchable registry, no in-person reporting and absence of direct conduct restraints support the current result after, not instead of, that inquiry. |
| Scalia | Retain reversal and full support for the present common rationale. His historical majority join supplies supporting evidence, while his distinct Double Jeopardy theory provides no substitute ground in this Ex Post Facto case. | His Hendricks dissent and W.P. position accept genuinely civil protection; his complete Seling join accepts proof through actual operation. He may agree with the actual nonpunitive classification without requiring Thomas's historical statute-only restriction. |
| Kennedy | Retain reversal and the complete bounded nonpunitive rationale. The historical public-record analogy is limited: he cannot equate compelled current home information with a publicly filed conviction in light of his Paul P. opinion. | His Hudson/W.P. joins and Hendricks dissent still support civil characterization despite serious burden. Paul P. requires a real information/recipient/purpose connection for its independent privacy claim but does not make every possible privacy defect punishment. The change affects the rationale's permissible scope, not his judgment. |
| Souter | Preserve the new independent judgment route and clarify its degree of certainty. The historical opinion strongly confirms intent ambiguity, rejection of clearest-proof deference here, and a close effects balance resolved by the ordinary presumption of constitutionality. He joins no actual clear-civil-intent or four-Justice high-burden application. | His published Ursery/Hudson joins concerned demonstrated civil design; they do not establish that every later mixed enactment is clearly civil. His W.P. opinion, Hendricks join and complete Seling join require scrutiny of actual notification and operation. They support the substantive concerns already in the historical opinion rather than a confident broader validation. The refined commitment is failure to establish punishment on this close record, not a general judgment that lifetime Internet registries are benign. |
| Thomas | Retain reversal and a full join in actual combined-operation analysis. Do not recreate his historical statute-only concurrence: its key doctrinal premise is absent in this timeline. | His own complete Seling join accepts evidence of actual punitive implementation, following the preserved operational Hudson/Hendricks framework. His W.P. position and Hendricks dissent support a nonpunitive result under that framework. The Internet medium is administrative implementation rather than statutory command, but its real effects are still pertinent under the rule he joined. |
| Ginsburg | Retain the punitive judgment and her intent ambiguity; qualify the supplemental model's actual clear-intent join. She may find punishment directly and also find the demanding standard satisfied even if civil intent is assumed, without contradicting her historical intent assessment. | Her Hendricks join supplies an actual punitive-operation holding under clearest proof; her Hudson and W.P. joins preserve meaningful cumulative review and the actual fit of disclosure. W.P.'s tailored audience and exceptions are absent here. These changed legal premises strengthen her sufficient effects case; they do not change Alaska's code placement or justify abandoning ambiguity. Her historical rehabilitation ground remains material and accurately confined to the supported Doe I evidence. |
| Breyer | Retain the punitive judgment and the ambiguous-intent position he historically joined with Ginsburg. The clearest-proof cumulative ground remains an independently sufficient alternative, not a clear-intent finding. | His authored Hendricks, Hudson and Seling opinions and W.P. joins give him concrete prior commitments to demanding but genuine operational review. Unlike historical Hendricks, the present law recognizes punishment on a proved cumulative application. That makes his stronger effects alternative supportable without importing custody facts or erasing his actual intent objection. |

**Historical departure:** Thomas's present full join reaches actual Internet implementation rather than repeating his historical statute-only qualification because he personally joined the unanimous Seling operational-review rule in this timeline; that directly displaces the legal premise of his historical separate concurrence while preserving his nonpunitive judgment.

**Historical departure:** Kennedy, with O'Connor, Scalia and Thomas, retains the historical nonpunitive result but does not rely on historical approval of Hendricks custody or Hudson's statutory-face-only account. Their own Hendricks dissent and later Seling joins, and Kennedy's intervening Paul P. opinion concerning current residential information, require the present bounded actual-operation rationale and prevent a categorical accurate-public-data exemption.

**Historical departure:** Ginsburg and Breyer additionally support punitive classification even assuming civil intent and applying the demanding clearest-proof standard because their own controlling joins in this timeline's punitive Hendricks application and preserved operational Hudson/Seling rule, together with W.P.'s actual safeguards, supply a stronger cumulative-effects basis than the historical opinion's premise that Hendricks upheld the confinement. Their historical ambiguous-intent position itself is retained; no altered Alaska fact is claimed.

No judgment departure from an actual historical Associate vote occurs. Souter's separate route is retained on its historically supported terms. The different grouping of punitive reasoning reflects sufficient common grounds, not a transplanted historical authorship choice or a claim that the historical opinions were a single writing.

### Proposition and remedy arithmetic for assembly

| Proposition or component | Direct Associate support | Qualification |
|---|---|---|
| Sequential intent inquiry and meaningful cumulative examination of purpose and effects | Stevens, O'Connor, Scalia, Kennedy, Souter, Thomas, Ginsburg, Breyer | An established civil choice receives clearest-proof protection; no single feature is conclusive. Souter, Ginsburg and Breyer dispute whether that premise is established here. |
| Alaska's intended civil character is sufficiently established to apply the heightened override here | O'Connor, Scalia, Kennedy, Thomas | Souter, Ginsburg and Breyer withhold this finding; Stevens's sufficient effects position does not require it. No seven-Justice finding is recorded. |
| On the civil-intent/clearest-proof route, the supported combined scheme has not been proved punitive | O'Connor, Scalia, Kennedy, Thomas | Four direct application joins. Souter's result is independent and supplies no fifth full join. |
| Ambiguous intent, close effects balance, ordinary constitutionality presumption and failure to establish punishment | Souter | Judgment-only relationship to the four-Justice complete rationale; a substantive separate explanation is required. |
| The retrospective combined lifetime operation is punitive on these respondents, including even under clearest proof if civil intent is assumed | Stevens, Ginsburg, Breyer | Three direct supporters of this sufficient ground. Ginsburg and Breyer also preserve their ambiguous-intent/direct-effects route. |
| Reverse the reviewed ex post facto judgment and reject that claim | O'Connor, Scalia, Kennedy, Souter, Thomas | Five Associate judgment votes, with the distinct grounds above; no final Court count is supplied. |
| Affirm the punitive determination as applied and implement fitted protection with any necessary severability work | Stevens, Ginsburg, Breyer | Three Associate judgment votes. Confidential registration alone is not independently declared punitive; no substitute risk-hearing system is ordered. |

The judgment supporters share a result, not five identical operative premises. The four-Justice rationale turns on established civil intent and lack of the demanding override; Souter withholds that predicate and reaches the result through a close direct-effects evaluation and the ordinary presumption. Neither actual finding is a logical subset of the other merely because one proof standard is more demanding. No Marks synthesis or controlling fifth application join is declared here. Assembly must identify any direct five-Justice proposition support after the remaining Justice's authorized position enters and preserve the actual relationships.

The common permissible nonpunitive scope rejects this ex post facto claim while treating accuracy, noncustodial duties and search access as considerations within actual-operation review. It does not immunize all registries, treat all private consequences as legally irrelevant or resolve an independent privacy claim. Those are genuine join limits; ordinary hypothetical caveats need not be published when the final opinion does not advance the barred proposition. The substantive Souter explanation and punitive combined-operation dissent each perform necessary legal work. Thomas needs no separate writing because the former statute-only objection is displaced by his own prior join, and Stevens's broader historical theory requires no separate publication when the common sufficient ground preserves his position.

### Reconciliation changes and source integrity

No judgment or remedy vote changes from either independent handoff. The clean supplemental model already moved Souter from the original full clearest-proof application to an independent ambiguous-intent route. This reconciliation (1) preserves and clarifies that route as close-case review with the ordinary presumption; (2) retains Ginsburg's and Breyer's historically supported ambiguity rather than counting them as actual clear-intent joiners, while retaining the stronger assumed-civil-intent effects ground supported by their prior public positions; and (3) records why Thomas's omitted historical concurrence is not reproduced. These refinements respond to the complete historical writings and existing prior law, not to new neutral facts or private material.

Cornell source pages read completely: https://www.law.cornell.edu/supct/html/01-729.ZS.html; https://www.law.cornell.edu/supct/html/01-729.ZO.html; https://www.law.cornell.edu/supct/html/01-729.ZC.html; https://www.law.cornell.edu/supct/html/01-729.ZC1.html; https://www.law.cornell.edu/supct/html/01-729.ZD.html; https://www.law.cornell.edu/supct/html/01-729.ZD1.html. The saved official Reports text/PDF cross-check fixes the citations and complete topology: majority at 89–106, Thomas at 106–107, Souter at 107–110 including the footnote continued on 110, Stevens at 110–114 including his companion-reference footnote, and Ginsburg at 114–118 including both footnotes. No long quotation is independently authored in this handoff.
'''

validation = '''## Final handoff validation

- Each of the four matters supplies all eight named Associate commitments and distinguishes judgment from proposition support. No assignment or controlled-position contribution is inferred.
- Bach: eight affirm; Wheat: five affirm and three would reverse the initial-stop ground; Buckland: eight reject facial invalidity, five retain Angle and remand remaining plain-error review, three would affirm under their maintained contrary allocation premise.
- Smith: five reverse and three affirm the ex post facto determination. Four reversal supporters join the full civil-intent/clearest-proof application; Souter supplies an independent judgment ground. The three punitive supporters share a sufficient cumulative-effects ground; Ginsburg and Breyer retain intent ambiguity.
- The lower comparators in Bach, Wheat and Buckland provide no historical Supreme Court Justice vote or assignment. Buckland preserves the correct offense-date thresholds, distinct statutory and binding-range inquiries, ordinary Rule 52(b) burden and separate fourth condition.
- The three completed partial sections are copied without substantive change. Smith uses the freshly validated operation facts and affected supplemental model, with the stated historical-reconciliation refinements. No additional material neutral fact is silently introduced.
- Every current Smith opinion and footnote was fully read in its separate Cornell source and material topology/grounds cross-checked against the official report. The missing Thomas concurrence is accounted for; no future-law, copied historical authorship or invented private conduct enters.
- No unresolved source predicate prevents the bounded dispositions and grounds stated. Final compatibility, assignment, Records, workspace projection and public rendering belong to subsequent stages.
'''

text = '\n\n'.join([intro.rstrip(), bach, smith_intro.rstrip(), smith, smith_annex.rstrip(), wheat, buckland, validation.rstrip()]) + '\n'
runtime = base / 'runtime/OT_2002CHUNK6_A_RECONCILED.md'
frozen = base / 'freeze/OT_2002CHUNK6_A_RECONCILED.md'
runtime.write_text(text, encoding='utf-8')
frozen.write_bytes(runtime.read_bytes())
assert frozen.read_bytes() == runtime.read_bytes()
for saved in (bach, wheat, buckland):
    assert saved in text
assert text.count('## Reconciled Justice-specific commitments') == 1
assert 'Those seven share that framework and initial classification' not in text
assert '## Smith v. Doe — March 5, 2003' in text
print('Runtime and frozen reconciliation identical.')
print('Bytes:', len(frozen.read_bytes()))
print('SHA256:', hashlib.sha256(frozen.read_bytes()).hexdigest())
