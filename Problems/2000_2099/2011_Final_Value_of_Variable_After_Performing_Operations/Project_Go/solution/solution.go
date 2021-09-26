package solution

import (
	"fmt"
	"strings"
	"time"
)

func finalValueAfterOperations(operations []string) int {
	// 4ms
	ans := 0
	for _, op := range operations {
		if op[1] == '+' {
			ans++
		} else {
			ans--
		}
	}
	return ans
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	temp = strings.Replace(temp, "]", "", -1)
	operations := strings.Split(temp, ",")
	fmt.Printf("operations = %s\n", operations)

	timeStart := time.Now()

	result := finalValueAfterOperations(operations)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
