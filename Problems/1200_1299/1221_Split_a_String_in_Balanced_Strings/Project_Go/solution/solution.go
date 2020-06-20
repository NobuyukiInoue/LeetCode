package solution

import (
	"fmt"
	"strings"
	"time"
)

func balancedStringSplit(s string) int {
	// 0ms
	res, cnt := 0, 0
	for i := 0; i < len(s); i++ {
		if s[i] == 'L' {
			cnt++
		} else {
			cnt--
		}
		if cnt == 0 {
			res++
		}
	}
	return res
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[", "", -1)

	s := strings.Replace(temp, "]", "", -1)
	fmt.Printf("s = %s\n", s)

	timeStart := time.Now()

	result := balancedStringSplit(s)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
