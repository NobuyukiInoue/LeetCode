package solution

import (
	"fmt"
	"strings"
	"time"
)

func minOperations(logs []string) int {
	// 0ms
	depth := 0
	for _, log := range logs {
		if log == "../" {
			if depth > 0 {
				depth--
			}
		} else if log != "./" {
			depth++
		}
	}
	return depth
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	temp = strings.Replace(temp, "]", "", -1)
	logs := strings.Split(temp, ",")
	fmt.Printf("logs = %s\n", logs)

	timeStart := time.Now()

	result := minOperations(logs)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
