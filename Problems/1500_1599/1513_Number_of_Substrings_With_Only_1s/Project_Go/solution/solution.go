package solution

import (
	"fmt"
	"strings"
	"time"
)

func numSub(s string) int {
	// 5ms
	res, count, mod := 0, 0, int(1e9 + 7)
	for i := 0; i < len(s); i++ {
		if s[i] == '1' {
			count++
		} else {
			count = 0
		}
		res = (res + count)% mod
	}
	return res
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	s := strings.Replace(temp, "]", "", -1)
	fmt.Printf("s = %s\n", s)

	timeStart := time.Now()

	result := numSub(s)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
