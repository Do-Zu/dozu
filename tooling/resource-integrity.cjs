'use strict';
// Build-host inventory and offline verifier. Supervisor/signature integration is #28/#24.
const fs = require('node:fs');
const path = require('node:path');
const crypto = require('node:crypto');
const hash = bytes => crypto.createHash('sha256').update(bytes).digest('hex');
const denied = /^(?:\.git|\.env(?:\..*)?|\.npmrc|\.pypirc|\.netrc|\.venv|venv|__pycache__|\.cache|\.downloads|\.runs|uploads|logs|backups|pgdata|dump\.rdb|appendonlydir|token-githubs\.txt)$/i;
function relativeName(name) {
  if (typeof name !== 'string' || !name || name.includes('\\') || name.includes(':') || name.includes('\0') ||
      name.startsWith('/') || name.split('/').some(p => !p || p === '.' || p === '..' || /[. ]$/.test(p))) {
    throw new Error('Invalid relative resource path: ' + name);
  }
  if (name.split('/').some(p => denied.test(p)) || /\.(?:pem|key|pfx|p12)$/i.test(name)) {
    throw new Error('Forbidden release resource: ' + name);
  }
  return name;
}
function inside(root, candidate) {
  const rel = path.relative(root, candidate);
  return rel === '' || (!rel.startsWith('..' + path.sep) && rel !== '..' && !path.isAbsolute(rel));
}
function inventory(root) {
  root = fs.realpathSync(root);
  const entries = [];
  const seen = new Set();
  function walk(dir, prefix) {
    for (const item of fs.readdirSync(dir, { withFileTypes: true }).sort((a,b) => a.name.localeCompare(b.name))) {
      const name = relativeName(prefix + item.name);
      const key = name.toLowerCase();
      if (seen.has(key)) throw new Error('Case-colliding resource: ' + name);
      seen.add(key);
      const full = path.join(dir, item.name);
      const stat = fs.lstatSync(full);
      if (stat.isSymbolicLink()) {
        const target = fs.readlinkSync(full);
        // Preserve internal macOS framework links. No absolute, external, dangling or cyclic links.
        if (path.isAbsolute(target) || /^[A-Za-z]:|^\\\\/.test(target) ||
            !inside(root, path.resolve(dir, target)) || !inside(root, fs.realpathSync(full))) {
          throw new Error('Escaping resource link: ' + name);
        }
        entries.push({ path: name, type: 'symlink', target: target.replaceAll('\\', '/') });
      } else if (stat.isDirectory()) {
        entries.push({ path: name, type: 'directory' });
        walk(full, name + '/');
      } else if (stat.isFile()) {
        const row = { path: name, type: 'file', bytes: stat.size, sha256: hash(fs.readFileSync(full)) };
        if (process.platform !== 'win32') row.executable = !!(stat.mode & 0o111);
        entries.push(row);
      } else throw new Error('Unsupported resource type: ' + name);
    }
  }
  walk(root, '');
  return entries.sort((a,b) => a.path.localeCompare(b.path));
}
function create(root, target, resourceSet, approvedRoots) {
  if (!['win32-x64', 'darwin-x64', 'darwin-arm64', 'linux-x64'].includes(target)) throw new Error('Unsupported target');
  if (typeof resourceSet !== 'string' || !resourceSet.trim()) throw new Error('Resource set required');
  if (!Array.isArray(approvedRoots) || !approvedRoots.length) throw new Error('Explicit allowlist required');
  approvedRoots.forEach(relativeName);
  const entries = inventory(root);
  if (!entries.some(e => e.type === 'file')) throw new Error('Empty resource set');
  for (const e of entries) {
    if (!approvedRoots.some(p => e.path === p || e.path.startsWith(p + '/') || (e.type === 'directory' && p.startsWith(e.path + '/')))) {
      throw new Error('Resource outside reviewed allowlist: ' + e.path);
    }
  }
  for (const p of approvedRoots) if (!entries.some(e => e.path === p)) throw new Error('Missing allowlisted resource: ' + p);
  return { schemaVersion: 1, target, resourceSet, builtOn: process.platform, approvedRoots, entries };
}
function verify(root, manifestBytes, trustedDigest, expectedTarget, expectedResourceSet) {
  if (!/^[a-f0-9]{64}$/.test(trustedDigest || '') || hash(manifestBytes) !== trustedDigest) throw new Error('Untrusted resource manifest');
  const m = JSON.parse(manifestBytes);
  if (m.schemaVersion !== 1 || m.target !== expectedTarget || m.resourceSet !== expectedResourceSet || !Array.isArray(m.entries)) {
    throw new Error('Resource compatibility mismatch');
  }
  if ((m.builtOn === 'win32') !== (process.platform === 'win32')) throw new Error('Native file-mode inventory required');
  const actual = create(root, m.target, m.resourceSet, m.approvedRoots);
  if (JSON.stringify(actual.entries) !== JSON.stringify(m.entries)) throw new Error('Resource integrity mismatch');
  return { verified: true, target: m.target, resourceSet: m.resourceSet, files: m.entries.filter(e => e.type === 'file').length };
}
module.exports = { create, verify, inventory, hash };
if (require.main === module) {
  try {
    const [command, root, manifestPath, arg, target, resourceSet] = process.argv.slice(2);
    if (command === 'create') {
      // arg is a reviewed spec: {target,resourceSet,approvedRoots}. Output must live outside immutable root.
      if (inside(fs.realpathSync(root), path.resolve(manifestPath))) throw new Error('Manifest must be outside resource root');
      const spec = JSON.parse(fs.readFileSync(arg));
      const bytes = Buffer.from(JSON.stringify(create(root, spec.target, spec.resourceSet, spec.approvedRoots), null, 2) + '\n');
      fs.writeFileSync(manifestPath, bytes, { flag: 'wx' });
      console.log(JSON.stringify({ manifestSha256: hash(bytes) }));
    } else if (command === 'verify') {
      console.log(JSON.stringify(verify(root, fs.readFileSync(manifestPath), arg, target, resourceSet)));
    } else throw new Error('Usage: resource-integrity.cjs create ROOT MANIFEST SPEC | verify ROOT MANIFEST TRUSTED_SHA256 TARGET RESOURCE_SET');
  } catch (error) { console.error(error.message); process.exitCode = 1; }
}
