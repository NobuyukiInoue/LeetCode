package solution

import (
	"fmt"
	"strings"
	"time"
)

func minPathSum(grid [][]int) int {
	// 8ms
	m, n := len(grid), len(grid[0])

	for i := 1; i < n; i++ {
		grid[0][i] += grid[0][i-1]
	}
	for i := 1; i < m; i++ {
		grid[i][0] += grid[i-1][0]
	}
	for i := 1; i < m; i++ {
		for j := 1; j < n; j++ {
			grid[i][j] += myMin(grid[i-1][j], grid[i][j-1])
		}
	}

	return grid[m-1][n-1]
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
	grid_str := strings.Split(flds, "],[")

	grid := make([][]int, len(grid_str))
	for i := 0; i < len(grid_str); i++ {
		grid[i] = StringToIntArray(grid_str[i])
	}
	fmt.Printf("grid = %s\n", IntIntArrayToGridString(grid))

	timeStart := time.Now()

	result := minPathSum(grid)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
