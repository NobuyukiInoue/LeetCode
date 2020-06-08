package solution

import (
	"fmt"
	"strings"
	"time"
)

func calculate(s string) int {
	// 0ms
	op, op2 := '+', '+'
	prefix, count, val := 0, 0, 0
	expr1 := false
	for _, c := range s {
		if '0' <= c && c <= '9' {
			count = count*10 + int(c) - '0'
		} else if c == ' ' {
			continue
		} else {
			if c == '/' || c == '*' {
				if op == '/' {
					count = val / count
				} else if op == '*' {
					count = val * count
				}
				val = count
				expr1 = true
			} else {
				if op == '+' {
					prefix += count
				} else if op == '-' {
					prefix -= count
				} else if op == '/' {
					if op2 == '+' {
						prefix += val / count
					} else {
						prefix -= val / count
					}
				} else if op == '*' {
					if op2 == '+' {
						prefix += val * count
					} else {
						prefix -= val * count
					}
				}
				val = 0
				op2 = c
				expr1 = false
			}
			count = 0
			op = c
		}
	}
	if expr1 {
		if op == '*' {
			count = val * count
		} else if op == '/' {
			count = val / count
		} else {
			count = 0
		}
	}
	if count > 0 {
		if op2 == '+' {
			prefix += count
		} else {
			prefix -= count
		}
	}

	return prefix
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	s := strings.Replace(temp, "]", "", -1)
	fmt.Printf("s = %s\n", s)

	timeStart := time.Now()

	result := calculate(s)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
