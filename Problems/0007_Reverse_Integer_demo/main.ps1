param( $csFile, $testDataFile )

$CommandName = Split-Path -Leaf $PSCommandPath

add-type -path $csFile -passThru
$sl = New-Object Solution

$f = (Get-Content $testDataFile) -as [string[]]

foreach ($currentLine in $f) {
    $sl.Main($currentLine)
}
