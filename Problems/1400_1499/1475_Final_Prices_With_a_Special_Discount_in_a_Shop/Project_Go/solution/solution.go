package solution

import (
	"fmt"
	"strings"
	"time"
)

func finalPrices(prices []int) []int {
	// 4ms
	pricesLength := len(prices)
	for i := 0; i < pricesLength-1; i++ {
		for j := i + 1; j < pricesLength; j++ {
			if prices[i] >= prices[j] {
				prices[i] -= prices[j]
				break
			}
		}
	}
	return prices
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

	result := finalPrices(prices)

	timeEnd := time.Now()

	fmt.Printf("result = [%s]\n", IntArrayToString(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
