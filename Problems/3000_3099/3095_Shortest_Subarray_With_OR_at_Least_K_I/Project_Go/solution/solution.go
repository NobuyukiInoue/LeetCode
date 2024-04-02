package solution

import (
	"fmt"
	"math"
	"strconv"
	"strings"
	"time"
)

func minimumSubarrayLength(nums []int, k int) int {
	// 0ms
	n, res := len(nums), math.MaxInt32
	for i := 0; i < n; i++ {
		for j := i; j < n; j++ {
			bitwise := 0
			for p := i; p <= j; p++ {
				bitwise |= nums[p]
			}
			if bitwise >= k {
				res = myMin(res, j-i+1)
			}
		}
	}
	if res == math.MaxInt32 {
		return -1
	}
	return res
}

func myMin(a, b int) int {
	if a < b {
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

	nums := StringToIntArray(flds[0])
	k, _ := strconv.Atoi(flds[1])
	fmt.Printf("nums = %s, k = %d\n", IntArrayToString(nums), k)

	timeStart := time.Now()

	result := minimumSubarrayLength(nums, k)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
