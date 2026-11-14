import fs from 'node:fs';
import vm from 'node:vm';
import assert from 'node:assert/strict';
const root=new URL('../',import.meta.url);
const src=fs.readFileSync(new URL('site/data.js',root),'utf8');
const data=vm.runInNewContext(src+';({STAGES,LABS,RESOURCES,CONCEPTS,PROJECTS,SAFETY,SOURCE_BRANCH,SOURCE_MEMORY,SOURCE_PARSER,ENGD})');
const ids=xs=>new Set(xs.map(x=>x.id));
for(const k of ['STAGES','LABS','RESOURCES','CONCEPTS','PROJECTS'])assert.equal(ids(data[k]).size,data[k].length,`Duplicate ID in ${k}`);
const stages=ids(data.STAGES),labs=ids(data.LABS),resources=ids(data.RESOURCES);
assert.equal(data.STAGES.length,8);assert.equal(data.LABS.length,20);
for(const l of data.LABS)assert(data.STAGES.find(s=>s.id===l.stage).labs.includes(l.id),`Lab ${l.id} missing from its stage`);
for(const s of data.STAGES)for(const l of s.labs)assert(labs.has(l));
for(const l of data.LABS){assert(stages.has(l.stage));assert(resources.has(l.resource));assert(l.steps.length>=3);assert(l.evidence.length>=3);assert(l.objective);}
for(const r of data.RESOURCES){assert(stages.has(r.stage));assert(new URL(r.url).protocol==='https:');assert(r.verified===''||/^2026-\d{2}-\d{2}$/.test(r.verified),`Resource ${r.id}: verified must be a date or empty (not yet checked)`);}
for(const c of data.CONCEPTS)assert(resources.has(c.resource));
for(const p of data.PROJECTS)for(const l of p.labs)assert(labs.has(l));
for(const l of data.LABS)for(const f of l.files||[])assert(fs.existsSync(new URL('labs/'+l.id+'/'+f,root)),`Missing lab script labs/${l.id}/${f}`);
const projects=ids(data.PROJECTS);
assert(data.ENGD.facts.every(f=>f.length===2&&f[1]),'Every EngD fact needs a source');
for(const c of data.ENGD.competencies)for(const l of c.labs)assert(labs.has(l));
for(const d of data.ENGD.directions){assert(projects.has(d.project));for(const k of ['problem','scenario','approach','validation','bridge','risk'])assert(d[k]);}
const html=fs.readFileSync(new URL('site/index.html',root),'utf8');
assert(!html.includes('codex-preview'));
for(const f of ['styles.css','app.js','data.js'])assert(fs.existsSync(new URL('site/'+f,root)));
console.log(`Content integrity passed: ${data.STAGES.length} stages, ${data.LABS.length} labs, ${data.RESOURCES.length} official resources, ${data.CONCEPTS.length} concepts, ${data.PROJECTS.length} project ideas.`);
if(process.argv.includes('--extract-samples')){
 const dir='/tmp/binary-atlas-sample-qa';fs.mkdirSync(dir,{recursive:true});
 fs.writeFileSync(dir+'/branch.c',data.SOURCE_BRANCH);fs.writeFileSync(dir+'/memory.c',data.SOURCE_MEMORY);fs.writeFileSync(dir+'/parser_lab.c',data.SOURCE_PARSER);
 fs.writeFileSync(dir+'/parser_fixed.c',data.SOURCE_PARSER.replace('size_t length = buf[0];','size_t length = buf[0];\n    if (length > size - 1) return -1;'));
 console.log('Teaching samples extracted for compiler checks.');
}
