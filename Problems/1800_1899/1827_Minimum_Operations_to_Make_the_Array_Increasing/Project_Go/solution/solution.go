package solution

import (
	"fmt"
	"strings"
	"time"
)

func minOperations(nums []int) int {
	// 8ms
	cnt, prev := 0, 0
	for _, cur := range(nums) {
		if cur <= prev {
			prev++
			cnt += prev - cur
		} else {
			prev = cur
		}
	}
	return cnt
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "[", "", -1)
	flds := strings.Replace(temp, "]", "", -1)

	nums := StringToIntArray(flds)
	fmt.Printf("nums = %s\n", IntArrayToString(nums))

	timeStart := time.Now()

	result := minOperations(nums)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
