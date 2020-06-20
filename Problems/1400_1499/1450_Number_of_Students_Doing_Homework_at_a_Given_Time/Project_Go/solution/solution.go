package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func busyStudent(startTime []int, endTime []int, queryTime int) int {
	// 0ms
	count := 0
	for i := 0; i < len(startTime); i++ {
		if startTime[i] <= queryTime && queryTime <= endTime[i] {
			count++
		}
	}
	return count
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)

	flds := strings.Split(temp, "],[")
	startTime := StringToIntArray(flds[0])
	endTime := StringToIntArray(flds[1])
	queryTime, _ := strconv.Atoi(flds[2])

	fmt.Printf("startTime = [%s]\n", IntArrayToString(startTime))
	fmt.Printf("endTime   = [%s]\n", IntArrayToString(endTime))
	fmt.Printf("queryTime = %d\n", queryTime)

	timeStart := time.Now()

	result := busyStudent(startTime, endTime, queryTime)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
