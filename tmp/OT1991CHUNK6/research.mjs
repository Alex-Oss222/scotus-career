import fs from 'node:fs';
import path from 'node:path';
import {execFileSync} from 'node:child_process';
import crypto from 'node:crypto';
const dir='tmp/OT1991CHUNK6';
const headers={'User-Agent':'SCOTUS historical research/1.0'};
const mode=process.argv[2];
async function get(url,name){const r=await fetch(url,{headers,signal:AbortSignal.timeout(45000)});if(!r.ok)throw Error(`${r.status} ${url}`);const b=Buffer.from(await r.arrayBuffer());fs.writeFileSync(`${dir}/${name}`,b);if(name.endsWith('.pdf'))execFileSync('C:/Program Files/Git/mingw64/bin/pdftotext.exe',['-layout',`${dir}/${name}`,`${dir}/${name.replace('.pdf','.txt')}`]);return {url,name,bytes:b.length};}
if(mode==='baseline'){
 const out={};for(const base of ['foundation','state','terms/OT1991/briefs','terms/OT1991/runtime','terms/OT1991/records','terms/OT1991/render-inputs','terms/OT1991/output','terms/OT1991/close']){for(const p of fs.readdirSync(base,{recursive:true})){const f=path.join(base,p);if(fs.statSync(f).isFile())out[f]=crypto.createHash('sha256').update(fs.readFileSync(f)).digest('hex');}}
 fs.writeFileSync(`${dir}/protected-before.json`,JSON.stringify(out,null,2));fs.copyFileSync('terms/OT1991/workspace.md',`${dir}/workspace-before.md`);console.log(Object.keys(out).length+' existing protected files inventoried');
}
if(mode==='archive'){
 const names=['Dawson','Romein','Williams','Stringer','Germain','PFZ','Holmes','R.L.C.','Darden','Wilson'];
 for(const name of names){try {const url='https://archive.org/advancedsearch.php?'+new URLSearchParams({q:`collection:us-supreme-court AND title:(${name}) AND year:1991`,'fl[]':'identifier,title',output:'json'});const j=await(await fetch(url,{headers})).json();fs.writeFileSync(`${dir}/${name}_search.json`,JSON.stringify(j));console.log(JSON.stringify({name,docs:j.response?.docs}));}catch(e){console.log(name+': '+e.message);}}
}
if(mode==='lower'){
 const specs=[['a2d',581,'1078','Dawson'],['mich',436,'515','Romein'],['f2d',910,'1574','Williams'],['f2d',909,'111','Stringer'],['f2d',926,'191','Germain'],['f2d',928,'28','PFZ'],['f2d',908,'1461','Holmes'],['f2d',915,'320','RLC'],['f2d',922,'203','Darden'],['f2d',916,'1115','Wilson']];
 const rs=await Promise.allSettled(specs.map(async([rep,vol,page,name])=>get(`https://static.case.law/${rep}/${vol}/html/${page.padStart(4,'0')}-01.html`,`${name}-below.html`)));rs.forEach(x=>console.log(x.status==='fulfilled'?x.value:String(x.reason)));
}
if(mode==='reports'){
 const rs=await Promise.allSettled([159,181,193,222,249,257,258,291,318,329].map(p=>get(`https://www.govinfo.gov/content/pkg/USREPORTS-503/pdf/USREPORTS-503-${p}.pdf`,`USREPORTS-503-${p}.pdf`)));rs.forEach(x=>console.log(x.status==='fulfilled'?x.value:String(x.reason)));
}
if(mode==='pfz')console.log(await get('https://www.supremecourt.gov/pdfs/transcripts/1991/91-122_02-26-1992.pdf','PFZ-argument.pdf'));
