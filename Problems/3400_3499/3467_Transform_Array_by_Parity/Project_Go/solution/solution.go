package solution

import (
	"fmt"
	"strings"
	"time"
)

func transformArray(nums []int) []int {
	// 0ms
	cnt_odd, n := 0, len(nums)
	for _, num := range nums {
		if num%2 == 1 {
			cnt_odd++
		}
	}
	res := make([]int, n)
	for i := n - cnt_odd; i < n; i++ {
		res[i] = 1
	}
	return res
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "[", "", -1)
	flds := strings.Replace(temp, "]", "", -1)

	nums := StringToIntArray(flds)
	fmt.Printf("nums = [%s]\n", IntArrayToString(nums))

	timeStart := time.Now()

	result := transformArray(nums)

	timeEnd := time.Now()

	fmt.Printf("result = [%s]\n", IntArrayToString(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
