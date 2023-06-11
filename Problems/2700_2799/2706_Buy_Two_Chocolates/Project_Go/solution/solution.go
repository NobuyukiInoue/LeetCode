package solution

import (
	"fmt"
	"sort"
	"strconv"
	"strings"
	"time"
)

func buyChoco(prices []int, money int) int {
	// 7ms - 9ms
	sort.Sort(sort.IntSlice(prices))
	if prices[0]+prices[1] <= money {
		return money - (prices[0] + prices[1])
	}
	return money
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)
	flds := strings.Split(temp, "],[")

	prices := StringToIntArray(flds[0])
	money, _ := strconv.Atoi(flds[1])
	fmt.Printf("prices = [%s], money = %d\n", IntArrayToString(prices), money)

	timeStart := time.Now()

	result := buyChoco(prices, money)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
