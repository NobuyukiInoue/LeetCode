package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func isValid(S string) bool {
	// 6ms
	for strings.Contains(S, "abc") {
		S = strings.Replace(S, "abc", "", -1)
	}
	return S == ""
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	S := strings.Replace(temp, "]", "", -1)
	fmt.Printf("s = %s\n", S)

	timeStart := time.Now()

	result := isValid(S)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", strconv.FormatBool(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
