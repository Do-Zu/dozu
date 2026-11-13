'use strict';
const fs=require('node:fs'),path=require('node:path'),{execFileSync}=require('node:child_process');
const {createRequire}=require('node:module');
const root=path.resolve(__dirname,'../..'),web=path.join(root,'apps/web');
const {ESLint}=createRequire(path.join(web,'package.json'))('eslint');
const files=['src/app/[locale]/auth/forgotPassword/page.tsx',
    'src/app/[locale]/profile/components/AccountSettings.tsx','src/components/class/InviteStudentsModal.tsx','src/i18n/messages.ts'];
function signatures(result) {
    const count=new Map();
    for(const m of result.messages) {
        const key=JSON.stringify({rule:m.ruleId,severity:m.severity,message:m.message});
        count.set(key,(count.get(key)||0)+1);
    }
    return count;
}
async function main() {
    const eslint=new ESLint({cwd:web}),report=[];
    for(const file of files) {
        const repositoryPath=`apps/web/${file}`,filePath=path.join(web,file);
        const before=execFileSync('git',['show',`HEAD:${repositoryPath}`],{cwd:root,encoding:'utf8',windowsHide:true});
        const oldResult=(await eslint.lintText(before,{filePath}))[0];
        const current=(await eslint.lintText(fs.readFileSync(filePath,'utf8'),{filePath}))[0];
        const a=signatures(oldResult),b=signatures(current);
        report.push({file:repositoryPath,errors:current.errorCount,warnings:current.warningCount,
            added:[...b].flatMap(([key,count])=>Array(Math.max(0,count-(a.get(key)||0))).fill(JSON.parse(key))),
            removed:[...a].flatMap(([key,count])=>Array(Math.max(0,count-(b.get(key)||0))).fill(JSON.parse(key)))});
    }
    fs.writeFileSync(path.join(__dirname,'web-lint-comparison.json'),JSON.stringify(report,null,2)+'\n');
    console.log(JSON.stringify(report,null,2));
    if(report.some(x=>x.added.length)) process.exitCode=1;
}
main().catch(e=>{console.error(e);process.exitCode=1;});
