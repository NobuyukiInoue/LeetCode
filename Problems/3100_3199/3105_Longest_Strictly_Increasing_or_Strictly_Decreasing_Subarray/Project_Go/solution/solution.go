package solution

import (
	"fmt"
	"strings"
	"time"
)

func longestMonotonicSubarray(nums []int) int {
	// 0ms
	incr, decr, ans := 1, 1, 1
	prev := nums[0]
	for _, num := range nums {
		if num > prev {
			incr += 1
		} else {
			incr = 1
		}
		if num < prev {
			decr += 1
		} else {
			decr = 1
		}
		prev = num
		ans = myMax(ans, myMax(incr, decr))
	}
	return ans
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

	result := longestMonotonicSubarray(nums)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
