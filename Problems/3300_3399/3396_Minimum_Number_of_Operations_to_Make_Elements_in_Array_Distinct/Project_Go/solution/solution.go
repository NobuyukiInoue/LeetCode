package solution

import (
	"fmt"
	"strings"
	"time"
)

func minimumOperations(nums []int) int {
	// 0ms
	var cnts []int
	for i := len(nums) - 1; i >= 0; i-- {
		if contains(cnts, nums[i]) {
			return i/3 + 1
		}
		cnts = append(cnts, nums[i])
	}
	return 0
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

	result := minimumOperations(nums)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
