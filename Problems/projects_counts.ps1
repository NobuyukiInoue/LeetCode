$dirs = @(
  ".\0001_0099\"
 ,".\0100_0199\"
 ,".\0200_0299\"
 ,".\0300_0399\"
 ,".\0400_0499\"
 ,".\0500_0599\"
 ,".\0600_0699\"
 ,".\0700_0799\"
 ,".\0800_0899\"
 ,".\0900_0999\"
 ,".\1000_1099\"
 ,".\1100_1199\"
 ,".\1200_1299\"
 ,".\1300_1399\"
 ,".\1400_1499\"
 ,".\1500_1599\"
 ,".\1600_1699\"
)

$total = 0
foreach ($dir in $dirs) {
    $count = (Get-ChildItem $dir -Name).Count
    $resultStr = "$dir" + "`t...`t" + $count
    Write-Output $resultStr
    $total += $count
}

$resultStr = "Total = " + $total
Write-Output $resultStr
