package solution

import (
	"fmt"
	"math"
	"strings"
	"time"
)

func largestTriangleArea(points [][]int) float64 {
	area := 0.0
	for i := 0; i < len(points); i++ {
		for j := i + 1; j < len(points); j++ {
			for k := j + 1; k < len(points); k++ {
				x1 := points[i][0]
				y1 := points[i][1]
				x2 := points[j][0]
				y2 := points[j][1]
				x3 := points[k][0]
				y3 := points[k][1]
				temparea := (float64)(x1*(y2-y3) - y1*(x2-x3) + (x2*y3 - x3*y2))
				area = math.Max(area, math.Abs(temparea))
			}
		}
	}
	return area / 2.0
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
	fmt.Printf("points = %s\n", IntIntArrayToGridString(points))

	timeStart := time.Now()

	result := largestTriangleArea(points)

	timeEnd := time.Now()

	fmt.Printf("result = %f\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
