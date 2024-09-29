package solution

import (
	"fmt"
	"math"
	"strings"
	"time"
)

func minElement(nums []int) int {
	// 0ms - 6ms
	ans := math.MaxInt32
	for _, num := range nums {
		v_sum := 0
		for num > 0 {
			v_sum += num % 10
			num /= 10
		}
		ans = myMin(ans, v_sum)
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

	result := minElement(nums)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
