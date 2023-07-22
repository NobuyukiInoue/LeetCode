package solution

import (
	"fmt"
	"strings"
	"time"
)

func sumOfSquares(nums []int) int {
	// 7ms - 11ms
	ans, n := 0, len(nums)
	for i, num := range nums {
		if n%(i+1) == 0 {
			ans += num * num
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

	result := sumOfSquares(nums)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
