package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func subtractProductAndSum(n int) int {
	// 0ms
	prod, sum := 1, 0
	for n > 0 {
		prod *= n % 10
		sum += n % 10
		n /= 10
	}
	return prod - sum
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	fld := strings.Replace(temp, "]", "", -1)

	n, _ := strconv.Atoi(fld)
	fmt.Printf("n = %d\n", n)

	timeStart := time.Now()

	result := subtractProductAndSum(n)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
