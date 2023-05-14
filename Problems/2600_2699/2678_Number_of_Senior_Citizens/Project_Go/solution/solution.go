package solution

import (
	"fmt"
	"strings"
	"time"
)

func countSeniors(details []string) int {
	// 3ms - 6ms
	ans := 0
	for _, detail := range details {
		age := (detail[11]-'0')*10 + (detail[12] - '0')
		if age > 60 {
			ans++
		}
	}
	return ans
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	temp = strings.Replace(temp, "]", "", -1)
	details := strings.Split(temp, ",")

	fmt.Printf("details = %s\n", StringArrayToString(details))

	timeStart := time.Now()

	result := countSeniors(details)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
