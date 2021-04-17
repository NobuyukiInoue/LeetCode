package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func maxProfit(prices []int, fee int) int {
	// 88ms
	pricesLength := len(prices)
	if pricesLength < 2 {
		return 0
	}
	ans := 0
	minimum := prices[0]
	for i := 1; i < pricesLength; i++ {
		if prices[i] < minimum {
			minimum = prices[i]
		} else if prices[i] > minimum + fee {
			ans += prices[i] - fee - minimum
			minimum = prices[i] - fee
		}
	}
	return ans
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)
	flds := strings.Split(temp, "],[")

	prices := StringToIntArray(flds[0])
	fee, _ := strconv.Atoi(flds[1])
	fmt.Printf("prices = [%s], fee = %d\n", IntArrayToString(prices), fee)

	timeStart := time.Now()

	result := maxProfit(prices, fee)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
