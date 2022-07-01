package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func checkXMatrix(grid [][]int) bool {
	// 39ms - 68ms
	len_grid := len(grid)
	for i, _ := range grid {
		for j, _ := range grid[i] {
			if i == j || i+j == len_grid-1 {
				if grid[i][j] == 0 {
					return false
				}
			} else {
				if grid[i][j] != 0 {
					return false
				}
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
	flds := strings.Replace(temp, "]]", "", -1)

	str_mat := strings.Split(flds, "],[")
	bombs := make([][]int, len(str_mat))
	for i := 0; i < len(str_mat); i++ {
		bombs[i] = StringToIntArray(str_mat[i])
	}
	fmt.Printf("bombs = %s\n", IntIntArrayToGridString(bombs))

	timeStart := time.Now()

	result := checkXMatrix(bombs)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", strconv.FormatBool(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
