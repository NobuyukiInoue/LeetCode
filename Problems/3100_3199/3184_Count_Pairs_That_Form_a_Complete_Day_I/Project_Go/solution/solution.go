package solution

import (
	"fmt"
	"strings"
	"time"
)

func countCompleteDayPairs(hours []int) int {
	// 0ms
	cnt, n := 0, len(hours)
	for i := 0; i < n-1; i++ {
		for j := i + 1; j < n; j++ {
			if (hours[i]+hours[j])%24 == 0 {
				cnt++
			}
		}
	}
	return cnt
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "[", "", -1)
	flds := strings.Replace(temp, "]", "", -1)

	hours := StringToIntArray(flds)
	fmt.Printf("hours = [%s]\n", IntArrayToString(hours))

	timeStart := time.Now()

	result := countCompleteDayPairs(hours)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
