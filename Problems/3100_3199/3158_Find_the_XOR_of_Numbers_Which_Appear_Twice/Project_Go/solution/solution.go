package solution

import (
	"fmt"
	"strings"
	"time"
)

func duplicateNumbersXOR(nums []int) int {
	// 5ms - 7ms
	cnts := make(map[int]int, 0)
	for _, num := range nums {
		cnts[num]++
	}
	ans := 0
	for k, v := range cnts {
		if v == 2 {
			ans ^= k
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

	result := duplicateNumbersXOR(nums)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
