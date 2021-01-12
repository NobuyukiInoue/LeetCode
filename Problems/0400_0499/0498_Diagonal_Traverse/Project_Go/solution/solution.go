package solution

import (
	"fmt"
	"strings"
	"time"
)

func findDiagonalOrder(matrix [][]int) []int {
	// 20ms
	if len(matrix) == 0 {
		return make([]int, 0)
	}
	m, n := len(matrix), len(matrix[0])
	res := make([]int, m*n)
	direction := true
	pos := 0
	for i := 0; i < m + n - 1; i++ {
		up := myMin(i, m - 1);
		down := myMax(i - n + 1, 0);
		if direction {
			for j := up; j > down - 1; j-- {
				res[pos] = matrix[j][i - j]
				pos++
			}
		} else {
			for j := down; j < up + 1; j++ {
				res[pos] = matrix[j][i - j]
				pos++
			}
		}
		direction = !direction
	}
	return res
}

func myMax(a int, b int) int {
	if a > b {
		return a
	}
	return b
}

func myMin(a int, b int) int {
	if a < b {
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
	matrix := make([][]int, len(matrixStr))
	for i := 0; i < len(matrixStr); i++ {
		matrix[i] = StringToIntArray(matrixStr[i])
	}
	fmt.Printf("matrix = %s\n", IntIntArrayToGridString(matrix))

	timeStart := time.Now()

	result := findDiagonalOrder(matrix)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
