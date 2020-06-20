package solution

import (
	"fmt"
	"strings"
	"time"
)

func canCompleteCircuit(gas []int, cost []int) int {
	// 4ms
	start, count, cur, n := 0, 0, 0, len(gas)
	for count < n && start < 2*n {
		cur += gas[start%n] - cost[start%n]
		if cur < 0 {
			count = 0
			cur = 0
		} else {
			count++
		}
		start++
	}
	if count < n {
		return -1
	} else {
		return start % n
	}
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)
	flds := strings.Split(temp, "],[")

	gas := StringToIntArray(flds[0])
	cost := StringToIntArray(flds[1])
	fmt.Printf("gas  = [%s]\n", IntArrayToString(gas))
	fmt.Printf("cost = [%s]\n", IntArrayToString(cost))

	timeStart := time.Now()

	result := canCompleteCircuit(gas, cost)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
