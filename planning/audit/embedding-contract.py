"""Real-model HTTP contract probe; uses only a supplied local model and loopback PDF."""
import functools
import http.server
import importlib.metadata
import json
import math
from pathlib import Path
import sys
import threading
import socket
import time
import urllib.request
import urllib.error
import subprocess

sys.path.insert(0, str(Path.cwd()))
from PyPDF2 import PdfWriter
from PyPDF2.generic import NameObject, DictionaryObject, DecodedStreamObject

rows = []
sock = socket.socket()
sock.bind(('127.0.0.1', 0))
port = sock.getsockname()[1]
sock.close()
server_process = subprocess.Popen([sys.executable, '-m', 'uvicorn', 'src.app.main:app', '--host', '127.0.0.1', '--port', str(port), '--log-level', 'info'])
deadline = time.monotonic() + 150
ready = False
while server_process.poll() is None and time.monotonic() < deadline:
    try:
        with urllib.request.urlopen(f'http://127.0.0.1:{port}/health', timeout=1) as response:
            ready = response.status == 200
        if ready:
            break
    except (OSError, urllib.error.URLError):
        time.sleep(.2)
if not ready:
    server_process.terminate()
    server_process.wait(timeout=10)
assert ready, 'Actual Uvicorn startup failed'
try:
    def probe(method, url, body=None, expected=200):
        request = urllib.request.Request(f'http://127.0.0.1:{port}{url}', data=json.dumps(body).encode() if body is not None else None, method=method, headers={'Content-Type':'application/json'})
        try:
            response = urllib.request.urlopen(request, timeout=60)
        except urllib.error.HTTPError as error:
            response = error
        raw = response.read().decode()
        try:
            data = json.loads(raw)
        except ValueError:
            data = {'nonJsonResponse': raw[:150]}
        rows.append({'method': method, 'path': url, 'status': response.status, 'expected': expected, 'keys': list(data) if isinstance(data, dict) else type(data).__name__})
        return data

    health = probe('GET', '/health')
    assert health['status'] == 'ok' and health['device'] == 'cpu'
    single = probe('POST', '/single/text/embedding', {'query': 'Learning with flashcards.'})
    vector = single['embedding']
    assert len(vector) == 384 and all(math.isfinite(x) for x in vector)
    norm = math.sqrt(sum(x*x for x in vector))
    assert abs(norm - 1) < 0.001
    batch = probe('POST', '/segments/embedding', {'segments': [{'text': 'Learning with flashcards.', 'start': 0}]})
    comparison = probe('POST', '/embedding/compare', {'query': 'Learning with flashcards.', 'pattern': 'Learning with flashcards.'})
    assert comparison['similarity'] > .999
    segments = {'segments': [{'text': 'Learning with flashcards.', 'start': 0, 'duration': 2}], 'query': 'flashcards'}
    yt_embedding = probe('POST', '/youtube/segments/embedding', segments)
    yt_similarity = probe('POST', '/youtube/segments/similarity', segments)
    probe('POST', '/single/text/embedding', {}, expected=422)
    probe('POST', '/embedding/compare', {'query': 'missing pattern'}, expected=422)
    fixture = Path('contract-fixture')
    fixture.mkdir(exist_ok=True)
    writer = PdfWriter()
    writer.add_blank_page(width=300, height=300)
    with (fixture / 'blank.pdf').open('wb') as stream:
        writer.write(stream)
    writer_text = PdfWriter()
    writer_text.add_blank_page(width=300, height=300)
    page = writer_text.pages[0]
    font = DictionaryObject({NameObject('/Type'):NameObject('/Font'), NameObject('/Subtype'):NameObject('/Type1'), NameObject('/BaseFont'):NameObject('/Helvetica')})
    page[NameObject('/Resources')] = DictionaryObject({NameObject('/Font'): DictionaryObject({NameObject('/F1'): font})})
    content = DecodedStreamObject()
    content.set_data(b'BT /F1 12 Tf 20 200 Td (Learning with flashcards.) Tj ET')
    page[NameObject('/Contents')] = writer_text._add_object(content)
    with (fixture / 'text.pdf').open('wb') as stream:
        writer_text.write(stream)
    server = http.server.ThreadingHTTPServer(('127.0.0.1', 0), functools.partial(http.server.SimpleHTTPRequestHandler, directory=str(fixture)))
    threading.Thread(target=server.serve_forever, daemon=True).start()
    try:
        probe('POST', '/pdf/page/embedding', {'fileUrl': f'http://127.0.0.1:{server.server_port}/blank.pdf'}, expected=400)
        pdf = probe('POST', '/pdf/page/embedding', {'fileUrl': f'http://127.0.0.1:{server.server_port}/text.pdf'})
        assert pdf['pageCount'] == 1 and len(pdf['embeddings'][0]['embedding']) == 384
    finally:
        server.shutdown()
        server.server_close()
finally:
    server_process.terminate()
    server_process.wait(timeout=10)

result = {'runtime': sys.version.split()[0], 'dependencies': {p: importlib.metadata.version(p) for p in ['fastapi','uvicorn','sentence-transformers','torch','transformers','youtube-transcript-api','PyPDF2','requests']}, 'health': health, 'dimension': len(vector), 'norm': norm, 'identicalTextSimilarity': comparison['similarity'], 'batchType': type(batch).__name__, 'checks': rows, 'note': 'Real cached CPU model; actual loopback Uvicorn HTTP server and startup. No mocked embeddings or provider success. YouTube network transcript retrieval not exercised. Text PDF and blank PDF exercise positive and negative extraction paths.'}
print(json.dumps(result, indent=2))
Path('../../baselines/embedding-contract.json').write_text(json.dumps(result, indent=2), encoding='utf-8')
assert all(r['status'] == r['expected'] for r in rows), rows
