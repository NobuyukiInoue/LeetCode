package solution

import (
	"fmt"
	"math"
	"strings"
	"time"
)

func countElements(nums []int) int {
	// 3ms
	v_min, v_max := math.MaxInt64, math.MinInt64
	for _, num := range nums {
		v_min = myMin(v_min, num)
		v_max = myMax(v_max, num)
	}
	res := 0
	for _, num := range nums {
		if v_min < num && num < v_max {
			res++
		}
	}
	return res
}

func myMin(a int, b int) int {
	if a < b {
		return a
	}
	return b
}

func myMax(a int, b int) int {
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
	fmt.Printf("nums = %s\n", IntArrayToString(nums))

	timeStart := time.Now()

	result := countElements(nums)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
