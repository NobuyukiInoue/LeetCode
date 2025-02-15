package solution

import (
	"fmt"
	"strings"
	"time"
)

func minBitwiseArray(nums []int) []int {
	// 0ms - 6ms
	n := len(nums)
	ans := make([]int, n)
	for i, num := range nums {
		if num%2 == 0 {
			ans[i] = -1
		} else {
			ans[i] = num - ((num+1)&(-num-1))/2
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

	result := minBitwiseArray(nums)

	timeEnd := time.Now()

	fmt.Printf("result = [%s]\n", IntArrayToString(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
