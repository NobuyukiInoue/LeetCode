package solution

import (
	"fmt"
	"math"
	"strconv"
	"strings"
	"time"
)

func luckyNumbers(matrix [][]int) []int {
	// 12ms
	m, n := len(matrix), len(matrix[0])
	mr := make([]int, m)
	mc := make([]int, n)

	for i := 0; i < m; i++ {
		mr[i] = math.MaxInt64
	}

	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			mr[i] = myMin(matrix[i][j], mr[i])
			mc[j] = myMax(matrix[i][j], mc[j])
		}
	}

	res := make([]int, 0)
	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			if mr[i] == mc[j] {
				res = append(res, mr[i])
			}
		}
	}

	return res
}

func myMax(a int, b int) int {
	if a > b {
		return a
	}

	return b
}

func myMin(a int, b int) int {
	if a < b {
		return a
	}

	return b
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

	result := luckyNumbers(matrix)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", intArrayToString(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
