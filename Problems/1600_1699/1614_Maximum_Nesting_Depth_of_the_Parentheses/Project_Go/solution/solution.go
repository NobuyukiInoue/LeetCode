package solution

import (
	"fmt"
	"strings"
	"time"
)

func maxDepth(s string) int {
	// 0ms
	depth, max_depth := 0, 0
	for _, ch := range(s) {
		if ch == '(' {
			depth++
			if depth > max_depth {
				max_depth = depth
			}
		} else if ch == ')' {
			depth--
		}
	}
	return max_depth
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	s := strings.Replace(temp, "]", "", -1)
	fmt.Printf("s = %s\n", s)

	timeStart := time.Now()

	result := maxDepth(s)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
