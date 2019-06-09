$TargetPath=".."
$TargetProject="Project_Python3"

#$MakeCommand=""

$Now=Get-Date -UFormat "%Y%m%d_%H%M%S"
$LogFile="${TargetProject}_${Now}.log"

$list=Get-ChildItem $targetPath\$TargetProject -Recurse -Directory | Select-String -Pattern ":"
$StartPath=Get-Location

foreach ($currentLine in $list) {
    $currentLine=[String]$currentLine
    $currentLine=$currentLine.Replace("`n", "")

    if ($currentLine -eq "") {
        continue
    }

    Write-Output ${currentLine} | Out-File ${StartPath}\${LogFile} -Append -Encoding Default

    Set-Location -Path ${currentLine}
    $resultPath=Get-Location
    Write-Host $resultPath
#   $MakeCommand

    $pyFiles=Get-ChildItem -Name *.py
    foreach ($current_py in $pyFiles) {
        Write-Host $current_py
        if ($current_py -eq "") {
            continue
        }

        Write-Host "##==== Execute ====###"
        $ExecCmd="python ./$current_py ../testdata.txt"
        invoke-expression $ExecCmd
    }
}

Set-Location $StartPath
