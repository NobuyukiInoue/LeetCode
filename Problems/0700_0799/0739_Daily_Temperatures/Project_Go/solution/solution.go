package solution

import (
	"fmt"
	"strings"
	"time"
)

func dailyTemperatures(T []int) []int {
	// 48ms
	stack := make([]int, len(T))
	top := -1
	ret := make([]int, len(T))
	for i := 0; i < len(T); i++ {
		for top > -1 && T[i] > T[stack[top]] {
			idx := stack[top]
			top--
			ret[idx] = i - idx
		}
		top++
		stack[top] = i
	}
	return ret
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	flds := strings.Replace(temp, "]", "", -1)

	T := StringToIntArray(flds)
	fmt.Printf("T = [%s]\n", IntArrayToString(T))

	timeStart := time.Now()

	result := dailyTemperatures(T)

	timeEnd := time.Now()

	fmt.Printf("result = [%s]\n", IntArrayToString(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
