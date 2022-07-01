package solution

import (
	"fmt"
	"strings"
	"time"
)

func countAsterisks(s string) int {
	// 4ms - 5ms
	cnt, bar := 0, 0
	for _, ch := range s {
		if ch == '|' {
			bar++
		}
		if bar%2 == 0 && ch == '*' {
			cnt++
		}
	}
	return cnt
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	s := strings.Replace(temp, "]", "", -1)
	fmt.Printf("s = \"%s\"\n", s)

	timeStart := time.Now()

	result := countAsterisks(s)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
