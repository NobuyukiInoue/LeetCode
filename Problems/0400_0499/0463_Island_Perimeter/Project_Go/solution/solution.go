package solution

import (
	"fmt"
	"strings"
	"time"
)

func islandPerimeter(grid [][]int) int {
	island, redge := 0, 0
	row, col := len(grid), len(grid[0])
	for i := 0; i < row; i++ {
		for j := 0; j < col; j++ {
			if grid[i][j] == 1 {
				island++
				if j < col-1 && grid[i][j+1] == 1 {
					redge++
				}
				if i < row-1 && grid[i+1][j] == 1 {
					redge++
				}
			}
		}
	}

	return 4*island - 2*redge
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)

	flds := strings.Split(temp, "],[")
	grid := make([][]int, len(flds))
	for i, _ := range grid {
		grid[i] = StringToIntArray(flds[i])
	}

	fmt.Printf("grid = %s\n", IntIntArrayToGridString(grid))

	timeStart := time.Now()

	result := islandPerimeter(grid)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
