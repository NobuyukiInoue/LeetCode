package solution

import (
	"fmt"
	"sort"
	"strings"
	"time"
)

func findMinArrowShots(points [][]int) int {
	// 72ms
	sort.Slice(points, func(i int, j int) bool {
		return points[i][1] < points[j][1]
	})

	n, count := len(points), 1
	x := points[0][1]
	for i := 1; i < n; i++ {
		if x >= points[i][0] && x <= points[i][1] {
			continue
		} else {
			count++
			x = points[i][1]
		}
	}
	return count
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)
	flds := strings.Split(temp, "],[")

	points := make([][]int, len(flds))
	for i := 0; i < len(points); i++ {
		points[i] = StringToIntArray(flds[i])
	}
	fmt.Printf("points = %s\n", IntIntArrayToString(points))

	timeStart := time.Now()

	result := findMinArrowShots(points)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
