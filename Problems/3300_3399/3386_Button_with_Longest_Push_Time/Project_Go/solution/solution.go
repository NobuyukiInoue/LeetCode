package solution

import (
	"fmt"
	"strings"
	"time"
)

func buttonWithLongestTime(events [][]int) int {
	// 0ms
	ans, p_time := events[0][0], events[0][1]
	mx := p_time
	for _, cur := range events {
		diff := cur[1] - p_time
		if diff > mx {
			mx = diff
			ans = cur[0]
		} else if diff == mx && cur[0] < ans {
			ans = cur[0]
		}
		p_time = cur[1]
	}
	return ans
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)
	flds := strings.Split(temp, "],[")

	events := make([][]int, len(flds))
	for i, _ := range flds {
		events[i] = StringToIntArray(flds[i])
	}

	fmt.Printf("events = %s\n", IntIntArrayToString(events))

	timeStart := time.Now()

	result := buttonWithLongestTime(events)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
