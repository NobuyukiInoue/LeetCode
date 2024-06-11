package solution

import (
	"fmt"
	"strings"
	"time"
)

func clearDigits(s string) string {
	// 0ms
	var ans []rune
	for _, ch := range s {
		if '0' <= ch && ch <= '9' {
			ans = ans[:len(ans)-1]
		} else {
			ans = append(ans, ch)
		}
	}
	return string(ans)
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	s := strings.Replace(temp, "]", "", -1)
	fmt.Printf("s = \"%s\"\n", s)

	timeStart := time.Now()

	result := clearDigits(s)

	timeEnd := time.Now()

	fmt.Printf("result = \"%s\"\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
