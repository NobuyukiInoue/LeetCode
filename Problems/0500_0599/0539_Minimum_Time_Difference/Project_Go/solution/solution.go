package solution

import (
	"fmt"
	"math"
	"strconv"
	"strings"
	"time"
)

func findMinDifference(timePoints []string) int {
	// 4ms
	visited := make([]bool, 24*60)
	for _, time := range timePoints {
		h, _ := strconv.Atoi(time[0:2])
		m, _ := strconv.Atoi(time[3:])
		if visited[h*60+m] {
			return 0
		}
		visited[h*60+m] = true
	}

	prev, min := 0, math.MaxInt64
	first, last := 0, 0
	idx := len(visited) - 1
	for !visited[idx] {
		idx--
	}
	last = idx

	idx = 0
	for !visited[idx] {
		idx++
	}
	first, prev = idx, first
	for i := first + 1; i <= last; i++ {
		if visited[i] {
			min = myMin(min, i-prev)
			prev = i
		}
	}

	min = myMin(min, (24*60 - last + first))
	return min
}

func myMin(a int, b int) int {
	if a < b {
		return a
	}
	return b
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, ", ", ",", -1)
	temp = strings.Replace(temp, "[", "", -1)
	flds := strings.Replace(temp, "]", "", -1)

	timePoints := strings.Split(flds, ",")
	fmt.Printf("timePoints = %s\n", timePoints)

	timeStart := time.Now()

	result := findMinDifference(timePoints)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
