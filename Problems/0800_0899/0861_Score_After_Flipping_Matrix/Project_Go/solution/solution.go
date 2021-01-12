package solution

import (
	"fmt"
	"strings"
	"time"
)

func matrixScore(A [][]int) int {
	// 0ms
	r, c := len(A), len(A[0])
	answer := r * (1 << (uint64(c) - 1))
	for j := 1; j < c; j++ {
		count := 0
		for i := 0; i < r; i++ {
			if A[i][0] == 1 {
				count += A[i][j]
			} else {
				count += A[i][j] ^ 1
			}
		}
		answer += myMax(r - count, count) * (1 << (uint64(c - 1 - j)));
	}
	return answer
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
	temp = strings.Replace(temp, "[[", "", -1)
	flds := strings.Replace(temp, "]]", "", -1)

	matrixStr := strings.Split(flds, "],[")
	A := make([][]int, len(matrixStr))
	for i := 0; i < len(matrixStr); i++ {
		A[i] = StringToIntArray(matrixStr[i])
	}
	fmt.Printf("A = %s\n", IntIntArrayToGridString(A))

	timeStart := time.Now()

	result := matrixScore(A)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
