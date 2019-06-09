$TargetPath=".."
$RemoveFiles="*0605*.log"

Get-ChildItem -Path ${TargetPath} -Include ${RemoveFiles} -Recurse | Remove-Item
