import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import {cases} from './day2.mjs';
import {all} from './data.mjs';
const dir='tmp/OT1991CHUNK6';
const term='terms/OT1991';
const mode=process.argv[2]||'check';
const hash=f=>crypto.createHash('sha256').update(fs.readFileSync(f)).digest('hex');
const baseline=JSON.parse(fs.readFileSync(`${dir}/protected-before.json`,'utf8'));
function invariant(ok,msg){if(!ok)throw new Error(msg);}
for(const [f,digest] of Object.entries(baseline))invariant(hash(f)===digest,`Protected file changed: ${f}`);
const brief=fs.readFileSync(`${term}/briefs/OT_1991CHUNK6.md`,'utf8');
const stoneRuntime=fs.readFileSync(`${term}/runtime/OT_1991CHUNK6_STONE.md`,'utf8');
const norm=s=>s.replace(/\r/g,'').replace(/\s+/g,' ').trim();
const coreMap={};
for(const block of stoneRuntime.split(/^# (?!(?:SECTION|OT_1991CHUNK6))(?=\S)/m).slice(1)){
 const name=block.slice(0,block.indexOf('\n')).trim();
 const core=block.slice(block.indexOf('# SECTION II:')).replace(/\s*---\s*$/,'').trim();
 invariant(norm(brief).includes(norm(core)),`Runtime Section II mismatch: ${name}`);
 invariant(core.includes('**Version:** 1.'),`Wrong approved version: ${name}`);
 coreMap[name]=core;
}
invariant(Object.keys(coreMap).length===10,'Expected ten version-1 cores');
const before=fs.readFileSync(`${dir}/workspace-before.md`,'utf8');
const oldLinks=[...before.matchAll(/CDR — `records\/([^`]+)`|ASR — `records\/([^`]+)`/g)].map(m=>m[1]||m[2]);
invariant(oldLinks.length===42,'Opening ledger must have 42 records');
for(const f of oldLinks)invariant(fs.existsSync(`${term}/records/${f}`),`Missing opening record: ${f}`);
const participation="Chief Justice Alex-Lamar Stone-Zsela and Justices White, Blackmun, Stevens, O'Connor, Scalia, Kennedy, Souter and Thomas participated at argument and decision. Every argument occurred after Thomas’s October 23, 1991 oath. No established recusal or nonparticipation. Nine participants; six-member quorum satisfied; five votes required for a judgment or controlling opinion.";
const names=a=>a.length?a.join(', '):'None';
const filename=c=>`${c.key}_${c.type==='DIG'?'dismissal_of_writ':'merits'}_${c.date}.md`;
const holdings=c=>c.holdings.length?c.holdings.map(x=>`### ${x.title}\n\n**Holding and operative rule:** ${x.rule}\n\n**Authority:** ${x.part}\n\n**Controlling explanation:** ${x.explanation}\n\n**Precedent treatment:**\n\n${x.precedents.map(p=>'- '+p).join('\n')}`).join('\n\n'):'No substantive holding. The unexplained dismissal of the writ decides no merits proposition and adopts no lower-court rationale.';
function opinions(c){return '| Writing | Author | Joined by | Judgment relationship and exact scope |\n|---|---|---|---|\n'+c.opinions.map(o=>`| ${o.name} | ${o.author} | ${names(o.join)} | ${o.scope} |`).join('\n');}
function judgment(c,pub=false){
 if(pub&&c.publicPoll===false)return `${c.action}\n\nThe Court dismisses the writ without a published individual poll. Stone’s noted dissent would reach and affirm the substantive claim. The lower judgment remains in place without an affirmance or a merits endorsement. No permit, damages or remand is ordered.`;
 return `${c.action}\n\n| Component | Disposition | Vote | Supporting Justices | Other positions | Remedy |\n|---|---|---|---|---|---|\n`+c.votes.map(v=>`| ${v.component} | ${v.result} | ${v.support.length}–${v.against.length} | ${names(v.support)} | ${names(v.against)} | ${v.remedy} |`).join('\n');
}
const sourceNotes=c=>`[Official United States Reports, 503 U.S. ${c.page}](https://www.govinfo.gov/content/pkg/USREPORTS-503/pdf/USREPORTS-503-${c.page}.pdf) supplies the historical docket, argument date, judgment below, material record, reported questions and separate historical writings. [Judgment below](${c.lowerUrl}) supplies the lower-court source. The present Court’s disposition, authorship and exact joins are stated above; the historical reporter is a source anchor, not an additional controlling decision in this term.${c.type==='DIG'?' [Official February 26 argument](https://www.supremecourt.gov/pdfs/transcripts/1991/91-122_02-26-1992.pdf) supports the question-scope and pleading disputes; counsel’s assertions are not findings.':''} Research cutoff: ${c.date}. No later law or unverified follow-on filing is included.`;
const blocks=c=>({
 Event:`${c.name}; No. ${c.docket}; October Term 1991. ${c.type==='DIG'?'Dismissal of writ after plenary argument':'Merits decision'}, ${c.date}; argued ${c.argued}. On writ of certiorari to ${c.lower}.\n\nQuestion: ${c.question}\n\nRecord and relief sought: ${c.facts}\n\nRender form: ${c.form}; ${c.basis}`,
 Participation:participation,
 'Public Action':c.action,
 'Judgment & Remedy':judgment(c,true),
 'Opinion Topology':opinions(c),
 Holdings:holdings(c),
 'Precedent Treatment':c.holdings.length?c.holdings.flatMap(x=>x.precedents).filter((x,i,a)=>a.indexOf(x)===i).map(p=>'- '+p).join('\n'):'No precedent is adopted, extended, limited or overruled by the dismissal. The lower court’s reasoning acquires no Supreme Court authority.',
 'Law After Decision':c.after,
 'Separate Writings':c.separate,
 'Procedure After Action':c.procedure,
 'Source Notes':sourceNotes(c)
});
const cutoff=c=>`The in-world source and connected-event cutoff is ${c.date}. Research was performed September 14, 2026. All ten official report PDFs for this chunk were downloaded and their full extracted texts, including separate opinions and footnotes, were reviewed before final assembly; archival typesetting dates are not later legal authority. Internet Archive Records and Briefs catalog searches were attempted first for the captions; returned catalog entries are discovery only, not a claim that the underlying briefs were read. No Justia source was used. The CAP lower opinion is available at the linked source; material issue and disposition support was checked against the official report, without claiming that every lengthy lower opinion or the complete party-brief set was independently read. No quotation, concession, docket event or factual finding is supplied from an unread brief. No intervening Wyoming implementation filing is established, and no follow-on event is automatically admitted.`;
function record(c){
 const b=blocks(c);
 return `# Canonical Decision Record — ${c.name}\n\n## Event and chronology\n\n${b.Event}\n\nStage before: plenary review on an existing writ of certiorari. Stage after: ${c.procedure}\n\nChronology: ${c.date==='1992-03-09'?'All six March 9 events use the common start-of-day baseline after the 42-entry opening ledger, through McCarthy on March 4. Their internal inventory sequence is not an order of precedential priority.':'All March 9 records have been validated, durably committed and applied before this March 24 refresh. The four March 24 inventory events share a common start-of-day baseline; none treats another March 24 decision as earlier law.'}\n\n## Participation and law entering the event\n\n${participation}\n\nLaw-Entering Snapshot: ${c.entering}\n\nThe opening Holdings and Standards and Tests contain no completed simulated term or substantive entry. Their processed cutoff is October 7, 1991, issued September 14, 2026. Current-term law comes from the effective records indexed in the workspace, not a tracker edit. No current Standards and Tests provision title or wording authority is invented. Constitutional and statutory provisions are applied as effective on the event date.\n\n## Stone: approval, fixed core and revalidation\n\nSection II version 1 in briefs/OT_1991CHUNK6.md was expressly approved as written by the user’s instruction to Run chunk 6 on September 14, 2026. That direction supersedes the preserved input label “Proposed and unapproved.” The runtime core was mechanically matched to the combined brief.\n\n${c.stoneCheck}\n\nNo additional discretion envelope is inferred. Compatible proposition-level joins express the approved ground; a broader ground is withheld. No new Stone burden, alternative ground, remedy or fallback is supplied. The approved source core is preserved verbatim below.\n\n## Public action, judgment and opinions\n\n${judgment(c)}\n\n${opinions(c)}\n\nAssignment: ${c.assignment} Assignment and authorship are simulation inferences under the Engine, not assertions about historical conference activity. No fictional dialogue or draft history is created.\n\n## Law of the decision\n\n${holdings(c)}\n\n## Law after the decision and authority limits\n\n${c.after}\n\n${c.type==='DIG'?'No Marks inquiry is applicable: there is no merits rationale.':c.key==='United_States_v_RLC'?'No Marks reconstruction is used for the common Court parts, and no majority is manufactured from the incompatible methodological opinions.':'Every controlling proposition listed above has at least five explicit joins at the same operative level. Judgment-only or dissenting votes are not added to its support; no Marks reconstruction is necessary.'}\n\n## Material published noncontrolling positions\n\n${c.separate}\n\nEvery separate position above is noncontrolling unless its exact proposition is also expressly included in the majority holding. Its date is ${c.date}, its source is the writing named in the topology, and no later treatment is asserted. The public selection includes only positions needed to explain authority, scope, remedy or the procedural action.\n\n## Procedure and continuity\n\n${c.procedure}\n\nNo roster, seniority or circuit-allotment change results. The October 23 allotment remains: Stone—D.C., Fourth, Federal; Souter—First; Scalia—Second and Third; O’Connor—Fifth; Stevens—Sixth and Seventh; Blackmun—Eighth; Kennedy—Ninth; White—Tenth; Thomas—Eleventh. Wyoming’s retained original implementation jurisdiction is unaffected. Lower-court proceedings do not imply retained Supreme Court supervision.\n\n## Sources, cutoff and validation\n\n${sourceNotes(c)}\n\nSource-to-fact map:\n\n- The official report’s caption and introductory record establish docket, argument date, reported decision date, channel and lower judgment. The simulation adopts the authorized inventory date as the event date.\n- The official report and CAP lower opinion support the record/posture and litigation-position description, with allegations, assumptions and holdings kept distinct.${c.type==='DIG'?' The complete official argument was also read; OCR gaps were not reconstructed as quotations and historical Chief Justice remarks were not attributed to Stone.':''}\n- The neutral runtime packet supplies the initial issue map; its stale assertion of no current-term law was replaced by the dated entering-law refresh.\n- The pre-divergence authorities and statutory text discussed in the neutral packet and official report supply received law; this matter’s historical opinion is used for source facts and comparator reconciliation, not as prior simulated precedent.\n- The opening trackers, 42 earlier ledger records and dated current-term additions supply simulated law. Source facts and simulation assignment/coalition inferences remain separate.\n\n${cutoff(c)}\n\nValidation: the local build checks protected-file integrity, ten approved version-1 runtime cores against the brief, all 42 opening ledger targets, participant membership, unique vote entries and complete nine-person judgment partitions, majority support for each holding, opinion join membership, 120–200 words for every controlling explanation, exact Holdings identity in the eleven-block projection, block order and append-only destination absence. These checks passed before this record was written. Substantive review separately checked legal reach, fixed-core compatibility, correct lower-court remedy, same-day independence, proposition-level joins and the historical reconciliation below. Mechanical tools checked consistency and did not choose legal outcomes. No unresolved event blocker remains for this completed matter.\n\nDurable location: records/${filename(c)}. Committed to Current Term State on September 14, 2026, effective ${c.date}; see the cumulative workspace ledger. Full check output is retained in tmp/OT1991CHUNK6/validation-${c.date}.json. No prior immutable record is corrected or replaced.\n\n## Adaptive audit annex\n\nMode: single-conversation staged adjudication; true blindness was unavailable. Neutral runtime was opened first, and provisional commitments were frozen in tmp/OT1991CHUNK6/neutral-freeze.md before opening the comparator. Comparator review and supplemental neutral-source reconciliation were frozen in tmp/OT1991CHUNK6/reconciliation-freeze.md before opening Stone last. General model knowledge and earlier conversational exposure remain limitations. Neutral web discovery revealed Germain’s reversal and some archive catalog disposition wording; those exposures were disclosed in the first freeze. New neutral details learned from official reports were explicitly refreshed before Stone rather than silently treated as initially known. Clean-context repair was unavailable in the chosen single-conversation mode; independence is weaker, and no blindness is claimed.\n\n| Justice(s), individually identified | Provisional commitment and sufficient ground | Comparator reconciliation / final commitment |\n|---|---|---|\n${c.audit.map(r=>'| '+r.join(' | ')+' |').join('\n')}\n\nAlternative-path review: ${c.alternatives}\n\nHistorical reconciliation: ${c.comparison}\n\nFinal compatibility: ${c.assignment} No non-Stone substantive commitment changed after the reconciliation freeze. The exact partial joins in the topology preserve all recorded barriers.\n\n## Approved Stone core — verbatim source preservation\n\n${coreMap[c.name]}\n`;
}
const keys=['Event','Participation','Public Action','Judgment & Remedy','Opinion Topology','Holdings','Precedent Treatment','Law After Decision','Separate Writings','Procedure After Action','Source Notes'];
// Dawson's two actual opinion parts are represented separately for precise joins.
const d=cases[0];
d.opinions.splice(0,1,
 {name:'Opinion of the Court, Part A',author:'White',join:all.filter(j=>!['White','Thomas'].includes(j)),scope:'Constitutional relevance and application; supports sentence-only vacatur.'},
 {name:'Opinion of the Court, Part B',author:'White',join:all.filter(j=>!['Stone','White','Thomas'].includes(j)),scope:'Remand leaving both the availability and application of harmless-error review open.'});
const selected=mode==='day1'?cases.filter(c=>c.date==='1992-03-09'):mode==='day2'?cases.filter(c=>c.date==='1992-03-24'):cases;
const check={protectedFilesUnchanged:Object.keys(baseline).length,approvedCoresMatched:10,openingLedgerTargets:42,events:[]};
fs.mkdirSync(`${dir}/drafts`,{recursive:true});
for(const c of selected){
 invariant(coreMap[c.name],`Missing Stone core: ${c.name}`);
 invariant(c.argued.includes('1991')||c.argued.includes('1992'),'Argument date absent');
 for(const v of c.votes){invariant(new Set(v.support).size===v.support.length&&new Set(v.against).size===v.against.length,'Duplicate vote');invariant(new Set([...v.support,...v.against]).size===9&&[...v.support,...v.against].every(j=>all.includes(j)),'Incomplete participant partition');invariant(v.support.length+v.against.length===9,'Overlapping votes');}
 for(const o of c.opinions){invariant(new Set(o.join).size===o.join.length&&o.join.every(j=>all.includes(j)),'Invalid opinion join');invariant(!o.join.includes(o.author),'Author listed as own joiner');}
 const counts=c.holdings.map(x=>{const n=x.explanation.trim().split(/\s+/).length;invariant(n>=120&&n<=200,`${c.name}: ${x.title}: explanation ${n} words`);invariant(x.support.length>=5&&new Set(x.support).size===x.support.length&&x.support.every(j=>all.includes(j)),'Invalid holding coalition');return {title:x.title,words:n,support:x.support.length};});
 const b=blocks(c);invariant(JSON.stringify(Object.keys(b))===JSON.stringify(keys),'Render block order mismatch');
 const rec=record(c);const proj=`# ${c.name}\n\n`+keys.map(k=>`## ${k}\n\n${b[k]}`).join('\n\n')+'\n';
 invariant(rec.includes(b.Holdings),'Holdings differ');
 fs.writeFileSync(`${dir}/drafts/${filename(c)}`,rec);
 fs.writeFileSync(`${dir}/drafts/${c.key}.render.md`,proj);
 check.events.push({case:c.name,date:c.date,holdings:counts,blocks:11,record:filename(c)});
}
if(mode==='day1'||mode==='day2'){
 if(mode==='day2')for(const c of cases.filter(c=>c.date==='1992-03-09'))invariant(fs.existsSync(`${term}/records/${filename(c)}`),'March 9 predecessor not committed');
 for(const c of selected)invariant(!fs.existsSync(`${term}/records/${filename(c)}`),'Immutable destination already exists');
 fs.writeFileSync(`${dir}/validation-${selected[0].date}.json`,JSON.stringify({...check,result:'passed before record commitment'},null,2));
 for(const c of selected){fs.writeFileSync(`${term}/records/${filename(c)}`,fs.readFileSync(`${dir}/drafts/${filename(c)}`),{flag:'wx'});fs.writeFileSync(`${dir}/current-state-${c.date}.md`,selected.filter(x=>cases.indexOf(x)<=cases.indexOf(c)).map(x=>`## ${x.name}\n\n${x.after}\n\n${x.procedure}`).join('\n\n'));}
}
fs.writeFileSync(`${dir}/data.json`,JSON.stringify(cases,null,2));
fs.writeFileSync(`${dir}/check-latest.json`,JSON.stringify(check,null,2));
console.log(JSON.stringify({mode,...check},null,2));
export {cases,blocks,filename,record,keys};
