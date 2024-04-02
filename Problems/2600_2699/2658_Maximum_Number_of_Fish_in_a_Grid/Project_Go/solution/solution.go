package solution

import (
	"fmt"
	"strings"
	"time"
)

func findMaxFish(grid [][]int) int {
	// 22ms - 33ms
	ans := 0
	for i := 0; i < len(grid); i++ {
		for j := 0; j < len(grid[i]); j++ {
			if grid[i][j] != 0 {
				ans = myMax(ans, dfs(grid, i, j, grid[i][j]))
			}
		}
	}
	return ans
}

func dfs(grid [][]int, i int, j int, cnt int) int {
	grid[i][j] = 0
	for _, d := range [][]int{{1, 0}, {-1, 0}, {0, 1}, {0, -1}} {
		ni, nj := i+d[0], j+d[1]
		if ni < 0 || len(grid) <= ni || nj < 0 || len(grid[0]) <= nj {
			continue
		}
		if grid[ni][nj] != 0 {
			cnt += dfs(grid, ni, nj, grid[ni][nj])
		}
	}
	return cnt
}

func myMax(a, b int) int {
	if a > b {
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

	grid := make([][]int, len(flds))
	for i, _ := range flds {
		grid[i] = StringToIntArray(flds[i])
	}

	fmt.Printf("grid = %s\n", IntIntArrayToString(grid))

	timeStart := time.Now()

	result := findMaxFish(grid)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
