'use strict';
// Component checks only: no DB, real dotenv, provider credentials or model loads.
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const { spawnSync } = require('node:child_process');
const { createRequire } = require('node:module');
const crypto = require('node:crypto');
const root = path.resolve(__dirname, '../..');
const api = path.join(root, 'apps/api');
fs.mkdirSync(path.join(__dirname, '.runs'), { recursive: true });
const run = fs.mkdtempSync(path.join(__dirname, '.runs', 'paths with spaces-'));
const data = path.join(run, 'user data');
const unrelated = path.join(run, 'unrelated cwd');
fs.mkdirSync(data); fs.mkdirSync(unrelated);
const env = Object.fromEntries(Object.entries(process.env).filter(([key]) =>
    ['PATH', 'SYSTEMROOT', 'WINDIR', 'COMSPEC', 'PATHEXT', 'TEMP', 'TMP'].includes(key.toUpperCase())));
Object.assign(env, { NODE_ENV: 'production', DOZU_DATA_DIR: data, HOST: '127.0.0.1', PORT: '0',
    ALLOWED_ORIGINS: 'http://localhost', DATABASE_URL: 'postgresql://fixture:fixture@127.0.0.1:1/fixture',
    REDIS_HOST: '127.0.0.1', REDIS_PORT: '1', REDIS_PUBSUB_HOST: '127.0.0.1', REDIS_PUBSUB_PORT: '1',
    AWS_EC2_METADATA_DISABLED: 'true' });
const reads = [path.join(api, 'dist'), path.join(root, 'node_modules'), path.join(api, 'node_modules'),
    path.join(api, 'package.json'), path.join(root, 'package.json'), data];
const flags = ['--permission', ...reads.map(p => `--allow-fs-read=${p}`), `--allow-fs-write=${data}`];
const report = { node: process.versions.node, modules: process.versions.modules, napi: process.versions.napi,
    platform: process.platform, arch: process.arch, checks: [] };
function probe(name, code, extraEnv = {}, extraFlags = []) {
    const result = spawnSync(process.execPath, [...flags, ...extraFlags, '-e', code], {
        cwd: unrelated, env: { ...env, ...extraEnv }, encoding: 'utf8', timeout: 15000, windowsHide: true,
    });
    fs.writeFileSync(path.join(__dirname, `${name}.log`), result.stdout + result.stderr);
    assert.equal(result.status, 0, `${name}: ${result.stdout}${result.stderr}`);
    report.checks.push({ name, passed: true });
}
const register = JSON.stringify(path.join(api, 'dist/register.js'));
probe('all-compiled-aliases', `const fs=require('node:fs'),p=require('node:path'),{createRequire}=require('node:module');
require(${register}); let checked=0;
function walk(dir) { for(const entry of fs.readdirSync(dir,{withFileTypes:true})) {
 const file=p.join(dir,entry.name);
 if(entry.isDirectory()) walk(file);
 else if(file.endsWith('.js')) for(const match of fs.readFileSync(file,'utf8').matchAll(/require\\(["'](@\\/[^"']+)["']\\)/g)) {
  createRequire(file).resolve(match[1]); checked++;
 }
}}
walk(${JSON.stringify(path.join(api, 'dist'))});
if(checked<100) throw Error('Compiled alias inventory unexpectedly small');
console.log(JSON.stringify({resolvedAliases:checked}));`);
probe('compiled-alias-and-writes', `
const assert = require('node:assert/strict'), fs = require('node:fs'), p = require('node:path');
require(${register});
const {runtimePaths: r} = require('@/config/runtimePaths.config');
assert.equal(r.uploads, p.join(process.env.DOZU_DATA_DIR, 'uploads'));
assert.equal(require('@/config/generate.config').generateConfig.uploadDir, r.uploads);
const c = require('@/services/convert/config/convert.config').CONVERT_CONFIG;
assert.equal(c.UPLOAD_DIR, r.convertUploads); assert.equal(c.OUTPUT_DIR, r.convertOutputs);
require('@/middleware/upload.middleware'); require('@/middleware/storage/convert-upload.middleware');
for(const dir of [r.uploads, c.UPLOAD_DIR, c.OUTPUT_DIR]) {
 fs.writeFileSync(p.join(dir, 'fixture.txt'), 'portable');
 assert.equal(fs.readFileSync(p.join(dir, 'fixture.txt'), 'utf8'), 'portable');
}
assert.throws(() => fs.writeFileSync(p.join(process.cwd(), 'forbidden.txt'), 'x'), {code:'ERR_ACCESS_DENIED'});
const logger = require('@/utils/logger').default;
logger.on('finish', () => {
 const deadline = Date.now()+5000;
 const timer = setInterval(() => {
  const file=p.join(r.logs,'error.log');
  if(fs.existsSync(file) && fs.readFileSync(file,'utf8').includes('portability fixture')) {
   clearInterval(timer); console.log('alias/write/log paths passed');
  } else if(Date.now()>deadline) { clearInterval(timer); throw Error('Logger did not flush to writable data directory'); }
 },25);
});
logger.error('portability fixture'); logger.end();
`);
probe('relative-data-root-rejected', `const a=require('node:assert/strict'); require(${register});
a.throws(()=>require('@/config/runtimePaths.config'), /must be an absolute/);`, {DOZU_DATA_DIR: 'relative'});
probe('path-overrides', `const a=require('node:assert/strict'),p=require('node:path'); require(${register});
const r=require('@/config/runtimePaths.config').runtimePaths;
a.equal(r.uploads,p.join(process.env.DOZU_DATA_DIR,'custom uploads'));
a.equal(r.logs,process.env.LOG_DIR);
a.equal(r.convertUploads,p.join(process.env.DOZU_DATA_DIR,'custom convert'));
`, {UPLOAD_DIR:'custom uploads', LOG_DIR:path.join(data, 'custom logs'), UPLOAD_CONVERT_FILE_DIR:'custom convert'});
probe('website-default-paths', `const a=require('node:assert/strict'),p=require('node:path'); require(${register});
const r=require('@/config/runtimePaths.config').runtimePaths;
a.equal(r.uploads,p.join(process.cwd(),'uploads'));`, {DOZU_DATA_DIR:''});
// Evaluate an exact config copy at a relocated filename; no real dotenv or DB access.
const configFile = path.join(api, 'drizzle.config.ts');
const relocatedConfig = path.join(run, 'relocated api', 'drizzle.config.ts');
fs.mkdirSync(path.dirname(relocatedConfig));
fs.copyFileSync(configFile, relocatedConfig);
probe('migration-config-paths', `const fs=require('node:fs'),p=require('node:path'),a=require('node:assert/strict');
const {createRequire,Module}=require('node:module'); const filename=${JSON.stringify(relocatedConfig)};
const original=${JSON.stringify(configFile)},r=createRequire(original),ts=r('typescript'),m=new Module(filename);
m.filename=filename; m.paths=Module._nodeModulePaths(p.dirname(original));
m._compile(ts.transpileModule(fs.readFileSync(filename,'utf8'),{compilerOptions:{module:ts.ModuleKind.CommonJS,esModuleInterop:true}}).outputText,filename);
a.equal(m.exports.default.out,p.join(p.dirname(filename),'drizzle'));
a.equal(m.exports.default.schema,p.join(p.dirname(filename),'src/models'));
console.log('migration config resolved; no migration executed');`, {}, [`--allow-fs-read=${run}`]);
// A scrubbed real entrypoint attempt is expected to reveal inherited optional-provider blockers.
const startup = spawnSync(process.execPath, [...flags, path.join(api, 'dist/index.js')], {
    cwd: unrelated, env, encoding: 'utf8', timeout: 10000, windowsHide: true,
});
fs.writeFileSync(path.join(__dirname, 'production-startup.log'), startup.stdout + startup.stderr);
report.productionStartup = { exitCode: startup.status, signal: startup.signal,
    passed: startup.status === 0, timedOut: startup.error?.code === 'ETIMEDOUT',
    note: 'Real entrypoint under scrubbed environment; not backend-ready evidence' };
const nextRequire = createRequire(fs.realpathSync(path.join(root, 'apps/web/node_modules/next/package.json')));
report.native = [];
if (process.platform === 'win32' && process.arch === 'x64') {
    const bindingPath = nextRequire.resolve('@next/swc-win32-x64-msvc');
    const binding = nextRequire('@next/swc-win32-x64-msvc');
    report.native.push({package:'@next/swc-win32-x64-msvc', loaded:true,
        target:binding.getTargetTriple(), sha256:crypto.createHash('sha256').update(fs.readFileSync(bindingPath)).digest('hex')});
}
const pdfRequire = createRequire(fs.realpathSync(path.join(root, 'apps/web/node_modules/pdfjs-dist/package.json')));
try { pdfRequire('canvas'); report.native.push({package:'canvas',loaded:true}); }
catch (error) { report.native.push({package:'canvas',loaded:false,code:error.code,
    note:'Lifecycle suppressed; native/browser delivery remains unpassed'}); }
fs.writeFileSync(path.join(__dirname, 'runtime-checks.json'), JSON.stringify(report, null, 2) + '\n');
console.log(JSON.stringify(report, null, 2));
