package solution

import (
	"fmt"
	"strings"
	"time"
)

func maximumDifference(nums []int) int {
	// 0ms
	ans := 0
	prefix := nums[0]
	for i := 1; i < len(nums); i++ {
		ans = myMax(ans, nums[i]-prefix)
		prefix = myMin(prefix, nums[i])
	}
	if ans == 0 {
		return -1
	}
	return ans
}

func myMax(a int, b int) int {
	if a > b {
		return a
	}
	return b
}

func myMin(a int, b int) int {
	if a < b {
		return a
	}
	return b
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "[", "", -1)
	flds := strings.Replace(temp, "]", "", -1)

	nums := StringToIntArray(flds)
	fmt.Printf("nums = %s\n", IntArrayToString(nums))

	timeStart := time.Now()

	result := maximumDifference(nums)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
