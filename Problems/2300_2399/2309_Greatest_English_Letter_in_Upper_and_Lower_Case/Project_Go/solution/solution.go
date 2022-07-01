package solution

import (
	"fmt"
	"strings"
	"time"
)

func greatestLetter(s string) string {
	// 0ms
	for i := 26; i >= 0; i-- {
		capital := string(int('A' + i))
		small := string(int('a' + i))
		if strings.Index(s, small) != -1 && strings.Index(s, capital) != -1 {
			return "" + capital
		}
	}
	return ""
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	s := strings.Replace(temp, "]", "", -1)
	fmt.Printf("s = %s\n", s)

	timeStart := time.Now()

	result := greatestLetter(s)

	timeEnd := time.Now()

	fmt.Printf("result = \"%s\"\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
