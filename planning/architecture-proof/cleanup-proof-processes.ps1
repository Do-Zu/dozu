$ErrorActionPreference = 'Stop'
$proofExecutable = Join-Path $PSScriptRoot '.downloads\electron\electron.exe'
$proofWorker = Join-Path $PSScriptRoot 'embedding-probe.py'
$proofProcesses = @(Get-CimInstance Win32_Process -Filter "Name='electron.exe' OR Name='python.exe'" | Where-Object {
    $_.ExecutablePath -eq $proofExecutable -or ($_.CommandLine -and $_.CommandLine.Contains($proofWorker) -and $_.CommandLine -match '\bworker\b')
})
$proofStopped = @()
foreach ($proofProcess in $proofProcesses) {
    $proofCurrent = Get-CimInstance Win32_Process -Filter "ProcessId=$($proofProcess.ProcessId)" -ErrorAction SilentlyContinue
    if ($proofCurrent -and $proofCurrent.ExecutablePath -eq $proofProcess.ExecutablePath -and $proofCurrent.CreationDate -eq $proofProcess.CreationDate) {
        Stop-Process -Id $proofCurrent.ProcessId -Force
        $proofStopped += @{ pid = $proofCurrent.ProcessId; executable = $proofCurrent.ExecutablePath; reason = 'Exact owned proof executable or embedding worker after experiments' }
    }
}
$proofRemaining = @(Get-CimInstance Win32_Process -Filter "Name='electron.exe' OR Name='python.exe'" | Where-Object {
    $_.ExecutablePath -eq $proofExecutable -or ($_.CommandLine -and $_.CommandLine.Contains($proofWorker) -and $_.CommandLine -match '\bworker\b')
})
@{ utc=[DateTime]::UtcNow.ToString('o'); stopped=$proofStopped; remainingOwnedProcessCount=$proofRemaining.Count; method='Exact executable/worker-script match plus creation-date verification before stop; no unrelated process stopped. No application/data directories deleted.' } | ConvertTo-Json -Depth 5 | Set-Content -Encoding utf8 (Join-Path $PSScriptRoot 'cleanup.json')
Get-Content (Join-Path $PSScriptRoot 'cleanup.json')
