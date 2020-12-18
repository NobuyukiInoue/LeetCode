package solution

import (
	"fmt"
	"strings"
	"time"
)

func largestRectangleArea(heights []int) int {
	// 12ms
	maxArea := 0
	stack := make([][]int, 0)

	for i := 0; i < len(heights); i++ {
		start := i
		stackLen := len(stack)
		for stackLen > 0 && stack[stackLen-1][1] > heights[i] {
			height := stack[stackLen-1][1]
			width := i - stack[stackLen-1][0]
			maxArea = myMax(maxArea, height*width)
			start = stack[stackLen-1][0]
			stack = stack[:stackLen-1]
			stackLen = len(stack)
		}
		stack = append(stack, []int{start, heights[i]})
	}

	for i := 0; i < len(stack); i++ {
		height := stack[i][1]
		start := stack[i][0]
		area := height*(len(heights) - start)
		maxArea = myMax(area, maxArea)
	}

	return maxArea
}

func myMax(a int, b int) int {
	if a > b {
		return a
	}
	return b
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	flds := strings.Replace(temp, "]", "", -1)

	heights := StringToIntArray(flds)
	fmt.Printf("heights = [%s]\n", IntArrayToString(heights))

	timeStart := time.Now()

	result := largestRectangleArea(heights)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
