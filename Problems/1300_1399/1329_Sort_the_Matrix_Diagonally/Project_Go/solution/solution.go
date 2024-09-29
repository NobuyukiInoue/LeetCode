package solution

import (
	"fmt"
	"sort"
	"strings"
	"time"
)

func diagonalSort(mat [][]int) [][]int {
	// 0ms
	for a := 0; a < len(mat); a++ {
		sortStartingFrom(a, 0, mat)
	}
	for b := 0; b < len(mat[0]); b++ {
		sortStartingFrom(0, b, mat)
	}

	return mat
}

func sortStartingFrom(a, b int, arr [][]int) {
	diagonal := make([]int, 0, 50)
	for i, j := a, b; (i < len(arr)) && (j < len(arr[0])); i, j = i+1, j+1 {
		diagonal = append(diagonal, arr[i][j])
	}
	sort.Ints(diagonal)
	for i, j := a, b; (i < len(arr)) && (j < len(arr[0])); i, j = i+1, j+1 {
		arr[i][j] = diagonal[0]
		diagonal = diagonal[1:]
	}
}

func diagonalSort2(mat [][]int) [][]int {
	// 7ms - 8ms
	d := make([][]int, len(mat)*len(mat[0]))
	m, n := len(mat), len(mat[0])
	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			k := j - i
			if k >= 0 {
				d[k] = append(d[k], mat[i][j])
			} else {
				k = k * -n
				d[k] = append(d[k], mat[i][j])
			}
		}
	}
	for i := range d {
		sort.Sort(sort.IntSlice(d[i]))

	}
	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			k := j - i
			if k >= 0 {
				mat[i][j] = d[k][0]
				d[k] = d[k][1:]
			} else {
				k *= -n
				mat[i][j] = d[k][0]
				d[k] = d[k][1:]
			}
		}
	}
	return mat
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)
	flds := strings.Split(temp, "],[")

	mat := make([][]int, len(flds))
	for i, _ := range flds {
		mat[i] = StringToIntArray(flds[i])
	}

	fmt.Printf("mat = %s\n", IntIntArrayToString(mat))

	timeStart := time.Now()

	result := diagonalSort(mat)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", IntIntArrayToString(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
