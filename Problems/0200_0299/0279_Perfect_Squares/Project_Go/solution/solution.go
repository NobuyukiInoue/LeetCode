package solution

import (
	"fmt"
	"math"
	"strconv"
	"strings"
	"time"
)

func numSquares(n int) int {
	// 16ms
	dp := make([]int, n+1)
	dp[0] = 0
	for i := 1; i < n+1; i++ {
		dp[i] = math.MaxInt64
	}

	for i := 1; i < n+1; i++ {
		sqi := i * i
		for j := sqi; j < n+1; j++ {
			dp[j] = myMin(dp[j], 1+dp[j-sqi])
		}
	}
	return dp[n]
}

func myMin(a int, b int) int {
	if a < b {
		return a
	}
	return b
}

func strArrayToString(data []string) string {
	if len(data) <= 0 {
		return ""
	}

	resultStr := data[0]
	for i := 1; i < len(data); i++ {
		resultStr += ", " + data[i]
	}

	return resultStr
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	flds := strings.Replace(temp, "]", "", -1)

	n, _ := strconv.Atoi(flds)
	fmt.Printf("n = %d\n", n)

	timeStart := time.Now()

	result := numSquares(n)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
