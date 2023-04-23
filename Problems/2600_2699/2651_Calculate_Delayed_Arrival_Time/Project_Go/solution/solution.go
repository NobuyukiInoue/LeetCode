package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func findDelayedArrivalTime(arrivalTime int, delayedTime int) int {
	// 0ms
	return (arrivalTime + delayedTime) % 24
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)
	flds := strings.Split(temp, "],[")

	arrivalTime, _ := strconv.Atoi(flds[0])
	delayedTime, _ := strconv.Atoi(flds[1])
	fmt.Printf("arrivalTime = %d, delayedTime = %d\n", arrivalTime, delayedTime)

	timeStart := time.Now()

	result := findDelayedArrivalTime(arrivalTime, delayedTime)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
