package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func numSubarrayProductLessThanK(nums []int, k int) int {
	// 128ms
	if len(nums) == 0 || k <= 1 {
		return 0
	}

	count, prod, left, right := 0, 1, 0, 0

	for right < len(nums) {
		prod *= nums[right]
		for left <= right && prod >= k {
			prod /= nums[left]
			left++
		}
		count += right - left + 1
		right++
	}

	return count
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)
	flds := strings.Split(temp, "],[")

	nums := StringToIntArray(flds[0])
	k, _ := strconv.Atoi(flds[1])
	fmt.Printf("nums = [%s], k = %d\n", IntArrayToString(nums), k)

	timeStart := time.Now()

	result := numSubarrayProductLessThanK(nums, k)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
