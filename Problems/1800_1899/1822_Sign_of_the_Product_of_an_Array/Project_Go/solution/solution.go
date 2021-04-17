package solution

import (
	"fmt"
	"strings"
	"time"
)

func arraySign(nums []int) int {
	// 4ms
	isPositive := 1
	for _, n := range(nums) {
		if n == 0 {
			return 0;
		} else if n < 0 {
			isPositive = -isPositive;
		}
	}
	return isPositive;
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "[", "", -1)
	flds := strings.Replace(temp, "]", "", -1)

	nums := StringToIntArray(flds)
	fmt.Printf("nums = %s\n", IntArrayToString(nums))

	timeStart := time.Now()

	result := arraySign(nums)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
