package solution

import (
	"fmt"
	"math"
	"strings"
	"time"
)

func maxProductDifference(nums []int) int {
	// 24ms
	max1, max2 := math.MinInt64, math.MinInt64
	min1, min2 := math.MaxInt64, math.MaxInt64
	for _, n := range nums {
		if n > max1 {
			max2, max1 = max1, n
		} else if n > max2 {
			max2 = n
		}
		if n < min1 {
			min2, min1 = min1, n
		} else if n < min2 {
			min2 = n
		}
	}
	return max1*max2 - min1*min2
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "[", "", -1)
	flds := strings.Replace(temp, "]", "", -1)

	nums := StringToIntArray(flds)
	fmt.Printf("nums = %s\n", IntArrayToString(nums))

	timeStart := time.Now()

	result := maxProductDifference(nums)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
