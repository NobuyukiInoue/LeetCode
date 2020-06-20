package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func isBoomerang(points [][]int) bool {
	return (points[0][0]-points[1][0])*(points[0][1]-points[2][1]) != (points[0][0]-points[2][0])*(points[0][1]-points[1][1])
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

	result := isBoomerang(points)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", strconv.FormatBool(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
