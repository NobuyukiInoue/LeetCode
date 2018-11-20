param( $testDataFile )

if (-Not($testDataFile)) {
    Write-Host "Usage : ./main_Submission.ps1 testDataFile"
    exit
}

add-type -path ./Length_of_Last_Word_Submission.cs -passThru
$sl = New-Object Solution

$f = (Get-Content $testDataFile) -as [string[]]

$i = 1
foreach ($currentLine in $f) {

	Write-Host ""
	Write-Host "##--------------------------------------------------------------------##"
	Write-Host "## Line["$i"]: = `"$currentLine`""
	Write-Host "##--------------------------------------------------------------------##"

	$sl.Main($currentLine)

	Write-Host ""
	$i++
}
