package solution

import (
	"fmt"
	"strings"
	"time"
)

func minimizedStringLength(s string) int {
	// 8ms - 11ms
	cnts := make(map[rune]bool, 0)
	for _, ch := range s {
		cnts[ch] = true
	}
	return len(cnts)
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	s := strings.Replace(temp, "]", "", -1)
	fmt.Printf("s = \"%s\"\n", s)

	timeStart := time.Now()

	result := minimizedStringLength(s)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
