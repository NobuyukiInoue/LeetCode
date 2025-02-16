package solution

import (
	"fmt"
	"math"
	"strconv"
	"strings"
	"time"
)

func minimumSumSubarray(nums []int, l int, r int) int {
	// 0ms
	n := len(nums)
	min_sum := math.MaxInt32
	for length := l; length <= r; length++ {
		if length > n {
			continue
		}
		window_sum := mySum(nums, length)
		if window_sum > 0 {
			min_sum = myMin(min_sum, window_sum)
		}
		for i := length; i < n; i++ {
			window_sum += nums[i] - nums[i-length]
			if window_sum > 0 {
				min_sum = myMin(min_sum, window_sum)
			}
		}
	}
	if min_sum < math.MaxInt32 {
		return min_sum
	} else {
		return -1
	}
}

func mySum(nums []int, length int) int {
	v_sum := 0
	for i := 0; i < length; i++ {
		v_sum += nums[i]
	}
	return v_sum
}

func myMin(a, b int) int {
	if a < b {
		return a
	}
	return b
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)
	flds := strings.Split(temp, "],[")

	nums := StringToIntArray(flds[0])
	l, _ := strconv.Atoi(flds[1])
	r, _ := strconv.Atoi(flds[2])
	fmt.Printf("nums = [%s], l = %d, r = %d\n", IntArrayToString(nums), l, r)

	timeStart := time.Now()

	result := minimumSumSubarray(nums, l, r)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
