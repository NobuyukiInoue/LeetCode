package solution

import (
	"fmt"
	"strings"
	"time"
)

func maxSum(grid [][]int) int {
	// 30ms - 32ms
	res := 0
	len_row, len_col := len(grid), len(grid[0])
	for i := 0; i < len_row-2; i++ {
		for j := 0; j < len_col-2; j++ {
			n_sum := grid[i][j] + grid[i][j+1] + grid[i][j+2] +
				grid[i+1][j+1] +
				grid[i+2][j] + grid[i+2][j+1] + grid[i+2][j+2]
			res = myMax(res, n_sum)
		}
	}
	return res
}

func myMax(a, b int) int {
	if a >= b {
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

	str_mat := strings.Split(flds, "],[")
	grid := make([][]int, len(str_mat))
	for i := 0; i < len(str_mat); i++ {
		grid[i] = StringToIntArray(str_mat[i])
	}
	fmt.Printf("grid = %s\n", IntIntArrayToGridString(grid))

	timeStart := time.Now()

	result := maxSum(grid)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
