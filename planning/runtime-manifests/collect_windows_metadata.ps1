# Read-only metadata collection; never copies redistributable DLLs into a release.
[CmdletBinding()]
param([string] $CrtRoot='C:/Program Files/Microsoft Visual Studio/18/Community/VC/Redist/MSVC/14.44.35112/x64/Microsoft.VC143.CRT')
$ErrorActionPreference='Stop'
$taskRepoRoot=(Resolve-Path (Join-Path $PSScriptRoot '../..')).Path
$taskCrtRows=@(Get-ChildItem -LiteralPath $CrtRoot -File | ForEach-Object {
    $taskSignature=Get-AuthenticodeSignature -LiteralPath $_.FullName
    [ordered]@{file=$_.Name;version=$_.VersionInfo.FileVersion;bytes=$_.Length;sha256=(Get-FileHash -LiteralPath $_.FullName -Algorithm SHA256).Hash.ToLower();signatureStatus=[string]$taskSignature.Status;signer=$taskSignature.SignerCertificate.Subject}
})
[ordered]@{status='candidate-inventory-only-not-redistributed';source=$CrtRoot.Replace('C:/Program Files/Microsoft Visual Studio/','Visual Studio ');redistributionGate='Licensed Visual Studio distributor must review exact installed license/REDIST list; no System32 DLL copying';cleanMachineVerified=$false;files=$taskCrtRows} |
    ConvertTo-Json -Depth 7 | Set-Content -LiteralPath (Join-Path $taskRepoRoot 'resources/manifests/microsoft-crt-candidate.json') -Encoding utf8
$taskPgRoot=Join-Path $PSScriptRoot '.runs/postgresql/pgsql/bin'
$taskPgRows=@(Get-ChildItem -LiteralPath $taskPgRoot -Filter *.dll -File | ForEach-Object {
    [ordered]@{file=$_.Name;fileVersion=$_.VersionInfo.FileVersion;productVersion=$_.VersionInfo.ProductVersion;sha256=(Get-FileHash -LiteralPath $_.FullName -Algorithm SHA256).Hash.ToLower()}
})
[ordered]@{status='version-resources-only-not-complete-SBOM';component='postgresql-17.12-1-windows-x64';files=$taskPgRows;note='Blank version fields remain unresolved; EDB vendor source/dependency/license mapping is still required'} |
    ConvertTo-Json -Depth 6 | Set-Content -LiteralPath (Join-Path $taskRepoRoot 'resources/manifests/postgresql-library-versions.json') -Encoding utf8
