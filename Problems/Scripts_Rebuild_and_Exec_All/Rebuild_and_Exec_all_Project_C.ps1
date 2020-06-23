##-------------------------------------------------------------------------------##"
## If you want to save the execution result in the log, execute the following."
## > ./Rebuild_and_Exec_all_Project_?.ps1 | Out-File -Encording default <FileName>"
##-------------------------------------------------------------------------------##"
param($enablePathLog, $dirList, $enable_debug)


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

if ($IsMacOS) {
    $exeFiles="main_for_mac"
    $MakeCommand = "make"
}
elseif ($IsLinux) {
    $exeFiles="main_for_linux"
    $MakeCommand = "make"
}
elseif ($IsWindows) {
    $exeFiles="main.exe"
    $MakeCommand = "mingw32-make.exe"
}
else {
    $exeFiles="main.exe"
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

    Invoke-Expression $MakeCommand

    foreach ($current_exe in $exeFiles) {
        Write-Output $current_exe
        if ($current_exe -eq "") {
            continue
        }

        Write-Output "##==== Execute ====###"
        $ExecCmd="./$current_exe ../testdata.txt"
        Invoke-Expression $ExecCmd
    }
}

Set-Location $StartPath
