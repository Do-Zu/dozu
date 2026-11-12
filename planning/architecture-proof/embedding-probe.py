"""Native real CPU model measurements; invoked by existing venv, no install/download."""
import ctypes
from ctypes import wintypes
import importlib.metadata
import json
import math
import os
from pathlib import Path
import socket
import subprocess
import sys
import threading
import time
import urllib.error
import urllib.request

OUT = Path(__file__).resolve().parent
ROOT = OUT.parents[1]
RUN = OUT / '.runs/dozu-embedding-service'
MODEL = Path.home()/'.cache/huggingface/hub/models--sentence-transformers--paraphrase-multilingual-MiniLM-L12-v2/snapshots/86741b4e3f5cb7765a600d3a3d55a0f6a6cb443d'

class Counters(ctypes.Structure):
    _fields_ = [('cb',wintypes.DWORD),('PageFaultCount',wintypes.DWORD),('PeakWorkingSetSize',ctypes.c_size_t),('WorkingSetSize',ctypes.c_size_t),('QuotaPeakPagedPoolUsage',ctypes.c_size_t),('QuotaPagedPoolUsage',ctypes.c_size_t),('QuotaPeakNonPagedPoolUsage',ctypes.c_size_t),('QuotaNonPagedPoolUsage',ctypes.c_size_t),('PagefileUsage',ctypes.c_size_t),('PeakPagefileUsage',ctypes.c_size_t),('PrivateUsage',ctypes.c_size_t)]

def memory(pid):
    kernel=ctypes.WinDLL('kernel32',use_last_error=True)
    kernel.OpenProcess.restype=wintypes.HANDLE
    kernel.CloseHandle.argtypes=[wintypes.HANDLE]
    psapi=ctypes.WinDLL('psapi',use_last_error=True)
    psapi.GetProcessMemoryInfo.argtypes=[wintypes.HANDLE,ctypes.POINTER(Counters),wintypes.DWORD]
    handle=kernel.OpenProcess(0x410,False,pid)
    if not handle:
        return {'error':ctypes.get_last_error()}
    counters=Counters();counters.cb=ctypes.sizeof(counters)
    ok=psapi.GetProcessMemoryInfo(handle,ctypes.byref(counters),counters.cb)
    kernel.CloseHandle(handle)
    return {'workingSetBytes':counters.WorkingSetSize,'peakWorkingSetBytes':counters.PeakWorkingSetSize,'privateBytes':counters.PrivateUsage} if ok else {'error':ctypes.get_last_error()}

def loaded_modules(pid):
    kernel=ctypes.WinDLL('kernel32',use_last_error=True)
    kernel.OpenProcess.restype=wintypes.HANDLE
    kernel.CloseHandle.argtypes=[wintypes.HANDLE]
    psapi=ctypes.WinDLL('psapi',use_last_error=True)
    modules=(wintypes.HMODULE*2048)();needed=wintypes.DWORD()
    psapi.EnumProcessModulesEx.argtypes=[wintypes.HANDLE,ctypes.c_void_p,wintypes.DWORD,ctypes.POINTER(wintypes.DWORD),wintypes.DWORD]
    psapi.GetModuleFileNameExW.argtypes=[wintypes.HANDLE,wintypes.HMODULE,wintypes.LPWSTR,wintypes.DWORD]
    handle=kernel.OpenProcess(0x410,False,pid)
    paths=[]
    if handle and psapi.EnumProcessModulesEx(handle,modules,ctypes.sizeof(modules),ctypes.byref(needed),3):
        for module in modules[:needed.value//ctypes.sizeof(wintypes.HMODULE)]:
            buffer=ctypes.create_unicode_buffer(32768)
            if psapi.GetModuleFileNameExW(handle,module,buffer,len(buffer)):
                paths.append(buffer.value)
    if handle:kernel.CloseHandle(handle)
    return paths

def worker(port):
    # This worker imports the actual application, not a synthetic embedding implementation.
    import uvicorn
    uvicorn.run('src.app.main:app',host='127.0.0.1',port=port,log_level='info')

def main():
    from build import prepare,ENV
    prepare('dozu-embedding-service')
    RUN.mkdir(parents=True,exist_ok=True)
    with socket.socket() as sock:
        sock.bind(('127.0.0.1',0));port=sock.getsockname()[1]
    env=ENV|{'PYTHONPATH':str(RUN),'MODEL_NAME':str(MODEL),'HF_HOME':str(OUT/'.runs/fresh-hf'),'HF_HUB_OFFLINE':'1','TRANSFORMERS_OFFLINE':'1','OMP_NUM_THREADS':'2','MKL_NUM_THREADS':'2','TOKENIZERS_PARALLELISM':'false'}
    # Execute the base interpreter directly with the existing venv's site-packages.
    # This avoids a venv launcher wrapper obscuring the measured worker PID.
    site = ROOT/'dozu-embedding-service/.venv/Lib/site-packages'
    env['PYTHONPATH']=os.pathsep.join([str(RUN),str(site)])
    samples=[];stop=threading.Event();result={}
    suffix='-serial' if len(sys.argv)>1 and sys.argv[1]=='serial' else ''
    with (OUT/f'embedding-runtime{suffix}.log').open('wb') as log:
        started=time.perf_counter()
        proc=subprocess.Popen([sys._base_executable,str(Path(__file__).resolve()),'worker',str(port)],cwd=RUN,env=env,stdout=log,stderr=subprocess.STDOUT)
        def sample():
            while not stop.wait(.1):
                samples.append({'seconds':round(time.perf_counter()-started,3),**memory(proc.pid)})
        thread=threading.Thread(target=sample);thread.start()
        def request(path,payload=None):
            data=json.dumps(payload).encode() if payload is not None else None
            req=urllib.request.Request(f'http://127.0.0.1:{port}{path}',data=data,headers={'Content-Type':'application/json'})
            t=time.perf_counter()
            try:
                with urllib.request.urlopen(req,timeout=30) as response:
                    return response.status,json.load(response),round(time.perf_counter()-t,4)
            except urllib.error.HTTPError as exc:
                return exc.code,{'error':exc.read().decode()[:200]},round(time.perf_counter()-t,4)
        try:
            while time.perf_counter()-started<120:
                if proc.poll() is not None:
                    raise RuntimeError(f'Worker exited {proc.returncode}')
                try:
                    status,health,_=request('/health')
                    if status==200:
                        break
                except (OSError,urllib.error.URLError):
                    time.sleep(.1)
            else:
                raise RuntimeError('Readiness timeout')
            ready=round(time.perf_counter()-started,3)
            result={'pid':proc.pid,'utc':__import__('datetime').datetime.now(__import__('datetime').timezone.utc).isoformat(),'versions':{p:importlib.metadata.version(p) for p in ['torch','transformers','sentence-transformers','fastapi','uvicorn']},'python':sys.version,'baseExecutable':sys._base_executable,'modelRevision':MODEL.name,'cache':'explicit existing model snapshot; HF_HOME fresh; offline env flags; no downloads; OS file cache not evicted','threadLimits':2,'backendReadySeconds':ready,'health':health,'readyMemory':memory(proc.pid),'checks':[]}
            for path,payload in [('/single/text/embedding',{'query':'Local study data remains on this device.'}),('/segments/embedding',{'segments':[{'text':'Local study data remains on this device.'}]}),('/embedding/compare',{'pattern':'local study','query':'local study'})]:
                status,data,seconds=request(path,payload)
                check={'path':path,'status':status,'seconds':seconds,'memory':memory(proc.pid)}
                if 'embedding' in data:
                    vector=data['embedding'];check|={'dimension':len(vector),'finite':all(math.isfinite(v) for v in vector),'norm':math.sqrt(sum(v*v for v in vector))}
                if 'similarity' in data:
                    check['similarity']=data['similarity']
                result['checks'].append(check)
            time.sleep(2)
            result['idleMemoryAfterRequests']=memory(proc.pid)
            result['nativeLoadedModulePaths']=loaded_modules(proc.pid)
            result['torchCpuDll']={'path':str(site/'torch/lib/torch_cpu.dll'),'bytes':(site/'torch/lib/torch_cpu.dll').stat().st_size}
        finally:
            stop.set();thread.join()
            proc.terminate()
            try:proc.wait(timeout=10)
            except subprocess.TimeoutExpired:proc.kill();proc.wait()
            result['workerExitCodeAfterTermination']=proc.returncode
            result['memorySamples']=samples
            result['sampledPeakWorkingSetBytes']=max((s.get('workingSetBytes',0) for s in samples),default=0)
            result['method']='GetProcessMemoryInfo worker PID every 100ms, plus snapshots. Only embedding worker; excludes orchestrator and all not-yet-running Electron/Next/API/DB/converter processes. Windows shared pages can affect summation; private bytes also recorded. No clean-machine or cold-cache/normal full-app claim. Forced worker termination is not graceful supervisor proof.'
            (OUT/f'embedding-runtime{suffix}.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
    print(json.dumps({k:v for k,v in result.items() if k not in {'memorySamples','nativeLoadedModulePaths'}}),flush=True)

if __name__=='__main__':
    if len(sys.argv)>1 and sys.argv[1]=='worker':worker(int(sys.argv[2]))
    else:main()
