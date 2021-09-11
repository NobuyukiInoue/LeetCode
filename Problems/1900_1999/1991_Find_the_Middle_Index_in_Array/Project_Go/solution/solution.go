package solution

import (
	"fmt"
	"strings"
	"time"
)

func findMiddleIndex(nums []int) int {
	// 0ms
	left, right := 0, 0
	for _, n := range nums {
		right += n
	}
	for i, n := range nums {
		right -= n
		if left == right {
			return i
		}
		left += n
	}
	return -1
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "[", "", -1)
	flds := strings.Replace(temp, "]", "", -1)

	nums := StringToIntArray(flds)
	fmt.Printf("nums = %s\n", IntArrayToString(nums))

	timeStart := time.Now()

	result := findMiddleIndex(nums)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
