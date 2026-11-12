/* Static evidence collector: TypeScript AST, no application imports or dotenv reads. */
const fs = require('fs');
const path = require('path');
const cp = require('child_process');
const crypto = require('crypto');
const root = path.resolve(__dirname, '../..');
const ts = require(path.join(root, 'dozu-ui-service/node_modules/typescript'));
const posix = p => p.replaceAll('\\', '/');
const out = (name, data) => fs.writeFileSync(path.join(__dirname, name), JSON.stringify(data, null, 2) + '\n');
const repos = ['dozu-ui-service', 'dozu-api-service', 'dozu-embedding-service'];
const records = [], provenance = [];
for (const repo of repos) {
  const cwd = path.join(root, repo);
  const git = (...a) => cp.execFileSync('git', ['-C', cwd, ...a], {encoding:'utf8'}).trim();
  const trackedFiles = git('ls-files', '-z').split('\0').filter(Boolean);
  const files = [...trackedFiles];
  // Existing ignored migrations are audit evidence too; never assume Git clean means complete.
  if (repo === 'dozu-api-service') {
    function addMigrations(dir) {if(!fs.existsSync(dir))return; for(const ent of fs.readdirSync(dir,{withFileTypes:true})){const full=path.join(dir,ent.name); if(ent.isDirectory())addMigrations(full);else if(/\.(sql|json)$/.test(ent.name))files.push(posix(path.relative(cwd,full)));}}
    addMigrations(path.join(cwd,'drizzle'));
  }
  let origin='';try{origin=git('config','--get','remote.origin.url').replace(/(https?:\/\/)[^/@]+@/,'$1').split('?')[0];}catch{}
  provenance.push({repo, origin, commit:git('rev-parse','HEAD'), branch:git('branch','--show-current'), dirty:git('status','--porcelain=v1'), trackedFiles:trackedFiles.length, ignoredAuditPaths:files.filter(f=>!trackedFiles.includes(f)), trackedEnvPaths: trackedFiles.filter(f=>/(^|\/)\.env/.test(f)), licensePaths:trackedFiles.filter(f=>/(^|\/)(LICENSE|COPYING|NOTICE)/i.test(f))});
  for (const rel of files) {
    if (!/\.(tsx?|jsx?|mjs|cjs|py|sql|json|ya?ml|toml)$/.test(rel) && !/Dockerfile|Jenkinsfile|requirements\.txt/.test(rel)) continue;
    if (/^(node_modules|\.venv|dist|dist-stage|dist-lambda|logs|uploads|outputs)\//.test(rel) || /(^|\/)\.env/.test(rel) || /token-github/i.test(rel)) continue;
    const abs = path.join(cwd, rel);
    if (!fs.existsSync(abs)) continue;
    const bytes = fs.readFileSync(abs);
    const encoding = bytes[0]===255&&bytes[1]===254?'utf16le':'utf8';
    const source = repo+'/'+rel, text = encoding==='utf16le'?bytes.subarray(2).toString('utf16le'):bytes.toString('utf8');
    const r = {source, tracked:trackedFiles.includes(rel), encoding, lines:text.split('\n').length, sha256:crypto.createHash('sha256').update(bytes).digest('hex'), imports:[], declarations:[], calls:[], jsx:[], environment:[], storage:[], outboundHosts:[]};
    records.push(r);
    const lineAt = p => text.slice(0,p).split('\n').length;
    for (const match of text.matchAll(/(?:process\.env(?:\.([A-Z][A-Z0-9_]*)|\[['"]([A-Z][A-Z0-9_]*)['"]\])|(?:getEnv|os\.getenv|os\.environ\.get)\(\s*['"]([A-Z][A-Z0-9_]*)['"])/g)) r.environment.push({name:match[1]||match[2]||match[3],line:lineAt(match.index)});
    if (/Dockerfile|\.ya?ml$/.test(rel)) for(const match of text.matchAll(/\$\{([A-Z][A-Z0-9_]*)(?::[^}]*)?\}|^\s*ENV\s+([A-Z][A-Z0-9_]*)[=\s]|^\s*-?\s*([A-Z][A-Z0-9_]*)\s*[:=]/gm)) {if(match[3]&&/^\s*-D/.test(match[0]))continue;r.environment.push({name:match[1]||match[2]||match[3],line:lineAt(match.index)});}
    for (const match of text.matchAll(/https?:\/\/[^\s'"`<>\\)]+/g)) {
      try { const u = new URL(match[0].replace(/\$\{.*$/,'')); if (u.hostname) r.outboundHosts.push({host:u.hostname,line:lineAt(match.index)}); } catch {}
    }
    for (const match of text.matchAll(/\b(localStorage|sessionStorage|indexedDB|caches|navigator\.mediaDevices|URL\.createObjectURL|window\.open|document\.cookie)\b/g)) r.storage.push({kind:match[0],line:lineAt(match.index)});
    if (!/\.[cm]?[jt]sx?$/.test(rel)) continue;
    const sf = ts.createSourceFile(abs,text,ts.ScriptTarget.Latest,true,rel.endsWith('tsx')?ts.ScriptKind.TSX:undefined);
    const literal = n => n && (ts.isStringLiteralLike(n) || ts.isNoSubstitutionTemplateLiteral(n)) ? n.text : undefined;
    const compact = n => n ? n.getText(sf).replace(/\s+/g,' ').slice(0,350) : '';
    const names = n => { const list=[]; function walk(c){if(ts.isIdentifier(c))list.push(c.text); ts.forEachChild(c,walk);} walk(n); return [...new Set(list)]; };
    function walk(n) {
      const line = sf.getLineAndCharacterOfPosition(n.getStart(sf)).line+1;
      if (source.startsWith('dozu-ui-service/src/')) {
        if (ts.isPropertyAssignment(n)&&/^(href|url|to|path|redirectTo)$/.test(compact(n.name))) r.calls.push({kind:'navigation-config',callee:compact(n.name),line,target:literal(n.initializer)??compact(n.initializer)});
        if (/\/utils\/constants\/routes\.ts$|\/configs\/layout\//.test(source) && (ts.isStringLiteralLike(n)||ts.isTemplateExpression(n)) && compact(n).match(/^['"`]\//)) r.calls.push({kind:'navigation-config',callee:'route/layout constant',line,target:literal(n)??compact(n)});
      }
      if ((ts.isImportDeclaration(n)||ts.isExportDeclaration(n)) && n.moduleSpecifier) {
        r.imports.push({specifier:literal(n.moduleSpecifier),line,clause:compact(n.importClause||n.exportClause)});
      }
      if ((ts.isFunctionDeclaration(n)||ts.isClassDeclaration(n)||ts.isVariableDeclaration(n)||ts.isMethodDeclaration(n)) && n.name && ts.isIdentifier(n.name)) r.declarations.push({name:n.name.text,line,kind:ts.SyntaxKind[n.kind]});
      if (ts.isCallExpression(n)) {
        const callee = compact(n.expression);
        if (callee==='withAuth') r.calls.push({kind:'auth',callee,line,arguments:n.arguments.map(a=>ts.isArrowFunction(a)||ts.isFunctionExpression(a)?'<component>':compact(a))});
        if (/^(registerRoute|.*\.(get|post|put|patch|delete|use|all|route))$/.test(callee) && /\/routes\//.test(source)) {
          r.calls.push({kind:'route',callee,line,path:literal(n.arguments[0])??null,arguments:n.arguments.map(a=>({text:ts.isArrowFunction(a)||ts.isFunctionExpression(a)?'<inline handler>':compact(a),names:names(a)}))});
        }
        if (/^(use[A-Z]\w*|.*\.(push|replace|redirect)|redirect|fetch|.*Request|.*\.(emit|on|subscribe|publish)|.*\.(setItem|getItem|removeItem))$/.test(callee)) {
          r.calls.push({kind:'interaction',callee,line,target:literal(n.arguments[0])??(n.arguments[0]&&ts.isTemplateExpression(n.arguments[0])?compact(n.arguments[0]):null)});
        }
        if (callee==='pgTable'||callee==='pgEnum') r.calls.push({kind:'schema',callee,line,name:literal(n.arguments[0]),columns:n.arguments[1]&&ts.isObjectLiteralExpression(n.arguments[1])?n.arguments[1].properties.map(p=>({name:compact(p.name),definition:compact(p.initializer),line:sf.getLineAndCharacterOfPosition(p.getStart(sf)).line+1})):undefined,constraints:n.arguments[2]?compact(n.arguments[2]):undefined});
        if (callee==='import'||callee==='require') r.imports.push({specifier:literal(n.arguments[0]),line,clause:'dynamic'});
      }
      if (ts.isJsxOpeningElement(n)||ts.isJsxSelfClosingElement(n)) {
        const tag = compact(n.tagName);
        if (/^[A-Z]/.test(tag)) r.jsx.push({tag,line});
        for (const a of n.attributes.properties) {
          if (!ts.isJsxAttribute(a)) continue;
          const name=compact(a.name);
          if (name==='href'||/^on[A-Z]/.test(name)||/role|permission/i.test(name)) r.calls.push({kind:'jsx',callee:tag+'.'+name,line,target:literal(a.initializer)||(/role|permission/i.test(name)?compact(a.initializer):null),identifiers:a.initializer?names(a.initializer):[]});
        }
      }
      ts.forEachChild(n,walk);
    }
    walk(sf);
  }
}
const bySource = new Map(records.map(r=>[r.source,r]));
function resolve(from,spec) {
  if (!spec || (!spec.startsWith('.')&&!spec.startsWith('@/'))) return null;
  const base=spec.startsWith('@/')?from.split('/')[0]+'/src/'+spec.slice(2):posix(path.posix.normalize(path.posix.join(path.posix.dirname(from),spec)));
  return [base,...['.ts','.tsx','.js','.jsx','.json','/index.ts','/index.tsx'].map(s=>base+s)].find(p=>bySource.has(p))||null;
}
for(const r of records) for(const i of r.imports) i.resolved=resolve(r.source,i.specifier);
function closure(starts) {
  const seen=new Set(),queue=[...starts];
  while(queue.length){const s=queue.pop();if(seen.has(s))continue;seen.add(s);for(const i of bySource.get(s)?.imports||[])if(i.resolved)queue.push(i.resolved);}
  return [...seen].sort();
}
const ui=records.filter(r=>r.source.startsWith(repos[0]+'/src/'));
const layouts=ui.filter(r=>r.source.endsWith('/layout.tsx'));
const pages=ui.filter(r=>r.source.endsWith('/page.tsx')).map(r=>{
  const ancestors=layouts.filter(l=>r.source.startsWith(l.source.slice(0,-10))).map(l=>l.source);
  const reach=closure([r.source,...ancestors]);
  const own=closure([r.source]);
  return {source:r.source,route:r.source.replace('dozu-ui-service/src/app','').replace(/\/\([^/]+\)/g,'').replace(/\/page\.tsx$/,'')||'/',layouts:ancestors,imports:r.imports,rendered:r.jsx,ownReach:own,withLayoutReach:reach,interactionSources:own.filter(s=>(bySource.get(s)?.calls||[]).some(c=>c.kind!=='route')),interactionLookup:'Join interactionSources to source-inventory.json calls by source; no repeated full call payloads.',roleEvidence:own.filter(s=>/auth|permission|guard/i.test(s)),apiConsumers:own.filter(s=>/\/services\/|\/api\//.test(s)),status:'Source traced; runtime workflow and desktop parity unverified'};
});
const env=records.flatMap(r=>r.environment.map(e=>({source:r.source,...e})));
out('source-provenance.json',provenance);
out('source-inventory.json',records);
out('ui-workflows.json',{method:'AST imports and reexports, relative/@ alias closure, inherited layouts; dynamic expressions remain review candidates. Source reachability is not runtime execution or authorization proof.',pages,layouts:layouts.map(r=>r.source),navigation:ui.flatMap(r=>r.calls.filter(c=>c.kind==='navigation-config'||c.kind==='jsx'&&c.callee.endsWith('.href')||c.kind==='interaction'&&/push|replace|redirect/.test(c.callee)).map(c=>({source:r.source,...c}))),components:ui.filter(r=>r.source.endsWith('.tsx')&&!/\/(page|layout)\.tsx$/.test(r.source)).map(r=>({source:r.source,declarations:r.declarations,rendered:r.jsx,imports:r.imports,usedByPages:pages.filter(p=>p.withLayoutReach.includes(r.source)).map(p=>p.route)})),hooksAndProviders:ui.filter(r=>/\/hooks\/|\/contexts?\/|Provider|\/providers\//.test(r.source)||r.declarations.some(d=>/^use[A-Z]|Provider$/.test(d.name))).map(r=>({source:r.source,declarations:r.declarations,imports:r.imports,usedByPages:pages.filter(p=>p.withLayoutReach.includes(r.source)).map(p=>p.route)}))});
out('configuration-inventory.json',{environmentNames:[...new Set(env.map(e=>e.name))].sort(),consumers:env,hosts:records.flatMap(r=>r.outboundHosts.map(h=>({source:r.source,...h}))),note:'Names and public hostnames only. No dotenv content, token files, endpoint credentials, query strings or secret values read.'});
// Resolve Express mounts and nested routers from syntax; preserve unmounted declarations.
const routes=records.filter(r=>r.source.startsWith('dozu-api-service/src/routes/'));
const apiEntry='dozu-api-service/src/routes/api.routes.ts';
const reachable=new Set(closure([apiEntry]));
const mounts=[];
for(const r of routes) for(const c of r.calls.filter(c=>c.kind==='route'&&c.callee==='registerRoute')) mounts.push({source:r.source,line:c.line,prefix:c.path,active:reachable.has(r.source),options:c.arguments[2]?.text||'',router:c.arguments[1]?.text});
function join(a,b){return (a+'/'+b).replace(/\/+/g,'/').replace(/\/$/,'')||'/';}
const endpoints=[];
function mounted(source,prefix,chain,seen=new Set()) {
  if(seen.has(source))return;
  seen=new Set(seen).add(source);
  const r=bySource.get(source);if(!r)return;
  const calls=r.calls.filter(c=>c.kind==='route'&&/^(router|\w*Router|\w*Routes)\./.test(c.callee));
  const globalBefore=c=>calls.filter(g=>g.callee.endsWith('.use')&&g.path===null&&g.line<c.line).map(g=>({source,line:g.line,middleware:g.arguments.map(a=>a.text).join(', ')}));
  for(const c of calls) {
    const verb=c.callee.split('.').pop();
    if(c.path!==null&&verb==='use') {
      for(const arg of c.arguments.slice(1)) {
        const imp=r.imports.find(i=>i.clause.match(new RegExp('\\b'+arg.text+'\\b'))&&i.resolved&&i.resolved.includes('/routes/'));
        if(imp) mounted(imp.resolved,join(prefix,c.path),[...chain,...globalBefore(c),{source,line:c.line,middleware:c.arguments.slice(1,-1).map(a=>a.text).join(', ')}],seen);
      }
    } else if(c.path!==null&&['get','post','put','patch','delete','all'].includes(verb)) endpoints.push({method:verb.toUpperCase(),path:join(prefix,c.path),source,line:c.line,handlers:c.arguments.slice(1).map(a=>a.text),middlewareChain:[...chain,...globalBefore(c)],reachableFiles:closure([source]),evidence:'Static mounted declaration, not request-tested'});
  }
}
for(const m of mounts.filter(m=>m.active&&!/isEnabled:\s*false/.test(m.options)))mounted(m.source,join('/api',m.prefix),[]);
out('backend-endpoints.json',{mounts,endpoints,unreachableRouteFiles:routes.filter(r=>!reachable.has(r.source)).map(r=>r.source),method:'AST registerRoute + imported nested router.use mounts. Middleware chain lists file/global declarations conservatively, without proving order-specific authorization. Runtime confirmation remains required.'});
out('database-inventory.json',{models:records.filter(r=>r.source.includes('dozu-api-service/src/models/')).map(r=>({source:r.source,lines:r.lines,sha256:r.sha256,entities:r.calls.filter(c=>c.kind==='schema'),imports:r.imports})),migrations:records.filter(r=>/^dozu-api-service\/drizzle\/.+\.sql$/.test(r.source)).map(r=>({source:r.source,tracked:r.tracked,sha256:r.sha256,lines:r.lines})),journal:JSON.parse(fs.readFileSync(path.join(root,'dozu-api-service/drizzle/meta/_journal.json'),'utf8'))});
console.log(JSON.stringify({sources:records.length,pages:pages.length,layouts:layouts.length,endpoints:endpoints.length,mounts:mounts.length,envNames:[...new Set(env.map(e=>e.name))].length}));
