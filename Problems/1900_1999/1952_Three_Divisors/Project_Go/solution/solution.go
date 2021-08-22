package solution

import (
	"fmt"
	"math"
	"strconv"
	"strings"
	"time"
)

func isThree(n int) bool {
	// 0ms
	if n < 3 {
		return false
	}
	dq := math.Sqrt(float64(n))
	if dq-float64(int64(dq)) > 0 {
		return false
	}
	for i := 2; i < int(dq/2); i++ {
		if n%i == 0 {
			return false
		}
	}
	return true
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "[", "", -1)
	flds := strings.Replace(temp, "]", "", -1)

	n, _ := strconv.Atoi(flds)
	fmt.Printf("n = %d\n", n)

	timeStart := time.Now()

	result := isThree(n)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", strconv.FormatBool(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
