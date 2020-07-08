package solution

import (
	"fmt"
	"strings"
	"time"
)

func maxProfit(prices []int) int {
	// 4ms
	pricesLength := len(prices)
	if pricesLength <= 1 {
		return 0;
	}

	start := make([]int, pricesLength + 1)
	end := make([]int, pricesLength + 1)
	maxp := prices[pricesLength - 1]

	for i := pricesLength - 1; i >= 0; i-- {
		if prices[i] < maxp {
			start[i] = myMax(start[i + 1], maxp - prices[i])
		} else if prices[i] >= maxp {
			start[i] = start[i + 1]
			maxp = prices[i]
		}
	}

	minp := prices[0]
	for i := 1; i < pricesLength; i++ {
		if prices[i] > minp {
			end[i] = myMax(end[i - 1], prices[i] - minp);
		} else if prices[i] <= minp {
			end[i] = end[i - 1]
			minp = prices[i]
		}
	}

	res := 0
	for i := 0; i < pricesLength; i++ {
		if start[i + 1] + end[i] > res {
			res = start[i + 1] + end[i]
		}
	}

	return res
}

func myMax(a int, b int) int {
	if a >= b {
		return a
	}
	return b
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, " ", "", -1)
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
