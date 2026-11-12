'use strict';
const fs = require('node:fs');
const path = require('node:path');
const { root, output, isInside, assertOutput, walkLinks } = require('./standalone-paths.cjs');

assertOutput();
if (!fs.existsSync(output)) throw new Error('Next standalone build output is missing.');
const changes = [];
walkLinks(output, (file) => {
    const resolved = fs.realpathSync(file);
    let target;
    if (isInside(output, resolved)) target = resolved;
    else if (isInside(root, resolved)) target = path.join(output, path.relative(root, resolved));
    else throw new Error(`Traced dependency link points outside the workspace: ${file}`);
    if (!fs.existsSync(target)) throw new Error(`Traced dependency target was not copied: ${file}`);
    changes.push({ file, target, directory: fs.statSync(target).isDirectory() });
});
// Validate the whole mapping before replacing any generated link.
for (const { file, target, directory } of changes) {
    fs.unlinkSync(file);
    fs.symlinkSync(path.relative(path.dirname(file), target), file, directory ? 'dir' : 'file');
}
walkLinks(output, (file) => {
    const raw = fs.readlinkSync(file);
    if (path.isAbsolute(raw) || !isInside(output, fs.realpathSync(file))) {
        throw new Error(`Standalone link is not portable and contained: ${file}`);
    }
});
console.log(`Normalized ${changes.length} standalone links to internal relative targets.`);
