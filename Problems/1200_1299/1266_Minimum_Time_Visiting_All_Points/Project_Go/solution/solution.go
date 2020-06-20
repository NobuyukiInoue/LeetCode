package solution

import (
	"fmt"
	"strings"
	"time"
)

func minTimeToVisitAllPoints(points [][]int) int {
	// 4ms
	total := 0
	for i := 1; i < len(points); i++ {
		total += max(abs(points[i][0]-points[i-1][0]), abs(points[i][1]-points[i-1][1]))
	}
	return total
}

func max(a int, b int) int {
	if a > b {
		return a
	} else {
		return b
	}
}

func abs(a int) int {
	if a >= 0 {
		return a
	} else {
		return -a
	}
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)
	flds := strings.Split(temp, "],[")

	points := make([][]int, len(flds))
	for i := 0; i < len(flds); i++ {
		points[i] = StringToIntArray(flds[i])
	}
	fmt.Printf("points = %s\n", IntIntArrayToString(points))

	timeStart := time.Now()

	result := minTimeToVisitAllPoints(points)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
