package solution

import (
	"fmt"
	"strings"
	"time"
)

func areaOfMaxDiagonal(dimensions [][]int) int {
	// 4ms - 9ms
	max_diag, max_area := 0, 0
	for _, rect := range dimensions {
		area := rect[0] * rect[1]
		diag := rect[0]*rect[0] + rect[1]*rect[1]
		if diag > max_diag || diag == max_diag && area > max_area {
			max_diag = diag
			max_area = area
		}
	}
	return max_area
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	flds := strings.Replace(temp, "]]", "", -1)

	str_mat := strings.Split(flds, "],[")
	dimensions := make([][]int, len(str_mat))
	for i := 0; i < len(str_mat); i++ {
		dimensions[i] = StringToIntArray(str_mat[i])
	}
	fmt.Printf("dimensions = %s\n", IntIntArrayToString(dimensions))

	timeStart := time.Now()

	result := areaOfMaxDiagonal(dimensions)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
