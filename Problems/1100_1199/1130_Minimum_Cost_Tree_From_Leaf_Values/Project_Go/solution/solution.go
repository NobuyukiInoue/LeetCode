package solution

import (
	"fmt"
	"strings"
	"time"
)

func mctFromLeafValues(arr []int) int {
	// 0ms
	stack := make([]int, 0)
	result := 0
	for i, _ := range arr {
		for len(stack) > 0 && stack[len(stack)-1] <= arr[i] {
			temp := stack[len(stack)-1]
			stack = stack[:len(stack)-1]
			if len(stack) == 0 {
				result += temp * arr[i]
			} else {
				result += temp * myMin(stack[len(stack)-1], arr[i])
			}
		}
		stack = append(stack, arr[i])
	}
	for len(stack) > 1 {
		temp := stack[len(stack)-1]
		stack = stack[:len(stack)-1]
		result += temp * stack[len(stack)-1]
	}
	return result
}

func myMin(a int, b int) int {
	if a < b {
		return a
	}
	return b
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "[", "", -1)
	flds := strings.Replace(temp, "]", "", -1)

	arr := StringToIntArray(flds)
	fmt.Printf("arr = %s\n", IntArrayToString(arr))

	timeStart := time.Now()

	result := mctFromLeafValues(arr)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
