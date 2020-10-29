package solution

import (
	"fmt"
	"strings"
	"time"
)

func maxLengthBetweenEqualCharacters(s string) int {
	// 0ms
	maxLength := -1
	for _, ch := range(s) {
		chStr := string(ch)
		maxLength = myMax(maxLength, strings.LastIndex(s, chStr) - strings.Index(s, chStr) - 1)
	}
	return maxLength
}

func myMax(a int, b int) int {
	if a > b {
		return a
	}
	return b
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	s := strings.Replace(temp, "]", "", -1)
	fmt.Printf("s = %s\n", s)

	timeStart := time.Now()

	result := maxLengthBetweenEqualCharacters(s)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
