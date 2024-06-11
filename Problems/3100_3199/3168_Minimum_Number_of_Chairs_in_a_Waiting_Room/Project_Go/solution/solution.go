package solution

import (
	"fmt"
	"strings"
	"time"
)

func minimumChairs(s string) int {
	// 0ms
	ans, cnt := 0, 0
	for _, ch := range s {
		if ch == 'E' {
			cnt++
		} else {
			cnt--
		}
		ans = myMax(ans, cnt)
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

	result := minimumChairs(s)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
