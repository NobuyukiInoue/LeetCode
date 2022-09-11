package solution

import (
	"fmt"
	"math"
	"strings"
	"time"
)

func largestLocal(grid [][]int) [][]int {
	// 13ms - 20ms
	n := len(grid)
	res := make([][]int, n-2)
	for i, _ := range res {
		res[i] = make([]int, n-2)
	}
	for i := 1; i < n-1; i++ {
		for j := 1; j < n-1; j++ {
			res[i-1][j-1] = myMax(i, j, grid)
		}
	}
	return res
}

func myMax(t_row int, t_col int, grid [][]int) int {
	maxElement := math.MinInt
	for i := t_row - 1; i < t_row+2; i++ {
		for j := t_col - 1; j < t_col+2; j++ {
			if grid[i][j] > maxElement {
				maxElement = grid[i][j]
			}
		}
	}
	return maxElement
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

	result := largestLocal(grid)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("result = %s\n", IntIntArrayToGridString(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
