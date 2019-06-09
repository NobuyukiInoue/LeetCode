$TargetPath="~/OneDrive/Develop-works/LANGS/LeetCode/Problems"
$TargetProject="Project_CS"

$Now=Get-Date -UFormat "%Y%m%d_%H%M%S"
$LogFile="removeList_$Now.log"

$list=Get-ChildItem $targetPath/$TargetProject -Recurse -Directory | Select-String -Pattern ":"
$StartPath=Get-Location

foreach ($currentLine in $list) {
    $currentLine=[String]$currentLine
    $currentLine=$currentLine.Replace("`n", "")

    if ($currentLine -eq "") {
        continue
    }

    ##== Remove */Project_CS/bin ==##
    $RemoveDir="$currentLine/bin"
    Write-Host $RemoveDir
    Remove-Item -Recurse $RemoveDir
    Write-Output $RemoveDir | Add-Content ${StartPath}\${LogFile} -Encoding Default

    ##== Remove */Project_CS/obj ==##
    $RemoveDir="$currentLine/obj"
    Write-Host $RemoveDir
    Remove-Item -Recurse $RemoveDir
    Write-Output $RemoveDir | Add-Content ${StartPath}\${LogFile} -Encoding Default
}
