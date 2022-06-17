package solution

import (
	"fmt"
	"strings"
	"time"
)

func minMaxGame(nums []int) int {
	// 2ms - 5ms
	for len(nums) > 1 {
		arr := make([]int, len(nums)/2)
		for i := 0; i < len(arr); i++ {
			if i%2 == 0 {
				arr[i] = myMin(nums[2*i], nums[2*i+1])
			} else {
				arr[i] = myMax(nums[2*i], nums[2*i+1])
			}
		}
		nums = arr
	}
	return nums[0]
}

func myMin(a, b int) int {
	if a < b {
		return a
	}
	return b
}

func myMax(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "[", "", -1)
	flds := strings.Replace(temp, "]", "", -1)

	nums := StringToIntArray(flds)
	fmt.Printf("nums = [%s]\n", IntArrayToString(nums))

	timeStart := time.Now()

	result := minMaxGame(nums)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
