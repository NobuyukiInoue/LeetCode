package solution

import (
	"fmt"
	"strings"
	"time"
)

func firstMissingPositive(nums []int) int {
	// 0ms
	start := 0
	end := len(nums) - 1
	for start <= end {
		index := nums[start] - 1
		if index == start {
			start++
		} else if index < 0 || index > end || nums[start] == nums[index] {
			nums[start] = nums[end]
			end--
		} else {
			nums[start] = nums[index]
			nums[index] = index + 1
		}
	}
	return start + 1
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

	result := firstMissingPositive(nums)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
