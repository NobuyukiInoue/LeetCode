package solution

import (
	"fmt"
	"strings"
	"time"
)

func findClosestNumber(nums []int) int {
	// 12ms - 16ms
	min_v := []int{myAbs(nums[0]), nums[0]}
	for i := 1; i < len(nums); i++ {
		if myAbs(nums[i]) < min_v[0] {
			min_v[0] = myAbs(nums[i])
			min_v[1] = nums[i]
		} else if myAbs(nums[i]) == min_v[0] {
			min_v[1] = myMax(min_v[1], nums[i])
		}
	}
	return min_v[1]
}

func myAbs(n int) int {
	if n >= 0 {
		return n
	}
	return -n
}

func myMax(a, b int) int {
	if a >= b {
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

	result := findClosestNumber(nums)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
