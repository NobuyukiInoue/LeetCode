package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func searchMatrix(matrix [][]int, target int) bool {
	// 24ms
	if matrix == nil || len(matrix) == 0 || len(matrix[0]) == 0 {
		return false
	}
	n, m := len(matrix), len(matrix[0])
	i, j := 0, m-1
	for i < n && j >= 0 {
		num := matrix[i][j]
		if num == target {
			return true
		} else if num > target {
			j--
		} else {
			i++
		}
	}
	return false
}

func strToIntArray(flds string) []int {
	numsStr := strings.Split(flds, ",")
	nums := make([]int, len(numsStr))

	for i := 0; i < len(nums); i++ {
		nums[i], _ = strconv.Atoi(numsStr[i])
	}

	return nums
}

func intArrayToString(arr []int) string {
	if len(arr) <= 0 {
		return ""
	}

	resultStr := "["
	for i := 0; i < len(arr); i++ {
		if i > 0 {
			resultStr += ","
		}
		resultStr += strconv.Itoa(arr[i])
	}

	return resultStr + "]"
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	flds := strings.Split(temp, "]],[")
	flds[0] = strings.Replace(flds[0], "[[[", "", -1)
	dataStr := strings.Split(flds[0], "],[")

	var matrix [][]int
	if len(dataStr) > 0 {
		matrix = make([][]int, len(dataStr))
		fmt.Printf("matrix = [\n")
		for i := 0; i < len(matrix); i++ {
			matrix[i] = strToIntArray(dataStr[i])
			if i == 0 {
				fmt.Printf("  %s\n", intArrayToString(matrix[i]))
			} else {
				fmt.Printf(", %s\n", intArrayToString(matrix[i]))
			}
		}
		fmt.Printf("]\n")
	} else {
		matrix = make([][]int, 0)
	}

	flds[1] = strings.Replace(flds[1], "]", "", -1)
	target, _ := strconv.Atoi(flds[1])
	fmt.Printf("target = %d\n", target)

	timeStart := time.Now()

	result := searchMatrix(matrix, target)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", strconv.FormatBool(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
