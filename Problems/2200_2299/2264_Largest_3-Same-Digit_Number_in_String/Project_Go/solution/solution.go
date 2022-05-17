package solution

import (
	"fmt"
	"strings"
	"time"
)

func largestGoodInteger(num string) string {
	// 0ms
	ans := byte(0)
	for i := 2; i < len(num); i++ {
		if num[i] == num[i-1] && num[i] == num[i-2] {
			ans = myMax(ans, num[i])
		}
	}
	if ans == 0 {
		return ""
	}
	return string([]byte{ans, ans, ans})
}

func myMax(a byte, b byte) byte {
	if a > b {
		return a
	}
	return b
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	num := strings.Replace(temp, "]", "", -1)
	fmt.Printf("num = %s\n", num)

	timeStart := time.Now()

	result := largestGoodInteger(num)

	timeEnd := time.Now()

	fmt.Printf("result = \"%s\"\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
