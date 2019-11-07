package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func minimumTotal(triangle [][]int) int {
	// 4ms
	A := make([]int, len(triangle)+1)
	for i := len(triangle) - 1; i >= 0; i-- {
		for j := 0; j < len(triangle[i]); j++ {
			A[j] = Min(A[j], A[j+1]) + triangle[i][j]
		}
	}
	return A[0]
}

func Min(a int, b int) int {
	if a < b {
		return a
	} else {
		return b
	}
}

func intArrayTostring(arr []int) string {
	if len(arr) <= 0 {
		return ""
	}

	resultStr := ""
	for i := 0; i < len(arr); i++ {
		if i > 0 {
			resultStr += ","
		}
		resultStr += strconv.Itoa(arr[i])
	}

	return resultStr
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)
	flds := strings.Split(temp, "],[")

	triangle := make([][]int, len(flds))
	for i, _ := range flds {
		line := strings.Split(flds[i], ",")
		triangle[i] = make([]int, len(line))
		for j, _ := range line {
			triangle[i][j], _ = strconv.Atoi(line[j])
		}
	}
	fmt.Printf("triangle = [")
	for i := 0; i < len(triangle); i++ {
		if i == 0 {
			fmt.Printf("[%s]", intArrayTostring(triangle[i]))
		} else {
			fmt.Printf(",[%s]", intArrayTostring(triangle[i]))
		}
	}
	fmt.Printf("]\n")

	timeStart := time.Now()

	result := minimumTotal(triangle)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
