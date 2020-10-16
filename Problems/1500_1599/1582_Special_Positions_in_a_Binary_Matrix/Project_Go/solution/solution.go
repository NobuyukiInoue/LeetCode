package solution

import (
	"fmt"
	"strings"
	"time"
)

func numSpecial(mat [][]int) int {
	// 16ms
	result := 0
	for _, row := range mat {
		if arraySum(row) == 1 {
			if getColumnSum(mat, getIndex(row)) == 1 {
				result++
			}
		}
	}
	return result
}

func getIndex(row []int) int {
	for j := 0; j < len(row); j++ {
		if row[j] == 1 {
			return j
		}
	}
	return -1
}

func getColumnSum(mat [][]int, i int) int {
	total := 0
	for _, row := range mat {
		total += row[i]
	}
	return total
}

func arraySum(row []int) int {
	total := 0
	for _, col := range row {
		total += col
	}
	return total
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

	result := numSpecial(mat)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
