package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func sumOfGoodNumbers(nums []int, k int) int {
	// 0ms
	ans, n := 0, len(nums)
	for i := 0; i < n; i++ {
		if i+k < n {
			if nums[i] <= nums[i+k] {
				continue
			}
		}
		if 0 <= i-k {
			if nums[i] <= nums[i-k] {
				continue
			}
		}
		ans += nums[i]
	}
	return ans
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

	result := sumOfGoodNumbers(nums, k)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
