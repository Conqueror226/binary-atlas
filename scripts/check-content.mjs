import fs from 'node:fs';
import vm from 'node:vm';
import assert from 'node:assert/strict';
const root=new URL('../',import.meta.url);
const src=fs.readFileSync(new URL('site/data.js',root),'utf8');
const data=vm.runInNewContext(src+';({STAGES,LABS,RESOURCES,CONCEPTS,PROJECTS,SAFETY,SOURCE_BRANCH,SOURCE_MEMORY,SOURCE_PARSER})');
const ids=xs=>new Set(xs.map(x=>x.id));
for(const k of ['STAGES','LABS','RESOURCES','CONCEPTS','PROJECTS'])assert.equal(ids(data[k]).size,data[k].length,`Duplicate ID in ${k}`);
const stages=ids(data.STAGES),labs=ids(data.LABS),resources=ids(data.RESOURCES);
assert.equal(data.STAGES.length,6);assert.equal(data.LABS.length,12);
for(const s of data.STAGES)for(const l of s.labs)assert(labs.has(l));
for(const l of data.LABS){assert(stages.has(l.stage));assert(resources.has(l.resource));assert(l.steps.length>=3);assert(l.evidence.length>=3);assert(l.objective);}
for(const r of data.RESOURCES){assert(stages.has(r.stage));assert(new URL(r.url).protocol==='https:');assert.equal(r.verified,'2026-11-11');}
for(const c of data.CONCEPTS)assert(resources.has(c.resource));
for(const p of data.PROJECTS)for(const l of p.labs)assert(labs.has(l));
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
