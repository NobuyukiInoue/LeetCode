package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func timeRequiredToBuy(tickets []int, k int) int {
	// 0ms
	ans := 0
	for i, num := range tickets {
		if i > k {
			ans += myMin(tickets[k]-1, num)
		} else {
			ans += myMin(tickets[k], num)
		}
	}
	return ans
}

func myMin(a int, b int) int {
	if a < b {
		return a
	}
	return b
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)
	flds := strings.Split(temp, "],[")
	tickets := StringToIntArray(flds[0])
	k, _ := strconv.Atoi(flds[1])
	fmt.Printf("tickets = %s, k = %d\n", IntArrayToString(tickets), k)

	timeStart := time.Now()

	result := timeRequiredToBuy(tickets, k)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
