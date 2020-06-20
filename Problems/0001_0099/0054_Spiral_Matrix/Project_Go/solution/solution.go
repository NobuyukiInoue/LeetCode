package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func spiralOrder(matrix [][]int) []int {
	// 0ms
	if matrix == nil || len(matrix) == 0 {
		return []int{}
	}

	result := make([]int, len(matrix)*len(matrix[0]))
	pos := 0

	top, left := 0, 0
	right, bottom := len(matrix[0])-1, len(matrix)-1
	for top <= bottom && left <= right {
		for col := left; col <= right; col++ {
			result[pos] = matrix[top][col]
			pos++
		}
		top++
		for row := top; row <= bottom; row++ {
			result[pos] = matrix[row][right]
			pos++
		}
		right--

		if top > bottom {
			break
		}
		for col := right; col >= left; col-- {
			result[pos] = matrix[bottom][col]
			pos++
		}
		bottom--

		if left > right {
			break
		}
		for row := bottom; row >= top; row-- {
			result[pos] = matrix[row][left]
			pos++
		}
		left++
	}
	return result
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)
	flds := strings.Split(temp, "],[")

	matrix := make([][]int, len(flds))
	for i, _ := range flds {
		line := strings.Split(flds[i], ",")
		matrix[i] = make([]int, len(line))
		for j, _ := range line {
			matrix[i][j], _ = strconv.Atoi(line[j])
		}
	}
	fmt.Printf("matrix = %s\n", IntIntArrayToGridString(matrix))

	timeStart := time.Now()

	result := spiralOrder(matrix)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", IntArrayToString(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
