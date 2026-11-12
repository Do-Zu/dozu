"""Measure default model compression, without modifying its files or storing an archive."""
import hashlib
import json
import lzma
import time
from pathlib import Path
from inventory import MODEL, OUT

files = sorted(p for p in MODEL.rglob('*') if p.is_file())
started = time.perf_counter()
compressor = lzma.LZMACompressor(format=lzma.FORMAT_XZ, preset=6)
checksum = hashlib.sha256()
raw = packed = 0
for path in files:
    with path.open('rb') as stream:
        while block := stream.read(2**20):
            raw += len(block)
            chunk = compressor.compress(block)
            packed += len(chunk)
            checksum.update(chunk)
chunk = compressor.flush()
packed += len(chunk)
checksum.update(chunk)
result = {'method':'Concatenate model snapshot files in lexical relative-path order into one XZ/LZMA2 preset-6 stream; output counted/hashed and discarded. No archive filename metadata; not an NSIS installer and not a mathematical lower bound for all compressors.','modelRevision':MODEL.name,'files':[p.relative_to(MODEL).as_posix() for p in files],'rawBytes':raw,'compressedBytes':packed,'compressedMB':round(packed/1e6,3),'compressedMiB':round(packed/2**20,3),'seconds':round(time.perf_counter()-started,3),'compressedSha256':checksum.hexdigest()}
(OUT/'model-compression.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
print(json.dumps(result),flush=True)
