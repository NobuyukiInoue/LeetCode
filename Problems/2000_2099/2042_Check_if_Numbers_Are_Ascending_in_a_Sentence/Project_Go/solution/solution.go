package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func areNumbersAscending(s string) bool {
	// 0ms
	prev := -1
	var cur int
	for _, ch := range s {
		if ch >= '0' && ch <= '9' {
			cur *= 10
			cur += int(ch - '0')
			continue
		}
		if cur != 0 {
			if cur <= prev {
				return false
			}
			prev = cur
			cur = 0
		}
	}
	return cur == 0 || prev < cur
}

func areNumbersAscending2(s string) bool {
	// 0ms
	words := strings.Split(s, " ")
	prev := -1
	for _, word := range words {
		if val, err := strconv.Atoi(word); err == nil {
			if val <= prev {
				return false
			}
			prev = val
		}
	}
	return true
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	s := strings.Replace(temp, "]", "", -1)
	fmt.Printf("s = %s\n", s)

	timeStart := time.Now()

	result := areNumbersAscending(s)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", strconv.FormatBool(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
