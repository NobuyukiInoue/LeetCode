package solution

import (
	"fmt"
	"sort"
	"strings"
	"time"
)

func minimumAverage(nums []int) float64 {
	// 0ms
	sort.Sort(sort.IntSlice(nums))
	n := len(nums)
	ans := float64(nums[0]+nums[n-1]) / 2.0
	for i := 1; i < n/2+1; i++ {
		ans = myMin(ans, float64(nums[i]+nums[n-i-1])/2.0)
	}
	return ans
}

func myMin(a, b float64) float64 {
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

	result := minimumAverage(nums)

	timeEnd := time.Now()

	fmt.Printf("result = %f\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
