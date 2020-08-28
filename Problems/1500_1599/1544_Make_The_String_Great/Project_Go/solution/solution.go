package solution

import (
	"fmt"
	"strings"
	"time"
)

func makeGood(s string) string {
	// 0ms
	stack := []byte{}
	for i := 0; i < len(s); i++ {
		if len(stack) > 0 && myAbs(int(stack[len(stack)-1])-int(s[i])) == 32 {
			stack = stack[:len(stack)-1]
		} else {
			stack = append(stack, s[i])
		}
	}
	return string(stack)
}

func myAbs(n int) int {
	if n > 0 {
		return n
	}
	return -n
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	s := strings.Replace(temp, "]", "", -1)

	fmt.Printf("s = \"%s\"\n", s)

	timeStart := time.Now()

	result := makeGood(s)

	timeEnd := time.Now()

	fmt.Printf("result = \"%s\"\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
