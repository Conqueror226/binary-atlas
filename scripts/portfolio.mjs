import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
export const root = path.resolve(fileURLToPath(new URL('../', import.meta.url)));
export function readProjects() {
 const items = JSON.parse(fs.readFileSync(path.join(root, 'portfolio/projects.json'), 'utf8'));
 if (!Array.isArray(items)) throw Error('portfolio/projects.json must be an array.');
 const ids = new Set();
 for (const p of items) {
  for (const k of ['id','title','question','status','report']) if (typeof p[k] !== 'string' || !p[k].trim()) throw Error('Published projects require '+k);
  if (!/^[a-z0-9][a-z0-9-]*$/.test(p.id) || ids.has(p.id)) throw Error('Project IDs must be unique URL-safe slugs.');
  ids.add(p.id);
  if (!['in-progress','self-verified'].includes(p.status)) throw Error('Invalid published project status.');
  if (!/^projects\/[a-z0-9][a-z0-9-]*\.md$/.test(p.report)) throw Error('Report must be projects/<slug>.md');
  if (!fs.existsSync(path.join(root,'portfolio',p.report))) throw Error('Missing report: '+p.report);
  if (p.status === 'self-verified') {
   for (const k of ['provenance','tools','method','observations','limits','rerun']) if(typeof p[k] !== 'string' || !p[k].trim()) throw Error('Self-verification requires '+k);
   if (!Array.isArray(p.evidence) || !p.evidence.length) throw Error('Self-verification requires evidence files.');
  }
  if(p.evidence!==undefined && !Array.isArray(p.evidence)) throw Error('Evidence must be an array.');
  for (const file of p.evidence || []) {
   if (typeof file !== 'string' || !/^evidence\/[a-zA-Z0-9_./-]+$/.test(file) || file.split('/').includes('..')) throw Error('Invalid evidence path.');
   if (!fs.existsSync(path.join(root,'portfolio',file))) throw Error('Missing evidence: '+file);
  }
 }
 return items;
}
