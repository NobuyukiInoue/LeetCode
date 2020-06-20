package solution

import (
	"fmt"
	"sort"
	"strings"
	"time"
)

func minSubsequence(nums []int) []int {
	// 4ms
	sort.Sort(sort.IntSlice(nums))

	n := len(nums)
	ans, sum := 0, 0
	res := make([]int, 0)

	for i := 0; i < n; i++ {
		sum += nums[i]
	}

	for i := n - 1; i >= 0; i-- {
		ans += nums[i]
		res = append(res, nums[i])
		if ans > sum-ans {
			return res
		}
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

	result := minSubsequence(nums)

	timeEnd := time.Now()

	fmt.Printf("result = [%s]\n", IntArrayToString(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
