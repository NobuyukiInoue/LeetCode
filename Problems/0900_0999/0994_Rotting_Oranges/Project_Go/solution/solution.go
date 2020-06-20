package solution

import (
	"fmt"
	"strings"
	"time"
)

func orangesRotting(grid [][]int) int {
	fresh, d := 0, 0
	for i := 0; i < len(grid); i++ {
		for j := 0; j < len(grid[i]); j++ {
			if grid[i][j] == 1 {
				fresh++
			}
		}
	}
	for old_fresh := fresh; fresh > 0; old_fresh = fresh {
		for i := 0; i < len(grid); i++ {
			for j := 0; j < len(grid[i]); j++ {
				if grid[i][j] == d+2 {
					ret := rot(&grid, i+1, j, d) + rot(&grid, i-1, j, d) + rot(&grid, i, j+1, d) + rot(&grid, i, j-1, d)
					fresh -= ret
				}
			}
		}
		if fresh == old_fresh {
			return -1
		}
		d++
	}
	return d
}

func rot(grid *[][]int, i int, j int, d int) int {
	if i < 0 || j < 0 || i >= len(*grid) || j >= len((*grid)[i]) || (*grid)[i][j] != 1 {
		return 0
	}
	(*grid)[i][j] = d + 3
	return 1
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)
	flds := strings.Split(temp, "],[")

	grid := make([][]int, len(flds))
	for i := 0; i < len(flds); i++ {
		grid[i] = StringToIntArray(flds[i])
	}

	fmt.Printf("grid = %s\n", IntIntArrayToGridString(grid))

	timeStart := time.Now()

	result := orangesRotting(grid)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
