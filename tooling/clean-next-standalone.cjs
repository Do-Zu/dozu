'use strict';
const fs = require('node:fs');
const { output, assertOutput, walkLinks } = require('./standalone-paths.cjs');

assertOutput();
if (fs.existsSync(output)) {
    let detached = 0;
    // Next 14 cleanup follows directory links. Unlink every link first without
    // ever traversing its target, then remove only this fixed owned output.
    walkLinks(output, (file) => { fs.unlinkSync(file); detached += 1; });
    fs.rmSync(output, { recursive: true, force: true });
    console.log(`Removed previous standalone output after detaching ${detached} links.`);
}
