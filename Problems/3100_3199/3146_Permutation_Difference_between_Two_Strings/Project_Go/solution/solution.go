package solution

import (
	"fmt"
	"strings"
	"time"
)

func findPermutationDifference(s string, t string) int {
	// 0ms - 2ms
	ans := 0
	for i := 0; i < len(s); i++ {
		ch := string(s[i])
		ans += myAbs(strings.Index(s, ch) - strings.Index(t, ch))
	}
	return ans
}

func myAbs(n int) int {
	if n > 0 {
		return n
	}
	return -n
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, ", ", ",", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	temp = strings.Replace(temp, "]", "", -1)
	flds := strings.Split(temp, ",")

	s, t := flds[0], flds[1]
	fmt.Printf("s = \"%s\", t = \"%s\"\n", s, t)

	timeStart := time.Now()

	result := findPermutationDifference(s, t)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
