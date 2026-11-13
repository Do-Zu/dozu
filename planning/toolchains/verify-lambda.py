"""Exercise packaging in a disposable checkout with spaces and shell metacharacters."""
import json
import os
from pathlib import Path
import shutil
import subprocess
import tempfile
import zipfile

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
(HERE / '.runs').mkdir(exist_ok=True)
fixture = Path(tempfile.mkdtemp(prefix="lambda [literal] $value ' spaces-", dir=HERE / '.runs'))
scripts = fixture / 'scripts'
dist = fixture / 'dist-lambda'
scripts.mkdir()
dist.mkdir()
(dist / 'index.js').write_text('exports.handler = async () => 42;\n', encoding='utf-8')
(dist / 'asset with spaces.txt').write_text('fixture', encoding='utf-8')
shutil.copyfile(ROOT / 'apps/api/scripts/package-lambda.js', scripts / 'package-lambda.js')
env = {k: v for k, v in os.environ.items() if k.upper() in
       {'PATH', 'SYSTEMROOT', 'WINDIR', 'COMSPEC', 'PATHEXT', 'TEMP', 'TMP'}}
result = subprocess.run([shutil.which('node'), str(scripts / 'package-lambda.js')],
                        cwd=HERE, env=env, capture_output=True, timeout=30)
(HERE / 'lambda-package.log').write_bytes(result.stdout + result.stderr)
assert result.returncode == 0, 'See lambda-package.log'
with zipfile.ZipFile(dist / 'function.zip') as archive:
    assert set(archive.namelist()) == {'index.js', 'asset with spaces.txt'}, archive.namelist()
    assert archive.read('asset with spaces.txt') == b'fixture'
report = {'platform': os.name, 'exitCode': result.returncode,
          'spacesAndShellMetacharacters': True, 'fixtureZipContentsVerified': True,
          'deploymentExecuted': False, 'nativeMacOSLinux': 'unpassed on this Windows host'}
(HERE / 'lambda-package.json').write_text(json.dumps(report, indent=2) + '\n', encoding='utf-8')
print(json.dumps(report))
