"""Static PE normal/delay-import inventory; does not certify loader resolution."""
import hashlib
import json
import mmap
import os
from pathlib import Path
import struct
import subprocess
import zipfile

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
OUT = ROOT / "resources/manifests"


def sha(path):
    with path.open("rb") as stream:
        return hashlib.file_digest(stream, "sha256").hexdigest()


def pe(path):
    with path.open("rb") as stream, mmap.mmap(stream.fileno(), 0, access=mmap.ACCESS_READ) as data:
        def u16(o): return struct.unpack_from('<H', data, o)[0]
        def u32(o): return struct.unpack_from('<I', data, o)[0]
        def u64(o): return struct.unpack_from('<Q', data, o)[0]
        assert data[:2] == b'MZ'
        start = u32(0x3c)
        assert data[start:start+4] == b'PE\0\0'
        machine, count, opt_size = u16(start+4), u16(start+6), u16(start+20)
        opt = start+24
        plus = u16(opt) == 0x20b
        directories = opt + (112 if plus else 96)
        image_base = u64(opt+24) if plus else u32(opt+28)
        sections = []
        for i in range(count):
            s = opt + opt_size + i*40
            sections.append((u32(s+12), max(u32(s+8), u32(s+16)), u32(s+20)))
        def offset(rva):
            for base, size, raw in sections:
                if base <= rva < base + size:
                    return raw + rva - base
            if 0 <= rva < u32(opt+60): return rva
            raise ValueError(f'Invalid RVA {rva} in {path.name}')
        def string(rva):
            pos = offset(rva)
            end = data.find(b'\0', pos, pos+1024)
            assert end >= pos
            return data[pos:end].decode('ascii')
        imports = []
        rva = u32(directories+8)
        if rva:
            pos = offset(rva)
            while any(data[pos:pos+20]):
                imports.append(string(u32(pos+12)))
                pos += 20
        delay = []
        rva = u32(directories+13*8)
        if rva:
            pos = offset(rva)
            while any(data[pos:pos+32]):
                name = u32(pos+4)
                if not u32(pos) & 1: name -= image_base
                delay.append(string(name))
                pos += 32
        return {"machine": hex(machine), "architecture": {0x8664: "x64", 0xaa64: "arm64", 0x14c: "x86"}.get(machine, "unknown"),
                "imports": sorted(set(imports), key=str.lower), "delayImports": sorted(set(delay), key=str.lower)}


def main():
    run = HERE / ".runs"
    run.mkdir(exist_ok=True)
    artifacts = json.loads((OUT / 'artifact-candidates.json').read_text())["artifacts"]
    for component, name in [('electron', 'electron-v45.2.3-win32-x64.zip'), ('node', 'node-v22.22.0-win-x64.zip'), ('postgresql', 'postgresql-17.12-1-windows-x64-binaries.zip')]:
        archive = HERE / '.downloads' / name
        row = next(a for a in artifacts if a['filename'] == name)
        assert sha(archive) == row['sha256']
        target = run / component
        if not target.exists():
            with zipfile.ZipFile(archive) as z:
                # Official hash verified first; still refuse unexpected archive path escapes.
                for member in z.namelist():
                    p = Path(member)
                    assert not p.is_absolute() and '..' not in p.parts and ':' not in member and '\\' not in member
                if component == 'postgresql':
                    for member in z.namelist():
                        if member.startswith(('pgsql/bin/', 'pgsql/lib/', 'pgsql/share/', 'pgsql/doc/')):
                            z.extract(member, target)
                else: z.extractall(target)
    embedding = ROOT / 'planning/embedding-runtime/.runs/Verified torch tiếng Việt'
    # Selected production/build native modules only; foreign optional binaries are excluded.
    swc = ROOT / 'node_modules/.pnpm/@next+swc-win32-x64-msvc@14.2.33/node_modules/@next/swc-win32-x64-msvc'
    roots = {'electron': run/'electron', 'node': run/'node', 'postgresql': run/'postgresql/pgsql', 'embedding-torch': embedding, 'next-swc-build': swc}
    groups = []
    for name, base in roots.items():
        assert base.is_dir(), f'Missing input {base}'
        files = []
        for p in sorted(base.rglob('*')):
            if p.suffix.lower() in {'.exe', '.dll', '.pyd', '.node'}:
                files.append({"path": p.relative_to(base).as_posix(), "bytes": p.stat().st_size, "sha256": sha(p), **pe(p)})
        provided = {Path(f['path']).name.lower() for f in files}
        required = {n.lower() for f in files for n in f['imports']+f['delayImports']}
        external = sorted(required - provided)
        cpp = sorted(n for n in required if n.startswith(('msvcp', 'vcruntime', 'concrt', 'vcomp')))
        groups.append({"component": name, "files": files, "externalImportNames": external,
                       "foreignArchitecturePayloads": [f['path'] for f in files if f['architecture'] != 'x64'],
                       "cppImportCandidates": [{"name": n, "providedPaths": [f['path'] for f in files if Path(f['path']).name.lower() == n]} for n in cpp],
                       "microsoftCppExternalImports": [n for n in external if n.startswith(('msvcp', 'vcruntime', 'concrt', 'vcomp'))],
                       "note": "Basename presence is not Windows loader search-path proof. In particular sklearn/.libs/msvcp140.dll does not establish resolution for Torch. Existing measurements observed host msvcp140.dll. Normal/delay imports only; dynamic LoadLibrary and CPU feature gates require native runs"})
    result = {"status": "static-developer-host-only", "os": "Windows 11 Pro 10.0.26300 x64 (existing host.json)",
              "cleanMachineVerified": False, "components": groups}
    (OUT/'native-windows-x64.json').write_text(json.dumps(result, indent=2)+'\n', encoding='utf-8')
    node = next((run/'node').rglob('node.exe'))
    env = {k:v for k,v in os.environ.items() if k.upper() in {'SYSTEMROOT','WINDIR','TEMP','TMP'}}
    env['PATH'] = str(node.parent) + os.pathsep + str(Path(os.environ['SYSTEMROOT'])/'System32')
    probes = []
    for name, args in [('node-versions', ['-p', 'JSON.stringify({versions:process.versions,arch:process.arch,platform:process.platform})']),
                       ('node-swc-load', ['-e', 'const swc=require(process.argv[1]); console.log(JSON.stringify({loaded:!!swc.transformSync,modules:process.versions.modules,napi:process.versions.napi}));', str(swc)])]:
        p = subprocess.run([str(node), *args], env=env, capture_output=True, text=True, timeout=30)
        probes.append({"probe": name, "exitCode": p.returncode, "stdout": p.stdout.strip(), "stderr": p.stderr.strip()})
    pg_bin = run/'postgresql/pgsql/bin'
    env['PATH'] = str(pg_bin) + os.pathsep + str(Path(os.environ['SYSTEMROOT'])/'System32')
    for name in ['postgres', 'initdb', 'pg_ctl', 'psql', 'pg_dump', 'pg_restore', 'pg_isready', 'pg_upgrade', 'pg_basebackup']:
        p = subprocess.run([str(pg_bin/(name+'.exe')), '--version'], env=env, capture_output=True, text=True, timeout=30)
        probes.append({'probe': 'postgresql-'+name+'-version', 'exitCode': p.returncode, 'stdout': p.stdout.strip(), 'stderr': p.stderr.strip()})
    (HERE/'windows-probes.json').write_text(json.dumps({"cleanMachineVerified": False,
        "scope": "Downloaded standalone Node, scrubbed environment, existing Windows developer host; SWC is build-only evidence", "probes": probes}, indent=2)+'\n', encoding='utf-8')
    print(json.dumps({"nativeFiles": sum(len(g['files']) for g in groups), "groups": [{"name":g['component'],"files":len(g['files']),"externalCpp":g['microsoftCppExternalImports']} for g in groups],"probes":[p['exitCode'] for p in probes]}))


if __name__ == '__main__':
    main()
