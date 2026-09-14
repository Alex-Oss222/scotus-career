import fs from 'node:fs';
import {dir,term,blocks,report,renderInput,holdings,validate,checkProtected} from './build.mjs';
const files=['Hudson_v_McMillian_merits_1992-02-25.md','United_States_v_Nordic_Village_merits_1992-02-25.md','Holywell_Corp_v_Smith_merits_1992-02-25.md','Franklin_v_Gwinnett_County_Public_Schools_merits_1992-02-26.md','INDOPCO_v_Commissioner_merits_1992-02-26.md','Arkansas_v_Oklahoma_merits_1992-02-26.md','Collins_v_City_of_Harker_Heights_merits_1992-02-26.md','Willy_v_Coastal_Corp_merits_1992-03-03.md','McCarthy_v_Madigan_merits_1992-03-04.md'];
const events=files.map(f=>JSON.parse(fs.readFileSync(`${dir}/${f}.json`,'utf8')));
const backup=`${dir}/workspace-before.md`;
if(!fs.existsSync(backup))fs.copyFileSync(`${term}/workspace.md`,backup,fs.constants.COPYFILE_EXCL);
const original=fs.readFileSync(backup,'utf8');
for(const e of events){
 validate(e);
 if(fs.readFileSync(`${dir}/${e.file}`,'utf8')!==fs.readFileSync(`${term}/records/${e.file}`,'utf8'))throw Error('Committed/staged mismatch '+e.name);
 const cdr=fs.readFileSync(`${term}/records/${e.file}`,'utf8');
 if(!cdr.includes('## Law of the decision\n\n'+holdings(e)+'\n\n## Law after the decision'))throw Error('Holding mismatch '+e.name);
 if(e.audit.length!==8||new Set(e.audit.map(a=>a.justice)).size!==8)throw Error('Audit coverage '+e.name);
}

// Project only the validated public fields. The chosen form stays fixed; the
// accompanying basis omits the private historical-reconciliation detail.
function publicInput(e){
 const r=renderInput(e);
 const grouping=e.date==='1992-02-25'?'One of three uncoordinated decisions on February 25; listed in supplied order, without a within-day sequence of legal effect.':e.date==='1992-02-26'?'One of four uncoordinated decisions on February 26; listed in supplied order, without a within-day sequence of legal effect.':'No same-day grouping is supplied.';
 const basis=e.form==='compact'?'the judgment margin is at least two votes and there is no material change requiring full form.':e.page===1?'the Court has partial joins and different authority at the narrow holding and universal-rule levels.':e.page===115?'the unanimous judgment has different nine-Justice and eight-Justice rationale coalitions and a partial concurrence.':'the controlling rationale has seven Justices, with a distinct two-Justice judgment concurrence; the material coalition difference requires full form.';
 r.values[0]=`${e.name}; ${e.docket}; OT1991. Reporter reference: 503 U.S. ${e.page} (1992). Merits decision, ${e.date}. Argued ${e.argued}. On writ${e.docket.includes(';')?'s':''} of certiorari to the ${e.below}. ${e.event}\n\nQuestions: ${e.questions}\n\nRecord and posture: ${e.record}\n\nChronology: ${grouping}\n\nRender form: ${e.form}; ${basis}`;
 if(e.page===1)r.values[4]=r.values[4].replace('Rejects the significant-injury floor and universal Whitley extension; also addresses nonphysical pain and docket concerns.','Rejects the significant-injury floor and universal Whitley extension.');
 r.values[10]=`[Official United States Reports, 503 U.S. ${e.page}–${e.end}](${report(e.page)}) supplies the dates, lower-court record, procedural history and reproduced governing provisions. The reporter reference identifies the historical source; the disposition, authorship and joins to be presented are those specified in this event’s public-action fields. No opinion quotation is supplied for republication. No later-law source or unrecorded later procedural event is incorporated.`;
 if(r.values[5]!==holdings(e))throw Error('RI Holdings changed');
 return `## ${e.name}\n\n`+blocks.map((b,i)=>`### ${i+1}. ${b}\n\n${r.values[i]}`).join('\n\n');
}
const riName='OT_1991CHUNK5.md';
const ri=`# OCTOBER TERM 1991, CHUNK 5 — RENDER INPUTS\n\n## Chunk metadata\n\n- **October Term:** 1991.\n- **Chunk:** 5.\n- **Completed events:** Nine merits decisions, listed below in effective-date order. The Holywell and Arkansas entries each include both supplied dockets.\n- **Chronological range:** February 25–March 4, 1992.\n- **Same-day groups:** Three events on February 25; four on February 26. Each group is uncoordinated and retains the supplied inventory order.\n- **Stopped matters:** None.\n\n| Effective date | Event | Posture after action |\n|---|---|---|\n`+events.map(e=>`| ${e.date} | ${e.name}; ${e.docket} — merits decision | ${e.procedure} |`).join('\n')+'\n\n'+events.map(publicInput).join('\n\n---\n\n')+'\n';
if(/provisional commitment|provisional vote|Stone.s approved|user.s approval|fixed core|private Stone|historical reconciliation|discretion envelope|audit annex|certiorari poll|conference poll|comparator/i.test(ri))throw Error('Private/operator field in public projection');
for(const b of blocks)if(ri.split(`. ${b}\n\n`).length-1!==9)throw Error('RI block count '+b);
fs.writeFileSync(`${dir}/${riName}`,ri);

let w=original.replace('**Workspace status:** Chunk 4 completed; thirty-two Court events and one admitted institutional source have been processed.','**Workspace status:** Chunk 5 completed; forty-one Court events and one admitted institutional source have been processed.').replace('**Chronology cursor:** January 27, 1992, after *Lechmere, Inc. v. NLRB*.','**Chronology cursor:** March 4, 1992, after *McCarthy v. Madigan*.');
const stages=[
 'Completed: reversed and remanded 7–2; six-Justice narrow force holding; universal Whitley rule has four votes.',
 'Completed: reversed 7–2; federal monetary waiver absent for this recovery.',
 'Completed: reversed unanimously in both dockets; statutory returns and payment duties govern on remand.',
 'Completed: reversed and remanded 9–0; compensatory relief available in the established Title IX action.',
 'Completed: affirmed 9–0; disputed acquisition expenses are capital expenditures.',
 'Completed: reversed 9–0 in both dockets; EPA permit determination sustained on its existing conditions.',
 'Completed: affirmed 9–0; extra §1983 element rejected; substantive constitutional claim fails.',
 'Completed: affirmed 9–0; $19,307 collateral Rule 11 sanction preserved.',
 'Completed: reversed and remanded 9–0; this damages action requires no exhaustion of the described BOP process.'
];
let updated=0;
w=w.split('\n').map(line=>{
 if(!line.startsWith('| ')||!line.includes('| OT_1991CHUNK5 |'))return line;
 const c=line.split('|');
 const i=events.findIndex(e=>c[2].trim()===`${e.name}, 503 U.S. ${e.page} (1992)`);
 if(i<0)throw Error('Unmatched chunk 5 manifest row '+line);
 c[5]=' '+stages[i]+' Record committed. ';
 c[6]=` Completed and projected into current state; see records/${events[i].file}. ${events[i].date<'1992-03-01'?'Uncoordinated same-day baseline preserved.':'All earlier effective decisions applied.'} `;
 updated++;return c.join('|');
}).join('\n');
if(updated!==9)throw Error('Manifest updates '+updated);
const ledgerNew=events.map((e,i)=>`| ${i+34} | ${e.date} | *${e.name}*${e.docket.includes(';')?' (both dockets)':''}, merits decision | CDR — \`records/${e.file}\` | Validated and committed${e.date<'1992-03-01'?'; same-day start-of-day baseline preserved':''} |`).join('\n');
w=w.replace(/\n\n+(## Term Continuity Note)/,`\n${ledgerNew}\n\n$1`);
function replaceSection(n,body){
 const re=new RegExp(`(### ${n}\\. [^\\n]+\\n)[\\s\\S]*?(?=\\n### ${n+1}\\. |\\n## Current-Term Neutral Projection)`);
 if(!re.test(w))throw Error('Missing continuity section '+n);
 w=w.replace(re,(_,h)=>h+'\n'+body.trim()+'\n');
}
replaceSection(1,`- **Term / exact opening trackers:** OT1991; \`state/HOLDINGS.md\`, \`state/STANDARDS_AND_TESTS.md\` and \`state/STANDING_STATE.md\`, each processed through October 7, 1991 and issued September 14, 2026.
- **Manifest:** All 123 items remain: 122 inventory entries plus Thomas’s oath and circuit reallotment. Forty-two entries are completed: forty-one Court events and one admitted institutional source. No item was added, removed or rescheduled. Wyoming’s completed merits event does not close its retained original proceeding.
- **Coverage:** Chunks 1–5. Previously established same-day baselines remain. February 25 and February 26 each use a common start-of-day baseline; the February 25 records were committed before the February 26 refresh. Willy was committed before the March 4 refresh for McCarthy.
- **Latest processed change:** *McCarthy v. Madigan*, March 4, 1992.
- **Next dated eligible item:** *Dawson v. Delaware*, 503 U.S. 159 (1992), March 9, 1992, first of the six-event same-day group in chunk 6. Any actual filing in the retained Wyoming proceeding must be reconciled by its effective date.`);
replaceSection(2,`All forty-two validated records appear in the Term Working Ledger above with their natural identities, effective dates and durable locations; the manifest and the records supply dispositions. Entries 1–33 remain unchanged. Entries 34–42 are the nine chunk 5 merits decisions, including both Holywell/United States v. Smith and Arkansas/EPA v. Oklahoma dockets. No correction exists. The exact new public projection is \`render-inputs/OT_1991CHUNK5.md\`; the four earlier Render Inputs remain unchanged. This Run does not produce a public render.`);
const laws=events.map(e=>`#### ${e.name} — ${e.date}\n\n${e.law}\n\n`+e.holdings.map(h=>`**${h.title}.** ${h.rule}\n\n**Authority:** ${h.authority}\n\n**Precedent treatment:**\n\n${h.precedents.map(p=>'- '+p).join('\n')}`).join('\n\n')+(e.nonholding?'\n\n**Authority limits:** '+e.nonholding:'')+`\n\n[Source record](records/${e.file}).`).join('\n\n');
w=w.replace('\n### 4. Material Published Noncontrolling Positions','\n'+laws+'\n\n### 4. Material Published Noncontrolling Positions');
const published=events.filter(e=>e.continuity).map(e=>`- **${e.name}, ${e.date}:** ${e.continuity.replace(' and imports no private Master text','')} [Source record](records/${e.file}).`).join('\n');
w=w.replace('\n### 5. Current Procedure and Institution','\n'+published+'\n\n### 5. Current Procedure and Institution');
const old5=original.split('### 5. Current Procedure and Institution\n')[1].split('\n### 6.')[0].trim();
replaceSection(5,old5.replace('five votes supply a majority for either participating Court size in chunk 4.','five votes supply a majority for the participating Court sizes in chunks 4 and 5.').replace('Earlier participation facts remain in entries 1–25.','All nine participated at argument and decision in every chunk 5 event; each was argued after Thomas’s oath. Earlier participation facts remain in entries 1–25.')+`\n- **Chunk 5 stages:** Supreme Court merits review ends in all nine events. Hudson returns without the rejected injury floor or a new award; Nordic Village’s monetary judgment is reversed; Holywell’s ordinary remand applies the specified filing/payment duties; Franklin returns for liability, attribution, causation and loss; INDOPCO’s denial of immediate deductions stands; Arkansas’s permit is sustained with existing conditions; Collins’s federal dismissal stands; Willy’s $19,307 sanction and prior state-court direction stand; McCarthy returns without the rejected exhaustion gate. No new Supreme Court proceeding, return date or external follow-on act is established.`);
replaceSection(6,`No chunk 5 matter is stopped, and no missing approved choice or unresolved source conflict remains. Wyoming’s implementation proceeding is open, not blocked. Before chunk 6, refresh neutral packets against every effective holding, reservation and published noncontrolling position above; preserve the March 9 common baseline unless authorized sources establish coordination. Hudson establishes a six-Justice narrow rule, not a majority universal Whitley formulation. Nordic Village does not supply a State-immunity disposition; Franklin decides compensation’s availability, not recipient attribution; Collins adopts no general affirmative-danger test; McCarthy governs this claim and contemporaneous process, without changing a congressional command or expanding Bivens. Preserve Doherty’s absence of a substantive majority, Elias-Zacarias’s distinct nexus/review holdings and Rufo’s consent obligations. No historical follow-on event is automatically admitted.`);
replaceSection(7,`Continuation requires the three identified opening trackers, the complete manifest and ledger, all forty-two durable records, and five Render Input files. Earlier source support remains in the prior records. Chunk 5 used all nine separate official United States Reports PDFs spanning 503 U.S. 1–158, downloaded from GovInfo and read in full, including footnotes and separate writings. Records map those primary sources to material facts, dates and rules; Internet Archive entries identify docket-collection discovery, without representing unread briefs as reviewed. Research performed September 14, 2026; each record states its own in-world effective-date cutoff, through March 4, 1992 for the chunk. No later law or unverified connected external event is admitted; no intervening Wyoming filing is established.`);
const projection=`## Current-Term Neutral Projection

### Projection boundary

This projection contains current law, public procedure, roster, allotments, published Justice positions and manifest dependencies. It excludes private Stone cores, provisional commitments, historical reconciliation and audit annexes.

### Authority and chronology

- **Term / divergence:** OT1991; Stone replaced Rehnquist on October 7, 1991.
- **Chronology cursor:** March 4, 1992, after *McCarthy v. Madigan*.
- **Effective records:** All forty-two ledger entries. The identified opening trackers remain the October 7 baseline.
- **Next dated event:** *Dawson v. Delaware*, March 9, 1992, first of six uncoordinated same-day events, subject to any verified intervening implementation filing in Wyoming.

### Current law

The complete cumulative additions, exact operative propositions, proposition-level authority, precedent treatment and preserved limitations appear in Term Continuity Note §3. Earlier law remains unless expressly displaced. Doherty’s asylum disposition has no common majority rationale, and its equally divided withholding judgment has no precedential force. The eight chunk 4 decisions retain the scopes stated there. Chunk 5 adds Hudson’s narrow six-Justice force holding; Nordic Village’s specific federal monetary-waiver ruling; Holywell’s statutory tax duties; Franklin’s compensation remedy; INDOPCO’s capital classification; Arkansas’s federal permit authority and review rules; Collins’s distinct liability and substantive-right holdings; Willy’s collateral Rule 11 authority; and McCarthy’s statutory and practical exhaustion ruling. Hudson’s universal force standard has four votes and is noncontrolling. Each record controls any conflict in this projection.

### Public procedure, roster and allotments

Use Note §5, including all nine members, unchanged circuit allotments, the pre-oath participation rule, six-member quorum and majority requirement. All nine participated in every chunk 5 argument and decision. A dissent or judgment-only writing is not a proposition-level join.

### Open matters and dependencies

Wyoming retains original implementation jurisdiction over the January 22 injunction. No next filing or hearing date is established. All other completed chunk proceedings are terminal at the Supreme Court stage; lower-court or agency work continues only on the recorded terms. Do not erase Wyoming at term close without a terminal action or express carry-forward. Later matters must respect the specific claim, statutory source, relief and reserved questions of each effective decision.

### Material published Justice positions

Note §4 and its cited records preserve the complete cumulative material positions for Justice-specific modeling at their stated noncontrolling scope. Keep Hudson’s four-Justice formulation, Stevens’s separate standard, Blackmun’s judgment concurrence and Thomas/Scalia’s dissent distinct from the six-Justice narrow Court holding. Keep the two-Justice Franklin and McCarthy judgment concurrences and Stone’s Collins partial concurrence distinct from the Court’s respective rationales. None acquires controlling force merely because it is useful in a later matter.
`;
w=w.slice(0,w.indexOf('## Current-Term Neutral Projection'))+projection;
fs.writeFileSync(`${dir}/workspace-after.md`,w);

// Mechanical integrity checks do not select legal outcomes.
const manifest=s=>s.split('## Full-Term Event Manifest')[1].split('### Manifest controls')[0].split('\n').filter(l=>/^\| \d{4}-/.test(l));
const beforeRows=manifest(original),afterRows=manifest(w);
if(beforeRows.length!==123||afterRows.length!==123)throw Error('Manifest count');
if(beforeRows.filter((l,i)=>l!==afterRows[i]).length!==9)throw Error('Unexpected manifest changes');
beforeRows.forEach((l,i)=>{const a=l.split('|'),b=afterRows[i].split('|');for(const k of [1,2,3,4,7])if(a[k]!==b[k])throw Error('Inventory field changed');});
const ledger=s=>s.split('## Term Working Ledger')[1].split('## Term Continuity Note')[0].split('\n').filter(l=>/^\| \d+ \|/.test(l));
const priorLedger=ledger(original),newLedger=ledger(w);
if(priorLedger.length!==33||newLedger.length!==42)throw Error('Ledger count');
priorLedger.forEach((l,i)=>{if(newLedger[i]!==l)throw Error('Prior ledger modified');});
newLedger.forEach((l,i)=>{if(Number(l.split('|')[1].trim())!==i+1)throw Error('Ledger sequence');const f=l.match(/`(records\/[^`]+)`/)[1];if(!fs.existsSync(`${term}/${f}`))throw Error('Missing record '+f);});
if(afterRows.filter(l=>/^Completed(?: merits)?:/.test(l.split('|')[5].trim())).length!==42)throw Error('Completed manifest count');
if((w.match(/### [1-7]\. /g)||[]).length!==7)throw Error('Continuity headings');
for(const e of events){if(!w.includes(e.law))throw Error('Missing law');for(const h of e.holdings)if(!w.includes(h.rule)||!w.includes(h.authority))throw Error('Missing current rule/authority');if(!ri.includes(holdings(e)))throw Error('RI holding continuity');}
const originalLaw=original.split('### 3. Current Law\n')[1].split('\n### 4.')[0].trim();
const originalPositions=original.split('### 4. Material Published Noncontrolling Positions\n')[1].split('\n### 5.')[0].trim();
if(!w.includes(originalLaw)||!w.includes(originalPositions))throw Error('Cumulative prior material missing');
if(!w.includes('No later decree, filing, hearing, compliance finding or terminal event is established.'))throw Error('Wyoming status lost');
if(fs.existsSync(`${term}/output/${riName}`))throw Error('Unexpected chunk 5 public render');
console.log(checkProtected());
console.log('Validated: nine immutable CDRs; nine ordered eleven-block inputs; exact Holdings projection; 123 manifest items, 42 completed; 42 ledger entries; prior 33 entries and cumulative law/positions preserved; Wyoming remains open.');
if(process.argv.includes('--commit')){
 if(fs.readFileSync(`${term}/workspace.md`,'utf8')!==original)throw Error('Workspace changed since baseline');
 fs.copyFileSync(`${dir}/${riName}`,`${term}/render-inputs/${riName}`,fs.constants.COPYFILE_EXCL);
 fs.copyFileSync(`${dir}/workspace-after.md`,`${term}/workspace.md`);
 console.log('Wrote the chunk 5 Render Inputs exclusively and replaced workspace.md.');
}
