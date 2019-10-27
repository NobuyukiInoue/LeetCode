package solution

import (
	"fmt"
	"strings"
	"time"
)

var result []string

func removeInvalidParentheses(s string) []string {
	// 0ms
	result = []string{}
	braces := []byte{'(', ')'}
	dfs(s, braces, 0, 0)

	return result
}

func Reverse(s string) (result string) {
	for _, v := range s {
		result = string(v) + result
	}
	return
}

func dfs(s string, braces []byte, lastI, lastJ int) {
	count := 0
	i := lastI
	for i < len(s) && count >= 0 {
		if s[i] == braces[0] {
			count++
		} else if s[i] == braces[1] {
			count--
		}
		i++
	}

	if count >= 0 {
		reversed := Reverse(s)
		if braces[0] == '(' {
			dfs(reversed, []byte{braces[1], braces[0]}, 0, 0)
		} else {
			result = append(result, reversed)
		}
	} else {
		i -= 1
		for j := lastJ; j <= i; j++ {
			if s[j] == braces[1] && (j == lastJ || s[j-1] != braces[1]) {
				dfs(s[0:j]+s[j+1:], braces, i, j)
			}
		}
	}
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	s := strings.Replace(temp, "]", "", -1)

	fmt.Printf("s = %s\n", s)
	timeStart := time.Now()

	result := removeInvalidParentheses(s)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
