$ErrorActionPreference = 'Stop'
$proofOut = Join-Path $PSScriptRoot 'database-availability.json'
$proofRequests = @()
foreach ($proofUrl in @('https://get.enterprisedb.com/postgresql/postgresql-17.11-3-windows-x64-binaries.zip', 'https://sbp.enterprisedb.com/getfile.jsp?fileid=1260491')) {
    try {
        $proofResponse = Invoke-WebRequest -Method Head -Uri $proofUrl -TimeoutSec 20
        $proofRequests += @{ url = $proofUrl; httpStatus = [int]$proofResponse.StatusCode; contentLength = $proofResponse.Headers['Content-Length'] }
    } catch {
        $proofRequests += @{ url = $proofUrl; httpStatus = [int]$_.Exception.Response.StatusCode; error = $_.Exception.Message }
    }
}
$proofVS = & 'C:\Program Files (x86)\Microsoft Visual Studio\Installer\vswhere.exe' -latest -products '*' -requires Microsoft.VisualStudio.Component.VC.Tools.x86.x64 -property installationPath
@{
    utc = [DateTime]::UtcNow.ToString('o')
    requests = $proofRequests
    postgresOnPath = [bool](Get-Command postgres -ErrorAction SilentlyContinue)
    standardPostgresDirectory = Test-Path -LiteralPath 'C:\Program Files\PostgreSQL'
    cppBuildTools = $proofVS
    result = 'Native PostgreSQL/pgvector execution not performed: no existing portable binary; official EDB archive requests denied. C++ build tools are available for a later pinned pgvector build after obtaining a verified PostgreSQL distribution.'
    migrationState = '20 ignored local SQL migrations inventoried in audit; no cluster/migrations/seeds/vector writes executed by this proof.'
    references = @('https://www.postgresql.org/download/windows/', 'https://www.enterprisedb.com/download-postgresql-binaries', 'https://github.com/pgvector/pgvector#installation')
} | ConvertTo-Json -Depth 6 | Set-Content -Encoding utf8 -LiteralPath $proofOut
Get-Content -LiteralPath $proofOut
