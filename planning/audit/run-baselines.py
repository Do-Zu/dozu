"""Run source baselines from disposable tracked-file copies without dotenv secrets."""
import concurrent.futures
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import time

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / 'planning/audit'
RUN = OUT / '.runs'
LOG = OUT / 'baselines'
RUN.mkdir(parents=True, exist_ok=True)
LOG.mkdir(exist_ok=True)

def tracked(repo):
    return subprocess.check_output(['git', '-C', str(repo), 'ls-files', '-z']).decode().split('\0')

def prepare(name):
    src, dst = ROOT / name, RUN / name
    dst.mkdir(exist_ok=True)
    for rel in tracked(src):
        if not rel or Path(rel).parts[0] in {'.git', 'node_modules', '.venv', 'dist', 'dist-stage', 'dist-lambda', 'logs', 'outputs', 'uploads'}:
            continue
        if Path(rel).name.startswith('.env') or Path(rel).name in {'.npmrc', '.pypirc', '.netrc'} or 'token-github' in rel.lower():
            continue
        if not (src / rel).is_file():
            continue
        target = dst / rel
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(src / rel, target)
    if (src / 'node_modules').exists() and not (dst / 'node_modules').exists():
        subprocess.run(['powershell', '-NoProfile', '-Command', f"New-Item -ItemType Junction -Path '{dst / 'node_modules'}' -Target '{src / 'node_modules'}' | Out-Null"], check=True)
    return dst

safe_names = {'PATH', 'SYSTEMROOT', 'WINDIR', 'COMSPEC', 'PATHEXT', 'TEMP', 'TMP', 'PROCESSOR_ARCHITECTURE', 'NUMBER_OF_PROCESSORS', 'APPDATA', 'LOCALAPPDATA', 'USERPROFILE', 'PROGRAMFILES', 'PROGRAMFILES(X86)', 'PROGRAMDATA', 'SYSTEMDRIVE'}
ENV = {k: v for k, v in os.environ.items() if k.upper() in safe_names}
ENV.update({'CI': '1', 'NEXT_TELEMETRY_DISABLED': '1', 'NEXT_PUBLIC_API_URL': 'http://127.0.0.1:3333', 'NEXT_PUBLIC_WEBSOCKET_URL': 'http://127.0.0.1:3333', 'NODE_ENV': 'test', 'HF_HUB_OFFLINE': '1', 'TRANSFORMERS_OFFLINE': '1', 'HF_HOME': str(RUN / 'empty-hf-cache'), 'PYTHONDONTWRITEBYTECODE': '1', 'DATABASE_URL': 'postgresql://audit:audit@127.0.0.1:1/audit', 'REDIS_HOST': '127.0.0.1', 'REDIS_PORT': '1'})

def run(label, args, cwd, timeout=300, extra=None):
    start = time.monotonic()
    env = ENV | (extra or {})
    try:
        result = subprocess.run(args, cwd=cwd, env=env, capture_output=True, timeout=timeout)
        code, output = result.returncode, result.stdout + result.stderr
    except subprocess.TimeoutExpired as e:
        code, output = 'timeout', (e.stdout or b'') + (e.stderr or b'')
    (LOG / (label + '.log')).write_bytes(output)
    return {'check': label, 'command': args, 'cwd': str(Path(cwd).relative_to(ROOT)), 'exitCode': code, 'seconds': round(time.monotonic() - start, 2), 'log': f'baselines/{label}.log'}

if __name__ == '__main__':
    ui = prepare('dozu-ui-service')
    api = prepare('dozu-api-service')
    emb = prepare('dozu-embedding-service')
    node = shutil.which('node')
    jobs = [
        ('ui-lint', [node, str(ui / 'node_modules/next/dist/bin/next'), 'lint'], ui, 180, None),
        ('ui-build', [node, str(ui / 'node_modules/next/dist/bin/next'), 'build'], ui, 480, {'NODE_ENV': 'production'}),
        ('api-typecheck', [node, str(api / 'node_modules/typescript/bin/tsc'), '--noEmit', '--incremental', 'false'], api, 180, None),
        ('api-lint', [node, str(api / 'node_modules/eslint/bin/eslint.js'), '.'], api, 180, None),
        ('api-jest', [node, str(api / 'node_modules/jest/bin/jest.js'), '--runInBand', '--forceExit', '--cacheDirectory', str(RUN / 'jest-cache')], api, 240, None),
        ('embedding-startup', [str(ROOT / 'dozu-embedding-service/.venv/Scripts/python.exe'), '-c', 'from src.app.main import app; from src.app.core.model_manager import model_manager; model_manager.load_model(); print(model_manager.get_health_info())'], emb, 180, None),
    ]
    # An optional caller-selected local model permits real HTTP verification with no downloads.
    model_path = os.environ.get('AUDIT_MODEL_PATH')
    if model_path:
        jobs.append(('embedding-contract', [str(ROOT / 'dozu-embedding-service/.venv/Scripts/python.exe'), str(OUT / 'embedding-contract.py')], emb, 220, {'MODEL_NAME':model_path, 'OMP_NUM_THREADS':'2', 'MKL_NUM_THREADS':'2', 'TOKENIZERS_PARALLELISM':'false'}))
    if len(sys.argv) > 1:
        jobs = [job for job in jobs if job[0] in sys.argv[1:]]
    results = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
        for result in pool.map(lambda job: run(*job), jobs):
            results.append(result)
            print(json.dumps(result), flush=True)
    prior = json.loads((LOG / 'results.json').read_text(encoding='utf-8')) if (LOG / 'results.json').exists() else []
    results = [r for r in prior if r['check'] not in {n['check'] for n in results}] + results
    (LOG / 'results.json').write_text(json.dumps(results, indent=2), encoding='utf-8')
