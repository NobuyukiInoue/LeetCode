package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func generateMatrix(n int) [][]int {
	// 0ms
	if n == 0 {
		return [][]int{}
	}

	result := make([][]int, n)
	for i := 0; i < len(result); i++ {
		result[i] = make([]int, n)
	}

	top, left := 0, 0
	right, bottom := n-1, n-1
	count := 1

	for top <= bottom && left <= right {
		for col := left; col <= right; col++ {
			result[top][col] = count
			count++
		}
		top++
		for row := top; row <= bottom; row++ {
			result[row][right] = count
			count++
		}
		right--

		if top > bottom {
			break
		}
		for col := right; col >= left; col-- {
			result[bottom][col] = count
			count++
		}
		bottom--

		if left > right {
			break
		}
		for row := bottom; row >= top; row-- {
			result[row][left] = count
			count++
		}
		left++
	}
	return result
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	fld := strings.Replace(temp, "]", "", -1)
	n, _ := strconv.Atoi(fld)

	fmt.Printf("n = %d\n", n)
	timeStart := time.Now()

	result := generateMatrix(n)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", IntIntArrayToString(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
