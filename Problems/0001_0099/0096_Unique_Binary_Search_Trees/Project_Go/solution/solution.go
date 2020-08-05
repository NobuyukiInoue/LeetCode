package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func numTrees(n int) int {
	// 0ms
	dp := make([]int, n + 5)
	dp[0], dp[1] = 1, 1
	for i := 2; i <= n; i++ {
		dp[i] = 0
		for j := 1; j <= i; j++ {
			dp[i] = dp[i] + dp[j - 1]*dp[i - j]
		}
	}
	return dp[n]
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	fld := strings.Replace(temp, "]", "", -1)

	n, _ := strconv.Atoi(fld);
	fmt.Printf("n = %d\n", n)

	timeStart := time.Now()

	result := numTrees(n)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
