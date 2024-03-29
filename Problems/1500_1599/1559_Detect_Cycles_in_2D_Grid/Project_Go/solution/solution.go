package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

// 34ms - 52ms
var m, n int
var visited [][]bool
var direction [][]int

func containsCycle(grid [][]byte) bool {
	direction = [][]int{{0, 1}, {1, 0}, {0, -1}, {-1, 0}}
	m, n = len(grid), len(grid[0])
	n = len(grid[0])
	visited = make([][]bool, m)
	for i, _ := range visited {
		visited[i] = make([]bool, n)
	}

	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			if !visited[i][j] && bfs(grid, i, j, -1, -1) {
				return true
			}
		}
	}
	return false
}

func bfs(g [][]byte, i, j, x, y int) bool {
	c := g[i][j]
	var q [][]int
	visited[i][j] = true
	q = append(q, []int{i, j, x, y})
	for len(q) > 0 {
		l := len(q)
		for k := 0; k < l; k++ {
			curr := q[0]
			q = q[1:]
			for _, d := range direction {
				ni, nj := curr[0]+d[0], curr[1]+d[1]
				if ni < 0 || ni >= m || nj < 0 || nj >= n || g[ni][nj] != c {
					continue
				}
				if ni == curr[2] && nj == curr[3] {
					continue
				}
				if visited[ni][nj] {
					return true
				}
				q = append(q, []int{ni, nj, curr[0], curr[1]})
				visited[ni][nj] = true
			}
		}
	}
	return false
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)
	flds := strings.Split(temp, "],[")

	grid := make([][]byte, len(flds))
	for i, _ := range flds {
		grid[i] = StringToByteArray(strings.Replace(flds[i], ",", "", -1))
	}

	fmt.Printf("grid = %s\n", ByteByteArrayToGridString(grid))

	timeStart := time.Now()

	result := containsCycle(grid)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", strconv.FormatBool(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
