package solution

import (
	"fmt"
	"sort"
	"strings"
	"time"
)

func minimumCost(cost []int) int {
	// 4ms
	sort.Sort(sort.IntSlice(cost))
	res := 0
	for i := 0; i < len(cost); i++ {
		if i%3 != len(cost)%3 {
			res += cost[i]
		}
	}
	return res
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "[", "", -1)
	flds := strings.Replace(temp, "]", "", -1)

	cost := StringToIntArray(flds)
	fmt.Printf("cost = %s\n", IntArrayToString(cost))

	timeStart := time.Now()

	result := minimumCost(cost)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
