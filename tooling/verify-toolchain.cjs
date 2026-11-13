'use strict';
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const policy = require('./toolchain-policy.json');
const root = path.resolve(__dirname, '..');
assert.equal(process.versions.node, policy.node, 'Use the pinned Node build baseline');
for (const file of ['.nvmrc', '.node-version', 'apps/api/.nvmrc']) {
    assert.equal(fs.readFileSync(path.join(root, file), 'utf8').trim(), policy.node, file);
}
assert.equal(require('../package.json').packageManager, `pnpm@${policy.pnpm}`);
const agent = process.env.npm_config_user_agent;
if (agent) assert.ok(agent.startsWith(`pnpm/${policy.pnpm} `), 'Run with the pinned pnpm');
assert.equal(require('../node_modules/turbo/package.json').version, policy.turbo);
for (const app of ['api', 'web']) {
    assert.equal(require(`../apps/${app}/node_modules/typescript/package.json`).version, policy.typescript);
}
console.log(JSON.stringify({node: process.versions.node, modules: process.versions.modules,
    napi: process.versions.napi, platform: process.platform, arch: process.arch,
    pnpm: policy.pnpm, turbo: policy.turbo, typescript: policy.typescript}));
