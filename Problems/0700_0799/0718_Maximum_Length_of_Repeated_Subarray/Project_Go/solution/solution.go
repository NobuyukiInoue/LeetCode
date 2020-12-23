package solution

import (
	"fmt"
	"strings"
	"time"
)

func findLength(A []int, B []int) int {
	// 52ms
	m, n := len(A), len(B)
	res := 0
	dp := make([][]int, m + 1)
	for i, _ := range(dp) {
		dp[i] = make([]int, n + 1);
	}
	for i := 1; i <= m; i++ {
		for j := 1; j <= n; j++ {
			if A[i - 1] == B[j - 1] {
				dp[i][j] = dp[i - 1][j - 1] + 1
				res = myMax(res, dp[i][j])
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

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)
	flds := strings.Split(temp, "],[")

	A := StringToIntArray(flds[0])
	B := StringToIntArray(flds[1])
	fmt.Printf("A = %s\n", IntArrayToString(A))
	fmt.Printf("B = %s\n", IntArrayToString(B))

	timeStart := time.Now()

	result := findLength(A, B)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
