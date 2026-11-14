import assert from 'node:assert/strict';
import fs from 'node:fs';
import path from 'node:path';
import { root, readProjects } from './portfolio.mjs';
const projects = readProjects();
const app=fs.readFileSync(path.join(root,'site/app.js'),'utf8');
assert(app.includes('publishedPortfolio'));
const html=fs.readFileSync(path.join(root,'site/index.html'),'utf8');
assert(html.indexOf('published-projects.js') < html.indexOf('app.js'));
assert(!html.includes('chatgpt.site'));
console.log('Portfolio manifest passed: '+projects.length+' entries. Structure checked; truth of findings is not automated.');


const workflow=fs.readFileSync(path.join(root,'.github/workflows/pages.yml'),'utf8');
const uses=workflow.split(String.fromCharCode(10)).map(s=>s.trim()).filter(s=>s.startsWith('- uses:')||s.startsWith('uses:')).map(s=>s.split('uses:')[1].trim());
assert.equal(uses.length,5);
for(const action of uses) {
 const [name,version,...extra]=action.split('@');
 assert(name.startsWith('actions/') && /^v[0-9]+$/.test(version||'') && !extra.length,'Invalid action reference: '+action);
}
console.log('Deployment action references validated.');
