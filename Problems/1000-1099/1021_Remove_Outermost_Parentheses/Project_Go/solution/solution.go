package solution

import (
	"fmt"
	"strings"
	"time"
)

func removeOuterParentheses(S string) string {
	res := make([]rune, 0)
	opened := 0
	for _, ch := range S {
		if ch == '(' {
			if opened != 0 {
				res = append(res, ch)
			}
			opened++
		} else if ch == ')' {
			opened--
			if opened != 0 {
				res = append(res, ch)
			}
		}
	}
	return string(res)
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, ", ", ",", -1)
	temp = strings.Replace(temp, "[", "", -1)
	S := strings.Replace(temp, "]", "", -1)

	fmt.Printf("S = %s\n", S)

	timeStart := time.Now()

	result := removeOuterParentheses(S)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
