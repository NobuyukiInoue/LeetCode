package main

import (
	"fmt"
	"math"
	"strconv"
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

func IntArray2string(arr [][]int) string {
	if len(arr) <= 0 {
		return ""
	}

	resultStr := "["
	for i := 0; i < len(arr); i++ {
		if i == 0 {
			resultStr += "["
		} else {
			resultStr += ",["
		}
		for j := 0; j < len(arr[i]); j++ {
			if j > 0 {
				resultStr += ","
			}
			resultStr += strconv.Itoa(arr[i][j])
		}
		resultStr += "]"
	}

	return resultStr + "]"
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
		points[i] = make([]int, 2)

		pt := strings.Split(flds[i], ",")
		temp, _ := strconv.Atoi(pt[0])
		points[i][0] = temp

		temp, _ = strconv.Atoi(pt[1])
		points[i][1] = temp

	}

	fmt.Printf("points[] = %s\n", IntArray2string(points))

	timeStart := time.Now()

	result := largestTriangleArea(points)
	fmt.Printf("result = %f\n", result)

	timeEnd := time.Now()

	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
