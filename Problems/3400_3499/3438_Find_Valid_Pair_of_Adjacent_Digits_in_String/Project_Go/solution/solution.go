package solution

import (
	"fmt"
	"strings"
	"time"
)

func findValidPair(s string) string {
	// 3ms - 4ms
	cnts := make(map[byte]int, 0)
	for i := 0; i < len(s); i++ {
		cnts[s[i]] += 1
	}
	for i := 0; i < len(s)-1; i++ {
		if s[i] != s[i+1] && cnts[s[i]] == int(s[i]-'0') && cnts[s[i+1]] == int(s[i+1]-'0') {
			return s[i : i+2]
		}
	}
	return ""
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	word := strings.Replace(temp, "]", "", -1)
	fmt.Printf("word = \"%s\"\n", word)

	timeStart := time.Now()

	result := findValidPair(word)

	timeEnd := time.Now()

	fmt.Printf("result = \"%s\"\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
