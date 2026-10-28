from pathlib import Path
import hashlib

base = Path('terms/OT1998')
source = base / 'freeze/OT_1998CHUNK6_B_PROC_COMMITMENTS.md'
original = source.read_text(encoding='utf-8')
start = original.index('## 1. Murphy Brothers, Inc.')
end = original.index('## 2. Conn v. Gabbert')
murphy = original[start:end]
header = '''# OT1998 chunk 6 — reconciled Associate commitments: Murphy Brothers

**Stage and scope:** Historical reconciliation under Engine §§3C, 7 and 14. This handoff finalizes the eight non-Stone commitments for Murphy Brothers only, before assignment or Stone assembly. Conn is expressly not ready and is not finalized by this file. No Stone position, Court vote total, author assignment or completed adjudication is supplied.

**Inputs and chronology:** The controlling provisional handoff is `freeze/OT_1998CHUNK6_B_PROC_COMMITMENTS.md`, read with `freeze/OT_1998CHUNK6_B_FRESH_PREFLIGHT.md`, the Murphy and Conn entries of `runtime/OT_1998CHUNK6_B_NEUTRAL.md`, the relevant Murphy and Conn parts of `entering-law/OT_1998CHUNK6_B_FRESH_SELECTED.md`, and `runtime/OT_1998CHUNK6_B_PROC_COMPARATOR.md`. The fresh preflight corrects the stale original packet's baseline and Murphy posture. Entering law is validated through March 17, 1999; the scheduled event is April 5, 1999. Final earlier-law review remains a control task. No newly completed earlier event or new intervening law has yet been supplied to this reconciliation. Independent April 5 matters do not become authority for each other merely through writing order.

**Final commitment content:** The complete Murphy section below is copied mechanically from the frozen independent commitments. It preserves every judgment, proposition, join boundary and remedy. The subsequent reconciliation tests those positions against the complete historical writings; it does not incorporate their authorship, rhetoric or every additional discussion into this Court's commitments.

'''
review = '''## 2. Murphy historical reconciliation

The historical Court reversed and remanded, 6–3. Its six supporting Associates were Stevens, O'Connor, Kennedy, Souter, Ginsburg and Breyer. Scalia and Thomas joined the historical dissent's receipt construction. All eight frozen judgment positions therefore match their historical positions. That match is confirmed by the preserved premises: the courtesy copy preceded formal service, the established intervals put removal outside the receipt period but within the service period, and review followed a certified denial of remand. The independent analysis already used those premises; historical agreement supplies corroboration, not a substitute for the statutory analysis.

The historical majority's full explanation treats formal process as the background for responsive duties, interprets the 1949 amendment as giving access to the complaint across different state procedures, and compares the parallel answer-period language. Its footnote 4 expressly addresses the separate summons branch and its filed-pleading/no-service-required conditions. Its footnote 6 distinguishes permissible removal before completed service from an obligation to remove before service. Neither footnote permits erasing a statutory trigger. The final frozen construction preserves both branches, their thirty-day periods and the shorter-period direction; it does not transform the opinion's illustrative categories into a new factual ruling about an unpresented service sequence. Precise waiver timing and any other unpresented process equivalent remain unresolved.

The historical dissent treats receipt through service or otherwise as an express trigger and rejects adding service as an unstated precondition, reinforced by strict construction of removal statutes. That is the actual source of Scalia's and Thomas's historical disagreement, not a contrary fact or a denial of the importance of summons for personal jurisdiction. Their independently frozen construction retains that distinction and applies the receipt interval without finding a valid default or enlarging state-court authority.

| Associate | Frozen position after comparison | Justice-specific reconciliation and operative boundary |
|---|---|---|
| Stevens | Retained: reverse and remand; complete service-linked rule. | His historical join relied on the procedural function of service. His simulated Henderson join likewise distinguishes service procedure from subject-matter jurisdiction, while his Caterpillar join preserves the enacted removal sequence. Neither prior position supplies an earlier deadline contrary to the two statutory branches. The unchanged fax/service premise supports his retained result and full join. |
| O'Connor | Retained: reverse and remand; complete service-linked rule. | Her historical join is consistent with her simulated Caterpillar opinion's distinction between prospective statutory compliance and preservation of a completed jurisdictionally sound trial judgment. Her Henderson dissent concerns the particular sovereign-consent condition, not an informal-receipt trigger. She adopts statutory construction here, without an equitable excuse or a new jurisdictional classification. |
| Scalia | Retained: affirm the appellate remand direction; complete receipt rule. | The historical dissent he joined gives direct effect to the first branch's express receipt language. His simulated Henderson opinion's source-specific treatment of conflicting enacted provisions and his Caterpillar join do not displace that textual objection. Prior service added to the first branch remains his join barrier; personal-jurisdiction requirements do not independently determine removal timing. |
| Kennedy | Retained: reverse and remand; complete service-linked rule. | His historical join rests on process as the background for the pleading-information trigger. His simulated Henderson and Caterpillar joins preserve different procedural events and their statutory consequences. He can retain that construction while rejecting both universal jurisdictional treatment and an asserted Caterpillar cure. |
| Souter | Retained: reverse and remand; complete service-linked rule. | The historical contextual construction fits his simulated Henderson join without treating notice as process. The summons alternative's express conditions answer the concern that a general actual-receipt requirement would erase one statutory branch. No changed premise requires departure from his historical join. |
| Thomas | Retained: affirm the appellate remand direction; complete receipt rule. | His historical dissent join rests on the enacted receipt trigger, not merely a generic preference for narrow federal jurisdiction. His simulated Things Remembered opinion enforces actual statutory categories, and his Henderson dissent requires an enacted basis before relaxing a retained condition. Those commitments support distinguishing receipt in the first branch from expressly required summons service in the second. |
| Ginsburg | Retained: reverse and remand; complete service-linked rule. | Her historical reasoning distinguishes actual notice from an imposed litigation obligation and accommodates different state pleading-service systems. Her simulated Henderson and Caterpillar joins preserve that procedural distinction without discretionary deadline extensions. The frozen statutory rule retains that sufficient ground; historical authorship supplies no present assignment. |
| Breyer | Retained: reverse and remand; complete service-linked rule. | His historical join accords with his simulated Henderson and Caterpillar joins' attention to the statutory procedure's actual operation. Practical uncertainty reinforces the contextual construction without creating an independent fairness exception or a power to enlarge the thirty days. Both statutory alternatives remain operative. |

**No changed Associate row:** No Murphy commitment is replaced. No material historical departure is established in judgment, controlling statutory construction or remedy. The historical closing reference to a clearer congressional statement is understood as the explanation of this particular interpretation, not an independently adopted universal clear-statement doctrine; the frozen analysis expressly rejects creating such a doctrine. The source's broader discussions of foreign-service difficulties, older procedural practice and illustrative state categories are not additional findings about this record or independently frozen holdings.

**Separate-writing function, without assignment:** Scalia and Thomas support a dissenting explanation that receipt of the filed complaint is the first branch's statutory event; the phrase allowing receipt otherwise than by service must do its enacted work. The second branch, with its filed-pleading and no-service-required conditions, remains distinct. Congress may require a timely election of a federal forum before state process creates a duty to answer, and that election deadline neither authorizes default without service nor establishes personal jurisdiction. They would sustain the appellate remand direction on untimeliness. The six supporting reversal reject that construction for the contextual reasons copied above. No separate concurrence or additional ground is required by a frozen Associate position. The assembly stage assigns the actual writing or writings under Engine §8.

**Final Murphy arithmetic and remedy:** Six Associates support reversal and the same service-linked rule; two support affirmance and the receipt rule. No distinct rationale is added to create a coalition. The six would reverse the Eleventh Circuit's timeliness judgment and remand for otherwise authorized federal proceedings; the two would preserve its direction to remand to state court. No contract merits, fees, waiver, equitable extension, other removal defect or new service fact is adjudicated. Final assignment, Stone compatibility and the event-date earlier-law check remain necessary.

## 3. Conn — source return required; no final commitment in this handoff

The complete historical writings reveal a material difference obscured by a judgment-only comparison. All eight Associates historically supported reversal, but Stevens's concurrence did **not** use qualified immunity as its sufficient ground. It concluded that the supplied injury did not deprive Gabbert of liberty or property, relying on the stated absence of evidence of adverse effects on income, reputation, clientele or professional qualifications and the stated absence of real evidence or allegation of substantial client prejudice. It separately rejected treating a possible Fourth Amendment violation as sufficient to extinguish an independently established due-process violation. The other seven Associates joined the historical majority's occupational-merits ground; its own footnote expressly left the pleaded Fourth Amendment claim outside review.

The frozen independent Stevens row instead reserves the occupational merits and rests on conduct-time qualified immunity alone. Those grounds must not be counted as equivalent, and a concurrence-in-the-judgment label cannot conceal their difference. The fresh neutral packet reports no ban or disqualification, but it does not supply the more specific absence-of-evidence recitations on which the historical Stevens concurrence relied. Lack of those statements in the packet is a research limit, not a finding that the historical evidence was different. His simulated Albright dissent and Lewis immunity position support preserving independently applicable rights and considering immunity; standing alone, they do not establish a concrete changed premise warranting departure from his actual Conn ground, which also preserved overlapping protections.

**Required affected refresh:** Return only the record propositions concerning occupational injury and client prejudice, with their exact source limitation, through fresh neutral validation. The published opinion can establish what its author reported about the record under Engine §14; it does not authorize independent certification of unrecovered pleadings, the cited appendix or actual absence of harm. The fresh model must then assess the resulting bounded premise, refreeze the affected Conn commitments, and undergo reconciliation before assembly. No Stevens row is patched here, no newly discovered fact is adopted by this reconciliation, and no hypothetical client injury or actual economic loss is invented. Control has been notified of this precise issue.

The seven other frozen occupational-merits positions remain available for the affected review, but this handoff does not certify Conn final readiness or determine whether the added neutral statement changes any row, scope or join. Its prior Fourth Amendment reservation remains essential: that claim was pleaded but is outside review; the occupational disposition must neither validate nor extinguish it. No new client-right or third-party-standing holding is supplied merely because the historical majority discussed one.

## 4. Source-read and separation receipt

Read the complete saved Cornell syllabus, majority and dissent for Murphy Brothers: `97-1909.ZS.html.txt`, `97-1909.ZO.html.txt` (including notes 1–7), and `97-1909.ZD.html.txt`. Read the complete saved Cornell syllabus, majority and Stevens concurrence for Conn: `97-1802.ZS.html.txt`, `97-1802.ZO.html.txt` (including the footnote reserving the separately pleaded Fourth Amendment claim), and `97-1802.ZC.html.txt`. The official U.S. Reports text crosscheck covered Murphy, 526 U.S. 344–357, and Conn, 526 U.S. 286–294, including every writing and footnote. The published primary writings support the comparator; neither syllabus alone nor an aggregator summary substitutes for an opinion.

Public source locations: [Murphy majority](https://www.law.cornell.edu/supct/html/97-1909.ZO.html), [Murphy dissent](https://www.law.cornell.edu/supct/html/97-1909.ZD.html), [Conn majority](https://www.law.cornell.edu/supct/html/97-1802.ZO.html), [Conn concurrence](https://www.law.cornell.edu/supct/html/97-1802.ZC.html), and [official volume 526](https://www.supremecourt.gov/opinions/boundvolumes/526bv.pdf). All are historical comparator sources here, not independently effective simulated adjudications.

The original saved Murphy official extract contained an extraneous tail from the next case's opening syllabus pages, printed 358–359, UNUM Life Insurance Co. of America v. Ward. Reading that supplied extract exposed the tail. No proposition, fact, outcome or later law from it was used. Control subsequently trimmed the source to Murphy's printed 344–357. This receipt discloses the actual exposure; it does not claim the original file was correctly bounded. Occasional tool-output truncation was repaired by rereading the complete bounded Cornell writings and the missing official passage; no unread omitted footnote is represented as read.

The fresh preflight's Mitchell discussion was visible in the authorized shared preflight; no Mitchell modeling or reconciliation was performed. The substantive entering-law review used its Murphy section, Conn section, and supplied West Covina, Haddle and Albright public material. No current or earlier private Stone core, supplement or certiorari poll, raw Decision Record, or top-level `stone/` path was read, listed or searched. No Git operation was performed. No opinion assignment was made. Writes are confined to OT1998; Python ran with `-B`. Original pleadings, warrants, service papers, merits briefs and the Conn appendix were not independently recovered or represented as read.

**Status:** Murphy ready for the later event-date check and assembly; Conn returned for affected neutral/model refresh. The frozen copy of this handoff is byte-identical to runtime. This artifact completes no adjudication and alters no workspace, brief, state tracker, foundation file or public render.

## 5. Mechanical content receipt

These SHA-256 digests identify input bytes at completion, not repository-history identifiers. The trimmed Murphy official digest identifies the corrected bounded file; the preceding receipt preserves the actual earlier tail exposure.

| Input | SHA-256 |
|---|---|
'''
paths = [source,
base/'freeze/OT_1998CHUNK6_B_FRESH_PREFLIGHT.md',
base/'runtime/OT_1998CHUNK6_B_NEUTRAL.md',
base/'entering-law/OT_1998CHUNK6_B_FRESH_SELECTED.md',
base/'runtime/OT_1998CHUNK6_B_PROC_COMPARATOR.md']
paths += [base/'sources/chunk6-comparator'/n for n in ['97-1909.ZS.html.txt','97-1909.ZO.html.txt','97-1909.ZD.html.txt','97-1802.ZS.html.txt','97-1802.ZO.html.txt','97-1802.ZC.html.txt','murphy_brothers_official.txt','conn_official.txt']]
rows=''.join(f'| `{p.as_posix()}` | `{hashlib.sha256(p.read_bytes()).hexdigest()}` |\n' for p in paths)
data=(header+murphy+review+rows).encode('utf-8')
runtime=base/'runtime/OT_1998CHUNK6_B_PROC_RECONCILED.md'
frozen=base/'freeze/OT_1998CHUNK6_B_PROC_RECONCILED.md'
runtime.write_bytes(data)
frozen.write_bytes(data)
assert runtime.read_bytes()==frozen.read_bytes()
assert runtime.read_text(encoding='utf-8').count('| Stevens |')==2
assert 'Conn is expressly not ready' in header
print(f'Wrote identical runtime/freeze: {len(data)} bytes; SHA-256 {hashlib.sha256(data).hexdigest()}')
