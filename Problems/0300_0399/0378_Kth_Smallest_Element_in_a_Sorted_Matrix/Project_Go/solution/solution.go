package solution

import (
	"fmt"
	"sort"
	"strconv"
	"strings"
	"time"
)

func kthSmallest(matrix [][]int, k int) int {
	// 24ms
	n := len(matrix)
	lo, hi := matrix[0][0], matrix[n-1][n-1]
	for lo <= hi {
		mid := lo + (hi-lo)/2
		count := getLessEqual(matrix, mid)
		if count < k {
			lo = mid + 1
		} else {
			hi = mid - 1
		}
	}
	return lo
}

func getLessEqual(matrix [][]int, val int) int {
	res := 0
	n := len(matrix)
	for i, j := n-1, 0; i >= 0 && j < n; {
		if matrix[i][j] > val {
			i--
		} else {
			res += i + 1
			j++
		}
	}
	return res
}

func kthSmallest2(matrix [][]int, k int) int {
	// 36ms
	m, n := len(matrix), len(matrix[0])
	data := make([]int, m*n)
	pos := 0
	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			data[pos] = matrix[i][j]
			pos++
		}
	}
	sort.Sort(sort.IntSlice(data))
	return data[k-1]
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[[[", "", -1)
	flds := strings.Split(temp, "]],[")
	matrixStr := strings.Split(flds[0], "],[")
	matrix := make([][]int, len(matrixStr))
	for i := 0; i < len(matrixStr); i++ {
		matrix[i] = StringToIntArray(matrixStr[i])
	}
	k, _ := strconv.Atoi(strings.Replace(flds[1], "]]", "", -1))

	fmt.Printf("matrix = %s\n", IntIntArrayToGridString(matrix))

	timeStart := time.Now()

	result := kthSmallest(matrix, k)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
