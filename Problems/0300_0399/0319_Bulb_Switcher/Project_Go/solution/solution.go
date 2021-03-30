package solution

import (
	"fmt"
	"math"
	"strconv"
	"strings"
	"time"
)

func bulbSwitch(n int) int {
	// 0ms
	return int(math.Sqrt(float64(n)))
}

func bulbSwitch2(n int) int {
	// 0ms
	if n == 0 {
		return 0
	}
	ans := 1
	for i := 2; i * i <= n; i++ {
		ans++
	}
	return ans
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

	result := bulbSwitch(n)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
