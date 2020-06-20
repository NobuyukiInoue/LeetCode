package solution

import (
	"fmt"
	"strings"
	"time"
)

func jump(nums []int) int {
	// 8ms
	end, furthest, result := 0, 0, 0

	for i := 0; i < len(nums)-1; i++ {
		furthest = max(furthest, i+nums[i])
		if i == end {
			result++
			end = furthest
		}
	}

	return result
}

func max(a int, b int) int {
	if a > b {
		return a
	} else {
		return b
	}
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	flds := strings.Replace(temp, "]", "", -1)
	nums := StringToIntArray(flds)

	fmt.Printf("nums = [%s]\n", IntArrayToString(nums))
	timeStart := time.Now()

	result := jump(nums)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
