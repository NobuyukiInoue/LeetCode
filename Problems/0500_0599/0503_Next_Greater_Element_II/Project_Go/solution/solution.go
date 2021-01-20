package solution

import (
	"fmt"
	"strings"
	"time"
)

func nextGreaterElements(nums []int) []int {
	// 20ms
	numsLen := len(nums)
	res := make([]int, numsLen)
	for i := 0; i < len(res); i++ {
		res[i] = -1
	}

	stack := make([]int, 0)
	for i := numsLen - 1; i >= 0; i-- {
		stack = append(stack, nums[i])
	}

	for i := numsLen - 1; i >= 0; i-- {
		for len(stack) > 0 && stack[len(stack)-1] <= nums[i] {
			stack = stack[:len(stack)-1]
		}
		if len(stack) > 0 {
			res[i] = stack[len(stack)-1]
		}
		stack = append(stack, nums[i])
	}
	return res
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	flds := strings.Replace(temp, "]", "", -1)

	nums := StringToIntArray(flds)
	fmt.Printf("nums = [%s]\n", IntArrayToString(nums))

	timeStart := time.Now()

	result := nextGreaterElements(nums)

	timeEnd := time.Now()

	fmt.Printf("result = [%s]\n", IntArrayToString(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
