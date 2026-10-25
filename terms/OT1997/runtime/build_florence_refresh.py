from pathlib import Path
import hashlib
import re

base = Path(__file__).resolve().parents[1]
old_path = base / 'freeze/OT_1997CHUNK9_NEUTRAL_LATER.md'
law_path = base / 'entering-law/OT_1997CHUNK9_LEWIS_PUBLIC.md'
out_path = base / 'freeze/OT_1997CHUNK9_NEUTRAL_FLORENCE_REFRESHED.md'
old = old_path.read_text(encoding='utf-8')
start = old.index('## City of Florence')
end = old.index('## Duffy', start)
packet = old[start:end].strip()

header = '''# Florence / Stemler — neutral dependency refresh after Lewis

This immutable preparation replaces only the Florence section of `OT_1997CHUNK9_NEUTRAL_LATER.md` for future modeling. It changes no completed adjudication and contains no vote or provisional commitment. The earlier packet remains preserved. The new substantive input is the validated, public-only May 26 *County of Sacramento v. Lewis* projection, copied exactly in the annex below. No current commitment, reconciliation, private position, raw Record or audit annex was opened.

**Event cutoff:** June 1, 1998. **Admitted preparation baseline:** the frozen May 21 current-term public law, now supplemented by the May 26 Lewis decision. Original lower-source research and this refresh occurred October 24, 2026. Use the [original entering-law slice](../entering-law/OT_1997CHUNK9.md), [May 21 neutral projection](OT_1997CHUNK9_ENTERING_NEUTRAL_PROJECTION.md), and [Lewis public law](../entering-law/OT_1997CHUNK9_LEWIS_PUBLIC.md). The copied source annex, not a historical same-matter comparator, supplies the new law.

**Participation and authority:** Stone-Zsela, Stevens, O'Connor, Scalia, Kennedy, Souter, Thomas, Ginsburg and Breyer remain seated. No case-specific nonparticipation or argument date is established for this added matter. Its authorized June 1 setting and inventory caption supply no invented Supreme Court docket, intervening grant, party substitution, new filing or waiver. The actual federal appellate channel is §1254(1). Six qualified Justices are required for a quorum; the applicable judgment threshold is a majority participating. No participation change is inferred from missing materials.

**Readiness:** The Lewis dependency is now incorporated, and this complete packet is ready for independent neutral modeling on the currently supplied public law. The May 28 DeCarlo event has not yet been supplied as committed public law. Under Engine §3G, before the June 1 event the operator must compare its eventual public decision and any other earlier effective event with this packet. If it materially changes immunity, personal responsibility, attribution, proof or remedy, replace the affected neutral portion and rerun the affected downstream stages. A DeCarlo proposal, commitment or expected result supplies no law. The residual chronological check is not a fabricated source gap and does not predetermine a change.

'''

old_sentence = 'Its formulation sometimes says “knew or reasonably should have known”; the actual entering law and any new Lewis holding must determine the proper culpability, not that shorthand.'
new_sentence = 'Its formulation sometimes says “knew or reasonably should have known.” Lewis now requires a contextual constitutional culpability inquiry and preserves the actual-awareness and reasonable-response limits of the distinct custodial authorities. The lower shorthand therefore cannot by itself establish the required mental state or turn constructive notice into actual awareness.'
assert packet.count(old_sentence) == 1
packet = packet.replace(old_sentence, new_sentence)

anchor = '*Harlow*, *Anderson*, *Elder* and simulated *Lanier*'
law_section = '''### Lewis's now-effective rule and its exact boundary

On May 26 the Court adopted a **six-Justice contextual constitutional rule** in Kennedy's opinion, joined by Stone-Zsela, O'Connor, Souter, Ginsburg and Breyer. In the supported rapidly evolving high-speed pursuit, instant choices amid competing enforcement and safety obligations required a purpose to cause harm unrelated to a legitimate law-enforcement objective; reckless risk-taking or deliberate indifference alone did not suffice there. That proposition governs at its stated setting and level of generality. The record's unintended collision and lack of an improper harmful purpose defeated the federal individual claim in that setting. Neither reversal's nine votes nor the words “unintended collision” enlarge it into a purpose-to-harm rule for every injury involving a vehicle.

Lewis expressly preserves the importance of **actual opportunity for deliberation**, the distinct duties and proof rules of custody cases, and analysis of purposeful collisions, deliberate terrorizing, contrived encounters and materially different opportunities for considered action. It establishes no seconds-based cutoff, no broad noncustodial immunity, and no automatic deliberate-indifference rule whenever an official could stop acting. Constitutional culpability must be grounded in precedent, constitutional tradition and the actual circumstances, rather than a judge's personal shock. Negligence remains insufficient. It does not license an official to manufacture the emergency on which a heightened threshold would depend.

The present allegations concern a **roadside decision after the private pursuit had stopped**: warnings, conversations, a threatened arrest, and officers' physical removal and placement of Black with a reportedly intoxicated and abusive driver. The complaint concerns the officers' own compelled transfer and the resulting danger; they were not the pursuing driver who unintentionally struck a passenger during a rapid chase. The warnings, successive choices and division of tasks are pertinent to a real opportunity to assess and respond. They do not establish any invented minimum deliberation time, identical knowledge among the officers, or a final finding that an opportunity existed for every defendant. A model must evaluate the supported situation and each actor, not transplant Lewis merely because a private chase preceded the stop or a fatal crash followed it.

The inquiry keeps separate: **(1)** the protected interest and actual deprivation or custodial restraint, **(2)** the culpability appropriate to the supported opportunity and function, **(3)** the particular officer's awareness, authority, action and causal responsibility, and **(4)** the separate conduct-time immunity defense. In a path relying on the preserved custodial deliberate-indifference authorities, the model must identify an actually known serious risk, a reasonable opportunity and authority to respond, a culpable disregard rather than a reasonable protective response, and attributable injury. Circumstantial evidence may establish awareness; “should have known,” official title, an unsuccessful response or the fatal outcome alone cannot replace it. Doe's supervisory-abuse framework is an instructive existing boundary, not a mechanically transplanted roadside checklist. Lewis creates no new independent state-law-to-constitutional conversion and does not resolve municipal attribution or state tort liability.

The lower court treated Black as actually in the officers' custody through threatened arrest and physical control and did not reach noncustodial state-created danger. The supported motion-to-dismiss account allows that question to be examined without declaring the conflicting evidence true. Pinder's reservation of a distinct affirmative-deprivation theory remains; it supplies neither a categorical duty in all danger cases nor a prohibition here. Where a specific constitutional provision actually covers a presented claim, Lanier's specific-provision principle remains. Lewis also preserves Albright's lack of a controlling universal displacement rationale. No new Fourth Amendment claim is silently substituted for the due-process claim actually reinstated below.

**Published Lewis positions, with their authority limits:** Stevens joined only the judgment on the particular May 22, 1990 qualified-immunity ground and reserved constitutional merits; his position supplies no seventh vote for the Court's standard and no automatic immunity for February 1994 coercion. Scalia and Thomas joined only the judgment on a distinct text/history/precedent ground concerning the carefully described reckless-pursuit claim; they did not join the Court's affirmative purpose-to-harm definition, and their writing does not categorically exclude intentional official assaults outside custody. Breyer joined the Court in full and separately preserved flexibility to resolve a suitable case on immunity first. These writings are publicly available individual positions for modeling, not controlling substitutes for the six-Justice rule or commitments in Florence.

### Conduct-time law remains a separate question

'''
assert packet.count(anchor) == 1
packet = packet.replace(anchor, law_section + anchor)

old_path_para = '''One Black path treats the coercive transfer as the officers' own custodial deprivation, applies the constitutionally sufficient culpability on properly assumed facts and rejects immunity where earlier law obviously covered it. Its strongest limits are individual knowledge, the correct mental state, the particular deprivation, causation and the possibility that later cases created rather than merely explained an extension. The competing path grants conduct-time immunity or a narrower correction if the required duty/culpability application was not sufficiently clear; it must explain why actual coercive custody differs insufficiently from received protection rules, rather than rely on abstract uncertainty about all substantive due process. A specific constitutional provision may require analysis if actually applicable and presented, but no new Fourth Amendment claim is silently substituted for the authorized due-process theory.'''
new_path_para = '''Lewis is present law for the constitutional analysis but supplies **no retroactive notice in February 1994**. Its rule also imposes no mandatory merits-first sequence. A suitable disposition may rest on the particular conduct-time clarity question without resolving a difficult constitutional extension; conversely, present merits may be resolved when properly reached. The model must state which ground does the work and must not label an immunity-only judgment a holding that the challenged conduct was constitutional.

### Supported alternatives after the refresh

One Black path preserves the reinstatement of the individual claim because the favorable allegations identify an actual coercive deprivation with an opportunity for considered action, sufficient constitutional culpability under the applicable custodial authorities, and conduct that pre-event law made obviously unlawful. Its strongest counterargument is that the custody, each officer's knowledge and available response, causal relationship, and particular clarity must be established rather than inferred from the tragic result or generalized bodily-security language. The pleading posture permits testing legal sufficiency, not findings against the plaintiff from the conflicting testimony.

A competing path resolves a genuinely unclear application on qualified immunity, or narrowly corrects the lower judgment where it used a “should have known” formulation or undifferentiated attribution that cannot sustain the actual constitutional inquiry. Its strongest counterargument is that threatening and physically transferring a vulnerable person into a known danger is materially different from Pinder's noncoercive assurance or Lewis's rapid pursuit; uncertainty at the margins does not erase the obvious core of an established protection. A notice-based resolution must examine all actual pre-February-1994 authority without demanding a factual twin or using a tally of judicial disagreement. A narrower remand may clarify a legal standard or defendant-specific claim without deciding factual truth, finding liability, or mandating new discovery.

A constitutional path dismissing the claim under Lewis must independently justify why the supported restraint and opportunity fall within an applicable no-violation rule. Merely asserting no purpose to cause the eventual crash, calling all police work an emergency, or invoking every officer's ability to desist is insufficient under Lewis's express boundaries. Likewise, the claimant cannot obtain automatic liability by showing a deliberate act, a known risk in the abstract, noncompliance with local policy, or time to pause. The present rule does not select among these paths or predetermine how any Justice resolves the different facts.

Lewis decides no equal-protection rule. Stemler's selective-enforcement claim therefore remains separately analyzed under the authorities and allegations below, with its own effect, purpose, comparator, individual participation, causation and conduct-time notice requirements.'''
assert packet.count(old_path_para) == 1
packet = packet.replace(old_path_para, new_path_para)

packet = packet.replace('### Sources and required dependency refresh', '### Sources, remaining chronology check, and readiness')
old_ready = '**Record preparation is ready; final neutral law and independent commitments are not ready until Lewis\'s May 26 public law has been checked and the affected analysis refrozen.** A newly effective DeCarlo rule must also be checked, though its different facts and capacities cannot be assumed dispositive.'
new_ready = '''**The completed Lewis public law has now been read and incorporated; this neutral packet is ready for independent modeling on the supplied effective baseline.** Before the June 1 action, check the eventual May 28 DeCarlo Public Projection and every other earlier effective relevant event. DeCarlo's procedural-due-process, consultation, capacity or immunity holdings could be material only at the scope actually adopted; its outcome is not yet supplied and none is predicted. Any material change requires an affected neutral refresh and fresh affected modeling/reconciliation before assembly. No current DeCarlo commitment or private material may substitute for its eventual public law.

The prior four-case packet was left byte-unchanged. Source facts and the posture come from its clean preparation and the complete lower judicial texts already read, including all footnotes, the concurrence and the rehearing addition. This refresh adds no historical documents, reconstruction premise, later Kentucky outcome, new participation fact or litigant default. Selected exact prior law remains available in [LATER_EXTRACT](../entering-law/OT_1997CHUNK9_LATER_EXTRACT.md), [LATER_STANDARDS](../entering-law/OT_1997CHUNK9_LATER_STANDARDS.md), and [LATER_CURRENT](../entering-law/OT_1997CHUNK9_LATER_CURRENT.md); the full authorized sources control.'''
assert packet.count(old_ready) == 1
packet = packet.replace(old_ready, new_ready)

law = law_path.read_text(encoding='utf-8')
receipt = f'''\n\n## Refresh source receipt\n\nThe following source was mechanically copied in full without retyping or substantive alteration: `entering-law/OT_1997CHUNK9_LEWIS_PUBLIC.md`. SHA-256 of its file bytes: `{hashlib.sha256(law_path.read_bytes()).hexdigest()}`. The source contains only the validated Public Projection supplied by control. No judicial choice was generated by this copying script.\n\n## Exact new-law annex\n\n'''
assert not out_path.exists(), 'Refusing to replace an already frozen refresh.'
out_path.write_text(header + packet + receipt + law, encoding='utf-8')

written = out_path.read_text(encoding='utf-8')
assert written.split('## Exact new-law annex\n\n', 1)[1] == law
missing = []
for target in re.findall(r'\]\(([^)]+)\)', header + packet):
    if target.startswith('http'):
        continue
    if not (out_path.parent / target.split('#')[0]).exists():
        missing.append(target)
assert not missing, missing
print(out_path)
print('Exact new-law annex identity: passed')
print('Relative-link targets: passed')
print('Bytes:', out_path.stat().st_size)
print('SHA-256:', hashlib.sha256(out_path.read_bytes()).hexdigest())
