package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func myPow(x float64, n int) float64 {
	// 0ms
	ans := 1.0
	if n < 0 {
		x = 1.0 / x
		n = -n
	}
	for n != 0 {
		if n%2 == 1 {
			ans *= x
		}
		x *= x
		n >>= 1
	}
	return ans
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	temp = strings.Replace(temp, "]", "", -1)
	flds := strings.Split(temp, ",")

	x, _ := strconv.ParseFloat(flds[0], 64)
	n, _ := strconv.Atoi(flds[1])

	fmt.Printf("x = %f, n = %d\n", x, n)
	timeStart := time.Now()

	result := myPow(x, n)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", strconv.FormatFloat(result, 'f', 4, 64))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
