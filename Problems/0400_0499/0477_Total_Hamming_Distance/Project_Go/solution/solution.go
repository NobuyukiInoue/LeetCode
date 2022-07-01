package solution

import (
	"fmt"
	"strings"
	"time"
)

func totalHammingDistance(nums []int) int {
	// 27ms - 40ms
	ans := 0
	for current_bit := 0; current_bit < 32; current_bit++ {
		counter := 0
		for _, num := range nums {
			counter += ((num >> current_bit) & 1)
		}
		ans += counter * (len(nums) - counter)
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

	result := totalHammingDistance(nums)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
