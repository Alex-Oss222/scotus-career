from pathlib import Path
import re

term=Path(__file__).resolve().parents[1]
source=term/'runtime/OT_1997CHUNK4_NEUTRAL.md'
text=source.read_text(encoding='utf-8')
text=text.replace(text.split('\n\n',2)[1], 'Thirteen dated matters. This derived neutral candidate carries the current public-law baseline through February 13, 1998 and links the source validation supplements. It supplies no completed chunk-4 outcome. Current-term holdings apply only from their effective dates; uncoordinated same-day matters share one entering baseline.')
chunks=re.split(r'(?=^# (?!SECTION I|OT_1997CHUNK4).+$)',text,flags=re.M)
index=0
for k,block in enumerate(chunks):
    if not block.startswith('# ') or block.startswith('# OT_1997CHUNK4'):continue
    index+=1
    # Replace retired preparation baselines and references with the current authorized publications.
    block=re.sub(r'^\* \*\*Current Through:\*\*.*$', '* **Current Through:** Current state trackers, OT1996 completed through September 15, 1997, plus every effective current-term public holding through February 13, 1998. The case-specific entering-law slice below supplies exact current authority and reusable standards. Add any actually completed material earlier chunk-4 decision before this event; proposed positions supply no law.', block, flags=re.M)
    block=re.sub(r'^\* \*\*Earlier Same-Term Decisions:\*\*.*$', '* **Earlier Same-Term Decisions:** See the case-specific verbatim reading slice and the Current-Term Neutral Projection. Earlier effective law enters; no uncoordinated same-day peer enters by processing order.',block,flags=re.M)
    block=re.sub(r'^\* \*\*Unresolved Same-Term Dependencies:\*\*.*$', '* **Unresolved Same-Term Dependencies:** Apply the refresh gates in [the entering-law index](../entering-law/OT_1997CHUNK4_INDEX.md). A gate requires checking the actual earlier holding, not assuming a change. Material changes require refreshed neutral validation and modeling.',block,flags=re.M)
    block=re.sub(r'^\* \*\*Governing simulation law:\*\*.*$', '* **Governing public law:** [Current Holdings volumes](../../../state/holdings/INDEX.md), [Standards and Tests](../../../state/STANDARDS_AND_TESTS.md), [Standing State](../../../state/STANDING_STATE.md), and the [Current-Term Neutral Projection](../workspace/neutral-projection.md). The case-specific slices copy the operative authority; retired supplied-file references are not authority.',block,flags=re.M)
    block=re.sub(r'^\* \*\*Stone’s position evidence:\*\*.*\n?', '',block,flags=re.M)
    block=re.sub(r'^\* \*\*Preserved source brief:\*\*.*\n?', '',block,flags=re.M)
    # Unavailable old extract links are replaced by live per-case selections below.
    block=re.sub(r'Exact holdings, rationale support, and limitations are preserved in \[law/[^\]]+\]\(law/[^)]+\)\.', 'Exact holdings, rationale support, limits and remedies are copied in the live case-specific entering-law slice below.',block)
    block=re.sub(r'^\* \*\*Current Reusable Doctrine:\*\* See \[law/.*$', '* **Current Reusable Doctrine:** The live case-specific entering-law slice below copies the selected current modules, including their exact titles, operation dates and authority. The controlling holding governs any apparent conflict.',block,flags=re.M)
    block=block.replace('the proposed outcome in Section II is not evidence resolving them', 'a proposed disposition is not evidence resolving them')
    block=block.replace('The historical participation and separate writings are stated in Section III. Historical participation is not silently imposed on Stone’s new Court; no case-specific new-run recusal order has been supplied.', 'No case-specific new-run recusal order has been supplied. Participation at argument or submission and at decision must be validated independently; no historical absence or its reason is inferred.')
    if 'Johnson v. Rodriguez' in block.splitlines()[0]:
        block=block.replace('The Fifth Circuit rejected the due-process and equal-protection claims but remanded a limited retaliation theory.', 'The Fifth Circuit reversed the protest-letter ruling and directed dismissal of that claim with prejudice; reversed and remanded the distinct writ-writer claim for reconsideration or further proceedings, including its retaliation and equal-protection theories; and vacated the dependent attorney-fee award.')
        block=block.replace('Texas law left parole discretionary. Johnson alleged that officials denied release because of protest letters, complaints, and his activity as a jailhouse writ writer. The letters themselves did not identify a protected classification, and the record did not establish an entitlement to parole.', 'This is an official-capacity class action for prospective declaratory and injunctive relief following a bench trial, not an individual-capacity damages case. The class covers present and future Texas prisoners. The distinct claims concern parole protest letters and adverse treatment of prisoners engaged in writ writing. The lower court treated Texas parole as discretionary and distinguished the protest-letter category from the writ-writer group. Whether particular legal activity is protected, whether the representative has standing, whether the findings establish an authorized policy or attributable practice, and whether relief fits the proved injury remain separate questions.')
        block=block.replace('The three claims arise from shared facts but require separate sources and elements. Qualified immunity, personal participation, and causation remain for remand on the retaliation issue.', 'The protest-letter and writ-writer claims require separate analysis. Personal-damages qualified immunity is not at issue in this official-capacity prospective action. Standing, protected legal activity, actual causation, attribution of any policy or practice, the equal-protection comparison, and classwide remedy must be tested on the bench-trial record; the attorney-fee award depends on lawful prevailing-party status.')
    if 'Aponte Matos' in block.splitlines()[0]:
        block=block.replace('Summary judgment involving a warrant affiant and additional officers or supervisors, as supplied.', 'The First Circuit reversed summary judgment only on the material-fabrication claim against warrant affiant Ernesto Laboy-Escobar and remanded that claim; it left the other dismissals effective. The computer-search claim against FBI Agent Plichta and the claim against federal supervisor Ilario were outside appellate jurisdiction because their separate final judgments were not timely appealed. Those components were not affirmed on their constitutional merits.')
        block=block.replace('The complete lower opinion, conduct dates, preserved issues, and defendant-specific record are not supplied. Resolve the question on the facts the actual review posture permits; no factual finding is invented.', 'The full lower opinion is now supplied in the neutral lower-source supplement. The search occurred December 6, 1993. The computer-search and Ilario components were untimely under the separately entered Rule 54(b) judgments; the counsel-access theory was waived by failure to develop it on appeal. The knock-and-announce ruling rested on conduct-date qualified immunity and did not adjudicate the entry’s constitutional reasonableness. Other execution, force, joint-participation and supervision claims require their own record. No finding of fabrication or ultimate damages liability follows from a triable dispute.')
    if 'Spencer v. Kemna' in block.splitlines()[0]:
        block=block.replace('Whether a challenge to parole revocation remains a live Article III controversy after the petitioner completes the entire sentence and shows no concrete continuing consequence.', 'Whether a challenge to parole revocation remains a live Article III controversy after the petitioner completes the entire sentence, what continuing consequences must be shown, and whether the asserted consequences or exceptions suffice.')
        block=block.replace('The Eighth Circuit dismissed the habeas appeal as moot after Spencer’s release.', 'The Eighth Circuit affirmed the district court’s mootness dismissal after Spencer’s sentence expired.')
    if 'Rivet v. Regions' in block.splitlines()[0]:
        block=block.replace('treated the prior federal judgment as completely preempting the state action', 'treated the prior federal judgment as completely precluding the state action and used that asserted preclusion as a removal ground')
    if 'Bogan v. Scott-Harris' in block.splitlines()[0]:
        block=block.replace('Whether local legislators and executive officials are absolutely immune from § 1983 damages for acts that are legislative in form and substance.', 'Whether the challenged municipal budget and ordinance acts are legislative for absolute-immunity purposes and whether that immunity reaches the participating local legislators and executive officials despite the alleged retaliatory motive.')
        block=block.replace('The District Court twice denied petitioners\' motions to dismiss on the ground of absolute immunity from suit.', 'The District Court rejected absolute immunity before trial and again on the post-verdict motion for judgment.')
    if 'Alaska v. Native Village' in block.splitlines()[0]:
        block=block.replace('; Moreau v. Klevenhagen, 508 U.S. 22 (1993) (effective May 3, 1993.)','')
    if 'National Credit Union' in block.splitlines()[0]:
        block=block.replace('; McIntyre v. Ohio Elections Commission (effective April 19, 1995.)','')
        block=block.replace('The agency’s policy history may persuade but cannot rewrite the singular statutory structure.', 'The competing constructions concern the reach of the plural word groups and the common-bond limitation across a credit union’s members. Statutory text, structure and the permissible role of agency interpretation must each be addressed.')
        block=block.replace('and holding that the NCUA had permissibly interpreted § 109.', 'and finding statutory ambiguity; it did not decide second-step reasonableness because respondents had not seriously disputed it.')
    chunks[k]=block

text=''.join(chunks)
slugs=['01_KIRK','02_JOHNSON','03_NEWSWEEK','04_ARTEAGA','05_REGIONS','06_RIVET','07_NCUA','08_VENETIE','09_APONTE','10_SHAHAR','11_SPENCER','12_LEXECON','13_BOGAN']
caseblocks=re.split(r'(?=^# (?!SECTION I|OT_1997CHUNK4).+$)',text,flags=re.M)
index=0
for k,block in enumerate(caseblocks):
    if not block.startswith('# ') or block.startswith('# OT_1997CHUNK4'):continue
    slug=slugs[index];index+=1
    source_note='Read the applicable case sections of [control-extracted neutral facts](../research/chunk4_control/NEUTRAL_FACTS.md) and [additional neutral facts](../research/chunk4_control/NEUTRAL_FACTS_ADDITIONAL.md). They supply the complete supported record qualifications and competing submissions; factual corrections there supersede inconsistent introductory shorthand above. Full same-matter Supreme Court opinions remain outside neutral/modeling access.'
    if slug in ['02_JOHNSON','09_APONTE','10_SHAHAR']:
        lower={'02_JOHNSON':'johnson','09_APONTE':'aponte','10_SHAHAR':'shahar'}[slug]
        source_note=f'Read the applicable case section of [lower-source validation report](../research/chunk4_lower/SOURCE_REPORT.md), with [full date-eligible lower opinion](../research/chunk4_lower/{lower}_opinion.txt) available for the material fork. The report supplies the complete component map and record limits; its supported corrections supersede inconsistent introductory shorthand above. These contain lower-court reasons, not a Supreme Court voting coalition.'
    if slug=='01_KIRK': source_note='The supplied date-eligible lower-opinion recitations and current Rybar/Parker selections remain the sources for this possession-only question. Count One alone is under review; commercial-transfer counts are not substituted for it.'
    addition=f'## F. CURRENT PREFLIGHT AND LIVE SOURCE MAP\n\n**Entering law:** [Case-specific verbatim authority](../entering-law/OT_1997CHUNK4_{slug}.md). The original preparation snapshot does not supersede this current authority.\n\n**Source validation:** {source_note}\n\n**Cutoff:** The assigned event date. No later Supreme Court disposition, private position, unsupported finding, concession, deadline or procedural default supplies a premise. Source unavailability remains distinct from litigant conduct.\n\n'
    caseblocks[k]=block.rstrip()+'\n\n'+addition
candidate=term/'runtime/OT_1997CHUNK4_NEUTRAL_CANDIDATE.md'
candidate.write_text(''.join(caseblocks).rstrip()+'\n',encoding='utf-8')
print(candidate)
print('Cases',index)
