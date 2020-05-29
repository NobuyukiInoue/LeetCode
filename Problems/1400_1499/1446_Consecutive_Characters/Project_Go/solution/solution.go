package solution

import (
	"fmt"
	"strings"
	"time"
)

func maxPower(s string) int {
	// 0ms
	ch := s[0]
	countMax, count := 1, 1
	for i := 1; i < len(s); i++ {
		if s[i] == ch {
			count++
			if count > countMax {
				countMax = count
			}
		} else {
			ch = s[i]
			count = 1
		}
	}
	return countMax
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	s := strings.Replace(temp, "]", "", -1)
	fmt.Printf("s = %s\n", s)

	timeStart := time.Now()

	result := maxPower(s)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
