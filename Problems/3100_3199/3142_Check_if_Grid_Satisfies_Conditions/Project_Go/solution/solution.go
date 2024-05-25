package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func satisfiesConditions(grid [][]int) bool {
	// 10ms
	m, n := len(grid), len(grid[0])
	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			if j < n-1 && grid[i][j] == grid[i][j+1] {
				return false
			}
			if i < m-1 && grid[i][j] != grid[i+1][j] {
				return false
			}
		}
	}
	return true
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)
	flds := strings.Split(temp, "],[")

	matrix := make([][]int, len(flds))
	for i, _ := range flds {
		matrix[i] = StringToIntArray(flds[i])
	}

	fmt.Printf("matrix = %s\n", IntIntArrayToString(matrix))

	timeStart := time.Now()

	result := satisfiesConditions(matrix)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", strconv.FormatBool(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
