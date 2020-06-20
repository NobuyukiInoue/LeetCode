package solution

import (
	"fmt"
	"strings"
	"time"
)

func maxCoins(nums []int) int {
	// 4ms
	dp := make([][]int, len(nums)+2)
	for i := 0; i < len(dp); i++ {
		dp[i] = make([]int, len(nums)+2)
	}
	for k := 1; k <= len(nums); k++ {
		for i := 0; i+k <= len(nums); i++ {
			for j := i + 1; j <= i+k; j++ {
				var left int
				if i == 0 {
					left = 1
				} else {
					left = nums[i-1]
				}
				var right int
				if i+k == len(nums) {
					right = 1
				} else {
					right = nums[i+k]
				}
				dp[i][i+k+1] = max(dp[i][i+k+1], nums[j-1]*left*right+dp[i][j]+dp[j][i+k+1])
			}
		}
	}
	return dp[0][len(nums)+1]
}

func max(a int, b int) int {
	if a > b {
		return a
	} else {
		return b
	}
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	flds := strings.Replace(temp, "]", "", -1)

	nums := StringToIntArray(flds)

	fmt.Printf("nums = [%s]\n", IntArrayToString(nums))
	timeStart := time.Now()

	result := maxCoins(nums)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
