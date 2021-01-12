package solution

import (
	"fmt"
	"math"
	"strconv"
	"strings"
	"time"
)

var line1 float64
var line2 float64

func validSquare(p1 []int, p2 []int, p3 []int, p4 []int) bool {
	// 0ms
	line1, line2 = 0.0, 0.0
	return decider(p1, p2) && decider(p1, p3) && decider(p1, p4) && decider(p2, p3) && decider(p2, p4) && decider(p3, p4)
}
    
func decider(x1 []int, x2 []int) bool {  
	dist := math.Sqrt(float64((x2[0] - x1[0])*(x2[0] - x1[0]) + (x2[1] - x1[1])*(x2[1] - x1[1])))
	if dist == 0.0 {
		return false
	} else if line1 == 0.0 {
		line1 = dist
	} else if line2 == 0.0 && dist != line1 {
		line2 = dist
	} else if dist != line1 && dist != line2 {
		return false
	}
	return true
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	flds := strings.Replace(temp, "]]", "", -1)

	points := strings.Split(flds, "],[")
	p1 := StringToIntArray(points[0])
	p2 := StringToIntArray(points[1])
	p3 := StringToIntArray(points[2])
	p4 := StringToIntArray(points[3])
	fmt.Printf("p1 = %s\n", IntArrayToString(p1))
	fmt.Printf("p2 = %s\n", IntArrayToString(p2))
	fmt.Printf("p3 = %s\n", IntArrayToString(p3))
	fmt.Printf("p4 = %s\n", IntArrayToString(p4))

	timeStart := time.Now()

	result := validSquare(p1, p2, p3, p4)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", strconv.FormatBool(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
