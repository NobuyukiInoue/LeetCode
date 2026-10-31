package solution

import (
	"fmt"
	"strings"
	"time"
)

func dominantIndices(nums []int) int {
	// 1ms
	n := len(nums)
	res, total := 0, 0
	for i := 0; i < n; i++ {
		count := i
		num := nums[n-1-i]
		if num*count > total {
			res++
		}
		total += num
	}
	return res
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "[", "", -1)
	flds := strings.Replace(temp, "]", "", -1)

	nums := StringToIntArray(flds)
	fmt.Printf("nums = [%s]\n", IntArrayToString(nums))

	timeStart := time.Now()

	result := dominantIndices(nums)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
