package solution

import (
	"fmt"
	"strings"
	"time"
)

func maximumCount(nums []int) int {
	// 18ms - 19ms
	pos, neg := 0, 0
	for _, n := range nums {
		if n > 0 {
			pos++
		} else if n < 0 {
			neg++
		}
	}
	return myMax(pos, neg)
}

func myMax(a, b int) int {
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
	fmt.Printf("nums = [%s]\n", IntArrayToString(nums))

	timeStart := time.Now()

	result := maximumCount(nums)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
