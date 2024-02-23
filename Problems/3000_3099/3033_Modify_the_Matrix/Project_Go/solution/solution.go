package solution

import (
	"fmt"
	"strings"
	"time"
)

func modifiedMatrix(matrix [][]int) [][]int {
	// 0ms - 9ms
	n := myMax(len(matrix), len(matrix[0]))
	max_col := make([]int, n)
	for _, row := range matrix {
		for j := 0; j < len(row); j++ {
			max_col[j] = myMax(max_col[j], row[j])
		}
	}
	for i := 0; i < len(matrix); i++ {
		for j := 0; j < len(matrix[i]); j++ {
			if matrix[i][j] == -1 {
				matrix[i][j] = max_col[j]
			}
		}
	}
	return matrix
}

func myMax(a, b int) int {
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
	temp = strings.Replace(temp, "]]", "", -1)
	flds := strings.Split(temp, "],[")

	matrix := make([][]int, len(flds))
	for i, _ := range flds {
		matrix[i] = StringToIntArray(flds[i])
	}

	fmt.Printf("matrix = %s\n", IntIntArrayToString(matrix))

	timeStart := time.Now()

	result := modifiedMatrix(matrix)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", IntIntArrayToString(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
