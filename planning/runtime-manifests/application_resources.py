"""Inventory actual local frontend assets and current production-input provenance."""
import hashlib
import json
from pathlib import Path
import subprocess

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT/'resources/manifests'


def sha(p):
    with p.open('rb') as stream: return hashlib.file_digest(stream,'sha256').hexdigest()


def main():
    refs = [{'path': name, 'sha256': sha(ROOT/name)} for name in [
        'pnpm-lock.yaml','package.json','apps/web/package.json','apps/api/package.json',
        'services/embedding/packaging/model-manifest.json','services/embedding/packaging/requirements-torch-windows-x64.lock']]
    rows = []
    for label, base in [('web-public', ROOT/'apps/web/public'), ('built-web-static', ROOT/'apps/web/.package/apps/web/.next/static')]:
        assert base.is_dir(), str(base)
        for p in sorted(base.rglob('*')):
            if p.is_file(): rows.append({'component':label,'path':p.relative_to(base).as_posix(),'bytes':p.stat().st_size,'sha256':sha(p)})
    public_worker = ROOT/'apps/web/public/pdf.worker.min.mjs'
    module_worker = ROOT/'apps/web/node_modules/pdfjs-dist/build/pdf.worker.min.mjs'
    result = {'status':'local-source-and-build-assets-only-not-final-target-payload',
        'sourceBaseline':subprocess.check_output(['git','rev-parse','HEAD'],cwd=ROOT,text=True).strip(),
        'inputs':refs,'assets':rows,
        'pdfWorker':{'declaredVersion':'4.8.69','localPublicHash':sha(public_worker),'installedModuleHash':sha(module_worker),
                     'matchesInstalledModule':sha(public_worker)==sha(module_worker),
                     'unresolvedConsumers':['apps/web/src/app/[locale]/mindmap/components/FileSheet.tsx',
                       'apps/web/src/app/[locale]/topics/[topicId]/(topic)/components/material/pdf/PDFLearningMaterial.tsx',
                       'apps/web/src/app/[locale]/topics/[topicId]/(topic)/components/material/pdf/CustomPDFViewer.tsx'],
                     'gate':'#32 must remove retained local workflow reliance on CDN workers and align all PDF.js versions'},
        'conversion':{'puppeteerVersion':'24.32.0','headlessShellRevision':'143.0.7499.40','nativeBrowserArchivesVerified':False,
                      'officeSource':'apps/api/src/services/convert/strategies/libreoffice-converter.strategy.ts',
                      'urlSource':'apps/api/src/services/convert/strategies/url-converter.strategy.ts',
                      'nativeOfficeConverterSelected':False,'gate':'CONVERSION-32'},
        'remaining':'Target production dependency/native SBOM and notice closure, complete routes/features, local converter/browser/font/media resources; no release approval'}
    (OUT/'application-resources.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'assets':len(rows),'pdfWorkerMatches':result['pdfWorker']['matchesInstalledModule']}))


if __name__=='__main__': main()
