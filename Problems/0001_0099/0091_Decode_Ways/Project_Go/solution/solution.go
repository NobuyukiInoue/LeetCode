package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func numDecodings(s string) int {
	// 0ms
	if len(s) == 0 || s[0] == '0' {
		return 0
	}

	lenS := len(s)
	results := make([]int, lenS+1)
	results[0], results[1] = 1, 1

	for i := 2; i <= lenS; i++ {
		first, _ := strconv.Atoi(s[i-1 : i])
		second, _ := strconv.Atoi(s[i-2 : i])

		if first >= 1 && first <= 9 {
			results[i] += results[i-1]
		}
		if second >= 10 && second <= 26 {
			results[i] += results[i-2]
		}
	}
	return results[lenS]
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	s := strings.Replace(temp, "]", "", -1)

	fmt.Printf("s = [%s]\n", s)
	timeStart := time.Now()

	result := numDecodings(s)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
