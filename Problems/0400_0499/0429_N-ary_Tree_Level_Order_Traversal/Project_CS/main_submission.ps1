param( $csFile )

$CommandName = Split-Path -Leaf $PSCommandPath

if (-Not($csFile)) {
    Write-Host "Usage : $CommandName CSharp_Source"
    exit
}

add-type -path $csFile -passThru
$sl = New-Object Solution
$sl.Main()
