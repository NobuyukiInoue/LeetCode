package solution

import (
	"fmt"
	"strings"
	"time"
)

func insert(intervals [][]int, newInterval []int) [][]int {
	// 8ms
	ret := make([][]int, 0)
	for i, v := range intervals {
		if v[1] < newInterval[0] {
			ret = append(ret, v)
			continue
		}

		if v[0] > newInterval[1] {
			ret = append(ret, newInterval)
			ret = append(ret, intervals[i:]...)
			return ret
		}

		newInterval[0] = min(newInterval[0], v[0])
		newInterval[1] = max(newInterval[1], v[1])
	}
	return append(ret, newInterval)
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "[[[", "", -1)
	flds := strings.Split(temp, "]],[")

	data0 := strings.Split(flds[0], "],[")
	intervals := make([][]int, len(data0))
	for i, _ := range data0 {
		intervals[i] = StringToIntArray(data0[i])
	}
	fmt.Printf("intervals = %s\n", IntIntArrayToString(intervals))

	data1 := strings.Replace(flds[1], "]]", "", -1)
	newInterval := StringToIntArray(data1)
	fmt.Printf("newInterval = [%s]\n", IntArrayToString(newInterval))

	timeStart := time.Now()

	result := insert(intervals, newInterval)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", IntIntArrayToString(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
