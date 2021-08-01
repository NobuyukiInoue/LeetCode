package solution

import (
	"fmt"
	"strings"
	"time"
)

// 28ms
var dirs [][]int

func longestIncreasingPath(matrix [][]int) int {
	if len(matrix) == 0 {
		return 0
	}
	dirs = [][]int{{0, 1}, {1, 0}, {0, -1}, {-1, 0}}
	m, n := len(matrix), len(matrix[0])
	cache := make([][]int, m)
	for i := 0; i < m; i++ {
		cache[i] = make([]int, n)
	}
	max := 1
	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			length := dfs(matrix, i, j, m, n, cache)
			max = myMax(max, length)
		}
	}
	return max
}

func dfs(matrix [][]int, i int, j int, m int, n int, cache [][]int) int {
	if cache[i][j] != 0 {
		return cache[i][j]
	}
	max := 1
	for _, dir := range dirs {
		x, y := i+dir[0], j+dir[1]
		if x < 0 || x >= m || y < 0 || y >= n || matrix[x][y] <= matrix[i][j] {
			continue
		}
		length := 1 + dfs(matrix, x, y, m, n, cache)
		max = myMax(max, length)
	}
	cache[i][j] = max
	return max
}

func myMax(i int, j int) int {
	if i >= j {
		return i
	}
	return j
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)
	flds := strings.Split(temp, "],[")

	matrix := make([][]int, len(flds))
	for i := 0; i < len(flds); i++ {
		matrix[i] = StringToIntArray(flds[i])
	}

	fmt.Printf("matrix = %s\n", IntIntArrayToGridString(matrix))

	timeStart := time.Now()

	result := longestIncreasingPath(matrix)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
