package solution

import (
	"fmt"
	"strings"
	"time"
)

func minBitFlips(start int, goal int) int {
	// 0ms - 4ms
	ans := 0
	for x := start ^ goal; x > 0; x >>= 1 {
		if x&1 == 1 {
			ans++
		}
	}
	return ans
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "[", "", -1)
	flds := strings.Replace(temp, "]", "", -1)

	nums := StringToIntArray(flds)
	start, goal := nums[0], nums[1]
	fmt.Printf("start = %d, goal = %d\n", start, goal)

	timeStart := time.Now()

	result := minBitFlips(start, goal)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
