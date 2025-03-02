package solution

import (
	"fmt"
	"strings"
	"time"
)

func minimumOperations(grid [][]int) int {
	// 0ms
	ans, m, n := 0, len(grid), len(grid[0])
	for col := 0; col < n; col++ {
		cur := grid[0][col]
		for row := 1; row < m; row++ {
			if grid[row][col] <= cur {
				ans += cur - grid[row][col] + 1
				cur++
			} else {
				cur = grid[row][col]
			}
		}
	}
	return ans
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)
	flds := strings.Split(temp, "],[")

	grid := make([][]int, len(flds))
	for i, _ := range flds {
		grid[i] = StringToIntArray(flds[i])
	}

	fmt.Printf("grid = %s\n", IntIntArrayToString(grid))

	timeStart := time.Now()

	result := minimumOperations(grid)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
