package solution

import (
	"fmt"
	"strings"
	"time"
)

func longestNiceSubstring(s string) string {
	// 3ms
	if s == "" {
		return ""
	}
	ss := make(map[byte]int, 0)
	for i := 0; i < len(s); i++ {
		ss[s[i]] = 1
	}
	for i := 0; i < len(s); i++ {
		_, contains_upper := ss[toUpper(s[i])]
		_, contains_lower := ss[toLower(s[i])]
		if !contains_upper || !contains_lower {
			s0 := longestNiceSubstring(s[:i])
			s1 := longestNiceSubstring(s[i+1:])
			if len(s0) >= len(s1) {
				return s0
			}
			return s1
		}
	}
	return s
}

func toUpper(ch byte) byte {
	if 'a' <= ch && ch <= 'z' {
		return ch - ('a' - 'A')
	}
	return ch
}

func toLower(ch byte) byte {
	if 'A' <= ch && ch <= 'Z' {
		return ch + ('a' - 'A')
	}
	return ch
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	s := strings.Replace(temp, "]", "", -1)
	fmt.Printf("s = \"%s\"\n", s)

	timeStart := time.Now()

	result := longestNiceSubstring(s)

	timeEnd := time.Now()

	fmt.Printf("result = \"%s\"\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
