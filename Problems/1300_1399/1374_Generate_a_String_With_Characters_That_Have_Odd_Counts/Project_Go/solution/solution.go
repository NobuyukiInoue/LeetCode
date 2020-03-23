package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func generateTheString(n int) string {
	// 0ms
	if n%2 == 1 {
		return strings.Repeat("a", n)
	} else {
		return strings.Repeat("a", n-1) + "b"
	}
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	flds := strings.Replace(temp, "]", "", -1)

	n, _ := strconv.Atoi(flds)
	fmt.Printf("n = %d\n", n)

	timeStart := time.Now()

	result := generateTheString(n)

	timeEnd := time.Now()

	fmt.Printf("result = [%s]\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
