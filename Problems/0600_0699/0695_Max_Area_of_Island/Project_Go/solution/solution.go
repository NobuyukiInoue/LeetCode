package solution

import (
	"fmt"
	"strings"
	"time"
)

var ans int
var count int

func maxAreaOfIsland(grid [][]int) int {
	// 12ms
	if grid == nil || grid[0] == nil {
		return 0
	}
	ans = 0
	checkTable := make([][]int, len(grid))
	for i := range grid {
		checkTable[i] = make([]int, len(grid[i]))
		copy(checkTable[i], grid[i])
	}

	for i := 0; i < len(grid); i++ {
		for j := 0; j < len(grid[i]); j++ {
			count = 0
			dfs(grid, i, j, checkTable)
		}
	}
	return ans
}

func dfs(grid [][]int, i int, j int, checkTable [][]int) {
	if i < 0 || i >= len(grid) || j < 0 || j >= len(grid[i]) {
		return
	}
	if checkTable[i][j] != 1 {
		return
	}
	count++
	checkTable[i][j] = -1
	dfs(grid, i-1, j, checkTable)
	dfs(grid, i+1, j, checkTable)
	dfs(grid, i, j-1, checkTable)
	dfs(grid, i, j+1, checkTable)
	if count > ans {
		ans = count
	}
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	flds := strings.Replace(temp, "]]", "", -1)

	str_grid := strings.Split(flds, "],[")
	grid := make([][]int, len(str_grid))
	for i := 0; i < len(str_grid); i++ {
		grid[i] = StringToIntArray(str_grid[i])
	}
	fmt.Printf("grid = %s\n", IntIntArrayToGridString(grid))

	timeStart := time.Now()

	result := maxAreaOfIsland(grid)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
