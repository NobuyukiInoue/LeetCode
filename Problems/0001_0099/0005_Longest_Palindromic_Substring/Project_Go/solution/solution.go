package solution

import (
	"fmt"
	"strings"
	"time"
)

func longestPalindrome(s string) string {
	if len(s) < 2 {
		return s
	}
	max := string(s[0])
	for i := 0; i < len(s); i++ {
		max = checkPalindrome(s, i, i, max)
		max = checkPalindrome(s, i, i+1, max)
	}
	return max
}

func checkPalindrome(s string, i int, j int, max string) string {
	leng := len(s)
	var sub string
	for i >= 0 && j <= (leng-1) && s[i] == s[j] {
		sub = s[i : j+1]
		i--
		j++
	}
	if len(max) < len(sub) {
		max = sub
	}
	return max
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[", "", -1)

	s := strings.Replace(temp, "]", "", -1)
	fmt.Printf("s = %s\n", s)

	timeStart := time.Now()

	result := longestPalindrome(s)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
