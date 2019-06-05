param( $targetList, $args )

$CommandName = Split-Path -Leaf $PSCommandPath

if (-Not($targetList)) {
    Write-Host "Usage : $CommandName <targetList_file> <arg_string>"
    Write-Host
    Write-Host "Example)"
    Write-Host $CommandName .\11_exec_file_list.txt
    exit
}


$f = (Get-Content $targetList) -as [string[]]

$i = 1
foreach ($currentLine in $f) {
    if ($currentLine.Trim() -eq "") {
        continue
    }

    $flds = $currentLine -split " "
    Write-Host "python "$flds[0]" "$flds[1]
    &python $flds[0] $flds[1]

    Write-Host ""
    $i++
}
