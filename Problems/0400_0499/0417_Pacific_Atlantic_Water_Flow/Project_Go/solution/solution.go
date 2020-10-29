package solution

import (
	"fmt"
	"strings"
	"time"
)

func pacificAtlantic(matrix [][]int) [][]int {
	// 32ms
	xz := len(matrix)
	res := make([][]int, 0)
	if xz <= 0 {
		return res
	}
	yz := len(matrix[0])
	if yz <= 0 {
		return res
	}

	// reachablity matrices
	p_visited := make([][]int, xz)
	a_visited := make([][]int, xz)
	for i := 0; i < xz; i++ {
		p_visited[i] = make([]int, yz)
		a_visited[i] = make([]int, yz)
		for j := 0; j < yz; j++ {
			p_visited[i][j] = 0
			a_visited[i][j] = 0
		}
	}

	for i := 0; i < xz; i++ {
		dfs(matrix, p_visited, i, 0, xz, yz)    // test the reachablity from pacific
		dfs(matrix, a_visited, i, yz-1, xz, yz) // test the reachablity from altantic
	}
	for i := 0; i < yz; i++ {
		dfs(matrix, p_visited, 0, i, xz, yz)    // test the reachablity from pacific
		dfs(matrix, a_visited, xz-1, i, xz, yz) // test the reachablity from altantic
	}
	for i := 0; i < xz; i++ {
		for j := 0; j < yz; j++ {
			if p_visited[i][j] == 1 && a_visited[i][j] == 1 {
				// reachable from pacific and altantic
				res_tmp := []int{i, j}
				res = append(res, res_tmp)
			}
		}
	}
	return res
}

func dfs(matrix [][]int, visited [][]int, x int, y int, xz int, yz int) {
	visited[x][y] = 1
	direction := [][]int{{1, 0}, {0, 1}, {-1, 0}, {0, -1}}

	for _, d := range direction {
		xd := x + d[0]
		yd := y + d[1]
		if xd >= 0 && yd >= 0 && xd < xz && yd < yz {
			if visited[xd][yd] != 1 && matrix[x][y] <= matrix[xd][yd] {
				// move to next position
				dfs(matrix, visited, xd, yd, xz, yz)
			}
		}
	}
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	flds := strings.Replace(temp, "]]", "", -1)

	str_matrix := strings.Split(flds, "],[")
	matrix := make([][]int, len(str_matrix))
	for i := 0; i < len(str_matrix); i++ {
		matrix[i] = StringToIntArray(str_matrix[i])
	}
	fmt.Printf("matrix = %s\n", IntIntArrayToGridString(matrix))

	timeStart := time.Now()

	result := pacificAtlantic(matrix)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", IntIntArrayToGridString(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
