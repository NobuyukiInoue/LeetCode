package solution

import (
	"fmt"
	"strings"
	"time"
)

func maximalRectangle(matrix [][]byte) int {
	// 0ms
	if matrix == nil || len(matrix) == 0 || len(matrix[0]) == 0 {
		return 0
	}

	hist := make([]int, len(matrix[0])+1)
	res := 0

	for _, row := range matrix {
		for i := 0; i < len(row); i++ {
			if row[i] == '0' {
				hist[i] = 0
			} else {
				hist[i]++
			}
		}
		res = myMax(res, max_area(hist))
	}

	return res
}

func max_area(hist []int) int {
	stack := make([]int, 0)
	max_ := 0

	for i := 0; i < len(hist); i++ {
		stackLen := len(stack)
		for stackLen > 0 && hist[stack[stackLen-1]] > hist[i] {
			v := hist[stack[stackLen-1]]
			stack = stack[:stackLen-1]
			stackLen = len(stack)
			var j int
			if len(stack) > 0 {
				j = stack[len(stack)-1] + 1
			} else {
				j = 0
			}
			max_ = myMax(max_, v*(i-j))
		}
		stack = append(stack, i)
		stackLen = len(stack)
	}

	return max_
}

func myMax(a int, b int) int {
	if a > b {
		return a
	}
	return b
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	flds := strings.Replace(temp, "]]", "", -1)

	var matrix [][]byte
	if flds == "[]" {
		matrix = nil
	} else {
		str_matrix := strings.Split(flds, "],[")
		matrix = make([][]byte, len(str_matrix))
		for i := 0; i < len(str_matrix); i++ {
			matrix[i] = StringToByteArray(strings.Replace(str_matrix[i], ",", "", -1))
		}
	}
	fmt.Printf("matrix = %s\n", ByteByteArrayToGridString(matrix))

	timeStart := time.Now()

	result := maximalRectangle(matrix)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
