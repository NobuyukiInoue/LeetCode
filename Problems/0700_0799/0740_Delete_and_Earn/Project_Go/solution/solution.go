package solution

import (
	"fmt"
	"strings"
	"time"
)

func deleteAndEarn(nums []int) int {
	// 4ms
	dp := make([]int, 10001)
	for _, num := range(nums) {
		dp[num] += num
	}
	for i := 2; i < len(dp); i++ {
		dp[i] = myMax(dp[i-1], dp[i-2] + dp[i])
	}
	return dp[len(dp) - 1]
}

func myMax(a int, b int) int {
	if a > b {
		return a
	}
	return b
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, ", ", ",", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	flds := strings.Replace(temp, "]", "", -1)

	nums := StringToIntArray(flds)
	fmt.Printf("nums = %s\n", IntArrayToString(nums))

	timeStart := time.Now()

	result := deleteAndEarn(nums)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
