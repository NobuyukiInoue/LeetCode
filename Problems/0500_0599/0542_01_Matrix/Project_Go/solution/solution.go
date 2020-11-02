package solution

import (
	"fmt"
	"math"
	"strings"
	"time"
)

func updateMatrix(matrix [][]int) [][]int {
	// 48ms
	m, n := len(matrix), len(matrix[0])
	dp := make([][]int, m)
	for i := 0; i < m; i++ {
		dp[i] = make([]int, n)
		for j := 0; j < n; j++ {
			if matrix[i][j] == 1 {
				dp[i][j] = math.MaxInt32 - 1
			}
		}
	}

	for i := 1; i < m; i++ {
		dp[i][0] = myMin(dp[i][0], dp[i - 1][0] + 1)
	}

	for i := 1; i < n; i++ {
		dp[0][i] = myMin(dp[0][i], dp[0][i - 1] + 1)
	}

	for i := 1; i < m; i++ {
		for j := 1; j < n; j++ {
			dp[i][j] = myMin(dp[i][j], myMin(dp[i][j - 1], dp[i - 1][j]) + 1)
		}
	}

	for i := m - 2; i >= 0; i-- {
		dp[i][n - 1] = myMin(dp[i + 1][n - 1] + 1, dp[i][n - 1])
	}
	for i := n - 2; i >= 0; i-- {
		dp[m - 1][i] = myMin(dp[m - 1][i + 1] + 1, dp[m - 1][i])
	}

	for i := m - 2; i >= 0; i-- {
		for j := n - 2; j >= 0; j-- {
			dp[i][j] = myMin(dp[i][j], myMin(dp[i][j + 1], dp[i + 1][j]) + 1)
		}
	}

	return dp
}

func myMin(a int, b int) int {
	if a < b {
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

	str_matrix := strings.Split(flds, "],[")
	matrix := make([][]int, len(str_matrix))
	for i := 0; i < len(str_matrix); i++ {
		matrix[i] = StringToIntArray(str_matrix[i])
	}
	fmt.Printf("matrix = %s\n", IntIntArrayToGridString(matrix))

	timeStart := time.Now()

	result := updateMatrix(matrix)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", IntIntArrayToGridString(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
