package solution

import (
	"fmt"
	"strings"
	"time"
)

func surfaceArea(grid [][]int) int {
	res, n := 0, len(grid)
	for i := 0; i < n; i++ {
		for j := 0; j < n; j++ {
			if grid[i][j] > 0 {
				res += grid[i][j]*4 + 2
			}
			if i > 0 {
				res -= min(grid[i][j], grid[i-1][j]) * 2
			}
			if j > 0 {
				res -= min(grid[i][j], grid[i][j-1]) * 2
			}
		}
	}
	return res
}

func min(a int, b int) int {
	if a < b {
		return a
	} else {
		return b
	}
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
	fmt.Printf("grid = [%s]\n", IntIntArrayToGridString(grid))

	timeStart := time.Now()

	result := surfaceArea(grid)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
