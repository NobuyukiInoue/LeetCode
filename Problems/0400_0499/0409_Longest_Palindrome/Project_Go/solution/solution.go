package solution

import (
	"fmt"
	"strings"
	"time"
)

func longestPalindrome(s string) int {
	// 0ms
	count := make([]int, 256)
	l := 0
	for _, c := range s {
		count[c]++
	}
	for _, i := range count {
		l += i >> 1 << 1
	}
	if l == len(s) {
		return l
	} else {
		return l + 1
	}
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, ", ", ",", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	s := strings.Replace(temp, "]", "", -1)

	fmt.Printf("s = %s\n", s)
	timeStart := time.Now()

	result := longestPalindrome(s)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
