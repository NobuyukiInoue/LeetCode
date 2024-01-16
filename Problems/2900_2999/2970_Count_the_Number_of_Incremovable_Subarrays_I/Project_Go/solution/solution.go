package solution

import (
	"fmt"
	"strings"
	"time"
)

func incremovableSubarrayCount(nums []int) int {
	// 28ms - 32ms
	ans, n := 0, len(nums)
	for i := 0; i < n; i++ {
		for j := i; j < n; j++ {
			ok := true
			lst := -1

			for k := 0; k < n; k++ {
				if k >= i && k <= j {
					continue
				}
				if lst < nums[k] {
					ok = ok && true
				} else {
					ok = ok && false
				}
				lst = nums[k]
			}
			if ok {
				ans++
			}
		}
	}
	return ans
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "[", "", -1)
	flds := strings.Replace(temp, "]", "", -1)

	nums := StringToIntArray(flds)
	fmt.Printf("nums = [%s]\n", IntArrayToString(nums))

	timeStart := time.Now()

	result := incremovableSubarrayCount(nums)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
