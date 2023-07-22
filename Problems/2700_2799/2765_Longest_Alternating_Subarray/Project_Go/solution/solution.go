package solution

import (
	"fmt"
	"strings"
	"time"
)

func alternatingSubarray(nums []int) int {
	// 0ms
	res, n := 0, len(nums)
	for i, _ := range nums {
		for j := i + 1; j < n; j++ {
			if nums[j] != nums[i]+(j-i)%2 {
				break
			}
			res = myMax(res, j-i+1)
		}
	}
	if res > 1 {
		return res
	}
	return -1
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

	result := alternatingSubarray(nums)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
