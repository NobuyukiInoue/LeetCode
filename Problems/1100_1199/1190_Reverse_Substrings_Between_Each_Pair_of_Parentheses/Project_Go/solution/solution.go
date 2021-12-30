package solution

import (
	"fmt"
	"strings"
	"time"
)

func reverseParentheses(s string) string {
	// 0ms
	n := len(s)
	opened := make([]int, 0)
	pair := make([]int, n)
	for i := 0; i < n; i++ {
		if s[i] == '(' {
			opened = append(opened, i)
		}
		if s[i] == ')' {
			j := opened[len(opened)-1]
			opened = opened[0 : len(opened)-1]
			pair[i] = j
			pair[j] = i
		}
	}
	ans := ""
	d := 1
	for i := 0; i < n; i += d {
		if s[i] == '(' || s[i] == ')' {
			i = pair[i]
			d = -d
		} else {
			ans = ans + string(s[i])
		}
	}
	return ans
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	s := strings.Replace(temp, "]", "", -1)
	fmt.Printf("s = %s\n", s)

	timeStart := time.Now()

	result := reverseParentheses(s)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
