package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func setZeroes(matrix [][]int) {
	// 8ms
	m, n, k := len(matrix), len(matrix[0]), 0

	for k < n && matrix[0][k] != 0 {
		k++
	}

	for i := 1; i < m; i++ {
		for j := 0; j < n; j++ {
			if matrix[i][j] == 0 {
				matrix[0][j], matrix[i][0] = 0, 0
			}
		}
	}

	for i := 1; i < m; i++ {
		for j := n - 1; j >= 0; j-- {
			if matrix[0][j] == 0 || matrix[i][0] == 0 {
				matrix[i][j] = 0
			}
		}
	}

	if k < n {
		for j := 0; j < n; j++ {
			matrix[0][j] = 0
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

func printIntArray(nums []int) string {
	if len(nums) <= 0 {
		return ""
	}

	resultStr := strconv.Itoa(nums[0])
	for i := 1; i < len(nums); i++ {
		resultStr += ", " + strconv.Itoa(nums[i])
	}

	return resultStr
}

func intintArrayToString(nums [][]int) string {
	if len(nums) <= 0 {
		return ""
	}

	resultStr := "[\n  " + intArrayToString(nums[0]) + "\n"
	for i := 1; i < len(nums); i++ {
		resultStr += ", " + intArrayToString(nums[i]) + "\n"
	}

	return resultStr + "]"
}

func intArrayToString(nums []int) string {
	if len(nums) <= 0 {
		return "[]"
	}

	resultStr := "[" + strconv.Itoa(nums[0])
	for i := 1; i < len(nums); i++ {
		resultStr += ", " + strconv.Itoa(nums[i])
	}

	return resultStr + "]"
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	flds := strings.Replace(temp, "]]", "", -1)

	str_matrix := strings.Split(flds, "],[")
	matrix := make([][]int, len(str_matrix))
	for i := 0; i < len(str_matrix); i++ {
		matrix[i] = str2IntArray(str_matrix[i])
	}

	fmt.Printf("matrix = %s\n", intintArrayToString(matrix))

	timeStart := time.Now()

	setZeroes(matrix)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", intintArrayToString(matrix))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
