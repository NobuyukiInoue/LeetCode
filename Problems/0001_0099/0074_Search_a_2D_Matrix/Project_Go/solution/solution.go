package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func searchMatrix(matrix [][]int, target int) bool {
	// 4ms
	if len(matrix) <= 0 || len(matrix[0]) <= 0 {
		return false
	}
	if matrix[0][0] == target {
		return true
	}
	for i := 0; i < len(matrix); {
		if i+1 < len(matrix) {
			if matrix[i+1][0] == target {
				return true
			} else if matrix[i+1][0] < target {
				i++
				continue
			}
		}
		if matrix[i][0] == target {
			return true
		} else if matrix[i][0] < target {
			for j := 1; j < len(matrix[i]); j++ {
				if matrix[i][j] == target {
					return true
				} else if matrix[i][j] > target {
					return false
				}
			}
		}
		return false
	}
	return false
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
	temp = strings.Replace(temp, "[[[", "", -1)
	flds := strings.Split(temp, "]],[")
	matrixStr := strings.Split(flds[0], "],[")
	matrix := make([][]int, len(matrixStr))
	for i := 0; i < len(matrixStr); i++ {
		matrix[i] = str2IntArray(matrixStr[i])
	}
	target, _ := strconv.Atoi(strings.Replace(flds[1], "]]", "", -1))

	fmt.Printf("matrix = %s\n", intintArrayToString(matrix))

	timeStart := time.Now()

	result := searchMatrix(matrix, target)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", strconv.FormatBool(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
