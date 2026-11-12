"""Run each existing API test file separately so one eager Redis crash cannot hide others."""
import concurrent.futures
import json
from pathlib import Path
import runpy

n = runpy.run_path(str(Path(__file__).with_name('run-baselines.py')), run_name='audit_runner')
api = n['prepare']('dozu-api-service')
jobs = [('jest-'+p.stem.replace('.test',''), ['node', str(api/'node_modules/jest/bin/jest.js'), '--runInBand', '--forceExit', '--runTestsByPath', str(p), '--cacheDirectory', str(n['RUN']/'jest-cache')], api, 120, None) for p in (api/'src').rglob('*.test.ts')]
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool:
    results = list(pool.map(lambda job:n['run'](*job), jobs))
(n['LOG']/'jest-suites.json').write_text(json.dumps(results,indent=2), encoding='utf-8')
print(json.dumps(results,indent=2))
