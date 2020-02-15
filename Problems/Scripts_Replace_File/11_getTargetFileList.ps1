param($targetPath, $targetFile, $resultFile)

if ((-Not $targetFile) -Or (-Not $resultFile)) {
    Write-Host "Usage :"$MyInvocation.MyCommand.Name" [Path] [targetFile] [output file]"
    exit
}

if (-Not $targetPath) {
    $targetPath = "../.."
}

$filterPath = "Scripts"

Get-ChildItem -Path $targetPath -Filter $filterPath $targetFile -Recurse | ForEach {$_.FullName.Replace($targetFile, "")} | Out-File $resultFile -Encoding default
