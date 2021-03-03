package solution

import (
	"fmt"
	"strings"
	"time"
)

func restoreMatrix(rowSum []int, colSum []int) [][]int {
	// 72ms
	height := len(rowSum)
	width := len(colSum)
	matrix := make([][]int, height)
	for i := 0; i < height; i++ {
		matrix[i] = make([]int, width)
	}

	i, j := 0, 0;
	for i < height && j < width {
		matrix[i][j] = myMin(rowSum[i], colSum[j]);
		if rowSum[i] == colSum[j] {
			i++
			j++
		} else if rowSum[i] > colSum[j] {
			rowSum[i] -= colSum[j]
			j++
		} else {
			colSum[j] -= rowSum[i]
			i++
		}
	}
	return matrix
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
	temp = strings.Replace(temp, "]]", "", -1)
	flds := strings.Split(temp, "],[")

	rowSum := StringToIntArray(flds[0])
	colSum := StringToIntArray(flds[1])

	fmt.Printf("rowSum = %s\n", IntArrayToString(rowSum))
	fmt.Printf("colSum = %s\n", IntArrayToString(colSum))

	timeStart := time.Now()

	result := restoreMatrix(rowSum, colSum)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", IntIntArrayToGridString(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
