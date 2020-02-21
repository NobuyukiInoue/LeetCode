package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func uniquePaths(m int, n int) int {
	// 0ms
	count := make([][]int, m)
	for i := 0; i < m; i++ {
		count[i] = make([]int, n)
	}

	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			if i == 0 || j == 0 {
				count[i][j] = 1
			} else {
				count[i][j] = count[i-1][j] + count[i][j-1]
			}
		}
	}

	return count[m-1][n-1]
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	temp = strings.Replace(temp, "]", "", -1)
	flds := strings.Split(temp, ",")

	m, _ := strconv.Atoi(flds[0])
	n, _ := strconv.Atoi(flds[1])
	fmt.Printf("m = %d, n = %d\n", m, n)

	timeStart := time.Now()

	result := uniquePaths(m, n)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
