package solution

import (
	"fmt"
	"strings"
	"time"
)

func setZeroes(matrix [][]int) {
	// 8ms
	m, n, k := len(matrix), len(matrix[0]), 0

	for k < n && matrix[0][k] != 0 {
		k++
	}

	for i := 1; i < m; i++ {
		for j := 0; j < n; j++ {
			if matrix[i][j] == 0 {
				matrix[0][j], matrix[i][0] = 0, 0
			}
		}
	}

	for i := 1; i < m; i++ {
		for j := n - 1; j >= 0; j-- {
			if matrix[0][j] == 0 || matrix[i][0] == 0 {
				matrix[i][j] = 0
			}
		}
	}

	if k < n {
		for j := 0; j < n; j++ {
			matrix[0][j] = 0
		}
	}
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	flds := strings.Replace(temp, "]]", "", -1)

	str_matrix := strings.Split(flds, "],[")
	matrix := make([][]int, len(str_matrix))
	for i := 0; i < len(str_matrix); i++ {
		matrix[i] = StringToIntArray(str_matrix[i])
	}
	fmt.Printf("matrix = %s\n", IntIntArrayToGridString(matrix))

	timeStart := time.Now()

	setZeroes(matrix)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", IntIntArrayToGridString(matrix))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
