$TargetPath=".."
$TargetProject="Project_C"

$MakeCommand="mingw32-make.exe"

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
    $MakeCommand

    $exeFiles=Get-ChildItem -Name *.exe
    foreach ($current_exe in $exeFiles) {
        Write-Host $current_exe
        if ($current_exe -eq "") {
            continue
        }

        Write-Host "##==== Execute ====###"
        $ExecCmd="./$current_exe ../testdata.txt"
        invoke-expression $ExecCmd
    }
}

Set-Location $StartPath
