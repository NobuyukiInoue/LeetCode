param($enable_log, $dirList)

##--------------------------------------------------------##
## ENABLE LOG Check.
##--------------------------------------------------------##
if (-Not($enable_log)) {
    $enable_log = $FALSE
}
else {
    if ($enable_log -eq $TRUE) {
        $enable_log = $TRUE
    }
    else {
        $enable_log = $FALSE
    }
}


##--------------------------------------------------------##
## Set Variables
##--------------------------------------------------------##
$TargetPath=".."
$TargetProject="Project_CS"
$ExecCmd="dotnet run ../testdata.txt"
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
        Write-Host "$dirList Not found."
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

    if ($enable_log) {
        Write-Output ${currentLine} | Out-File ${StartPath}\${LogFile} -Append -Encoding Default
    }
    else {
        Write-Output ${currentLine}
    }

    Set-Location -Path ${currentLine}
    $resultPath=Get-Location
    Write-Host $resultPath


    Write-Host "##==== Execute ====###"
    Invoke-Expression $ExecCmd
}

Set-Location $StartPath
