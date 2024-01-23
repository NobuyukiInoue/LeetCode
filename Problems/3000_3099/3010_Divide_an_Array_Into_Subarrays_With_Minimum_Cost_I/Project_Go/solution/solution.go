package solution

import (
	"fmt"
	"math"
	"sort"
	"strings"
	"time"
)

func minimumCost(nums []int) int {
	// 4ms
	n, ans := len(nums), math.MaxInt32
	for i := 1; i < n-1; i++ {
		for j := 1; j < n-i; j++ {
			ans = myMin(ans, nums[0]+nums[i]+nums[i+j])
		}
	}
	return ans
}

func myMin(a, b int) int {
	if a < b {
		return a
	}
	return b
}

func minimumCost2(nums []int) int {
	// 4ms
	sort.Sort(sort.IntSlice(nums[1:]))
	return nums[0] + nums[1] + nums[2]
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "[", "", -1)
	flds := strings.Replace(temp, "]", "", -1)

	nums := StringToIntArray(flds)
	fmt.Printf("nums = [%s]\n", IntArrayToString(nums))

	timeStart := time.Now()

	result := minimumCost(nums)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
