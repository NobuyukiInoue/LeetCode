package solution

import (
	"fmt"
	"strings"
	"time"
)

func constructTransformedArray(nums []int) []int {
	// 3ms - 5ms
	n := len(nums)
	ans := make([]int, n)
	for i, step := range nums {
		ans[i] = nums[(i+step%n+n)%n]
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

	result := constructTransformedArray(nums)

	timeEnd := time.Now()

	fmt.Printf("result = [%s]\n", IntArrayToString(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
