const { app, utilityProcess, BrowserWindow, session } = require('electron');
const fs = require('node:fs');
const path = require('node:path');
const http = require('node:http');
const config = JSON.parse(fs.readFileSync(process.argv[2], 'utf8'));
app.setPath('userData', path.join(config.runDir, 'electron-profile'));
app.setPath('logs', path.join(config.runDir, 'electron-logs'));
app.commandLine.appendSwitch('disable-background-networking');
app.commandLine.appendSwitch('disable-component-update');
app.on('window-all-closed', () => { /* explicit proof teardown owns app.quit */ });
const began = performance.now();
const result = { mode: config.mode, versions: process.versions, mainPid: process.pid, checks: [], childEvents: [] };
const wait = ms => new Promise(resolve => setTimeout(resolve, ms));
async function get(url) {
  return new Promise((resolve, reject) => {
    const request = http.get(url, response => {
      let bytes = 0, body = '';
      response.on('data', block => { bytes += block.length; body += block.toString(); });
      response.on('end', () => resolve({ url, status: response.statusCode, bytes, body }));
    });
    request.setTimeout(4000, () => request.destroy(new Error('HTTP timeout')));
    request.on('error', reject);
  });
}
app.whenReady().then(async () => {
  let child, win;
  const samples = [];
  const timer = setInterval(() => samples.push({ seconds: (performance.now() - began) / 1000, processes: app.getAppMetrics() }), 200);
  try {
    // Only the retained UI's loopback requests are allowed in the proof renderer.
    // Deliberate remote providers are not exercised by this startup experiment.
    session.defaultSession.webRequest.onBeforeRequest((details, callback) => {
      const url = new URL(details.url);
      callback({ cancel: !['127.0.0.1', 'localhost'].includes(url.hostname) && !['data:', 'blob:', 'devtools:'].includes(url.protocol) });
    });
    child = utilityProcess.fork(path.join(__dirname, 'utility-entry.cjs'), [config.entry], {
      cwd: config.cwd, env: config.env, stdio: 'pipe', serviceName: `Dozu proof ${config.mode}`
    });
    child.stdout.on('data', chunk => fs.appendFileSync(config.log, chunk));
    child.stderr.on('data', chunk => fs.appendFileSync(config.log, chunk));
    child.on('message', value => result.childEvents.push(value));
    child.on('exit', code => { result.childExitCode = code; result.childExitedSeconds = (performance.now() - began) / 1000; });
    child.on('spawn', () => { result.childPid = child.pid; });
    // Windows process creation/AV can delay module execution beyond spawn.
    // Await actual worker JS telemetry instead of assuming a PID means ready.
    for (let i = 0; i < 300 && result.childEvents.length === 0 && !('childExitCode' in result); i++) await wait(100);
    result.childTelemetrySeconds = (performance.now() - began) / 1000;
    if (config.mode.startsWith('api')) {
      let response, lastError;
      for (let i = 0; i < 300 && !('childExitCode' in result); i++) {
        try { response = await get('http://127.0.0.1:43333/health'); break; }
        catch (error) { lastError = error.message; }
        await wait(100);
      }
      result.checks.push(response || { kind: 'health-unavailable', error: lastError || 'worker exited' });
    } else {
      let response;
      for (let i = 0; i < 100; i++) {
        if ('childExitCode' in result) throw new Error('Next utility process exited before HTTP readiness');
        try { response = await get('http://localhost:43000/en/welcome'); if (response.status === 200) break; }
        catch { /* bounded loopback readiness polling */ }
        await wait(100);
      }
      if (!response || response.status !== 200) throw new Error('Next HTTP readiness failed');
      result.httpReadySeconds = (performance.now() - began) / 1000;
      for (const route of ['/en/welcome', '/vi/welcome', '/en/topics/proof-topic', '/vi/auth/login']) {
        const current = await get(`http://localhost:43000${route}`);
        result.checks.push({ url: current.url, status: current.status, bytes: current.bytes, hasNextScripts: current.body.includes('/_next/static/') });
        fs.writeFileSync(path.join(config.runDir, `${route.replaceAll('/', '_')}.html`), current.body);
      }
      const asset = response.body.match(/src="([^" ]+\/_next\/static\/[^" ]+|\/_next\/static\/[^" ]+)"/);
      if (asset) {
        const current = await get(`http://localhost:43000${asset[1]}`);
        result.checks.push({ kind: 'static-script', status: current.status, bytes: current.bytes, url: current.url });
      }
      win = new BrowserWindow({ show: false, width: 1366, height: 768, webPreferences: { nodeIntegration: false, contextIsolation: true, sandbox: true } });
      win.webContents.on('console-message', event => {
        fs.appendFileSync(config.log, `renderer: ${JSON.stringify({level:event.level,message:event.message})}\n`);
      });
      win.webContents.on('render-process-gone', (_event, details) => { result.rendererGone = details; });
      await win.loadURL('http://localhost:43000/en/welcome');
      await wait(2500);
      result.rendererProbe = await win.webContents.executeJavaScript(`({title:document.title,readyState:document.readyState,bodyCharacters:document.body.innerText.length,buttons:document.querySelectorAll('button').length,links:document.querySelectorAll('a').length,rootLang:document.documentElement.lang})`);
      result.loadedHiddenRendererSeconds = (performance.now() - began) / 1000;
      result.note = 'Hidden BrowserWindow DOM load and HTTP smoke only; no user interaction/interactive-UI budget or 84-workflow/auth/data/provider parity claim.';
      fs.writeFileSync(path.join(config.runDir, 'welcome.png'), (await win.webContents.capturePage()).toPNG());
    }
    result.metricsBeforeStop = app.getAppMetrics();
  } catch (error) { result.error = error.stack; }
  finally {
    clearInterval(timer);
    result.metricSamples = samples;
    fs.writeFileSync(config.result, JSON.stringify(result, null, 2));
    if (win && !win.isDestroyed()) win.destroy();
    if (child?.pid) { result.killRequested = child.kill(); await wait(500); }
    result.elapsedSeconds = (performance.now() - began) / 1000;
    result.method = 'app.getAppMetrics every 200ms includes Electron main/GPU/renderer/utility processes; excludes Python/DB/native converters not running here. Samples are not full-app memory. Child kill is not graceful shutdown proof. Electron runtime archive executed with explicit app entry; no installer/ASAR/signing/clean-machine claim.';
    fs.writeFileSync(config.result, JSON.stringify(result, null, 2));
    app.quit();
  }
}).catch(error => { fs.writeFileSync(config.result, JSON.stringify({error:error.stack})); app.exit(1); });
