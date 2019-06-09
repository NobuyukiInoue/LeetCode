$TargetPath=".."
$TargetProject=".\Project_Python3"
$MakeCommand=""

$Now=Get-Date -UFormat "%Y%m%d_%H%M%S"
$LogFile="execList_$Now.log"

$list=Get-ChildItem $targetPath\$TargetProject -Recurse -Directory | Select-String -Pattern ":"
$currentPath=Get-Location

foreach ($currentLine in $list) {
    if ($currentLine -eq "") {
        continue
    }

    Write-Host $currentLine
    & cd $currentLine
    Get-Location
    # & $MakeCommand

    $pyFiles=Get-ChildItem -Name *.py
    foreach ($current_py in $pyFiles) {
        Write-Host $current_py
        if ($current_py -eq "") {
            continue
        }
        Write-Host "python ./$current_py ../testdata.txt"
        & python ./$current_py ../testdata.txt
    }
}

Set-Location $currentPath
