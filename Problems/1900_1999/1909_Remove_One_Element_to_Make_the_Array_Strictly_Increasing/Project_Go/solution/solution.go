package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func canBeIncreasing(nums []int) bool {
	// 4ms
	cnt := 0
	for i := 1; i < len(nums) && cnt < 2; i++ {
		if nums[i-1] >= nums[i] {
			cnt++
			if i > 1 && nums[i-2] >= nums[i] {
				nums[i] = nums[i-1]
			}
		}
	}
	return cnt < 2
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "[", "", -1)
	flds := strings.Replace(temp, "]", "", -1)

	nums := StringToIntArray(flds)
	fmt.Printf("nums = %s\n", IntArrayToString(nums))

	timeStart := time.Now()

	result := canBeIncreasing(nums)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", strconv.FormatBool(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
