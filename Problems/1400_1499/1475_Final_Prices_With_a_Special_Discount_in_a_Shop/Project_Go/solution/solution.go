package solution

import (
	"fmt"
	"strconv"
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

func strToIntArray(flds string) []int {
	numsStr := strings.Split(flds, ",")
	nums := make([]int, len(numsStr))

	for i := 0; i < len(nums); i++ {
		nums[i], _ = strconv.Atoi(numsStr[i])
	}

	return nums
}

func intArrayToString(nums []int) string {
	if len(nums) <= 0 {
		return ""
	}

	resultStr := strconv.Itoa(nums[0])
	for i := 1; i < len(nums); i++ {
		resultStr += ", " + strconv.Itoa(nums[i])
	}

	return resultStr
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	flds := strings.Replace(temp, "]", "", -1)

	prices := strToIntArray(flds)
	fmt.Printf("prices = [%s]\n", intArrayToString(prices))

	timeStart := time.Now()

	result := finalPrices(prices)

	timeEnd := time.Now()

	fmt.Printf("result = [%s]\n", intArrayToString(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
