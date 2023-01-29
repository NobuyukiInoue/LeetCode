package solution

import (
	"fmt"
	"strings"
	"time"
)

func differenceOfSum(nums []int) int {
	// 3ms - 11ms
	ele, dig := 0, 0
	for _, num := range nums {
		ele += num
		if num >= 10 {
			for num > 0 {
				dig += num % 10
				num /= 10
			}
		} else {
			dig += num
		}
	}
	return ele - dig
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "[", "", -1)
	flds := strings.Replace(temp, "]", "", -1)

	nums := StringToIntArray(flds)
	fmt.Printf("nums = [%s]\n", IntArrayToString(nums))

	timeStart := time.Now()

	result := differenceOfSum(nums)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
