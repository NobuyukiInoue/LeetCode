package solution

import (
	"fmt"
	"strings"
	"time"
)

func numSteps(s string) int {
	// 0ms
	res, carry := 0, byte(0)
	for i := len(s) - 1; i > 0; i-- {
		res++
		if s[i]-'0'+carry == 1 {
			carry = 1
			res++
		}
	}
	return res + int(carry)
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	s := strings.Replace(temp, "]", "", -1)
	fmt.Printf("s = %s\n", s)

	timeStart := time.Now()

	result := numSteps(s)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
