param($enable_log, $dirList, $enable_debug)

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
## ENABLE DEBUG Check.
##--------------------------------------------------------##
if (-Not($enable_debug)) {
    $enable_debug = $FALSE
}
else {
    if ($enable_debug -eq $TRUE) {
        $enable_debug = $TRUE
    }
    else {
        $enable_debug = $FALSE
    }
}

##--------------------------------------------------------##
## Set Variables
##--------------------------------------------------------##
$TargetPath=".."
$TargetProject="Project_C"

if ($IsMacOS -Or $IsLinux) {
    $MakeCommand = "make"
}
elseif ($IsWindows) {
    $MakeCommand = "mingw32-make.exe"
}
else {
    $MakeCommand = "mingw32-make.exe"
}

if ($enable_debug) {
    $MakeCommand += " debug"
}

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
    Invoke-Expression $MakeCommand

    $exeFiles=Get-ChildItem -Name *.exe
    foreach ($current_exe in $exeFiles) {
        Write-Host $current_exe
        if ($current_exe -eq "") {
            continue
        }

        Write-Host "##==== Execute ====###"
        $ExecCmd="./$current_exe ../testdata.txt"
        Invoke-Expression $ExecCmd
    }
}

Set-Location $StartPath
