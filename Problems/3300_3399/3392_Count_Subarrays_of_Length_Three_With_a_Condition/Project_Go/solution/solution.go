package solution

import (
	"fmt"
	"strings"
	"time"
)

func countSubarrays(nums []int) int {
	// 0ms
	ans := 0
	for i := 0; i < len(nums)-2; i++ {
		if nums[i+1] == (nums[i]+nums[i+2])*2 {
			ans++
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

	result := countSubarrays(nums)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
