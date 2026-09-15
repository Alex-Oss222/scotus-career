import fs from 'node:fs';
import crypto from 'node:crypto';
const dir='tmp/OT1991CHUNK6',term='terms/OT1991';
const cases=JSON.parse(fs.readFileSync(`${dir}/data.json`,'utf8'));
const baseline=JSON.parse(fs.readFileSync(`${dir}/protected-before.json`,'utf8'));
const hash=f=>crypto.createHash('sha256').update(fs.readFileSync(f)).digest('hex');
const assert=(ok,msg)=>{if(!ok)throw Error(msg);};
const filename=c=>`${c.key}_${c.type==='DIG'?'dismissal_of_writ':'merits'}_${c.date}.md`;
const before=fs.readFileSync(`${dir}/workspace-before.md`,'utf8');
const blocker='Holmes v. Securities Investor Protection Corp., No. 90-727 (March 24, 1992): the official record presents an independent claim under SIPA §78eee(d) for liquidation-administration advances. Section II version 1 supplies no Stone disposition or legal ground for that claim. Engine §4 requires that missing approved choice before the matter can be adjudicated. The question has been sent to the user; no decision, vote, holding or remedy for this event is committed.';
assert(cases.length===9,'This finalization expects nine completed cases and one stopped matter');
const now=cases.map(c=>({c,f:filename(c),r:fs.readFileSync(`${term}/records/${filename(c)}`,'utf8'),p:fs.readFileSync(`${dir}/drafts/${c.key}.render.md`,'utf8')}));
for(const {f,r} of now)assert(r===fs.readFileSync(`${dir}/drafts/${f}`,'utf8'),`Record differs from validated draft: ${f}`);
let w=before;
w=w.replace('**Workspace status:** Chunk 5 completed; forty-one Court events and one admitted institutional source have been processed.','**Workspace status:** Chunk 6 processed: nine events completed and Holmes stopped for the specific approval gap below. Fifty Court events and one admitted institutional source have been processed in the term.');
w=w.replace('**Chronology cursor:** March 4, 1992, after *McCarthy v. Madigan*.','**Chronology cursor:** March 24, 1992, after *United States v. Wilson*, with the same-day Holmes event still open and unadjudicated.');
const lines=w.split('\n');let changed=0;
for(let i=0;i<lines.length;i++){
 const c=cases.find(c=>lines[i].startsWith(`| ${c.date} | ${c.name},`));
 if(c){const a=lines[i].split('|');a[3]=` ${c.type==='DIG'?'PROCEDURAL — dismissal of writ':'MERITS decision'} `;a[5]=` Completed: ${c.action} Record committed. `;a[6]=` See records/${filename(c)}. Common start-of-day baseline preserved. `;lines[i]=a.join('|');changed++;}
 else if(lines[i].startsWith('| 1992-03-24 | Holmes v. Securities Investor Protection Corp.,')){
  const a=lines[i].split('|');a[5]=' Stopped and open: no adjudication or Decision Record. ';a[6]=' Missing approved Stone disposition and legal ground for the independent SIPA §78eee(d) claim for administration advances. Obtain that choice before completing this event; the other March 24 cases are uncoordinated and independent. ';lines[i]=a.join('|');changed++;
 }
}
assert(changed===10,'Manifest chunk-six rows not all updated');w=lines.join('\n');
const ledger=now.map(({c,f},i)=>`| ${43+i} | ${c.date} | *${c.name}*, ${c.type==='DIG'?'dismissal of writ':'merits decision'} | CDR — \`records/${f}\` | Validated and committed; common start-of-day baseline preserved |`).join('\n');
w=w.replace('\n## Term Continuity Note',`\n${ledger}\n\n## Term Continuity Note`);
function replaceSection(title,nextTitle,body){const start=w.indexOf(title),end=w.indexOf(nextTitle,start+title.length);assert(start>=0&&end>start,`Missing section ${title}`);w=w.slice(0,start)+title+'\n\n'+body.trim()+'\n\n'+w.slice(end);}
replaceSection('### 1. Scope and Chronology Cursor','### 2. Completed Events and Admitted Sources',`- **Term / exact opening trackers:** OT1991; \`state/HOLDINGS.md\`, \`state/STANDARDS_AND_TESTS.md\` and \`state/STANDING_STATE.md\`, each processed through October 7, 1991 and issued September 14, 2026.
- **Manifest:** All 123 items remain: 122 inventory entries plus Thomas’s oath and circuit reallotment. Fifty-one entries are completed: fifty Court events and one admitted institutional source. Nine chunk 6 events were completed; Holmes remains stopped. PFZ’s anticipated merits event is now a dismissal of the writ. No item was added, removed or rescheduled. Wyoming’s completed merits event does not close its retained original proceeding.
- **Coverage:** Chunks 1–5 and the nine completed events in chunk 6. Previous same-day baselines remain. All March 9 events use the baseline after McCarthy; their six records were committed before the March 24 refresh. The March 24 events use that common refreshed baseline, without same-day precedential priority.
- **Latest processed change:** *United States v. Wilson*, March 24, 1992. The chronology cursor does not falsely close Holmes, another March 24 event.
- **Next pending work:** Resolve the stated Holmes approval gap. The next inventory date is March 25, beginning with *Suter v. Artist M.*; before a later case proceeds, check whether the still-open Holmes issue is a material dependency. A later Holmes completion must preserve the March 24 start-of-day baseline and audit any later completed matter for dependence. Any actual Wyoming filing must be reconciled by effective date.`);
replaceSection('### 2. Completed Events and Admitted Sources','### 3. Current Law',`All fifty-one validated records appear in the Term Working Ledger above with their natural identities, effective dates and durable locations. Entries 1–42 remain unchanged. Entries 43–51 are the nine completed chunk 6 decisions: Dawson, Romein, Williams, Stringer, Germain, PFZ, R.L.C., Darden and Wilson. Holmes has no record and supplies no law. No correction exists. The exact new public projection is \`render-inputs/OT_1991CHUNK6.md\`; the five earlier Render Inputs remain unchanged. This Run produces no public render.`);
const newLaw=now.map(({c,f,r})=>{
 const start=r.indexOf('## Law of the decision\n\n')+'## Law of the decision\n\n'.length;
 const end=r.indexOf('\n## Law after the decision',start);
 const holdingText=r.slice(start,end).trim().replace(/^### /gm,'##### ');
 return `#### ${c.name} — ${c.date}\n\n**Record:** \`records/${f}\`.\n\n${holdingText}\n\n**Current operation and change:** ${c.after}\n\n**Posture and limits:** ${c.procedure}`;
}).join('\n\n');
w=w.replace('\n### 4. Material Published Noncontrolling Positions',`\n${newLaw}\n\n### 4. Material Published Noncontrolling Positions`);
const noncontrolling=now.filter(({c})=>!c.separate.startsWith('No separate')).map(({c,f})=>`- **${c.name}, ${c.date}** — source: the separately named writings in \`records/${f}\`. ${c.separate} No later treatment is established; these positions do not change controlling law.`).join('\n\n');
w=w.replace('\n### 5. Current Procedure and Institution',`\n${noncontrolling}\n\n### 5. Current Procedure and Institution`);
w=w.replace('five votes supply a majority for the participating Court sizes in chunks 4 and 5.','five votes supply a majority for the nine participating Justices in every completed chunk 6 event; earlier reduced-Court thresholds remain as recorded.');
w=w.replace('Earlier participation facts remain in entries 1–25.','Earlier participation facts remain in entries 1–25. All nine participated at argument and decision in each completed chunk 6 event; all arguments were after Thomas’s oath.');
const newProcedure='- **Chunk 6 stages:** '+cases.map(c=>`${c.name}: ${c.procedure}`).join(' ')+' Holmes remains open for the specific workflow gap in §6, not a merits ruling. No new external filing, return date or retained Supreme Court proceeding is inferred.';
w=w.replace('\n### 6. Blockers and Revalidation Needs',`\n${newProcedure}\n\n### 6. Blockers and Revalidation Needs`);
replaceSection('### 6. Blockers and Revalidation Needs','### 7. Source and Research Cutoff',`${blocker}

The missing choice affects Holmes only. R.L.C. concerns the juvenile statutory cap, Darden the ERISA employee definition, and Wilson sentence-credit administration; none depends on the unresolved RICO/SIPA matter. They were completed on the March 24 start-of-day baseline. Before any later event dependent on Holmes proceeds, resolve that block and perform the required chronological dependency review.

Wyoming remains open for implementation, not blocked. Preserve the exact current-term limits: Dawson leaves harmless-error availability open by seven Justices; Williams requires both causal harmlessness and reasonable departure extent; Stringer leaves procedural default and actual cure unresolved; Germain grants no automatic appeal; PFZ supplies no merits law; R.L.C. establishes a ceiling without a majority lenity methodology; Darden decides no ultimate employee status; Wilson preserves review of proper BOP calculations. Earlier limitations in §3 remain unchanged, including Doherty’s fracture, Elias-Zacarias’s separate grounds, Rufo’s decree obligations, Hudson’s narrow majority, Nordic Village’s federal waiver scope, Franklin’s unresolved attribution and McCarthy’s particular claim/process. No historical follow-on event is automatically admitted.`);
replaceSection('### 7. Source and Research Cutoff','## Current-Term Neutral Projection',`Continuation requires the three identified opening trackers, the complete manifest and ledger, all fifty-one durable records and six Render Input files. The earlier records preserve their source support. Chunk 6 used the ten official United States Reports PDFs for 503 U.S. 159–346, downloaded from GovInfo and read in full, including footnotes and separate writings, plus the complete official PFZ argument and the CAP lower-court materials identified in the records. Holmes’s report was researched but its event was not adjudicated. Internet Archive catalog searches were discovery only; no unread briefs are represented as reviewed. Research performed September 14, 2026; completed events have in-world cutoffs of March 9 or March 24, 1992. No later law or unverified connected external event is admitted, and no intervening Wyoming filing is established.`);
const pstart=w.indexOf('## Current-Term Neutral Projection');assert(pstart>0,'Projection marker missing');
w=w.slice(0,pstart)+`## Current-Term Neutral Projection

### Projection boundary

This projection contains current law, public procedure, roster, allotments, published Justice positions and manifest dependencies. It excludes private Stone cores, provisional commitments, comparator reconciliation and audit annexes. Workflow gaps identify the missing input without supplying its substance.

### Authority and chronology

- **Term / divergence:** OT1991; Stone replaced Rehnquist on October 7, 1991.
- **Chronology cursor:** March 24, 1992, after *United States v. Wilson*. Holmes’s same-day event remains unadjudicated.
- **Effective records:** All fifty-one ledger entries. The identified opening trackers remain the October 7 baseline.
- **Next work:** The unresolved Holmes input must be supplied before its event can be completed. The next inventory date is March 25, beginning with Suter; dependency review must account for the open Holmes event and any verified Wyoming filing.

### Current law

The complete cumulative additions, exact propositions, majority authority, precedent treatment and limits are in Term Continuity Note §3. Those records control any conflict. Earlier law is preserved unless expressly displaced. Chunk 6 adds Dawson’s relevance application and reserved remand, Romein’s contract and retroactivity applications, Williams’s separate error-effect and reasonableness inquiries, Stringer’s old-rule and weighing-cure holdings, Germain’s available statutory appeal route, R.L.C.’s adult-derived ceiling, Darden’s general agency definition and Wilson’s credit-calculation rule. PFZ is a dismissal without a merits holding. Holmes contributes no holding. Neither R.L.C.’s divided methodology nor any separate writing becomes law through aggregation.

### Public procedure, roster and allotments

Use Note §5: all nine members, unchanged October 23 circuit allotments, the pre-oath participation rule and six-member quorum. All nine participated at argument and decision in every completed chunk 6 event. Five explicit joins are necessary for a controlling proposition in these cases. No private dismissal poll is published.

### Open matters and dependencies

Wyoming retains original implementation jurisdiction over the January 22 injunction; no later filing or hearing date is established. Holmes remains an uncompleted March 24 event requiring an additional approved issue position as identified in §6. The nine completed chunk 6 proceedings are terminal at the Supreme Court stage; lower-court work continues only on the recorded terms. Stringer’s procedural default and actual state cure are unresolved on remand. R.L.C.’s resentencing already occurred. Do not invent a new Supreme Court return or erase an open proceeding at term close without a terminal action or express carry-forward.

### Material published Justice positions

Note §4 preserves all cumulative published positions with their author, joins, source, date and noncontrolling scope. For chunk 6, preserve Stone’s distinct Dawson remedy, Blackmun’s harmlessness reservation and Thomas’s relevance dissent; White/Kennedy’s Williams statutory dissent; Souter/Scalia/Thomas’s Stringer new-rule dissent; Germain’s four judgment-only writers; Stone’s PFZ dissent seeking a merits affirmance; the separate R.L.C. methodology and juvenile-discretion positions; and Stevens/White’s Wilson actor/timing dissent. No unpublished provisional commitment or comparator enters this projection.
`;
// Preserve all earlier substantive and noncontrolling text, not just a summary.
const oldCurrent=before.slice(before.indexOf('### 3. Current Law'),before.indexOf('### 4. Material Published Noncontrolling Positions')).trim();
const oldNC=before.slice(before.indexOf('### 4. Material Published Noncontrolling Positions'),before.indexOf('### 5. Current Procedure and Institution')).trim();
assert(w.includes(oldCurrent),'Earlier cumulative current law was lost');
assert(w.includes(oldNC),'Earlier published positions were lost');
const manifestCount=w.split('\n').filter(l=>/^\| 199[12]-/.test(l)).length;assert(manifestCount===123,`Manifest count ${manifestCount}`);
const ledgerRows=[...w.matchAll(/^\| (\d+) \| (199[12]-\d\d-\d\d) \|/gm)];assert(ledgerRows.length===51,'Ledger must contain 51 entries');
assert(ledgerRows.every((m,i)=>Number(m[1])===i+1),'Ledger sequence broken');
for(const m of w.matchAll(/(?:CDR|ASR) — `records\/([^`]+)`/g))assert(fs.existsSync(`${term}/records/${m[1]}`),`Missing ledger target ${m[1]}`);
const meta=`# OT_1991CHUNK6 — Render Inputs

## Chunk metadata

- **October Term:** 1991.
- **Chunk:** 6.
- **Completed events:** Nine, in the ordered sequence below: Dawson; General Motors v. Romein; Williams; Stringer; Connecticut National Bank v. Germain; PFZ Properties; United States v. R.L.C.; Nationwide v. Darden; United States v. Wilson.
- **Effective-date range:** March 9–24, 1992. The six March 9 events share a start-of-day baseline; the March 24 entries use the baseline after those six records, without intra-day precedence.
- **Stopped matter / Simulation Workflow Blocker:** ${blocker}
- **Projection status:** Every completed entry below has its validated Canonical Decision Record. This is the eleven-block input for a separate Render task, not the public render. No private conference or certiorari poll is supplied.

`;
const ri=meta+now.map(x=>x.p).join('\n---\n\n');
const blockNames=['Event','Participation','Public Action','Judgment & Remedy','Opinion Topology','Holdings','Precedent Treatment','Law After Decision','Separate Writings','Procedure After Action','Source Notes'];
for(const {c,r,p} of now){const actual=[...p.matchAll(/^## (.+)$/gm)].map(m=>m[1]);assert(JSON.stringify(actual)===JSON.stringify(blockNames),`Bad eleven-block projection: ${c.name}`);const a=p.indexOf('## Holdings\n\n')+'## Holdings\n\n'.length,z=p.indexOf('\n\n## Precedent Treatment',a);const h=p.slice(a,z);assert(r.includes(h),`Holdings changed in projection: ${c.name}`);}
assert(!/\b8[–-]1\b/.test(now.find(x=>x.c.type==='DIG').p),'PFZ private poll leaked');
assert(!ri.includes('Approved Stone core')&&!ri.includes('Adaptive audit annex'),'Private core or audit leaked');
for(const [f,digest] of Object.entries(baseline))assert(hash(f)===digest,`Protected file changed: ${f}`);
const newHashes=Object.fromEntries(now.map(x=>[`${term}/records/${x.f}`,hash(`${term}/records/${x.f}`)]));
fs.writeFileSync(`${dir}/workspace-final.md`,w);
fs.writeFileSync(`${dir}/render-input-final.md`,ri);
const audit={result:'passed',completedChunkEvents:9,stoppedMatters:1,completedTermLedgerEntries:51,termCourtEvents:50,institutionalSources:1,manifestItems:123,orderedRenderBlocks:99,protectedFilesUnchanged:123,earlierCumulativeLawPreserved:true,earlierPublishedPositionsPreserved:true,allLedgerTargetsExist:true,holdingsIdentity:true,noPFZPrivatePoll:true,newRecordHashes:newHashes};
fs.writeFileSync(`${dir}/final-validation.json`,JSON.stringify(audit,null,2));
if(process.argv[2]==='write'){
 assert(!fs.existsSync(`${term}/render-inputs/OT_1991CHUNK6.md`),'Render Input already exists');
 assert(fs.readFileSync(`${term}/workspace.md`,'utf8')===before,'Workspace changed since baseline; reconcile first');
 fs.writeFileSync(`${term}/render-inputs/OT_1991CHUNK6.md`,ri,{flag:'wx'});
 fs.writeFileSync(`${term}/workspace.md`,w);
 for(const [f,digest] of Object.entries({...baseline,...newHashes}))assert(hash(f)===digest,`Immutable file changed on final write: ${f}`);
 assert(fs.readFileSync(`${term}/workspace.md`,'utf8')===w,'Workspace write mismatch');
 assert(fs.readFileSync(`${term}/render-inputs/OT_1991CHUNK6.md`,'utf8')===ri,'Render Input write mismatch');
}
console.log(JSON.stringify({...audit,mode:process.argv[2]||'draft',workspaceBytes:Buffer.byteLength(w),renderInputBytes:Buffer.byteLength(ri)},null,2));
