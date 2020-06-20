package solution

import (
	"fmt"
	"strings"
	"time"
)

func freqAlphabets(s string) string {
	// 0ms
	sb := ""
	for i := 0; i < len(s); i++ {
		if i < len(s)-2 && s[i+2] == '#' {
			n := (s[i]-'0')*10 + (s[i+1] - '0')
			sb += (string)('j' + n - 10)
			i += 2
		} else {
			sb += (string)('a' + s[i] - '1')
		}
	}
	return sb
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	s := strings.Replace(temp, "]", "", -1)

	fmt.Printf("s = %s\n", s)
	timeStart := time.Now()

	result := freqAlphabets(s)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
