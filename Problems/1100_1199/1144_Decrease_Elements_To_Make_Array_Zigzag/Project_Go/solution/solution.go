package solution

import (
	"fmt"
	"math"
	"strings"
	"time"
)

func movesToMakeZigzag(nums []int) int {
	// 0ms
	var res [2]int
	var left, right int
	for i, _ := range nums {
		if i > 0 {
			left = nums[i-1]
		} else {
			left = math.MaxInt64
		}
		if i+1 < len(nums) {
			right = nums[i+1]
		} else {
			right = math.MaxInt64
		}
		res[i%2] += myMax(0, nums[i]-myMin(left, right)+1)
	}
	return myMin(res[0], res[1])
}

func myMax(a int, b int) int {
	if a > b {
		return a
	}
	return b
}

func myMin(a int, b int) int {
	if a < b {
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

	result := movesToMakeZigzag(nums)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
