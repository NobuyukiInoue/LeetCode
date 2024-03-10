package solution

import (
	"fmt"
	"strings"
	"time"
)

func minimumDeletions(nums []int) int {
	// 110ms - 118ms
	min_v, max_v := nums[0], nums[0]
	min_p, max_p := 0, 0
	for i, num := range nums {
		if num < min_v {
			min_v = num
			min_p = i
		} else if num > max_v {
			max_v = num
			max_p = i
		}
	}
	left := myMin(min_p, max_p)
	right := myMax(min_p, max_p)
	n := len(nums)
	return myMin(right+1, myMin(n-left, left+1+(n-right)))
}

func myMin(a, b int) int {
	if a < b {
		return a
	}
	return b
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

	result := minimumDeletions(nums)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
