package solution

import (
	"fmt"
	"math"
	"strconv"
	"strings"
	"time"
)

func nearestValidPoint(x int, y int, points [][]int) int {
	// 100ms
	smallest, index := math.MaxInt64, -1
	for i := 0; i < len(points); i++ {
		if points[i][0] == x || points[i][1] == y {
			if points[i][0] == x && points[i][1] == y {
				return i
			}
			calced := myAbs(points[i][0] - x + points[i][1] - y);
			if calced < smallest {
				smallest, index = calced, i
			}
		}
	}
	return index
}

func myAbs(n int) int {
	if n >= 0 {
		return n
	}
	return -n
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, ", ", ",", -1)
	temp = strings.Replace(temp, "]]]", "", -1)
	flds := strings.Split(temp, "],[[")

	flds0 := strings.Split(strings.Replace(flds[0], "]]", "", -1), "],[")
	x, _ := strconv.Atoi(flds0[0])
	y, _ := strconv.Atoi(flds0[1])
	fmt.Printf("x = %d, y = %d\n", x, y)

	flds1 := strings.Split(flds[1], "],[")
	points := make([][]int, len(flds1))
	for i := 0; i < len(points); i++ {
		points[i] = StringToIntArray(flds1[i])
	}
	fmt.Printf("points = %s\n", IntIntArrayToString(points))

	timeStart := time.Now()

	result := nearestValidPoint(x, y, points)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
