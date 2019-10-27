package solution

import (
	"fmt"
	"strings"
	"time"
)

func decodeString(s string) string {
	stackNums := make([]int, 0)
	stackStr := make([]string, 0)
	var res string
	var num int
	for i := 0; i < len(s); i++ {
		switch {
		case s[i] >= '0' && s[i] <= '9':
			num = 10*num + int(s[i]) - '0'
		case s[i] == '[':
			stackNums = append(stackNums, num)
			num = 0
			stackStr = append(stackStr, res)
			res = ""
		case s[i] == ']':
			tmp := stackStr[len(stackStr)-1]
			stackStr = stackStr[:len(stackStr)-1]
			count := stackNums[len(stackNums)-1]
			stackNums = stackNums[:len(stackNums)-1]
			res = tmp + strings.Repeat(res, count)
		default:
			res += string(s[i])
		}
	}
	return res
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "[\"", "", -1)
	s := strings.Replace(temp, "\"]", "", -1)

	fmt.Printf("s = %s\n", s)
	timeStart := time.Now()

	result := decodeString(s)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
