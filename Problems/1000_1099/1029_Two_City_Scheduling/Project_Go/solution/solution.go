package solution

import (
	"fmt"
	"sort"
	"strings"
	"time"
)

func twoCitySchedCost(costs [][]int) int {
	if len(costs) == 0 || len(costs[0]) == 0 {
		return 0
	}

	diff := make([]int, len(costs))
	sum := 0
	for i := 0; i < len(diff); i++ {
		sum += costs[i][0]
		diff[i] = costs[i][1] - costs[i][0]
	}

	sort.Sort(sort.IntSlice(diff))

	for i := 0; i < len(diff)/2; i++ {
		sum += diff[i]
	}

	return sum
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)
	flds := strings.Split(temp, "],[")

	costs := make([][]int, len(flds))
	for i := 0; i < len(flds); i++ {
		costs[i] = StringToIntArray(flds[i])
	}
	fmt.Printf("costs = %s\n", IntIntArrayToString(costs))

	timeStart := time.Now()

	result := twoCitySchedCost(costs)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
