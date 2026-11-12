#requires -Version 5.1
<#
Refresh live GitHub issue tracking for the generated Dozu backlog.
Existing status/priority/complexity labels and Assignees are authoritative.
Ready/waiting are recalculated from prerequisite issues closed AS COMPLETED.
Active/review/blocked/backlog states are preserved. No automatic owner assignment.
#>
[CmdletBinding()]
param(
    [string] $ManifestPath = (Join-Path $PSScriptRoot 'issues.json'),
    [switch] $ValidateOnly
)
$ErrorActionPreference = 'Stop'

function Invoke-TrackingGh {
    param([string[]] $GhArguments)
    $taskOutput = & gh @GhArguments 2>&1
    if ($LASTEXITCODE -ne 0) { throw ("GitHub CLI failed: " + ($taskOutput -join [Environment]::NewLine)) }
    $taskText = $taskOutput -join [Environment]::NewLine
    if (-not [string]::IsNullOrWhiteSpace($taskText)) { return ($taskText | ConvertFrom-Json) }
}
function Write-TrackingGh {
    param([string] $Method, [string] $Endpoint, [object] $Payload)
    $taskPath = [System.IO.Path]::GetTempFileName()
    try {
        [System.IO.File]::WriteAllText($taskPath, (ConvertTo-Json -InputObject $Payload -Depth 30), (New-Object System.Text.UTF8Encoding($false)))
        return (Invoke-TrackingGh -GhArguments @('api', '--method', $Method, $Endpoint, '--input', $taskPath))
    }
    finally { if (Test-Path -LiteralPath $taskPath) { Remove-Item -LiteralPath $taskPath } }
}
function Get-OneTrackingLabel {
    param([object] $Issue, [string] $Prefix)
    $taskLabels = @($Issue.labels | ForEach-Object { $_.name } | Where-Object { $_.StartsWith($Prefix) })
    if ($taskLabels.Count -gt 1) { throw ("Issue #" + $Issue.number + " has multiple " + $Prefix + " labels. Replace the previous value rather than adding another.") }
    if ($taskLabels.Count -eq 1) { return $taskLabels[0].Substring($Prefix.Length) }
    return ''
}
function Resolve-TrackingStatus {
    param([object] $Draft, [object] $Issue, [hashtable] $IssuesById)
    if ($Issue.state -eq 'closed') {
        if ($Issue.state_reason -eq 'completed') { return 'done' }
        return 'closed'
    }
    $taskCurrent = Get-OneTrackingLabel -Issue $Issue -Prefix 'status:'
    if (-not $taskCurrent) { $taskCurrent = $Draft.initialStatus }
    if ($taskCurrent -in @('in-progress', 'in-review', 'blocked', 'backlog')) { return $taskCurrent }
    foreach ($taskDep in $Draft.dependsOn) {
        $taskDepIssue = $IssuesById[$taskDep]
        if (-not $taskDepIssue -or $taskDepIssue.state -ne 'closed' -or $taskDepIssue.state_reason -ne 'completed') { return 'waiting' }
    }
    return 'ready'
}
function Get-TrackingFilterUrl {
    param([string] $Query)
    return ('https://github.com/Do-Zu/dozu/issues?q=' + [System.Uri]::EscapeDataString($Query))
}
function Escape-TrackingCell {
    param([object] $Value)
    return ([string]$Value).Replace('|', '\|').Replace("`r", ' ').Replace("`n", ' ')
}

$taskManifest = Get-Content -LiteralPath $ManifestPath -Raw -Encoding UTF8 | ConvertFrom-Json
if ($taskManifest.repository -ne 'Do-Zu/dozu') { throw 'This tracker is scoped to Do-Zu/dozu.' }
$taskIds = @{}
$taskAllowedStatuses = @('backlog','ready','waiting','in-progress','in-review','blocked','done','closed')
foreach ($taskDraft in $taskManifest.issues) {
    if ($taskIds.ContainsKey($taskDraft.id)) { throw "Duplicate draft ID: $($taskDraft.id)" }
    $taskIds[$taskDraft.id] = $true
    if ($taskDraft.priority -notin @('P0','P1','P2','P3')) { throw "Missing/invalid priority: $($taskDraft.id)" }
    if ($taskDraft.complexity -notin @('S','M','L','XL') -or -not $taskDraft.complexityReason) { throw "Missing complexity/rationale: $($taskDraft.id)" }
    if ($taskDraft.initialStatus -notin $taskAllowedStatuses) { throw "Missing/invalid initial status: $($taskDraft.id)" }
    if ($taskDraft.initialStatus -eq 'blocked' -and -not $taskDraft.blockReason) { throw "Blocked item requires a reason: $($taskDraft.id)" }
    foreach ($taskName in @($taskDraft.label, ('priority:' + $taskDraft.priority), ('complexity:' + $taskDraft.complexity), ('status:' + $taskDraft.initialStatus))) {
        if ($taskName -notin @($taskManifest.labels.name)) { throw "Undefined label: $taskName" }
    }
}
foreach ($taskDraft in $taskManifest.issues) {
    foreach ($taskDep in $taskDraft.dependsOn) { if (-not $taskIds.ContainsKey($taskDep)) { throw "Unknown dependency: $taskDep" } }
}
if ($ValidateOnly) {
    Write-Output ("Validated tracking metadata for {0} issues; no GitHub calls." -f $taskManifest.issues.Count)
    return
}

$taskRepo = 'repos/' + $taskManifest.repository
$taskLabels = @(Invoke-TrackingGh -GhArguments @('api', ($taskRepo + '/labels?per_page=100')))
foreach ($taskLabel in $taskManifest.labels) {
    if ($taskLabel.name -notin @($taskLabels.name)) {
        $null = Write-TrackingGh -Method 'POST' -Endpoint ($taskRepo + '/labels') -Payload @{name=$taskLabel.name; color=$taskLabel.color; description=$taskLabel.description}
    }
}
$taskPages = @(Invoke-TrackingGh -GhArguments @('api','--paginate','--slurp', ($taskRepo + '/issues?state=all&per_page=100')))
$taskAll = @($taskPages | ForEach-Object { foreach ($taskItem in $_) { if (-not $taskItem.pull_request) { $taskItem } } })
$taskById = @{}
foreach ($taskDraft in $taskManifest.issues) {
    $taskMarker = '<!-- dozu-roadmap:' + $taskDraft.id + ' -->'
    $taskMatches = @($taskAll | Where-Object { $_.body -and $_.body.Contains($taskMarker) })
    if ($taskMatches.Count -ne 1) { throw "Expected exactly one published issue for $($taskDraft.id). Publish the backlog first." }
    $taskById[$taskDraft.id] = $taskMatches[0]
}
# Preflight label conflicts before updating any issue.
foreach ($taskIssue in $taskById.Values) {
    foreach ($taskPrefix in @('status:','priority:','complexity:')) {
        $null = Get-OneTrackingLabel -Issue $taskIssue -Prefix $taskPrefix
    }
}
$taskDoingUrl = Get-TrackingFilterUrl 'is:issue is:open label:"status:in-progress"'
$taskReadyUrl = Get-TrackingFilterUrl 'is:issue is:open label:"status:ready"'
$taskBlockedUrl = Get-TrackingFilterUrl 'is:issue is:open label:"status:blocked"'
$taskWaitingUrl = Get-TrackingFilterUrl 'is:issue is:open label:"status:waiting"'
$taskReviewUrl = Get-TrackingFilterUrl 'is:issue is:open label:"status:in-review"'
$taskRows = @()
foreach ($taskDraft in $taskManifest.issues) {
    # Fresh state prevents overwriting workflow labels changed since the initial listing.
    $taskIssue = Invoke-TrackingGh -GhArguments @('api', ($taskRepo + '/issues/' + $taskById[$taskDraft.id].number))
    $taskStatus = Resolve-TrackingStatus -Draft $taskDraft -Issue $taskIssue -IssuesById $taskById
    if ($taskStatus -notin $taskAllowedStatuses) { throw "Unknown status label on #$($taskIssue.number)" }
    if ($taskStatus -in @('in-progress','in-review') -and @($taskIssue.assignees).Count -eq 0) {
        throw "Assign an owner to active/review issue #$($taskIssue.number) before synchronizing tracking."
    }
    $taskPriority = Get-OneTrackingLabel -Issue $taskIssue -Prefix 'priority:'
    if (-not $taskPriority) { $taskPriority = $taskDraft.priority }
    $taskComplexity = Get-OneTrackingLabel -Issue $taskIssue -Prefix 'complexity:'
    if (-not $taskComplexity) { $taskComplexity = $taskDraft.complexity }
    if ($taskPriority -notin @('P0','P1','P2','P3') -or $taskComplexity -notin @('S','M','L','XL')) { throw "Invalid tracking labels on #$($taskIssue.number)" }
    $taskBody = [regex]::Replace($taskIssue.body, '(?s)<!-- dozu-tracking:start -->.*?<!-- dozu-tracking:end -->\s*', '')
    $taskBlockReason = ''
    if ($taskStatus -eq 'blocked') {
        $taskManualReason = [regex]::Match($taskBody, '(?m)^Blocked because:\s*(.+)$')
        if ($taskManualReason.Success) { $taskBlockReason = $taskManualReason.Groups[1].Value.Trim() }
        elseif ($taskDraft.blockReason) { $taskBlockReason = $taskDraft.blockReason }
        else { throw "Issue #$($taskIssue.number) is blocked without a reason. Add 'Blocked because: ...' to its description." }
    }
    $taskOpenDeps = @($taskDraft.dependsOn | Where-Object {
        $taskById[$_].state -ne 'closed' -or $taskById[$_].state_reason -ne 'completed'
    } | ForEach-Object { $taskById[$_].html_url })
    $taskTracking = "<!-- dozu-tracking:start -->`n## Work tracking`n"
    $taskTracking += "Use the live **status:**, **priority:** and **complexity:** labels above; **Assignees** identifies the owner. These labels are separate from the task/ticket type.`n`n"
    $taskTracking += "**Planning complexity:** " + $taskDraft.complexity + " - " + $taskDraft.complexityReason + "`n"
    $taskTracking += "Complexity is a provisional scope/uncertainty estimate, not a delivery-time commitment. XL work must be split into executable subtasks before starting.`n"
    $taskTracking += "**Planning priority:** " + $taskDraft.priority + " - " + $taskDraft.priorityReason + "`n"
    if ($taskBlockReason) { $taskTracking += "`n**Blocking decision/impediment:** " + $taskBlockReason + "`n" }
    if ($taskDraft.id -eq 'ROADMAP') {
        $taskTracking += "`n### Live views`n"
        $taskTracking += "- [Your Project #6 board](https://github.com/orgs/Do-Zu/projects/6)`n"
        $taskTracking += "- [Doing](" + $taskDoingUrl + ") | [Review](" + $taskReviewUrl + ") | [Ready](" + $taskReadyUrl + ")`n"
        $taskTracking += "- [Blocked](" + $taskBlockedUrl + ") | [Waiting on prerequisites](" + $taskWaitingUrl + ")`n"
        $taskTracking += "`n### Workflow rules`n"
        $taskTracking += "Keep exactly one status, priority and complexity label per issue. Assign an owner when work starts. Waiting means ordinary dependencies remain; blocked requires a specific reason. Close as completed only after acceptance evidence/review; a closed-not-planned item is not done. Start no more than one issue per owner unless deliberately agreed. Your main board is [Dozu Project #6](https://github.com/orgs/Do-Zu/projects/6). Issue labels and project fields are initialized consistently, but no automatic two-way synchronization is configured. Built-in Labels and Assignees reflect their issues; custom project Status/Priority/Complexity must be maintained deliberately. Local dashboard counts are snapshots refreshed by sync-issue-tracking.ps1.`n"
        $taskTracking += "`nPriority: P0 architecture/foundation unblockers; P1 required feature/integration/release work; P2 required supporting work later in the sequence; P3 optional/future only if explicitly added. Complexity: S contained; M moderate; L cross-system/native/security; XL umbrella/high uncertainty requiring breakdown.`n"
    }
    $taskTracking += "<!-- dozu-tracking:end -->`n`n"
    # Keep the old body priority header consistent with the live label.
    $taskBody = [regex]::Replace($taskBody, '(?m)^(Phase: [^\r\n]* \| Priority: )P[0-3]', ('$' + '1' + $taskPriority))
    $taskFinalBody = $taskTracking + $taskBody
    $taskMergedLabels = @($taskIssue.labels.name | Where-Object { $_ -notmatch '^(status|priority|complexity):' })
    $taskMergedLabels += @($taskDraft.label, ('status:'+$taskStatus), ('priority:'+$taskPriority), ('complexity:'+$taskComplexity))
    $taskMergedLabels = @($taskMergedLabels | Sort-Object -Unique)
    $taskCurrentLabels = @($taskIssue.labels.name | Sort-Object -Unique)
    if ($taskFinalBody -cne $taskIssue.body -or ($taskMergedLabels -join '|') -cne ($taskCurrentLabels -join '|')) {
        $null = Write-TrackingGh -Method 'PATCH' -Endpoint ($taskRepo + '/issues/' + $taskIssue.number) -Payload @{body=$taskFinalBody; labels=$taskMergedLabels}
    }
    $taskCheck = Invoke-TrackingGh -GhArguments @('api', ($taskRepo + '/issues/' + $taskIssue.number))
    if ($taskCheck.body -cne $taskFinalBody -or (Get-OneTrackingLabel -Issue $taskCheck -Prefix 'status:') -cne $taskStatus -or (Get-OneTrackingLabel -Issue $taskCheck -Prefix 'priority:') -cne $taskPriority -or (Get-OneTrackingLabel -Issue $taskCheck -Prefix 'complexity:') -cne $taskComplexity -or $taskDraft.label -notin @($taskCheck.labels.name)) {
        throw "Tracking verification failed for #$($taskIssue.number)"
    }
    $taskOwnerNames = @($taskCheck.assignees | ForEach-Object { $_.login } | Where-Object { -not [string]::IsNullOrWhiteSpace([string]$_) })
    $taskRows += [ordered]@{id=$taskDraft.id; number=$taskIssue.number; url=$taskIssue.html_url; type=$taskDraft.label; title=$taskIssue.title; status=$taskStatus; priority=$taskPriority; complexity=$taskComplexity; assignees=$taskOwnerNames; waitingOn=$taskOpenDeps; blockReason=$taskBlockReason}
    Write-Output ("Tracking verified #{0}: {1}, {2}, {3}" -f $taskIssue.number,$taskStatus,$taskPriority,$taskComplexity)
}
$taskSnapshot = [ordered]@{
    capturedAtUtc=[DateTimeOffset]::UtcNow.ToString('o')
    repository=$taskManifest.repository
    doingUrl=$taskDoingUrl
    readyUrl=$taskReadyUrl
    blockedUrl=$taskBlockedUrl
    waitingUrl=$taskWaitingUrl
    inReviewUrl=$taskReviewUrl
    completedTaskCount=@($taskRows | Where-Object { $_.type -eq 'task' -and $_.status -eq 'done' }).Count
    totalTaskCount=@($taskRows | Where-Object { $_.type -eq 'task' }).Count
    issues=$taskRows
}
$taskCounts = @($taskRows | Group-Object { $_.status } | ForEach-Object { [ordered]@{status=$_.Name;count=$_.Count} })
if (@($taskCounts | Where-Object { $_.status -notin $taskAllowedStatuses }).Count -gt 0 -or ($taskCounts | ForEach-Object { $_.count } | Measure-Object -Sum).Sum -ne $taskRows.Count) {
    throw 'Dashboard status aggregation failed.'
}
$taskSnapshot.statusCounts=$taskCounts
[System.IO.File]::WriteAllText((Join-Path $PSScriptRoot 'tracking-snapshot.json'), (ConvertTo-Json -InputObject $taskSnapshot -Depth 15), (New-Object System.Text.UTF8Encoding($false)))
$taskMd = "# Task dashboard`n`nSnapshot UTC: " + $taskSnapshot.capturedAtUtc + ". GitHub labels and Assignees are live; this file refreshes only when the sync script runs.`n`n"
$taskMd += "[Doing](" + $taskDoingUrl + ") | [Review](" + $taskReviewUrl + ") | [Ready](" + $taskReadyUrl + ") | [Blocked](" + $taskBlockedUrl + ") | [Waiting](" + $taskWaitingUrl + ")`n`n"
$taskMd += "Completed tasks (including audits): " + $taskSnapshot.completedTaskCount + " / " + $taskSnapshot.totalTaskCount + ". This count excludes the four tickets and does not measure implemented features or effort-weighted progress.`n`n"
$taskMd += "| Issue | Type | Status | Priority | Complexity | Owner | Unfinished prerequisites | Blocker |`n| --- | --- | --- | --- | --- | --- | --- | --- |`n"
foreach ($taskRow in $taskRows) {
    $taskDisplayOwners = @($taskRow.assignees | Where-Object { -not [string]::IsNullOrWhiteSpace([string]$_) })
    $taskOwner = if ($taskDisplayOwners.Count) { $taskDisplayOwners -join ', ' } else { 'Unassigned' }
    $taskDeps = @($taskRow.waitingOn | ForEach-Object { '[#' + ($_ -replace '^.*/','') + '](' + $_ + ')' }) -join ', '
    $taskMd += '| [#' + $taskRow.number + '](' + $taskRow.url + ') ' + (Escape-TrackingCell $taskRow.title) + ' | ' + $taskRow.type + ' | ' + $taskRow.status + ' | ' + $taskRow.priority + ' | ' + $taskRow.complexity + ' | ' + (Escape-TrackingCell $taskOwner) + ' | ' + $taskDeps + ' | ' + (Escape-TrackingCell $taskRow.blockReason) + " |`n"
}
[System.IO.File]::WriteAllText((Join-Path $PSScriptRoot 'task-dashboard.md'), $taskMd, (New-Object System.Text.UTF8Encoding($false)))
Write-Output ("Verified tracking for {0} issues; completed tasks (including audits): {1}/{2}." -f $taskRows.Count,$taskSnapshot.completedTaskCount,$taskSnapshot.totalTaskCount)
$taskCounts | ForEach-Object { Write-Output ($_.status + ': ' + $_.count) }

