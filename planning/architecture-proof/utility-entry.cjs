// Generic Node-compatible child; executes actual compiled service entrypoints.
const path = require('node:path');
console.log(JSON.stringify({ kind: 'runtime', pid: process.pid, versions: process.versions, argv: process.argv }));
process.parentPort?.postMessage({ kind: 'runtime', pid: process.pid, versions: process.versions });
if (process.env.PROOF_ENFORCE_RUNTIME_ROOT) {
    const Module = require('node:module');
    const resolve = Module._resolveFilename;
    const root = path.resolve(process.env.PROOF_ENFORCE_RUNTIME_ROOT).toLowerCase() + path.sep;
    Module._resolveFilename = function (...args) {
        const resolved = resolve.apply(this, args);
        if (path.isAbsolute(resolved) && !resolved.toLowerCase().startsWith(root)) {
            throw new Error(`Proof rejected external runtime module: ${resolved}`);
        }
        return resolved;
    };
}
require(path.resolve(process.argv[2]));
