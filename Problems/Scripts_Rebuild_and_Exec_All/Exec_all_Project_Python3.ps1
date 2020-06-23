##-------------------------------------------------------------------------------##"
## If you want to save the execution result in the log, execute the following."
## > ./Exec_all_Project_?.ps1 | Out-File -Encording default <FileName>"
##-------------------------------------------------------------------------------##"
param($enablePathLog, $dirList)

##--------------------------------------------------------##
## ENABLE LOG Check.
##--------------------------------------------------------##
if (-Not($enablePathLog)) {
    $enablePathLog = $FALSE
}
else {
    if ($enablePathLog -eq $TRUE) {
        $enablePathLog = $TRUE
    }
    else {
        $enablePathLog = $FALSE
    }
}

##--------------------------------------------------------##
## Set Variables
##--------------------------------------------------------##
$TargetPath=".."
$TargetProject="Project_Python3"

#$MakeCommand=""

$Now=Get-Date -UFormat "%Y%m%d_%H%M%S"
$LogFile="${TargetProject}_${Now}.log"
$StartPath=Get-Location

if (-Not($dirList)) {
    if ($IsMacOS -Or $IsLinux) {
        $list=Get-ChildItem $targetPath\$TargetProject -Recurse -Directory | Select-String -Pattern "/"
    }
    elseif ($IsWindows) {
        $list=Get-ChildItem $targetPath\$TargetProject -Recurse -Directory | Select-String -Pattern ":"
    }
    else {
        $list=Get-ChildItem $targetPath\$TargetProject -Recurse -Directory | Select-String -Pattern ":"
    }
}
else {
    if ((Test-Path $dirList) -eq $FALSE) {
        Write-Output "$dirList Not found."
        return
    }
    $list = (Get-Content $dirList) -as [string[]]
}

##--------------------------------------------------------##

foreach ($currentLine in $list) {
    $currentLine=[String]$currentLine
    $currentLine=$currentLine.Replace("`n", "")

    if ($currentLine -eq "") {
        continue
    }

    Set-Location -Path ${currentLine}
    $resultPath=Get-Location

    Write-Output ${resultPath}
    if ($enablePathLog) {
        Write-Output ${resultPath}.Path | Out-File ${StartPath}\${LogFile} -Append -Encoding Default
    }

  ##Invoke-Expression $MakeCommand

    $pyFiles=Get-ChildItem -Name *.py
    foreach ($current_py in $pyFiles) {
        Write-Output $current_py
        if ($current_py -eq "") {
            continue
        }

        Write-Output "##==== Execute ====###"
        $ExecCmd="python ./$current_py ../testdata.txt"
        invoke-expression $ExecCmd
    }
}

Set-Location $StartPath
