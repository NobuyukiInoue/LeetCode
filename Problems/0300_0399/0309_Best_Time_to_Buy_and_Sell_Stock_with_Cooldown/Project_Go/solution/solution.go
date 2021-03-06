package solution

import (
	"fmt"
	"strings"
	"time"
)

func maxProfit(prices []int) int {
	if prices == nil || len(prices) == 0 {
		return 0
	}

	dp := make([][]int, len(prices))
	for i := 0; i < len(dp); i++ {
		dp[i] = make([]int, 2)
	}

	dp[0][0] -= prices[0]
	dp[0][1] = 0

	for i := 1; i < len(prices); i++ {
		dp[i][1] = max(dp[i-1][1], dp[i-1][0]+prices[i])

		var temp int
		if i > 2 {
			temp = dp[i-2][1]
		} else {
			temp = 0
		}
		dp[i][0] = max(dp[i-1][0], temp-prices[i])
	}

	return dp[len(prices)-1][1]
}

func max(a int, b int) int {
	if a > b {
		return a
	} else {
		return b
	}
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	flds := strings.Replace(temp, "]", "", -1)

	prices := StringToIntArray(flds)
	fmt.Printf("prices = [%s]\n", IntArrayToString(prices))

	timeStart := time.Now()

	result := maxProfit(prices)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
