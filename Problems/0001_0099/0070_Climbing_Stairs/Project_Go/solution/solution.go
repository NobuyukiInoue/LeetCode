package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func climbStairs(n int) int {
	// 1ms
	results := make([]int, n+1)
	results[0] = 0
	if n > 0 {
		results[1] = 1
	}
	if n > 1 {
		results[2] = 2
	}
	for i := 3; i <= n; i++ {
		results[i] = results[i-1] + results[i-2]
	}
	return results[n]
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	fld := strings.Replace(temp, "]", "", -1)

	n, _ := strconv.Atoi(fld)
	fmt.Printf("x = %d\n", n)

	timeStart := time.Now()

	result := climbStairs(n)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
