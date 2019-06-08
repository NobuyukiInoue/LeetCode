$TargetPath="~\OneDrive\Develop-works\LANGS\LeetCode\Problems"
$TargetProject=".\Project_CS"
$MakeCommand=""

$Now=Get-Date -UFormat "%Y%m%d_%H%M%S"
$LogFile="execList_$Now.log"

$list=Get-ChildItem $targetPath\$TargetProject -Recurse -Directory | Select-String -Pattern ":"
$currentPath=Get-Location

foreach ($currentLine in $list) {
    if ($currentLine -eq "") {
        continue
    }

    Write-Host $currentLine
    & cd $currentLine
    Get-Location
    # & $MakeCommand

    & dotnet run ../testdata.txt
}

Set-Location $currentPath
