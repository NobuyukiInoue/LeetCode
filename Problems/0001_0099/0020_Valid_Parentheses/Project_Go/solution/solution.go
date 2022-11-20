package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func isValid(s string) bool {
	// 0ms - 4ms
	stack := make([]rune, 0)
	for _, element := range s {
		if element == '(' || element == '[' || element == '{' {
			stack = append(stack, element)
			continue
		} else if len(stack) == 0 {
			return false
		}
		top := stack[len(stack)-1]
		stack = stack[:len(stack)-1]
		if top == '(' && element != ')' {
			return false
		} else if top == '[' && element != ']' {
			return false
		} else if top == '{' && element != '}' {
			return false
		}
	}
	return len(stack) == 0
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	s := strings.Replace(temp, "\"", "", -1)

	fmt.Printf("s = %s\n", s)

	timeStart := time.Now()

	result := isValid(s)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", strconv.FormatBool(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
