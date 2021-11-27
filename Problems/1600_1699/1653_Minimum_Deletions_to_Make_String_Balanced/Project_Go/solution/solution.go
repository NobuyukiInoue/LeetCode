package solution

import (
	"fmt"
	"strings"
	"time"
)

func minimumDeletions(s string) int {
	// 34ms
	dp, count_b := 0, 0
	for _, ch := range s {
		if ch == 'a' {
			dp = myMin(dp+1, count_b)
		} else {
			count_b++
		}
	}
	return dp
}

func myMin(a int, b int) int {
	if a < b {
		return a
	}
	return b
}

func minimumDeletions_stack(s string) int {
	// 37ms
	var stack []rune
	count := 0
	for _, ch := range s {
		if ch == 'b' {
			stack = append(stack, ch)
		} else if len(stack) > 0 {
			stack = stack[:len(stack)-1]
			count++
		}
	}
	return count
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	s := strings.Replace(temp, "]", "", -1)
	fmt.Printf("s = %s\n", s)

	timeStart := time.Now()

	result := minimumDeletions(s)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
