package solution

import (
	"fmt"
	"strings"
	"time"
)

func findBall(grid [][]int) []int {
	// 20ms
	m, n := len(grid), len(grid[0])
	res := make([]int, n)
	for i := 0; i < n; i++ {
		pos := i
		for j := 0; j < m; j++ {
			dir := grid[j][pos]
			if nextPos := pos + dir; nextPos < 0 || nextPos >= n || grid[j][nextPos] == -dir {
				pos = -1
				break
			}
			pos += dir
		}
		res[i] = pos
	}
	return res
}

func findBall2(grid [][]int) []int {
	// 31ms
	m, n := len(grid), len(grid[0])
	res := make([]int, n)
	for i, _ := range res {
		res[i] = fall(i, grid, m, n)
	}
	return res
}

func fall(pos int, grid [][]int, m int, n int) int {
	for j, _ := range grid {
		npos := pos + grid[j][pos]
		if npos < 0 || npos >= n || grid[j][npos] != grid[j][pos] {
			return -1
		}
		pos = npos
	}
	return pos
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	flds := strings.Replace(temp, "]]", "", -1)

	str_mat := strings.Split(flds, "],[")
	grid := make([][]int, len(str_mat))
	for i := 0; i < len(str_mat); i++ {
		grid[i] = StringToIntArray(str_mat[i])
	}
	fmt.Printf("grid = %s\n", IntIntArrayToGridString(grid))

	timeStart := time.Now()

	result := findBall(grid)

	timeEnd := time.Now()

	fmt.Printf("result = [%s]\n", IntArrayToString(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
