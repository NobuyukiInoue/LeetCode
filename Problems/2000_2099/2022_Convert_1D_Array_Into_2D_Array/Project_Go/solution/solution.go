package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func construct2DArray(original []int, m int, n int) [][]int {
	// 124ms
	if m*n != len(original) {
		return make([][]int, 0)
	}
	ans := make([][]int, m)
	pos := 0
	for i := 0; i < m; i++ {
		ans[i] = make([]int, n)
		for j := 0; j < n; j++ {
			ans[i][j] = original[pos]
			pos++
		}
	}
	return ans
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)
	flds := strings.Split(temp, "],[")
	original := StringToIntArray(flds[0])
	m, _ := strconv.Atoi(flds[1])
	n, _ := strconv.Atoi(flds[2])
	fmt.Printf("nums = %s, m = %d, n = %d\n", IntArrayToString(original), m, n)

	timeStart := time.Now()

	result := construct2DArray(original, m, n)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", IntIntArrayToString(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
