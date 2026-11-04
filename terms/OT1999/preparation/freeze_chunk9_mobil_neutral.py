from pathlib import Path
import hashlib

term=Path(__file__).resolve().parents[1]
paths=[term/'preparation'/'OT_1999CHUNK9_MOBIL_CONTROL_FACTS.md',term/'preparation'/'OT_1999CHUNK9_MOBIL_OPERATIVE_SOURCE.md',term/'entering-law'/'OT_1999CHUNK9_MOBIL.md',term/'preparation'/'OT_1999CHUNK9_MOBIL_OBPA_STATUTE.md',term/'preparation'/'OT_1999CHUNK9_MOBIL_OCSLA_STATUTE.md']
texts=[p.read_text(encoding='utf-8-sig').rstrip() for p in paths]
intro='''# Frozen neutral packet — Mobil Oil / Marathon v. United States

Fresh neutral validation completed November 3, 2026. No modeled vote, assignment, Stone position or target historical Supreme Court disposition is supplied. Exact saved facts, operative terms, entering law and statutory copies follow.

## Event and independent completeness assessment

Nos. 99-244 and 99-253; argument March 22, 2000; merits consideration June 26, 2000. The judgment under review is the Federal Circuit's revised May 13, 1999 reversal, not its superseded 1998 opinion or a liability affirmance. Both petitioners' remaining North Carolina contract claims must be accounted for; earlier settled parties, a takings claim and separate CZMA administrative litigation are not adjudicated here. The nine seated Justices are Chief Justice Stone-Zsela and Justices Stevens, O'Connor, Scalia, Kennedy, Souter, Thomas, Ginsburg and Breyer; no case-specific nonparticipation is supplied. Independent modeling concerns the eight Associates.

Use effective pre-June-26 law; unrelated June 26 cases do not govern this event retroactively or as coordinated precedents. Winstar's actual assumed-risk holding, not its noncontrolling broader theories, supplies the contractual baseline. An authorized promise must be identified before breach, materiality, repudiation, election, restitution and amount are examined separately. The case cannot begin with Section I's conclusory assertion that a material replacement of the bargain is already an established breach.

Lease section 1's named statutes, existing regulations, specified future waste/conservation/correlative-right regulations and other applicable laws remain distinct. Sections 9–10, 13 and 19 qualify operation, suspension, cancellation and reserved rights without automatically resolving the contested risk allocation. The promised process is not a guarantee of a permit, state concurrence, a successful well or profits. Interior's favorable review does not eliminate North Carolina's independent objections, while those objections do not themselves decide whether depriving the separately purchased process is material. The fifth lease has no submitted exploration plan; its theory is anticipatory repudiation rather than a fabricated application.

The lower majority's independent-permit and no-operative-causation rationale, Newman's process bargain analysis, the Government's incorporated-suspension account, and its independent waiver/election defense are all preserved. Seeking performance or extensions can bear on election, but the legal consequence and record preservation remain contested. No litigant concession, waiver or recovery amount is supplied by inference.

The exact OBPA text is added to cure an abbreviated qualification in the initial handoff. It prohibits six listed activities in the defined North Carolina area until the later of October 1, 1991 or forty-five days of continuous congressional session after the specified certification/explanation report. Continuity breaks only at adjournment ending the session; days when either House is absent because of an adjournment longer than three days to a day certain are excluded. The scientific panel advises and supplies findings; the Secretary may disagree with detailed explanation and justification. A fixed calendar-day interval or absolute panel veto would misstate the law. The panel's own reporting/termination provisions and the Secretary's study/consultation duties remain as quoted. Congressional findings mention a July 14, 1989 memorandum; the supplied MOU recitation dates the actual agreement July 12. No two-day timing issue is decided from that discrepancy.

The exact OCSLA section 1334(a) text preserves the lessee-request condition for national-interest/proper-development/transportation suspension and the separate serious-harm suspension ground. Equivalent term extension has a gross-negligence/willful-violation exception; no such conduct is found. Cancellation requires the Secretary's post-hearing findings of probable serious harm, persistence beyond a reasonable time and comparative advantages, plus five continuous suspension years or a shorter period requested by the lessee. The distinct compensation formula, pre-September-18-1978 exception and joint-lessee due-diligence provisions do not establish any satisfied cancellation predicate here. The statutory compensation route and common-law contract restitution are separate.

The actual June 2, 1995 suspension letter requires rent and caps the new suspension at five years. It qualifies the Government brief's broader rent-free description. Neither continued suspension through June 2000 nor a later renewal is established; earlier rent-waived periods and the independent value of term extension remain available at their proved scope. No current lease expiration, waiver or offset is inferred simply from the absence of another research source.

Lawful paths include sustaining a supported no-undertaking/no-breach/no-material-breach or independent-election ground, or finding contractual liability and a lawful restitution entitlement with genuinely unresolved amount issues remanded. The precise legal ground determines the remedy. Bonus consideration, annual rentals, cognizable benefits/returned rights, profits and interest are different items. The exact award is not established by rounded $156/$158 million references; interest requires its own legal authority. No drilling order, CZMA override, legislative injunction or automatic evidentiary hearing follows.

## Readiness and exact source limits

Ready for independent modeling of the consolidated contract questions. The packet uses supported recitations rather than certifying complete line-by-line reading of the joint appendix. Exact judgment amounts, benefits evidence, later suspension/renewal/payment history and disputed preservation must be verified if they determine a chosen ground. A bounded entitlement/remand disposition may preserve those matters without pretending they are established. The supplied statutory cancellation predicates remain unproved; missing material cannot be turned into default. The research cutoff is June 26, 2000, with conduct and statutory-change dates maintained separately. No additional reconstruction premise is adopted.

'''
packet=intro
for label,text in zip(['Validated source facts','Exact operative contract and letter passages','Exact entering law and prior public positions','Exact OBPA section 6003','Exact OCSLA section 1334(a)'],texts):
    packet+=f'## {label}\n\n{text}\n\n'
out=term/'freeze'/'OT_1999CHUNK9_MOBIL_NEUTRAL.md'
receipt=term/'freeze'/'OT_1999CHUNK9_MOBIL_NEUTRAL_VALIDATION.md'
if out.exists() or receipt.exists(): raise RuntimeError('Existing freeze')
out.write_text(packet,encoding='utf-8',newline='\n')
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
body='''# Mobil / Marathon — fresh neutral validation receipt

Status: READY for independent non-Stone modeling. No modeled vote or assignment produced.

Allowed inputs read: governing AGENTS.md and neutral Engine rules; the Mobil/Marathon runtime Section I; the five handoffs below; current neutral-projection opening chronology/institutional facts. Other neutral current-chunk handoffs remain in this neutral-only context, but no target historical Supreme Court source, comparator, Stone supplement, commitment or raw Record was opened for Mobil.

The validator found and corrected two abbreviated source qualifications by requesting exact OBPA and OCSLA provisions. The original control text is preserved in the freeze, and the controlling exact copies and explicit clarification supply continuous-session/adjournment conditions, the lessee-request suspension limit, extension exception, hearing/continued-harm/cancellation predicates and compensation exceptions. These provisions establish available authority, not findings that cancellation or an exception occurred.

Independent framing preserves the revised lower judgment, separate permit regimes, actual promise/risk questions, every supported liability and election path, fifth-tract anticipatory posture, sovereign-act/unmistakability limits, source conflict over rent-free characterization, and distinct entitlement/amount/remedy inquiries. The two-day MOU-date discrepancy between the legislative recital and supplied instrument account is identified without selecting a timing consequence.

Exact gaps: no precise final amount from rounded reports; no new benefits/offset findings; no certified later suspension, renewal or payment history; no new preservation or waiver ruling; no complete-JA review claim. Those propositions require specific verification if decisive. Existing supported recitations permit bounded merits and restitution analysis, with genuinely unresolved issues retained for the appropriate procedural stage. Missing research is not default, refusal or a proved contractual breach.

All five saved handoffs are copied exactly by script, not manually retyped. The source PDFs or original instruments control OCR discrepancies. This validator has not independently reread those raw sources and does not claim to have done so.

Snapshot integrity:

'''
for p in paths+[out]: body+=f'- `{p.relative_to(term).as_posix()}`: SHA-256 `{sha(p)}`.\n'
receipt.write_text(body,encoding='utf-8',newline='\n')
assert all(t in out.read_text(encoding='utf-8') for t in texts)
print('Mobil neutral freeze and receipt created; all five exact handoff copies verified.')
