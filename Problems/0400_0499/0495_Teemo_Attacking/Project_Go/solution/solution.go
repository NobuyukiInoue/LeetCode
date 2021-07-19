package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func findPoisonedDuration(timeSeries []int, duration int) int {
	// 32ms
	total := duration
	for i := len(timeSeries) - 2; i >= 0; i-- {
		diff := timeSeries[i+1] - timeSeries[i]
		if diff > duration {
			total += duration
		} else {
			total += diff
		}
	}
	return total
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)
	flds := strings.Split(temp, "],[")

	timeSeries := StringToIntArray(flds[0])
	duration, _ := strconv.Atoi(flds[1])
	fmt.Printf("timeSeries = %s\n", IntArrayToString(timeSeries))
	fmt.Printf("duration = %d\n", duration)

	timeStart := time.Now()

	result := findPoisonedDuration(timeSeries, duration)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
