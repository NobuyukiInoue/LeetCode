package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func checkOverlap(radius int, x_center int, y_center int, x1 int, y1 int, x2 int, y2 int) bool {
	// 0ms
	 c1 := float64(x2 + x1) / 2.0
	 c2 := float64(y2 + y1) / 2.0
	 v1 := myAbs(float64(x_center) - c1)
	 v2 := myAbs(float64(y_center) - c2)
	 h1 := float64(x2 - x1) / 2.0
	 h2 := float64(y2 - y1) / 2.0
	 u1 := myMax(0.0, v1 - h1)
	 u2 := myMax(0.0, v2 - h2)
	return u1 * u1 + u2 * u2 <= float64(radius * radius)
}

func myMax(a float64, b float64) float64 {
	if a >= b {
		return a
	}
	return b
}

func myAbs(a float64) float64 {
	if a >= 0 {
		return a
	}
	return -a
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)
	flds := strings.Split(temp, "],[")

	circle := strings.Split(flds[0], ",")
	radius, _ := strconv.Atoi(circle[0])
	x_center, _ := strconv.Atoi(circle[1])
	y_center, _ := strconv.Atoi(circle[2])
	fmt.Printf("radius = %d, x_center = %d, y_center = %d\n", radius, x_center, y_center)

	rect := strings.Split(flds[1], ",")
	x1, _ := strconv.Atoi(rect[0])
	y1, _ := strconv.Atoi(rect[1])
	x2, _ := strconv.Atoi(rect[2])
	y2, _ := strconv.Atoi(rect[3])
	fmt.Printf("x1, y1, x2, y2 = %d, %d, %d, %d\n", x1, y1, x2, y2)

	timeStart := time.Now()

	result := checkOverlap(radius, x_center, y_center, x1, y1, x2, y2)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", strconv.FormatBool(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
