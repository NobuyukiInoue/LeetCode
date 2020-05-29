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

func strToIntArray(flds string) []int {
	numsStr := strings.Split(flds, ",")
	nums := make([]int, len(numsStr))

	for i := 0; i < len(nums); i++ {
		nums[i], _ = strconv.Atoi(numsStr[i])
	}

	return nums
}

func intArrayToString(nums []int) string {
	if len(nums) <= 0 {
		return ""
	}

	resultStr := strconv.Itoa(nums[0])
	for i := 1; i < len(nums); i++ {
		resultStr += ", " + strconv.Itoa(nums[i])
	}

	return resultStr
}

func strArrayToString(data []string) string {
	if len(data) <= 0 {
		return ""
	}

	resultStr := data[0]
	for i := 1; i < len(data); i++ {
		resultStr += ", " + data[i]
	}

	return resultStr
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)

	flds := strings.Split(temp, "],[")
	startTime := strToIntArray(flds[0])
	endTime := strToIntArray(flds[1])
	queryTime, _ := strconv.Atoi(flds[2])

	fmt.Printf("startTime = [%s]", intArrayToString(startTime))
	fmt.Printf("endTime   = [%s]", intArrayToString(endTime))
	fmt.Printf("queryTime = %d\n", queryTime)

	timeStart := time.Now()

	result := busyStudent(startTime, endTime, queryTime)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
