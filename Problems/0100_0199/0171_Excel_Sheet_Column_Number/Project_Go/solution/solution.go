package solution

import (
	"fmt"
	"strings"
	"time"
)

func titleToNumber(s string) int {
	number := 0
	for i, _ := range s {
		number *= 26
		number += int(s[i]) - 'A' + 1
	}
	return number
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	s := strings.Replace(temp, "]", "", -1)

	fmt.Printf("s = %s\n", s)

	timeStart := time.Now()

	result := titleToNumber(s)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
