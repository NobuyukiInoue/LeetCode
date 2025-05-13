package solution

import (
	"fmt"
	"strings"
	"time"
)

func zigzagTraversal(grid [][]int) []int {
	// 0ms
	for i, _ := range grid {
		if i%2 != 0 {
			right := len(grid[i]) - 1
			for left := 0; left < right; left++ {
				grid[i][left], grid[i][right] = grid[i][right], grid[i][left]
				right--
			}
		}
	}
	var res []int
	alt := true
	for _, row := range grid {
		for _, col := range row {
			if alt {
				res = append(res, col)
			}
			alt = !alt
		}
	}
	return res
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

	result := zigzagTraversal(grid)

	timeEnd := time.Now()

	fmt.Printf("result = [%s]\n", IntArrayToString(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
