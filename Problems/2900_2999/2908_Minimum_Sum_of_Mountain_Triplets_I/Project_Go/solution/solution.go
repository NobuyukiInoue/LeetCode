package solution

import (
	"fmt"
	"math"
	"strings"
	"time"
)

func minimumSum(nums []int) int {
	// 0ms
	ans, m := math.MaxInt, len(nums)
	for i := 0; i < m-2; i++ {
		for j := i + 1; j < m-1; j++ {
			if nums[i] < nums[j] {
				for k := j + 1; k < m; k++ {
					if nums[k] < nums[j] {
						ans = myMin(ans, nums[i]+nums[j]+nums[k])
					}
				}
			}
		}
	}
	if ans == math.MaxInt {
		return -1
	}
	return ans
}

func myMin(a, b int) int {
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

	result := minimumSum(nums)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
