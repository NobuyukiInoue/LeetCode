package solution

import (
	"fmt"
	"strings"
	"time"
)

func findMissingAndRepeatedValues(grid [][]int) []int {
	// 9ms - 12ms
	n := len(grid)
	cnts := make([]int, n*n+1)
	for _, row := range grid {
		for _, col := range row {
			cnts[col]++
		}
	}
	ans := make([]int, 2)
	for i := 1; i < len(cnts); i++ {
		if cnts[i] == 2 {
			ans[0] = i
		} else if cnts[i] == 0 {
			ans[1] = i
		}
	}
	return ans
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
	fmt.Printf("grid = %s\n", IntIntArrayToString(grid))

	timeStart := time.Now()

	result := findMissingAndRepeatedValues(grid)

	timeEnd := time.Now()

	fmt.Printf("result = [%s]\n", IntArrayToString(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
