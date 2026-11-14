import fs from 'node:fs';
import vm from 'node:vm';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
const root=path.resolve(fileURLToPath(new URL('../',import.meta.url)));
const {LABS,RESOURCES}=vm.runInNewContext(fs.readFileSync(path.join(root,'site/data.js'),'utf8')+';({LABS,RESOURCES})');
const fence=String.fromCharCode(96).repeat(3);
for(const l of LABS){
 const dir=path.join(root,'labs',l.id);fs.mkdirSync(dir,{recursive:true});
 const resource=RESOURCES.find(r=>r.id===l.resource);
 const text='# '+l.title+'\n\nStatus: starter exercise; not completed portfolio work.\n\n'+l.objective+'\n\nScope: owned or explicitly authorized programs in an isolated lab. Commands describe the stated lab environment, not every host platform.\n\n## Investigation steps\n\n'+l.steps.map((s,i)=>(i+1)+'. '+s).join('\n\n')+(l.commands?'\n\n## Commands\n\n'+fence+'sh\n'+l.commands+'\n'+fence:'')+(l.files?'\n\n## Lab scripts\n\n'+l.files.map(f=>'- ['+f+']('+f+')').join('\n')+'\n\nRead each script before running it. Its header states assumptions and limits.':'')+'\n\n## Evidence and validation\n\n'+l.evidence.map(e=>'- '+e).join('\n')+'\n\n## Learning output\n\n'+l.outcome+'\n\n## Resource\n\n['+resource.name+']('+resource.url+')\n\nUse the website lab page for the worked solution and concept links. Preserve your own actual results separately.\n';
 fs.writeFileSync(path.join(dir,'README.md'),text);
 if(l.source&&l.filename)fs.writeFileSync(path.join(dir,path.basename(l.filename)),l.source);
}
console.log('Exported '+LABS.length+' starter lab guides.');
