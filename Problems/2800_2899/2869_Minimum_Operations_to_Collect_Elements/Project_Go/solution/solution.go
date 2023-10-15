package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func minOperations(nums []int, k int) int {
	// 0ms - 5ms
	left := int64((1 << k) - 1)
	n := len(nums)
	for i := n - 1; i >= 0; i-- {
		if nums[i] <= k && left&(1<<(nums[i]-1)) > 0 {
			left ^= 1 << (nums[i] - 1)
		}
		if left == 0 {
			return n - i
		}
	}
	return -1
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)
	flds := strings.Split(temp, "],[")

	nums := StringToIntArray(flds[0])
	k, _ := strconv.Atoi(flds[1])
	fmt.Printf("nums = [%s], k = %d\n", IntArrayToString(nums), k)

	timeStart := time.Now()

	result := minOperations(nums, k)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
