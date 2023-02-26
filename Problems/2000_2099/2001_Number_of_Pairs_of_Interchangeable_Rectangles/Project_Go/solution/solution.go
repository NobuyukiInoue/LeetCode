package solution

import (
	"fmt"
	"strings"
	"time"
)

func interchangeableRectangles(rectangles [][]int) int64 {
	// 278ms - 284ms
	cnts := make(map[float64]int64, 0)
	ans := int64(0)
	for _, rect := range rectangles {
		ratio := float64(rect[0]) / float64(rect[1])
		ans += cnts[ratio]
		cnts[ratio]++
	}
	return ans
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)
	flds := strings.Split(temp, "],[")

	rectangles := make([][]int, len(flds))
	for i, _ := range flds {
		rectangles[i] = StringToIntArray(flds[i])
	}

	fmt.Printf("rectangles = %s\n", IntIntArrayToString(rectangles))

	timeStart := time.Now()

	result := interchangeableRectangles(rectangles)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
