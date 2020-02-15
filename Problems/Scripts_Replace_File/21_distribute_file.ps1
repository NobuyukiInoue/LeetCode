param($listFile)

if (-Not $listFile) {
    Write-Host "Usage :"$MyInvocation.MyCommand.Name" [listFile]"
    exit
}

$sourceFile1 = "./sourcefile/Mylib.java"
$sourceFile2 = "./sourcefile/Mylib.class"

function loadFile($listFile)
{
    $f = (Get-Content $listFile) -as [string[]]
    $lines = @()

    foreach ($currentLine in $f) {
       if ($currentLine.Contains("Scripts")) {
           continue
       }

       # Write-Host "Copy-Item $sourceFile1 $currentLine"
       # Write-Host "Copy-Item $sourceFile2 $currentLine"
       Copy-Item $sourceFile1 $currentLine
       Copy-Item $sourceFile2 $currentLine
    }
}

loadFile $listFile
