package solution

import (
	"fmt"
	"strings"
	"time"
)

func scoreOfString(s string) int {
	// 0ms
	ans := 0
	for i := 1; i < len(s); i++ {
		ans += myAbs(int(s[i]) - int(s[i-1]))
	}
	return ans
}

func myAbs(n int) int {
	if n >= 0 {
		return n
	}
	return -n
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	s := strings.Replace(temp, "]", "", -1)
	fmt.Printf("s = \"%s\"\n", s)

	timeStart := time.Now()

	result := scoreOfString(s)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
