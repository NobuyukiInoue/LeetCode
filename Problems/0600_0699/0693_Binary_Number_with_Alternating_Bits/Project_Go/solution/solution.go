package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func hasAlternatingBits(n int) bool {
	targetStr := fmt.Sprintf("%b", n)
	//	fmt.Printf("targetStr = %s\n", targetStr)

	for i := 1; i < len(targetStr); i++ {
		if targetStr[i] == targetStr[i-1] {
			return false
		}
	}
	return true
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	flds := strings.Replace(temp, "]", "", -1)
	n, _ := strconv.Atoi(flds)

	fmt.Printf("n = %d\n", n)

	timeStart := time.Now()

	result := hasAlternatingBits(n)
	fmt.Printf("result = %s\n", strconv.FormatBool(result))

	timeEnd := time.Now()

	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
