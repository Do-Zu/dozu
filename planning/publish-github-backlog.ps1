#requires -Version 5.1
<#
Publishes the reviewed Dozu planning backlog using the current GitHub CLI login.
Does not read workspace token files or modify application code.
Run -ValidateOnly for offline structural validation.
Reruns identify generated issues by stable markers and preserve unrelated issues.
Generated issue bodies are refreshed from issues.json; edit that file for changes.
#>
[CmdletBinding()]
param(
    [string] $ManifestPath = (Join-Path $PSScriptRoot 'issues.json'),
    [switch] $ValidateOnly
)
$ErrorActionPreference = 'Stop'

function Invoke-GhJson {
    param([string[]] $GhArguments)
    $taskGhOutput = & gh @GhArguments 2>&1
    if ($LASTEXITCODE -ne 0) {
        throw ("GitHub CLI failed: " + ($taskGhOutput -join [Environment]::NewLine))
    }
    $taskGhText = $taskGhOutput -join [Environment]::NewLine
    if (-not [string]::IsNullOrWhiteSpace($taskGhText)) {
        return ($taskGhText | ConvertFrom-Json)
    }
}

function Invoke-GhJsonWrite {
    param(
        [string] $Method,
        [string] $Endpoint,
        [object] $Payload
    )
    $taskPayloadPath = [System.IO.Path]::GetTempFileName()
    try {
        $taskPayloadJson = ConvertTo-Json -InputObject $Payload -Depth 30
        [System.IO.File]::WriteAllText(
            $taskPayloadPath, $taskPayloadJson, (New-Object System.Text.UTF8Encoding($false))
        )
        return (Invoke-GhJson -GhArguments @(
            'api', '--method', $Method, $Endpoint, '--input', $taskPayloadPath
        ))
    }
    finally {
        if (Test-Path -LiteralPath $taskPayloadPath) {
            Remove-Item -LiteralPath $taskPayloadPath
        }
    }
}

$taskManifest = Get-Content -LiteralPath $ManifestPath -Raw -Encoding UTF8 | ConvertFrom-Json
if ($taskManifest.repository -ne 'Do-Zu/dozu') {
    throw 'This publisher is scoped to Do-Zu/dozu.'
}
# Keep the accepted global resource contract current without rewriting historical
# manifest bodies or replacing unrelated local manifest edits. Do not run a full
# publication merely to amend resources: targeted live updates preserve live ACs.
$taskResourceContract = Get-Content -LiteralPath (Join-Path $PSScriptRoot 'resource-contract-2026-11-14.md') -Raw -Encoding UTF8
if (-not $taskResourceContract.Contains('<!-- dozu-resource-contract-2026-11-14:start -->')) {
    throw 'Missing accepted resource-contract revision.'
}
foreach ($taskResourceDraft in $taskManifest.issues) {
    if (-not $taskResourceDraft.body.Contains('<!-- dozu-resource-contract-2026-11-14:start -->')) {
        $taskResourceDraft.body = $taskResourceContract.Trim() + "`n`n" + $taskResourceDraft.body
    }
    if ($taskResourceDraft.id -eq 'PYTHON' -and -not $taskResourceDraft.body.Contains('<!-- dozu-embedding-component-ac-review-2026-11-14:start -->')) {
        $taskComponentReview = Get-Content -LiteralPath (Join-Path $PSScriptRoot 'resource-amendment-2026-11-14/issue-8-component-review.md') -Raw -Encoding UTF8
        $taskResourceDraft.body += "`n`n" + $taskComponentReview.Trim()
    }
}
$taskIssueById = @{}
$taskKnownLabels = @($taskManifest.labels | ForEach-Object { $_.name })
foreach ($taskDraft in $taskManifest.issues) {
    if ($taskDraft.id -notmatch '^[A-Z][A-Z0-9-]*$') { throw 'Invalid draft ID.' }
    if ($taskIssueById.ContainsKey($taskDraft.id)) { throw "Duplicate ID: $($taskDraft.id)" }
    if ($taskDraft.label -notin @('task', 'ticket') -or $taskDraft.label -notin $taskKnownLabels) {
        throw "Invalid label: $($taskDraft.id)"
    }
    if ([string]::IsNullOrWhiteSpace($taskDraft.title) -or [string]::IsNullOrWhiteSpace($taskDraft.body)) {
        throw "Missing issue content: $($taskDraft.id)"
    }
    $taskIssueById[$taskDraft.id] = $taskDraft
}
foreach ($taskDraft in $taskManifest.issues) {
    foreach ($taskDependency in $taskDraft.dependsOn) {
        if (-not $taskIssueById.ContainsKey($taskDependency)) {
            throw "Unknown dependency: $taskDependency"
        }
    }
}
$taskVisiting = @{}
$taskVisited = @{}
function Test-DraftAcyclic {
    param([string] $DraftId)
    if ($taskVisiting.ContainsKey($DraftId)) { throw "Dependency cycle at $DraftId" }
    if ($taskVisited.ContainsKey($DraftId)) { return }
    $taskVisiting[$DraftId] = $true
    foreach ($taskDependency in $taskIssueById[$DraftId].dependsOn) {
        Test-DraftAcyclic -DraftId $taskDependency
    }
    $taskVisiting.Remove($DraftId)
    $taskVisited[$DraftId] = $true
}
foreach ($taskDraft in $taskManifest.issues) { Test-DraftAcyclic -DraftId $taskDraft.id }
if ($ValidateOnly) {
    & (Join-Path $PSScriptRoot 'sync-issue-tracking.ps1') -ManifestPath $ManifestPath -ValidateOnly
    Write-Output ("Validated {0} drafts and an acyclic dependency graph; no GitHub calls." -f $taskManifest.issues.Count)
    return
}

if (-not (Get-Command gh -ErrorAction SilentlyContinue)) { throw 'Install GitHub CLI first.' }
# Read access alone does not prove Issues write access. Fail before mutations if auth is invalid.
$null = Invoke-GhJson -GhArguments @('api', 'user')
$taskRepoPath = 'repos/' + $taskManifest.repository
$taskRepo = Invoke-GhJson -GhArguments @('api', $taskRepoPath)
if (-not $taskRepo.has_issues) { throw 'The target repository has Issues disabled.' }

$taskExistingLabels = @(Invoke-GhJson -GhArguments @(
    'api', ($taskRepoPath + '/labels?per_page=100')
))
foreach ($taskLabel in $taskManifest.labels) {
    if ($taskLabel.name -notin @($taskExistingLabels | ForEach-Object { $_.name })) {
        $null = Invoke-GhJsonWrite -Method 'POST' -Endpoint ($taskRepoPath + '/labels') -Payload @{
            name = $taskLabel.name
            color = $taskLabel.color
            description = $taskLabel.description
        }
    }
}

$taskPages = @(Invoke-GhJson -GhArguments @(
    'api', '--paginate', '--slurp', ($taskRepoPath + '/issues?state=all&per_page=100')
))
$taskExistingIssues = @($taskPages | ForEach-Object { foreach ($taskEntry in $_) { $taskEntry } })
$taskPublished = @{}
foreach ($taskDraft in $taskManifest.issues) {
    $taskMarker = '<!-- dozu-roadmap:' + $taskDraft.id + ' -->'
    $taskMatches = @($taskExistingIssues | Where-Object {
        -not $_.pull_request -and $_.body -and $_.body.Contains($taskMarker)
    })
    if ($taskMatches.Count -gt 1) { throw "Multiple published issues match $($taskDraft.id)." }
    if ($taskMatches.Count -eq 1) {
        $taskCreated = $taskMatches[0]
        Write-Output ("Found {0}: #{1}" -f $taskDraft.id, $taskCreated.number)
    }
    else {
        $taskInitialBody = $taskDraft.body + "`n`n" + $taskMarker +
            "`n`nPhase: " + $taskDraft.phase + " | Priority: " + $taskDraft.priority +
            "`n`nDependency links are populated by the publication pass."
        $taskCreated = Invoke-GhJsonWrite -Method 'POST' -Endpoint ($taskRepoPath + '/issues') -Payload @{
            title = $taskDraft.title
            body = $taskInitialBody
            labels = @($taskDraft.label)
        }
        Write-Output ("Created {0}: {1}" -f $taskDraft.id, $taskCreated.html_url)
    }
    $taskPublished[$taskDraft.id] = $taskCreated
    $taskStatePath = Join-Path $PSScriptRoot 'published-issues.json'
    $taskState = @($taskManifest.issues | Where-Object {
        $taskPublished.ContainsKey($_.id)
    } | ForEach-Object {
        @{
            id = $_.id
            number = $taskPublished[$_.id].number
            url = $taskPublished[$_.id].html_url
            label = $_.label
        }
    })
    [System.IO.File]::WriteAllText(
        $taskStatePath, (ConvertTo-Json -InputObject $taskState -Depth 10),
        (New-Object System.Text.UTF8Encoding($false))
    )
}

foreach ($taskDraft in $taskManifest.issues) {
    $taskIssue = $taskPublished[$taskDraft.id]
    $taskMarker = '<!-- dozu-roadmap:' + $taskDraft.id + ' -->'
    $taskFinalBody = $taskDraft.body + "`n`n" + $taskMarker +
        "`n`nPhase: " + $taskDraft.phase + " | Priority: " + $taskDraft.priority
    if ($taskDraft.id -ne 'ROADMAP') {
        $taskFinalBody += "`n`nParent roadmap: " + $taskPublished['ROADMAP'].html_url
    }
    $taskFinalBody += "`n`n## Dependencies`n"
    if (@($taskDraft.dependsOn).Count -eq 0) {
        $taskFinalBody += "None; this work can start independently.`n"
    }
    else {
        foreach ($taskDependency in $taskDraft.dependsOn) {
            $taskLinked = $taskPublished[$taskDependency]
            $taskFinalBody += "- #" + $taskLinked.number + " - " +
                $taskIssueById[$taskDependency].title + "`n"
        }
    }
    if ($taskDraft.id -eq 'ROADMAP') {
        $taskFinalBody += "`n## Delivery checklist`n"
        foreach ($taskChild in $taskManifest.issues) {
            if ($taskChild.id -ne 'ROADMAP') {
                $taskLinked = $taskPublished[$taskChild.id]
                $taskCheck = if ($taskLinked.state -eq 'closed' -and $taskLinked.state_reason -eq 'completed') { 'x' } else { ' ' }
                $taskFinalBody += "- [" + $taskCheck + "] #" + $taskLinked.number +
                    " - " + $taskChild.title + "`n"
            }
        }
    }
    $taskTrackingBlock = [regex]::Match($taskIssue.body, '(?s)^<!-- dozu-tracking:start -->.*?<!-- dozu-tracking:end -->\s*')
    $taskManualBlockLine = [regex]::Match($taskIssue.body, '(?m)^Blocked because:\s*(.+)$')
    if ($taskManualBlockLine.Success -and -not $taskFinalBody.Contains($taskManualBlockLine.Value)) {
        $taskFinalBody += "`n" + $taskManualBlockLine.Value + "`n"
    }
    if ($taskTrackingBlock.Success) { $taskFinalBody = $taskTrackingBlock.Value + $taskFinalBody }
    if ($taskFinalBody -cne $taskIssue.body -or $taskDraft.title -cne $taskIssue.title) {
        $null = Invoke-GhJsonWrite -Method 'PATCH' -Endpoint (
            $taskRepoPath + '/issues/' + $taskIssue.number
        ) -Payload @{ title = $taskDraft.title; body = $taskFinalBody }
    }
    # Add the generated label without removing unrelated labels.
    if ($taskDraft.label -notin @($taskIssue.labels | ForEach-Object { $_.name })) {
        $null = Invoke-GhJsonWrite -Method 'POST' -Endpoint (
            $taskRepoPath + '/issues/' + $taskIssue.number + '/labels'
        ) -Payload @{ labels = @($taskDraft.label) }
    }

    $taskVerified = Invoke-GhJson -GhArguments @(
        'api', ($taskRepoPath + '/issues/' + $taskIssue.number)
    )
    if ($taskVerified.body -cne $taskFinalBody -or $taskVerified.title -cne $taskDraft.title -or $taskDraft.label -notin @(
        $taskVerified.labels | ForEach-Object { $_.name }
    )) {
        throw "Publication verification failed for $($taskDraft.id)."
    }
    Write-Output ("Verified {0}: #{1}" -f $taskDraft.id, $taskIssue.number)
}
Write-Output ("Verified all {0} issues and labels. Roadmap: {1}" -f
    $taskManifest.issues.Count, $taskPublished['ROADMAP'].html_url)
& (Join-Path $PSScriptRoot 'sync-issue-tracking.ps1') -ManifestPath $ManifestPath

