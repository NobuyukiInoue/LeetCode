package solution

import (
	"fmt"
	"strings"
	"time"
)

// 235ms - 237ms
var R, C int

func countSubIslands(grid1 [][]int, grid2 [][]int) int {
	R, C = len(grid1), len(grid1[0])
	ans := 0
	for i := 0; i < R; i++ {
		for j := 0; j < C; j++ {
			if grid2[i][j] == 1 {
				if dfs(grid1, grid2, i, j) {
					ans++
				}
			}
		}
	}
	return ans
}

func dfs(grid1, grid2 [][]int, i, j int) bool {
	isSubIsland := true
	if 0 <= i && i < R && 0 <= j && j < C && grid2[i][j] == 1 {
		if grid1[i][j] != 1 {
			return false
		}
		grid2[i][j] = -1
		dirr := [][]int{{0, 1}, {1, 0}, {-1, 0}, {0, -1}}
		for _, d := range dirr {
			res := dfs(grid1, grid2, i+d[0], j+d[1])
			if isSubIsland && res {
				isSubIsland = true
			} else {
				isSubIsland = false
			}
		}
	}
	return isSubIsland
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[[[", "", -1)
	temp = strings.Replace(temp, "]]]", "", -1)
	flds := strings.Split(temp, "]],[[")

	flds0 := strings.Split(flds[0], "],[")
	grid1 := make([][]int, len(flds0))
	for i, _ := range flds0 {
		grid1[i] = StringToIntArray(flds0[i])
	}

	flds1 := strings.Split(flds[1], "],[")
	grid2 := make([][]int, len(flds1))
	for i, _ := range flds1 {
		grid2[i] = StringToIntArray(flds1[i])
	}

	fmt.Printf("grid1 = %s\n", IntIntArrayToString(grid1))
	fmt.Printf("grid2 = %s\n", IntIntArrayToString(grid2))

	timeStart := time.Now()

	result := countSubIslands(grid1, grid2)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
