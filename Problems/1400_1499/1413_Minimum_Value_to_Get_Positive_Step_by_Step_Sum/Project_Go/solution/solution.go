package solution

import (
	"fmt"
	"math"
	"strings"
	"time"
)

func minStartValue(nums []int) int {
	// 0ms
	total, totalMin := 0, math.MaxInt64
	for _, v := range nums {
		total += v
		if total < totalMin {
			totalMin = total
		}
	}

	if -totalMin+1 > 0 {
		return -totalMin + 1
	}
	return 1
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

	result := minStartValue(nums)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
