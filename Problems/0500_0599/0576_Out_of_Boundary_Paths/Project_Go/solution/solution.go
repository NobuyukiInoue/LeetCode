package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func findPaths(m int, n int, N int, i int, j int) int {
	// 8ms
	mod := int(1E9 + 7)
	dp := make([][][]int, N+1)
	for i := range dp {
		dp[i] = make([][]int, m)
		for I := range dp[i] {
			dp[i][I] = make([]int, n)
		}
	}
	dirs := [][]int{{-1, 0}, {1, 0}, {0, -1}, {0, 1}}
	for s := 1; s <= N; s++ {
		for y := 0; y < m; y++ {
			for x := 0; x < n; x++ {
				for _, dir := range dirs {
					ty := dir[0] + y
					tx := dir[1] + x
					if tx < 0 || ty < 0 || tx >= n || ty >= m {
						dp[s][y][x] += 1
					} else {
						dp[s][y][x] = (dp[s][y][x] + dp[s-1][ty][tx]) % mod
					}
				}
			}
		}
	}
	return dp[N][i][j]
}

/*
Time Limited Exceeded.

var memo [][][]int
var mod int
var directions [][]int

func findPaths(m int, n int, N int, i int, j int) int {
	mod = 1E9 + 7
	memo = make([][][]int, m)
	directions = [][]int{{1, 0}, {-1, 0}, {0, 1}, {0, -1}}
	for i := 0; i < len(memo); i++ {
		memo[i] = make([][]int, n)
		for j := 0; j < len(memo[i]); j++ {
			memo[i][j] = make([]int, N + 1)
		}
	}
	return int(dfs(m, n, i, j, N) % mod)
}

func dfs(rows int, cols int, r int, c int, steps int) int {
	if !inBound(rows, cols, r, c) {
		return 1
	}
	if steps == 0 {
		return 0
	}
	if memo[r][c][steps] != 0 {
		return memo[r][c][steps]
	}
	res := 0
	for _, direction := range(directions) {
		res = (res + dfs(rows, cols, r + direction[0], c + direction[1], steps -1)) % mod
	}
	memo[r][c][steps] = res
	return res
}

func inBound(rows int, cols int, r int, c int) bool {
	return r >= 0 && c >= 0 && r < rows && c < cols
}
*/

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)
	flds := strings.Split(temp, "],[")
	m, _ := strconv.Atoi(flds[0])
	n, _ := strconv.Atoi(flds[1])
	N, _ := strconv.Atoi(flds[2])
	i, _ := strconv.Atoi(flds[3])
	j, _ := strconv.Atoi(flds[4])

	fmt.Printf("m = %d, n = %d, N = %d, i = %d, j = %d\n", m, n, N, i, j)

	timeStart := time.Now()

	result := findPaths(m, n, N, i, j)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
