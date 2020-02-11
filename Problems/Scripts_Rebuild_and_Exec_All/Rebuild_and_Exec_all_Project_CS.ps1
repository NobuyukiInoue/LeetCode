$TargetPath=".."
$TargetProject="Project_CS"
$ExecCmd="dotnet run ../testdata.txt"
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
    Start-Process -Wait $MakeCommand

    Write-Host "##==== Execute ====###"
    invoke-expression $ExecCmd
}

Set-Location $StartPath
