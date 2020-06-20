package solution

import (
	"fmt"
	"strings"
	"time"
)

func minCostToMoveChips(chips []int) int {
	// 0ms
	nOdd, nEven := 0, 0
	for _, i := range chips {
		if i%2 == 0 {
			nEven++
		} else {
			nOdd++
		}
	}
	return min(nEven, nOdd)
}

func min(a int, b int) int {
	if a < b {
		return a
	} else {
		return b
	}
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	flds := strings.Replace(temp, "]", "", -1)

	chips := StringToIntArray(flds)
	fmt.Printf("chips = [%s]\n", IntArrayToString(chips))

	timeStart := time.Now()

	result := minCostToMoveChips(chips)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
