param( $targetList, $code_before, $code_after )

$CommandName = Split-Path -Leaf $PSCommandPath

if (-Not($targetList) -Or -Not($code_before) -Or -Not($code_after)) {
    Write-Host "Usage : $CommandName <targetList_file> <code_before_file> <code_after_file>"
    Write-Host
    Write-Host "Example)"
    Write-Host $CommandName .\target_file_list.txt .\code_before.txt .\code_after.txt
    exit
}


$f = (Get-Content $targetList) -as [string[]]

$i = 1
foreach ($currentLine in $f) {
    if ($currentLine.Trim() -eq "") {
        continue
    }

    Write-Host "dotnet run "$currentLine" "$code_before" "$code_after
    &dotnet run $currentLine $code_before $code_after

    Write-Host ""
    $i++
}
