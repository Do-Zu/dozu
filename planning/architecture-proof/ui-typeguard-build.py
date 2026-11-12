"""Measured F01 workaround in disposable copy only; preserves type validation."""
import difflib
from pathlib import Path
import shutil
import subprocess
import sys
from build import OUT, ROOT, ENV, prepare, run

ui = prepare('dozu-ui-service')
rel = 'src/app/[locale]/topics/[topicId]/(topic)/media/core/youtube/YoutubePlayerAdapter.ts'
path = ui/rel
before = path.read_text(encoding='utf-8')
after = before.replace('        return this.player.getCurrentTime() || 0;', '''        // react-youtube forwards the raw ready-event IFrame player, but its
        // published target type describes the asynchronous youtube-player facade.
        const currentTime: unknown = this.player.getCurrentTime();
        if (typeof currentTime !== 'number') {
            throw new TypeError('YoutubePlayerAdapter requires the ready IFrame player');
        }
        return currentTime || 0;''')
if before == after:
    raise RuntimeError('Measured F01 source site changed; review before patching')
path.write_text(after,encoding='utf-8')
(OUT/'ui-f01-typeguard.patch').write_text(''.join(difflib.unified_diff(before.splitlines(True),after.splitlines(True),fromfile='a/'+rel,tofile='b/'+rel)),encoding='utf-8')
# Check the adapter's actual synchronous contract without pretending a real
# YouTube provider flow has occurred.
check = '''const fs = require('node:fs');
const assert = require('node:assert/strict');
const ts = require(process.argv[2]);
const source = fs.readFileSync(process.argv[3], 'utf8');
const output = ts.transpileModule(source, {compilerOptions:{module:ts.ModuleKind.CommonJS}}).outputText;
const loaded = {exports:{}};
new Function('module', 'exports', output)(loaded, loaded.exports);
const Adapter = loaded.exports.YoutubePlayerAdapter;
let seek, played = 0;
const raw = new Adapter({getCurrentTime:()=>42.25,seekTo:(s)=>{seek=s},playVideo:()=>{played++}});
assert.equal(raw.getCurrentTime(),42.25);
raw.seekTo(12); assert.equal(seek,12); assert.equal(played,1);
assert.equal(new Adapter({getCurrentTime:()=>0}).getCurrentTime(),0);
assert.throws(()=>new Adapter({getCurrentTime:()=>Promise.resolve(42)}).getCurrentTime(),TypeError);
console.log('Ready-player number/zero/seek contracts pass; async facade rejected. No provider runtime claim.');
'''
check_path=ui/'proof-adapter-contract.cjs';check_path.write_text(check,encoding='utf-8')
node=shutil.which('node')
if run('ui-f01-adapter-contract',[node,str(check_path),str(ui/'node_modules/typescript'),str(path)],ui):
    sys.exit(1)
sys.exit(run('ui-build-typeguard',[node,str(ui/'node_modules/next/dist/bin/next'),'build'],ui))
