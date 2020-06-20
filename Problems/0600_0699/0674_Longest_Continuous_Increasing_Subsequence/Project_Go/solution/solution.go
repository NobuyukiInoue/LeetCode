package solution

import (
	"fmt"
	"strings"
	"time"
)

func findLengthOfLCIS(nums []int) int {
	if len(nums) <= 0 {
		return 0
	}
	count, max_count := 1, 1
	for i := 1; i < len(nums); i++ {
		if nums[i] > nums[i-1] {
			count++
			if count > max_count {
				max_count = count
			}
		} else {
			count = 1
		}
	}

	return max_count
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	flds := strings.Replace(temp, "]", "", -1)

	nums := StringToIntArray(flds)
	fmt.Printf("nums = [%s]\n", IntArrayToString(nums))

	timeStart := time.Now()

	result := findLengthOfLCIS(nums)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
