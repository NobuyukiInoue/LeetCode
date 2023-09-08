package solution

import (
	"fmt"
	"strings"
	"time"
)

func maxProfit(prices []int) int {
	// 5ms - 6ms
	profit, prev := 0, prices[0]
	for _, price := range prices {
		if price > prev {
			profit += price - prev
		}
		prev = price
	}
	return profit
}

func maxProfit2(prices []int) int {
	// 5ms
	profit := 0
	for i := 1; i < len(prices); i++ {
		if prices[i] > prices[i-1] {
			profit += prices[i] - prices[i-1]
		}
	}
	return profit
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
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
