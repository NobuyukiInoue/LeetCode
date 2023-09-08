package solution

import (
	"fmt"
	"math"
	"strings"
	"time"
)

func maxProfit(prices []int) int {
	// 105ms - 115ms
	v_max, v_min := 0, math.MaxInt64
	for _, price := range prices {
		if v_min > price {
			v_min = price
		}
		if price-v_min > v_max {
			v_max = price - v_min
		}
	}
	return v_max
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
