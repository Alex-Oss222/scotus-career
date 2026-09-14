import fs from 'node:fs';
import path from 'node:path';
import {execFileSync} from 'node:child_process';
const root='tmp/OT1991CHUNK5';
const headers={'User-Agent':'SCOTUS-Term-Research/1.0 (historical legal research)'};
const mode=process.argv[2];
if(mode==='archive'){
 const dockets=['90-6531','90-1629','90-1361','90-918','90-1278','90-1262','90-1279','90-1150','90-6861'];
 for(const docket of dockets){
  try{
   const u='https://archive.org/advancedsearch.php?'+new URLSearchParams({q:`collection:us-supreme-court AND "${docket}"`,'fl[]':'identifier,title',output:'json'});
   const j=await(await fetch(u,{headers})).json();
   for(const doc of j.response.docs){
    const meta=await(await fetch('https://archive.org/metadata/'+doc.identifier,{headers})).json();
    fs.writeFileSync(path.join(root,docket+'_archive.json'),JSON.stringify(meta,null,2));
    console.log(JSON.stringify({docket,identifier:doc.identifier,title:doc.title,files:meta.files.filter(x=>/pdf$|text$|txt$/.test(x.name)).map(x=>({name:x.name,size:x.size}))}));
   }
   if(!j.response.docs.length)console.log(docket+' no archive item');
  }catch(e){console.log(docket+' '+e.message);}
 }
}
if(mode==='reports'){
 const pages=[1,30,47,60,79,91,115,131,140];
 await Promise.allSettled(pages.map(async page=>{
  const filename=`USREPORTS-503-${page}`;
  const url=`https://www.govinfo.gov/content/pkg/USREPORTS-503/pdf/USREPORTS-503-${page}.pdf`;
  const r=await fetch(url,{headers}); if(!r.ok)throw new Error(filename+' '+r.status);
  fs.writeFileSync(path.join(root,filename+'.pdf'),Buffer.from(await r.arrayBuffer()));
  execFileSync('C:/Program Files/Git/mingw64/bin/pdftotext.exe',['-layout',path.join(root,filename+'.pdf'),path.join(root,filename+'.txt')]);
  console.log(filename+' downloaded and all pages extracted');
 } )).then(results=>results.forEach(r=>{if(r.status==='rejected')console.log(r.reason.message)}));
}
