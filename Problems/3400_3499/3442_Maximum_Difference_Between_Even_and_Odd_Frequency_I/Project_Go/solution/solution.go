package solution

import (
	"fmt"
	"strings"
	"time"
)

func maxDifference(s string) int {
	// 0ms
	cnts := make(map[rune]int, 0)
	for _, ch := range s {
		cnts[ch] += 1
	}

	max_odd, min_even := 1, len(s)
	for _, cnt := range cnts {
		if cnt%2 == 1 {
			max_odd = myMax(max_odd, cnt)
		} else {
			min_even = myMin(min_even, cnt)
		}
	}
	return max_odd - min_even
}

func myMax(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func myMin(a, b int) int {
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
	fmt.Printf("s = \"%s\"\n", s)

	timeStart := time.Now()

	result := maxDifference(s)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
