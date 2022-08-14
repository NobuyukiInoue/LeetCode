package solution

import (
	"fmt"
	"strings"
	"time"
)

func maxValue(n int, index int, maxSum int) int {
	// 0ms - 6ms
	maxSum -= n
	left, right := 0, maxSum
	for left < right {
		mid := (left + right + 1) / 2
		if test(n, index, mid) <= int64(maxSum) {
			left = mid
		} else {
			right = mid - 1
		}
	}
	return left + 1
}

func test(n int, index int, a int) int64 {
	b := myMax(a-index, 0)
	res := int64(a+b) * int64(a-b+1) / int64(2)
	b = myMax(a-((n-1)-index), 0)
	res += int64(a+b) * int64(a-b+1) / int64(2)
	return res - int64(a)
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
	n, index, maxSum := nums[0], nums[1], nums[2]
	fmt.Printf("n = %d, index = %d, maxSum = %d\n", n, index, maxSum)

	timeStart := time.Now()

	result := maxValue(n, index, maxSum)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
