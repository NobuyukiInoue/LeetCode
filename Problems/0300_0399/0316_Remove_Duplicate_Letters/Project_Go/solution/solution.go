package solution

import (
	"fmt"
	"strings"
	"time"
)

func removeDuplicateLetters(s string) string {
	lastInstanceOf := [26]int{}
	seen := [26]bool{}

	for i := range s {
		lastInstanceOf[s[i]-'a'] = i
	}

	var res []rune
	for i, r := range s {
		for len(res) > 0 {
			lastRune := res[len(res)-1]
			if r <= lastRune && lastInstanceOf[lastRune-'a'] >= i && !seen[r-'a'] {
				seen[lastRune-'a'] = false
				res = res[:len(res)-1]
				continue
			}
			break
		}

		if !seen[r-'a'] {
			res = append(res, r)
			seen[r-'a'] = true
		}
	}

	return string(res)
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	s := strings.Replace(temp, "]", "", -1)

	fmt.Printf("s = %s\n", s)
	timeStart := time.Now()

	result := removeDuplicateLetters(s)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
