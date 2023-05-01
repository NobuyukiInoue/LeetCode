package solution

import (
	"fmt"
	"strings"
	"time"
)

func subArrayRanges(nums []int) int64 {
	// 20ms - 21ms
	res := int64(0)
	n := len(nums)
	for i, _ := range nums {
		l, r := nums[i], nums[i]
		for j := i + 1; j < n; j++ {
			l = myMin(l, nums[j])
			r = myMax(r, nums[j])
			res += int64(r - l)
		}
	}
	return res
}

func myMin(a, b int) int {
	if a <= b {
		return a
	}
	return b
}

func myMax(a, b int) int {
	if a >= b {
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

	result := subArrayRanges(nums)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
