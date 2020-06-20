package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func smallestRangeI(A []int, K int) int {
	mx, mn := A[0], A[0]
	for _, a := range A {
		mx = max(mx, a)
		mn = min(mn, a)
	}

	return max(0, mx-mn-2*K)
}

func max(a int, b int) int {
	if a > b {
		return a
	} else {
		return b
	}
}

func min(a int, b int) int {
	if a < b {
		return a
	} else {
		return b
	}
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)
	flds := strings.Split(temp, "],[")

	A := StringToIntArray(flds[0])
	K, _ := strconv.Atoi(flds[1])

	fmt.Printf("A = [%s]\n", IntArrayToString(A))
	fmt.Printf("K = %d\n", K)

	timeStart := time.Now()

	result := smallestRangeI(A, K)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
