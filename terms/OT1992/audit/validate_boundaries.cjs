const fs = require('fs');
const path = require('path');
const base = process.argv[2] || '.';
const expected = JSON.parse(fs.readFileSync(path.join(base, 'OT_1992_LOAD_MANIFEST.json'), 'utf8')).matters;
const actual = [];
for (let chunk = 1; chunk <= 11; chunk++) {
  const text = fs.readFileSync(path.join(base, `OT_1992CHUNK${chunk}.md`), 'utf8');
  const modules = text.split(/^## /m).slice(1).map(block => ({
    caption: block.slice(0, block.indexOf('\n')).trim(),
    date: block.match(/\*\*Simulated Event Date:\*\*\s*(\d{4}-\d\d-\d\d)/)[1],
    chunk
  }));
  if (modules.length !== (chunk === 11 ? 3 : 12)) throw Error(`Wrong count in chunk ${chunk}`);
  actual.push(...modules);
}
if (actual.length !== expected.length || actual.length !== 123) throw Error('Inventory count mismatch');
for (let i = 0; i < actual.length; i++) {
  for (const key of ['caption', 'date', 'chunk']) {
    if (expected[i][key] !== actual[i][key]) throw Error(`Mismatch at position ${i + 1}: ${key}`);
  }
  if (i && actual[i - 1].date > actual[i].date) throw Error(`Backward date at position ${i + 1}`);
}
for (let chunk = 1; chunk <= 10; chunk++) {
  const last = actual.filter(x => x.chunk === chunk).at(-1);
  const next = actual.find(x => x.chunk === chunk + 1);
  console.log(`${chunk} -> ${chunk + 1}: ${last.caption} [${last.date}] / ${next.caption} [${next.date}]`);
}
console.log('PASS: 123 module/date/chunk memberships; all ten chronological boundaries; ten chunks of twelve plus three.');
