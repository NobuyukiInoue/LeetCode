package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func evalRPN(tokens []string) int {
	// 4ms
	var st []string
	for _, ch := range tokens {
		if ch == "+" {
			n := len(st) - 1
			b, _ := strconv.Atoi(st[n])
			a, _ := strconv.Atoi(st[n-1])
			st[n-1] = strconv.Itoa(a + b)
			st = st[:n]
		} else if ch == "-" {
			n := len(st) - 1
			b, _ := strconv.Atoi(st[n])
			a, _ := strconv.Atoi(st[n-1])
			st[n-1] = strconv.Itoa(a - b)
			st = st[:n]
		} else if ch == "*" {
			n := len(st) - 1
			b, _ := strconv.Atoi(st[n])
			a, _ := strconv.Atoi(st[n-1])
			st[n-1] = strconv.Itoa(a * b)
			st = st[:n]
		} else if ch == "/" {
			n := len(st) - 1
			b, _ := strconv.Atoi(st[n])
			a, _ := strconv.Atoi(st[n-1])
			st[n-1] = strconv.Itoa(a / b)
			st = st[:n]
		} else {
			st = append(st, ch)
		}
	}
	result, _ := strconv.Atoi(st[0])
	return result
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	temp = strings.Replace(temp, "]", "", -1)
	tokens := strings.Split(temp, ",")

	fmt.Printf("tokens = [")
	for i := 0; i < len(tokens); i++ {
		if i == 0 {
			fmt.Printf("%s", tokens[i])
		} else {
			fmt.Printf(",%s", tokens[i])
		}
	}
	fmt.Printf("]\n")

	timeStart := time.Now()

	result := evalRPN(tokens)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
