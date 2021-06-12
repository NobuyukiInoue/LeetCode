package solution

import (
	"fmt"
	"strings"
	"time"
)

func subsetXORSum(nums []int) int {
	// 0ms
	return sums(nums, 0, 0)
}

func sums(nums []int, term int, idx int) int {
	if idx == len(nums) {
		return term
	}
	return sums(nums, term, idx+1) + sums(nums, term^nums[idx], idx+1)
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "[", "", -1)
	flds := strings.Replace(temp, "]", "", -1)

	nums := StringToIntArray(flds)
	fmt.Printf("nums = %s\n", IntArrayToString(nums))

	timeStart := time.Now()

	result := subsetXORSum(nums)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
