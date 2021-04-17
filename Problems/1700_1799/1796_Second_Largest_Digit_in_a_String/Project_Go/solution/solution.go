package solution

import (
	"fmt"
	"strings"
	"time"
)

func secondHighest(s string) int {
	// 0ms
	firstLargest, secondLargest := -1, -1
	for _, ch := range(s) {
		if '0' <= ch && ch <= '9' {
			d := int(ch - '0')
			if d > firstLargest {
				secondLargest = firstLargest
				firstLargest = d
			} else if d > secondLargest && d < firstLargest {
				secondLargest = d
			}
		}
	}
	return secondLargest
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	s := strings.Replace(temp, "]", "", -1)
	fmt.Printf("s = %s\n", s)

	timeStart := time.Now()

	result := secondHighest(s)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
