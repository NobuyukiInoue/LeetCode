package solution

import (
	"fmt"
	"strings"
	"time"
)

func maximumLengthSubstring(s string) int {
	// 0ms
	ans, j := 0, 0
	var freq [26]int
	for i, ch := range s {
		freq[ch-'a']++
		for freq[ch-'a'] == 3 {
			freq[s[j]-'a']--
			j++
		}
		ans = myMax(ans, i-j+1)
	}
	return ans
}

func myMax(a, b int) int {
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
	fmt.Printf("s = \"%s\"\n", s)

	timeStart := time.Now()

	result := maximumLengthSubstring(s)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
