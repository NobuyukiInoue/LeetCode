package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

// 3ms - 11ms
var VALID_MOVES [8][2]int = [8][2]int{
	{-1, -2}, {1, -2},
	{-2, -1}, {2, -1},

	{-2, 1}, {2, 1},
	{-1, 2}, {1, 2},
}

func checkValidGrid(grid [][]int) bool {
	return isValid(grid, 0, 0, 0)
}

func isValid(grid [][]int, x int, y int, expectedPos int) bool {
	if x >= len(grid) || y >= len(grid) || x < 0 || y < 0 || grid[x][y] != expectedPos {
		return false
	}
	if expectedPos == len(grid)*len(grid[0])-1 {
		return true
	}
	for _, delta := range VALID_MOVES {
		if isValid(grid, x+delta[0], y+delta[1], expectedPos+1) {
			return true
		}
	}
	return false
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

	result := checkValidGrid(grid)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", strconv.FormatBool(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
