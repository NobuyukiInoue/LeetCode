package solution

import (
	"fmt"
	"strings"
	"time"
)

func secondsToRemoveOccurrences(s string) int {
	// 0ms
	ans, prefix, prev := 0, 0, 0
	for i := 0; i < len(s); i++ {
		if s[i] == '1' {
			ans = myMax(prev, i-prefix)
			prefix++
			if ans > 0 {
				prev = ans + 1
			}
		}
	}
	return ans
}

func myMax(a, b int) int {
	if a > b {
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

	result := secondsToRemoveOccurrences(s)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
