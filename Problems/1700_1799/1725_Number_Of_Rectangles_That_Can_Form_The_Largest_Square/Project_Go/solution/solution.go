package solution

import (
	"fmt"
	"strings"
	"time"
)

func countGoodRectangles(rectangles [][]int) int {
	// 24ms
	maxLen := 0
	numSquares := 0

	for _, arr := range(rectangles) {
		curLen := myMin(arr[0], arr[1]);

		if curLen == maxLen {
			numSquares++
		} else if curLen > maxLen {
			maxLen = curLen
			numSquares = 1
		} else {
			// do nothing
		}
	}

	return numSquares
}

func myMin(a int, b int) int {
	if a < b {
		return a
	}
	return b
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)
	temp = strings.Replace(temp, ", ", ",", -1)
	flds := strings.Split(temp, "],[")

	rectangles := make([][]int, len(flds))
	for i := 0; i < len(rectangles); i++ {
		rectangles[i] = StringToIntArray(flds[i])
	}
	fmt.Printf("rectangles = %s\n", IntIntArrayToString(rectangles))

	timeStart := time.Now()

	result := countGoodRectangles(rectangles)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
