package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func totalMoney(n int) int {
	// 0ms
	startSum := 28
	startMonday := 1
	total := 0
	for n > 0 {
		if n > 7 {
			total += startSum
		} else {
			total += startMonday
		}
		if n > 7 {
			n -= 7
		} else {
			n--
		}
		startMonday++
		startSum += 7
	}
	return total
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

	result := totalMoney(n)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
