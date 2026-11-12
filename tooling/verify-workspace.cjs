'use strict';

const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const { createRequire } = require('node:module');
const root = path.resolve(__dirname, '..');
const read = (relative) => JSON.parse(fs.readFileSync(path.join(root, relative), 'utf8'));
const manifest = read('package.json');
assert.equal(manifest.private, true);
assert.equal(manifest.packageManager, 'pnpm@10.28.2');
const packages = ['apps/web', 'apps/api'];
for (const relative of packages) {
    const app = read(`${relative}/package.json`);
    assert.equal(app.private, true);
    for (const script of Object.values(app.scripts)) assert.ok(!script.startsWith('set NODE_ENV='));
    assert.ok(!fs.existsSync(path.join(root, relative, 'package-lock.json')));
    for (const name of Object.keys(app.dependencies || {})) {
        assert.ok(!['dozu-ui-service', 'api-services'].includes(name), 'No invented internal dependency');
    }
}
const web = path.join(root, 'apps/web');
const local = createRequire(path.join(web, 'package.json'));
const reactPath = fs.realpathSync(local.resolve('react'));
const consumers = ['react-dom', 'next', '@tiptap/react', '@react-pdf/renderer', 'react-pdf'];
const resolutions = {};
for (const consumer of consumers) {
    const consumerRequire = createRequire(local.resolve(consumer));
    const resolved = fs.realpathSync(consumerRequire.resolve('react'));
    assert.equal(resolved, reactPath, `${consumer} must resolve the same React instance`);
    resolutions[consumer] = path.relative(root, resolved).replaceAll('\\', '/');
}
assert.equal(local('react/package.json').version, '18.3.1');
assert.equal(local('react-dom/package.json').version, '18.3.1');
const config = local('./next.config.js');
assert.equal(config.output, 'standalone');
assert.equal(config.experimental.outputFileTracingRoot, root);
const turbo = read('turbo.json');
assert.equal(turbo.remoteCache.enabled, false);
assert.deepEqual(turbo.tasks.package.dependsOn, ['build']);
for (const [name, task] of Object.entries(turbo.tasks)) {
    if (/^(dev|start|.*:watch|db:)/.test(name)) assert.equal(task.cache, false, name);
    if (task.persistent) assert.equal(task.cache, false, name);
}
assert.ok(fs.existsSync(path.join(root, 'services/embedding/requirements.txt')));
assert.ok(!fs.existsSync(path.join(root, 'services/embedding/package.json')));
console.log(JSON.stringify({ verified: true, workspacePackages: packages,
    reactVersion: '18.3.1', sameReactInstanceFor: consumers,
    resolutions, nextTracingRoot: root, pythonPipelineIndependent: true }, null, 2));
