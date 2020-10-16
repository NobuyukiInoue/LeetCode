package solution

import (
	"fmt"
	"strings"
	"time"
)

func diagonalSum(mat [][]int) int {
	// 12ms
	total, matLength := 0, len(mat)
	for i := 0; i < matLength; i++ {
		total += mat[i][i] + mat[matLength-1-i][i]
	}

	if matLength%2 == 0 {
		return total
	}

	return total - mat[matLength/2][matLength/2]
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

	result := diagonalSum(mat)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
