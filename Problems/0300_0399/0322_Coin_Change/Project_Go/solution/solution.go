package solution

import (
	"fmt"
	"math"
	"strconv"
	"strings"
	"time"
)

func coinChange(coins []int, amount int) int {
	// 8ms
	dp := make([]int, amount+1)
	dp[0] = 0
	for i := 1; i < len(dp); i++ {
		dp[i] = math.MaxInt64
	}

	for _, coin := range coins {
		for j := coin; j <= amount; j++ {
			if dp[j-coin] != math.MaxInt64 {
				dp[j] = min(dp[j], dp[j-coin]+1)
			}
		}
	}

	if dp[amount] == math.MaxInt64 {
		return -1
	} else {
		return dp[amount]
	}
}

func min(a int, b int) int {
	if a < b {
		return a
	} else {
		return b
	}
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)
	flds := strings.Split(temp, "],[")

	coins := StringToIntArray(flds[0])
	fmt.Printf("coins = [%s]\n", IntArrayToString(coins))
	amount, _ := strconv.Atoi(flds[1])

	timeStart := time.Now()

	result := coinChange(coins, amount)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
