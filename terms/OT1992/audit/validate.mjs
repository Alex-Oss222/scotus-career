import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import assert from 'node:assert/strict';

const root=path.resolve(import.meta.dirname,'..');
const target=process.argv[2]?path.resolve(root,process.argv[2]):root;
const read=p=>fs.readFileSync(path.join(target,p),'utf8').replace(/\r\n/g,'\n');
const sha=t=>crypto.createHash('sha256').update(t).digest('hex');
const source=JSON.parse(fs.readFileSync(path.join(root,'audit/source_inventory.json'),'utf8'));
const provenance=JSON.parse(fs.readFileSync(path.join(root,'audit/case_provenance.json'),'utf8'));
const manifest=JSON.parse(read('OT_1992_LOAD_MANIFEST.json'));
const checks=[];
function check(label,fn) { fn(); checks.push(label); }
function blocks(text) {
  return [...text.matchAll(/^## (.+)\n([\s\S]*?)(?=^## |$(?![\s\S]))/gm)].map(m=>({caption:m[1],body:m[0].trim().replace(/\n+---\s*$/,'').trim()}));
}
function split(body) {
  const at=[...body.matchAll(/^### SECTION (I|II|III) — .+$/gm)];
  assert.equal(at.map(m=>m[1]).join(','),'I,II,III');
  return {prefix:body.slice(0,at[0].index).trim(),parts:at.map((m,i)=>body.slice(m.index,at[i+1]?.index??body.length).trim())};
}
const expected=source.matters.toSorted((a,b)=>a.date.localeCompare(b.date)||a.sourceSet-b.sourceSet||a.listRank-b.listRank);
const expectedNames=Array.from({length:11},(_,i)=>`OT_1992CHUNK${i+1}`);
check('Original 51 plus additional 72 equals 123 unique matter identities',()=>{
  assert.equal(expected.length,123); assert.equal(new Set(expected.map(m=>m.caption)).size,123);
  assert.equal(new Set(expected.map(m=>m.listedDocket)).size,123);
});
check('Exactly 11 consecutively numbered chunks',()=>assert.deepEqual(fs.readdirSync(target).filter(n=>/^OT_1992CHUNK\d+\.md$/.test(n)).sort(),expectedNames.map(n=>n+'.md').sort()));
const runtimeNames=expectedNames.flatMap(n=>['NEUTRAL','STONE','COMPARATOR'].map(k=>n+'_'+k+'.md'));
check('Exactly 33 correctly numbered runtime exports',()=>assert.deepEqual(fs.readdirSync(path.join(target,'runtime')).sort(),runtimeNames.sort()));
const gathered=[];
for(let i=0;i<11;i++) {
  const name=expectedNames[i],text=read(name+'.md'),ms=blocks(text);
  check(`${name}: correct header, count and source-list membership`,()=>{
    assert(text.startsWith('# '+name+'\n')); assert.equal(ms.length,i===10?3:12);
    assert.deepEqual(ms.map(m=>m.caption),expected.slice(i*12,(i+1)*12).map(m=>m.caption));
  });
  ms.forEach(m=>gathered.push({...m,chunk:i+1}));
  ['NEUTRAL','STONE','COMPARATOR'].forEach((kind,k)=>{
    const actual=read(`runtime/${name}_${kind}.md`);
    const wanted=`# ${name}_${kind}\n\n`+ms.map(m=>{const s=split(m.body);return s.prefix+'\n\n'+s.parts[k];}).join('\n\n---\n\n')+'\n';
    check(`${name}_${kind}: exact section text and exact membership`,()=>assert.equal(actual,wanted));
    check(`${name}_${kind}: section isolation`,()=>{
      assert.equal((actual.match(/^### SECTION /gm)||[]).length,ms.length);
      const permitted=['I','II','III'][k];
      assert([...actual.matchAll(/^### SECTION (I|II|III) /gm)].every(m=>m[1]===permitted));
      if(k===0) assert(!/\*\*Historical (Outcome|Opinion Structure)|\*\*Stone[’']s Proposed/.test(actual));
    });
  });
}
check('Canonical, manifest, and original list identities agree in stable date order',()=>{
  assert.equal(manifest.matterCount,123); assert.equal(manifest.chunkCount,11); assert.equal(manifest.chunkLimit,12);
  assert.deepEqual(manifest.matters.map(m=>m.caption),expected.map(m=>m.caption));
  assert.deepEqual(gathered.map(m=>m.caption),expected.map(m=>m.caption));
});
for(let i=0;i<123;i++) {
  const m=gathered[i],e=expected[i],mm=manifest.matters[i],p=provenance.find(x=>x.caption===m.caption);
  check(`${m.caption}: original docket, event date, source priority and preservation`,()=>{
    assert.equal(mm.listedDocket,e.listedDocket); assert.equal(mm.docket,e.listedDocket.split(';')[0].trim());
    assert.equal(mm.date,e.date); assert.equal(mm.chunk,m.chunk); assert.equal(mm.position,i+1);
    assert.equal(m.body.match(/\*\*Simulated Event Date:\*\* (\d{4}-\d{2}-\d{2})/)[1],e.date);
    const identity=m.body.match(/\*\*Citation or Docket:\*\* (.+)/)[1];
    const docketTokens=e.listedDocket.split(';')[0].match(/A-\d+|\d{2}-\d+|\d+(?=, Original)/g);
    assert(docketTokens.every(d=>identity.includes(d)));
    assert.equal(mm.sourcePath,e.sourcePath); assert.equal(p.sourceBodySha256,e.sourceBodySha256);
    assert.equal(sha(m.body),p.finalBodySha256); assert.equal(mm.bodySha256,p.finalBodySha256);
    const s=split(m.body); assert.deepEqual(s.parts.map(sha),p.sectionHashes);
    assert.equal(p.sectionHashes[1],p.sourceSectionHashes[1]); assert.equal(p.sectionHashes[2],p.sourceSectionHashes[2]);
    if(!p.changed) assert.equal(p.finalBodySha256,p.sourceBodySha256);
    assert(!/OT_1992CHUNK\d+/.test(m.body),'Stale numerical chunk reference');
    if(i) assert(e.date>=expected[i-1].date);
  });
}
const indexRows=read('OT_1992_CASE_INDEX.md').split('\n').filter(l=>/^\| \d+ \|/.test(l)).map(l=>l.split('|').slice(1,-1).map(x=>x.trim()));
check('All 123 index rows exactly mirror manifest and canonical assignments',()=>assert.deepEqual(indexRows,manifest.matters.map(m=>[String(m.position),String(m.chunk),m.caption,m.docket,m.date,m.eventType,m.category])));
const apps={
  'Grubbs v. Delo':['Blackmun','Eighth','1992-10-20'],
  'Martin v. District of Columbia Court of Appeals':['Stone-Zsela','District of Columbia','1992-11-02'],
  'Demos v. Storrie':['Kennedy','Ninth','1993-03-08'],
  'Turner Broadcasting System, Inc. v. FCC':['Stone-Zsela','District of Columbia','1993-04-29'],
  'Blodgett v. Campbell':['Kennedy','Ninth','1993-05-14'],
  'Delo v. Blair':['Blackmun','Eighth','1993-07-21'],
  'DeBoer v. DeBoer':['Stevens','Sixth','1993-07-26'],
};
check('Exactly seven applications, three original actions, three procedural dispositions',()=>{
  assert.deepEqual(manifest.matters.filter(m=>m.category==='APPLICATION').map(m=>m.caption).sort(),Object.keys(apps).sort());
  assert.equal(manifest.matters.filter(m=>m.category==='ORIGINAL').length,3);
  assert.equal(manifest.matters.filter(m=>m.category==='PROCEDURAL').length,3);
  assert.equal(manifest.matters.filter(m=>m.category==='MERITS').length,110);
});
for(const [caption,[presenter,circuit,date]] of Object.entries(apps)) {
  check(`${caption}: full Court, presenter, posture and conditional order`,()=>{
    const m=gathered.find(m=>m.caption===caption),n=split(m.body).parts[0];
    assert.equal(manifest.matters.find(m=>m.caption===caption).date,date);
    assert(n.includes(presenter),caption+' presenter'); assert(n.includes(circuit),caption+' circuit'); assert(/majority/.test(n));
    assert(/refer(?:red|s|ral)/i.test(n)); assert(/full.Court/i.test(n));
    assert(/presented to [^.\n]+referred to the Court is \[/.test(n));
    assert(/without a merits opinion/.test(n)); assert(/Consequences|consequences/.test(n));
    if(caption.startsWith('Delo v. Blair')||caption.startsWith('DeBoer')) assert(/eight|Eight/.test(n));
  });
}
for(const f of manifest.files) check(`File integrity: ${f.path}`,()=>assert.equal(sha(fs.readFileSync(path.join(target,f.path))),f.sha256));
check('No source or completed-record files selected for cleanup',()=>{
  for(const f of source.files) assert(/^(OT_1992CHUNK\d+\.md|OT_1992_COMPLETE_PACKET_REVISED\/(OT_1992CHUNK\d+\.md|OT_1992_CASE_INDEX\.md|runtime\/OT_1992CHUNK\d+_(NEUTRAL|STONE|COMPARATOR)\.md)|OT_1992_ADDITIONAL_72\/(OT_1992_CASE_INDEX\.md|OT_1992_ADDITIONAL_72_(RUNTIME_MANIFEST|VALIDATION)\.md|runtime\/OT_1992CHUNK\d+_(NEUTRAL|STONE|COMPARATOR)\.md))$/.test(f.path));
});
const result={status:'PASS',checks:checks.length,matters:123,chunks:11,runtimeFiles:33,unalteredStoneSections:123,unalteredComparatorSections:123,checksPassed:checks};
fs.writeFileSync(path.join(root,'audit','validation_results.json'),JSON.stringify(result,null,2)+'\n');
console.log(JSON.stringify({...result,checksPassed:undefined},null,2));
