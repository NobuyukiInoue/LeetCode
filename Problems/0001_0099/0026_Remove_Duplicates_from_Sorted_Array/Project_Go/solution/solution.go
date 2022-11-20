package solution

import (
	"fmt"
	"strings"
	"time"
)

func removeDuplicates(nums []int) int {
	// 9ms - 15ms
	if len(nums) == 0 {
		return 0
	}
	n := 1
	for i := 1; i < len(nums); i++ {
		if nums[i] > nums[i-1] {
			nums[n] = nums[i]
			n++
		}
	}
	return n
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "[", "", -1)
	flds := strings.Replace(temp, "]", "", -1)

	nums := StringToIntArray(flds)
	fmt.Printf("nums = [%s]\n", IntArrayToString(nums))

	timeStart := time.Now()

	result := removeDuplicates(nums)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
