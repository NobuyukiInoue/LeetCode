package solution

import (
	"fmt"
	"sort"
	"strconv"
	"strings"
	"time"
)

func carPooling(trips [][]int, capacity int) bool {
	// 4ms
	tripMap := map[int]int{}
	for _, row := range trips {
		tripMap[row[1]] += row[0]
		tripMap[row[2]] -= row[0]
	}

	// sort key.
	pos := make([]int, len(tripMap))
	index := 0
	for key := range tripMap {
		pos[index] = key
		index++
	}
	sort.Sort(sort.IntSlice(pos))

	passenger := 0
	for _, key := range pos {
		passenger += tripMap[key]
		if passenger > capacity {
			return false
		}
	}

	return true
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[[[", "", -1)
	flds := strings.Split(temp, "]],[")

	flds0 := strings.Split(flds[0], "],[")
	trips := make([][]int, len(flds0))
	for i := 0; i < len(trips); i++ {
		trips[i] = StringToIntArray(flds0[i])
	}
	capacity, _ := strconv.Atoi(strings.Replace(flds[1], "]", "", -1))
	fmt.Printf("trips = %s, capacity = %d\n", IntIntArrayToString(trips), capacity)

	timeStart := time.Now()

	result := carPooling(trips, capacity)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", strconv.FormatBool(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
