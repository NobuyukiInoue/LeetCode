package solution

import (
	"fmt"
	"strings"
	"time"
)

func findMaximumXOR(nums []int) int {
	// 92ms
	res := 0
	for i := 31; i >= 0; i-- {
		res <<= 1
		pre := make(map[int]bool)
		for _, n := range nums {
			pre[n >> i] = true
		}
		for p := range pre {
			if pre[res ^ 1 ^ p] {
				res += 1; break
			}
		}
	}
	return res
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	flds := strings.Replace(temp, "]", "", -1)

	nums := StringToIntArray(flds)
	fmt.Printf("nums = [%s]\n", IntArrayToString(nums))

	timeStart := time.Now()

	result := findMaximumXOR(nums)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
