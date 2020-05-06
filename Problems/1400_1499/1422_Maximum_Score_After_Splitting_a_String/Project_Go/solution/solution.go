package solution

import (
	"fmt"
	"strings"
	"time"
)

func maxScore(s string) int {
	// 0ms
	zeroCount, oneCount, max := 0, 0, 0

	for i := 0; i < len(s); i++ {
		if s[i] == '1' {
			oneCount++
		}
	}

	for i := 0; i < len(s)-1; i++ {
		if s[i] == '0' {
			zeroCount++
		} else {
			oneCount--
		}
		if zeroCount+oneCount > max {
			max = zeroCount + oneCount
		}
	}

	return max
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	s := strings.Replace(temp, "]", "", -1)

	fmt.Printf("s = [%s]\n", s)
	timeStart := time.Now()

	result := maxScore(s)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
