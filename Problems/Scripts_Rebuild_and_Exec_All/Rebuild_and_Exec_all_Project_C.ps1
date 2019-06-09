$TargetPath=".."
$TargetProject=".\Project_C"
$MakeCommand="mingw32-make.exe"

$Now=Get-Date -UFormat "%Y%m%d_%H%M%S"
$LogFile="execList_$Now.log"

$list=Get-ChildItem $targetPath\$TargetProject -Recurse -Directory | Select-String -Pattern ":"
$currentPath=Get-Location

foreach ($currentLine in $list) {
    if ($currentLine -eq "") {
        continue
    }

    ## Write-Host $currentLine
    & cd $currentLine
    Get-Location
    & $MakeCommand

    $exeFiles=Get-ChildItem -Name *.exe
    foreach ($current_exe in $exeFiles) {
        Write-Host $current_exe
        if ($current_exe -eq "") {
            continue
        }
        Write-Host "./$current_exe ../testdata.txt"
        & ./$current_exe ../testdata.txt
    }
}

Set-Location $currentPath
