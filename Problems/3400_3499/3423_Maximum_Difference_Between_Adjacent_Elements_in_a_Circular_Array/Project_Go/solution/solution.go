package solution

import (
	"fmt"
	"strings"
	"time"
)

func maxAdjacentDistance(nums []int) int {
	// 0ms
	ans, n := 0, len(nums)
	for i, num := range nums {
		next_i := (i + 1) % n
		ans = myMax(ans, myAbs(num-nums[next_i]))
	}
	return ans
}

func myMax(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func myAbs(a int) int {
	if a >= 0 {
		return a
	}
	return -a
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "[", "", -1)
	flds := strings.Replace(temp, "]", "", -1)

	nums := StringToIntArray(flds)
	fmt.Printf("nums = [%s]\n", IntArrayToString(nums))

	timeStart := time.Now()

	result := maxAdjacentDistance(nums)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
