from pathlib import Path
import json
import re

term = Path('terms/OT1999')
out = term / 'records/dickerson-v-united-states_merits_2000-06-26.md'
if out.exists():
    raise SystemExit('Refusing to overwrite an existing Record')
counts = json.loads((term / 'freeze/OT_1999CHUNK8_DICKERSON_COUNTS.json').read_text(encoding='utf-8-sig'))
reconciled = (term / 'freeze/OT_1999CHUNK8_C_RECONCILED.md').read_text(encoding='utf-8-sig')
annex = reconciled.split('## Dickerson — reconciliation of all eight Associates\n', 1)[1].split('\n## Reconciliation result and assembly conditions', 1)[0].strip()

holdings = '''### I. Miranda's constitutional safeguard cannot be replaced by voluntariness alone

**Holding and operative rule:** Miranda's warnings and waiver requirements implement the constitutional privilege against compelled self-incrimination in custodial interrogation, and Congress cannot authorize case-in-chief use of a statement that those requirements exclude merely because the statement is voluntary under 18 U.S.C. §3501(a)–(b). Genuinely equally effective safeguards remain permissible; no exact verbal formula is indispensable, and an unwarned statement is not necessarily actually coerced for every purpose.

**Authority:** Part I of Justice Stevens's Opinion of the Court, joined by Stone-Zsela, O'Connor, Kennedy, Souter, Ginsburg and Breyer. Seven direct rationale votes control the constitutional rule, statutory application, qualifications and suppression remedy.

**Controlling explanation:** Miranda supplies a prospective safeguard for an informed choice during custodial interrogation, not merely a later inquiry into whether a completed statement was coerced. Its operation in state prosecutions and the constitutional review preserved by Withrow cannot rest on this Court's supervisory authority over federal procedure. Congress may provide effective alternatives, but it may not remove the protection merely by reinstating the voluntariness inquiry Miranda found insufficient.

Section 3501 requires the judge to examine voluntariness outside the jury's presence, consider all circumstances including warnings and counsel, and permit the jury to assess the voluntary statement's weight. These are real protections. Their defect as a replacement is functional: retrospective examination does not itself inform the suspect before speaking. Smith v. Robbins distinguishes freedom to vary a safeguard's form from omission of its protected function; it does not decide this different safeguard's adequacy by analogy alone. Proposed training, civil remedies and warning incentives do not establish an equally effective replacement on this record, and civil relief cannot be assumed available regardless of its cause-of-action and immunity conditions.

The contrary argument relies on Tucker, Elstad, Harris, Hass and Quarles. Those decisions distinguish actual compulsion from warning-based exclusion and preserve particular derivative uses, later warned statements, impeachment or public-safety questioning. They do not make the original unwarned statement generally admissible in the prosecution's case in chief. The Court preserves those distinctions rather than equating every warning failure with actual coercion.

Here the district court found custody and found the disputed statements preceded warnings and waiver. The Fourth Circuit's voluntariness conclusion cannot substitute for the missing safeguard. Its section-3501 basis for reversing statement suppression fails. The statement-suppression order is restored and the prosecution remanded, subject to a properly preserved exception; no new credibility finding is made.

**Statutory qualifications:** Subsection (a) concerns federal or District of Columbia criminal prosecutions. It requires the judge to resolve voluntariness outside the jury's presence and, upon finding the confession voluntary, to allow the jury to hear relevant voluntariness evidence and instruct it to give the confession the weight it deserves in light of all the circumstances. Its admission command remains subject to the constitutional safeguard stated above. Under subsection (b), all circumstances must be considered, including the arrest-to-arraignment interval when applicable, knowledge of the suspected offense, advice or knowledge concerning silence and use, prior advice of counsel rights, and absence of counsel during questioning and confession. The presence or absence of a listed factor need not be conclusive; consideration is mandatory, conclusiveness is not. Independent voluntariness review survives.

The Court does not invalidate the whole section. Subsection (c) protects a voluntary confession against exclusion solely for presentment delay when its weight is left to the jury and it is given within six hours of the relevant arrest or detention; the time limit does not apply when the judge finds a longer delay reasonable considering transportation and distance to the nearest available qualifying magistrate or other committing officer. Alvarez-Sanchez's relevant-duty inquiry and unresolved post-six-hour and McNabb–Mallory questions remain. Subsection (d) does not bar voluntary statements given without interrogation or while the speaker is not under arrest or detention; those alternatives remain distinct. Subsection (e) includes an admission of guilt and any oral or written self-incriminating statement. Each provision remains subject to constitutional requirements.

**Limits and questions not reached:** No automatic civil liability, general fruit-of-the-statement rule, mandatory warning wording or elimination of recognized exceptions follows. The separate apartment-evidence ruling, car-evidence dispute, refusal to reopen the suppression record and circuit authority to raise section 3501 are outside this review. The Court orders no new suppression hearing, dismissal, acquittal, release or vacatur of a conviction; none exists at this interlocutory stage.

### II. The Court retains Miranda's core against the separate request for judicial abandonment

**Holding and operative rule:** The Court declines to replace Miranda's core case-in-chief safeguard with a voluntariness-only rule: congressional preference for that rule and the existing distinctions between unwarned and actually compelled statements do not supply sufficient justification for abandonment here. Retention of the core leaves genuinely effective alternatives and the recognized, separately bounded exceptions available.

**Authority:** Part II of Stevens's Opinion of the Court is joined by O'Connor, Kennedy, Souter, Ginsburg and Breyer. These six directly adopt the additional stare-decisis ground. Stone-Zsela agrees that the alternative request for judicial abandonment is rejected but adds no ground and does not join Part II. No Marks combination is needed.

**Controlling explanation:** The amicus defending the judgment separately asks this Court to revise Miranda even if Congress cannot displace it. That request requires a judicial justification independent of the statute's existence. Miranda has supplied the governing framework for custodial interrogation, and subsequent decisions have retained its case-in-chief core while defining limits. Existing administration and reliance count against replacing that framework without an adequate reason.

The exceptions do not establish the claimed doctrinal collapse. Elstad distinguishes a later voluntary warned statement from the original unwarned statement; Tucker concerns derivative evidence; Harris and Hass concern impeachment; Quarles addresses public safety. Their tailored consequences can coexist with a constitutional safeguard broader than a retrospective finding of actual compulsion. They do not silently overrule Miranda.

Claims about interrogation costs, improved training and other remedies deserve consideration, but they do not establish that the prospective informed-choice function has become unnecessary or has an adequate substitute here. The Court need not declare every application costless, every warning formulation immutable or every judicial implementation rule beyond revision. The constitutional function and the absence of sufficient grounds to abandon this settled core justify rejecting the requested change.''' 

topology = '''| Writing | Author | Joined by | Relationship to judgment | Scope joined |
|---|---|---|---|---|
| Opinion of the Court, Part I | Stevens | Stone-Zsela, O'Connor, Kennedy, Souter, Ginsburg and Breyer | Reversal, restoration of statement suppression and bounded remand | Constitutional authority, inadequate statutory substitute, statutory qualifications and remedy; Holding I |
| Opinion of the Court, Part II | Stevens | O'Connor, Kennedy, Souter, Ginsburg and Breyer | Rejects the alternative request for judicial abandonment | Additional stare-decisis ground; Holding II |
| Dissent | Scalia | Thomas | Would affirm the reviewed statutory-admissibility basis against this challenge | Actual-compulsion ground, necessary judicial reconsideration, statutory circumstances and bounded further proceedings |

Stone-Zsela joins Part I and the judgment, and agrees without an additional ground that the separate judicial-abandonment request is rejected; he does not join Part II. The six other Justices supporting reversal join both parts. The two parts each have a direct majority; no plurality or Marks synthesis is involved. No separate Stone opinion is filed.'''

precedents = '''- **Miranda v. Arizona, 384 U.S. 436 (1966):** Its constitutional custodial-interrogation safeguard, case-in-chief exclusion and allowance for equally effective alternatives are retained. Voluntariness alone cannot replace its applicable requirements.
- **Withrow v. Williams, 507 U.S. 680 (1993):** Its constitutional habeas operation supports Miranda's status; its distinction between a warning claim and separately presented coercion remains. No new collateral-review rule is adopted.
- **Michigan v. Tucker, 417 U.S. 433 (1974):** Its derivative-evidence setting and distinction between safeguards and actual compulsion remain; it does not authorize general case-in-chief use of the original unwarned statement.
- **Oregon v. Elstad, 470 U.S. 298 (1985):** Its treatment of a later voluntary warned statement remains; the original unwarned statement's exclusion is not erased.
- **Harris v. New York, 401 U.S. 222 (1971), and Oregon v. Hass, 420 U.S. 714 (1975):** Their impeachment uses remain subject to their own requirements and do not become ordinary prosecution case-in-chief permission.
- **New York v. Quarles, 467 U.S. 649 (1984):** Its public-safety exception remains limited to its governing conditions; the decision does not replace the general warning rule.
- **Colorado v. Connelly, 479 U.S. 157 (1986):** Police coercion remains necessary to due-process involuntariness; absence of warnings alone does not establish that distinct defect.
- **Smith v. Robbins, January 19, 2000:** Its distinction between equivalent form and preservation of the required function informs the substitute inquiry; its appellate-counsel setting does not itself decide confession admissibility.
- **United States v. Alvarez-Sanchez, 511 U.S. 350 (1994):** Its subsection-(c) relevant-presentment-duty rule, six-hour protection, transportation-and-distance proviso and reservations remain. Today's decision resolves the distinct voluntariness-only displacement question that it reserved.
- **Stansbury v. California, 511 U.S. 318 (1994), and Thompson v. Keohane, 516 U.S. 99 (1995):** Their objective custody rule and distinction between ultimate constitutional classification and historical facts remain; no new custody or credibility finding is made.
- **Davis v. United States, 512 U.S. 452 (1994):** Its actual postwaiver clarification, clear-invocation and waiver rules remain; its reservation of the overall section-3501 question is not treated as an earlier answer.'''

separate = '''**Justice Scalia, dissenting, joined by Justice Thomas.** They would sustain the Fourth Circuit's statutory-admissibility basis against the presented Miranda-displacement objection, provided voluntariness is sustainably determined and the statute's required circumstances are considered. Their ground distinguishes the constitutional prohibition of actual compelled self-incrimination from a categorical exclusion triggered solely by omitted warnings. Tucker, Elstad, Harris, Hass and Quarles demonstrate that the Court already treats warning violations differently from actual compulsion in consequential settings.

The dissent confronts Miranda's application in state prosecutions and constitutional habeas review. It does not claim federal supervisory power over state courts or assert that Congress can override a constitutional rule the dissent simultaneously accepts as binding. Rather, it would judicially reject the asserted constitutional necessity of an irrebuttable case-in-chief bar for a sustainably voluntary statement, and then apply section 3501's federal admissibility framework. That reconsideration is a proposed doctrinal change, not a claim that prior decisions have already overruled Miranda.

Scalia and Thomas regard the tension between actual compulsion and categorical exclusion as sufficient reason for reconsideration despite settled practice and their own prior applications of Miranda doctrine. In their view, institutional familiarity cannot cure a constitutional-authority defect. Their disagreement concerns that premise, not permission to coerce, a finding that warnings preceded these statements or a promise of universally available civil remedies. Subsection (b)'s circumstances remain mandatory considerations, though the presence or absence of an individual factor need not be conclusive. They would leave the prosecution to ordinary further proceedings and decide neither the independent search grounds nor the refusal to reopen the suppression record. The Court rejects their proposed change.

Chief Justice Stone-Zsela's additional disposition-only agreement concerns the separate request for judicial abandonment. His joined Part I supplies his public constitutional and substitute-adequacy grounds; he adds no stare-decisis rationale or separate writing.'''

event = '''**Dickerson v. United States**, No. 99-5525. Plenary merits decision, October Term 1999, chunk 8. Argued April 19, 2000; decided June 26, 2000. On writ of certiorari to the Fourth Circuit, reviewing 166 F.3d 667 (1999), an interlocutory suppression appeal in a federal bank-robbery and firearm prosecution. There is no conviction or sentence under review. The granted question concerns section 3501's asserted authorization of case-in-chief admission notwithstanding Miranda; the separate challenges to the circuit's taking up that statute and its physical-evidence ruling are outside the grant.

The district court found that Dickerson was in custody during the January 27, 1997 FBI interview and that the disputed statements preceded warnings and waiver. It declined to reopen the record for the Government's later affidavit and handwritten-statement proffer because previous unavailability was not shown; the Fourth Circuit sustained that refusal. The circuit treated the statements as voluntary by inference from the district court's derivative-evidence ruling. That is the appellate court's inference, not a fresh finding by this Court or proof that warnings preceded the statements.

The United States supports Dickerson on the statutory-displacement question and opposes overruling Miranda. Paul Cassell's defending amicus brief presents the principal contrary arguments, including the distinct request for judicial reconsideration. The Government retains its prosecution; its merits position is not an admission that every item of evidence must be suppressed.'''

judgment = '''**Reversed and remanded; statement suppression restored, 7–2.**

**Supporting:** Stone-Zsela, Stevens, O'Connor, Kennedy, Souter, Ginsburg and Breyer.

**Opposing:** Scalia and Thomas.

The Fourth Circuit's judgment is reversed insofar as section 3501 supplied its basis for reversing statement suppression. The District Court's order suppressing the disputed statement from the prosecution's case in chief is restored, subject to a properly preserved exception, and the prosecution returns for further proceedings consistent with Miranda. The independent physical-evidence disposition is undisturbed. The Court neither reopens the suppression record nor directs a new hearing, dismisses the indictment, acquits Dickerson, orders release or vacates a nonexistent conviction.'''

law_after = '''Effective June 26, 2000, Miranda's constitutional case-in-chief safeguard cannot be displaced by section 3501's voluntariness-only admission rule. The Court resolves that previously reserved relationship without invalidating the section's distinct lawful functions. Equally effective alternative safeguards remain possible, independent coercion remains a separate inquiry, and recognized exceptions keep their own conditions. Six Justices also reject the separate request to discard the core under stare decisis. No precedent is overruled and no universal rule immunizing every judicial procedure from legislation is adopted.'''

procedure = '''The case returns to the lower courts for ordinary continuation of the prosecution with the District Court's statement-suppression order restored at the stated case-in-chief scope, subject to a properly preserved exception. The independent apartment-evidence ruling, car-evidence dispute and refusal to reopen receive no new disposition. No new Supreme Court return date, evidentiary hearing, release condition or deadline is set.'''

sources = '''The [record and merits briefs](https://archive.org/details/micro_IA40385014_0386) supply the indictment, suppression proceedings, reconsideration proffer and interlocutory posture. The [United States' merits brief](https://www.justice.gov/osg/brief/dickerson-v-united-states-merits) supplies its support for retaining Miranda and its distinct evidentiary position. Cassell's March 9, 2000 amicus merits brief supplies the defense of section 3501 and the alternative request for judicial reconsideration. The [1994 official United States Code](https://www.govinfo.gov/content/pkg/USCODE-1994-title18/html/USCODE-1994-title18-partII-chap223-sec3501.htm) supplies every subsection of section 3501. The circuit's inference of voluntariness remains distinct from the district court's findings on custody and warning chronology; the later proffer is not an accepted substitute finding.'''

blocks = {
    'Event': event,
    'Participation': "All nine Justices participated at argument and decision: Chief Justice Stone-Zsela and Justices Stevens, O'Connor, Scalia, Kennedy, Souter, Thomas, Ginsburg and Breyer. No nonparticipation is established.",
    'Public Action': 'The Court reverses the reviewed statutory basis for statement admission, restores statement suppression at the stated scope and remands.',
    'Judgment & Remedy': judgment,
    'Opinion Topology': topology,
    'Holdings': holdings,
    'Precedent Treatment': precedents,
    'Law After Decision': law_after,
    'Separate Writings': separate,
    'Procedure After Action': procedure,
    'Source Notes': sources,
}

count_table = '| Justice | Count before assignment |\n|---|---:|\n' + '\n'.join(f'| {j} | {n} |' for j, n in counts['counts'].items())
record = '''**Case and dockets:** Dickerson v. United States; No. 99-5525.
**Event and date:** Plenary merits decision, October Term 1999, chunk 8; 2000-06-26; argued 2000-04-19.
**Result:** Reversed and remanded at the section-3501 statement-admission scope; statement suppression restored, 7–2.
**Version / lineage:** Version 1; new event, supersedes none. Filesystem Record only; no Git operation or commit hash is claimed.

## Decision kernel

### Event, record and reach

''' + event + '''

The indictment charges conspiracy under §371, three bank-robbery counts under §2113(a), (d), and three §924(c) counts. The district court's apartment-evidence suppression was separately reversed by the circuit; the separate request concerning a backpack and solvent recovered from the car was denied. Neither becomes a new merits component here. Review proceeds through the ordinary federal certiorari channel; no threshold bar prevents reaching the granted statutory-displacement question. The separate amicus request for judicial reconsideration is answered at the precise grounds and join scopes below.

### Participation, chronology and entering law

All nine listed Justices participated at argument and decision; quorum exists and five votes suffice for a majority disposition or rationale. The June 26 Apprendi matter is independent, stopped before decision and supplies no law or counted opinion. Both matters use the same earlier-effective baseline. No participation change or intervening case-specific procedural event is established.

The opening-law slice preserves Miranda's warning-and-waiver safeguard, its effective-alternative allowance and the actual-compulsion distinction. Withrow preserves constitutional Miranda review and separately presented coercion; Stansbury, Davis and Thompson preserve their distinct custody, invocation and review rules. Alvarez-Sanchez preserves subsection (c)'s relevant-duty and timing questions and reserved the overall displacement issue. Smith v. Robbins supplies the distinction between changing form and omitting a necessary protected function. Its actual Wende-inadequacy holding governs, not the different historical result quoted in advocacy. Boerne permits fitted constitutional enforcement without replacement of a substantive right; its Section 5 test is not transplanted into this federal evidence dispute. Hubbell concerns compelled production, not every unwarned statement.

The complete June 12 and June 19 refresh is documented in the frozen final-law and reconciliation reviews. Carter adds no Miranda rule; Miller permits valid changed prospective law while preserving independent adjudication and does not authorize congressional replacement of an accepted constitutional safeguard. Hawkins concerns an existing sentence; Harris Trust supplies no universal civil remedy; the remaining additions change no ground, scope or remedy here. No new constitutional rule is inferred from a statutory analogy. Substantive research cutoff: June 26, 2000. Modern retrieval metadata supplies no in-world premise.

### Stone: approval, compatibility and fallback

The sole current Stone input is `runtime/OT_1999CHUNK8_DICKERSON_STONE.md`, the October 31, 2026 approved supplement. It expressly reaches the merits, recognizes Miranda's constitutional admissibility framework, permits genuine equivalent safeguards, rejects voluntariness alone, reverses and restores the District Court's statement-suppression order, and returns the prosecution without case-in-chief use subject to a properly preserved exception. It excludes exact-formula compulsion, automatic civil liability, elimination of recognized exceptions and equating every unwarned statement with actual coercion. The actual entering law, supplied grant and corrected interlocutory posture leave that fixed core intact. No substantive narrowing, new Stone ground or clerical correction is made.

Stone joins Part I and the judgment. His supplement does not supply an independent stare-decisis rationale for the amicus's separate request that the Court itself abandon Miranda's core. The approved standing fallback is used only for the disposition of that unaddressed alternative request: he agrees with the majority's rejection and adds no ground. It supplies neither a Part II rationale join nor authorship eligibility for the whole lead. No Stone separate opinion is needed because Part I and the express Part II disposition-only relationship state his complete authorized position.

### Opinion topology

''' + topology + '''

### Judgment and remedy

''' + judgment + '''

## Controlling holdings

''' + holdings + '''

## Precedent treatment and resulting law

''' + precedents + '\n\n' + law_after + '''

## Continuity and published noncontrolling positions

''' + separate + '''

Scalia and Thomas's published June 26 dissent supplies the stated proposed judicial rejection of categorical warning-based exclusion for a sustainably voluntary statement. Its constitutional premise, statutory-factor requirements and limited affirmance are retained for future continuity as noncontrolling positions. Neither the dissent nor Stone's disposition-only agreement changes the law of Part I or Part II. There is no roster, circuit-allotment, standing-practice or companion change and no invented external consequence. The criminal prosecution continues at the stated evidentiary posture.

## Adaptive audit annex

### Form, assignment and counts

The signed two-part lead and one dissent were fixed on legal grounds in [the form receipt](../freeze/OT_1999CHUNK8_DICKERSON_FORM.md) before counting or choosing an author. The parts distinguish legislative displacement and substitute adequacy from the separate judicial-abandonment request and its additional stare-decisis ground. They are not split to alter eligibility or workload. One fully eligible Justice can write both parts, so multiple lead authors are unnecessary.

Chief Justice Stone-Zsela assigns as a member of the tentative judgment majority, including the fallback-supplied rejection of the alternative request. His assignment authority does not supply a rationale join or author eligibility. Counts were freshly derived from actual current-term Record opinion tables, including every earlier effective Record and earlier alphabetical same-day event, by the count tool with bytecode disabled. No earlier assignment tally supplied the count. [Count receipt](../freeze/OT_1999CHUNK8_DICKERSON_COUNTS.json).

''' + count_table + '''

**Last counted event:** Santa Fe Independent School District v. Doe, June 19, 2000, lead authored by Breyer. Eighty-eight signed lead-author counts precede this assignment. Apprendi is stopped and contributes zero; no later event enters.

**Eligible authors for the entire lead:** Stevens, O'Connor, Kennedy, Souter, Ginsburg and Breyer. All six support both parts in full, including each limiting accommodation. **Balance pool:** Stevens, O'Connor, Kennedy, Souter, Ginsburg and Breyer. The eligible minimum is nine and the pool ceiling ten. **Author selected:** Stevens.

This is a fit assignment: the six already share the additional retention ground, and the seven Part I joins are supported without changing a frozen commitment. Stevens's Robbins opinion supplies the concrete distinction between preserving a protected function and retaining an exact procedural form; his Roberson opinion and Withrow/Davis joins supply specific custodial-choice experience. He can state the inadequacy of this retrospective substitute while respecting controlling Elstad limitations that differ from his earlier separate view. Souter is the strongest alternative: his Withrow and Davis opinions closely fit constitutional implementation and informed custodial choice, and his Miller opinion preserves independent constitutional adjudication under valid changed law. Stevens can carry the common ground at least as well and has nine counted leads to Souter's ten. O'Connor's Elstad analysis is an important additional fit for the right/safeguard distinction, but its preserved limit is fully reflected without a necessary authorship accommodation. The other eligible Justices remain capable of the work. Stone cannot carry Part II's additional rationale; Scalia and Thomas reject both governing grounds. No historical author is imported, no future-career evidence is used and no fabricated draft circulation is asserted. Scalia states the common dissenting constitutional-authority argument, with Thomas joining its entire scope; that separate writing does not count as a lead.

### Final compatibility by Justice

| Justice | Judgment and precise join | Recorded barrier and final treatment |
|---|---|---|
| Stone-Zsela | Reverse, restore statement suppression and remand; Part I; disposition-only agreement rejecting the alternative request | Fixed constitutional/equivalent-safeguard core and preserved exceptions are stated. Fallback supplies no Part II reason. |
| Stevens | Same judgment; Parts I–II | Effective prospective choice is retained without importing his Elstad dissent as controlling law. |
| O'Connor | Same judgment; Parts I–II | Warning failure is not equated with actual compulsion; Elstad, Tucker and the impeachment rules remain. Effective alternatives stay open. |
| Scalia | Opposes reversal; authors dissent | State and habeas enforcement are confronted through express judicial reconsideration, not congressional override of a conceded binding constitutional rule. |
| Kennedy | Same judgment; Parts I–II | The informed-choice function remains; no immutable warning wording or universal hostility to alternatives is adopted. |
| Souter | Same judgment; Parts I–II | Constitutional implementation is distinguished from actual coercion and from universal constitutionalization of judicial procedure. |
| Thomas | Opposes reversal; full dissent join | Sustaining the statute rests on his own judicial-reconsideration premise, with actual-compulsion review and mandatory statutory circumstances retained. |
| Ginsburg | Same judgment; Parts I–II | Statutory subsections and independent remedies remain distinct; no new physical-evidence or civil-liability ruling follows. |
| Breyer | Same judgment; Parts I–II | Functional inadequacy is stated without treating empirical advocacy as an established fact or foreclosing future effective alternatives. |

Part I has seven direct votes and Part II six. The judgment has seven supporting and two opposing votes. No non-Stone judgment, material ground, limit or remedy changes after reconciliation. Restoring statement suppression expresses the consequence of reversing the only reviewed statutory ground; it creates no new suppression theory, finding or evidentiary hearing. Final compatibility is sufficient; no invented circulation history or changed-vote narrative is needed.

### Frozen non-Stone reconciliation and grounds — mechanically copied

The following entire Dickerson section is copied programmatically from [the frozen reconciliation](../freeze/OT_1999CHUNK8_C_RECONCILED.md). The unchanged original commitments remain in [the commitment freeze](../freeze/OT_1999CHUNK8_C_COMMITMENTS.md). The [final law review](../freeze/OT_1999CHUNK8_C_FINAL_LAW_REVIEW.md) and [final reconciliation review](../freeze/OT_1999CHUNK8_C_FINAL_RECONCILIATION_REVIEW.md) close the earlier-effective-law condition without replacing those freezes.

''' + annex + '''

### Historical comparison and departures

All eight Associate judgment directions match the verified historical judgment directions. No Rehnquist vote or authorship is transferred. The actual Robbins, Davis and Boerne holdings replace contrary historical descriptions in the advocacy and comparator; the frozen individual rows explain why those changed premises do not change the present results. Scalia and Thomas's express judicial-reconsideration premise is preserved. The six-Justice Part II and Stone's limited join result from actual authorization and direct support, not an invented historical topology. There is no material Associate vote departure requiring a Historical departure label and no displaced predicate of a later historical matter requiring a Consequence label.

## Sources, status and validation

The [validated neutral packet](../freeze/OT_1999CHUNK8_C_NEUTRAL.md) supplies objective record facts and the exact grant limits, with its source map. Petition, merits and appendix documents were located in the Archive collection by the preparation stage; the assembly stage relies on those validated extractions and does not claim a new full-document review. The official Code text saved in `sources/chunk8/c/3501_1994_statute.txt` was read for all statutory qualifications. Frozen reconciliation verifies all historical writings and footnotes from the official report; historical current-case reasoning is comparator evidence, not controlling entering law. No unavailable-document or reconstructed-procedure premise is used. No long source quotation is manually transcribed; the frozen annex is copied mechanically.

The complete Public Projection below supplies the mandatory public decision kernel. Controlling holdings are generated from the identical text used in the internal holding section. The companion validation receipt records actual arithmetic, block-order, identity, explanation-length, link and prohibited-link checks. Substantive self-review confirms the limited grant, interlocutory remedy, statutory exceptions, every Justice's frozen or approved scope and date-eligible grounds. Root integration into the current-term workspace and generated Render Input remains pending; no workspace, output, Render Input, opening tracker, foundation or earlier Record is altered by this assembly task. The Record was written to its natural-key location on November 3, 2026; no Git commitment is claimed under the user's prohibition.

## Public Projection

''' + '\n\n'.join('## ' + k + '\n\n' + v for k, v in blocks.items()) + '\n'

out.write_text(record, encoding='utf-8', newline='\n')
print(out.as_posix())
