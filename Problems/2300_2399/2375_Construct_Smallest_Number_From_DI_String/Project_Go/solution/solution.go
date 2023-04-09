package solution

import (
	"fmt"
	"strings"
	"time"
)

func smallestNumber(pattern string) string {
	// 0ms
	stack, res := "", ""
	for i := 0; i <= len(pattern); i++ {
		stack += string('1' + byte(i))
		if i == len(pattern) || pattern[i] == 'I' {
			res += reverse_string(stack)
			stack = ""
		}
	}
	return res
}

func reverse_string(s string) string {
	runes := []rune(s)
	for i, j := 0, len(runes)-1; i < j; i, j = i+1, j-1 {
		runes[i], runes[j] = runes[j], runes[i]
	}
	return string(runes)
}

func smallestNumber2(pattern string) string {
	// 2ms
	stack, res := []byte{}, ""
	for i := 0; i <= len(pattern); i++ {
		stack = append(stack, '1'+byte(i))
		if i == len(pattern) || pattern[i] == 'I' {
			res += string(reverse_byte(stack))
			stack = make([]byte, 0)
		}
	}
	return res
}

func reverse_byte(arr []byte) []byte {
	res := []byte{}
	for i := len(arr) - 1; i >= 0; i-- {
		res = append(res, arr[i])
	}
	return res
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	pattern := strings.Replace(temp, "]", "", -1)
	fmt.Printf("pattern = %s\n", pattern)

	timeStart := time.Now()

	result := smallestNumber(pattern)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
