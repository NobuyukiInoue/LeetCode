package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func change(amount int, coins []int) int {
	// 0ms
	dp := make([]int, amount+1)
	dp[0] = 1
	for _, coin := range coins {
		for j := coin; j < amount+1; j++ {
			dp[j] += dp[j-coin]
		}
	}
	return dp[amount]
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)
	flds := strings.Split(temp, "],[")

	amount, _ := strconv.Atoi(flds[0])
	coins := StringToIntArray(flds[1])
	fmt.Printf("ammount = %d, coins = [%s]\n", amount, IntArrayToString(coins))

	timeStart := time.Now()

	result := change(amount, coins)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
