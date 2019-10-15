package solution

import (
	"fmt"
	"strings"
	"time"
)

func minDeletionSize(A []string) int {
	m, n := len(A), len(A[0])
	res := 0
	for j := 0; j < n; j++ {
		for i := 1; i < m; i++ {
			if A[i-1][j] > A[i][j] {
				res++
				break
			}
		}
	}
	return res
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	temp = strings.Replace(temp, "]", "", -1)
	A := strings.Split(temp, ",")

	fmt.Printf("A = %s\n", A)

	timeStart := time.Now()

	result := minDeletionSize(A)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
