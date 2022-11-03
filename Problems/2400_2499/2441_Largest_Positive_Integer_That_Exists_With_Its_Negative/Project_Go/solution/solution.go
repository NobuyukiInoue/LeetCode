package solution

import (
	"fmt"
	"sort"
	"strings"
	"time"
)

func findMaxK(nums []int) int {
	// 35ms - 50ms
	sort.Sort(sort.IntSlice(nums))
	for i := len(nums) - 1; i >= 0; i-- {
		if contains(nums, -nums[i]) {
			return nums[i]
		}
	}
	return -1
}

func contains(nums []int, target int) bool {
	for _, num := range nums {
		if num == target {
			return true
		}
	}
	return false
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "[", "", -1)
	flds := strings.Replace(temp, "]", "", -1)

	nums := StringToIntArray(flds)
	fmt.Printf("nums = [%s]\n", IntArrayToString(nums))

	timeStart := time.Now()

	result := findMaxK(nums)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
