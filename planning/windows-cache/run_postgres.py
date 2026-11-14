"""Disposable native Windows cluster; never connects to application/user databases."""
import hashlib
import json
import os
from pathlib import Path
import secrets
import socket
import subprocess
import tempfile
import time

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[1]
PG=ROOT/'planning/runtime-manifests/.runs/postgresql/pgsql/bin'
NODE=ROOT/'planning/runtime-manifests/.runs/candidate-components/node/node.exe'


def main():
    run=Path(tempfile.mkdtemp(prefix='postgres-ascii-',dir=HERE/'.runs'))
    data=run/'data'
    password=secrets.token_hex(24)
    pw=run/'password.txt';pw.write_text(password,encoding='ascii')
    with socket.socket() as sock:
        sock.bind(('127.0.0.1',0));port=sock.getsockname()[1]
    env={k:v for k,v in os.environ.items() if k.upper() in {'SYSTEMROOT','WINDIR','TEMP','TMP','COMSPEC'}}
    env['PATH']=str(PG)+os.pathsep+str(Path(os.environ['SYSTEMROOT'])/'System32')
    env.update(DOZU_PROBE_PORT=str(port),DOZU_PROBE_PASSWORD=password)
    evidence={'host':'Windows 11 developer host; not clean or Windows 10','cluster':'new disposable isolated cluster; no application migrations/user records',
              'nodeSha256':hashlib.sha256(NODE.read_bytes()).hexdigest(),'phases':[]}
    def cmd(name,args,timeout=45):
        log=run/(name+'.log')
        # A daemon may inherit pipe handles; use a regular log rather than waiting
        # for EOF on a pipe that a running postmaster can keep open after pg_ctl exits.
        with log.open('w',encoding='utf-8') as stream:
            p=subprocess.run(args,env=env,cwd=run,stdout=stream,stderr=subprocess.STDOUT,timeout=timeout,creationflags=subprocess.CREATE_NO_WINDOW)
        evidence['phases'].append({'name':name,'exitCode':p.returncode})
        if p.returncode: raise RuntimeError(name+': '+log.read_text(encoding='utf-8',errors='replace')[-1500:])
    active=False
    try:
        cmd('initdb',[str(PG/'initdb.exe'),'-D',str(data),'-U','dozu_probe','--pwfile',str(pw),'--auth-host=scram-sha-256','--auth-local=scram-sha-256','--no-locale','-E','UTF8'])
        pw.unlink()
        def start(label):
            cmd(label,[str(PG/'pg_ctl.exe'),'-D',str(data),'-l',str(run/'server.log'),'-o',f'-h 127.0.0.1 -p {port} -c max_connections=40','-w','start'])
        def stop(label):
            cmd(label,[str(PG/'pg_ctl.exe'),'-D',str(data),'-m','fast','-w','stop'])
        start('start');active=True
        cmd('before',[str(NODE),str(HERE/'probe_postgres.cjs'),'before'],90)
        stop('stop-for-restart');active=False
        start('restart');active=True
        cmd('after',[str(NODE),str(HERE/'probe_postgres.cjs'),'after'],90)
        evidence['result']='passed'
    except Exception as exc:
        evidence['result']='failed'
        evidence['error']=str(exc)
        raise
    finally:
        if pw.exists():pw.unlink()
        if active or (data/'postmaster.pid').exists():stop('final-stop')
        evidence['ownedClusterStopped']=not (data/'postmaster.pid').exists()
        (HERE/'postgres-native-probe.json').write_text(json.dumps(evidence,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(evidence))


if __name__=='__main__':main()
