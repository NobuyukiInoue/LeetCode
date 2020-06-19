param($listFile)

if (-Not $listFile) {
    Write-Host "Usage :"$MyInvocation.MyCommand.Name" [listFile]"
    exit
}

$sourceFile1 = "./sources/Codec.java"
$sourceFile2 = "./sources/Codec.class"
$sourceFile3 = "./sources/OperateTreeNode.java"
$sourceFile4 = "./sources/OperateTreeNode.class"
$removeFile1 = "Operate_TreeNode.java"
$removeFile2 = "Operate_TreeNode.class"

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
       # Write-Host "Copy-Item $sourceFile3 $currentLine"
       # Write-Host "Copy-Item $sourceFile4 $currentLine"

       Copy-Item $sourceFile1 $currentLine
       Copy-Item $sourceFile2 $currentLine
       Copy-Item $sourceFile3 $currentLine
       Copy-Item $sourceFile4 $currentLine

       Remove-Item $currentLine\$removeFile1
       Remove-Item $currentLine\$removeFile2
    }
}

loadFile $listFile
