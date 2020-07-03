package solution

import (
	"fmt"
	"strings"
	"time"
)

func maxArea(height []int) int {
	// 12ms
	leftHigh := 0
	rightHigh := len(height) - 1
	maxArea := 0

	for leftHigh < rightHigh {
		if height[leftHigh] < height[rightHigh] {
			curArea := height[leftHigh] *(rightHigh - leftHigh)
			if curArea > maxArea {
				maxArea = curArea
			}
			leftHigh++
		} else {
			curArea := height[rightHigh] *(rightHigh - leftHigh)
			if curArea > maxArea {
				maxArea = curArea
			}
			rightHigh--
		}
	}

	return maxArea
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	flds := strings.Replace(temp, "]", "", -1)

	height := StringToIntArray(flds)
	fmt.Printf("height = [%s]\n", IntArrayToString(height))

	timeStart := time.Now()

	result := maxArea(height)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
