package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func isCovered(ranges [][]int, left int, right int) bool {
	// 0ms
	for i := left; i <= right; i++ {
		result := false
		for _, work := range ranges {
			if work[0] <= i && i <= work[1] {
				result = true
				break
			}
		}
		if !result {
			return false
		}
	}
	return true
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[[[", "", -1)
	flds := strings.Split(temp, "]],[")

	matrixStr := strings.Split(flds[0], "],[")
	ranges := make([][]int, len(matrixStr))
	for i := 0; i < len(matrixStr); i++ {
		ranges[i] = StringToIntArray(matrixStr[i])
	}
	fmt.Printf("ranges = %s\n", IntIntArrayToGridString(ranges))
	flds2 := strings.Split(strings.Replace(flds[1], "]]", "", -1), ",")
	left, _ := strconv.Atoi(flds2[0])
	right, _ := strconv.Atoi(flds2[1])
	fmt.Printf("left = %d, right = %d\n", left, right)

	timeStart := time.Now()

	result := isCovered(ranges, left, right)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", strconv.FormatBool(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
