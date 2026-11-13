from pathlib import Path

base = Path('terms/OT2002')
source = (base / 'freeze/OT_2002CHUNK6_A_COMMITMENTS.md').read_text(encoding='utf-8')

def block(name, next_name):
    start = source.index('## ' + name)
    end = source.index('## ' + next_name, start) if next_name else source.index('## Handoff checks', start)
    return source[start:end].rstrip()

intro = '''# OT2002 chunk 6 A — partial historical reconciliation

## Scope and status

Completed reconciliation of United States v. Bach, United States v. Wheat and United States v. Buckland. Smith v. Doe is deliberately excluded pending a freshly validated neutral operation/intent supplement and affected independent commitments. This partial handoff makes no Smith determination and is not the completed A reconciliation freeze.

The authorized frozen neutral packets, preflight, Bach validation, participation/scheduling handoff, A commitments, A comparator, A entering-law and relevant prior-public selections were reviewed in a fresh reconciliation context. No private controlled material, current raw Decision Record, current full brief or assembly work was opened. General model knowledge is not represented as erased. All nine participate; only the eight Associate commitments are stated. The record cutoffs remain March 5, 2003 for Bach and Wheat, and March 10, 2003 for Buckland. The neutral proper-review and scheduled-event premises remain unchanged.

The three full commitment sections below are copied mechanically from the frozen independent handoff. Reconciliation adopts their judgment positions, exact proposition commitments, strongest objections, narrower and broader supported positions, remedy limits and writing functions without change. Each ensuing reconciliation note supplies the comparator test; it does not assign an author or assemble the Court. Original provisional language identifies the source's stage, while this wrapper identifies the reconciled status of the three retained sections.
'''

bach_note = '''### Reconciliation — Bach

The historical Eighth Circuit judgment reversed suppression, with Beam writing for Murphy and Melloy. It assumed the pertinent privacy interest and rejected physical presence as a constitutional requirement for the provider's described retrieval; its statutory analysis concerned a state warrant. That lower-court result supports the narrower execution ground in the frozen commitments, but supplies no historical Supreme Court Justice vote, author or join.

The eight Associate positions remain independently supported. Stevens, Souter, Ginsburg and Breyer preserve the retained-confidence principle of Guest while accepting independent judicial authority for this search. O'Connor can assume the communications interest without enlarging her narrower Guest credential join. Scalia, Kennedy and Thomas likewise need not resolve their disagreement with Guest's wider scope: their complete Ortiz/Hurtado and Ayeni joins distinguish the existence of an information search, a lawful justification, and genuine technical assistance from an extraneous intrusion. None of those earlier positions makes an officer's bodily attendance indispensable to the execution shown here. All eight support the complete bounded constitutional ground, its application and affirmance of the circuit judgment.

The strongest contrary concern remains actual control of investigative scope. The neutral account supplies technically necessary retrieval within an identified judicial demand, rather than a provider's independent probable-cause or investigative selection. Neither the circuit outcome nor the absence of officers supplies an affirmative finding that every possible scope safeguard was satisfied; the commitments resolve the presented attendance requirement using the described execution. Section 3105's express attendance condition is not rewritten, and an inapplicable federal statute or a possible state-law breach is not converted into a constitutional exclusion rule.

**Historical comparison:** No historical Supreme Court merits alignment exists. The reconciled result agrees with the lower comparator at the question's actual scope. No Justice-specific historical departure is asserted. The Supreme Court action supported by all eight is affirmance of the circuit judgment, leaving the provider-suppression reversal operative and returning the prosecution for ordinary proceedings.
'''

wheat_note = '''### Reconciliation — Wheat

The historical Eighth Circuit panel sustained the initial stop through the contemporary eyewitness description of a moving hazard, corroborated vehicle and route, and public nature of the reported maneuvers. Goldberg's unanimous panel opinion with Loken and Bogue is a lower-court comparator only; there is no historical Supreme Court merits poll to import. Its reasoning does not replace this timeline's J. L., Wardlow, Valentine or Arvizu.

O'Connor, Scalia, Kennedy, Thomas and Breyer retain affirmance on a sufficiently reliable contemporaneous account under the totality rule. Stevens, Souter and Ginsburg retain the conclusion that this anonymous accusation remains inadequately verified. The five sustaining Justices do not adopt a driving-danger exception, a presumed traceable emergency caller, or the view that vehicle identification alone corroborates wrongdoing. Their particular firsthand inference rests on the described sequence of visible unlawful maneuvers, prompt moving-vehicle match and temporal connection. The three opposing Justices credit those details but find them insufficient to assure the truth of the accusation. That difference is an application disagreement permitted by the common J. L. rule; their commitments do not impose predictive detail as a mandatory condition.

The own-Justice support is material. O'Connor's White join and Arvizu opinion accept supported contextual inference; Scalia's White and Arvizu joins and Kennedy's White and Wardlow/Valentine positions permit this inference without eliminating J. L.'s antecedent reliability demand. Thomas's Wardlow and Valentine positions credit the specific conduct sequence, within his unanimous J. L. constraint. Breyer can distinguish his Wardlow/Valentine insufficiency votes because these reported maneuvers, if reliably attributed, directly describe wrongdoing rather than ambiguous flight or possession potentially lawful in itself. Stevens's White dissent and J. L. opinion, with Souter's and Ginsburg's J. L./Wardlow/Valentine positions, support refusal to convert apparent opportunity to observe into sufficient accusation reliability. Neither result is dictated simply by presumed policing preferences.

The later detention, consent, drugs and sentencing issues remain separate. The five affirm the reviewed judgment against the initial-stop challenge; the three would reverse that ground and remand the consequential suppression question for any preserved independent causal basis, applying Robinette's separation of voluntary consent from attenuation. A later discovery cannot repair inception. The commitments invent neither an acquittal nor a necessary attenuation finding.

**Historical comparison:** The five Associate affirmance positions agree with the lower comparator's result through the narrower stated rationale; the three opposing positions disagree with that lower court under their own established Fourth Amendment positions. No historical Supreme Court Justice vote exists from which a Justice-specific departure can be claimed. Every judgment and proposition commitment is retained.
'''

buckland_note = '''### Reconciliation — Buckland

The historical en banc circuit rejected facial invalidity and sustained the sentence, eight to three in judgment. The supplied comparator correctly separates the six votes for the stacking rationale from T. G. Nelson's partial join and Hug's distinct concurrence, and separates the dissent. Those circuit positions are not historical Supreme Court Justice commitments. No authorship or join is carried into the present Court from that topology.

The offense-date statutory premise controls independently of the circuit's later-threshold quotation: 100 grams of mixture reaches the forty-year grade and one kilogram reaches the life grade. The reported 749 grams crosses the former threshold, and 324 months is below forty years. That correction makes the supported statutory-threshold evidence relevant to the actual term without deeming it an element verdict, valid aggravated-offense admission or adequate proof of the contested binding Guidelines range. Counsel's proposed one-to-three-kilogram calculation likewise remains a sentencing position with its stated source status. The historical 500-gram comparison cannot be imported to claim the life grade was proved.

All eight uphold the ability to administer the enacted grades with constitutional element protections. Nothing identified in the text expressly requires the unconstitutional judge/preponderance allocation alleged by the facial challenge. This agrees with the lower result but preserves the stronger charging and punishment-authorization rules of Jones, Castillo, Apprendi, Angle and Harris in this timeline.

For the sentence, Stevens, Scalia, Souter, Thomas and Ginsburg retain their Angle commitments. The lower court's putatively mandatory 324-month aggregate presupposes the very judicial quantity finding that controls the binding range; unused maxima on four drug counts do not make that aggregate lawfully inevitable. Those Justices' Cotton joins remain real: they accept an independently adequate fourth-condition denial, and neither presume substantial-rights injury nor shift the ordinary burden to the Government. Cotton's essentially uncontested statutory threshold cannot itself determine a separate contested binding range. Their Harris positions distinguish a record establishing every condition for correction from this record's narrower basis for appellate reconsideration.

O'Connor, Kennedy and Breyer retain their contrary constitutional allocation premise and would affirm using a lawful compulsory total on that premise, together with the confined forfeiture assessment. They request reconsideration of Angle rather than purporting to distinguish it away. O'Connor's Angle/Harris dissents and Cotton opinion, Kennedy's Jones/Angle/Harris dissents and Castillo join, and Breyer's Jones/Angle dissents and qualified Harris position furnish Justice-specific support. Breyer does not adopt an artificial minimum/maximum distinction. If Angle remains controlling, all three recognize that their automatic lawful-total rationale fails unless an independently supported review ground sustains the term. No additional factual ground is manufactured for them.

The stronger immediate-vacatur route remains unselected because the supplied record has not established the remaining Rule 52(b) conditions for the actual lawful range and sentencing outcome. The five therefore vacate only the appellate sentence affirmance and remand the remaining plain-error inquiry; the sentence itself remains pending that inquiry. Four surviving drug counts remain, the firearm convictions stay vacated, and further sentencing requires authority independent of the remand. The mandate neither makes the Guidelines advisory nor authorizes new aggravated proceedings or automatic consecutive restructuring.

**Historical comparison:** The five-Associate remand differs from the lower comparator because governing Angle requires element protection for the binding range and rejects the unsupported aggregate premise. Stevens, Scalia, Souter, Thomas and Ginsburg each adopted that rule and reaffirmed the relevant protection in Harris; their unanimous Cotton joins preserve the distinct review possibility. This is a concrete changed-law explanation for the different lower-judgment treatment, not a claim that any Justice historically voted in Buckland. The three affirmance supporters maintain their own published contrary allocation positions rather than importing the circuit's result. No actual Supreme Court historical-departure label is warranted for this added review.
'''

parts = [intro,
         block('United States v. Bach', 'Smith v. Doe'), bach_note,
         block('United States v. Wheat', 'United States v. Buckland'), wheat_note,
         block('United States v. Buckland', None), buckland_note,
         '''## Partial handoff validation

- Bach: eight affirm the circuit judgment; all eight support the bounded execution rule and application.
- Wheat: five affirm and three would reverse the stop ground; all eight support the shared pre-stop reliability rule.
- Buckland: eight reject facial invalidity; five retain Angle and remand the remaining plain-error inquiry; three would affirm on their expressly maintained contrary allocation premise.
- Each copied commitment section retains the named Justices, exact remedy, strongest objection, authorities, scope and join barriers. No final Court vote, author or assignment is supplied.
- Source limits remain those in the validated neutral and commitment handoffs. This reconciliation adds no new factual premise for these three matters. Smith is excluded, and the full A freeze remains pending.
''']

output = base / 'runtime/OT_2002CHUNK6_A_OTHER_RECONCILED.md'
output.write_text('\n\n'.join(parts).rstrip() + '\n', encoding='utf-8')
print(output)
print('Characters:', len(output.read_text(encoding='utf-8')))
