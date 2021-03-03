package solution

import (
	"fmt"
	"strings"
	"time"
)

func sumOfUnique(nums []int) int {
	// 0ms
	dic := map[int]int {}
	for _, num := range(nums) {
		dic[num]++
	}

	res := 0
	for k, v := range dic {
		if v == 1 {
			res += k
		}
	}

	return res
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "[", "", -1)
	flds := strings.Replace(temp, "]", "", -1)

	nums := StringToIntArray(flds)
	fmt.Printf("nums = %s\n", IntArrayToString(nums))

	timeStart := time.Now()

	result := sumOfUnique(nums)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
