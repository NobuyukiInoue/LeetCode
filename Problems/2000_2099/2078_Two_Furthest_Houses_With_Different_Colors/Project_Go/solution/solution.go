package solution

import (
	"fmt"
	"strings"
	"time"
)

func maxDistance(colors []int) int {
	// 0ms
	res, colorsLen := 0, len(colors)
	for i, x := range colors {
		if x != colors[0] {
			res = myMax(res, i)
		}
		if x != colors[colorsLen-1] {
			res = myMax(res, colorsLen-1-i)
		}
	}
	return res
}

func myMax(a int, b int) int {
	if a > b {
		return a
	}
	return b
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "[", "", -1)
	flds := strings.Replace(temp, "]", "", -1)

	colors := StringToIntArray(flds)
	fmt.Printf("colors = [%s]\n", IntArrayToString(colors))

	timeStart := time.Now()

	result := maxDistance(colors)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
