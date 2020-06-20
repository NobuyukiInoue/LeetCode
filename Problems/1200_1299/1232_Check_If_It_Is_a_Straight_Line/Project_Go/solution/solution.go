package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func checkStraightLine(coordinates [][]int) bool {
	// 4ms
	dx := (float64)(coordinates[1][0] - coordinates[0][0])
	if dx == 0.0 {
		return false
	}
	inclination := (float64)(coordinates[1][1]-coordinates[0][1]) / dx
	for i := 1; i < len(coordinates)-1; i++ {
		dx = (float64)(coordinates[i+1][0] - coordinates[i][0])
		if dx == 0 {
			return false
		}
		if (float64)(coordinates[i+1][1]-coordinates[i][1])/dx != inclination {
			return false
		}
	}
	return true
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)
	flds := strings.Split(temp, "],[")

	coordinates := make([][]int, len(flds))
	for i := 0; i < len(flds); i++ {
		coordinates[i] = StringToIntArray(flds[i])
	}
	fmt.Printf("coordinates = %s\n", IntIntArrayToString(coordinates))

	timeStart := time.Now()

	result := checkStraightLine(coordinates)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", strconv.FormatBool(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
