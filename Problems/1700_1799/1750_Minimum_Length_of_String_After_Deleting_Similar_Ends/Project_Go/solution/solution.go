package solution

import (
	"fmt"
	"strings"
	"time"
)

func minimumLength(s string) int {
	// 4ms - 11ms
	left, right := 0, len(s)-1
	for left < right {
		if s[left] != s[right] {
			break
		}
		ch := s[left]
		for s[left] == ch && left < right {
			left++
		}
		for s[right] == ch && left <= right {
			right--
		}
	}
	return right - left + 1
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	s := strings.Replace(temp, "]", "", -1)
	fmt.Printf("s = %s\n", s)

	timeStart := time.Now()

	result := minimumLength(s)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
