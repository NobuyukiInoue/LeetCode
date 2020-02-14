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

func str2IntArray(flds string) []int {
	numsStr := strings.Split(flds, ",")
	nums := make([]int, len(numsStr))

	for i := 0; i < len(nums); i++ {
		nums[i], _ = strconv.Atoi(numsStr[i])
	}

	return nums
}

func intArray2string(arr []int) string {
	if len(arr) <= 0 {
		return ""
	}

	resultStr := "["
	for i := 0; i < len(arr); i++ {
		if i > 0 {
			resultStr += ","
		}
		resultStr += strconv.Itoa(arr[i])
	}

	return resultStr + "]"
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)
	flds := strings.Split(temp, "],[")

	distance := str2IntArray(flds[0])

	flds2 := strings.Split(flds[1], ",")
	start, _ := strconv.Atoi(flds2[0])
	destination, _ := strconv.Atoi(flds2[1])

	fmt.Printf("distance = %s, start = %d, destionation = %d\n", intArray2string(distance), start, destination)

	timeStart := time.Now()

	result := distanceBetweenBusStops(distance, start, destination)
	fmt.Printf("result = %d\n", result)

	timeEnd := time.Now()

	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
