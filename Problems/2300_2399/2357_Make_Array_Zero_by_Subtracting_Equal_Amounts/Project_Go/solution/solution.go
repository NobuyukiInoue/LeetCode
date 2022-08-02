package solution

import (
	"fmt"
	"strings"
	"time"
)

func minimumOperations(nums []int) int {
	// 0ms
	elements := make(map[int]int)
	for _, n := range nums {
		if n > 0 {
			elements[n]++
		}
	}
	return len(elements)
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "[", "", -1)
	flds := strings.Replace(temp, "]", "", -1)

	nums := StringToIntArray(flds)
	fmt.Printf("nums = [%s]\n", IntArrayToString(nums))

	timeStart := time.Now()

	result := minimumOperations(nums)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
