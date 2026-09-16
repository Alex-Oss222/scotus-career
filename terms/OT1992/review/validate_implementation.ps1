$ErrorActionPreference = 'Stop'
$workspaceDir = Split-Path -Parent $PSScriptRoot
function Read-Text([string]$path) { [IO.File]::ReadAllText($path).Replace("`r`n","`n") }
function Case-Map([string]$text) {
    $result = [ordered]@{}
    foreach ($m in [regex]::Matches($text,'(?ms)^## (?<caption>[^\n]+)\n(?<body>.*?)(?=^## |\z)')) {
        $caption = $m.Groups['caption'].Value.Trim()
        if ($result.Contains($caption)) { throw "Duplicate caption $caption" }
        $result[$caption] = $m.Groups['body'].Value
    }
    return $result
}
function Section([string]$body,[string]$roman) {
    $pattern = '(?ms)^### SECTION ' + $roman + '\b.*?(?=^### SECTION |\z)'
    $m = [regex]::Match($body,$pattern)
    if (-not $m.Success) { throw "Missing Section $roman" }
    return [regex]::Replace($m.Value.Trim(),'\n+---\s*\z','').Trim()
}
$indexPath = Join-Path $workspaceDir 'OT_1992_CASE_INDEX.md'
$rows = @()
foreach ($line in Get-Content -LiteralPath $indexPath) {
    if ($line -match '^\|\s*(\d+)\s*\|\s*(\d+)\s*\|\s*([^|]+)\|\s*([^|]+)\|\s*(\d{4}-\d{2}-\d{2})\s*\|') {
        $rows += [pscustomobject]@{id=[int]$Matches[1];chunk=[int]$Matches[2];caption=$Matches[3].Trim();date=$Matches[5]}
    }
}
if ($rows.Count -ne 123) { throw 'Index count is not 123.' }
$checks = @()
$changedFiles = [Collections.Generic.List[string]]::new()
$substantiveChanges = 0
$unchangedComparators = 0
foreach ($chunk in 1..11) {
    $base = 'OT_1992CHUNK' + $chunk
    $group = if ($chunk -le 3) {'chunks_01_03'} elseif ($chunk -le 6) {'chunks_04_06'} elseif ($chunk -le 9) {'chunks_07_09'} else {'chunks_10_11'}
    $backupDir = Join-Path $PSScriptRoot ('before_revision/' + $group)
    $combined = Case-Map (Read-Text (Join-Path $workspaceDir ($base+'.md')))
    $stone = Case-Map (Read-Text (Join-Path $workspaceDir ($base+'_STONE.md')))
    $neutral = Case-Map (Read-Text (Join-Path $workspaceDir ($base+'_NEUTRAL.md')))
    $comparator = Case-Map (Read-Text (Join-Path $workspaceDir ($base+'_COMPARATOR.md')))
    $before = Case-Map (Read-Text (Join-Path $backupDir ($base+'.md')))
    $chunkRows = @($rows | Where-Object {$_.chunk -eq $chunk})
    foreach ($map in @($combined,$stone,$neutral,$comparator,$before)) {
        if ($map.Count -ne $chunkRows.Count) { throw "Chunk $chunk case count mismatch." }
        if ((@($map.Keys) -join '|') -ne (($chunkRows.caption) -join '|')) { throw "Chunk $chunk caption/order mismatch." }
    }
    foreach ($row in $chunkRows) {
        $caption = $row.caption
        $stoneSection = Section $stone[$caption] 'II'
        if ($stoneSection -cne (Section $combined[$caption] 'II')) { throw "Stone/combined mismatch: $caption" }
        if ((Section $neutral[$caption] 'I') -cne (Section $combined[$caption] 'I')) { throw "Neutral/combined mismatch: $caption" }
        $oldComparator = Section $before[$caption] 'III'
        if ($oldComparator -cne (Section $combined[$caption] 'III')) { throw "Comparator changed: $caption" }
        if ((Section $comparator[$caption] 'III') -cne (Section $combined[$caption] 'III')) { throw "Comparator standalone mismatch: $caption" }
        $unchangedComparators++
        if (-not $combined[$caption].Contains($row.date)) { throw "Indexed date missing: $caption" }
        if ($stoneSection -notmatch '(?i)USER.DIRECTED|REVISED AT USER DIRECTION|USER.AUTHORIZED') { throw "Missing revised status: $caption" }
        $oldStone = Section $before[$caption] 'II'
        $oldBody = $oldStone.Substring($oldStone.IndexOf('#### B.'))
        $newBody = $stoneSection.Substring($stoneSection.IndexOf('#### B.'))
        # Exclude generic source-provenance cleanup when counting legal text changes.
        $normalize = {param($s)
            $s = [regex]::Replace($s,'(?m)^\*\*Position-source discipline:\*\*[^\n]*','')
            $s = [regex]::Replace($s,' ?filecite[^]+','')
            return $s.Trim()
        }
        $bodyChanged = (& $normalize $oldBody) -cne (& $normalize $newBody)
        if ($bodyChanged) {$substantiveChanges++}
        $checks += [pscustomobject]@{id=$row.id;caption=$caption;date=$row.date;chunk=$chunk;section_I_matches=$true;section_II_matches=$true;section_III_matches_and_unchanged=$true;legal_body_changed=$bodyChanged}
    }
    foreach ($suffix in @('.md','_STONE.md','_NEUTRAL.md','_COMPARATOR.md')) {
        $name=$base+$suffix
        $beforePath=Join-Path $backupDir $name
        if (Test-Path -LiteralPath $beforePath) {
            $liveHash=(Get-FileHash -LiteralPath (Join-Path $workspaceDir $name) -Algorithm SHA256).Hash
            $oldHash=(Get-FileHash -LiteralPath $beforePath -Algorithm SHA256).Hash
            if ($liveHash -ne $oldHash) {$changedFiles.Add($name)}
        }
    }
}
$stonePaths=Get-ChildItem -LiteralPath $workspaceDir -Filter 'OT_1992CHUNK*_STONE.md' -File
$obsolete=@($stonePaths | Select-String -Pattern 'Lane 1:|Lane 2:|PROPOSED AND UNAPPROVED|submitted for express approval')
if ($obsolete.Count -gt 0) { throw "Obsolete operative/status text remains in $($obsolete.Count) locations." }
$result=[ordered]@{
    indexed_cases=123
    reviewed_status_entries=123
    synchronized_stone_sections=123
    synchronized_neutral_sections=123
    preserved_comparator_sections=$unchangedComparators
    captions_order_and_dates_verified=$true
    changed_source_files=$changedFiles.ToArray()
    legal_bodies_changed=$substantiveChanges
    original_packets_preserved=$true
    simulated_decisions_entered=0
    cases=$checks
}
[IO.File]::WriteAllText((Join-Path $PSScriptRoot 'implementation_validation.json'),($result|ConvertTo-Json -Depth 6),[Text.UTF8Encoding]::new($false))
[pscustomobject]@{Cases=123;StoneMatches=123;NeutralMatches=123;ComparatorPreserved=$unchangedComparators;ChangedFiles=$changedFiles.Count;LegalBodiesChanged=$substantiveChanges}
