package solution

import (
	"fmt"
	"strings"
	"time"
)

func minCostClimbingStairs(cost []int) int {
	mc := make([]int, len(cost)+1)
	mc[0], mc[1] = cost[0], cost[1]
	costV := 0
	for i := 2; i <= len(cost); i++ {
		if i == len(cost) {
			costV = 0
		} else {
			costV = cost[i]
		}
		mc[i] = IntMin(mc[i-1]+costV, mc[i-2]+costV)
	}

	return mc[len(cost)]
}

func IntMin(a int, b int) int {
	if a <= b {
		return a
	} else {
		return b
	}
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	flds := strings.Replace(temp, "]", "", -1)

	cost := StringToIntArray(flds)
	fmt.Printf("cost = [%s]\n", IntArrayToString(cost))

	timeStart := time.Now()

	result := minCostClimbingStairs(cost)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
