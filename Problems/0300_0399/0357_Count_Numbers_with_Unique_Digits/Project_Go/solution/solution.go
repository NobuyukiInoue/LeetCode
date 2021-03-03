package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func countNumbersWithUniqueDigits(n int) int {
	// 0ms
	if n == 0 {
		return 1
	}
	res, h := 10, 9
	for i := 0; i < n - 1; i++ {
		res += 9*h
		h *= 8 - i
	}
	return res
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

	result := countNumbersWithUniqueDigits(n)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
