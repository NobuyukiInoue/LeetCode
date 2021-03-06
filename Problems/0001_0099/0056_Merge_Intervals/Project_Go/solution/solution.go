package solution

import (
	"fmt"
	"sort"
	"strconv"
	"strings"
	"time"
)

func merge(intervals [][]int) [][]int {
	// 8ms
	ans := [][]int{}
	sort.Slice(intervals, func(i, j int) bool {
		return intervals[i][0] < intervals[j][0]
	})

	for i, interval := range intervals {
		if i == 0 {
			ans = append(ans, interval)
			continue
		}

		top := ans[len(ans)-1]
		if interval[0] > top[1] {
			ans = append(ans, interval)
		} else if interval[1] > top[1] {
			top[1] = interval[1]
		}
	}

	return ans
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)
	flds := strings.Split(temp, "],[")

	intervals := make([][]int, len(flds))
	for i, _ := range flds {
		line := strings.Split(flds[i], ",")
		intervals[i] = make([]int, len(line))
		for j, _ := range line {
			intervals[i][j], _ = strconv.Atoi(line[j])
		}
	}
	fmt.Printf("intervals = %s\n", IntIntArrayToString(intervals))

	timeStart := time.Now()

	result := merge(intervals)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", IntIntArrayToString(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
