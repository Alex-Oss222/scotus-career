$ErrorActionPreference = 'Stop'
$reviewDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$workspaceDir = Split-Path -Parent $reviewDir
$indexPath = Join-Path $workspaceDir 'OT_1992_CASE_INDEX.md'
$indexRows = @()
foreach ($line in Get-Content -LiteralPath $indexPath) {
    if ($line -match '^\|\s*(\d+)\s*\|\s*(\d+)\s*\|\s*([^|]+)\|\s*([^|]+)\|\s*(\d{4}-\d{2}-\d{2})\s*\|') {
        $indexRows += [pscustomobject]@{ Id=[int]$Matches[1]; Chunk=[int]$Matches[2]; Caption=$Matches[3].Trim(); Docket=$Matches[4].Trim(); Date=$Matches[5] }
    }
}
if ($indexRows.Count -ne 123) { throw 'Expected 123 indexed cases.' }
$parts = @('part_01_03.md','part_04_06.md','part_07_09.md','part_10_11.md')
$entries = @()
foreach ($part in $parts) {
    $partText = Get-Content -LiteralPath (Join-Path $reviewDir $part) -Raw
    foreach ($entryMatch in [regex]::Matches($partText, '(?ms)^## (?<id>\d+)\. (?<caption>[^\r\n]+)\r?\n(?<body>.*?)(?=^## \d+\. |\z)')) {
        $caseBody = $entryMatch.Groups['body'].Value.Trim()
        $caseBody = [regex]::Replace($caseBody, '(?ms)^#{2,3} (?:Prioritized findings for (?:synthesis|integration)|Principal findings from cases[^\r\n]*|Principal findings for synthesis)[^\r\n]*\r?\n.*\z', '').Trim()
        $entries += [pscustomobject]@{ Id=[int]$entryMatch.Groups['id'].Value; Caption=$entryMatch.Groups['caption'].Value.Trim(); Body=$caseBody; Part=$part }
    }
}
if ($entries.Count -ne 123) { throw "Expected 123 reviewed cases; found $($entries.Count)." }
for ($entryNumber=0; $entryNumber -lt 123; $entryNumber++) {
    if ($entries[$entryNumber].Id -ne ($entryNumber+1)) { throw 'Case order or uniqueness mismatch.' }
}
$outputPath = Join-Path $workspaceDir 'STONE_JURISPRUDENCE_REVIEW.md'
$output = [System.Collections.Generic.List[string]]::new()
$output.Add((Get-Content -LiteralPath (Join-Path $reviewDir 'REVIEW_OVERVIEW.md') -Raw).Trim())
$output.Add('')
$sourceChecks = @()
foreach ($entry in $entries) {
    $row = $indexRows[$entry.Id-1]
    $stoneName = 'OT_1992CHUNK{0}_STONE.md' -f $row.Chunk
    $neutralName = 'OT_1992CHUNK{0}_NEUTRAL.md' -f $row.Chunk
    $stonePath = Join-Path $workspaceDir $stoneName
    $neutralPath = Join-Path $workspaceDir $neutralName
    $chunkRows = @($indexRows | Where-Object { $_.Chunk -eq $row.Chunk })
    $localOrdinal = $entry.Id - $chunkRows[0].Id
    $stoneHeadings = @(Select-String -LiteralPath $stonePath -Pattern '^## ')
    $neutralHeadings = @(Select-String -LiteralPath $neutralPath -Pattern '^## ')
    if ($stoneHeadings.Count -ne $chunkRows.Count -or $neutralHeadings.Count -ne $chunkRows.Count) { throw "Source heading count mismatch in chunk $($row.Chunk)." }
    $stoneHeading = $stoneHeadings[$localOrdinal]
    $neutralHeading = $neutralHeadings[$localOrdinal]
    if ($stoneHeading.Line.Substring(3).Trim() -ne $row.Caption -or $neutralHeading.Line.Substring(3).Trim() -ne $row.Caption) { throw "Source caption mismatch for $($row.Id): $($row.Caption)" }
    if ($entry.Caption -ne $row.Caption) { throw "Review caption mismatch for $($row.Id): $($entry.Caption) / $($row.Caption)" }
    $dateMatch = [regex]::Match($entry.Body, '\*\*Date:\*\* ([A-Za-z]+ \d{1,2}, \d{4})\.')
    if (-not $dateMatch.Success) { throw "Missing date in entry $($row.Id)." }
    $entryDate = [datetime]::ParseExact($dateMatch.Groups[1].Value, 'MMMM d, yyyy', [cultureinfo]::InvariantCulture).ToString('yyyy-MM-dd')
    if ($entryDate -ne $row.Date) { throw "Date mismatch in entry $($row.Id)." }
    $stoneUrl = $stonePath.Replace('\','/') + ':' + $stoneHeading.LineNumber
    $neutralUrl = $neutralPath.Replace('\','/') + ':' + $neutralHeading.LineNumber
    $output.Add(('## {0}. {1}' -f $entry.Id,$row.Caption))
    $output.Add('')
    $output.Add(('**Current packet:** [Stone position](<{0}>) · **Record and posture:** [Neutral packet](<{1}>). The assessment below describes the pre-revision draft.' -f $stoneUrl,$neutralUrl))
    $output.Add('')
    $output.Add($entry.Body)
    $output.Add('')
    $sourceChecks += [pscustomobject]@{id=$row.Id;caption=$row.Caption;date=$row.Date;source_chunk=$row.Chunk;stone_line=$stoneHeading.LineNumber;neutral_line=$neutralHeading.LineNumber;part=$entry.Part}
}
$finalText = ($output -join "`n") + "`n"
[System.IO.File]::WriteAllText($outputPath,$finalText,[System.Text.UTF8Encoding]::new($false))
$validation = [ordered]@{
    reviewed_cases=$entries.Count
    indexed_cases=$indexRows.Count
    unique_ordered_ids=$true
    captions_match_index_and_sources=$true
    dates_match_index=$true
    source_links_verified=$true
    source_files_modified=$true
    assessment_phase='Pre-revision assessment retained; source links refreshed after authorized implementation.'
    report=$outputPath
    cases=$sourceChecks
}
[System.IO.File]::WriteAllText((Join-Path $reviewDir 'coverage_validation.json'),($validation | ConvertTo-Json -Depth 5),[System.Text.UTF8Encoding]::new($false))
[pscustomobject]@{Report=$outputPath;Cases=$entries.Count;Characters=$finalText.Length;Words=([regex]::Matches($finalText,'\S+')).Count}
