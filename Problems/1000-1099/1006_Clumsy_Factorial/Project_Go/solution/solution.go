package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func clumsy(N int) int {
	// 0ms
	return clumsyHelper(N, 1)
}

func clumsyHelper(n int, sign int) int {
	if n <= 0 {
		return 0
	}
	return sign*n*myMax(n-1, 1)/myMax(n-2, 1) + myMax(n-3, 0) + clumsyHelper(n-4, -1)
}

func myMax(a int, b int) int {
	if a > b {
		return a
	}
	return b
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	flds := strings.Replace(temp, "]", "", -1)

	N, _ := strconv.Atoi(flds)
	fmt.Printf("N = %d\n", N)

	timeStart := time.Now()

	result := clumsy(N)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
