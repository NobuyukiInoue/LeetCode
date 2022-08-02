package solution

import (
	"fmt"
	"strings"
	"time"
)

func numberOfPairs(nums []int) []int {
	// 0ms - 5ms
	var cnts [101]int
	for _, num := range nums {
		cnts[num]++
	}
	pairs, leftover := 0, 0
	for _, cnt := range cnts {
		pairs += cnt / 2
		leftover += cnt % 2
	}
	return []int{pairs, leftover}
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "[", "", -1)
	flds := strings.Replace(temp, "]", "", -1)

	nums := StringToIntArray(flds)
	fmt.Printf("nums = [%s]\n", IntArrayToString(nums))

	timeStart := time.Now()

	result := numberOfPairs(nums)

	timeEnd := time.Now()

	fmt.Printf("result = [%s]\n", IntArrayToString(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
