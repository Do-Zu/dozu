"""Process-level offline proof guard; not an OS firewall or a runtime dependency."""
import json
from pathlib import Path
import runpy
import sys


def audit(event, args):
    if event in {"socket.connect", "socket.getaddrinfo", "socket.bind"}:
        address = args[1] if event in {"socket.connect", "socket.bind"} else args[0]
        host = address[0] if isinstance(address, tuple) else address
        if host not in {"127.0.0.1", "::1", None}:
            print("DOZU_OFFLINE_DENIED", event, flush=True)
            raise RuntimeError("Offline proof denies non-loopback networking")


sys.addaudithook(audit)
print("DOZU_WORKER_RUNTIME " + json.dumps({"executable": sys.executable, "prefix": sys.prefix,
    "paths": sys.path, "isolated": sys.flags.isolated}), flush=True)
runpy.run_path(str(Path(sys.argv[1]).resolve()), run_name="__main__")
