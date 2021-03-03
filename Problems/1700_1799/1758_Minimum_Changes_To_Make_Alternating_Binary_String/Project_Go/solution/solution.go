package solution

import (
	"fmt"
	"strings"
	"time"
)

func minOperations(s string) int {
	// 0ms
	res, n := 0, len(s)
	for i := 0; i < n; i++ {
		if int(s[i] - '0') != i % 2 {
			res++
		}
	}
	return myMin(res, n - res)
}

func myMin(a int, b int) int {
	if a < b {
		return a
	}
	return b
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	s := strings.Replace(temp, "]", "", -1)
	fmt.Printf("s = %s\n", s)

	timeStart := time.Now()

	result := minOperations(s)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
