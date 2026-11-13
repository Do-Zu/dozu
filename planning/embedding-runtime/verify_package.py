"""Real packaged CPU HTTP contracts in a fresh profile with non-loopback networking denied."""
import argparse
import ctypes
from ctypes import wintypes
import hashlib
import http.server
import json
import math
import os
from pathlib import Path
import secrets
import socket
import subprocess
import threading
import time
import urllib.error
import urllib.request
import uuid

HERE = Path(__file__).resolve().parent


class Counters(ctypes.Structure):
    _fields_ = [("cb", wintypes.DWORD), ("PageFaultCount", wintypes.DWORD)] + [(n, ctypes.c_size_t) for n in
        ["PeakWorkingSetSize", "WorkingSetSize", "QuotaPeakPagedPoolUsage", "QuotaPagedPoolUsage",
         "QuotaPeakNonPagedPoolUsage", "QuotaNonPagedPoolUsage", "PagefileUsage", "PeakPagefileUsage", "PrivateUsage"]]


def inspect_process(pid):
    kernel, psapi = ctypes.WinDLL("kernel32", use_last_error=True), ctypes.WinDLL("psapi", use_last_error=True)
    kernel.OpenProcess.restype = wintypes.HANDLE
    kernel.CloseHandle.argtypes = [wintypes.HANDLE]
    handle = kernel.OpenProcess(0x410, False, pid)
    psapi.GetProcessMemoryInfo.argtypes = [wintypes.HANDLE, ctypes.POINTER(Counters), wintypes.DWORD]
    counters = Counters(); counters.cb = ctypes.sizeof(counters)
    assert handle and psapi.GetProcessMemoryInfo(handle, ctypes.byref(counters), counters.cb)
    modules, needed = (wintypes.HMODULE * 2048)(), wintypes.DWORD()
    psapi.EnumProcessModulesEx.argtypes = [wintypes.HANDLE, ctypes.c_void_p, wintypes.DWORD, ctypes.POINTER(wintypes.DWORD), wintypes.DWORD]
    psapi.GetModuleFileNameExW.argtypes = [wintypes.HANDLE, wintypes.HMODULE, wintypes.LPWSTR, wintypes.DWORD]
    paths = []
    if psapi.EnumProcessModulesEx(handle, modules, ctypes.sizeof(modules), ctypes.byref(needed), 3):
        for module in modules[:needed.value // ctypes.sizeof(wintypes.HMODULE)]:
            buffer = ctypes.create_unicode_buffer(32768)
            if psapi.GetModuleFileNameExW(handle, module, buffer, len(buffer)):
                paths.append(buffer.value)
    kernel.CloseHandle(handle)
    return {"workingSetBytes": counters.WorkingSetSize, "peakWorkingSetBytes": counters.PeakWorkingSetSize,
            "privateBytes": counters.PrivateUsage, "modules": paths}


def pdf(path, text=None):
    from PyPDF2 import PdfWriter
    from PyPDF2.generic import NameObject, DictionaryObject, DecodedStreamObject
    writer = PdfWriter(); writer.add_blank_page(width=300, height=300)
    if text:
        page = writer.pages[0]
        font = DictionaryObject({NameObject('/Type'): NameObject('/Font'), NameObject('/Subtype'): NameObject('/Type1'), NameObject('/BaseFont'): NameObject('/Helvetica')})
        page[NameObject('/Resources')] = DictionaryObject({NameObject('/Font'): DictionaryObject({NameObject('/F1'): font})})
        content = DecodedStreamObject(); content.set_data(b'BT /F1 12 Tf 20 200 Td (' + text.encode('ascii') + b') Tj ET')
        page[NameObject('/Contents')] = writer._add_object(content)
    with path.open('wb') as stream:
        writer.write(stream)


def main():
    parser = argparse.ArgumentParser(); parser.add_argument("package", type=Path); parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args(); package = args.package.resolve()
    work = HERE / ".runs" / ("Người dùng mới " + uuid.uuid4().hex[:8]); work.mkdir(parents=True)
    files = work / "files"; files.mkdir()
    text = "Spaced repetition improves long term memory."
    pdf(files / "tài liệu.pdf", text); pdf(files / "blank.pdf"); pdf(work / "outside.pdf", text)
    service_token, file_token = secrets.token_urlsafe(32), secrets.token_urlsafe(32)
    file_requests = []
    class Files(http.server.BaseHTTPRequestHandler):
        def do_GET(self):
            authorized = self.headers.get("Authorization") == "Bearer " + file_token
            file_requests.append({"path": self.path, "authenticated": authorized})
            if not authorized:
                self.send_response(401); self.end_headers(); return
            if self.path == "/redirect":
                self.send_response(302); self.send_header("Location", "https://example.com/file.pdf"); self.end_headers(); return
            self.send_response(200); self.end_headers(); self.wfile.write((files / "tài liệu.pdf").read_bytes())
        def log_message(self, *args):
            pass
    file_server = http.server.ThreadingHTTPServer(("127.0.0.1", 0), Files)
    threading.Thread(target=file_server.serve_forever, daemon=True).start()
    with socket.socket() as sock:
        sock.bind(("127.0.0.1", 0)); port = sock.getsockname()[1]
    manifest = json.loads((package / "package-manifest.json").read_text())
    env = {k: v for k, v in os.environ.items() if k.upper() in {"SYSTEMROOT", "WINDIR", "TEMP", "TMP"}}
    env |= {"USERPROFILE": str(work), "HOME": str(work), "APPDATA": str(work / "roaming"), "LOCALAPPDATA": str(work / "local"),
        "HF_HOME": str(work / "hf"), "XDG_CACHE_HOME": str(work / "cache"), "PATH": str(package / "python"),
        "DOZU_EMBEDDING_TOKEN": service_token, "DOZU_EMBEDDING_FILE_TOKEN": file_token,
        "DOZU_EMBEDDING_FILE_ROOT": str(files), "DOZU_EMBEDDING_PORT": str(port),
        "DOZU_EMBEDDING_FILE_ORIGIN": f"http://127.0.0.1:{file_server.server_port}",
        "DOZU_EMBEDDING_BACKEND": manifest["backend"], "DOZU_EMBEDDING_MODEL_PATH": str(package / "service/resources/model"),
        "OMP_NUM_THREADS": "2", "MKL_NUM_THREADS": "2", "PYTHONPATH": "Z:/must-not-load-developer-packages"}
    checks = []; opener = urllib.request.build_opener(urllib.request.ProxyHandler({}))
    def request(path, payload=None, expected=200, headers=None, auth=True):
        head = {"Content-Type": "application/json"}
        if auth: head["Authorization"] = "Bearer " + service_token
        head.update(headers or {})
        req = urllib.request.Request(f"http://127.0.0.1:{port}{path}",
            data=json.dumps(payload).encode() if payload is not None else None, headers=head)
        try: response = opener.open(req, timeout=60)
        except urllib.error.HTTPError as exc: response = exc
        raw = response.read()
        try: data = json.loads(raw)
        except ValueError: data = {"textResponse": raw.decode("utf-8", errors="replace")[:180]}
        assert response.status == expected, (path, response.status, expected, str(data)[:180])
        checks.append({"path": path, "expected": expected, "status": response.status})
        return data
    def vector(values):
        assert len(values) == 384 and all(math.isfinite(v) for v in values)
        assert abs(math.sqrt(sum(v * v for v in values)) - 1) < .0001
        return values
    log_path = work / "service.log"; started = time.perf_counter()
    result = {"backend": manifest["backend"], "package": str(package), "freshProfile": str(work),
              "installedBytes": sum(p.stat().st_size for p in package.rglob("*") if p.is_file()), "method": "Bundled Python -I -B, sanitized environment, no PATH Python/pip or developer packages; Python audit hook denies non-loopback connect/DNS/bind. Not an OS firewall or clean/minimum machine proof."}
    with log_path.open("wb") as log:
        proc = subprocess.Popen([str(package / "python/python.exe"), "-I", "-B", str(HERE / "offline_worker.py"), str(package / "service/run.py")],
            cwd=work, env=env, stdout=log, stderr=subprocess.STDOUT)
        try:
            while time.perf_counter() - started < 120:
                if proc.poll() is not None: raise RuntimeError(f"Packaged process exited {proc.returncode}; see {log_path}")
                try:
                    health = request("/health"); break
                except (OSError, urllib.error.URLError): time.sleep(.1)
            else: raise RuntimeError("Readiness timeout")
            result |= {"backendReadySeconds": round(time.perf_counter() - started, 3), "health": health, "readyMemory": inspect_process(proc.pid)}
            request("/health", expected=401, auth=False)
            request("/health", expected=401, headers={"Authorization": "Bearer wrong"})
            request("/health", expected=401, headers={"Origin": "https://example.com"})
            request("/health", expected=400, headers={"Host": "example.com"})
            single = vector(request("/single/text/embedding", {"query": text})["embedding"])
            batch = request("/segments/embedding", {"segments": [{"text": text, "marker": "retained"}, {"text": "Ôn tập để ghi nhớ lâu hơn."}]})
            assert len(batch) == 2 and batch[0]["marker"] == "retained"; [vector(r["embedding"]) for r in batch]
            batch_delta = max(abs(a - b) for a, b in zip(single, batch[0]["embedding"]))
            result["singleVersusBatch"] = {"maxAbsoluteDelta": batch_delta,
                "cosine": sum(a * b for a, b in zip(single, batch[0]["embedding"]))}
            if manifest["backend"] == "torch": assert batch_delta < .0001
            assert request("/segments/embedding", {"segments": []}) == []
            assert request("/embedding/compare", {"query": text, "pattern": text})["similarity"] > .999
            request("/single/text/embedding", {}, expected=422)
            for invalid in [[{}], [{"text": 42}], [{"text": "x"}] * 513]:
                request("/segments/embedding", {"segments": invalid}, expected=422)
            segment = {"segments": [{"text": text, "start": 12, "duration": 3}], "query": "remember study material"}
            yt = request("/youtube/segments/embedding", segment)
            assert yt["count"] == 1 and yt["embeddings"][0]["start"] == 12; vector(yt["embeddings"][0]["embedding"])
            assert request("/youtube/segments/similarity", segment)["query_results"][0]["start"] == 12
            local_pdf = request("/pdf/page/embedding", {"fileUrl": str(files / "tài liệu.pdf")})
            assert local_pdf["pageCount"] == 1 and local_pdf["embeddings"][0]["pageNumber"] == 1
            pv = vector(local_pdf["embeddings"][0]["embedding"])
            assert sum(a * b for a, b in zip(single, pv)) > .999
            origin = env["DOZU_EMBEDDING_FILE_ORIGIN"]
            request("/pdf/page/embedding", {"fileUrl": origin + "/text.pdf"})
            for source in [str(files / "blank.pdf"), str(work / "outside.pdf"), str(files / ".." / "outside.pdf"),
                           "relative.pdf", "https://example.com/document.pdf", origin + "/redirect", "file:///etc/passwd", "http://[invalid"]:
                request("/pdf/page/embedding", {"fileUrl": source}, expected=400)
            fixture = json.loads((HERE / "retrieval-fixture.json").read_text(encoding="utf-8"))
            texts = [x["text"] for x in fixture["documents"] + fixture["queries"]]
            texts += ["", "  ", "Unicode tiếng Việt: học tập, dữ liệu, riêng tư!", "long token " * 200]
            vectors = request("/segments/embedding", {"segments": [{"text": t} for t in texts]})
            assert len(vectors) == len(texts); [vector(x["embedding"]) for x in vectors]
            (work / "vectors.json").write_text(json.dumps([v["embedding"] for v in vectors]), encoding="utf-8")
            result |= {"afterInferenceMemory": inspect_process(proc.pid), "fileRequests": file_requests,
                       "vectors": str(work / "vectors.json"), "checks": checks}
            request("/shutdown", {}, expected=401, auth=False)
            request("/shutdown", {})
            result["gracefulExitCode"] = proc.wait(timeout=15); assert proc.returncode == 0
        finally:
            if proc.poll() is None: proc.terminate(); proc.wait(timeout=10)
            file_server.shutdown(); file_server.server_close()
    logs = log_path.read_text(encoding="utf-8")
    assert "DOZU_OFFLINE_DENIED" not in logs
    runtime = json.loads(next(l.split("DOZU_WORKER_RUNTIME ")[1] for l in logs.splitlines() if l.startswith("DOZU_WORKER_RUNTIME ")))
    assert runtime["isolated"] == 1 and all(Path(p).is_relative_to(package) for p in runtime["paths"])
    assert not (work / "hf").exists(), "Unexpected Hugging Face cache created"
    failures = []
    corrupt = work / "corrupt-model"; corrupt.mkdir()
    (corrupt / "config.json").write_text("{}", encoding="utf-8")
    for label, overrides, message in [
        ("missing-token", {"DOZU_EMBEDDING_TOKEN": ""}, "requires a per-launch service token"),
        ("missing-model", {"DOZU_EMBEDDING_MODEL_PATH": str(work / "missing-model")}, "absolute installed model directory"),
        ("corrupt-model", {"DOZU_EMBEDDING_MODEL_PATH": str(corrupt)}, "Model checksum mismatch")]:
        failed = subprocess.run([str(package / "python/python.exe"), "-I", "-B", str(HERE / "offline_worker.py"), str(package / "service/run.py")],
            cwd=work, env=env | overrides, capture_output=True, timeout=30)
        output = (failed.stdout + failed.stderr).decode("utf-8", errors="replace")
        (work / (label + ".log")).write_text(output, encoding="utf-8")
        assert failed.returncode != 0 and message in output and "DOZU_OFFLINE_DENIED" not in output, label
        failures.append({"case": label, "exitCode": failed.returncode, "networkAttempts": 0, "expectedFailureObserved": True})
    result |= {"runtime": runtime, "offlineDeniedAttempts": 0, "log": str(log_path), "negativeStartup": failures, "pass": True}
    args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({k: result[k] for k in ["backend", "installedBytes", "backendReadySeconds", "gracefulExitCode", "pass"]}))


if __name__ == "__main__":
    main()
