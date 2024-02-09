package solution

import (
	"fmt"
	"strings"
	"time"
)

func countKeyChanges(s string) int {
	// 0ms - 4ms
	ans := 0
	for i := 1; i < len(s); i++ {
		val := myAbs(int(s[i]) - int(s[i-1]))
		if val == 0 || val == 0x20 {
			continue
		}
		ans++
	}
	return ans
}

func myAbs(n int) int {
	if n < 0 {
		return -n
	}
	return n
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	s := strings.Replace(temp, "]", "", -1)
	fmt.Printf("s = \"%s\"\n", s)

	timeStart := time.Now()

	result := countKeyChanges(s)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
