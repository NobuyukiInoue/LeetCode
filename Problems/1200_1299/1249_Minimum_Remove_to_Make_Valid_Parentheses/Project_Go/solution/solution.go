package solution

import (
	"fmt"
	"strings"
	"time"
)

func minRemoveToMakeValid(s string) string {
	// 12ms - 25ms
	res := make([]rune, 0)
	stack := make([]int, 0)
	for _, ch := range s {
		if ch == ')' {
			if len(stack) == 0 {
				continue
			} else {
				stack = stack[:len(stack)-1]
				res = append(res, ch)
			}
		} else if ch == '(' {
			stack = append(stack, len(res))
			res = append(res, ch)
		} else {
			res = append(res, ch)
		}
	}
	for len(stack) > 0 {
		pos := stack[len(stack)-1]
		res1 := res[:pos]
		res2 := res[pos+1:]
		res = append(res1, res2...)
		stack = stack[:len(stack)-1]
	}
	return string(res)
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	word := strings.Replace(temp, "]", "", -1)
	fmt.Printf("word = \"%s\"\n", word)

	timeStart := time.Now()

	result := minRemoveToMakeValid(word)

	timeEnd := time.Now()

	fmt.Printf("result = \"%s\"\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
