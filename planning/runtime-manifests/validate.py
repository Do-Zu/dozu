"""Offline candidate consistency/input verification; --release deliberately fails open gates."""
import argparse
import hashlib
import json
from pathlib import Path
import re
import subprocess

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
OUT = ROOT/'resources/manifests'


def sha(p):
    with p.open('rb') as stream: return hashlib.file_digest(stream, 'sha256').hexdigest()


def read(p): return json.loads(p.read_text(encoding='utf-8-sig'))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--release', action='store_true')
    args = parser.parse_args()
    scope = read(OUT/'scope.json')
    assert scope['requiredTargets'] == ['win32-x64']
    catalog = read(OUT/'artifact-candidates.json')['artifacts']
    assert len({a['id'] for a in catalog}) == len(catalog)
    artifacts = [a for a in catalog if a['target'] in scope['requiredTargets'] or a['target'] in {'win-x64', 'source-only'}]
    assert len(artifacts) == 7
    for a in artifacts:
        assert re.fullmatch('[a-f0-9]{64}', a['sha256']) and a['source'].startswith('https://')
        if a['archiveBytesVerified']:
            p = (ROOT/'planning/embedding-runtime/.downloads' if a['id'] == 'python-win32-x64' else HERE/'.downloads')/a['filename']
            assert sha(p) == a['sha256'] and p.stat().st_size == a['bytes'], a['id']
    targets = [read(OUT/'targets'/f'{target}.json') for target in scope['requiredTargets']]
    assert {t['target'] for t in targets} == set(scope['requiredTargets'])
    valid_ids = {a['id'] for a in artifacts}
    blockers = {}
    references = 0
    for t in targets:
        assert all(v is None or v in valid_ids for v in t['artifactRefs'].values())
        assert not t['releaseEligible'] and t['cleanMachineResults'] == [] and t['gates']
        assert t['embedding']['dimension'] == 384 and not t['embedding']['onnxRequired']
        for field in ['model', 'windowsHashLock', 'windowsWheelInventory', 'foreignAvailabilityOnly']:
            item = t['embedding'][field]
            if item:
                assert sha(ROOT/item['path']) == item['sha256'], item['path']
                references += 1
        blockers[t['target']] = t['gates']
    wheels = read(ROOT/'services/embedding/packaging/requirements-torch-windows-x64.json')['packages']
    assert len(wheels) == 45
    for w in wheels:
        p = ROOT/'planning/embedding-runtime/.downloads/wheels-torch'/w['wheel']
        assert sha(p) == w['sha256'] and p.stat().st_size == w['bytes'], w['wheel']
    model = read(ROOT/'services/embedding/packaging/model-manifest.json')
    model_files = [f for f in model['files'] if 'torch' in f['backends']]
    for f in model_files:
        p = ROOT/'planning/embedding-runtime/.downloads/model'/f['path']
        assert sha(p) == f['sha256'] and p.stat().st_size == f['bytes'], f['path']
    license_data = read(OUT/'license-evidence.json')
    for item in license_data['files']:
        assert sha(ROOT/item['path']) == item['sha256']
    # Existing embedding file manifest is a reference, not a new full release payload.
    component_checks = read(HERE/'component-inventory-checks.json')
    for item in component_checks['inventories']:
        r = item.get('manifest') or item['existingInventory']
        assert sha(ROOT/r['path']) == r['sha256']
    native = read(OUT/'native-windows-x64.json')
    assert not native['cleanMachineVerified']
    foreign = [{'component': g['component'], 'path': f['path'], 'architecture': f['architecture']}
               for g in native['components'] for f in g['files'] if f['architecture'] != 'x64']
    # These are upstream wheel launcher templates, not a mixed-ABI runtime claim.
    assert all(f['component'] == 'embedding-torch' and '/setuptools/' in f['path'] and f['path'].endswith('.exe') for f in foreign)
    cpp = read(OUT/'microsoft-crt-candidate.json')
    assert all(f['signatureStatus'] == 'Valid' and re.fullmatch('[a-f0-9]{64}',f['sha256']) for f in cpp['files'])
    result = {'candidateConsistencyPassed': True, 'releaseEligible': False,
        'sourceBaseline': subprocess.check_output(['git','rev-parse','HEAD'], cwd=ROOT, text=True).strip(),
        'requiredTargets': scope['requiredTargets'], 'ignoredTargets': scope['ignoredTargets'],
        'verifiedArchives': sum(a['archiveBytesVerified'] for a in artifacts), 'upstreamArtifactPins': len(artifacts),
        'windowsWheelArchivesVerified': len(wheels), 'baselineModelFilesVerified': len(model_files),
        'targetReferenceHashesVerified': references, 'nativePEFilesInspected': sum(len(g['files']) for g in native['components']),
        'microsoftSignedCrtFilesInventoried': len(cpp['files']), 'cleanNativeTargetsPassed': 0,
        'foreignArchitecturePayloadsRequiringReview': foreign,
        'gates': blockers, 'note': 'Candidate consistency is not issue completion, native compatibility or security/redistribution approval'}
    (HERE/'validation.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result))
    if args.release:
        print('RELEASE REFUSED: candidate manifests have unresolved required gates')
        raise SystemExit(1)


if __name__ == '__main__': main()
