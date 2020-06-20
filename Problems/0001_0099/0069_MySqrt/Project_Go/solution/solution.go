package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func mySqrt(x int) int {
	// 0ms
	if x == 0 {
		return 0
	}
	left, right, ans := 1, x, 0
	for left <= right {
		mid := left + (right-left)/2
		if mid <= x/mid {
			left = mid + 1
			ans = mid
		} else {
			right = mid - 1
		}
	}
	return ans
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	fld := strings.Replace(temp, "]", "", -1)

	n, _ := strconv.Atoi(fld)

	fmt.Printf("n = %d\n", n)
	timeStart := time.Now()

	result := mySqrt(n)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
