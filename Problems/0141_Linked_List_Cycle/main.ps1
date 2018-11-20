param( $csFile, $testDataFile )

if (-Not($csFile)) {
    Write-Host "Usage : ./main.ps1 CSharp_Source testDataFile"
    exit
}

if (-Not($testDataFile)) {
    Write-Host "Usage : ./main.ps1 CSharp_Source testDataFile"
    exit
}

add-type -path $csFile -passThru
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
