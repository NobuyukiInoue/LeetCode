package solution

import (
	"fmt"
	"strings"
	"time"
)

func lengthOfLastWord(s string) int {
	// 2ms
	s = strings.Trim(s, " ")
	i := len(s) - 1
	for i >= 0 && s[i] != ' ' {
		i--
	}
	return len(s) - 1 - i
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	s := strings.Replace(temp, "]", "", -1)

	fmt.Printf("s = %s\n", s)

	timeStart := time.Now()

	result := lengthOfLastWord(s)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
