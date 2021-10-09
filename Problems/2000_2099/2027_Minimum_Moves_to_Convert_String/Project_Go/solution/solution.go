package solution

import (
	"fmt"
	"strings"
	"time"
)

func minimumMoves(s string) int {
	// 0ms
	left, right := 0, len(s)
	ans := 0
	for left < right {
		if s[left] == 'X' {
			ans++
			left += 3
		} else {
			left++
		}
	}
	return ans
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	s := strings.Replace(temp, "]", "", -1)
	fmt.Printf("s = %s\n", s)

	timeStart := time.Now()

	result := minimumMoves(s)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
