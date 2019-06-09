$TargetPath="~\OneDrive\Develop-works\LANGS\LeetCode\Problems"
$TargetProject=".\Project_Java"
$RemoveFiles="*`$*.class"

$Now=Get-Date -UFormat "%Y%m%d_%H%M%S"
$LogFile="removeList_$Now.log"

$list=Get-ChildItem $targetPath\$TargetProject -Recurse -Directory | Select-String -Pattern ":"

foreach ($currentLine in $list) {
    $currentLine=[String]$currentLine
    $currentLine=$currentLine.Replace("`n", "")

    if ($currentLine -eq "") {
        continue
    }

    Write-Host "$currentLine\$RemoveFiles"
    Remove-Item $currentLine\$RemoveFiles
    Write-Output "$currentLine\$RemoveFiles" | Add-Content $LogFile -Encoding Default
}
