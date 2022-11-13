package solution

import (
	"fmt"
	"strings"
	"time"
)

func applyOperations(nums []int) []int {
	// 0ms - 4ms
	for i := 0; i < len(nums)-1; i++ {
		if nums[i] == nums[i+1] {
			nums[i] *= 2
			nums[i+1] = 0
		}
	}
	result := make([]int, len(nums))
	pos := 0
	for i := 0; i < len(result); i++ {
		if nums[i] != 0 {
			result[pos] = nums[i]
			pos++
		}
	}
	return result
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "[", "", -1)
	flds := strings.Replace(temp, "]", "", -1)

	nums := StringToIntArray(flds)
	fmt.Printf("nums = [%s]\n", IntArrayToString(nums))

	timeStart := time.Now()

	result := applyOperations(nums)

	timeEnd := time.Now()

	fmt.Printf("result = [%s]\n", IntArrayToString(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
