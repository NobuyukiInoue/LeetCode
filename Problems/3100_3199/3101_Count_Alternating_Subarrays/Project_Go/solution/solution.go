package solution

import (
	"fmt"
	"strings"
	"time"
)

func countAlternatingSubarrays(nums []int) int64 {
	// 87ms - 94ms
	ans, size := int64(1), int64(1)
	for i := 1; i < len(nums); i++ {
		if nums[i-1] == nums[i] {
			size = 1
		} else {
			size += 1
		}
		ans += size
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

	result := countAlternatingSubarrays(nums)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
