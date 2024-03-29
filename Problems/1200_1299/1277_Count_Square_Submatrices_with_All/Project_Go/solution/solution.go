package solution

import (
	"fmt"
	"strings"
	"time"
)

func countSquares(matrix [][]int) int {
	// 40ms - 46ms
	count, m, n := 0, len(matrix), len(matrix[0])
	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			if matrix[i][j] == 1 && (i != 0 && j != 0) {
				matrix[i][j] = myMin(matrix[i-1][j-1], myMin(matrix[i-1][j], matrix[i][j-1])) + 1
			}
		}
		count += sum(matrix[i])
	}
	return count

}

func myMin(a, b int) int {
	if a < b {
		return a
	}
	return b
}

func sum(nums []int) int {
	res := 0
	for _, num := range nums {
		res += num
	}
	return res
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

	result := countSquares(matrix)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
