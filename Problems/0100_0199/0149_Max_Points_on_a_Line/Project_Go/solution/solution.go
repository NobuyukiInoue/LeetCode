package solution

import (
	"fmt"
	"math"
	"strings"
	"time"
)

func maxPoints(points [][]int) int {
	// 10ms
	if len(points) <= 2 {
		return len(points)
	}
	res := 0
	for i := 0; i < len(points); i++ {
		cur, overlap := 0, 0
		lines := map[float64]int{}
		for j := i + 1; j < len(points); j++ {
			dx := points[i][0] - points[j][0]
			dy := points[i][1] - points[j][1]
			if dx == 0 && dy == 0 {
				overlap++
				continue
			}
			var key float64
			if dx == 0 {
				key = math.MaxFloat64
			} else {
				key = 10.0 * float64(dy) / float64(dx)
			}
			if val, ok := lines[key]; ok {
				lines[key] = val + 1
			} else {
				lines[key] = 1
			}
			cur = myMax(cur, lines[key])
		}
		res = myMax(res, cur+overlap)
	}
	return res + 1
}

func myMax(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	flds := strings.Replace(temp, "]]", "", -1)

	str_mat := strings.Split(flds, "],[")
	points := make([][]int, len(str_mat))
	for i := 0; i < len(str_mat); i++ {
		points[i] = StringToIntArray(str_mat[i])
	}
	fmt.Printf("points = %s\n", IntIntArrayToString(points))

	timeStart := time.Now()

	result := maxPoints(points)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
