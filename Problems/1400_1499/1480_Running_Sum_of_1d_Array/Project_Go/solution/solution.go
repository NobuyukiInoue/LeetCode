package solution

import (
	"fmt"
	"strings"
	"time"
)

func runningSum(nums []int) []int {
	// 4ms
	numsLen := len(nums)
	res := make([]int, numsLen)
	res[0] = nums[0]
	for i := 1; i < numsLen; i++ {
		res[i] = res[i-1] + nums[i]
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

	result := runningSum(nums)

	timeEnd := time.Now()

	fmt.Printf("result = [%s]\n", IntArrayToString(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
