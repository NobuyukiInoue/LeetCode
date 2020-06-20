package solution

import (
	"fmt"
	"sort"
	"strings"
	"time"
)

func heightChecker(heights []int) int {
	sorted := make([]int, len(heights))
	copy(sorted[:], heights)
	sort.Ints(sorted)

	count := 0
	for i, _ := range heights {
		if sorted[i] != heights[i] {
			count++
		}
	}

	return count
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

	result := heightChecker(heights)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
