package solution

import (
	"fmt"
	"strings"
	"time"
)

func shortestPathBinaryMatrix(grid [][]int) int {
	// 38ms - 47ms
	m, n := len(grid), len(grid[0])
	if grid[0][0] != 0 || grid[m-1][n-1] != 0 {
		return -1
	}
	visited := make([][]bool, m)
	for i := 0; i < m; i++ {
		visited[i] = make([]bool, n)
	}
	visited[0][0] = true
	que := [][]int{{0, 0, 1}}
	for len(que) > 0 {
		cur := que[0]
		que = que[1:]
		i, j, dist := cur[0], cur[1], cur[2]
		if i == m-1 && j == n-1 {
			return dist
		}
		for _, d := range [][]int{{1, 1}, {1, -1}, {-1, -1}, {1, 0}, {0, 1}, {0, -1}, {-1, 1}, {-1, 0}, {-1, 1}} {
			ni, nj := i+d[0], j+d[1]
			if 0 <= ni && ni < m && 0 <= nj && nj < n && !visited[ni][nj] && grid[ni][nj] == 0 {
				visited[ni][nj] = true
				que = append(que, []int{ni, nj, dist + 1})
			}
		}
	}
	return -1
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

	result := shortestPathBinaryMatrix(grid)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
