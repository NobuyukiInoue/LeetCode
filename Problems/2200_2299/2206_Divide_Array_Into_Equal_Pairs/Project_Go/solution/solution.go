package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func divideArray(nums []int) bool {
	// 12ms
	pairSize := len(nums) / 2
	counts := make(map[int]int, 0)
	for _, num := range nums {
		counts[num]++
	}
	countPairs := 0
	for _, v := range counts {
		if v%2 == 1 {
			return false
		}
		countPairs += v / 2
	}
	return countPairs == pairSize
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "[", "", -1)
	flds := strings.Replace(temp, "]", "", -1)

	nums := StringToIntArray(flds)
	fmt.Printf("nums = [%s]\n", IntArrayToString(nums))

	timeStart := time.Now()

	result := divideArray(nums)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", strconv.FormatBool(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
