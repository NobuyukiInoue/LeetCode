package solution

import (
	"fmt"
	"strings"
	"time"
)

func finalString(s string) string {
	// 4ms - 11ms
	var ans []rune
	for _, ch := range s {
		if ch == 'i' {
			ans = reverse(ans)
		} else {
			ans = append(ans, ch)
		}
	}
	return string(ans)
}

func reverse(s []rune) []rune {
	runes := []rune(s)
	for i, j := 0, len(runes)-1; i < j; i, j = i+1, j-1 {
		runes[i], runes[j] = runes[j], runes[i]
	}
	return runes
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	s := strings.Replace(temp, "]", "", -1)
	fmt.Printf("s = \"%s\"\n", s)

	timeStart := time.Now()

	result := finalString(s)

	timeEnd := time.Now()

	fmt.Printf("result = \"%s\"\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
