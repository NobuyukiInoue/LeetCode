package solution

import (
	"fmt"
	"strings"
	"time"
)

func rotate(matrix [][]int) {
	// 0ms
	n := len(matrix)
	for l := 0; l < n/2; l++ {
		r := n - 1 - l
		for p := l; p < r; p++ {
			q := n - 1 - p
			cache := matrix[l][p]
			matrix[l][p] = matrix[q][l]
			matrix[q][l] = matrix[r][q]
			matrix[r][q] = matrix[p][r]
			matrix[p][r] = cache
		}
	}
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)
	flds := strings.Split(temp, "],[")

	matrix := make([][]int, len(flds))
	for i := 0; i < len(matrix); i++ {
		matrix[i] = StringToIntArray(flds[i])
	}

	fmt.Printf("matrix = %s\n", IntIntArrayToGridString(matrix))

	timeStart := time.Now()

	rotate(matrix)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", IntIntArrayToGridString(matrix))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
