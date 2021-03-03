package solution

import (
	"fmt"
	"math"
	"strconv"
	"strings"
	"time"
)

func minSteps(n int) int {
	// 0ms
	if n == 1 {
		return 0
	}

	for i := 2; i < int(math.Sqrt(float64(n))) + 1; i++ {
		if n%i == 0 {
			return minSteps(i) + minSteps(n/i)
		}
	}
	return n
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

	result := minSteps(n)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
