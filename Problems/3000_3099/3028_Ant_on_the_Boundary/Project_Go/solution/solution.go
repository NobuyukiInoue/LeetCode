package solution

import (
	"fmt"
	"strings"
	"time"
)

func returnToBoundaryCount(nums []int) int {
	// 0ms
	ans, pos := 0, 0
	for _, num := range nums {
		pos += num
		if pos == 0 {
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
	fmt.Printf("nums = [%s]\n", IntArrayToString(nums))

	timeStart := time.Now()

	result := returnToBoundaryCount(nums)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
