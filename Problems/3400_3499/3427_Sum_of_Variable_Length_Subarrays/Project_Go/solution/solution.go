package solution

import (
	"fmt"
	"strings"
	"time"
)

func subarraySum(nums []int) int {
	// 0ms
	ans := 0
	for i := 0; i < len(nums); i++ {
		ans += sum_subarray(nums, myMax(0, i-nums[i]), i)
	}
	return ans
}

func sum_subarray(arr []int, start, end int) int {
	v_sum := 0
	for i := start; i <= end; i++ {
		v_sum += arr[i]
	}
	return v_sum
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

	result := subarraySum(nums)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
