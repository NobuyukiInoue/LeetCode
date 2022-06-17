package solution

import (
	"fmt"
	"strings"
	"time"
)

func maxSumDivThree(nums []int) int {
	// 25ms - 45ms
	dp := make([]int, 3)
	for _, num := range nums {
		temp_dp := make([]int, 3)
		copy(temp_dp, dp)
		for _, i := range temp_dp {
			dp[(i+num)%3] = myMax(dp[(i+num)%3], i+num)
		}
	}
	return dp[0]
}

func myMax(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "[", "", -1)
	flds := strings.Replace(temp, "]", "", -1)

	nums := StringToIntArray(flds)
	fmt.Printf("nums = [%s]\n", IntArrayToString(nums))

	timeStart := time.Now()

	result := maxSumDivThree(nums)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
