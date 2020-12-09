package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func countDigitOne(n int) int {
	// 0ms
	count := 0
	for k := 1; k <= n; k *= 10 {
		r := int(n / k)
		m := int(n % k)
		if r % 10 == 1 {
			count += (r + 8) / 10 * k + m + 1
		} else {
			count += (r + 8) / 10 * k
		}
	}
	return count
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	fld := strings.Replace(temp, "]", "", -1)
	n, _ := strconv.Atoi(fld)
	fmt.Printf("n = %d\n", n)

	timeStart := time.Now()

	result := countDigitOne(n)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
