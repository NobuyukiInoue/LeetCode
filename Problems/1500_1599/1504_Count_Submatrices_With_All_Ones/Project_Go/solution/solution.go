package solution

import (
	"fmt"
	"strings"
	"time"
)

func numSubmat(mat [][]int) int {
	// 20ms
	matLength := len(mat)
	colLength := len(mat[0])
	for i := 0; i < matLength; i++ {
		for j := 1; j < colLength; j++ {
			if mat[i][j] == 1 {
				if j > 0 {
					mat[i][j] = mat[i][j - 1] + 1
				}
			}
		}
	}

	submatrices := 0
	for i := 0; i < matLength; i++ {
		for j := 0; j < colLength; j++ {
			if mat[i][j] > 0 {
				minValue := mat[i][j];
				for row := i; row < matLength && mat[row][j] > 0; row++ {
					minValue = myMin(minValue, mat[row][j])
					submatrices += minValue
				}
			}
		}
	}

	return submatrices
}

func myMin(a int, b int) int {
	if a < b {
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
	mat := make([][]int, len(str_mat))
	for i := 0; i < len(str_mat); i++ {
		mat[i] = StringToIntArray(str_mat[i])
	}
	fmt.Printf("mat = %s\n", IntIntArrayToGridString(mat))

	timeStart := time.Now()

	result := numSubmat(mat)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
