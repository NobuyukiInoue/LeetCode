package solution

import (
	"fmt"
	"reflect"
	"strconv"
	"strings"
	"time"
)

func findRotation(mat [][]int, target [][]int) bool {
	// 0ms
	for i := 0; i < 4; i++ {
		if reflect.DeepEqual(mat, target) {
			return true
		}
		rotate(mat)
	}
	return false
}

func rotate(mat [][]int) {
	for i, j := 0, len(mat)-1; i < j; i++ {
		tmp := mat[i]
		mat[i] = mat[j]
		mat[j] = tmp
		j--
	}
	for r, R := 0, len(mat); r < R; r++ {
		for c := r + 1; c < R; c++ {
			tmp := mat[r][c]
			mat[r][c] = mat[c][r]
			mat[c][r] = tmp
		}
	}
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[[[", "", -1)
	temp = strings.Replace(temp, "]]]", "", -1)
	flds := strings.Split(temp, "]],[[")

	matrixStr := strings.Split(flds[0], "],[")
	mat := make([][]int, len(matrixStr))
	for i := 0; i < len(matrixStr); i++ {
		mat[i] = StringToIntArray(matrixStr[i])
	}

	matrixStr = strings.Split(flds[1], "],[")
	target := make([][]int, len(matrixStr))
	for i := 0; i < len(matrixStr); i++ {
		target[i] = StringToIntArray(matrixStr[i])
	}

	fmt.Printf("mat = %s\n", IntIntArrayToGridString(mat))
	fmt.Printf("target = %s\n", IntIntArrayToGridString(target))

	timeStart := time.Now()

	result := findRotation(mat, target)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", strconv.FormatBool(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
