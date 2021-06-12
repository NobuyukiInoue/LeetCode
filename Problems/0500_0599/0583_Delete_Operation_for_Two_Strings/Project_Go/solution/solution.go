package solution

import (
	"fmt"
	"strings"
	"time"
)

func minDistance(word1 string, word2 string) int {
	// 4ms
	m, n := len(word1), len(word2)
	dp := make([][]int, m+1)
	for i := 0; i < len(dp); i++ {
		dp[i] = make([]int, n+1)
	}

	for i := 0; i <= m; i++ {
		for j := 0; j <= n; j++ {
			if i == 0 || j == 0 {
				dp[i][j] = 0
			} else {
				if word1[i-1] == word2[j-1] {
					dp[i][j] = dp[i-1][j-1] + 1
				} else {
					dp[i][j] = myMax(dp[i-1][j], dp[i][j-1])
				}
			}
		}
	}
	val := dp[m][n]
	return m - val + n - val
}

func myMax(a int, b int) int {
	if a > b {
		return a
	}
	return b
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, ", ", ",", -1)
	temp = strings.Replace(temp, "[", "", -1)
	temp = strings.Replace(temp, "]", "", -1)
	flds := strings.Split(temp, ",")

	word1, word2 := flds[0], flds[1]
	fmt.Printf("word1 = %s, word2 = %s\n", word1, word2)

	timeStart := time.Now()

	result := minDistance(word1, word2)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
