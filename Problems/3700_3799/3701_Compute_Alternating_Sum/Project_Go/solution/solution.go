package solution

import (
	"fmt"
	"strings"
	"time"
)

func alternatingSum(nums []int) int {
	// 0ms - 1ms
	ans := 0
	for i, num := range nums {
		if i%2 == 0 {
			ans += num
		} else {
			ans -= num
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

	result := alternatingSum(nums)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
