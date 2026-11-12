'use strict';

const fs = require('node:fs');
const path = require('node:path');
const { assertOutput } = require('./standalone-paths.cjs');
assertOutput();
const web = path.resolve(__dirname, '../apps/web');
const source = path.join(web, '.next/standalone');
const target = path.join(web, '.package');
const entry = path.join(source, 'apps/web/server.js');
if (!fs.existsSync(entry)) {
    throw new Error('Build apps/web first; monorepo standalone apps/web/server.js is missing.');
}
if (path.dirname(target) !== web || path.basename(target) !== '.package' ||
    path.relative(rootDirectory(), target).startsWith('..')) {
    throw new Error('Packaging output must stay inside this workspace.');
}
if (fs.lstatSync(target, { throwIfNoEntry: false })?.isSymbolicLink()) {
    throw new Error('Refusing to replace a symbolic-link packaging output.');
}
function rootDirectory() { return path.resolve(__dirname, '..'); }
// The resolved deletion target is the fixed app-owned output inside the workspace.
fs.rmSync(target, { recursive: true, force: true });
fs.cpSync(source, target, { recursive: true, verbatimSymlinks: true });
for (const [from, to] of [['public', 'public'], ['.next/static', '.next/static']]) {
    const input = path.join(web, from);
    if (fs.existsSync(input)) fs.cpSync(input, path.join(target, 'apps/web', to), { recursive: true });
}
function checkLinks(directory) {
    for (const entry of fs.readdirSync(directory, { withFileTypes: true })) {
        const file = path.join(directory, entry.name);
        if (entry.isSymbolicLink()) {
            if (path.isAbsolute(fs.readlinkSync(file))) {
                throw new Error(`Standalone package link must be relative: ${file}`);
            }
            const resolved = fs.realpathSync(file);
            const relative = path.relative(target, resolved);
            if (relative.startsWith('..') || path.isAbsolute(relative)) {
                throw new Error(`Standalone dependency link escapes package: ${file}`);
            }
        } else if (entry.isDirectory()) checkLinks(file);
    }
}
checkLinks(target);
console.log('Created apps/web/.package; launch with node apps/web/server.js from that directory.');
