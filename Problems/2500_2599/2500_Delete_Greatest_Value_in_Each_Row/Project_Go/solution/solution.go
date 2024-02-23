package solution

import (
	"fmt"
	"sort"
	"strings"
	"time"
)

func deleteGreatestValue(grid [][]int) int {
	// 6ms - 7ms
	for i, _ := range grid {
		sort.Sort(sort.IntSlice(grid[i]))
	}
	ans := 0
	for j := len(grid[0]) - 1; j >= 0; j-- {
		cur := grid[0][j]
		for i := 1; i < len(grid); i++ {
			cur = myMax(cur, grid[i][j])
		}
		ans += cur
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
	temp = strings.Replace(temp, "]]", "", -1)
	flds := strings.Split(temp, "],[")

	grid := make([][]int, len(flds))
	for i, _ := range flds {
		grid[i] = StringToIntArray(flds[i])
	}

	fmt.Printf("grid = %s\n", IntIntArrayToString(grid))

	timeStart := time.Now()

	result := deleteGreatestValue(grid)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
