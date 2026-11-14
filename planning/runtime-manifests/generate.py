"""Generate candidate target records and receipts from locally verified inputs."""
import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import tarfile
import zipfile

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
OUT = ROOT / 'resources/manifests'


def sha(path):
    with path.open('rb') as stream:
        return hashlib.file_digest(stream, 'sha256').hexdigest()


def save(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2)+'\n', encoding='utf-8')


def ref(path):
    return {'path': path.relative_to(ROOT).as_posix(), 'sha256': sha(path)}


def main():
    artifacts = json.loads((OUT/'artifact-candidates.json').read_text())['artifacts']
    by_id = {a['id']: a for a in artifacts}
    scope = json.loads((OUT/'scope.json').read_text())
    model = ROOT/'services/embedding/packaging/model-manifest.json'
    wheel_lock = ROOT/'services/embedding/packaging/requirements-torch-windows-x64.lock'
    wheel_inventory = ROOT/'services/embedding/packaging/requirements-torch-windows-x64.json'
    targets = [
        ('win32-x64', ['Windows 10 22H2 x64 legacy', 'Windows 11 x64 primary'], ['NSIS exe'], '22'),
    ]
    assert [t[0] for t in targets] == scope['requiredTargets']
    common_gates = ['SECURITY-48', 'POSTGRES-BINARY', 'CONVERSION-32', 'APPLICATION-PRODUCTION-CLOSURE', 'SIGNED-RESOURCE-ROOT', 'CLEAN-NATIVE-TARGET']
    for target, baselines, installers, native_owner in targets:
        node_id = 'node-'+target.replace('win32', 'win')
        windows = target == 'win32-x64'
        gate_ids = common_gates + (['WINDOWS-REDIS', 'WINDOWS-CRT-LOADER'] if windows else ['PYTHON-NATIVE-BUILD', 'PYTHON-NATIVE-LOCK', 'REDIS-NATIVE-BUILD'])
        if target == 'darwin-x64': gate_ids += ['TORCH-MAC-INTEL']
        data = {'schemaVersion': 1, 'target': target, 'status': 'candidate-incomplete', 'releaseEligible': False,
                'requiredBaselines': baselines, 'installerFormats': installers, 'cleanMachineResults': [],
                'artifactRefs': {'electron': by_id['electron-'+target]['id'], 'node': node_id,
                    'postgresqlSource': 'postgresql-source', 'postgresqlShippingBinary': 'postgresql-win32-x64' if windows else None,
                    'python': 'python-win32-x64' if windows else 'python-source',
                    'pythonShippingBinary': 'python-win32-x64' if windows else None,
                    'redisSource': 'redis-source', 'redisShippingBinary': None},
                'nodeStrategy': {'mode': 'standalone-node-children', 'nodeModulesABI': '127', 'nodeAPI': '10',
                    'electronNodeMustNotLoadAppNativeModules': True, 'productionNativeModulesVerified': False},
                'embedding': {'backend': 'torch-cpu', 'model': ref(model), 'dimension': 384, 'normalized': True, 'maxTokens': 128,
                    'windowsHashLock': ref(wheel_lock) if windows else None,
                    'windowsWheelInventory': ref(wheel_inventory) if windows else None,
                    'foreignAvailabilityOnly': ref(OUT/'embedding-wheel-availability.json') if not windows else None,
                    'onnxRequired': False},
                'installedResourceManifest': None, 'licenseClosureApproved': False,
                'upgradeCompatibility': {'resourceSchema': 1, 'postgresqlMajor': 17, 'appDataSchemaRange': None,
                    'redisPersistenceFormatVerified': False, 'embeddingSpace': 'MiniLM-L12-v2@86741b4e3f5cb7765a600d3a3d55a0f6a6cb443d/384/mean128/unit/torch',
                    'crossBackendVectorReuseApproved': False},
                'gates': gate_ids + (['FOREIGN-LAUNCHER-REVIEW'] if windows else []), 'nativeReleaseOwner': '#'+native_owner}
        save(OUT/'targets'/f'{target}.json', data)
    # Store modest upstream primary license texts. Large bundled notices stay in
    # archives and candidate file inventories; release assembly must preserve them.
    license_rows = []
    names = {'electron-win32-x64': ['LICENSE'], 'node-win-x64': ['node-v22.22.0-win-x64/LICENSE'],
             'postgresql-source': ['postgresql-17.12/COPYRIGHT'], 'redis-source': ['redis-7.2.17/COPYING'],
             'python-source': ['Python-3.13.7/LICENSE']}
    for artifact_id, members in names.items():
        row = by_id[artifact_id]
        archive = HERE/'.downloads'/row['filename']
        assert sha(archive) == row['sha256']
        for member in members:
            if archive.suffix == '.zip':
                with zipfile.ZipFile(archive) as z: content = z.read(member)
            else:
                with tarfile.open(archive) as t: content = t.extractfile(member).read()
            output = OUT/'licenses'/f'{artifact_id}.txt'
            output.parent.mkdir(exist_ok=True)
            output.write_bytes(content)
            license_rows.append({'artifactId': artifact_id, 'archiveMember': member, **ref(output),
                                 'sourceArchiveSha256': row['sha256'], 'allBundledDependencyLicensesReviewed': False})
    save(OUT/'license-evidence.json', {'status': 'primary-texts-only-not-complete-license-closure', 'files': license_rows,
         'embeddingNotices': ref(ROOT/'services/embedding/packaging/requirements-torch-windows-x64.json')})
    # A real installed-file inventory for candidate Node/Electron components only.
    # No npm/pip/corepack, developer caches or user data enter this stage.
    stage = HERE/'.runs/candidate-components'
    stage.mkdir(parents=True, exist_ok=True)
    node_source = HERE/'.runs/node/node-v22.22.0-win-x64'
    node_stage = stage/'node'
    node_stage.mkdir(exist_ok=True)
    for name in ['node.exe', 'LICENSE']:
        shutil.copyfile(node_source/name, node_stage/name)
    inventories = []
    for component, component_root, roots in [('node', node_stage, ['node.exe', 'LICENSE']),
            ('electron', HERE/'.runs/electron', sorted(p.name for p in (HERE/'.runs/electron').iterdir()))]:
        spec = HERE/'.runs'/f'{component}-spec.json'
        save(spec, {'target': 'win32-x64', 'resourceSet': 'inspection-only-2026-11-14', 'approvedRoots': roots})
        manifest = OUT/'installed-candidates'/f'{component}-win32-x64.json'
        manifest.parent.mkdir(exist_ok=True)
        # Deterministic regeneration, no overwrite operation in production CLI.
        command = "const fs=require('fs');const t=require(process.argv[1]);const s=JSON.parse(fs.readFileSync(process.argv[2]));process.stdout.write(JSON.stringify(t.create(process.argv[3],s.target,s.resourceSet,s.approvedRoots),null,2)+'\\n');"
        p = subprocess.run(['node', '-e', command, str(ROOT/'tooling/resource-integrity.cjs'), str(spec), str(component_root)], capture_output=True, check=True)
        manifest.write_bytes(p.stdout)
        # CLI verification binds the exact expected target and resource set.
        checked = subprocess.run(['node', str(ROOT/'tooling/resource-integrity.cjs'), 'verify', str(component_root), str(manifest), sha(manifest), 'win32-x64', 'inspection-only-2026-11-14'], capture_output=True, text=True, check=True)
        inventories.append({'component': component, 'manifest': ref(manifest), 'verification': json.loads(checked.stdout),
                            'releasePayload': False, 'note': 'Official Electron archive includes default demo app; replace it with Dozu during final assembly' if component == 'electron' else 'Standalone node.exe + its full upstream LICENSE only; npm/corepack omitted'})
    existing_package = ROOT/'planning/embedding-runtime/.runs/Verified torch tiếng Việt/package-manifest.json'
    # Existing assembler calls this package-manifest.json; refuse silently missing evidence.
    assert existing_package.exists(), 'Existing embedding package inventory missing'
    inventories.append({'component': 'embedding-torch', 'existingInventory': ref(existing_package), 'releasePayload': False,
                        'evidence': 'planning/embedding-runtime/measurements.json', 'cleanMachineVerified': False})
    save(HERE/'component-inventory-checks.json', {'status': 'candidate-components-only', 'inventories': inventories})
    print(json.dumps({'targets': len(targets), 'primaryLicenseTexts': len(license_rows), 'componentInventories': len(inventories)}))


if __name__ == '__main__':
    main()
