param( $csFile, $testDataFile )

$CommandName = Split-Path -Leaf $PSCommandPath

if (-Not($csFile) -Or -Not($testDataFile)) {
    Write-Host "Usage : $CommandName CSharp_Source testDataFile"
    exit
}

add-type -path ./Length_of_Last_Word.cs -passThru
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
