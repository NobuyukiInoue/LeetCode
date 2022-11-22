package solution

import (
	"fmt"
	"strings"
	"time"
)

func longestNiceSubarray(nums []int) int {
	// 159ms - 233ms
	AND, i, res, n := 0, 0, 0, len(nums)
	for j := 0; j < n; j++ {
		for (AND & nums[j]) > 0 {
			AND ^= nums[i]
			i++
		}
		AND |= nums[j]
		res = myMax(res, j-i+1)
	}
	return res
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

	result := longestNiceSubarray(nums)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
