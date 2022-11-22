package solution

import (
	"fmt"
	"strings"
	"time"
)

func unequalTriplets(nums []int) int {
	// 0ms - 2ms
	trips, pairs := 0, 0
	var cnts [1001]int
	for i, num := range nums {
		trips += pairs - cnts[num]*(i-cnts[num])
		pairs += i - cnts[num]
		cnts[num]++
	}
	return trips
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "[", "", -1)
	flds := strings.Replace(temp, "]", "", -1)

	nums := StringToIntArray(flds)
	fmt.Printf("nums = [%s]\n", IntArrayToString(nums))

	timeStart := time.Now()

	result := unequalTriplets(nums)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
