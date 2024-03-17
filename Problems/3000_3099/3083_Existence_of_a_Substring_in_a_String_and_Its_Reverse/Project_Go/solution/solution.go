package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func isSubstringPresent(s string) bool {
	// 0ms - 4ms
	r_s := []rune(s)
	for i, j := 0, len(s)-1; i < j; i, j = i+1, j-1 {
		r_s[i], r_s[j] = r_s[j], r_s[i]
	}
	for len(r_s) > 0 {
		if strings.Contains(s, string(r_s[:2])) {
			return true
		}
		r_s = r_s[1:]
	}
	return false
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	s := strings.Replace(temp, "]", "", -1)
	fmt.Printf("s = \"%s\"\n", s)

	timeStart := time.Now()

	result := isSubstringPresent(s)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", strconv.FormatBool(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
