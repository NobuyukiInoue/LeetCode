package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func findColumnWidth(grid [][]int) []int {
	// 14ms - 28ms
	ans := make([]int, len(grid[0]))
	for _, row := range grid {
		for col, val := range row {
			ans[col] = myMax(ans[col], len(strconv.Itoa(val)))
		}
	}
	return ans
}

func myMax(a, b int) int {
	if a > b {
		return a
	}
	return b
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

	result := findColumnWidth(grid)

	timeEnd := time.Now()

	fmt.Printf("result = [%s]\n", IntArrayToString(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
