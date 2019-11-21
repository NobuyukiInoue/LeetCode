package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func rotate(matrix [][]int) {
	// 0ms
	n := len(matrix)
	for l := 0; l < n/2; l++ {
		r := n - 1 - l
		for p := l; p < r; p++ {
			q := n - 1 - p
			cache := matrix[l][p]
			matrix[l][p] = matrix[q][l]
			matrix[q][l] = matrix[r][q]
			matrix[r][q] = matrix[p][r]
			matrix[p][r] = cache
		}
	}
}

func str2IntArray(flds string) []int {
	numsStr := strings.Split(flds, ",")
	nums := make([]int, len(numsStr))

	for i := 0; i < len(nums); i++ {
		nums[i], _ = strconv.Atoi(numsStr[i])
	}

	return nums
}

func intArrayToString(nums []int) string {
	if len(nums) <= 0 {
		return ""
	}

	resultStr := strconv.Itoa(nums[0])
	for i := 1; i < len(nums); i++ {
		resultStr += ", " + strconv.Itoa(nums[i])
	}

	return resultStr
}

func intIntArrayToString(matrix [][]int) string {
	if len(matrix) <= 0 {
		return ""
	}
	resultStr := "[" + intArrayToString(matrix[0]) + "]"
	for i := 1; i < len(matrix); i++ {
		resultStr += ",[" + intArrayToString(matrix[i]) + "]"
	}
	return resultStr + "]"
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)
	flds := strings.Split(temp, "],[")

	matrix := make([][]int, len(flds))
	for i := 0; i < len(matrix); i++ {
		matrix[i] = str2IntArray(flds[i])
	}

	fmt.Printf("matrix = %s\n", intIntArrayToString(matrix))

	timeStart := time.Now()

	rotate(matrix)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", intIntArrayToString(matrix))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
