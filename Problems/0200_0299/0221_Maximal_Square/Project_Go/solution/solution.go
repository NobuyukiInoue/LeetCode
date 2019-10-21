package solution

import (
	"fmt"
	"strings"
	"time"
	"unsafe"
)

func maximalSquare(matrix [][]byte) int {
	// 0ms
	if len(matrix) == 0 {
		return 0
	}
	m, n := len(matrix), len(matrix[0])
	result := 0
	areas := make([][]int, m+1)
	for i := 0; i < len(areas); i++ {
		areas[i] = make([]int, n+1)
	}
	for i := 1; i <= m; i++ {
		for j := 1; j <= n; j++ {
			if matrix[i-1][j-1] == '1' {
				areas[i][j] = min(min(areas[i][j-1], areas[i-1][j-1]), areas[i-1][j]) + 1
				result = max(areas[i][j], result)
			}
		}
	}
	return result * result
}

func min(a int, b int) int {
	if a < b {
		return a
	} else {
		return b
	}
}

func max(a int, b int) int {
	if a > b {
		return a
	} else {
		return b
	}
}

func strToByteArray(flds string) []byte {
	nums := make([]byte, len(flds))

	for i := 0; i < len(nums); i++ {
		nums[i] = (byte)(flds[i])
	}

	return nums
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\",\"", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)
	flds := strings.Split(temp, "],[")

	matrix := make([][]byte, len(flds))
	for i := 0; i < len(flds); i++ {
		matrix[i] = strToByteArray(flds[i])
	}

	fmt.Printf("matrix = [\n")
	for i := 0; i < len(matrix); i++ {
		if i == 0 {
			fmt.Printf(" [%s]\n", *(*string)(unsafe.Pointer(&matrix[i])))
		} else {
			fmt.Printf(",[%s]\n", *(*string)(unsafe.Pointer(&matrix[i])))
		}
	}
	fmt.Printf("]\n")

	timeStart := time.Now()

	result := maximalSquare(matrix)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
