package solution

import (
	"fmt"
	"strconv"
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

func str2IntArray(flds string) []int {
	numsStr := strings.Split(flds, ",")
	nums := make([]int, len(numsStr))

	for i := 0; i < len(nums); i++ {
		nums[i], _ = strconv.Atoi(numsStr[i])
	}

	return nums
}

func intintArrayToString(nums [][]int) string {
	if len(nums) <= 0 {
		return ""
	}

	resultStr := "[" + intArrayToString(nums[0]) + "]"
	for i := 1; i < len(nums); i++ {
		resultStr += ", [" + intArrayToString(nums[i]) + "]"
	}

	return resultStr
}

func intArrayToString(nums []int) string {
	if len(nums) <= 0 {
		return ""
	}

	resultStr := strconv.Itoa(nums[0])
	for i := 1; i < len(nums); i++ {
		resultStr += ", " + strconv.Itoa(nums[i])
	}

	return resultStr
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	flds := strings.Replace(temp, "]", "", -1)

	nums := str2IntArray(flds)

	fmt.Printf("nums = [%s]\n", intArrayToString(nums))
	timeStart := time.Now()

	result := maxCoins(nums)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
