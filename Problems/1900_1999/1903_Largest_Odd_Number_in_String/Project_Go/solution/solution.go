package solution

import (
	"fmt"
	"strings"
	"time"
)

func largestOddNumber(num string) string {
	// 4ms
	for i := len(num) - 1; i >= 0; i-- {
		if num[i]%2 == 1 {
			return num[:i+1]
		}
	}
	return ""
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	num := strings.Replace(temp, "]", "", -1)
	fmt.Printf("num = %s\n", num)

	timeStart := time.Now()

	result := largestOddNumber(num)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
