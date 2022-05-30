package solution

import (
	"fmt"
	"strings"
	"time"
)

func tupleSameProduct(nums []int) int {
	// 160ms - 226ms
	ans := 0
	cnts := make(map[int]int, 0)
	for i := 0; i < len(nums)-1; i++ {
		for j := i + 1; j < len(nums); j++ {
			prod := nums[i] * nums[j]
			freq := cnts[prod]
			ans = ans + freq*8
			cnts[prod] = freq + 1
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

	result := tupleSameProduct(nums)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
