package solution

import (
	"fmt"
	"strings"
	"time"
)

func maximumStrongPairXor(nums []int) int {
	// 4ms
	n, ans := len(nums), 0
	for i, x := range nums {
		for j := i; j < n; j++ {
			y := nums[j]
			if myAbs(x-y) <= myMin(x, y) {
				ans = myMax(ans, x^y)
			}
		}
	}
	return ans
}

func myAbs(n int) int {
	if n >= 0 {
		return n
	}
	return -n
}

func myMax(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func myMin(a, b int) int {
	if a < b {
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

	result := maximumStrongPairXor(nums)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
