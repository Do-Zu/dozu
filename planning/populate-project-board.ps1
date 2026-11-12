#requires -Version 5.1
<#
Populate the existing Do-Zu Project #6 from the 44 generated issues.
Default: add missing issues and fill missing fields; preserve user-edited fields.
-RefreshFromIssues deliberately refreshes existing fields from current issue labels.
Does not create a project, assign owners, close issues, change views or enable automation.
#>
[CmdletBinding()]
param(
    [string] $ManifestPath = (Join-Path $PSScriptRoot 'issues.json'),
    [switch] $RefreshFromIssues,
    [switch] $ValidateOnly
)
$ErrorActionPreference='Stop'
function Invoke-BoardGh {
    param([string[]] $GhArguments)
    $taskResult=& gh @GhArguments 2>&1
    if ($LASTEXITCODE -ne 0) { throw ('GitHub CLI failed: '+($taskResult -join [Environment]::NewLine)) }
    $taskText=$taskResult -join [Environment]::NewLine
    if ($taskText) { return ($taskText | ConvertFrom-Json) }
}
function Invoke-BoardGraphql {
    param([string] $Query,[hashtable] $Variables)
    $taskInput=[System.IO.Path]::GetTempFileName()
    try {
        $taskPayload=@{query=$Query;variables=$Variables}
        [System.IO.File]::WriteAllText($taskInput,(ConvertTo-Json -InputObject $taskPayload -Depth 30),(New-Object System.Text.UTF8Encoding($false)))
        $taskResponse=Invoke-BoardGh -GhArguments @('api','graphql','--input',$taskInput)
        if ($taskResponse.errors) { throw ($taskResponse.errors | ConvertTo-Json -Depth 10) }
        return $taskResponse.data
    }
    finally { if (Test-Path -LiteralPath $taskInput) { Remove-Item -LiteralPath $taskInput } }
}
function Quote-BoardGraphql {
    param([object] $Value)
    return (ConvertTo-Json -InputObject ([string]$Value) -Compress)
}
function Get-BoardItems {
    param([string] $ProjectId)
    $taskQuery='query($project:ID!,$after:String){node(id:$project){... on ProjectV2{items(first:100,after:$after){nodes{id content{... on Issue{id number url repository{nameWithOwner}}} fieldValues(first:100){nodes{... on ProjectV2ItemFieldSingleSelectValue{name optionId field{... on ProjectV2SingleSelectField{id name}}} ... on ProjectV2ItemFieldTextValue{text field{... on ProjectV2Field{id name}}}}}} pageInfo{hasNextPage endCursor}}}}}'
    $taskCursor=$null
    do {
        $taskData=Invoke-BoardGraphql -Query $taskQuery -Variables @{project=$ProjectId;after=$taskCursor}
        foreach ($taskItem in $taskData.node.items.nodes) { $taskItem }
        $taskPage=$taskData.node.items.pageInfo
        $taskCursor=$taskPage.endCursor
    } while ($taskPage.hasNextPage)
}
function Get-BoardLabelValue {
    param([object] $Issue,[string] $Prefix)
    $taskNames=@($Issue.labels.name | Where-Object { $_.StartsWith($Prefix) })
    if ($taskNames.Count -ne 1) { throw ("Issue #"+$Issue.number+" requires exactly one "+$Prefix+" label.") }
    return $taskNames[0].Substring($Prefix.Length)
}
function Get-BoardStatusName {
    param([string] $Status)
    switch ($Status) {
        'backlog' {return 'Todo'}
        'ready' {return 'Todo'}
        'waiting' {return 'Todo'}
        'in-progress' {return 'In Progress'}
        'in-review' {return 'In Progress'}
        'blocked' {return 'Block'}
        'done' {return 'Done'}
        'closed' {return 'Done'}
        default {throw "Unsupported issue status: $Status"}
    }
}
$taskManifest=Get-Content -LiteralPath $ManifestPath -Raw -Encoding UTF8 | ConvertFrom-Json
if ($taskManifest.repository -ne 'Do-Zu/dozu') { throw 'Publisher is scoped to Do-Zu/dozu and Project #6.' }
foreach ($taskDraft in $taskManifest.issues) {
    if (-not $taskDraft.complexity -or -not $taskDraft.priority -or -not $taskDraft.initialStatus) { throw 'Missing tracking metadata. Run the tracking validator.' }
}
if ($ValidateOnly) {
    Write-Output ("Validated {0} source items for existing Project #6; no network calls." -f $taskManifest.issues.Count)
    return
}
$taskProject=Invoke-BoardGh -GhArguments @('project','view','6','--owner','Do-Zu','--format','json')
if ($taskProject.url -ne 'https://github.com/orgs/Do-Zu/projects/6' -or $taskProject.closed) { throw 'Unexpected or closed project.' }
$taskProjectId=$taskProject.id
$taskFieldList=Invoke-BoardGh -GhArguments @('project','field-list','6','--owner','Do-Zu','--format','json','--limit','100')
$taskExistingFields=@($taskFieldList.fields)
$taskDefs=@(
    @{name='Priority';type='SINGLE_SELECT';options=@('P0','P1','P2','P3')},
    @{name='Complexity';type='SINGLE_SELECT';options=@('S','M','L','XL')},
    @{name='Phase';type='TEXT'},
    @{name='Depends on';type='TEXT'},
    @{name='Blocker';type='TEXT'}
)
foreach ($taskDef in $taskDefs) {
    $taskFound=@($taskExistingFields | Where-Object name -eq $taskDef.name)
    if ($taskFound.Count -gt 1) { throw "Multiple fields named $($taskDef.name)" }
    if ($taskFound.Count -eq 0) {
        $taskArgs=@('project','field-create','6','--owner','Do-Zu','--name',$taskDef.name,'--data-type',$taskDef.type,'--format','json')
        if ($taskDef.type -eq 'SINGLE_SELECT') { $taskArgs+=@('--single-select-options',($taskDef.options -join ',')) }
        $null=Invoke-BoardGh -GhArguments $taskArgs
        Write-Output ("Created project field: "+$taskDef.name)
    }
}
$taskFieldList=Invoke-BoardGh -GhArguments @('project','field-list','6','--owner','Do-Zu','--format','json','--limit','100')
$taskFields=@{}
foreach ($taskName in @('Status','Priority','Complexity','Phase','Depends on','Blocker')) {
    $taskFound=@($taskFieldList.fields | Where-Object name -eq $taskName)
    if ($taskFound.Count -ne 1) { throw "Missing/ambiguous project field: $taskName" }
    $taskFields[$taskName]=$taskFound[0]
}
foreach ($taskName in @('Status','Priority','Complexity')) {
    if ($taskFields[$taskName].type -ne 'ProjectV2SingleSelectField') { throw "$taskName must be a single-select field." }
}
foreach ($taskName in @('Phase','Depends on','Blocker')) {
    if ($taskFields[$taskName].type -ne 'ProjectV2Field') { throw "$taskName must be a text field." }
}
foreach ($taskOption in @('Todo','In Progress','Done','Block')) {
    if ($taskOption -notin @($taskFields.Status.options.name)) { throw "Existing Status field lacks $taskOption; its options will not be overwritten." }
}
$taskPages=@(Invoke-BoardGh -GhArguments @('api','--paginate','--slurp','repos/Do-Zu/dozu/issues?state=all&per_page=100'))
$taskIssues=@($taskPages | ForEach-Object {foreach ($taskIssue in $_) {if (-not $taskIssue.pull_request) {$taskIssue}}})
$taskById=@{}
foreach ($taskDraft in $taskManifest.issues) {
    $taskMarker='<!-- dozu-roadmap:'+$taskDraft.id+' -->'
    $taskMatches=@($taskIssues | Where-Object {$_.body -and $_.body.Contains($taskMarker)})
    if ($taskMatches.Count -ne 1) { throw "Published issue mapping mismatch: $($taskDraft.id)" }
    $taskById[$taskDraft.id]=$taskMatches[0]
}
$taskItems=@(Get-BoardItems -ProjectId $taskProjectId)
$taskNew=@()
foreach ($taskDraft in $taskManifest.issues) {
    $taskIssue=$taskById[$taskDraft.id]
    $taskMatches=@($taskItems | Where-Object {$_.content.url -eq $taskIssue.html_url})
    if ($taskMatches.Count -gt 1) {throw "Duplicate project item: $($taskIssue.html_url)"}
    if ($taskMatches.Count -eq 0) {$taskNew+=$taskDraft}
}
$taskAddedUrls=@{}
for ($taskStart=0;$taskStart -lt $taskNew.Count;$taskStart+=10) {
    $taskEnd=[Math]::Min($taskStart+9,$taskNew.Count-1)
    $taskParts=@()
    for ($taskIndex=$taskStart;$taskIndex -le $taskEnd;$taskIndex++) {
        $taskIssue=$taskById[$taskNew[$taskIndex].id]
        $taskParts+=('a'+$taskIndex+':addProjectV2ItemById(input:{projectId:$project,contentId:'+(Quote-BoardGraphql $taskIssue.node_id)+'}){item{id}}')
    }
    $null=Invoke-BoardGraphql -Query ('mutation($project:ID!){'+($taskParts -join ' ')+'}') -Variables @{project=$taskProjectId}
    for ($taskIndex=$taskStart;$taskIndex -le $taskEnd;$taskIndex++) {
        $taskIssue=$taskById[$taskNew[$taskIndex].id]
        $taskAddedUrls[$taskIssue.html_url]=$true
        Write-Output ("Added issue #"+$taskIssue.number+" to Project #6")
    }
}
$taskItems=@(Get-BoardItems -ProjectId $taskProjectId)
$taskExpected=@()
# Project item indexes can briefly lag successful add mutations. Re-read the
# same project before writing fields; never add duplicates to fix a stale list.
for ($taskReadAttempt=0; $taskReadAttempt -lt 3; $taskReadAttempt++) {
    $taskMissingUrls=@($taskManifest.issues | ForEach-Object {$taskById[$_.id].html_url} | Where-Object {$_ -notin @($taskItems.content.url)})
    if ($taskMissingUrls.Count -eq 0) {break}
    Write-Output ("Waiting for project item index: {0} known items not visible yet." -f $taskMissingUrls.Count)
    $taskItems=@(Get-BoardItems -ProjectId $taskProjectId)
}
if (@($taskManifest.issues | ForEach-Object {$taskById[$_.id].html_url} | Where-Object {$_ -notin @($taskItems.content.url)}).Count -gt 0) {
    throw 'Project item listing has not caught up. Re-read project state before retrying; do not add duplicate cards.'
}
foreach ($taskDraft in $taskManifest.issues) {
    $taskIssue=$taskById[$taskDraft.id]
    $taskItemMatches=@($taskItems | Where-Object {$_.content.url -eq $taskIssue.html_url})
    if ($taskItemMatches.Count -ne 1) {throw "Project item missing/duplicated: $($taskIssue.html_url)"}
    $taskItem=$taskItemMatches[0]
    $taskStatus=Get-BoardLabelValue -Issue $taskIssue -Prefix 'status:'
    $taskPriority=Get-BoardLabelValue -Issue $taskIssue -Prefix 'priority:'
    $taskComplexity=Get-BoardLabelValue -Issue $taskIssue -Prefix 'complexity:'
    $taskDependencies=@($taskDraft.dependsOn | ForEach-Object {$taskById[$_].html_url})
    $taskBlocker='None'
    if ($taskStatus -eq 'blocked') {
        $taskManualReason=[regex]::Match($taskIssue.body,'(?m)^Blocked because:\s*(.+)$')
        if ($taskManualReason.Success) {$taskBlocker=$taskManualReason.Groups[1].Value.Trim()}
        elseif ($taskDraft.blockReason) {$taskBlocker=$taskDraft.blockReason}
        else {throw "Blocked issue #$($taskIssue.number) has no reason."}
    }
    $taskValues=[ordered]@{
        Status=(Get-BoardStatusName $taskStatus)
        Priority=$taskPriority
        Complexity=$taskComplexity
        Phase=$taskDraft.phase
        'Depends on'=$(if ($taskDependencies.Count) {$taskDependencies -join "`n"} else {'None'})
        Blocker=$taskBlocker
    }
    $taskDesired=@{}
    $taskMutations=@()
    $taskAlias=0
    foreach ($taskName in $taskValues.Keys) {
        $taskField=$taskFields[$taskName]
        $taskCurrent=@($taskItem.fieldValues.nodes | Where-Object {$_.field.id -eq $taskField.id})
        if ($taskCurrent.Count -gt 1) {throw 'Duplicate project field value.'}
        $taskValue=[string]$taskValues[$taskName]
        if ($taskCurrent.Count -eq 1 -and -not $RefreshFromIssues -and -not $taskAddedUrls.ContainsKey($taskIssue.html_url)) {
            $taskValue=if ($taskField.type -eq 'ProjectV2SingleSelectField') {$taskCurrent[0].name} else {$taskCurrent[0].text}
        }
        $taskDesired[$taskName]=$taskValue
        $taskCurrentValue=if ($taskCurrent.Count -eq 1) {if ($taskField.type -eq 'ProjectV2SingleSelectField') {$taskCurrent[0].name} else {$taskCurrent[0].text}} else {$null}
        if ($taskCurrentValue -ceq $taskValue) {continue}
        if ($taskField.type -eq 'ProjectV2SingleSelectField') {
            $taskOptions=@($taskField.options | Where-Object name -eq $taskValue)
            if ($taskOptions.Count -ne 1) {throw "Missing/ambiguous option $taskValue in $taskName"}
            $taskGqlValue='singleSelectOptionId:'+(Quote-BoardGraphql $taskOptions[0].id)
        }
        else {$taskGqlValue='text:'+(Quote-BoardGraphql $taskValue)}
        $taskMutations+=('f'+$taskAlias+':updateProjectV2ItemFieldValue(input:{projectId:$project,itemId:'+(Quote-BoardGraphql $taskItem.id)+',fieldId:'+(Quote-BoardGraphql $taskField.id)+',value:{'+$taskGqlValue+'}}){projectV2Item{id}}')
        $taskAlias++
    }
    if ($taskMutations.Count) {
        $null=Invoke-BoardGraphql -Query ('mutation($project:ID!){'+($taskMutations -join ' ')+'}') -Variables @{project=$taskProjectId}
    }
    $taskExpected+=[pscustomobject]@{id=$taskDraft.id;number=$taskIssue.number;url=$taskIssue.html_url;itemId=$taskItem.id;fields=$taskDesired;assignees=@($taskIssue.assignees | ForEach-Object {$_.login} | Where-Object {$_})}
    Write-Output ("Populated fields for issue #"+$taskIssue.number)
}
$taskVerifiedItems=@(Get-BoardItems -ProjectId $taskProjectId)
foreach ($taskRow in $taskExpected) {
    $taskMatches=@($taskVerifiedItems | Where-Object {$_.id -eq $taskRow.itemId -and $_.content.url -eq $taskRow.url})
    if ($taskMatches.Count -ne 1) {throw 'Final project item identity mismatch.'}
    foreach ($taskName in $taskRow.fields.Keys) {
        $taskValuesFound=@($taskMatches[0].fieldValues.nodes | Where-Object {$_.field.id -eq $taskFields[$taskName].id})
        if ($taskValuesFound.Count -ne 1) {throw "Field missing after update: #$($taskRow.number) $taskName"}
        $taskActual=if ($taskFields[$taskName].type -eq 'ProjectV2SingleSelectField') {$taskValuesFound[0].name} else {$taskValuesFound[0].text}
        if ($taskActual -cne $taskRow.fields[$taskName]) {throw "Field verification failed: #$($taskRow.number) $taskName"}
    }
}
[System.IO.File]::WriteAllText((Join-Path $PSScriptRoot 'project-board-items.json'),(ConvertTo-Json -InputObject $taskExpected -Depth 15),(New-Object System.Text.UTF8Encoding($false)))
$taskReport=[ordered]@{project=$taskProject.url;projectId=$taskProjectId;backlogItemsVerified=$taskExpected.Count;totalProjectItems=$taskVerifiedItems.Count;newItemsAdded=$taskNew.Count;fieldsVerified=@('Status','Priority','Complexity','Phase','Depends on','Blocker');boardStatuses=@($taskExpected | Group-Object {$_.fields.Status} | ForEach-Object {[ordered]@{status=$_.Name;count=$_.Count}});assignedItems=@($taskExpected | Where-Object {$_.assignees.Count -gt 0}).Count;existingColumnsPreserved=$true;ownersInvented=$false;automaticTwoWaySyncConfigured=$false}
[System.IO.File]::WriteAllText((Join-Path $PSScriptRoot 'project-board-verification.json'),(ConvertTo-Json -InputObject $taskReport -Depth 15),(New-Object System.Text.UTF8Encoding($false)))
$taskReport | ConvertTo-Json -Depth 15

