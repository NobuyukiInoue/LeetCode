package solution

import (
	"fmt"
	"strings"
	"time"
)

func peakValleyDifference(nums []int) int {
	// 2ms
	ans := 0
	for i := 1; i < len(nums)-1; i++ {
		if nums[i-1] < nums[i] && nums[i] > nums[i+1] {
			ans += nums[i]
		} else if nums[i-1] > nums[i] && nums[i] < nums[i+1] {
			ans -= nums[i]
		}
	}
	return ans
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "[", "", -1)
	flds := strings.Replace(temp, "]", "", -1)

	nums := StringToIntArray(flds)
	fmt.Printf("nums = [%s]\n", IntArrayToString(nums))

	timeStart := time.Now()

	result := peakValleyDifference(nums)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
