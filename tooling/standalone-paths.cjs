'use strict';
const fs = require('node:fs');
const path = require('node:path');
const root = path.resolve(__dirname, '..');
const web = path.join(root, 'apps/web');
const output = path.join(web, '.next/standalone');

function isInside(parent, child) {
    const relative = path.relative(parent, child);
    return relative !== '..' && !relative.startsWith(`..${path.sep}`) && !path.isAbsolute(relative);
}

function assertOutput() {
    if (!isInside(root, output) || path.dirname(output) !== path.join(web, '.next')) {
        throw new Error('Standalone output must stay inside the fixed workspace build directory.');
    }
    for (const directory of [root, path.join(root, 'apps'), web, path.join(web, '.next'), output]) {
        if (fs.lstatSync(directory, { throwIfNoEntry: false })?.isSymbolicLink()) {
            throw new Error(`Refusing a linked build-output ancestor: ${directory}`);
        }
    }
}

function walkLinks(directory, onLink) {
    for (const entry of fs.readdirSync(directory, { withFileTypes: true })) {
        const file = path.join(directory, entry.name);
        if (entry.isSymbolicLink()) onLink(file);
        else if (entry.isDirectory()) walkLinks(file, onLink);
    }
}
module.exports = { root, web, output, isInside, assertOutput, walkLinks };
