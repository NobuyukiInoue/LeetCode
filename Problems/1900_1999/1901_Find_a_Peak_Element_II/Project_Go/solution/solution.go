package solution

import (
	"fmt"
	"strings"
	"time"
)

func findPeakGrid(mat [][]int) []int {
	// 164ms
	return check2dPeak(0, len(mat[0]), mat)
}

func check2dPeak(low int, high int, arr [][]int) []int {
	mid := low + (high-low)/2
	col_max := 0
	row, col := 0, 0
	for i := 0; i < len(arr); i++ {
		if arr[i][mid] > col_max {
			col_max = arr[i][mid]
			row = i
			col = mid
		}
	}
	if col > 0 && arr[row][col] < arr[row][col-1] {
		return check2dPeak(low, col, arr)
	} else if col+1 < len(arr[row]) && arr[row][col] < arr[row][col+1] {
		return check2dPeak(col, high, arr)
	} else {
		return []int{row, col}
	}
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	flds := strings.Replace(temp, "]]", "", -1)

	str_mat := strings.Split(flds, "],[")
	mat := make([][]int, len(str_mat))
	for i := 0; i < len(str_mat); i++ {
		mat[i] = StringToIntArray(str_mat[i])
	}
	fmt.Printf("mat = %s\n", IntIntArrayToGridString(mat))

	timeStart := time.Now()

	result := findPeakGrid(mat)

	timeEnd := time.Now()

	fmt.Printf("result = [%s]\n", IntArrayToString(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
