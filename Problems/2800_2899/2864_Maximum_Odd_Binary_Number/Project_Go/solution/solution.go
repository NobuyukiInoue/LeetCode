package solution

import (
	"fmt"
	"strings"
	"time"
)

func maximumOddBinaryNumber(s string) string {
	// 0ms - 6ms
	len_s, oneCount := len(s), 0
	for i := 0; i < len_s; i++ {
		if s[i] == '1' {
			oneCount++
		}
	}
	return strings.Repeat("1", oneCount-1) + strings.Repeat("0", len_s-oneCount) + "1"
}

func maximumOddBinaryNumber2(s string) string {
	// 7ms
	len_s, oneCount, ans := len(s), -1, ""
	for i := 0; i < len_s; i++ {
		if s[i] == '1' {
			oneCount++
		}
	}
	for i := 0; i < len_s; i++ {
		if oneCount > 0 {
			ans += "1"
		} else {
			ans += "0"
		}
		oneCount--
	}
	ans = ans[0 : len_s-1]
	return ans + "1"
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	s := strings.Replace(temp, "]", "", -1)
	fmt.Printf("s = \"%s\"\n", s)

	timeStart := time.Now()

	result := maximumOddBinaryNumber(s)

	timeEnd := time.Now()

	fmt.Printf("result = \"%s\"\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
