package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func minSubArrayLen(s int, nums []int) int {
	// 4ms
	i, n := 0, len(nums)
	res := n + 1
	for j := 0; j < n; j++ {
		s -= nums[j]
		for s <= 0 {
			res = myMin(res, j-i+1)
			s += nums[i]
			i++
		}
	}
	return res % (n + 1)
}

func myMin(a int, b int) int {
	if a <= b {
		return a
	}
	return b
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)
	flds := strings.Split(temp, "],[")

	s, _ := strconv.Atoi(flds[0])
	nums := StringToIntArray(flds[1])

	fmt.Printf("s = %d, nums = %s\n", s, IntArrayToString(nums))

	timeStart := time.Now()

	result := minSubArrayLen(s, nums)
	fmt.Printf("result = %d\n", result)

	timeEnd := time.Now()

	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
