package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func distanceBetweenBusStops(distance []int, start int, destination int) int {
	// 0ms
	if start == destination {
		return 0
	}

	r, l := 0, 0
	var p1, p2 int

	if destination > start {
		p1 = start
		p2 = destination
	} else {
		p1 = destination
		p2 = start
	}

	for i := p1; i < p2; i++ {
		r += distance[i]
	}
	for i := p2; i < len(distance); i++ {
		l += distance[i]
	}
	for i := 0; i < p1; i++ {
		l += distance[i]
	}

	if l < r {
		return l
	} else {
		return r
	}
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)
	flds := strings.Split(temp, "],[")

	distance := StringToIntArray(flds[0])

	flds2 := strings.Split(flds[1], ",")
	start, _ := strconv.Atoi(flds2[0])
	destination, _ := strconv.Atoi(flds2[1])
	fmt.Printf("distance = [%s], start = %d, destionation = %d\n", IntArrayToString(distance), start, destination)

	timeStart := time.Now()

	result := distanceBetweenBusStops(distance, start, destination)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
