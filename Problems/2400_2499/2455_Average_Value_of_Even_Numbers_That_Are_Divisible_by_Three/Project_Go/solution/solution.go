package solution

import (
	"fmt"
	"strings"
	"time"
)

func averageValue(nums []int) int {
	// 17ms - 23ms
	count, total := 0, 0
	for _, num := range nums {
		if num%6 == 0 {
			total += num
			count++
		}
	}
	if count > 0 {
		return total / count
	}
	return 0
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "[", "", -1)
	flds := strings.Replace(temp, "]", "", -1)

	nums := StringToIntArray(flds)
	fmt.Printf("nums = [%s]\n", IntArrayToString(nums))

	timeStart := time.Now()

	result := averageValue(nums)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
