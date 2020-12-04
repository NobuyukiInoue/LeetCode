package solution

import (
	"fmt"
	"strings"
	"time"
)

func shortestPalindrome(s string) string {
	// 0ms
	if len(s) <= 1 {
		return s
	}

	new_s := s + "#" + reverse(s)
	position := make([]int, len(new_s))

	for i := 1; i < len(position); i++ {
		pre_pos := position[i-1]

		for pre_pos > 0 && new_s[pre_pos] != new_s[i] {
			pre_pos = position[pre_pos-1]
		}

		if new_s[pre_pos] == new_s[i] {
			position[i] = pre_pos + 1
		} else {
			position[i] = pre_pos
		}
	}

	return reverse(s[position[len(position)-1]:]) + s
}

func reverse(s string) string {
	rs := []rune(s)
	for i, j := 0, len(s)-1; i < j; i, j = i+1, j-1 {
		rs[i], rs[j] = rs[j], rs[i]
	}
	return string(rs)
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	s := strings.Replace(temp, "]", "", -1)
	fmt.Printf("s = %s\n", s)

	timeStart := time.Now()

	result := shortestPalindrome(s)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
