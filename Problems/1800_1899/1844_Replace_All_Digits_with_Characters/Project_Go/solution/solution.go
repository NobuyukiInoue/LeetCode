package solution

import (
	"fmt"
	"strings"
	"time"
)

func replaceDigits(s string) string {
	// 0ms
	res := make([]byte, len(s))
	for i := 0; i < len(s); i++ {
		if i%2 == 0 {
			res[i] = s[i]
		} else {
			res[i] = byte(s[i-1] + s[i] - '0')
		}
	}
	return string(res)
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	s := strings.Replace(temp, "]", "", -1)
	fmt.Printf("s = %s\n", s)

	timeStart := time.Now()

	result := replaceDigits(s)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
