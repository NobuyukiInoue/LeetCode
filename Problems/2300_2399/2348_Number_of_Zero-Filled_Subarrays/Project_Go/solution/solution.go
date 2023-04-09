package solution

import (
	"fmt"
	"strings"
	"time"
)

func zeroFilledSubarray(nums []int) int64 {
	// 140ms - 146ms
	ans, j := int64(0), -1
	for i, num := range nums {
		if num != 0 {
			j = i
		} else {
			ans += int64(i - j)
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

	result := zeroFilledSubarray(nums)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
