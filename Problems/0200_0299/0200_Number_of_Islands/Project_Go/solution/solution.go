package solution

import (
	"fmt"
	"strings"
	"time"
)

func numIslands(grid [][]byte) int {
	// 0ms
	count := 0
	for i := 0; i < len(grid); i++ {
		for j := 0; j < len(grid[i]); j++ {
			if grid[i][j] == '1' {
				count++
				searchIslands(grid, i, j)
			}
		}
	}
	return count
}

func searchIslands(grid [][]byte, i int, j int) {
	if grid[i][j] == '0' {
		return
	}
	grid[i][j] = '0'
	if i-1 >= 0 {
		searchIslands(grid, i-1, j)
	}
	if i+1 < len(grid) {
		searchIslands(grid, i+1, j)
	}
	if j-1 >= 0 {
		searchIslands(grid, i, j-1)
	}
	if j+1 < len(grid[i]) {
		searchIslands(grid, i, j+1)
	}
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\",\"", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)
	flds := strings.Split(temp, "],[")

	grid := make([][]byte, len(flds))
	for i := 0; i < len(flds); i++ {
		grid[i] = StringToByteArray(flds[i])
	}
	fmt.Printf("grid = %s\n", ByteByteArrayToGridString(grid))

	timeStart := time.Now()

	result := numIslands(grid)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
