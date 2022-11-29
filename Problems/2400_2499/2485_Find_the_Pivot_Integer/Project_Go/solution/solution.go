package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func pivotInteger(n int) int {
	// 0ms - 7ms
	l_sum, r_sum := 0, n*(n+1)/2
	for i := 1; i < n+1; i++ {
		r_sum -= i
		if l_sum == r_sum {
			return i
		}
		l_sum += i
	}
	return -1
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "[", "", -1)
	flds := strings.Replace(temp, "]", "", -1)

	n, _ := strconv.Atoi(flds)
	fmt.Printf("n = %d\n", n)

	timeStart := time.Now()

	result := pivotInteger(n)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
