package solution

import (
	"fmt"
	"strings"
	"time"
)

func maxFrequencyElements(nums []int) int {
	// 5ms
	cnts := make(map[int]int, 0)
	for _, num := range nums {
		cnts[num]++
	}
	max_cnts := 0
	for _, v := range cnts {
		max_cnts = myMax(max_cnts, v)
	}
	ans := 0
	for _, v := range cnts {
		if v == max_cnts {
			ans += v
		}
	}
	return ans
}

func myMax(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "[", "", -1)
	flds := strings.Replace(temp, "]", "", -1)

	nums := StringToIntArray(flds)
	fmt.Printf("nums = [%s]\n", IntArrayToString(nums))

	timeStart := time.Now()

	result := maxFrequencyElements(nums)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
