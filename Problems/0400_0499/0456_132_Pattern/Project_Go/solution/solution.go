package solution

import (
	"fmt"
	"math"
	"strconv"
	"strings"
	"time"
)

func find132pattern(nums []int) bool {
	// 60ms
	max := -math.MaxInt32
	stack := make([]int, 0)
	for i := len(nums) - 1; i >= 0; i-- {
		if nums[i] < max {
			return true
		}
		for len(stack) > 0 && stack[len(stack)-1] < nums[i] {
			max = stack[len(stack)-1]
			stack = stack[:len(stack)-1]
		}
		stack = append(stack, nums[i])
	}
	return false
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "[", "", -1)
	flds := strings.Replace(temp, "]", "", -1)

	nums := StringToIntArray(flds)
	fmt.Printf("nums = %s\n", IntArrayToString(nums))

	timeStart := time.Now()

	result := find132pattern(nums)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", strconv.FormatBool(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
