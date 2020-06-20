package solution

import (
	"fmt"
	"math"
	"strings"
	"time"
)

func luckyNumbers(matrix [][]int) []int {
	// 12ms
	m, n := len(matrix), len(matrix[0])
	mr := make([]int, m)
	mc := make([]int, n)

	for i := 0; i < m; i++ {
		mr[i] = math.MaxInt64
	}

	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			mr[i] = myMin(matrix[i][j], mr[i])
			mc[j] = myMax(matrix[i][j], mc[j])
		}
	}

	res := make([]int, 0)
	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			if mr[i] == mc[j] {
				res = append(res, mr[i])
			}
		}
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

	str_matrix := strings.Split(flds, "],[")
	matrix := make([][]int, len(str_matrix))
	for i := 0; i < len(str_matrix); i++ {
		matrix[i] = StringToIntArray(str_matrix[i])
	}
	fmt.Printf("matrix = %s\n", IntIntArrayToGridString(matrix))

	timeStart := time.Now()

	result := luckyNumbers(matrix)

	timeEnd := time.Now()

	fmt.Printf("result = [%s]\n", IntArrayToString(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
