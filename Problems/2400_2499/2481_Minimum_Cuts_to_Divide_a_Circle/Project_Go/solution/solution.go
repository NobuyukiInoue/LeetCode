package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func numberOfCuts(n int) int {
	// 0ms
	if n == 1 {
		return 0
	}
	if n%2 > 0 {
		return n
	}
	return n / 2
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "[", "", -1)
	flds := strings.Replace(temp, "]", "", -1)

	n, _ := strconv.Atoi(flds)
	fmt.Printf("n = %d\n", n)

	timeStart := time.Now()

	result := numberOfCuts(n)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
